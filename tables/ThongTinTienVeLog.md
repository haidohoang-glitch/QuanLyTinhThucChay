# Table: `ThongTinTienVeLog`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThongTinTienVeLogID` | `INT` PK |  |
| `ThongTinTienVeREF` | `INT` nullable |  |
| `HopDongREF` | `INT` nullable |  |
| `NgayThanhToan` | `DATETIME` nullable |  |
| `IsPhieuThu` | `INT` nullable |  |
| `PhieuThuLinkNapTien` | `NVARCHAR(200)` nullable |  |
| `GiaTri` | `FLOAT` nullable |  |
| `TaiKhoanKhachHang` | `NVARCHAR(200)` nullable |  |
| `ThoiGianLog` | `DATETIME` nullable |  |
| `NguoiLog` | `NVARCHAR(200)` nullable |  |
| `LoaiLog` | `INT` nullable |  |
| `GhiChu` | `NVARCHAR(200)` nullable |  |
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
| `PK_ThongTinTienVeLog` | `ThongTinTienVeLogID` | PRIMARY KEY |
