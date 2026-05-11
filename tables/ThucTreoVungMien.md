# Table: `ThucTreoVungMien`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThucTreoVungMienID` | `INT` PK |  |
| `VungMienID` | `INT` NN |  |
| `BookingREF` | `INT` nullable |  |
| `SoLuong` | `INT` nullable |  |
| `DonViTinhREF` | `INT` nullable |  |
| `ThoiGianBatDau` | `DATETIME` nullable |  |
| `ThoiGianKetThuc` | `DATETIME` nullable |  |
| `DmBannerREF` | `INT` nullable |  |
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
| `PK_ThucTreoVungMien` | `ThucTreoVungMienID` | PRIMARY KEY |
