# Table: `AdminGroup`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `AdminGroupId` | `INT` PK IDENTITY |  |
| `Name` | `NVARCHAR(128)` NN |  |
| `Description` | `NVARCHAR(256)` nullable |  |
| `Status` | `INT` nullable |  |
| `Priority` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_AdminGroup` | `AdminGroupId` | PRIMARY KEY |
