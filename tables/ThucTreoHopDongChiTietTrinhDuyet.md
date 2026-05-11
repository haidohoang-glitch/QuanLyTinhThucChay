# Table: `ThucTreoHopDongChiTietTrinhDuyet`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThucTreoHopDongChiTietTrinhDuyetID` | `INT` NN |  |
| `HopDongREF` | `INT` NN |  |
| `HopDongChiTietREF` | `INT` NN |  |
| `DmHinhThucQuangCaoREF` | `INT` NN | 'Hinh thuc quang cao id' |
| `DmSanPhamREF` | `INT` NN |  |
| `TenNhanHang` | `NVARCHAR(300)` DEFAULT NULL nullable | 'Ten nhan hang', |
| `NhanHangREF` | `INT` NN DEFAULT '0' |  |
| `DmWebsiteREF` | `INT` DEFAULT NULL nullable |  |
| `TenWebsite` | `NVARCHAR(255)` DEFAULT NULL nullable |  |
| `Soluong` | `DECIMAL(18,0)` DEFAULT NULL nullable | 'So luong treo', |
| `DmDonViTinhREF` | `INT` DEFAULT NULL nullable |  |
| `DonViTinh` | `NVARCHAR(50)` DEFAULT NULL nullable |  |
| `DonGia` | `DECIMAL(10,0)` DEFAULT NULL nullable |  |
| `ChietKhau` | `FLOAT` DEFAULT NULL nullable |  |
| `TongTien` | `FLOAT` DEFAULT NULL nullable | 'thanh tien sau chiet khau', |
| `NgayBatDau` | `DATE` DEFAULT NULL nullable | 'Thoi gian bat dau chay', |
| `NgayKetThuc` | `DATE` DEFAULT NULL nullable | 'thoi gian ket thuc', |
| `TrangThai` | `SMALLINT` DEFAULT NULL nullable | 'trang thai: 0 = luu nhap, 1 = trinh duyet, 2 = da duyet, 3 = tu choi', |
| `IsLocked` | `SMALLINT` NN DEFAULT '0' |  |
| `CreatedAt` | `DATETIME` DEFAULT NULL nullable |  |
| `CreatedBy` | `NVARCHAR(50)` DEFAULT NULL nullable |  |
| `LastModifiedAt` | `DATETIME` DEFAULT NULL nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` DEFAULT NULL nullable |  |
| `SubmittedAt` | `DATETIME` DEFAULT NULL nullable |  |
| `SubmittedBy` | `NVARCHAR(50)` DEFAULT NULL nullable |  |
| `ApprovedAt` | `DATETIME` DEFAULT NULL nullable |  |
| `ApprovedBy` | `NVARCHAR(50)` DEFAULT NULL nullable |  |
| `Note` | `NVARCHAR(500)` DEFAULT NULL nullable |  |
| `ThucChayHopDongChiTietREF` | `INT` NN DEFAULT '0' |  |
| `DeletedStatus` | `SMALLINT` NN DEFAULT '0' |  |
| `Linkbai` | `NVARCHAR(MAX)` nullable |  |
| `Lst_NhanVienSoYeuLyLichREF` | `NVARCHAR(100)` nullable |  |
| `id` | `INT` PK IDENTITY |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ThucTreoHopDongChiTietTrinhDuyet` | `id` | PRIMARY KEY |
