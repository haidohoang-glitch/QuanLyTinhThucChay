# Table: `DotChayHopDongChiTietThayDoi`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DotChayHopDongChiTietThayDoiID` | `INT` PK | ID của table DotChayHopDongChiTietThayDoi |
| `ViTri` | `NVARCHAR(255)` nullable | Tên vị trí |
| `TenWebsite` | `NVARCHAR(100)` nullable | Tên website |
| `HopDongREF` | `INT` nullable | ID Foreign key từ table HopDong (HopDongID) |
| `HopDongThayDoiREF` | `INT` nullable | ID Foreign key từ table HopDongThayDoi (HopDongThayDoiID) |
| `HopDongChiTietREF` | `INT` nullable | ID Foreign key từ table HopDongChiTiet (HopDongChiTietID) |
| `ThoiGianBatDau` | `DATETIME` nullable | Ngày bắt đầu của đợt chạy |
| `ThoiGianKetThuc` | `DATETIME` nullable | Ngày kết thúc của đợt chạy |
| `ThoiGianBatDauBooking` | `DATETIME` nullable |  |
| `ThoiGianKetThucBooking` | `DATETIME` nullable |  |
| `GhiChu` | `NVARCHAR(250)` nullable |  |
| `TenBanner` | `NVARCHAR(250)` nullable |  |
| `DmBannerREF` | `NVARCHAR(250)` nullable |  |
| `BookingREF` | `INT` nullable | ID Booking |
| `IsWarning` | `INT` nullable |  |
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
| `PK_DotChayHopDongChiTietThayDoi` | `DotChayHopDongChiTietThayDoiID` | PRIMARY KEY |
