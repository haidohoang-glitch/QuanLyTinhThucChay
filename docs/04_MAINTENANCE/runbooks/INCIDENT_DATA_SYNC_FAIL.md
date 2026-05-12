# INCIDENT: Đồng Bộ Dữ Liệu Thất Bại

> **Loại sự cố:** Data Sync Failure (RecurringJob / Sync Jobs)
> **Mức độ:** 🟠 P2 — Không có dữ liệu đầu vào → Job tính bị delay
> **Skill:** `incident-response-playbook` | **Phiên bản:** v1.0 | **Ngày:** 2026-05-12

---

## 1. Triệu chứng nhận biết

- Các bảng staging trống hoặc chỉ có dữ liệu cũ (không có ngày hôm nay)
- Job tính thực chạy (B3) chạy xong nhưng không có bản ghi mới trong `ThucChayDaTinh`
- Email cảnh báo từ Job `Job_GetInforThucTreo_ThucChayMuaNgoai_GGFB_FromHDCN` fail
- `ThucChayHopDongChiTiet` không có dữ liệu mới sau 07:30 AM

---

## 2. Nguyên nhân thường gặp

| # | Nguyên nhân | Tần suất | Phạm vi |
|---|------------|---------|---------|
| N1 | RecurringJob (external) không chạy / chạy lỗi | Trung bình | Tất cả nhóm dùng RecurringJob |
| N2 | Kết nối network đến server thực treo bị lỗi | Thấp | `Job_GetInforThucTreo_*` |
| N3 | Google / Facebook API rate limit hoặc timeout | Thấp | GGFB jobs |
| N4 | Sync Job fail do dữ liệu nguồn có cấu trúc thay đổi | Rất thấp | Tất cả Sync Jobs |
| N5 | SQL Server Agent service bị dừng | Rất thấp | Toàn bộ pipeline |

---

## 3. Quy trình xử lý

### Bước 1: Xác nhận staging trống (5 phút)

```sql
-- Kiểm tra dữ liệu thực treo có về hôm nay chưa
SELECT CAST(NgayThucHien AS DATE) AS Ngay,
       COUNT(*) AS SoBanGhi,
       MAX(NgayThucHien) AS MoiNhat
FROM ThucChayHopDongChiTiet
WHERE CAST(NgayThucHien AS DATE) >= CAST(GETDATE()-1 AS DATE)
GROUP BY CAST(NgayThucHien AS DATE)
ORDER BY Ngay DESC;

-- Kiểm tra GGFB data
SELECT TOP 10 * FROM [OperatingResult_GGFB]  -- hoặc tên bảng GGFB tương ứng
ORDER BY ID DESC;
```

### Bước 2: Xác định nguồn bị lỗi (10 phút)

**Kiểm tra trạng thái Sync Jobs:**

```sql
SELECT j.name, h.run_date, h.run_time,
       CASE h.run_status WHEN 0 THEN '❌ FAILED' WHEN 1 THEN '✅ OK' END AS Status,
       h.message
FROM msdb.dbo.sysjobs j
JOIN msdb.dbo.sysjobhistory h ON j.job_id = h.job_id
WHERE j.name IN (
    'Job_GetInfo_ThucChay_GGFB',
    'Job_GetInforThucTreo_PR',
    'Job_GetInforThucTreo_ThucChayMuaNgoai_GGFB_FromHDCN'
)
AND h.run_date = CONVERT(INT, CONVERT(VARCHAR, GETDATE(), 112))
AND h.step_id = 0
ORDER BY h.run_date DESC;
```

**Phân loại theo nguồn:**

| Nguồn bị thiếu | Nhóm SP bị ảnh hưởng | Job cần kiểm tra |
|---------------|---------------------|-----------------|
| ThucChayHopDongChiTiet (thực treo) | CPD, PR, CPM, Chi phí, Mobile | `Job_GetInforThucTreo_ThucChayMuaNgoai_GGFB_FromHDCN` |
| GGFB Operating data | GGFB (thực tế + sản lượng) | `Job_GetInfo_ThucChay_GGFB` |
| Thực treo PR | PR | `Job_GetInforThucTreo_PR` |
| Dữ liệu Admatic | Admatic | RecurringJob (external) |

### Bước 3: Xử lý theo loại lỗi

**TH1: RecurringJob external chưa chạy (N1)**
```
1. Kiểm tra RecurringJob system (ngoài phạm vi SQL Agent)
2. Liên hệ team vận hành RecurringJob
3. Sau khi RecurringJob chạy xong:
   → Chạy lại Sync Jobs thủ công theo thứ tự
   → Sau đó chạy lại Job tính thực chạy
```

**TH2: Sync Job fail do network (N2)**
```
1. Verify kết nối network đến server thực treo:
   → Ping server thuctreo
   → Thử query linked server
2. Nếu network OK → thử chạy lại Sync Job thủ công
3. Nếu network lỗi → escalate team infra
```

**TH3: Google/Facebook API lỗi (N3)**
```
1. Kiểm tra error message trong Job_GetInfo_ThucChay_GGFB
2. Thường là rate limit → đợi 1-2 giờ và chạy lại
3. Nếu lỗi kéo dài → liên hệ team quản lý API credentials
```

### Bước 4: Chạy lại theo thứ tự (B1 → B2 → B3)

```
Thứ tự bắt buộc khi chạy lại thủ công:
1. Chạy RecurringJob (external) hoặc chờ nó tự chạy lại
2. Chạy các Sync Jobs (B2):
   - Job_GetInforThucTreo_ThucChayMuaNgoai_GGFB_FromHDCN
   - Job_GetInfo_ThucChay_GGFB
   - Job_GetInforThucTreo_PR (nếu cần)
3. Sau khi B2 xong, chạy các Job tính (B3):
   - ThucChay_CPD_Chiphi_PR
   - ThucChay_Admarket_PBdieuchinh_CPMngay_Mobile_Inventory_CPM_Admatic
   - ThucChay_GoogleFacebook_MktFee
   - ThucChay_MuaNgoai
```

### Bước 5: Verify

```sql
-- Xác nhận dữ liệu đã về đầy đủ sau sync
SELECT CAST(NgayThucHien AS DATE) AS Ngay, COUNT(*) AS SoBanGhi
FROM ThucChayHopDongChiTiet
WHERE CAST(NgayThucHien AS DATE) = CAST(GETDATE() AS DATE)
GROUP BY CAST(NgayThucHien AS DATE);

-- Xác nhận thực chạy đã được tính
SELECT COUNT(*) AS SoBanGhiMoi
FROM ThucChayDaTinh
WHERE CAST(NgayThucHien AS DATE) = CAST(GETDATE() AS DATE);
```

---

## 4. Escalation

| Khi nào | Đến ai | SLA |
|---------|--------|-----|
| RecurringJob lỗi, không tự fix được | Team RecurringJob | Trong 1 giờ |
| Network đến server thực treo lỗi | Team Infra | Trong 30 phút |
| API Google/Facebook lỗi > 4 giờ | Tech Lead + Manager | Trong 2 giờ |
| Sync Job fail do schema thay đổi | Developer | Trong ngày |

---

## 5. Phòng tránh

| Biện pháp | Trạng thái |
|----------|-----------|
| Email alert khi Sync Job fail (step Canh_Bao) | ✅ Đã có |
| Alert khi staging trống sau 07:30 AM | 🔴 Chưa có (WP-C04) |
| Monitor thời gian hoàn thành Sync Jobs | 🔴 Chưa có (WP-C01) |
