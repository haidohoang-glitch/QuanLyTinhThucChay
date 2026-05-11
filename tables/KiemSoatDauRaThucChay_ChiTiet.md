# Table: `KiemSoatDauRaThucChay_ChiTiet`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ID` | `BIGINT` NN IDENTITY |  |
| `NgayThucHien` | `DATETIME` nullable |  |
| `DotChayBooking` | `NVARCHAR(100)` nullable |  |
| `HopDongID` | `INT` nullable |  |
| `SoHopDong` | `NVARCHAR(100)` nullable |  |
| `HopDongChiTietREF` | `INT` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(100)` nullable |  |
| `DmHinhThucQuangCaoREF` | `NVARCHAR(100)` nullable |  |
| `ThongTinThucTreo` | `NVARCHAR(1000)` nullable |  |
| `ThongTinThucChay` | `NVARCHAR(1000)` nullable |  |
| `IDLoi` | `INT` nullable |  |
| `TenLoiChiTiet` | `NVARCHAR(300)` nullable |  |
| `SPXuLyLoi` | `NVARCHAR(500)` nullable |  |
| `TrangThaiXuLy` | `INT` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `DmBannerID` | `INT` nullable |  |
