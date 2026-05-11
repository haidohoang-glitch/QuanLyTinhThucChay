# Table: `ThucChayHopDongChiTietPR_ThucTreo`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThucChayHopDongChiTietPRID` | `INT` PK |  |
| `HopDongREF` | `INT` nullable |  |
| `HopDongChiTietREF` | `INT` nullable |  |
| `NhanHang` | `NVARCHAR(255)` nullable |  |
| `TenWebsite` | `NVARCHAR(255)` nullable |  |
| `ChuyenMuc` | `NVARCHAR(255)` nullable |  |
| `TieuDiem` | `TINYINT` nullable |  |
| `KhuyenMai` | `TINYINT` nullable |  |
| `GiaTien` | `BIGINT` nullable |  |
| `ThoiGianBatDau` | `DATETIME` nullable |  |
| `Link` | `NVARCHAR(MAX)` nullable |  |
| `GhiChu` | `NVARCHAR(255)` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` NN |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` NN |  |
| `DeletedStatus` | `INT` NN |  |
| `PrintStatus` | `INT` NN |  |
| `RecordStatus` | `INT` NN |  |
| `DmWebsiteREF` | `INT` nullable |  |
| `DmChuyenMucREF` | `INT` nullable |  |
| `TenChuyenMuc` | `NVARCHAR(200)` nullable |  |
| `DmNhanHangREF` | `INT` nullable |  |
| `DmHinhThucQuangCaoREF` | `INT` nullable |  |
| `TenHinhThucQuangCao` | `NVARCHAR(200)` nullable |  |
| `MaLinkBai` | `VARCHAR(50)` nullable |  |
| `SoHopDong` | `VARCHAR(50)` nullable |  |
| `SoLuong` | `INT` nullable |  |
| `ChietKhau` | `FLOAT` nullable |  |
| `DmViTriREF` | `INT` nullable |  |
| `TenViTri` | `NVARCHAR(200)` nullable |  |
| `ThucChayHopDongChiTietPrREF` | `INT` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `DmDonViTinhREF` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `csThucChayHopDongChiTietPR_ThucTreo` | `ThucChayHopDongChiTietPRID` | PRIMARY KEY |
