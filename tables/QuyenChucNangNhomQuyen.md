# Table: `QuyenChucNangNhomQuyen`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `QuyenChucNangNhomQuyenID` | `BIGINT` PK IDENTITY |  |
| `DmNhomNguoiDungREF` | `INT` NN |  |
| `TenNhomNguoiDung` | `NVARCHAR(200)` nullable |  |
| `DmChucNangREF` | `INT` nullable |  |
| `TenChucNang` | `NVARCHAR(200)` nullable |  |
| `GhiChu` | `NVARCHAR(200)` nullable |  |
| `CreatedBy` | `NVARCHAR(200)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(200)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_QuyenChucNangNhomQuyen` | `QuyenChucNangNhomQuyenID` | PRIMARY KEY |
