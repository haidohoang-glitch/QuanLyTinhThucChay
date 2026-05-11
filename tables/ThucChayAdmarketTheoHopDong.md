# Table: `ThucChayAdmarketTheoHopDong`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ID` | `BIGINT` PK IDENTITY |  |
| `USER_ID` | `INT` nullable |  |
| `USERNAME` | `NVARCHAR(150)` nullable |  |
| `ISNOIBO` | `SMALLINT` nullable |  |
| `TT_CLICK` | `BIGINT` nullable |  |
| `TT_VIEW` | `BIGINT` nullable |  |
| `MONEY` | `BIGINT` nullable |  |
| `PROMOTION` | `BIGINT` nullable |  |
| `CONTRACT_NUMBER` | `NVARCHAR(150)` nullable |  |
| `DOMAIN_NAME` | `NVARCHAR(150)` nullable |  |
| `DOMAIN_TT_CLICK` | `BIGINT` nullable |  |
| `DOMAIN_TT_VIEW` | `BIGINT` nullable |  |
| `DOMAIN_MONEY` | `BIGINT` nullable |  |
| `DOMAIN_PROMOTION` | `BIGINT` nullable |  |
| `EXECUTED_DATE` | `DATETIME` nullable |  |
| `CREATED_DATE` | `DATETIME` nullable |  |
| `FORMAT` | `NVARCHAR(150)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ThucChayAdmarketTheoHopDong` | `ID` | PRIMARY KEY |
