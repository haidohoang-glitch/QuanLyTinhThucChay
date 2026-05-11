# Table: `HopDongChiTietSyn`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `HopDongChiTietID` | `INT` NN |  |
| `HopDongFK` | `INT` NN |  |
| `DanhSachNhanHangREF` | `NVARCHAR(500)` nullable |  |
| `NhanHang` | `NVARCHAR(500)` nullable |  |
| `DmNhomNganhREF` | `NVARCHAR(500)` nullable |  |
| `TenNhomNganh` | `NVARCHAR(1500)` nullable |  |
| `DmLoaiREF` | `INT` nullable |  |
| `TenLoai` | `NVARCHAR(500)` nullable |  |
| `DmNhomWebsiteREF` | `NVARCHAR(500)` nullable |  |
| `TenNhomWebsite` | `NVARCHAR(500)` nullable |  |
| `DmWebsiteREF` | `INT` nullable |  |
| `TenWebsite` | `NVARCHAR(500)` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(500)` nullable |  |
| `DmLoaiBannerREF` | `INT` nullable |  |
| `TenLoaiBanner` | `NVARCHAR(500)` nullable |  |
| `DmChuyenMucREF` | `INT` nullable |  |
| `TenChuyenMuc` | `NVARCHAR(500)` nullable |  |
| `DmViTriREF` | `INT` nullable |  |
| `TenViTri` | `NVARCHAR(500)` nullable |  |
| `ThoiGian` | `NVARCHAR(50)` nullable |  |
| `SoLuong` | `INT` nullable |  |
| `DonViTinhREF` | `INT` nullable |  |
| `DonViTinh` | `NVARCHAR(50)` nullable |  |
| `DonGia` | `FLOAT` nullable |  |
| `ChietKhau` | `FLOAT` nullable |  |
| `GiamGia` | `FLOAT` nullable |  |
| `TiLeTuVan` | `FLOAT` nullable |  |
| `KhuyenMai` | `NVARCHAR(500)` nullable |  |
| `IsKhuyenMai` | `INT` nullable |  |
| `ChiPhiTuVan` | `FLOAT` nullable |  |
| `ThanhTien` | `FLOAT` nullable |  |
| `GhiChu` | `NVARCHAR(500)` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` NN |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` NN |  |
| `DeletedStatus` | `INT` NN |  |
| `PrintStatus` | `INT` NN |  |
| `RecordStatus` | `INT` NN |  |
| `DmSanphamREF_old` | `INT` nullable |  |
| `TK_AdMarket` | `NVARCHAR(1000)` nullable |  |
| `TK_AdMarketID` | `NVARCHAR(1000)` nullable |  |
| `SoluongThucChay` | `FLOAT` nullable |  |
| `ThanhtienThucChay` | `FLOAT` nullable |  |
| `TrangthaiThucChay` | `INT` nullable |  |
| `ThoiGianBatDau` | `DATETIME` nullable |  |
| `ThoiGianKetThuc` | `DATETIME` nullable |  |
| `ThucChayDenNgay` | `DATETIME` nullable |  |
| `DmBannerREF` | `INT` nullable |  |
| `TenBanner` | `NVARCHAR(1500)` nullable |  |
| `DmLoaiNenTangREF` | `INT` nullable |  |
| `TenLoaiNenTang` | `NVARCHAR(1500)` nullable |  |
| `DonViTinhThucChayMuaNgoaiREF` | `INT` nullable |  |
| `DonViTinhThucChayMuaNgoai` | `NVARCHAR(150)` nullable |  |
| `ThanhTienThucChayMuaNgoaiTruocCK` | `FLOAT` nullable |  |
| `ChietKhauMuaNgoai` | `INT` nullable |  |
| `IsVuotKhung` | `INT` nullable |  |
