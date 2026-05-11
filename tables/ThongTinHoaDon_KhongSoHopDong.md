# Table: `ThongTinHoaDon_KhongSoHopDong`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThongTinHoaDon_KhongSoHopDongID` | `INT` PK |  |
| `HopDongREF` | `INT` nullable |  |
| `SoHoaDon` | `NVARCHAR(200)` nullable |  |
| `NgayXuatHoaDon` | `DATETIME` nullable |  |
| `GiaTri` | `FLOAT` nullable |  |
| `NgayTraHoaDon` | `DATETIME` nullable |  |
| `SoBangThongKe` | `NVARCHAR(200)` nullable |  |
| `TaiKhoanKhachHang` | `NVARCHAR(200)` nullable |  |
| `IsDoanhThuKhac` | `INT` nullable |  |
| `IsHoaDonGiamTru` | `INT` nullable |  |
| `GhiChu` | `NVARCHAR(200)` nullable |  |
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
| `PK_ThongTinHoaDon_KhongSoHopDong` | `ThongTinHoaDon_KhongSoHopDongID` | PRIMARY KEY |
