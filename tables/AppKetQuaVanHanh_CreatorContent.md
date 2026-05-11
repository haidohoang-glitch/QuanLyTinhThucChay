# Table: `AppKetQuaVanHanh_CreatorContent`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `Id` | `INT` PK IDENTITY |  |
| `AppKetQuaVanHanh_CreatorContent_id` | `INT` NN |  |
| `HopDongBanRef` | `INT` nullable |  |
| `PhanBoRef` | `INT` nullable |  |
| `PbSoLuong` | `INT` nullable |  |
| `pbDonGia` | `DECIMAL(18,2)` nullable |  |
| `PbChietKhau` | `DECIMAL(18,2)` nullable |  |
| `PbThanhTien` | `DECIMAL(18,2)` nullable |  |
| `NgayThucHien` | `DATETIME` nullable |  |
| `Link` | `NVARCHAR(2500)` nullable |  |
| `TcDonGia` | `FLOAT` nullable |  |
| `TcSoLuong` | `INT` nullable |  |
| `TcDonViTinhREF` | `INT` nullable |  |
| `DonViTinh` | `NVARCHAR(100)` nullable |  |
| `TcThanhTien` | `DECIMAL(18,2)` nullable |  |
| `AppPageKolRef` | `INT` nullable |  |
| `AppHangMucRef` | `INT` nullable |  |
| `AppHopDongKolRef` | `INT` nullable |  |
| `DonGia` | `DECIMAL(18,2)` nullable |  |
| `ChietKhau` | `DECIMAL(18,2)` nullable |  |
| `ThanhTien` | `DECIMAL(18,2)` nullable |  |
| `VAT` | `DECIMAL(8,2)` nullable |  |
| `TienThanhToan` | `DECIMAL(18,2)` nullable |  |
| `LaiLo` | `DECIMAL(18,2)` nullable |  |
| `TrangThai` | `TINYINT` nullable | 1- Mới
2- Gửi duyệt (gửi leader duyệt)
3- Duyệt KQVH (leader duyệt)
4- Từ chối duyệt TC
5- Gửi duyệt TT: Gửi kế toán duyệt TT
6- Duyệt TT: Kế toán duyệt TT
7- Từ chối duyệt TT |
| `NguoiDuyet` | `INT` nullable |  |
| `NguoiDuyetTen` | `NVARCHAR(250)` nullable |  |
| `NgayDuyet` | `DATETIME` nullable |  |
| `NguoiDuyetTT` | `INT` nullable |  |
| `NguoiDuyetTTTen` | `NVARCHAR(250)` nullable |  |
| `NgayDuyetTT` | `DATETIME` nullable |  |
| `NguoiTuChoi` | `INT` nullable |  |
| `NguoiTuChoiTen` | `NVARCHAR(250)` nullable |  |
| `NgayTuChoi` | `DATETIME` nullable |  |
| `LyDoTuChoi` | `NVARCHAR(500)` nullable |  |
| `NguoiTuChoiTT` | `INT` nullable |  |
| `NguoiTuChoiTTTen` | `NVARCHAR(250)` nullable |  |
| `NgayTuChoiTT` | `DATETIME` nullable |  |
| `LyDoTuChoiTT` | `NVARCHAR(500)` nullable |  |
| `CreationTime` | `DATETIME2` nullable |  |
| `CreatorUserId` | `BIGINT` nullable |  |
| `CreatedBy` | `NVARCHAR(100)` nullable |  |
| `LastModificationTime` | `DATETIME2` nullable |  |
| `LastModifierUserId` | `BIGINT` nullable |  |
| `LastModifiedBy` | `NVARCHAR(100)` nullable |  |
| `DeletionTime` | `DATETIME2` nullable |  |
| `DeleterUserId` | `BIGINT` nullable |  |
| `IsDeleted` | `BIT` nullable |  |
| `NgayGuiDuyet` | `DATETIME` nullable |  |
| `NguoiGuiDuyet` | `INT` nullable |  |
| `NguoiGuiDuyetTen` | `NVARCHAR(250)` nullable |  |
| `NgayGuiDuyetTT` | `DATETIME` nullable |  |
| `NguoiGuiDuyetTT` | `INT` nullable |  |
| `NguoiGuiDuyetTTTen` | `NVARCHAR(250)` nullable |  |
| `RecordStatus` | `SMALLINT` nullable |  |
| `ThanhTienSauChietKhauThucChay` | `FLOAT` nullable |  |
| `NgayGhiNhanThucChay` | `DATETIME` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_AppKetQuaVanHanh_CreatorContent` | `Id` | PRIMARY KEY |
