# SKILL: CPD Troubleshooting — Điều tra Sai Lệch Ngày Tính Thực Chạy

> **Skill ID:** `cpd-troubleshooting-day-mismatch`  
> **Nhóm sản phẩm:** CPD đợt chạy (Loại A)  
> **File dự án:** [SKILL_CPD_Troubleshooting.md](file:///d:/QuanLyTinhThucChay/QuanLyTinhThucChay/docs/03_EXECUTION/SKILL_CPD_Troubleshooting.md)

---

## USE CASE 1: THIẾU NGÀY TÍNH THỰC CHẠY (Lệch ID, Ngoài cửa sổ...)

```
SHĐ: QC0020326   |   Phân bổ (HopDongChiTietID): 778668
Booking treo: 10056547

Vấn đề:
  - Tổng đợt chạy đánh số: 5 ngày
  - Tổng treo thực tế:      5 ngày
  - Hệ thống chỉ tính:      3 ngày  ← thiếu 2 ngày
  - Booking 10056547:        treo 2 ngày nhưng bị bỏ qua hoàn toàn
  - Chạy lại job:            vẫn không fix được
```

---

## 6 NGUYÊN NHÂN GỐC RỄ

| # | Nguyên nhân | Dấu hiệu nhận biết |
|---|---|---|
| 🔴 1 | **Ngày treo nằm ngoài cửa sổ đợt chạy** | `NgayTreo` của booking 10056547 < `ThoiGianBatDau` hoặc > `ThoiGianKetThuc` trong `DotChayHopDongChiTiet` |
| 🔴 2 | **Booking bị xóa hoặc chưa duyệt** | `DeletedStatus = 1` hoặc `TrangThaiDuyet ≠ giá trị hợp lệ` trong `ThucChayHopDongChiTiet` |
| 🔴 3 | **Kỳ kế toán đã khóa** | Chạy lại job nhiều lần vẫn không thay đổi kết quả — 2 ngày thuộc tháng đã chốt số |
| 🔴 4 | **Race condition: Sync chưa xong khi Calc chạy** | Booking 10056547 được tạo/cập nhật sau 7h sáng (sau Job Sync đã hoàn thành) |
| 🔴 5 | **Số ngày đợt chạy trên đánh số sai** | `SoNgayDotChay` = 3 thay vì 5 → chia mẫu số sai → bị bỏ bớt ngày |
| ⭐ 6 | **Lệch BookingREF giữa bảng Đánh số và Thực treo** | Tổng treo đủ, đợt chạy đủ, nhưng thiếu ngày cụ thể. Job tính JOIN theo cả `HopDongChiTietREF` và `BookingREF` nhưng 2 bảng lại khác `BookingREF`. |

---

## NGUYÊN NHÂN THỰC TẾ ĐÃ XÁC NHẬN — Nguyên nhân 6 ⭐

**Vấn đề cốt lõi:** Job tính CPD JOIN bảng `DotChayHopDongChiTiet` với `ThucChayHopDongChiTiet` theo **2 điều kiện đồng thời**:

```sql
ON dc.HopDongChiTietREF = tc.HopDongChiTietREF  -- ✅ khớp
AND dc.BookingREF        = tc.BookingREF          -- ❌ KHÔNG khớp → bỏ qua ngày treo
```

Kết quả: Các ngày treo có `BookingREF` khớp → tính được. Booking có `BookingREF` khác (do tạo lại ID mới, remap, hoặc lỗi sync) → bị bỏ qua hoàn toàn dù đúng ID phân bổ.

### Hướng Fix:

| Tình huống | Hành động |
|---|---|
| HDCN tạo lại booking (ID mới), đánh số giữ ID cũ | Sửa `BookingREF` trong `DotChayHopDongChiTiet` |
| Sync ghi sai `BookingREF` vào thực treo | Sửa `BookingREF` trong `ThucChayHopDongChiTiet` |
| Phân bổ remap nhưng đánh số chưa cập nhật | Sửa `BookingREF` trong `DotChayHopDongChiTiet` |

> ⚠️ **Sau khi sửa:** Bắt buộc chạy lại Job tính thực chạy chính (`Job_TinhThucChay_CPD` hoặc gọi thủ công `[dbo].[ThucChay_CPD_Job]`) để hệ thống tính bổ sung các ngày còn thiếu. (Lưu ý: Tuyệt đối KHÔNG dùng job `job_ThucChayDaTinh_ReInsertByHopDong` vì job đó chỉ dùng để xử lý khi có thay đổi thuộc tính đánh số như SoHopDong, KhachHang, SanPham...).

---

## CHECKLIST NHANH (7 điểm)

```
□ 1. Phân bổ 778668 tồn tại và chưa xóa?
       SELECT * FROM HopDongChiTiet WHERE ID = 778668 AND DeletedStatus = 0

□ 2. Đợt chạy bao phủ đủ 5 ngày?
       SELECT ThoiGianBatDau, ThoiGianKetThuc, SoNgayDotChay
       FROM DotChayHopDongChiTiet
       WHERE HopDongChiTietREF = 778668 AND DeletedStatus = 0

□ 3. Tổng treo hợp lệ là bao nhiêu?
       SELECT COUNT(DISTINCT NgayTreo) FROM ThucChayHopDongChiTiet
       WHERE HopDongChiTietREF = 778668
         AND DeletedStatus = 0 AND TrangThaiDuyet = [giá trị hợp lệ]

□ 4. Booking 10056547 trạng thái ra sao?
       SELECT ID, NgayTreo, TrangThaiDuyet, DeletedStatus
       FROM ThucChayHopDongChiTiet WHERE ID = 10056547

□ 5. 2 ngày treo của 10056547 có nằm trong cửa sổ đợt chạy không?
       → Chạy QUERY CHẨN ĐOÁN bên dưới

□ 6. 2 bảng có bị lệch BookingREF không?
       → Chạy QUERY CHẨN ĐOÁN bên dưới (để ý cột BookingREF)

□ 7. Hệ thống đã tính bao nhiêu bản ghi?
       SELECT NgayTinhThucChay, ThanhTienThucChay, SoLuongThucChay
       FROM ThucChayDaTinh WHERE HopDongChiTietREF = 778668
       ORDER BY NgayTinhThucChay

□ 8. Kỳ của 2 ngày thiếu có bị khóa không?
       → Kiểm tra CauHinhKyKeToan / bảng cấu hình kỳ
```

---

## QUERY CHẨN ĐOÁN QUAN TRỌNG NHẤT

```sql
-- Đối chiếu ngày treo với cửa sổ đợt chạy & kiểm tra BookingREF
SELECT
    tc.ID              AS BookingID,
    tc.BookingREF      AS Treo_BookingREF,
    tc.NgayTreo,
    tc.SoLuongTreo,
    tc.TrangThaiDuyet,
    tc.DeletedStatus,
    dc.BookingREF      AS DanhSo_BookingREF,
    dc.ThoiGianBatDau  AS DotChay_BatDau,
    dc.ThoiGianKetThuc AS DotChay_KetThuc,
    dc.SoNgayDotChay,
    CASE
        WHEN tc.DeletedStatus = 1
            THEN '❌ ĐÃ XÓA — bị bỏ qua'
        WHEN tc.NgayTreo NOT BETWEEN dc.ThoiGianBatDau AND dc.ThoiGianKetThuc
            THEN '❌ NGOÀI CỬA SỔ ĐỢT CHẠY — bị bỏ qua'
        WHEN tc.TrangThaiDuyet <> 1 
            THEN '⚠️ CHƯA DUYỆT — bị bỏ qua'
        WHEN tc.BookingREF IS NOT NULL AND dc.BookingREF IS NOT NULL AND tc.BookingREF <> dc.BookingREF
            THEN '❌ LỆCH BookingREF — ngày này KHÔNG được tính'
        ELSE '✅ HỢP LỆ — sẽ được tính'
    END AS PhanTich
FROM ThucChayHopDongChiTiet tc
LEFT JOIN (
    SELECT TOP 1 BookingREF, ThoiGianBatDau, ThoiGianKetThuc, SoNgayDotChay
    FROM DotChayHopDongChiTiet
    WHERE HopDongChiTietREF = 778668 AND DeletedStatus = 0
    ORDER BY ThoiGianBatDau
) dc ON 1=1
WHERE tc.HopDongChiTietREF = 778668
ORDER BY tc.NgayTreo;
```

---

## MA TRẬN QUYẾT ĐỊNH

| Kết quả kiểm tra | Nguyên nhân | Hành động |
|---|---|---|
| `NgayTreo` nằm ngoài `ThoiGianBatDau–KetThuc` | Cửa sổ đợt chạy hẹp | Mở rộng `ThoiGianKetThuc` trong `DotChayHopDongChiTiet`, chạy lại job |
| `DeletedStatus = 1` trên booking | Booking bị xóa | Khôi phục booking trong HDCN/tool đánh số |
| `TrangThaiDuyet` chưa hợp lệ | Chưa duyệt | Duyệt trong HDCN → Job Sync → Job Calc |
| 2 ngày thuộc kỳ đã chốt số | Kỳ khóa | Mở khóa kỳ hoặc ghi bút toán điều chỉnh kỳ hiện tại |
| `SoNgayDotChay` = 3 thay vì 5 | Số ngày đánh số sai | Sửa `SoNgayDotChay` = 5, chạy lại job đối trừ |
| Booking tạo sau 7h sáng | Race condition | Chạy lại Job Sync thủ công → Job Calc |
| `BookingREF` trên 2 bảng không khớp | Lệch ID do tạo lại/remap | Sửa lại `BookingREF` cho khớp giữa `ThucChayHopDongChiTiet` và `DotChayHopDongChiTiet` → Chạy lại Job tính thực chạy CPD chính |

---

## USE CASE 2: TỔNG THỰC CHẠY BỊ ÂM (NEGATIVE OFFSET) KHI HỦY PHÂN BỔ

```
SHĐ: P1381125   |   Phân bổ (HopDongChiTietREF): 770508, 770509, 770510, 770511
Sản phẩm: CPD / Chi phí

Vấn đề:
  - User báo cáo: Tổng giá trị thực chạy của hợp đồng/phân bổ này tính đến hiện tại bị ÂM tiền (so với phân bổ ký).
  - Không phải chỉ 1-2 dòng bị âm của ngày hôm nay, mà là Lũy kế tổng (SUM) bị thủng đáy.
```

### 1. Nguyên nhân gốc rễ (Root Cause)
Do **Lỗi quét trùng Job đối trừ đa nhóm sản phẩm**.
Khi một phân bổ (`HopDongChiTietREF`) bị Hủy/Xóa, hệ thống phải sinh ra bản ghi đối trừ (âm) để đưa giá trị thực chạy về `0`. Tuy nhiên:
- Phân bổ này bị **cả Job của nhóm Chi Phí** VÀ **Job của nhóm CPD** cùng quét trúng.
- Hậu quả: Cả 2 Job đều sinh ra lệnh đối trừ (trừ tiền 2 lần cho cùng 1 lượng base).
- VD: Base là 10tr. Hủy → Job CPD trừ 10tr, Job Chi phí cũng nhảy vào trừ 10tr → Tổng = 10 - 10 - 10 = -10tr (Bị âm).

### 2. Query Truy vết Lịch sử Dòng tiền
Để chứng minh có sự lặp đối trừ từ 2 Job khác nhau, ta truy vết thẳng vào bảng đích `ThucChayDaTinh`.

```sql
SELECT 
    NgayTinhThucChay,
    ThanhTienThucChay,
    GiaTriThayDoi,
    SoLuongThayDoi,
    LoaiBanGhi,      -- Xác định là record Tính mới hay record Đối trừ
    NguoiTao,        -- Xem Job / User nào sinh ra record này
    NgayTao
FROM ThucChayDaTinh
WHERE HopDongChiTietREF IN (770508, 770509, 770510, 770511)
ORDER BY HopDongChiTietREF, NgayTao;
```
*(Dấu hiệu xác nhận lỗi: Thấy có 2 record đối trừ mang giá trị âm giống hệt nhau, sinh ra gần cùng thời điểm khi phân bổ bị hủy).*

### 3. Hướng Fix
- **Fix Data (Tạm thời):** Xóa tay/Clear bớt các record đối trừ bị lặp (âm tiền) trong bảng `ThucChayDaTinh` (hoặc bảng lịch sử thay đổi tương ứng) để đưa tổng lũy kế về `0` đúng như kỳ vọng khi hủy phân bổ.
- **Fix Logic (Lâu dài - Giao cho Dev):** Sửa lại logic Filter (Mệnh đề `WHERE`) trong các Stored Procedure đối trừ của Job CPD và Job Chi phí. Đảm bảo SP chỉ quét đúng `DmSanPhamID` thuộc nhóm của nó khi thực hiện lệnh Hủy/Xóa, tránh dẫm chân lên nhau.

---

## MẪU TRẢ LỜI CHO PHÍA KIỂM SOÁT

### Mẫu 1 — Cửa sổ đợt chạy hẹp
> Em đã kiểm tra SHĐ **QC0020326** – phân bổ **778668**. Đợt chạy trên đánh số có cửa sổ từ **[ngày A]** đến **[ngày B]** (3 ngày). Booking 10056547 có 2 ngày treo là **[ngày X]** và **[ngày Y]** nằm **ngoài cửa sổ** này nên hệ thống bỏ qua — đây là đúng theo logic nghiệp vụ.
>
> **Hướng xử lý:** Yêu cầu team đánh số điều chỉnh `ThoiGianKetThuc` sang **[ngày Y]**, sau đó chạy lại job tính.

### Mẫu 2 — Booking chưa duyệt
> Em đã kiểm tra SHĐ **QC0020326**. Booking **10056547** có trạng thái **[TrangThaiDuyet = X]** — chưa được duyệt nên hệ thống không đưa vào tính.
>
> **Hướng xử lý:** Duyệt booking trong HDCN/Tool đánh số → Job Sync sẽ cập nhật → Job Calc sẽ tính thêm 2 ngày trong lần chạy tiếp (hoặc chạy lại thủ công).

### Mẫu 3 — Kỳ đã khóa
> Em đã kiểm tra SHĐ **QC0020326**. Lý do chạy lại không được là 2 ngày **[ngày X, Y]** thuộc kỳ **[tháng Z/năm]** đã được chốt số và khóa. Job không override được kỳ đã khóa.
>
> **Hướng xử lý:** Mở khóa kỳ (nếu được phép và trong thời hạn) hoặc ghi nhận bổ sung bằng bút toán điều chỉnh ở kỳ hiện tại.

---

## CÔNG THỨC THAM CHIẾU

```
CPD đợt chạy:
  TT_moingaytreo = SL_danhso × DG_danhso / SoNgayDotChay_danhso × (1 − CK%)
  SoLuongChay    = 1 (mỗi ngày)
  DonViTinh      = "ngày"

Điều kiện để một ngày treo được tính:
  NgayTreo BETWEEN ThoiGianBatDau AND ThoiGianKetThuc   -- đúng cửa sổ
  AND DeletedStatus = 0                                  -- chưa xóa
  AND TrangThaiDuyet = [giá trị hợp lệ]                 -- đã duyệt
```

---

> 💡 **Tip:** Luôn chạy **QUERY CHẨN ĐOÁN** trước — 90% trường hợp sẽ tìm ra nguyên nhân ngay lần đầu.
