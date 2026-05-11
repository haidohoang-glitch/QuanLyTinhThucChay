# Table: `DotChayChiTietHopDongChiTietLog`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DotChayChiTietHopDongChiTietLogID` | `INT` PK IDENTITY |  |
| `DotChayChiTietHopDongChiTietREF` | `INT` NN |  |
| `DotChayHopDongChitietREF` | `INT` NN |  |
| `BookingREF` | `INT` nullable |  |
| `SoLuong` | `FLOAT` nullable |  |
| `ThoiGianBatDau` | `DATETIME` nullable |  |
| `ThoiGianKetThuc` | `DATETIME` nullable |  |
| `VungMienID` | `INT` nullable |  |
| `TenVungMien` | `NVARCHAR(200)` nullable |  |
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
| `PK_DotChayChiTietHopDongChiTietLog` | `DotChayChiTietHopDongChiTietLogID` | PRIMARY KEY |
