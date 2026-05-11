# Table: `QLTC_Log_Admatic_ChitietSP_vs_ASD`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `LogId` | `INT` PK IDENTITY |  |
| `Admatic` | `NVARCHAR(MAX)` nullable |  |
| `DmSanPhamREF` | `NVARCHAR(MAX)` nullable |  |
| `TenSanPham` | `NVARCHAR(MAX)` nullable |  |
| `Tien (SP/ASD)` | `NVARCHAR(MAX)` nullable |  |
| `KM (SP/ASD)` | `NVARCHAR(MAX)` nullable |  |
| `TrangThai` | `NVARCHAR(MAX)` nullable |  |
| `NgayThucHien` | `DATE` nullable |  |
| `NguoiThucHien` | `NVARCHAR(255)` nullable |  |
| `NgayKiemTra` | `DATETIME` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK__QLTC_Log__5E548648AF104E1B` | `LogId` | PRIMARY KEY |
