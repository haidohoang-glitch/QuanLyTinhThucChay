# Table: `HopDongAttachFileBanCungLog`

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
| `ThoiGianLog` | `DATETIME` nullable |  |
| `NguoiLog` | `NVARCHAR(200)` nullable |  |
| `LoaiLog` | `INT` nullable |  |
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
| `PK_HopDongAttachFileBanCungLog` | `HopDongAttachFileBanCungID` | PRIMARY KEY |
