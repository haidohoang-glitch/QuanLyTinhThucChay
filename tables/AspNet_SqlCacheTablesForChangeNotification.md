# Table: `AspNet_SqlCacheTablesForChangeNotification`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `tableName` | `NVARCHAR(450)` PK |  |
| `notificationCreated` | `DATETIME` NN DEFAULT getdate |  |
| `changeId` | `INT` NN DEFAULT 0 |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK__AspNet_S__93F7AC692823D721` | `tableName` | PRIMARY KEY |
