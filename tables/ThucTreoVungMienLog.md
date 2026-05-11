# Table: `ThucTreoVungMienLog`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThucTreoVungMienLogID` | `INT` PK |  |
| `VungMienID` | `INT` NN |  |
| `BookingREF` | `INT` nullable |  |
| `SoLuong` | `INT` nullable |  |
| `DonViTinhREF` | `INT` nullable |  |
| `ThoiGianBatDau` | `DATETIME` nullable |  |
| `ThoiGianKetThuc` | `DATETIME` nullable |  |
| `DmBannerREF` | `INT` nullable |  |
| `DotChayChiTietREF` | `INT` nullable |  |
| `CreatedBy` | `NVARCHAR(200)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(200)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecodStatus` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ThucTreoVungMienLog` | `ThucTreoVungMienLogID` | PRIMARY KEY |
