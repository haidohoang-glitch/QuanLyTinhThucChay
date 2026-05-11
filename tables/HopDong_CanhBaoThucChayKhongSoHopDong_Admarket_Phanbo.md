# Table: `HopDong_CanhBaoThucChayKhongSoHopDong_Admarket_Phanbo`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ID` | `INT` PK IDENTITY |  |
| `NgayThucHien` | `DATETIME` nullable |  |
| `HopDongChiTietREF` | `INT` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(500)` nullable |  |
| `DmViTriREF` | `INT` nullable |  |
| `TenViTri` | `NVARCHAR(500)` nullable |  |
| `TongView` | `INT` nullable |  |
| `TongClick` | `INT` nullable |  |
| `GiaTriThucChay` | `MONEY` nullable |  |
| `Create_At` | `DATETIME` nullable |  |
| `Created_By` | `NVARCHAR(50)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_HopDong_CanhBaoThucChayKhongSoHopDong_Admarket_Phanbo` | `ID` | PRIMARY KEY |
