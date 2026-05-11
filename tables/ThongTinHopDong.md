# Table: `ThongTinHopDong`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `SoHopDong` | `NVARCHAR(50)` nullable |  |
| `TenMaHopDong` | `NVARCHAR(50)` nullable |  |
| `HopDongID` | `INT` NN |  |
| `DmKhachHangREF` | `INT` nullable |  |
| `TenKhachHang` | `NVARCHAR(255)` nullable |  |
| `SysNhanVienREF` | `INT` nullable |  |
| `TenDangNhap` | `NVARCHAR(25)` nullable |  |
| `TenNhanVien` | `NVARCHAR(100)` nullable |  |
| `HopDongChiTietID` | `INT` NN |  |
| `DmLoaiREF` | `INT` nullable |  |
| `TenLoai` | `NVARCHAR(250)` nullable |  |
| `DmLoaiBannerREF` | `INT` nullable |  |
| `TenLoaiBanner` | `NVARCHAR(250)` nullable |  |
| `DmWebsiteREF` | `INT` nullable |  |
| `TenWebsite` | `NVARCHAR(100)` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(500)` nullable |  |
| `TrangThaiHopDong` | `INT` nullable |  |
| `DeletedStatus` | `INT` NN |  |
| `ThanhTien` | `FLOAT` NN |  |
