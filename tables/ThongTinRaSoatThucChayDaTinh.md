# Table: `ThongTinRaSoatThucChayDaTinh`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ID` | `INT` NN IDENTITY |  |
| `NgayThucHien` | `DATETIME` nullable |  |
| `SoHopDong` | `NVARCHAR(50)` nullable |  |
| `HopDongID` | `INT` nullable |  |
| `DmKhachHangID` | `INT` nullable |  |
| `DmNhanVienID` | `INT` nullable |  |
| `HopDongChiTietID` | `INT` nullable |  |
| `LsDmNhanHangID` | `NVARCHAR(200)` nullable |  |
| `DmHinhThucQuangCaoID` | `INT` nullable |  |
| `DmSanPhamID` | `INT` nullable |  |
| `lsDmNhomWebsiteTagID` | `NVARCHAR(500)` nullable |  |
| `DmWebsiteID` | `INT` nullable |  |
| `DmChuyenMucID` | `INT` nullable |  |
| `DmBannerID` | `INT` nullable |  |
| `DmLoaiBannerID` | `INT` nullable |  |
| `DmLoaiNenTangID` | `INT` nullable |  |
| `DonGia` | `INT` nullable |  |
| `SoLuong` | `INT` nullable |  |
| `DonViTinhID` | `INT` nullable |  |
| `Chietkhau` | `INT` nullable |  |
| `ThanhTien` | `BIGINT` nullable |  |
| `DonGiaThucChay` | `INT` nullable |  |
| `SoLuongThucChay` | `INT` nullable |  |
| `DonViTinh` | `NVARCHAR(50)` nullable |  |
| `ThanhTienThucChaySauChietKhau` | `BIGINT` nullable |  |
| `DmLoaiVanDeID` | `INT` nullable |  |
| `TenLoaiVanDe` | `NVARCHAR(300)` nullable |  |
| `DoiTuongLoi` | `NVARCHAR(200)` nullable |  |
| `DanhSachID` | `NVARCHAR(300)` nullable |  |
| `DoiTuongXuLy` | `NVARCHAR(500)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `TrangThaiXuLy` | `INT` nullable | 0: Chua xu ly; 1 Da xu ly; 2 pending |
