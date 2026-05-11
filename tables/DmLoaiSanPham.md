# Table: `DmLoaiSanPham`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmLoaiSanPhamID` | `INT` PK |  |
| `TenLoaiSanPham` | `NVARCHAR(255)` nullable |  |
| `CreatedBy` | `NVARCHAR(255)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(255)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |
| `MaLoaiSanPham` | `NVARCHAR(200)` nullable |  |
| `GhiChu` | `NVARCHAR(200)` nullable |  |
| `DmHinhThucQuangCaoID` | `INT` nullable |  |
| `MaDmHinhThucQuangCao` | `NVARCHAR(200)` nullable |  |
| `TenHinhThucQuangCao` | `NVARCHAR(200)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `csDmLoaiSanPham` | `DmLoaiSanPhamID` | PRIMARY KEY |
