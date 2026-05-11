# Table: `ReportFilter`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ID` | `INT` PK IDENTITY |  |
| `TenTruong` | `NVARCHAR(50)` nullable |  |
| `Mota` | `NVARCHAR(2000)` nullable |  |
| `DoUuTien` | `INT` nullable |  |
| `KieuDuLieu` | `NVARCHAR(50)` nullable |  |
| `DataSource` | `NVARCHAR(50)` nullable |  |
| `UrlDataSource` | `NVARCHAR(2000)` nullable |  |
| `MaChucNang` | `NVARCHAR(4000)` nullable |  |
| `IsDefault` | `BIT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ReportFilter` | `ID` | PRIMARY KEY |
