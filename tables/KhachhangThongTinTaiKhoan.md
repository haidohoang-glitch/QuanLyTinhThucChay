# Table: `KhachhangThongTinTaiKhoan`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `KhachHangThongTinTaiKhoanID` | `BIGINT` PK |  |
| `KhachHangThongTinChungREF` | `BIGINT` NN |  |
| `SoTaiKhoan` | `NVARCHAR(200)` nullable |  |
| `NganHangREF` | `INT` nullable |  |
| `TenNganHang` | `NVARCHAR(200)` nullable |  |
| `MoTaiChiNhanh` | `NVARCHAR(200)` nullable |  |
| `GhiChu` | `NVARCHAR(200)` nullable |  |
| `CreatedBy` | `NVARCHAR(200)` NN |  |
| `CreatedAt` | `DATETIME` NN |  |
| `LastModifiedBy` | `NVARCHAR(200)` NN |  |
| `LastModifiedAt` | `DATETIME` NN |  |
| `DeletedStatus` | `INT` NN |  |
| `PrintStatus` | `INT` NN |  |
| `RecordStatus` | `INT` NN |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_KhachhangThongTinTaiKhoan` | `KhachHangThongTinTaiKhoanID` | PRIMARY KEY |
