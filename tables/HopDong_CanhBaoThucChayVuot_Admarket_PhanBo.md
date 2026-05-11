# Table: `HopDong_CanhBaoThucChayVuot_Admarket_PhanBo`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ID` | `INT` PK IDENTITY |  |
| `NgayThucHien` | `DATETIME` nullable |  |
| `SoHopDong` | `NVARCHAR(50)` nullable |  |
| `HopDongChiTietREF` | `INT` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(500)` nullable |  |
| `DmViTriREF` | `INT` nullable |  |
| `TenViTri` | `NVARCHAR(500)` nullable |  |
| `GiaTriHopDong` | `MONEY` nullable |  |
| `GiaTriThucChay_HienTai` | `MONEY` nullable |  |
| `GiaTriThucChay_TraVe` | `MONEY` nullable |  |
| `Created_By` | `NVARCHAR(50)` nullable |  |
| `Created_At` | `DATETIME` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_HopDong_CanhBaoThucChay_Admarket_PhanBo` | `ID` | PRIMARY KEY |
