# Table: `ThucChayHopDongChiTietPRLog`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThucChayHopDongChiTietPRLogID` | `BIGINT` PK IDENTITY |  |
| `ThucChayHopDongChiTietPRREF` | `INT` NN |  |
| `HopDongREF` | `BIGINT` NN |  |
| `HopDongChiTietREF` | `BIGINT` nullable |  |
| `DmWebsiteREF` | `INT` nullable |  |
| `TenWebsite` | `NVARCHAR(200)` nullable |  |
| `DmChuyenMucREF` | `INT` nullable |  |
| `TenChuyenMuc` | `NVARCHAR(200)` nullable |  |
| `TieuDiem` | `INT` nullable |  |
| `DmNhanHangREF` | `NVARCHAR(200)` nullable |  |
| `NhanHang` | `NVARCHAR(200)` nullable |  |
| `KhuyenMai` | `INT` nullable |  |
| `GiaTien` | `BIGINT` nullable |  |
| `ThoiGianBatDau` | `DATETIME` nullable |  |
| `Link` | `NVARCHAR(2000)` nullable |  |
| `GhiChu` | `NVARCHAR(200)` nullable |  |
| `DmHinhThucQuangCaoREF` | `INT` nullable |  |
| `TenHinhThucQuangCao` | `NVARCHAR(200)` nullable |  |
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
| `SoLuong` | `INT` nullable |  |
| `ChietKhau` | `FLOAT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ThucChayHopDongChiTietPRLog` | `ThucChayHopDongChiTietPRLogID` | PRIMARY KEY |
