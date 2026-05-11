# Table: `Log_MaxNgayThucHien`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ID` | `INT` PK IDENTITY |  |
| `MaxNgayThucHien` | `DATE` nullable |  |
| `NhomSanPham` | `SMALLINT` nullable | 1: Nhom san pham CPM, 2 : Mobile, 3: Admatic, 4: CPD,  |
| `LogTime` | `DATETIME` nullable |  |
| `Next_MaxNgayThucHien` | `DATE` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_Log_MaxNgayThucHien` | `ID` | PRIMARY KEY |
