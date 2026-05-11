# Table: `DotChayHopDongChiTiet`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DotChayHopDongChiTietID` | `BIGINT` PK | ID Primary key của table DotChayHopDongChiTiet |
| `ViTri` | `NVARCHAR(200)` nullable |  |
| `TenWebsite` | `NVARCHAR(200)` nullable | Tên website từ table DmWebsite |
| `HopDongREF` | `BIGINT` nullable | ID Foreign key từ table HopDong (HopdongID) |
| `HopDongChiTietREF` | `BIGINT` nullable | ID Foreign key từ table HopDongChiTiet (HopDongChiTietID) |
| `ThoiGianBatDau` | `DATETIME` nullable | Ngày bắt đầu của đợt chạy |
| `ThoiGianKetThuc` | `DATETIME` nullable | Ngày kết thúc của đợt chạy |
| `ThoiGianBatDauBooking` | `DATETIME` nullable |  |
| `ThoiGianKetThucBooking` | `DATETIME` nullable |  |
| `GhiChu` | `NVARCHAR(200)` nullable |  |
| `BookingREF` | `BIGINT` nullable | ID Booking của đợt chạy |
| `IsWarning` | `INT` nullable |  |
| `DmBannerREF` | `NVARCHAR(200)` nullable | ID Banner của đợt chạy |
| `TenBanner` | `NVARCHAR(200)` nullable | Tên banner của đợt chạy |
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
| `hopdongchitietREF` | `HopDongChiTietREF` | BTREE |
| `PK_DotChayHopDongChiTiet` | `DotChayHopDongChiTietID` | PRIMARY KEY |
