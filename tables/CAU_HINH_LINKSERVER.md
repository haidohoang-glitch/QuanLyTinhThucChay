# Table: `CAU_HINH_LINKSERVER`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ID` | `INT` PK IDENTITY |  |
| `SERVER_ID` | `NVARCHAR(200)` nullable |  |
| `DATA_NAME` | `NVARCHAR(200)` nullable |  |
| `GROUP_INPUT` | `NVARCHAR(200)` nullable |  |
| `CREATEDBY` | `NVARCHAR(200)` nullable |  |
| `CREATEDAT` | `DATETIME` nullable |  |
| `DELETEDSTATUS` | `SMALLINT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_CAU_HINH_LINKSERVER` | `ID` | PRIMARY KEY |
