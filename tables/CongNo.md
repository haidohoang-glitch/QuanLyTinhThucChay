# Table: `CongNo`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `CongNoID` | `INT` PK |  |
| `HopDongREF` | `INT` NN |  |
| `SoHoaDon` | `INT` nullable |  |
| `NgayXuat` | `DATETIME` nullable |  |
| `GiaTri` | `FLOAT` nullable |  |
| `GiaTriThanhToan` | `FLOAT` nullable |  |
| `NgayThanhToan` | `DATETIME` nullable |  |
| `HanThanhToanID` | `INT` nullable |  |
| `NgayTraHoaDon` | `DATETIME` nullable |  |
| `IsSoPhieuThu` | `INT` nullable |  |
| `SoHoaDonGiamTru` | `INT` nullable |  |
| `SoBangThongKe` | `INT` nullable |  |
| `NgayChuyenChoKeToan` | `DATETIME` nullable |  |
| `Sign` | `INT` nullable |  |
| `PhieuThuLinkNapTien` | `NVARCHAR(50)` nullable |  |
| `TaiKhoanKhachHangREF` | `INT` nullable |  |
| `GhiChu` | `NVARCHAR(4000)` nullable |  |
| `Active` | `INT` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` NN |  |
| `PrintStatus` | `INT` NN |  |
| `RecordStatus` | `INT` NN |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `csCongNo` | `CongNoID` | PRIMARY KEY |
