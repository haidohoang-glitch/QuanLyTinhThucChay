# Table: `QLTC_Log_Admatic_TongSP_vs_ChitietSP`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `LogId` | `INT` PK IDENTITY |  |
| `Admatic` | `NVARCHAR(MAX)` nullable |  |
| `DmSanPhamREF` | `NVARCHAR(MAX)` nullable |  |
| `TenSanPham` | `NVARCHAR(MAX)` nullable |  |
| `View (SP/ASD)` | `NVARCHAR(MAX)` nullable |  |
| `Click (SP/ASD)` | `NVARCHAR(MAX)` nullable |  |
| `Tien (SP/ASD)` | `NVARCHAR(MAX)` nullable |  |
| `TienKM (SP/ASD)` | `NVARCHAR(MAX)` nullable |  |
| `TrangThai` | `NVARCHAR(MAX)` nullable |  |
| `NgayThucHien` | `DATE` nullable |  |
| `NguoiThucHien` | `NVARCHAR(255)` nullable |  |
| `NgayKiemTra` | `DATETIME` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK__QLTC_Log__5E5486482FC44706` | `LogId` | PRIMARY KEY |
