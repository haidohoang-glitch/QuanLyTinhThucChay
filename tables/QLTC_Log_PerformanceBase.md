# Table: `QLTC_Log_PerformanceBase`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `LogId` | `INT` PK IDENTITY |  |
| `TenSanPham` | `NVARCHAR(MAX)` nullable |  |
| `DmViTriREF` | `NVARCHAR(MAX)` nullable |  |
| `TenViTri` | `NVARCHAR(MAX)` nullable |  |
| `soluonguser_SP` | `NVARCHAR(MAX)` nullable |  |
| `View (SP/Total)` | `NVARCHAR(MAX)` nullable |  |
| `Click (SP/Total)` | `NVARCHAR(MAX)` nullable |  |
| `TienTC (SP/Total)` | `NVARCHAR(MAX)` nullable |  |
| `TienKM (SP/Total)` | `NVARCHAR(MAX)` nullable |  |
| `TrangThai` | `NVARCHAR(MAX)` nullable |  |
| `NgayThucHien` | `DATE` nullable |  |
| `NguoiThucHien` | `NVARCHAR(255)` nullable |  |
| `NgayKiemTra` | `DATETIME` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK__QLTC_Log__5E5486489F9894A7` | `LogId` | PRIMARY KEY |
