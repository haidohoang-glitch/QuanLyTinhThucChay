# INCIDENT: Job Tính Thực Chạy Bị Fail

> **Loại sự cố:** SQL Agent Job Failure
> **Mức độ:** 🔴 P1 — Ảnh hưởng dữ liệu thực chạy hàng ngày
> **Skill:** `incident-response-playbook` | **Phiên bản:** v1.0 | **Ngày:** 2026-05-12

---

## 1. Triệu chứng nhận biết

- Email cảnh báo tự động từ step `Canh_Bao_job_chay_FAILURE` với subject: `[Canh bao job loi] [TênJob]`
- SQL Server Agent hiển thị Job status: ❌ Failed
- Dữ liệu trong `ThucChayDaTinh` thiếu bản ghi của ngày hiện tại (sau 08:30 AM)
- Đội Kiểm soát báo không thấy dữ liệu mới trên hệ thống

---

## 2. Nguyên nhân thường gặp

| # | Nguyên nhân | Tần suất | Nhận biết |
|---|------------|---------|----------|
| N1 | RecurringJob chưa lấy dữ liệu xong (B1 chưa hoàn thành) | Cao | Step 1 fail, staging table trống |
| N2 | Dữ liệu staging có giá trị NULL/bất thường làm SP crash | Trung bình | Error message trong Job history |
| N3 | Deadlock giữa các Jobs chạy song song | Thấp | Error 1205 trong SQL log |
| N4 | Server memory/disk không đủ | Thấp | SQL Server error log |
| N5 | SP có bug logic mới được deploy | Thấp | Job fail sau ngày deploy mới |
| N6 | CDC cleanup job xóa data cần thiết | Rất thấp | Mất dữ liệu change tracking |

---

## 3. Quy trình xử lý

### Bước 1: Xác nhận sự cố (5 phút)

```sql
-- Kiểm tra trạng thái các Jobs tính thực chạy hôm nay
SELECT 
    j.name AS JobName,
    h.run_date,
    h.run_time,
    CASE h.run_status 
        WHEN 0 THEN '❌ FAILED'
        WHEN 1 THEN '✅ SUCCEEDED'
        WHEN 4 THEN '⏳ RUNNING'
    END AS Status,
    h.message
FROM msdb.dbo.sysjobs j
JOIN msdb.dbo.sysjobhistory h ON j.job_id = h.job_id
WHERE j.name IN (
    'ThucChay_CPD_Chiphi_PR',
    'ThucChay_Admarket_PBdieuchinh_CPMngay_Mobile_Inventory_CPM_Admatic',
    'ThucChay_GoogleFacebook_MktFee',
    'ThucChay_MuaNgoai'
)
AND h.run_date = CONVERT(INT, CONVERT(VARCHAR, GETDATE(), 112))
AND h.step_id = 0  -- summary row
ORDER BY h.run_date DESC, h.run_time DESC;
```

### Bước 2: Triage — Xác định Step bị fail (10 phút)

```sql
-- Xem chi tiết từng step của Job bị fail
SELECT 
    step_id,
    step_name,
    CASE run_status 
        WHEN 0 THEN '❌ FAILED'
        WHEN 1 THEN '✅ OK'
        WHEN 2 THEN '⏭ RETRIED'
        WHEN 3 THEN '⏹ CANCELLED'
    END AS Status,
    run_duration,
    message
FROM msdb.dbo.sysjobhistory
WHERE job_id = (SELECT job_id FROM msdb.dbo.sysjobs WHERE name = N'[TÊN_JOB_FAIL]')
AND run_date = CONVERT(INT, CONVERT(VARCHAR, GETDATE(), 112))
ORDER BY step_id;
```

**Phân loại theo Step fail:**

| Step fail | Chẩn đoán | Action |
|-----------|----------|--------|
| Step 1 (Sync data) | Dữ liệu nguồn chưa sẵn sàng | Đợi RecurringJob hoàn thành, chạy lại |
| Step 2+ (Calc) | Lỗi logic SP tính toán | Xem error message → Bước 3 |
| Step cuối (Canh_Bao) | Job trước fail nhưng alert fail luôn | Fix step trước đó |

### Bước 3: Phân tích lỗi SP (15 phút)

```sql
-- Kiểm tra dữ liệu staging có vấn đề không
-- Ví dụ cho nhóm CPD:
SELECT COUNT(*) AS SoLuongTreo, 
       MIN(NgayThucHien) AS NgaySom, 
       MAX(NgayThucHien) AS NgayMuon
FROM ThucChayHopDongChiTiet
WHERE CAST(NgayThucHien AS DATE) = CAST(GETDATE() AS DATE);

-- Kiểm tra NULL bất thường
SELECT TOP 100 *
FROM ThucChayHopDongChiTiet
WHERE CAST(NgayThucHien AS DATE) = CAST(GETDATE() AS DATE)
AND (SoLuongThucTreo IS NULL OR DonGiaThucTreo IS NULL);
```

### Bước 4: Xử lý theo tình huống

**TH1: Dữ liệu nguồn chưa sẵn sàng (N1)**
```
1. Verify: RecurringJob đã chạy xong chưa?
2. Nếu chưa: Đợi RecurringJob xong rồi chạy lại Job tính
3. Nếu RecurringJob cũng lỗi: → Escalate tới team RecurringJob
4. Chạy lại Job thủ công:
   SQL Server Agent → Jobs → [TênJob] → Right-click → Start Job at Step
```

**TH2: Lỗi NULL/data bất thường (N2)**
```
1. Xác định bản ghi gây lỗi từ error message
2. Kiểm tra dữ liệu nguồn tương ứng
3. Options:
   a. Xóa bản ghi NULL tạm thời → chạy lại Job → tìm nguyên nhân sau
   b. Escalate developer nếu không rõ nguyên nhân
```

**TH3: Deadlock (N3)**
```
1. Kiểm tra: SELECT * FROM sys.dm_exec_requests (thời điểm xảy ra)
2. Chạy lại Job — deadlock thường tự giải quyết
3. Nếu lặp lại: Escalate Developer xem xét Job schedule
```

### Bước 5: Chạy lại Job an toàn

```sql
-- Kiểm tra xem đã có dữ liệu hôm nay trong ThucChayDaTinh chưa
SELECT 
    DmSanPhamREF,
    COUNT(*) AS SoBanGhi,
    SUM(ThanhTienThucChay) AS TongDoanhSo
FROM ThucChayDaTinh
WHERE CAST(NgayThucHien AS DATE) = CAST(GETDATE() AS DATE)
GROUP BY DmSanPhamREF
ORDER BY DmSanPhamREF;
```

> ⚠️ **Cảnh báo:** Nếu đã có dữ liệu một phần trong `ThucChayDaTinh`, kiểm tra SP có check idempotent không trước khi chạy lại (tránh tính trùng).

### Bước 6: Verify sau khi fix (5 phút)

```sql
-- Verify: Dữ liệu đã đầy đủ sau khi chạy lại
SELECT 
    CAST(NgayThucHien AS DATE) AS Ngay,
    COUNT(DISTINCT DmSanPhamREF) AS SoNhomSP,
    COUNT(*) AS SoBanGhi,
    SUM(ThanhTienThucChay) AS TongDoanhSo
FROM ThucChayDaTinh
WHERE CAST(NgayThucHien AS DATE) = CAST(GETDATE() AS DATE)
GROUP BY CAST(NgayThucHien AS DATE);
```

---

## 4. Escalation

| Khi nào escalate | Đến ai | SLA |
|-----------------|--------|-----|
| Không xác định được nguyên nhân trong 30 phút | Developer on-call | Ngay lập tức |
| Lỗi lặp lại nhiều ngày liên tiếp | Developer + Tech Lead | Trong ngày |
| RecurringJob fail (ngoài phạm vi DB) | Team RecurringJob | Trong 1 giờ |
| Nghi ngờ data corruption | Developer + DBA | Ngay lập tức |

---

## 5. Post-incident

Sau khi giải quyết xong, ghi log sự cố vào `DOC_SYNC_REPORT.md` (phần Incident Log):

```
Ngày: [DATE]
Job fail: [JOB_NAME] - Step [N]
Nguyên nhân: [ROOT_CAUSE]
Thời gian triage: [X] phút
Action: [MÔ TẢ]
Prevention: [GHI CHÚ PHÒNG TRÁNH]
```
