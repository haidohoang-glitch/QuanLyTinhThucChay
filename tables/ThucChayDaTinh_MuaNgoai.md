# Table: `ThucChayDaTinh_MuaNgoai`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ID` | `BIGINT` PK IDENTITY |  |
| `HopDongREF` | `INT` NN |  |
| `SoHopDong` | `NVARCHAR(50)` NN |  |
| `DmMaHopDongREF` | `INT` NN |  |
| `NgayDanhSoHopDong` | `DATETIME` NN |  |
| `TrangThaiHopDong` | `INT` NN |  |
| `DmNhanVienREF` | `INT` NN |  |
| `TenDangNhap` | `NVARCHAR(25)` NN |  |
| `DmPhongBanREF` | `INT` NN |  |
| `DmBoPhanREF` | `INT` NN |  |
| `DmNhomLamViecREF` | `INT` NN |  |
| `DmDiaDiemLamViecREF` | `INT` NN |  |
| `DmKhachHangREF` | `INT` NN |  |
| `HopDongChiTietREF` | `INT` nullable |  |
| `LstDmNhanHangREF` | `NVARCHAR(255)` nullable |  |
| `LstDmNhomNganhREF` | `NVARCHAR(250)` nullable |  |
| `DmHinhThucQuangCaoREF` | `INT` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `DmChuyenMucREF` | `INT` nullable |  |
| `DmLoaiBannerREF` | `INT` nullable |  |
| `DmViTriREF` | `INT` nullable |  |
| `SoLuong` | `INT` nullable |  |
| `DonViTinhREF` | `INT` nullable |  |
| `DonGia` | `FLOAT` nullable |  |
| `ChietKhau` | `FLOAT` nullable |  |
| `ThanhTien` | `FLOAT` nullable |  |
| `IsKhuyenMai` | `INT` nullable |  |
| `KhuyenMai` | `NVARCHAR(250)` nullable |  |
| `ThucChayMuaNgoaiChiTietREF` | `INT` nullable |  |
| `TongTienDuToanMuaSauCK` | `FLOAT` nullable |  |
| `TongTienDuToanLaiMuaSauCK` | `FLOAT` nullable |  |
| `ChietKhauMua` | `FLOAT` nullable |  |
| `DmBannerREF` | `INT` nullable |  |
| `DmChienDichREF` | `INT` nullable |  |
| `DmWebsiteREF` | `INT` nullable |  |
| `TenWebsite` | `NVARCHAR(255)` nullable |  |
| `NgayThucHien` | `DATETIME` nullable |  |
| `NgayBatDau` | `DATETIME` nullable |  |
| `NgayKetThuc` | `DATETIME` nullable |  |
| `DonViTinhThucChay` | `NVARCHAR(255)` nullable |  |
| `DonGiaTheoDonViTinhTC` | `FLOAT` nullable |  |
| `TongViewClickThucChay` | `FLOAT` nullable |  |
| `TongSoBaiVietChiPhiThucChay` | `FLOAT` nullable |  |
| `SoLuongThucChay` | `FLOAT` nullable |  |
| `TongThanhTienThucChayBanSauCK` | `FLOAT` nullable |  |
| `TongThanhTienThucChayMuaSauCK` | `FLOAT` nullable |  |
| `ThanhTienLaiThucChaySauCK` | `FLOAT` nullable |  |
| `ThanhTienLaiThucChayKM` | `FLOAT` nullable |  |
| `SoLuongThucChayKM` | `INT` nullable |  |
| `SoLuongThucChayLechTreoHa` | `INT` nullable |  |
| `ThanhTienLechTreoHa` | `FLOAT` nullable |  |
| `GiaTriThayDoiLaiSauCK` | `FLOAT` nullable |  |
| `SoLuongThayDoi` | `INT` NN |  |
| `SoLuongKMThayDoi` | `INT` NN |  |
| `GiaTriKMLaiThayDoi` | `FLOAT` NN |  |
| `GhiChu` | `NVARCHAR(MAX)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ID` | `ID` | PRIMARY KEY |
