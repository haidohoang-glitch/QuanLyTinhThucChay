# Table: `ThongTinTienVe`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThongTinTienVeID` | `INT` PK |  |
| `HopDongREF` | `INT` nullable |  |
| `NgayThanhToan` | `DATETIME` nullable |  |
| `IsPhieuThu` | `INT` nullable |  |
| `PhieuThuLinkNapTien` | `NVARCHAR(500)` nullable |  |
| `GiaTri` | `FLOAT` nullable |  |
| `TaiKhoanKhachHang` | `NVARCHAR(200)` nullable |  |
| `GhiChu` | `NVARCHAR(500)` nullable |  |
| `CreatedBy` | `NVARCHAR(200)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(200)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `GiaTriDatCoc` | `BIGINT` nullable |  |
| `Deleted` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `nonix_tttv_delstats` | `DeletedStatus` | BTREE |
| `PK_ThongTinTienVe` | `ThongTinTienVeID` | PRIMARY KEY |
