# Table: `NhanSuHopDongLaoDong`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `NhanSuHopDongLaoDongID` | `INT` PK |  |
| `TenNhanSu` | `NVARCHAR(200)` nullable |  |
| `MaNhanSu` | `NVARCHAR(200)` nullable |  |
| `NhanSuSoYeuLyLichREF` | `INT` nullable |  |
| `SoHopDongLaoDong` | `NVARCHAR(200)` nullable |  |
| `ThoiHanHopDongLaoDong` | `NVARCHAR(200)` nullable |  |
| `ThoiHanHopDongLaoDongREF` | `INT` nullable |  |
| `NgayBatDauLamViec` | `DATETIME` nullable |  |
| `NgayKetThucLamViec` | `DATETIME` nullable |  |
| `NgayKyHopDong` | `DATETIME` nullable |  |
| `DmHinhThucLaoDongREF` | `INT` nullable |  |
| `GhiChu` | `NVARCHAR(200)` nullable |  |
| `Active` | `BIGINT` nullable |  |
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
| `PK_NhanSuHopDongLaoDong` | `NhanSuHopDongLaoDongID` | PRIMARY KEY |
