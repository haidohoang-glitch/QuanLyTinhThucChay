# Table: `ThongTinHoaDon`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThongTinHoaDonID` | `INT` PK |  |
| `HopDongREF` | `INT` nullable |  |
| `SoHoaDon` | `NVARCHAR(200)` nullable |  |
| `NgayXuatHoaDon` | `DATETIME` nullable |  |
| `GiaTri` | `FLOAT` nullable |  |
| `NgayTraHoaDon` | `DATETIME` nullable |  |
| `SoBangThongKe` | `NVARCHAR(200)` nullable |  |
| `TaiKhoanKhachHang` | `NVARCHAR(200)` nullable |  |
| `GhiChu` | `NVARCHAR(2000)` nullable |  |
| `CreatedBy` | `NVARCHAR(200)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(200)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |
| `PrintStatus` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ThongTinHoaDon` | `ThongTinHoaDonID` | PRIMARY KEY |
