# Table: `HopDongHanThanhToan`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `HopDongHanThanhToanID` | `INT` PK |  |
| `HopDongREF` | `INT` NN |  |
| `LanThanhToan` | `INT` nullable |  |
| `NgayThanhToan` | `DATETIME` nullable |  |
| `SoTien` | `FLOAT` nullable |  |
| `NgayDuDinhThanhToan` | `DATETIME` nullable |  |
| `GiaTriDaThanhToan` | `FLOAT` nullable |  |
| `GhiChu` | `NVARCHAR(4000)` nullable |  |
| `Active` | `INT` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` NN |  |
| `PrintStatus` | `INT` NN |  |
| `RecordStatus` | `INT` NN |  |
| `NgayDuKienXuatHoaDon` | `DATETIME` nullable |  |
| `HinhThucThanhToan` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `csHopDongHanThanhToan` | `HopDongHanThanhToanID` | PRIMARY KEY |
