# Table: `DotChayHopDongChiTietLog`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DotChayHopDongChiTietLogID` | `BIGINT` PK IDENTITY |  |
| `DotChayHopDongChiTietID` | `BIGINT` NN |  |
| `ViTri` | `NVARCHAR(200)` nullable |  |
| `TenWebsite` | `NVARCHAR(200)` nullable |  |
| `HopDongREF` | `BIGINT` NN |  |
| `HopDongChiTietREF` | `BIGINT` NN |  |
| `ThoiGianBatDau` | `DATETIME` NN |  |
| `ThoiGianKetThuc` | `DATETIME` NN |  |
| `ThoiGianBatDauBooking` | `DATETIME` nullable |  |
| `ThoiGianKetThucBooking` | `DATETIME` nullable |  |
| `GhiChu` | `NVARCHAR(200)` nullable |  |
| `BookingREF` | `BIGINT` nullable |  |
| `IsWarning` | `INT` nullable |  |
| `DmBannerREF` | `NVARCHAR(200)` nullable |  |
| `TenBanner` | `NVARCHAR(200)` nullable |  |
| `TypeAdd` | `INT` nullable |  |
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
| `PK_DotChayHopDongChiTietLog` | `DotChayHopDongChiTietLogID` | PRIMARY KEY |
