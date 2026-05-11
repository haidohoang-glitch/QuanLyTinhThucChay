# Table: `PhanQuyenNhanHang`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmPhanQuyenID` | `INT` PK IDENTITY |  |
| `DmNhanHangREF` | `INT` NN |  |
| `OxUserREF` | `INT` NN |  |
| `NhanSuREF` | `INT` nullable |  |
| `TenNhanSu` | `NVARCHAR(255)` nullable |  |
| `MaNhanSu` | `VARCHAR(50)` nullable |  |
| `TenPhongBan` | `NVARCHAR(255)` nullable |  |
| `TenBoPhan` | `NVARCHAR(255)` nullable |  |
| `TenNhom` | `NVARCHAR(255)` nullable |  |
| `ThoiGianHieuLuc` | `DATE` nullable |  |
| `ThoiGianHetHieuLuc` | `DATE` nullable |  |
| `KichHoat` | `BIT` NN DEFAULT 1 |  |
| `IsLockPermission` | `SMALLINT` NN DEFAULT 0 |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `IX_PhanQuyenNhanHang` | `DmPhanQuyenID` | BTREE |
| `PK_PhanQuyenNhanHang_1` | `DmPhanQuyenID` | PRIMARY KEY |
