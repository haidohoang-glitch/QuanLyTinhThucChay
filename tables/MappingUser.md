# Table: `MappingUser`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `MappingUserID` | `INT` PK IDENTITY |  |
| `FromUserName` | `NVARCHAR(50)` nullable |  |
| `ToUserName` | `NVARCHAR(50)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_MappingUser` | `MappingUserID` | PRIMARY KEY |
