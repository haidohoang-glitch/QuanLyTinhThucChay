# Table: `ThucChay_LogNNTinhGiaTriThayDoi`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThuChay_LogNNTinhGiaTriThayDoiID` | `NVARCHAR(50)` PK |  |
| `HopDongREF` | `INT` NN |  |
| `SoHopDong` | `NVARCHAR(50)` NN |  |
| `HopDongChiTietREF` | `INT` NN |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `DmWebsiteREF` | `INT` nullable |  |
| `NgayThucHien` | `DATETIME` NN |  |
| `GiaTriThayDoi` | `FLOAT` NN |  |
| `GiaSauCK1` | `FLOAT` nullable |  |
| `Soluong1` | `INT` nullable |  |
| `GiaSauCK2` | `FLOAT` nullable |  |
| `Soluong2` | `INT` nullable |  |
| `NoiDungLog` | `NVARCHAR(MAX)` nullable |  |
| `NguonLog` | `NVARCHAR(200)` nullable |  |
| `GhiChu` | `NVARCHAR(500)` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `NgayThucHien_IDX` | `NgayThucHien` | BTREE |
| `PK_ThuChay_LogNNTinhGiaTriThayDoi` | `ThuChay_LogNNTinhGiaTriThayDoiID` | PRIMARY KEY |
