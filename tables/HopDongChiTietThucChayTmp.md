# Table: `HopDongChiTietThucChayTmp`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `HopDongChiTietID` | `INT` PK |  |
| `HopDongFK` | `INT` NN |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(500)` nullable |  |
| `SoLuong` | `INT` nullable |  |
| `DonViTinhREF` | `INT` nullable |  |
| `DonViTinh` | `NVARCHAR(50)` nullable |  |
| `DonGia` | `FLOAT` nullable |  |
| `ChietKhau` | `FLOAT` nullable |  |
| `KhuyenMai` | `NVARCHAR(250)` nullable |  |
| `IsKhuyenMai` | `INT` nullable |  |
| `ThanhTien` | `FLOAT` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` NN |  |
| `SoluongThucChay` | `FLOAT` nullable |  |
| `ThanhtienThucChay` | `FLOAT` nullable |  |
| `ThucChayDenNgay` | `DATETIME` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `csHopDongChiTietThucChayTmp` | `HopDongChiTietID` | PRIMARY KEY |
