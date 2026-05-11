# INPUT: Logic Tính Mới (New Calculation)

> **Nguồn:** Tổng hợp từ `docs/Logic_nghiepvu_tinh_thucchay.md`
> **Mục đích:** Mô tả luồng tính thực chạy MỚI cho từng nhóm sản phẩm Level 1
> **Ngày tạo:** 2026-05-08

---

## 1. Nguyên tắc chung — Tính Mới

**Định nghĩa "Tính mới"**: Ghi nhận doanh số thực chạy lần đầu cho một phân bổ (HopDongChiTiet) tại ngày tính thực chạy, khi phân bổ đó có thông tin vận hành (treo/view/click/kết quả vận hành) nhưng **chưa được tính thực chạy trước đó** trong bảng `ThucChayDaTinh`.

**Công thức chung:**
```
ThanhTienSauTrietKhauThucChay = ThanhTienTruocTrietKhau × (1 - ChietKhau/100)
```

Trong đó `ThanhTienTruocTrietKhau` được tính khác nhau tùy nhóm sản phẩm.

**Output chung:** Insert record vào bảng `ThucChayDaTinh` (hoặc `ThucChayDaTinhAdmarket` cho nhóm Admarket).

---

## 2. Chi tiết Tính Mới theo Nhóm Sản phẩm

### 2.1 CPD (Cost Per Day)

**Điều kiện nhận diện:**
- `DmSanPhamID IN (140, 228, 241, 564, 549, 5082)`
- `NOT (DmHinhThucQuangCao IN (42, 13) OR DmLoaiBannerREF = 18)`

**3 loại CPD — Công thức tính mới:**

#### a) CPD đợt chạy
- **Điều kiện:** Có thông tin đợt chạy trên đánh số
- **Khi có thông tin treo tại ngày tính:**
  ```
  TTthucchaysauCK_moingaytreo = SL_danhso × DG_danhso / songaydotchay_danhso × (1 - CK_danhso%)
  SoLuongChay_moingaytreo = 1
  DonViTinh = "ngày"
  ```

#### b) CPD không đợt chạy
- **Điều kiện:** Không có thông tin đợt chạy trên đánh số → lấy từ thông tin treo
- **Khi có thông tin treo tại ngày tính:**
  ```
  TTthucchaysauCK_moingaytreo = SL_danhso × DG_danhso / tongsongaytreo × (1 - CK_danhso%)
  SoLuongChay_moingaytreo = 1
  DonViTinh = "ngày"
  ```
- **Khác biệt:** Chia cho `tongsongaytreo` (tổng số ngày treo) thay vì `songaydotchay_danhso`

#### c) CPD đơn vị gói
- **Điều kiện:** Đơn giá và số lượng theo đơn vị gói
- **Khi có thông tin treo tại ngày tính:**
  ```
  TTthucchaysauCK = SL_danhso × DG_danhso × (1 - CK_danhso%)
  SoLuongChay = SL_danhso
  DonViTinh = "gói"
  ```
- **Đặc biệt:** Ghi nhận thực chạy FULL giá trị phân bổ khi phân bổ có thông tin treo. Chỉ khi phân bổ thay đổi thông tin đánh số mới xác định giá trị thay đổi.

**Job tính:** `ThucChay_CPD_Chiphi_PR` → Step 1: `EXEC [dbo].[ThucChay_CPD_Job]`
**Bảng đích:** `ThucChayDaTinh`

---

### 2.2 PR (Tuyến bài, Giao lưu trực tuyến, Adpage)

**Điều kiện nhận diện:**
- `DmSanPhamREF IN (141, 245, 250, 637, 305)`
- `NOT (DmHinhThucQuangCao IN (42, 13) OR DmLoaiBannerREF = 18)`

**Điều kiện tính mới:** Phân bổ có thông tin treo tại ngày tính thực chạy NHƯNG:
- Thông tin treo chưa tính thực chạy trước đó, HOẶC
- Thông tin treo trước nhưng đến ngày tính thực chạy mới đánh số

**Công thức:**
```
TTthucchaysauCK_IDtreo = SLtreo × Giatientreo × (1 - CKtreo%)
SoLuongChay_IDtreo = SLtreo
```

**Job tính:** `ThucChay_CPD_Chiphi_PR` → Step 3: `EXEC [dbo].[ThucChay_PR_Job]`
**Bảng đích:** `ThucChayDaTinh`

---

### 2.3 Inventory

**Điều kiện nhận diện:**
- `HopDongChiTietRef IN DmHopDongBanInventory`

**Công thức tính mới:**
```
ThanhTienThucChay = ThanhTienPhanBo
```
_(Ghi nhận nguyên giá trị phân bổ)_

**Job tính:** `ThucChay_Admarket_PBdieuchinh_CPMngay_Mobile_Inventory_CPM_Admatic` → Step 5: `EXEC dbo.ThucChay_job_TinhthucchayInventory`
**Bảng đích:** `ThucChayDaTinh`, `ThucChayDaTinh_Admarket` (cho sản phẩm Admarket)

---

### 2.4 Chi phí

**Điều kiện nhận diện:**
- `DmSanPhamREF IN (SELECT ID FROM CauHinhNhomTinhDoanhSoThucChay WHERE NhomTinhDoanhSoThucChay = 1)`
- `NOT (DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18)`
- `NOT (DmViTriREF IN (100093, 100478))`
- `NOT (DmSanPhamREF = 5188 OR DmViTriREF = 100774)`
- `NOT HDBAN_INVENTORY`
- `NOT (DmHinhThucQuangCao IN (26, 5010, 5000) AND DmChienDichREF = 3)`

#### a) Chi phí khác
- **Điều kiện tính mới:** Phân bổ có thông tin treo chưa tính trước đó, VÀ `TTthucchaysauCK_datinh + TTthucchaysauCK_Treo chưa vượt GiaTriPhanBo`
- **Công thức:**
  ```
  ThanhTienTruocTrietKhau = SoLuongThucTreo × DonGiaThucTreo
  ThanhTienSauTrietKhau = ThanhTienTruocTrietKhau - (ThanhTienTruocTrietKhau × ChietKhau / 100)
  SoLuongThucChay = SoLuongThucTreo
  ```

#### b) Chi phí sản phẩm chính
- **Điều kiện tính mới:** Tương tự chi phí khác + kiểm tra vượt giá trị
- **Khi chưa vượt giá trị:**
  ```
  ThanhTienSauTrietKhauThucChay = 0
  ThanhTienKM = 0
  SoLuongThayDoi = 0
  GiaTriThayDoi = hdct.ThanhTien
  ```
- **Nếu IsKhuyenMai = 1 hoặc ChietKhau = 100:**
  ```
  SoLuongThucChayKM = ThucChay_GetSoLuongThucChayChuanByDonViTinh_ChiPhi_SanPhamChinh(...)
  ```
- **Ngược lại:** `SoLuongThucChayKM = 0`

**Job tính:** `ThucChay_CPD_Chiphi_PR` → Step 2: `EXEC [dbo].[ThucChay_ChiPhi_Job]`
**Bảng đích:** `ThucChayDaTinh`

---

### 2.5 Admarket (Nạp tiền)

**2 loại:**
- Admarket thuần
- Admarket điều chỉnh giá trị

**Công thức tính mới:**
```
ThanhTienThucChay = ThanhTienThucChay_VanHanh
```
_(Lấy từ dữ liệu vận hành bên Admarket trả về)_

**Bảng đích:**
- `ThucChayDaTinh`: tính nguyên theo chiều sản phẩm và website
- `ThucChayDaTinhAdmarket`: ưu tiên tính theo chiều hợp đồng
- `ThucChayAdmarket_HopDong_online`: thực chạy dư để bù khi phân bổ tăng giá trị

**Job tính:**
- `ThucChay_Admarket_PBdieuchinh_...` → Step 1: `EXEC dbo.job_prc_asd_calc_admarket_PhanBo`
- Step 2: `EXEC dbo.prc_asd_calc_admarket_UpdateValue_With_HopDong` (điều chỉnh)

---

### 2.6 Admatic

**Điều kiện nhận diện:**
- `DmHinhThucQuangCao = 42`
- `DonViTinh <> N'CPV'`
- `DmLoaiBannerREF NOT IN (17, 18)`
- `DmSanPhamREF IN (231, 238, 339, 240, 598, 613, 370, 680, 735, 821, 342, 585, 5056, 5268)`

**Điều kiện tính mới:** Chưa tính trong `ThucChayDaTinh` nhưng đã được tính trong `ThucChay_ThanhTien_Admatic`

**Công thức:**
- **Nếu `ChietKhau <> 100`:**
  ```
  ThanhTienSauTrietKhauThucChay = Checkvuotgiatri(
      ThanhTienThucChaySauCK_ChuaVAT × TiLeThucChayHDCTSoVoiBanner / 100
  )
  SoLuongThucChay = Checkvuotsoluong(
      SoLuongThucChay_Admatic × TiLeThucChayHDCTSoVoiBanner / 100
  )
  ```
- **Ngược lại (Khuyến mãi):**
  ```
  ThanhTienKM = Checkvuotgiatri(...)
  SoLuongThucChayKM = Checkvuotsoluong(...)
  ```

**Job tính:** `ThucChay_Admarket_PBdieuchinh_...` → Step 7: `EXEC [dbo].[ThucChay_Admatic_Job]`
**Bảng đích:** `ThucChayDaTinh`, `ThucChayDaTinhAdmarket`

---

### 2.7 Mua ngoài

**Công thức tính mới:** Cho kết quả vận hành ID chưa ghi nhận doanh số thực chạy:
```
ThanhTienThucChayBan = ThanhTienThucChayBan_VanhanhID
SoLuongThucChay = SoLuongThucChay_VanhanhID
ThanhTienThucChayLai = ThanhTienThucChayLai_VanhanhID
```

**Job tính:** `ThucChay_MuaNgoai` → Step 1: `EXEC dbo.ThucChay_TinhMuaNgoai_BySQLJobs`
**Bảng đích:** `ThucChayDaTinh`, `ThucChayDaTinh_MuaNgoai`

---

### 2.8 CPM (Cost Per Mile) — 8 loại

**Điều kiện chung:**
- `DmLoaiNenTangREF <> 8`
- `NhomTinhDoanhSoThucChay = 2 (Branding)`
- `NOT (DmLoaiREF IN (13, 42) OR DmLoaiBannerREF IN (17, 18))`
- `NOT (DmHinhThucQuangCao IN (26, 5010, 5000) AND DmChienDichREF = 3)`

#### a) CPM thuần
- `DotChayHopDong <> N'NGAY'` (không phải đơn vị ngày)
- **Tính mới khi:** Đã tính trên `ThucChay` nhưng chưa có trong `ThucChayDaTinh`
- **Công thức:**
  ```
  ThanhTienSauTrietKhauThucChay = SoLuongThucChay × DonGia × (1 - ChietKhau)
  ```
  Trong đó SoLuong theo DonViTinh trên table `ThucChay`

#### b) CPV
- `DonViTinh = 'CPV'`
- Tương tự CPM thuần, nguồn SoLuong từ `ThucChay` + `ThucChayCPV`

#### c) CPR
- `DmSanPhamREF IN (680) AND DotChayBooking = N'CPR_GOI'` hoặc `DmSanPhamREF IN (680, 598) AND DonViTinh = 'CPR'`
- Nguồn SoLuong từ `ThucChay` + `ThucChayCPR`

#### d) Trueview
- `DmSanPhamREF = 240 AND (DonViTinh = N'True View' OR DonViTinh = N'TRUE REACH') AND DmHinhThucQuangCao <> 42`
- Nguồn SoLuong từ `ThucChay` + `ThucChayTrueview`

#### e) Native_Ads/On Image
- `DmSanPhamREF IN (821, 5133)`
- **Tính mới khi:** Đã tính trong `ThucChay_Native_Ads` nhưng chưa trong `ThucChayDaTinh`
- **Công thức:**
  ```
  ThanhTienSauTrietKhauThucChay = quy_doi(ThanhTienThucChaySauCK × TiLeThucChayHDCTSoVoiBanner)
  SoLuongThucChay = quy_doi(SoLuongThucChay_NativeAds × TiLeThucChayHDCTSoVoiBanner)
  ```

#### f) CPM đơn vị bài
- `DmSanPhamREF = 598 AND DmHinhThucQuangCao = 5001 AND DmViTriREF = 9198 AND DonViTinh = N'BÀI' AND DotChayHopDong = N'CPM_DonViBai'`
- **Tính mới khi:** Đã tính trên `ThucChay_DonViBai` nhưng chưa trong `ThucChayDaTinh`
- **Công thức:**
  ```
  ThanhTienSauTrietKhauThucChay = DonGia × (1 - ChietKhau)
  SoLuongThucChay = 1  (nếu ChietKhau <> 100 hoặc IsKhuyenMai = 0)
  SoLuongThucChay = 0  (ngược lại)
  ```

#### g) CPM đơn vị gói
- `DmSanPhamREF IN (339, 240, 598, 342, 5056, 5299) AND DotChayHopDong = N'CPM_DonViGoi'`
- **Tính mới khi:** Đã tính trên `ThucChay_DonViGoi`, chỉ 1 banner/1 SP/1 HDCT/1 đơn giá
- **Công thức:**
  ```
  ThanhTienSauTrietKhauThucChay = ThanhTienThucChaySauCK_ChuaVAT (từ ThucChay_DonViGoi, quy đổi)
  SoLuongThucChay = ThanhTienThucChay / DonGiaQuyDoi
  ```

#### h) CPM đơn vị ngày
- `DmSanPhamREF IN (231, 238, 339, 240, 598, 613, 370, 680, 735, 342, 821) AND DonViTinhREF IN (3, 4)`
- **Công thức:**
  ```
  ThanhTienTruocTrietKhau = @DonGia × @TiLeBannerSiteHDCT
  ThanhTienSauTrietKhau = ThanhTienTruocTrietKhau × (1 - ChietKhau/100)
  SoLuongThucChay = tổng view thực chạy quy đổi trên ThucChay
  ```
  Trong đó `@TiLeBannerSiteHDCT` = đơn vị tính trên HDCT × tỷ lệ (tổng view thực chạy / số lượng thực chạy trên ThucChay)

**Job tính CPM:**
- CPM thuần + CPV + CPR + Trueview + Native_Ads + đơn vị bài + đơn vị gói: `ThucChay_Admarket_PBdieuchinh_...` → Step 6: `EXEC [dbo].[ThucChay_CPM_Job]`
- CPM đơn vị ngày: Step 3: `EXEC dbo.ThucChay_TinhCPM_With_DonViTinh_Ngay_BySQLJobs`
**Bảng đích:** `ThucChayDaTinh`

---

### 2.9 Mobile

**Điều kiện nhận diện:**
- `DmSanPhamREF = 342`
- `NOT (DmHinhThucQuangCao IN (13, 42) OR DmLoaiBannerREF IN (17, 18))`
- `DotChayHopDong NOT IN (N'NGAY', N'CPM_DonViGoi', N'Tính mới CPM DonViGoi')`
- `DmLoaiNenTangREF <> 8`

**Quy tắc chung (Cơ chế Chống Vượt Phân Bổ):**
Hệ thống sử dụng đệ quy (CTE Recursive) để cộng dồn giá trị thực chạy của các bản ghi theo thời gian.
Công thức chốt chặn: `ThucChayGhiNhan = IIF (TichLuyCu + TichLuyMoi >= GiaTriPhanBo, GiaTriPhanBo - TichLuyCu, TichLuyMoi)`. Đảm bảo tổng thực chạy không bao giờ vượt quá phân bổ.
*(Trường hợp 1 banner dùng cho nhiều phân bổ được xử lý ngầm bằng cách nhân với tỷ lệ phân bổ chung `TiLeThucChayHDCTSoVoiBanner`).*

**2 Loại Xử Lý:**

#### a) LoaiXuLy = 1 (Phân bổ đơn vị GÓI)
- **Cơ chế chốt chặn:** Dựa trên **Thành Tiền** (ThanhTienSauCK và ThanhTienKM).
- **Công thức tính ban đầu:**
  ```text
  ThanhTienSauCK = SoLuongThucChay × DonGiaChay × (1 - ChietKhau/100)
  ThanhTienKM = SoLuongThucChay × DonGiaChay (nếu Khuyến mãi)
  ```
  Sau khi qua hàm chốt chặn đệ quy sẽ sinh ra giá trị `ThanhTienThucChay_GhiNhan` cuối cùng.
- **Tính lại Số lượng:** `SoLuongThucChay_GhiNhan = ThanhTienThucChay_GhiNhan / (DonGiaChay × (1-ChietKhau/100))`

#### b) LoaiXuLy = 2 (Phân bổ thường - CPM/CPC)
- **Cơ chế chốt chặn:** Dựa trên **Số Lượng** (SoLuongThucChay).
- **Công thức tính ban đầu:**
  ```text
  SoLuongThucChay = (View nếu CPM / Click nếu CPC) × (TiLeThucChayHDCTSoVoiBanner / 100)
  ```
  Sau khi qua hàm chốt chặn đệ quy sẽ sinh ra giá trị `SoLuongThucChay_GhiNhan`.
- **Tính Thành Tiền:** `ThanhTienThucChay_GhiNhan = SoLuongThucChay_GhiNhan × DonGiaChay × (1-ChietKhau/100)`

**Job tính:** `ThucChay_Admarket_PBdieuchinh_...` → Step 4: `EXEC [dbo].[ThucChay_Mobile_Job]`
**Bảng đích:** `ThucChayDaTinh`

---

### 2.10 Performance Base

- Đã nằm trong job Admarket
- **Job:** `Job_PerformanceBase_DieuChinhGiaTri` → `EXEC dbo.prc_asd_calc_admarket_UpdateValue_With_HopDong`
- **Bảng đích:** `ThucChayDaTinh`, `ThucChayDaTinhAdmarket`, `ThucChayDaTinh_MuaNgoai`

---

### 2.11 GG-Facebook

**Điều kiện nhận diện:**
- `DotChayHopDong = N'ThanhTien_GGFB'`

**2 loại:**
- Theo thực tế phát sinh
- Theo sản lượng chốt

**Công thức tính mới:** Cho kết quả vận hành ID chưa ghi nhận doanh số:
```
DonGiaTheoDonViTinh = ThanhTien_KQVH / SoLuong_KQVH
ThanhTienTCBan = ThanhTien_KQVH × (1 - CK_danhso%)
ThanhTienTCLai = ThanhTienTCBan - ThanhTienTCMua
SoLuongChay = ThanhTienTCBan / DonGiaTheoDonViTinh
DonViTinh = DonViTinh_Order
```
Trong đó `ThanhTien_KQVH` không quá giá trị còn lại của dự toán VÀ giá trị còn lại phân bổ.

**Job tính:** `ThucChay_GoogleFacebook_MktFee` → Step 1: `EXEC [dbo].[ThucChay_GGFB_Job]`
**Bảng đích:** `ThucChayDaTinh`, `ThucChayDaTinh_MuaNgoai`

---

## 3. Tóm tắt Mapping: Nhóm SP → Job → SP Orchestrator → Bảng đích

| # | Nhóm SP | Job | SP Orchestrator | Bảng đích |
|---|---------|-----|-----------------|-----------|
| 1 | CPD (3 loại) | ThucChay_CPD_Chiphi_PR | ThucChay_CPD_Job | ThucChayDaTinh |
| 2 | PR | ThucChay_CPD_Chiphi_PR | ThucChay_PR_Job | ThucChayDaTinh |
| 3 | Chi phí (2 loại) | ThucChay_CPD_Chiphi_PR | ThucChay_ChiPhi_Job | ThucChayDaTinh |
| 4 | Admarket (2 loại) | ThucChay_Admarket_PB... | job_prc_asd_calc_admarket_PhanBo | ThucChayDaTinh, ThucChayDaTinhAdmarket |
| 5 | CPM (8 loại) | ThucChay_Admarket_PB... | ThucChay_CPM_Job + ThucChay_TinhCPM_With_DonViTinh_Ngay_BySQLJobs | ThucChayDaTinh |
| 6 | Admatic | ThucChay_Admarket_PB... | ThucChay_Admatic_Job | ThucChayDaTinh, ThucChayDaTinhAdmarket |
| 7 | Mobile (3 loại) | ThucChay_Admarket_PB... | ThucChay_Mobile_Job | ThucChayDaTinh |
| 8 | Inventory | ThucChay_Admarket_PB... | ThucChay_job_TinhthucchayInventory | ThucChayDaTinh, ThucChayDaTinhAdmarket |
| 9 | Mua ngoài | ThucChay_MuaNgoai | ThucChay_TinhMuaNgoai_BySQLJobs | ThucChayDaTinh, ThucChayDaTinh_MuaNgoai |
| 10 | Performance Base | ThucChay_Admarket_PB... | prc_asd_calc_admarket_UpdateValue_With_HopDong | ThucChayDaTinh, ThucChayDaTinhAdmarket |
| 11 | GG-Facebook (2 loại) | ThucChay_GoogleFacebook_MktFee | ThucChay_GGFB_Job | ThucChayDaTinh, ThucChayDaTinh_MuaNgoai |
