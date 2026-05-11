# Table: `NhanSuQuyenNguoiDung`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `NhanSuQuyenNguoiDungID` | `INT` PK |  |
| `NhanSuSoYeuLyLichREF` | `INT` nullable |  |
| `DmNhomNguoiDungREF` | `INT` nullable |  |
| `UserName` | `NVARCHAR(200)` nullable |  |
| `OxUserREF` | `BIGINT` nullable |  |
| `LastLogInTime` | `DATETIME` nullable |  |
| `KhoaDangNhapNguoiDung` | `INT` nullable |  |
| `CreatedBy` | `NVARCHAR(200)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(200)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `BIGINT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_NhanSuQuyenNguoiDung` | `NhanSuQuyenNguoiDungID` | PRIMARY KEY |
