# Table: `PMS_QuanLyThucChay_Account`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `Id` | `INT` PK |  |
| `B_QuanLyThucChayREF` | `INT` nullable |  |
| `D_NhanSuREF` | `INT` nullable |  |
| `CreationTime` | `DATETIME2` nullable |  |
| `CreatorUserId` | `BIGINT` nullable |  |
| `LastModificationTime` | `DATETIME2` nullable |  |
| `LastModifierUserId` | `BIGINT` nullable |  |
| `IsDeleted` | `BIT` NN |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_PMS_QuanLyThucChay_Account` | `Id` | PRIMARY KEY |
