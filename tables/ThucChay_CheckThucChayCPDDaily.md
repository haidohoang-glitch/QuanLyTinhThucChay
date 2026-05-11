# Table: `ThucChay_CheckThucChayCPDDaily`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `NgayThucHien` | `DATETIME` nullable |  |
| `HopDongREF` | `INT` nullable |  |
| `SoHopDong` | `NVARCHAR(50)` nullable |  |
| `HopDongChiTietREF` | `INT` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(200)` nullable |  |
| `SoLuongHD` | `INT` nullable |  |
| `SoLuongNgayDotChay` | `INT` nullable |  |
| `SoLuongThucChayTest` | `INT` nullable |  |
| `SoLuongChay_tcdt` | `INT` nullable |  |
| `DonGiaNgay` | `FLOAT` nullable |  |
| `ThanhTienHD` | `FLOAT` nullable |  |
| `TienThucChayTest` | `FLOAT` nullable |  |
| `TienThucChay_tcdt` | `FLOAT` nullable |  |
| `TienLech` | `FLOAT` nullable |  |
| `CheckedStatus` | `INT` DEFAULT 0 nullable | =0 chua check, = 1 da check |
| `Status` | `INT` DEFAULT 0 nullable | =0 true, = 1 false, = 2 warning,pending |
| `NguyenNhan` | `NVARCHAR(MAX)` nullable |  |
| `GhuChuPhanBo` | `NVARCHAR(MAX)` nullable |  |
