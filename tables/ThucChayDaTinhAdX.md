# Table: `ThucChayDaTinhAdX`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThucChayDaTinhID` | `NVARCHAR(50)` NN |  |
| `HopDongID` | `INT` NN |  |
| `SoHopDong` | `NVARCHAR(50)` NN |  |
| `DmMaHopDongREF` | `INT` NN |  |
| `TenMaHopDong` | `NVARCHAR(50)` NN |  |
| `NgayDanhSoHopDong` | `DATETIME` NN |  |
| `NgayKyHopDong` | `DATETIME` NN |  |
| `NhanHopDong` | `NVARCHAR(1000)` nullable |  |
| `NgayNhanBanFax` | `DATETIME` nullable |  |
| `NgayNhanHopDongBanCung` | `DATETIME` nullable |  |
| `NgayChuyenHopDongChoKeToan` | `DATETIME` nullable |  |
| `So` | `NVARCHAR(50)` nullable |  |
| `Thang` | `INT` NN |  |
| `Nam` | `INT` NN |  |
| `GiaTriHopDong` | `FLOAT` nullable |  |
| `CongNo` | `FLOAT` NN |  |
| `HopDongChiTietREF` | `INT` nullable |  |
| `DangSuDung` | `INT` NN |  |
| `IsGiayPhep` | `INT` NN |  |
| `TrangThaiHopDong` | `INT` NN |  |
| `IsBanCung` | `INT` NN |  |
| `DmPhongBanREF` | `INT` NN |  |
| `TenPhongBan` | `NVARCHAR(50)` NN |  |
| `DmBoPhanREF` | `INT` NN |  |
| `TenBoPhan` | `NVARCHAR(50)` NN |  |
| `DmNhomLamViecREF` | `INT` NN |  |
| `TenNhomLamViec` | `NVARCHAR(50)` NN |  |
| `DmDiaDiemLamViecREF` | `INT` NN |  |
| `TenDiaDiemLamViec` | `NVARCHAR(250)` NN |  |
| `SysNhanVienREF` | `INT` NN |  |
| `TenDangNhap` | `NVARCHAR(25)` NN |  |
| `TenNhanVien` | `NVARCHAR(100)` NN |  |
| `TenKhachHang` | `NVARCHAR(255)` NN |  |
| `NhanHang` | `NVARCHAR(255)` nullable |  |
| `DmNhomNganhREF` | `NVARCHAR(250)` nullable |  |
| `TenNhomNganh` | `NVARCHAR(500)` nullable |  |
| `DmHinhThucQuangCao` | `INT` nullable |  |
| `TenHinhThucQuangCao` | `NVARCHAR(250)` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(500)` nullable |  |
| `DmNhomWebsiteREF` | `INT` nullable |  |
| `TenNhomWebsite` | `NVARCHAR(100)` nullable |  |
| `DmChuyenMucREF` | `INT` nullable |  |
| `TenChuyenMuc` | `NVARCHAR(500)` nullable |  |
| `DmLoaiBannerREF` | `INT` nullable |  |
| `TenLoaiBanner` | `NVARCHAR(500)` nullable |  |
| `DmViTriREF` | `INT` nullable |  |
| `TenViTri` | `NVARCHAR(500)` nullable |  |
| `DotChayHopDong` | `NVARCHAR(1000)` nullable |  |
| `SoLuongDotChayHD` | `INT` nullable |  |
| `DotChayBooking` | `NVARCHAR(1000)` nullable |  |
| `SoLuongDotChayBooking` | `INT` nullable |  |
| `SoLuong` | `INT` nullable |  |
| `DonViTinh` | `NVARCHAR(50)` nullable |  |
| `DonGia` | `FLOAT` nullable |  |
| `DonGiaTheoDonVi` | `FLOAT` nullable |  |
| `ChietKhau` | `FLOAT` nullable |  |
| `GiamGia` | `FLOAT` nullable |  |
| `ThanhTien` | `FLOAT` nullable |  |
| `TiLeTuVan` | `FLOAT` nullable |  |
| `ChiPhiTuVan` | `FLOAT` nullable |  |
| `IsKhuyenMai` | `INT` nullable |  |
| `KhuyenMai` | `NVARCHAR(250)` nullable |  |
| `DmBannerREF` | `INT` nullable |  |
| `DmChienDichREF` | `INT` nullable |  |
| `DmWebsiteREF` | `INT` nullable |  |
| `TenWebsite` | `NVARCHAR(255)` nullable |  |
| `TongViewThucChay` | `FLOAT` nullable |  |
| `TongClickThucChay` | `FLOAT` nullable |  |
| `TongSoBaiViet` | `FLOAT` nullable |  |
| `SoLuongThucChay` | `FLOAT` nullable |  |
| `NgayThucHien` | `DATETIME` nullable |  |
| `GiaTriThayDoi` | `FLOAT` nullable |  |
| `ThanhTienThucChayTruocTrietKhau` | `FLOAT` nullable |  |
| `GiaTriTrietKhauThucChay` | `FLOAT` nullable |  |
| `ThanhTienSauTrietKhauThucChay` | `FLOAT` nullable |  |
| `GiaTriHoaHongThucChay` | `FLOAT` nullable |  |
| `ThanhTienThucThu` | `FLOAT` nullable |  |
| `ThanhTienKM` | `FLOAT` nullable |  |
| `SoLuongThucChayKM` | `INT` nullable |  |
| `SoLuongThucChayLechTreoHa` | `INT` nullable |  |
| `ThanhTienLechTreoHa` | `FLOAT` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `IsPheDuyet` | `TINYINT` DEFAULT 0 nullable |  |
| `PheDuyetBy` | `NVARCHAR(50)` nullable |  |
| `PheDuyetAt` | `DATETIME` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `Index_ngaythuchien` | `NgayThucHien` | BTREE |
