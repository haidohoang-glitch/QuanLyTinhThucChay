# Table: `ThucChayDaTinh`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThucChayDaTinhID` | `NVARCHAR(50)` PK | ID Primary key của table ThucChayDaTinh |
| `HopDongID` | `INT` NN | ID Foreign key từ table HopDong (HopDongID) |
| `SoHopDong` | `NVARCHAR(50)` NN | Số hợp đồng từ table HopDong(SoHopDong) |
| `DmMaHopDongREF` | `INT` NN | DmMaHopDongREF từ table HopDong (DmMaHopDongREF) |
| `TenMaHopDong` | `NVARCHAR(50)` NN | TenMaHopDong từ table HopDong |
| `NgayDanhSoHopDong` | `DATETIME` NN | NgayDanhSoHopDong từ table HopDong |
| `NgayKyHopDong` | `DATETIME` NN | NgayKyHopDong từ table HopDong |
| `NhanHopDong` | `NVARCHAR(1000)` nullable | NhanHopDong từ table HopDong |
| `NgayNhanBanFax` | `DATETIME` nullable | NgayNhanBanFax từ table HopDong |
| `NgayNhanHopDongBanCung` | `DATETIME` nullable | NgayNhanBanCung từ table HopDong |
| `NgayChuyenHopDongChoKeToan` | `DATETIME` nullable | NgayChuyenHopDongChoKeToan từ table HopDong |
| `So` | `NVARCHAR(50)` nullable | So từ table HopDong |
| `Thang` | `INT` NN | Thang từ table HopDong |
| `Nam` | `INT` NN | Nam từ table HopDong |
| `GiaTriHopDong` | `FLOAT` nullable | GiaTriHopDong từ table HopDong |
| `CongNo` | `FLOAT` NN | CongNo từ table HopDong |
| `HopDongChiTietREF` | `INT` nullable | ID Foreign key từ table HopDongChiTiet (HopDongChiTietID) |
| `DangSuDung` | `INT` NN | DangSuDung từ table HopDong |
| `IsGiayPhep` | `INT` NN | IsGiayPhep từ table HopDong |
| `TrangThaiHopDong` | `INT` NN | TrangThaiHopDong từ table HopDong |
| `IsBanCung` | `INT` NN | IsBanCung từ table HopDong |
| `DmPhongBanREF` | `INT` NN | DmPhongBanREF từ table HopDong |
| `TenPhongBan` | `NVARCHAR(50)` NN | TenPhongBan từ table HopDong |
| `DmBoPhanREF` | `INT` NN | DmBoPhan từ table HopDong |
| `TenBoPhan` | `NVARCHAR(50)` NN | TenBoPhan từ table HopDong |
| `DmNhomLamViecREF` | `INT` NN | DmNhomLamViecREF từ table HopDong |
| `TenNhomLamViec` | `NVARCHAR(50)` NN | TenNhomLamViec từ table HopDong |
| `DmDiaDiemLamViecREF` | `INT` NN | DmDiaDiemLamViecREF từ table HopDong |
| `TenDiaDiemLamViec` | `NVARCHAR(250)` NN | TenDiaDiemLamViec từ table HopDong |
| `SysNhanVienREF` | `INT` NN | SysNhanVienREF từ table HopDong |
| `TenDangNhap` | `NVARCHAR(25)` NN | TenDangNhap từ table HopDong |
| `TenNhanVien` | `NVARCHAR(100)` NN | TenNhanVien từ table HopDong |
| `TenKhachHang` | `NVARCHAR(255)` NN | TenKhachHang từ table HopDong |
| `NhanHang` | `NVARCHAR(255)` nullable | Chưa thông tin ID nhãn hang (NhanHangID) được lấy từ HopDongChiTiet hoặc ThucChayHopDongChiTiet hoặc từ table ThucChay |
| `DmNhomNganhREF` | `NVARCHAR(250)` nullable | DmNhomNganhREF từ table HopDongChiTiet |
| `TenNhomNganh` | `NVARCHAR(500)` nullable | TenNhomNganh từ table HopDongChiTiet |
| `DmHinhThucQuangCao` | `INT` nullable | DmHinhThucQuangCao từ table HopDongChiTiet (DmLoaiREF) |
| `TenHinhThucQuangCao` | `NVARCHAR(250)` nullable | TenHinhThucQuangCao từ table HopDongChiTiet (TenLoai) |
| `DmSanPhamREF` | `INT` nullable | DmSanPhamREF từ table HopDongChiTiet |
| `TenSanPham` | `NVARCHAR(500)` nullable | TenSanPham từ table HopDongChiTiet |
| `DmNhomWebsiteREF` | `NVARCHAR(200)` nullable | DmNhomWebsiteREF từ table HopDongChiTiet |
| `TenNhomWebsite` | `NVARCHAR(300)` nullable | TenNhomWebsite từ table HopDongChiTiet |
| `DmChuyenMucREF` | `INT` nullable | DmChuyenMucREF từ table HopDongChiTiet |
| `TenChuyenMuc` | `NVARCHAR(500)` nullable | từ table HopDongChiTiet |
| `DmLoaiBannerREF` | `INT` nullable | từ table HopDongChiTiet |
| `TenLoaiBanner` | `NVARCHAR(500)` nullable | từ table HopDongChiTiet |
| `DmViTriREF` | `INT` nullable | từ table HopDongChiTiet ngoại trừ các sản phẩm Adx, ViewPlus, CPC Admarket thì lấy từ bên sản phẩm |
| `TenViTri` | `NVARCHAR(500)` nullable | từ table HopDongChiTiet ngoại trừ các sản phẩm Adx, ViewPlus, CPC Admarket thì lấy từ bên sản phẩm |
| `DotChayHopDong` | `NVARCHAR(1000)` nullable |  |
| `SoLuongDotChayHD` | `INT` nullable | Tổng số lượng ngày đợt chạy trên phân bổ tại ngày tính |
| `DotChayBooking` | `NVARCHAR(1000)` nullable |  |
| `SoLuongDotChayBooking` | `INT` nullable | Tổng số lượng ngày thực treo theo phân bổ |
| `SoLuong` | `INT` nullable | Giá trị trường số lượng trên phân bổ |
| `DonViTinh` | `NVARCHAR(50)` nullable | Đơn vị tính của số lượng thực chạy |
| `DonGia` | `FLOAT` nullable | Đơn giá trên phân bổ |
| `DonGiaTheoDonVi` | `FLOAT` nullable | Đơn giá được quy đổi theo đơn vị tính |
| `ChietKhau` | `FLOAT` nullable | Chiết khấu của table HopDongChiTiet hoặc ThucChayHopDongChiTiet hoặc ThucChayHopDongChiTietPR |
| `GiamGia` | `FLOAT` nullable |  |
| `ThanhTien` | `FLOAT` nullable | ThanhTien từ HopDongChiTiet |
| `TiLeTuVan` | `FLOAT` nullable |  |
| `ChiPhiTuVan` | `FLOAT` nullable |  |
| `IsKhuyenMai` | `INT` nullable | từ table HopDongChiTiet |
| `KhuyenMai` | `NVARCHAR(250)` nullable |  |
| `DmBannerREF` | `INT` nullable |  |
| `DmChienDichREF` | `INT` nullable |  |
| `DmWebsiteREF` | `INT` nullable |  |
| `TenWebsite` | `NVARCHAR(255)` nullable |  |
| `TongViewThucChay` | `FLOAT` nullable |  |
| `TongClickThucChay` | `FLOAT` nullable |  |
| `TongSoBaiViet` | `FLOAT` nullable |  |
| `SoLuongThucChay` | `FLOAT` nullable | Số lượng thực chạy cần tính |
| `NgayThucHien` | `DATETIME` nullable | Ngày thực hiện ghi nhận doanh số thực chạy |
| `GiaTriThayDoi` | `FLOAT` nullable | Giá trị thay đổi phát sinh khi có sự thay đổi về giá trị tính của phân bổ hoặc có sự thay đổi về thuộc tính đã chốt |
| `ThanhTienThucChayTruocTrietKhau` | `FLOAT` nullable | Thành tiền thực chạy được tính chưa bao gồm Chiết khấu |
| `GiaTriTrietKhauThucChay` | `FLOAT` nullable | Gia trị chiết khấu của tiền thực chạy |
| `ThanhTienSauTrietKhauThucChay` | `FLOAT` nullable | Thành tiền thực chạy sau khi đã trừ giá trị chiết khấu (ThanhTienSauTrietKhauThucChay = ThanhTienThucChayTruocTrietKhau - GiaTriTrietKhauThucChay |
| `GiaTriHoaHongThucChay` | `FLOAT` nullable |  |
| `ThanhTienThucThu` | `FLOAT` nullable | Thành tiền thực thu = ThanhTienSauTrietKhauThucChay |
| `ThanhTienKM` | `FLOAT` nullable | Thành tiền thực chạy khuyến mại từ là thành tiền thực chạy với chiết khấu = 100 hoặc iskhuyenmai = 1 |
| `SoLuongThucChayKM` | `INT` nullable | Số lượng thực chạy khuyến mại, tức là số lượng thực chạy với trường hợp Chietkhau = 100 hoặc iskhuyenmai = 1 |
| `SoLuongThucChayLechTreoHa` | `INT` nullable | Số lượng thực chạy lệch treo hạ, tức là số lượng thực chạy khi vượt số lượng HopDongChiTiet, hoặc số lượng thực chạy quy đổi thành tiền vượt giá trị thanhtien trên HopDongChiTiet |
| `ThanhTienLechTreoHa` | `FLOAT` nullable | Thành tiền thực chạy lệch treo hạ, tức là thành tiền thực chạy khi vượt thanhtien của HopDongChiTiet |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `IsPheDuyet` | `TINYINT` nullable |  |
| `PheDuyetBy` | `NVARCHAR(50)` DEFAULT 0 nullable |  |
| `PheDuyetAt` | `DATETIME` nullable |  |
| `SoLuongThayDoi` | `INT` NN DEFAULT 0 | Số lượng thay đổi là số lượng phát sinh khi có sự thay đổi về giá trị của HopDongChiTiet hoặc có sự thay đổi về thông tin của HopDongChiTiet đã tính trước đó |
| `SoLuongKMThayDoi` | `INT` NN DEFAULT 0 | Số lượng khuyến mại thay đổi là số lượng khuyến mại phát sinh khi có sự thay đổi về giá trị của HopDongChiTiet hoặc có sự thay đổi về thông tin của HopDongChiTiet đã tính trước đó |
| `GiaTriKMThayDoi` | `FLOAT` NN DEFAULT 0 | Giá trị khuyến mại thay đổi phát sinh khi có sự thay đổi về giá trị tính của phân bổ hoặc có sự thay đổi về thuộc tính đã chốt |
| `GhiChu` | `NVARCHAR(MAX)` nullable | Ghi chú |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `<Name of Missing Index, sysname,>` | `HopDongChiTietREF, DmHinhThucQuangCao, DmLoaiBannerREF, NgayThucHien` | BTREE |
| `CI_ThucChayDaTinh_NTH` | `NgayThucHien` | BTREE |
| `nix_h_d_d_n` | `HopDongChiTietREF, DmHinhThucQuangCao, DmLoaiBannerREF, NgayThucHien` | BTREE |
| `NonClusteredIndex - HopDongChiTiet-NgayThucHien` | `HopDongID, HopDongChiTietREF, NgayThucHien` | BTREE |
| `nonix_nam_tthd` | `NgayThucHien, Nam, TrangThaiHopDong` | BTREE |
| `PK_ThucChayDaTinh` | `ThucChayDaTinhID` | PRIMARY KEY |
