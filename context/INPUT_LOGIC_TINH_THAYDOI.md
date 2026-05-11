# INPUT: Logic Tính Thay Đổi (Change Detection & Recalculation)

> **Nguồn:** Tổng hợp từ `docs/Logic_nghiepvu_tinh_thucchay.md`
> **Mục đích:** Mô tả luồng phát hiện thay đổi và tính lại thực chạy cho từng nhóm sản phẩm
> **Ngày tạo:** 2026-05-08

---

## 1. Nguyên tắc chung — Tính Thay Đổi

### 1.1 Khi nào kích hoạt "Tính thay đổi"?
Hệ thống tính thay đổi khi phát hiện một trong các sự kiện sau trên dữ liệu đã được tính thực chạy trước đó:

| Sự kiện | Mô tả | Áp dụng cho |
|---------|-------|-------------|
| **Thay đổi thông tin đánh số** | SL_danhso, DG_danhso, songaydotchay, CK thay đổi | CPD, CPM |
| **Thay đổi thuộc tính** | sohopdong, tenkhachhang, nhanvienID, sanphamID, hinhthucquangcaoID, tennhanhangID, tendangnhap | CPD, PR, Admatic |
| **Thay đổi thông tin treo** | SLtreo, tongsongaytreo, DonGia treo thay đổi | CPD, Chi phí, PR |
| **Xóa phân bổ** | Phân bổ (HopDongChiTiet) bị xóa | Tất cả nhóm |
| **Hủy hợp đồng** | Hợp đồng bị hủy trạng thái | Chi phí, PR, Mobile |
| **Thay đổi giá trị phân bổ** | Giá trị phân bổ tăng/giảm | Admarket, Inventory |
| **Thay đổi kết quả vận hành** | Dữ liệu vận hành được cập nhật | Mua ngoài, GG-FB |
| **Thay đổi nhãn hàng** | Phân bổ gán sang nhãn hàng khác | Admatic |
| **Hủy banner** | Banner bị hủy | Admatic |

### 1.2 Phương pháp chung: Đối trừ (Offset & Recalculate)
```
Bước 1: Lấy giá trị thực chạy ĐÃ TÍNH (Before)
Bước 2: Tính lại giá trị thực chạy MỚI (After) theo thông tin hiện tại
Bước 3: GiaTriThayDoi = After - Before
Bước 4: Ghi nhận vào các cột: giatrithaydoi, soluongthaydoi, SoLuongKMThayDoi, GiaTriKMThayDoi
```

### 1.3 Output — Các cột thay đổi được ghi nhận
Tất cả kết quả đối trừ đều được ghi vào các cột sau trong `ThucChayDaTinh`:

| Cột | Ý nghĩa |
|-----|---------|
| `GiaTriThayDoi` | Chênh lệch thành tiền sau triết khấu |
| `SoLuongThayDoi` | Chênh lệch số lượng |
| `GiaTriKMThayDoi` (= TTKhuyenMaiThayDoi) | Chênh lệch giá trị khuyến mãi |
| `SoLuongKMThayDoi` (= SLKhuyenMaiThayDoi) | Chênh lệch số lượng khuyến mãi |

---

## 2. Chi tiết Tính Thay Đổi theo Nhóm Sản phẩm

### 2.1 CPD — Tính thay đổi

#### a) CPD đợt chạy

| Trường hợp | Hành động |
|------------|-----------|
| Thay đổi SL_danhso, DG_danhso, songaydotchay_danhso, CK | ⇒ Tính lại `TTthucchaysauCK_denngaytinh`, `TTKhuyenmai_denngaytinh`, `SLkhuyenmai_denngaytinh`, `SLthucchay_denngaytinh` |
| Thay đổi thuộc tính (sohopdong, tenkhachhang, nhanvienID...) | ⇒ Đối trừ tại ngày tính + ghi nhận thay đổi |
| Xóa phân bổ | ⇒ Đối trừ toàn bộ thực chạy đã tính |
| Thay đổi thông tin treo (SLtreo_denngaytinh) | ⇒ Tính lại `TTthucchaysauCK_denngaytinh`... |

**Kết quả đối trừ:**
- Nếu thay đổi SLkhuyenmai hoặc GTkhuyenmai hoặc thuộc tính ⇒ đối trừ vào `giatrithaydoi`, `soluongthaydoi`, `SLkhuyenmaithaydoi`, `TTkhuyenmaithaydoi`
- Nếu phân bổ bị xóa ⇒ đối trừ
- Trường hợp khác ⇒ Update `giatrithaydoi`, `soluongthaydoi` tại ngày tính hoặc insert mới

#### b) CPD không đợt chạy
- Tương tự CPD đợt chạy nhưng:
  - Thay đổi SL_danhso, DG_danhso, CK (không có songaydotchay)
  - Thay đổi thông tin treo: SLtreo_denngaytinh, **tongsongaytreo**

#### c) CPD đơn vị gói
- Chỉ phát sinh thay đổi khi **thông tin đánh số** thay đổi
- Đối trừ tính lại: `giatrithaydoi`, `soluongthaydoi`, `SLkhuyenmaithaydoi`, `TTkhuyenmaithaydoi`
- Đối trừ nếu phân bổ bị xóa

**Job đối trừ CPD:** `job_ThucChayDaTinh_ReInsertByHopDong` (Job: `job_TinhLaiThucChay`)

---

### 2.2 PR — Tính thay đổi

| Trường hợp | Hành động |
|------------|-----------|
| Thông tin treo đã tính TC nhưng có thay đổi (bao gồm gán lại phân bổ) | ⇒ Đối trừ vào `giatrithaydoi`, `SLthaydoi`, `giatriKMthaydoi`, `SLKMthaydoi` + tính mới |
| Phân bổ/hợp đồng thay đổi thuộc tính | ⇒ Đối trừ + tính mới |
| Phân bổ hoặc hợp đồng bị hủy | ⇒ Chỉ đối trừ (không tính mới) |

---

### 2.3 Inventory — Tính thay đổi

| Trường hợp | Hành động |
|------------|-----------|
| Thay đổi thông tin đánh số phân bổ | ⇒ Đối trừ, tính lại `ThucChayDaTinh` |
| Sản phẩm Admarket | ⇒ Đối trừ tính lại trên CẢ `ThucChayDaTinh` VÀ `ThucChayDaTinh_Admarket` |

---

### 2.4 Chi phí — Tính thay đổi (theo từng TreoID)

#### a) Chi phí khác

| Trường hợp | Hành động |
|------------|-----------|
| HĐ, phân bổ thay đổi VÀ `GiaTriDaTinh <= GiaTriPhanBo` | ⇒ Đối trừ + tính mới vào `giatrithaydoi`, `soluongthaydoi`, `SoLuongKMThayDoi`, `GiaTriKMThayDoi` |
| Hợp đồng hủy | ⇒ Đối trừ đã tính hoặc update vào giatrithaydoi tại `NgayThucHien` |
| Thực treo thay đổi thông tin | ⇒ Đối trừ + tính mới |
| Thực treo hủy | ⇒ Chỉ đối trừ |

#### b) Chi phí sản phẩm chính

| Trường hợp | Hành động |
|------------|-----------|
| HĐ, phân bổ thay đổi | ⇒ Nếu đã tính TC tại ngày hiện tại: Update `GiaTriThayDoi = GiaTriThayDoi_HienTai - GiaTriThayDoi_TruocDo` |
| | ⇒ Nếu chưa tính: Tính mới `GiaTriThayDoi`, `SoLuongThayDoi`, `SoLuongKMThayDoi`, `GiaTriKMThayDoi` |
| Thực treo thay đổi | ⇒ Đối trừ + tính mới |

---

### 2.5 Admarket — Tính thay đổi

| Trường hợp | Hành động |
|------------|-----------|
| Thay đổi thông tin đánh số | ⇒ Đối trừ tính lại |
| Thay đổi giá trị phân bổ (TĂNG) | ⇒ Kiểm tra dữ liệu online (`ThucChayAdmarket_HopDong_online`), nếu có tiền ⇒ ghi nhận thêm thực chạy + đối trừ phần online |
| Thay đổi giá trị phân bổ (GIẢM) | ⇒ _(không mô tả rõ — cần xác nhận)_ |

---

### 2.6 Admatic — Tính thay đổi

| Trường hợp | Hành động |
|------------|-----------|
| Phân bổ thay đổi thông tin | ⇒ Đối trừ + tính lại vào `giatrithaydoi`, `soluongthaydoi`, `SoLuongKMThayDoi`, `GiaTriKMThayDoi` |
| Phân bổ xóa | ⇒ Chỉ đối trừ |
| Banner hủy | ⇒ Đối trừ + tính lại |
| Phân bổ thay đổi nhãn hàng | ⇒ Đối trừ TC của các ngày chạy nhãn hàng CŨ + ghi nhận TC cho các ngày đó với nhãn hàng MỚI |

---

### 2.7 Mua ngoài — Tính thay đổi

| Trường hợp | Hành động |
|------------|-----------|
| HopDong, HopDongChiTiet thay đổi thông tin, giá trị | ⇒ Đối trừ + tính lại TOÀN BỘ phân bổ |
| Dự toán thay đổi (`HopDongChiTiet_MuaNgoai`) | ⇒ Đối trừ + tính lại theo vận hành ID |
| `ThucChayMuaNgoaiChiTiet` thay đổi | ⇒ Đối trừ + tính lại theo vận hành ID |

---

### 2.8 CPM — Tính thay đổi

#### CPM thuần, Trueview, Native_Ads, CPM đơn vị ngày
| Trường hợp | Hành động |
|------------|-----------|
| Phân bổ thay đổi thông tin | ⇒ Đối trừ + tính lại thực chạy |
| Phân bổ bị xóa | ⇒ Đối trừ thực chạy. Nếu chưa tính TC tại ngày thực hiện thì update gttd, ngược lại thì tính thực treo thay đổi |

#### CPV, CPR
- **Hiện tại KHÔNG thấy logic tính thay đổi** _(cần xác nhận)_

#### CPM đơn vị bài
| Trường hợp | Hành động |
|------------|-----------|
| Phân bổ thay đổi thông tin | ⇒ Đối trừ + tính lại + cập nhật trạng thái thực treo |
| Phân bổ bị xóa | ⇒ Đối trừ + cập nhật trạng thái thực treo |

#### CPM đơn vị gói
| Trường hợp | Hành động |
|------------|-----------|
| Phân bổ thay đổi thông tin | ⇒ Đối trừ + tính lại TC cho cả CPM_DonViGoi VÀ Native_Ads/On Image |
| Phân bổ hủy | ⇒ Đối trừ TC cho cả CPM_DonViGoi VÀ Native_Ads/On Image |
| Thực treo hủy | ⇒ Đối trừ + tính lại cho cả CPM_DonViGoi VÀ Native_Ads/On Image |
| Thay đổi đơn giá banner treo | ⇒ Đối trừ + tính lại cho cả CPM_DonViGoi VÀ Native_Ads/On Image |

---

### 2.9 Mobile — Tính thay đổi (2 Loại Xử Lý: Gói & Thường)

> **Lưu ý:** Việc đối trừ và tính lại áp dụng cơ chế chốt chặn đệ quy (CTE Recursive) tương tự như logic tính mới, nhằm đảm bảo tổng số lượng (hoặc thành tiền) sau khi đối trừ không bao giờ vượt quá phân bổ.

| Trường hợp | Hành động |
|------------|-----------|
| Phân bổ thay đổi thông tin | ⇒ Đối trừ + tính lại thực chạy theo cơ chế chốt chặn đệ quy + **ghi log GTTĐ** |
| Phân bổ bị xóa | ⇒ Đối trừ toàn bộ thực chạy đã tính + **ghi log GTTĐ** |
| Hợp đồng hủy | ⇒ Nếu đã tính TC tại ngày thực hiện: đối trừ giảm. Ngược lại: insert thực treo thay đổi do HĐ hủy |

---

### 2.10 GG-Facebook — Tính thay đổi

| Trường hợp | Nguồn phát hiện | Hành động |
|------------|-----------------|-----------|
| Thay đổi thực chạy hàng ngày | `ADS_Operating_Result_Map_Order` | ⇒ Đối trừ + tính lại |
| Thay đổi thực chạy theo sản lượng | `ADS_Operating_Result_Quantity` | ⇒ Đối trừ + tính lại |
| Thông tin order thay đổi | `Operating_Order` | ⇒ Đối trừ + tính lại |
| Thay đổi thành tiền mua | `ADS_Operating_Result` | ⇒ Đối trừ + tính lại |
| HDCT thay đổi thuộc tính/giá trị | `HopDongChiTiet` | ⇒ Đối trừ + tính lại |

---

## 3. Bảng Tổng hợp: Nguồn Phát hiện Thay đổi

| Nhóm SP | Bảng detect thay đổi | Cách detect |
|---------|----------------------|-------------|
| CPD | `HopDongChiTietThayDoi`, `ThucChayHopDongChiTiet` | So sánh SL, DG, CK trước/sau |
| PR | `ThucChayHopDongChiTiet`, `HopDong` | Kiểm tra trạng thái treo đã tính |
| Chi phí | `ThucChayHopDongChiTiet`, `HopDong` | Theo từng TreoID |
| Admarket | `ThucChayAdmarket_PhanBo`, `HopDongChiTiet` | Giá trị phân bổ tăng/giảm |
| Admatic | `ThucChay_ThanhTien_Admatic`, `HopDongChiTiet` | Phân bổ/banner thay đổi |
| CPM | `ThucChay`, bảng con (CPV, CPR, Trueview...) | Phân bổ thay đổi |
| Mobile | `ThucChay`, `HopDongChiTiet` | Phân bổ thay đổi |
| Mua ngoài | `ThucChayMuaNgoaiChiTiet`, `HopDongChiTiet_MuaNgoai` | HDCT/dự toán thay đổi |
| GG-FB | `ADS_Operating_Result*`, `Operating_Order` | Kết quả vận hành thay đổi |
| Inventory | `HopDongChiTiet` | Đánh số phân bổ thay đổi |

---

## 4. Câu hỏi mở (cần xác nhận)

> [!WARNING]
> Các điểm sau chưa rõ trong tài liệu nghiệp vụ, cần user xác nhận:

1. **CPV, CPR:** File ghi "Hiện ko thấy tính" cho TH2 (thay đổi) — có phải các nhóm này chưa implement logic thay đổi?
2. **Admarket giảm giá trị:** Khi giá trị phân bổ GIẢM, quy trình xử lý thế nào?
3. **Inventory:** Bảng nào detect thay đổi? Có dùng `HopDongChiTietThayDoi` không?
4. **Performance Base:** Logic thay đổi cụ thể ra sao? File chỉ ghi "Đã nằm trong job Admarket"
