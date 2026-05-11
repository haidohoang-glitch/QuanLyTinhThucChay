# Table: `ThucTreoHopDongChiTietTrinhDuyet_ThucTreo`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThucTreoHopDongChiTietTrinhDuyetID` | `INT` NN |  |
| `HopDongREF` | `INT` NN |  |
| `HopDongChiTietREF` | `INT` NN |  |
| `DmHinhThucQuangCaoREF` | `INT` NN |  |
| `DmSanPhamREF` | `INT` NN |  |
| `TenNhanHang` | `NVARCHAR(300)` nullable |  |
| `NhanHangREF` | `INT` NN |  |
| `DmWebsiteREF` | `INT` nullable |  |
| `TenWebsite` | `NVARCHAR(255)` nullable |  |
| `Soluong` | `DECIMAL(18,0)` nullable |  |
| `DmDonViTinhREF` | `INT` nullable |  |
| `DonViTinh` | `NVARCHAR(50)` nullable |  |
| `DonGia` | `DECIMAL(10,0)` nullable |  |
| `ChietKhau` | `FLOAT` nullable |  |
| `TongTien` | `FLOAT` nullable |  |
| `NgayBatDau` | `DATE` nullable |  |
| `NgayKetThuc` | `DATE` nullable |  |
| `TrangThai` | `SMALLINT` nullable |  |
| `IsLocked` | `SMALLINT` NN |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `SubmittedAt` | `DATETIME` nullable |  |
| `SubmittedBy` | `NVARCHAR(50)` nullable |  |
| `ApprovedAt` | `DATETIME` nullable |  |
| `ApprovedBy` | `NVARCHAR(50)` nullable |  |
| `Note` | `NVARCHAR(500)` nullable |  |
| `ThucChayHopDongChiTietREF` | `INT` NN |  |
| `DeletedStatus` | `SMALLINT` NN |  |
| `Linkbai` | `NVARCHAR(MAX)` nullable |  |
| `Lst_NhanVienSoYeuLyLichREF` | `NVARCHAR(100)` nullable |  |
| `id` | `INT` PK IDENTITY |  |
| `TenBanner` | `NVARCHAR(500)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo` | `id` | PRIMARY KEY |
