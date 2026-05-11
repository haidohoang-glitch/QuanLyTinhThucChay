# Table: `ThucChayHopDongChiTiet_dev`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThucChayHopDongChiTietID` | `INT` NN |  |
| `HopDongREF` | `INT` nullable |  |
| `NhanHang` | `NVARCHAR(1000)` nullable |  |
| `ThoiGianBatDau` | `DATETIME` nullable |  |
| `ThoiGianKetThuc` | `DATETIME` nullable |  |
| `Link` | `NVARCHAR(2000)` nullable |  |
| `DmBannerREF` | `NVARCHAR(255)` nullable |  |
| `TenBanner` | `NVARCHAR(255)` nullable |  |
| `ViTri` | `NVARCHAR(255)` nullable |  |
| `GhiChu` | `NVARCHAR(255)` nullable |  |
| `BookingREF` | `INT` nullable |  |
| `HopDongChiTietREF` | `INT` nullable |  |
| `TypeThucChay` | `INT` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` NN |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` NN |  |
| `DeletedStatus` | `INT` NN |  |
| `PrintStatus` | `INT` NN |  |
| `RecordStatus` | `INT` NN |  |
| `DmViTriREF` | `INT` nullable |  |
| `DmNhanHangREF` | `NVARCHAR(200)` nullable |  |
| `SoLuongThucTreo` | `FLOAT` nullable |  |
| `SoLuongThucChay` | `FLOAT` nullable |  |
| `DmDonViTinhREF` | `BIGINT` nullable |  |
| `DonViTinh` | `NVARCHAR(200)` nullable |  |
| `DmHinhThucQuangCaoREF` | `INT` nullable |  |
| `TenHinhThucQuangCao` | `NVARCHAR(200)` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(200)` nullable |  |
| `InputType` | `INT` nullable |  |
| `IsReadBooking` | `INT` nullable |  |
| `KichThuoc` | `NVARCHAR(300)` nullable |  |
| `DonGia` | `FLOAT` nullable |  |
| `ChietKhau` | `FLOAT` nullable |  |
| `ThanhTien` | `FLOAT` nullable |  |
| `Id` | `INT` NN IDENTITY |  |
| `LoaiThucTreo` | `NVARCHAR(50)` nullable |  |
