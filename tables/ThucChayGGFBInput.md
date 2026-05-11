# Table: `ThucChayGGFBInput`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThucChayGGFBInputID` | `INT` PK IDENTITY |  |
| `SoHopDong` | `NVARCHAR(50)` nullable |  |
| `DanhSachTaiKhoan` | `NVARCHAR(200)` nullable |  |
| `SoLuongHopDong` | `INT` nullable |  |
| `DonViTinh` | `NVARCHAR(50)` nullable |  |
| `NgayThucHien` | `DATETIME` nullable |  |
| `SoLuongThucChay` | `INT` nullable |  |
| `ThanhTienThucChay` | `FLOAT` nullable |  |
| `NguoiCapNhat` | `NVARCHAR(50)` nullable |  |
| `GhiChu` | `NVARCHAR(500)` nullable |  |
| `DmSanPhamREF` | `NVARCHAR(50)` nullable |  |
| `DmLoaiBannerREF` | `INT` nullable |  |
| `TenLoaiBanner` | `NVARCHAR(100)` nullable |  |
| `GiaTriThanhToan` | `FLOAT` nullable |  |
| `NgayThanhToan` | `DATETIME` nullable |  |
| `ChenhLech` | `FLOAT` nullable |  |
| `ThanhTienHopDong` | `FLOAT` nullable |  |
| `NhanHopDong` | `NVARCHAR(500)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ThucChayGGFBInput` | `ThucChayGGFBInputID` | PRIMARY KEY |
