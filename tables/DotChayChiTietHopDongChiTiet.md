# Table: `DotChayChiTietHopDongChiTiet`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DotChayChiTietHopDongChiTietID` | `INT` PK | ID primary key của table DotChayHopDongChiTietThayDoi |
| `DotChayHopDongChitietREF` | `INT` NN | ID Foreign key từ table DotChayHopDongChiTiet (DotChayHopDongChiTietID) |
| `BookingREF` | `INT` NN | ID Của Booking |
| `SoLuong` | `FLOAT` nullable | Số lượng đợt chạy  |
| `ThoiGianBatDau` | `DATETIME` nullable | Ngày bắt đầu |
| `ThoiGianKetThuc` | `DATETIME` nullable | Ngày kết thúc |
| `VungMienID` | `INT` nullable | ID Vùng miền từ table VungMien |
| `TenVungMien` | `NVARCHAR(200)` nullable | Tên vùng miền từ table VungMien |
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
| `PK_DotChayChiTietHopDongChiTiet` | `DotChayChiTietHopDongChiTietID` | PRIMARY KEY |
