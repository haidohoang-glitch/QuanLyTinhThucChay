# Table: `ThongTinHoaDonLog`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThongTinHoaDonLogID` | `INT` PK |  |
| `ThongTinHoaDonREF` | `INT` nullable |  |
| `HopDongREF` | `INT` nullable |  |
| `SoHoaDon` | `NVARCHAR(200)` nullable |  |
| `NgayXuatHoaDon` | `DATETIME` nullable |  |
| `GiaTri` | `FLOAT` nullable |  |
| `NgayTraHoaDon` | `DATETIME` nullable |  |
| `SoBangThongKe` | `NVARCHAR(200)` nullable |  |
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
| `PK_ThongTinHoaDonLog` | `ThongTinHoaDonLogID` | PRIMARY KEY |
