# Table: `DM_BANNER_TYPE_NAME_PRODUCT`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ID` | `INT` PK IDENTITY |  |
| `BANNER_TYPE_NAME` | `NVARCHAR(200)` NN |  |
| `PRODUCT_ID` | `INT` NN |  |
| `CREATED_AT` | `DATETIME` NN |  |
| `CREATED_BY` | `NVARCHAR(50)` NN |  |
| `LASTMODIFIED_AT` | `DATETIME` NN |  |
| `LASTMODIFIED_BY` | `NVARCHAR(50)` NN |  |
| `DELETED_STATUS` | `SMALLINT` NN |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_DM_BANNER_TYPE_NAME_PRODUCT` | `ID` | PRIMARY KEY |
