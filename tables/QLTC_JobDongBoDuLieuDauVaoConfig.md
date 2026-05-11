# Table: `QLTC_JobDongBoDuLieuDauVaoConfig`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `Id` | `INT` PK IDENTITY |  |
| `TenJob` | `NVARCHAR(255)` NN |  |
| `ThoiGianBatDau` | `DATETIME` nullable |  |
| `CreatedTime` | `DATETIME` nullable |  |
| `IsDeleted` | `BIT` NN DEFAULT 0 |  |
| `LoaiSanPhamCode` | `VARCHAR(50)` nullable |  |
| `EnableRunJob` | `BIT` DEFAULT 0 nullable |  |
| `IsFromAsdAg2` | `BIT` NN DEFAULT 0 |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK__QLTC_Job__3214EC072C4AB38A` | `Id` | PRIMARY KEY |
