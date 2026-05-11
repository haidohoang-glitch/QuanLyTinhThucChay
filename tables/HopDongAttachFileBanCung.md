# Table: `HopDongAttachFileBanCung`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `HopDongAttachFileBanCungID` | `INT` PK |  |
| `HopDongAttachFileREF` | `INT` nullable |  |
| `HopDongREF` | `INT` nullable |  |
| `NgayNhanBanCung` | `DATETIME` nullable |  |
| `NgayNhanBanFax` | `DATETIME` nullable |  |
| `NgayChuyenChoKeToan` | `DATETIME` nullable |  |
| `KhongTheNhapBanCung` | `INT` nullable |  |
| `GhiChu` | `NVARCHAR(200)` nullable |  |
| `CreatedBy` | `NVARCHAR(200)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(200)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |
| `CanLayBangKeThucChayYN` | `SMALLINT` nullable |  |
| `NgayHenTraBanCung` | `DATETIME` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_HopDongAttachFileBanCung` | `HopDongAttachFileBanCungID` | PRIMARY KEY |
