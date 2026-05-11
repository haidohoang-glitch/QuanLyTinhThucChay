# Table: `HopDongChiTiet`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `HopDongChiTietID` | `INT` PK | ID primary key của table HopDongChiTiet |
| `HopDongFK` | `INT` NN | ID foreign key của table HopDong |
| `DanhSachNhanHangREF` | `NVARCHAR(500)` nullable | ID foreign key của table nhãn hàng chi tiết của từng bản ghi trên table HopDongChiTiet |
| `NhanHang` | `NVARCHAR(1000)` nullable | Tên nhãn hàng |
| `DmNhomNganhREF` | `NVARCHAR(250)` nullable | ID foreign key từ table DmNganhHang |
| `TenNhomNganh` | `NVARCHAR(1000)` nullable | Tên ngành hàng |
| `DmLoaiREF` | `INT` nullable | ID foreign key DmHinhThucQuangCao |
| `TenLoai` | `NVARCHAR(250)` nullable | Tên của hình thức quảng cáo từ table DmHinhThucQuangCao |
| `DmNhomWebsiteREF` | `NVARCHAR(200)` nullable | ID của table DmNhomWebsite |
| `TenNhomWebsite` | `NVARCHAR(500)` nullable | Tên nhóm Website |
| `DmWebsiteREF` | `INT` nullable | ID foreign key của table DmWebsite |
| `TenWebsite` | `NVARCHAR(500)` nullable | Tên website từ table DmWebsite |
| `DmSanPhamREF` | `INT` nullable | ID foreign key từ table DmSanPham |
| `TenSanPham` | `NVARCHAR(500)` nullable | Tên sản phẩm từ table DmSanPham |
| `DmLoaiBannerREF` | `INT` nullable | ID của DmLoaiBanner |
| `TenLoaiBanner` | `NVARCHAR(250)` nullable | Tên loại banner |
| `DmChuyenMucREF` | `INT` nullable | ID của DmChuyenMuc |
| `TenChuyenMuc` | `NVARCHAR(500)` nullable | Tên của chuyên mục từ table DmChuyenMuc |
| `DmViTriREF` | `INT` nullable | ID từ table DmVitri |
| `TenViTri` | `NVARCHAR(500)` nullable | Tên vị trí quảng cáo trên site từ table DmViTri |
| `ThoiGian` | `NVARCHAR(100)` nullable |  |
| `SoLuong` | `INT` nullable | Số lượng chi tiết của từng đơn hàng |
| `DonViTinhREF` | `INT` nullable | ID Foreign key của DmDonViTinh |
| `DonViTinh` | `NVARCHAR(100)` nullable | Mã đơn vị tính |
| `DonGia` | `FLOAT` nullable | Đơn giá trên từng số lượng sản phẩm |
| `ChietKhau` | `FLOAT` nullable | Chiết khấu |
| `GiamGia` | `FLOAT` nullable |  |
| `TiLeTuVan` | `FLOAT` nullable |  |
| `KhuyenMai` | `NVARCHAR(500)` nullable |  |
| `IsKhuyenMai` | `INT` nullable | Thông tin HopDongChiTiet có khuyến mãi hay không , = 1 là chiết khấu = 100%, = 0 là không có chiết khấu. |
| `ChiPhiTuVan` | `FLOAT` nullable |  |
| `ThanhTien` | `FLOAT` nullable | tổng thành tiến của HopDongChiTiet (phân bổ), đã bao gồm chiết khấu |
| `GhiChu` | `NVARCHAR(2000)` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` NN |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` NN |  |
| `DeletedStatus` | `INT` NN |  |
| `PrintStatus` | `INT` NN |  |
| `RecordStatus` | `INT` NN |  |
| `DmSanphamREF_old` | `INT` nullable |  |
| `TK_AdMarket` | `NVARCHAR(1000)` nullable | Tên tài khoản chạy trên các sản phẩm Adx, Viewplus |
| `TK_AdMarketID` | `NVARCHAR(200)` nullable | ID của tài khoản |
| `SoluongThucChay` | `FLOAT` nullable |  |
| `ThanhtienThucChay` | `FLOAT` nullable |  |
| `TrangthaiThucChay` | `INT` nullable |  |
| `ThoiGianBatDau` | `DATETIME` nullable |  |
| `ThoiGianKetThuc` | `DATETIME` nullable |  |
| `ThucChayDenNgay` | `DATETIME` nullable |  |
| `DmBannerREF` | `INT` nullable |  |
| `TenBanner` | `NVARCHAR(500)` nullable |  |
| `DmLoaiNenTangREF` | `INT` nullable |  |
| `TenLoaiNenTang` | `NVARCHAR(500)` nullable |  |
| `DonViTinhThucChayMuaNgoaiREF` | `INT` nullable |  |
| `DonViTinhThucChayMuaNgoai` | `NVARCHAR(50)` nullable |  |
| `ThanhTienThucChayMuaNgoaiTruocCK` | `FLOAT` nullable |  |
| `ChietKhauMuaNgoai` | `INT` nullable |  |
| `IsVuotKhung` | `INT` nullable |  |
| `SoHopDongHT` | `NVARCHAR(200)` nullable |  |
| `DmSuKienREF` | `INT` nullable |  |
| `TenSuKien` | `NVARCHAR(1000)` nullable |  |
| `SuKienREF` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `csHopDongChiTiet` | `HopDongChiTietID` | PRIMARY KEY |
| `HopDong_IDX` | `HopDongFK, DmSanPhamREF` | BTREE |
| `nonix_dm_del_tk` | `DmSanPhamREF, DeletedStatus, TK_AdMarket` | BTREE |
| `nonix_dmspref_del_tk` | `DmSanPhamREF, DeletedStatus, TK_AdMarket` | BTREE |
| `nonix_dmspref_delstat_tkadmarket` | `DmSanPhamREF, DeletedStatus, TK_AdMarket` | BTREE |
