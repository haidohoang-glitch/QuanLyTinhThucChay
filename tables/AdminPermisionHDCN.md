# Table: `AdminPermisionHDCN`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `AdminPermisionHDCNID` | `INT` PK |  |
| `NhanSuSoYeuLyLichID` | `INT` nullable |  |
| `TenDangNhap` | `NVARCHAR(50)` nullable |  |
| `AdminGroupId` | `INT` nullable |  |
| `KhoaNguoiDung` | `INT` nullable |  |
| `ThoiGianDangNhap` | `DATETIME` nullable |  |
| `SalerID` | `INT` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` NN |  |
| `CreatedAt` | `DATETIME` NN |  |
| `LastModifiedBy` | `NVARCHAR(50)` NN |  |
| `LastModifiedAt` | `DATETIME` NN |  |
| `DeletedStatus` | `NVARCHAR(50)` nullable |  |
| `PrintStatus` | `INT` NN |  |
| `RecordStatus` | `INT` NN |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_AdminPermisionHDCN` | `AdminPermisionHDCNID` | PRIMARY KEY |
