# Table: `Admarket_KhachHangHopDongTaiKhoan`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ID` | `INT` PK IDENTITY |  |
| `KhachHangID` | `INT` nullable |  |
| `TenKhachHang` | `NVARCHAR(512)` nullable |  |
| `TenSale` | `NVARCHAR(255)` nullable |  |
| `TkAdmarket` | `NVARCHAR(50)` nullable |  |
| `HopDongID` | `INT` nullable |  |
| `SoHopDong` | `NVARCHAR(50)` nullable |  |
| `SanPhamID` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(50)` nullable |  |
| `ThanhTien` | `FLOAT` nullable |  |
| `TienThucChay` | `FLOAT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_Admarket_KhachHangHopDongTaiKhoan` | `ID` | PRIMARY KEY |
