# Table: `DmLoaiSanPhamDetail`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmLoaiSanPhamDetailId` | `INT` PK |  |
| `DmLoaiSanPhamFK` | `INT` NN |  |
| `DmSanPhamFK` | `INT` NN |  |
| `DmSanPhamName` | `NVARCHAR(250)` nullable |  |
| `DmLoaiSanPhamName` | `NVARCHAR(250)` nullable |  |
| `IsDeleted` | `BIT` nullable |  |
| `LastModifiedBy` | `NVARCHAR(250)` NN |  |
| `LastModifiedAt` | `DATETIME` NN |  |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |
| `CreatedBy` | `NVARCHAR(200)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_DmLoaiSanPhamDetail` | `DmLoaiSanPhamDetailId` | PRIMARY KEY |
