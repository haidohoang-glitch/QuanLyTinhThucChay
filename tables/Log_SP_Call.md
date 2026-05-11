# Table: `Log_SP_Call`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ID` | `INT` PK IDENTITY |  |
| `SP_NAME` | `NVARCHAR(500)` NN |  |
| `SP_TIME_CALL` | `DATETIME` NN |  |
| `SP_END_TIME_CALL` | `DATETIME` nullable |  |
| `NOTE` | `NVARCHAR(500)` nullable |  |
| `VALUE_INPUT` | `NVARCHAR(2000)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_Log_SP_Call` | `ID` | PRIMARY KEY |
