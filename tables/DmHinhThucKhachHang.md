# Table: `DmHinhThucKhachHang`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmHinhThucKhachHangID` | `INT` PK |  |
| `MaHinhThucKhachHang` | `NVARCHAR(50)` nullable |  |
| `TenHinhThucKhachHang` | `NVARCHAR(200)` nullable |  |
| `GhiChu` | `NVARCHAR(4000)` nullable |  |
| `Active` | `INT` NN |  |
| `CreatedBy` | `NVARCHAR(1)` NN |  |
| `CreatedAt` | `DATETIME` NN |  |
| `LastModifiedBy` | `NVARCHAR(1)` NN |  |
| `LastModifiedAt` | `DATETIME` NN |  |
| `DeletedStatus` | `INT` NN |  |
| `PrintStatus` | `INT` NN |  |
| `RecordStatus` | `INT` NN |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `csDmHinhThucKhachHang` | `DmHinhThucKhachHangID` | PRIMARY KEY |
