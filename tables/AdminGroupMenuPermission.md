# Table: `AdminGroupMenuPermission`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `AdminGroupId` | `INT` PK |  |
| `AdminMenuId` | `INT` PK |  |
| `Status` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_AdminGroupMenuPermission` | `AdminGroupId, AdminMenuId` | PRIMARY KEY |
