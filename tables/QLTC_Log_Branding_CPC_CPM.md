# Table: `QLTC_Log_Branding_CPC_CPM`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `LogId` | `INT` PK IDENTITY |  |
| `Branding` | `NVARCHAR(MAX)` nullable |  |
| `TenSanPham` | `NVARCHAR(MAX)` nullable |  |
| `DmSanPhamREF` | `NVARCHAR(MAX)` nullable |  |
| `TypeProduct` | `NVARCHAR(MAX)` nullable |  |
| `View HN (ASD/SP)` | `NVARCHAR(MAX)` nullable |  |
| `Click HN (ASD/SP)` | `NVARCHAR(MAX)` nullable |  |
| `View HQ → HN (ASD)` | `NVARCHAR(MAX)` nullable |  |
| `Click HQ → HN (ASD)` | `NVARCHAR(MAX)` nullable |  |
| `TrangThai` | `NVARCHAR(MAX)` nullable |  |
| `NgayThucHien` | `DATE` nullable |  |
| `NguoiThucHien` | `NVARCHAR(255)` nullable |  |
| `NgayKiemTra` | `DATETIME` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK__QLTC_Log__5E54864865729C44` | `LogId` | PRIMARY KEY |
