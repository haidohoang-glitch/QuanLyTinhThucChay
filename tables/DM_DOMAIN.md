# Table: `DM_DOMAIN`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ID` | `INT` NN IDENTITY |  |
| `DOMAIN_ID` | `INT` NN |  |
| `DOMAIN_NAME` | `NVARCHAR(500)` NN |  |
| `WEBSITE_ID` | `INT` NN |  |
| `WEBSITE_NAME` | `NVARCHAR(500)` NN |  |
| `CREATED_BY` | `NVARCHAR(50)` NN |  |
| `CREATED_AT` | `DATETIME` NN |  |
| `LASTMODIFIED_BY` | `NVARCHAR(50)` NN |  |
| `LASTMODIFIED_AT` | `DATETIME` NN |  |
| `DELETED_STATUS` | `SMALLINT` NN |  |
| `RECORD_STATUS` | `INT` nullable |  |
| `NOTE` | `NVARCHAR(500)` nullable |  |
