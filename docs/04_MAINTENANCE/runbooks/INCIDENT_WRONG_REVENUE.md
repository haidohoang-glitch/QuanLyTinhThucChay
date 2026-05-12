# INCIDENT: Doanh Số Thực Chạy Tính Sai

> **Loại sự cố:** Wrong Revenue Calculation
> **Mức độ:** 🔴 P1 — Ảnh hưởng trực tiếp đến báo cáo tài chính
> **Skill:** `incident-response-playbook` | **Phiên bản:** v1.0 | **Ngày:** 2026-05-12

---

## 1. Triệu chứng nhận biết

- Đội Kiểm soát báo: doanh số hợp đồng X / nhóm SP Y cao/thấp bất thường
- Doanh số lệch so với báo cáo vận hành gốc (RecurringJob / Google / Facebook)
- Tổng doanh số vượt giá trị phân bổ hợp đồng (không được phép — vi phạm BR-C-01)
- Doanh số âm (vi phạm INV-01)
- BI/IBiz báo cáo số liệu bất thường sau khi chốt sang Release

---

## 2. Nguyên nhân thường gặp

| # | Nguyên nhân | Tần suất | Phân loại |
|---|------------|---------|----------|
| N1 | Dữ liệu thực treo/view/click lỗi từ nguồn | Trung bình | Lỗi dữ liệu nguồn |
| N2 | SP logic thay đổi gần đây làm sai công thức | Thấp | Lỗi code |
| N3 | Cơ chế anti-overcap không hoạt động đúng | Thấp | Lỗi code |
| N4 | Offset/Đối trừ tính sai sau thay đổi HĐ/HĐCT | Trung bình | Lỗi logic offset |
| N5 | Phân bổ gán nhầm DmSanPhamID / DmHinhThucID | Thấp | Lỗi cấu hình |
| N6 | Job tính trùng do chạy lại thủ công | Rất thấp | Lỗi orchestration |

---

## 3. Quy trình xử lý

### Bước 1: Thu thập thông tin (5 phút)

Cần lấy đủ từ người báo lỗi:
- [ ] Mã hợp đồng (SoHopDong) hoặc HopDongChiTietREF cụ thể
- [ ] Ngày/kỳ bị sai (NgayThucHien)
- [ ] Giá trị hiện tại là bao nhiêu?
- [ ] Giá trị kỳ vọng là bao nhiêu? Dựa trên nguồn nào?
- [ ] Nhóm sản phẩm bị ảnh hưởng (CPD / PR / CPM / Mobile / GGFB / ...)

### Bước 2: Xem dữ liệu thực chạy đã tính (10 phút)

```sql
-- Xem thực chạy đã tính cho HDCT
SELECT ID, NgayThucHien, ThanhTienThucChay, SoLuongThucChay,
       GiaTriThayDoi, SoLuongThayDoi, LoaiXuLy, GhiChu
FROM ThucChayDaTinh
WHERE HopDongChiTietREF = [HDCT_REF]
ORDER BY NgayThucHien, ID;

-- Kiểm tra tổng vs phân bổ
SELECT hdct.GiaTriPhanBo,
       SUM(tcdt.ThanhTienThucChay) AS TongDaTinh,
       SUM(tcdt.GiaTriThayDoi)     AS TongThayDoi,
       SUM(tcdt.ThanhTienThucChay) + SUM(tcdt.GiaTriThayDoi) AS TongThucTe
FROM HopDongChiTiet hdct
JOIN ThucChayDaTinh tcdt ON hdct.ID = tcdt.HopDongChiTietREF
WHERE hdct.ID = [HDCT_REF]
GROUP BY hdct.GiaTriPhanBo;
```

**Bảng tra công thức kỳ vọng theo nhóm SP:**

| Nhóm SP | Công thức tính mới | Tài liệu gốc |
|---------|-------------------|-------------|
| CPD đợt chạy | `SL × DG / SoNgayDotChay × (1-CK%)` | Logic_nghiepvu STT 1.0 |
| CPD không đợt | `SL × DG / TongSoNgayTreo × (1-CK%)` | Logic_nghiepvu STT 1.0 |
| PR | `SLTreo × GiaTienTreo × (1-CKTreo%)` | Logic_nghiepvu STT 2.0 |
| Chi phí | `SLTreo × DonGiaTreo × (1-CK%)`, cap ≤ GiaTriPhanBo | Logic_nghiepvu STT 4.0 |
| CPM thuần | `SoLuong × DonGia × (1-CK%)` | Logic_nghiepvu STT 8.0 |
| Mobile | CTE Recursive, cap theo LoaiXuLy | Logic_nghiepvu STT 9.0 |
| Admatic | `ThanhTienThucChaySauCK × TiLeHDCT/100`, cap | Logic_nghiepvu STT 6.0 |

### Bước 3: Phân loại — Dữ liệu nguồn hay Code? (15 phút)

```sql
-- Kiểm tra dữ liệu nguồn (thực treo)
SELECT tc.NgayThucHien, tc.SoLuongThucTreo, tc.DonGiaThucTreo,
       tchdct.HopDongChiTietREF
FROM ThucChay tc
JOIN ThucChayHopDongChiTiet tchdct ON tc.ID = tchdct.ThucChayREF
WHERE tchdct.HopDongChiTietREF = [HDCT_REF]
AND CAST(tc.NgayThucHien AS DATE) = '[NGAY_SAI]';
```

- Dữ liệu nguồn **SAI** → N1 — fix từ nguồn
- Dữ liệu nguồn **ĐÚNG**, kết quả tính sai → N2/N3/N4 — lỗi code/logic

### Bước 4: Fix theo tình huống

**TH1: Sai do dữ liệu nguồn (N1)**
1. Yêu cầu team nguồn fix và re-push dữ liệu
2. Sau khi dữ liệu nguồn đúng, chạy lại:
```sql
-- Tính lại thực chạy cho 1 hợp đồng
EXEC job_ThucChayDaTinh_ReInsertByHopDong @HopDongREF = [HOPDONG_ID];
```

**TH2: Sai do offset (N4)**
```sql
-- Xem lịch sử thay đổi HĐ
SELECT * FROM HopDongThayDoi
WHERE HopDongREF = [HD_ID]
ORDER BY NgayThayDoi DESC;
```
Tính tay GiaTriThayDoi kỳ vọng = Mới - Cũ → so sánh với ThucChayDaTinh.GiaTriThayDoi

**TH3: Sai do bug SP (N2/N3)**
→ Escalate Developer ngay, không tự sửa SP production.

### Bước 5: Verify sau fix

```sql
SELECT hdct.GiaTriPhanBo,
       SUM(tcdt.ThanhTienThucChay) + SUM(tcdt.GiaTriThayDoi) AS TongThucTe,
       CASE WHEN SUM(tcdt.ThanhTienThucChay) + SUM(tcdt.GiaTriThayDoi) > hdct.GiaTriPhanBo
            THEN '⚠️ VƯỢT PHÂN BỔ' ELSE '✅ OK' END AS TrangThai
FROM HopDongChiTiet hdct
JOIN ThucChayDaTinh tcdt ON hdct.ID = tcdt.HopDongChiTietREF
WHERE hdct.ID = [HDCT_REF]
GROUP BY hdct.GiaTriPhanBo;
```

---

## 4. Escalation

| Khi nào | Đến ai | SLA |
|---------|--------|-----|
| Không xác định nguồn gốc trong 30 phút | Developer (T3) | Ngay |
| Bug SP rõ ràng | Developer | Trong ngày |
| Sai lệch > 10% tổng doanh số ngày | Developer + Tech Lead + BA | Ngay |
| Dữ liệu đã chốt sang Release | Developer + BA + Manager | Ngay |

---

## 5. Phòng tránh

| Biện pháp | Trạng thái |
|----------|-----------|
| Job `KiemSoat_ThucChayDaTinh` chạy hàng ngày | ✅ Đã có |
| `KiemSoat_DataThucChay_ThayDoi_KhiTinhThucChay` | ✅ Đã có |
| Alert khi doanh số ngày lệch > 15% so với hôm trước | 🔴 Chưa có (WP-C02) |
