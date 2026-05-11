# Table: `CauHinh`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `TenCauHinh` | `NVARCHAR(100)` PK |  |
| `GiaTri` | `NVARCHAR(500)` nullable |  |
| `NgayCapNhat` | `DATETIME` DEFAULT getdate nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK__CauHinh__13FC1E28786D28D4` | `TenCauHinh` | PRIMARY KEY |
