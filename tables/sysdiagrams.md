# Table: `sysdiagrams`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `name` | `SYSNAME` NN |  |
| `principal_id` | `INT` NN |  |
| `diagram_id` | `INT` PK IDENTITY |  |
| `version` | `INT` nullable |  |
| `definition` | `VARBINARY` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK__sysdiagr__C2B05B61725BF7F6` | `diagram_id` | PRIMARY KEY |
| `UK_principal_name` | `principal_id, name` | UNIQUE |
