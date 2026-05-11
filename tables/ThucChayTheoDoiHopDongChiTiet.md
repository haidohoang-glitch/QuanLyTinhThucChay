# Table: `ThucChayTheoDoiHopDongChiTiet`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `HopDongChiTietID` | `INT` NN |  |
| `HopDongFK` | `INT` NN |  |
| `NhanHang` | `NVARCHAR(255)` nullable |  |
| `DmNhomNganhREF` | `INT` nullable |  |
| `TenNhomNganh` | `NVARCHAR(50)` nullable |  |
| `DmLoaiREF` | `INT` nullable |  |
| `TenLoai` | `NVARCHAR(50)` nullable |  |
| `DmNhomWebsiteREF` | `INT` nullable |  |
| `TenNhomWebsite` | `NVARCHAR(100)` nullable |  |
| `DmWebsiteREF` | `INT` nullable |  |
| `TenWebsite` | `NVARCHAR(100)` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(100)` nullable |  |
| `DmLoaiBannerREF` | `INT` nullable |  |
| `TenLoaiBanner` | `NVARCHAR(50)` nullable |  |
| `DmChuyenMucREF` | `INT` nullable |  |
| `TenChuyenMuc` | `NVARCHAR(100)` nullable |  |
| `DmViTriREF` | `INT` nullable |  |
| `TenViTri` | `NVARCHAR(50)` nullable |  |
| `ThoiGian` | `NVARCHAR(50)` nullable |  |
| `SoLuong` | `INT` nullable |  |
| `DonViTinh` | `NVARCHAR(50)` nullable |  |
| `DonGia` | `FLOAT` nullable |  |
| `ChietKhau` | `FLOAT` nullable |  |
| `GiamGia` | `FLOAT` nullable |  |
| `TiLeTuVan` | `FLOAT` nullable |  |
| `KhuyenMai` | `NVARCHAR(50)` nullable |  |
| `IsKhuyenMai` | `INT` nullable |  |
| `ChiPhiTuVan` | `FLOAT` nullable |  |
| `ThanhTien` | `FLOAT` nullable |  |
| `GhiChu` | `NVARCHAR(255)` nullable |  |
| `DotChayHopDongChiTiet` | `NVARCHAR(4000)` nullable |  |
| `NgayDaChay` | `NVARCHAR(4000)` nullable |  |
| `ThucChayDenNgay` | `DATETIME` nullable |  |
| `TrangThaiHopDongChiTietThucChay` | `INT` nullable |  |
| `SoLuongDaChay` | `FLOAT` nullable |  |
| `SoLuongChuaChay` | `FLOAT` nullable |  |
| `ThanhTienDaChay` | `FLOAT` nullable |  |
| `ThanhTienChuaChay` | `FLOAT` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` NN |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` NN |  |
| `DeletedStatus` | `INT` NN |  |
| `PrintStatus` | `INT` NN |  |
| `RecordStatus` | `INT` NN |  |
