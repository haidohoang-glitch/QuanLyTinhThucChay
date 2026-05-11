# 06 — Data Architecture Audit (Relations & References)

> Document này ghi nhận các mối quan hệ logic (Virtual Relations) giữa các bảng trong hệ thống.
> Hệ thống không sử dụng Foreign Keys cứng, các liên kết được suy luận từ mô tả (Description) của cột.

## 1. Các Liên Kết Logic (Dựa trên mô tả cột)

| Bảng (Table) | Cột (Column) | Mô tả (Mối quan hệ) |
|--------------|--------------|---------------------|
| `ADS_Operating_Result_Quantity` | `Status` | 1: thêm mới, 2: chốt, 3: hủy |
| `DotChayHopDongChiTiet` | `DotChayHopDongChiTietID` | ID Primary key của table DotChayHopDongChiTiet |
| `DotChayHopDongChiTiet` | `TenWebsite` | Tên website từ table DmWebsite |
| `DotChayHopDongChiTiet` | `HopDongREF` | ID Foreign key từ table HopDong (HopdongID) |
| `DotChayHopDongChiTiet` | `HopDongChiTietREF` | ID Foreign key từ table HopDongChiTiet (HopDongChiTietID) |
| `DotChayHopDongChiTiet` | `ThoiGianBatDau` | Ngày bắt đầu của đợt chạy |
| `DotChayHopDongChiTiet` | `ThoiGianKetThuc` | Ngày kết thúc của đợt chạy |
| `DotChayHopDongChiTiet` | `BookingREF` | ID Booking của đợt chạy |
| `DotChayHopDongChiTiet` | `DmBannerREF` | ID Banner của đợt chạy |
| `DotChayHopDongChiTiet` | `TenBanner` | Tên banner của đợt chạy |
| `DotChayHopDongChiTietThayDoi` | `DotChayHopDongChiTietThayDoiID` | ID của table DotChayHopDongChiTietThayDoi |
| `DotChayHopDongChiTietThayDoi` | `ViTri` | Tên vị trí |
| `DotChayHopDongChiTietThayDoi` | `TenWebsite` | Tên website |
| `DotChayHopDongChiTietThayDoi` | `HopDongREF` | ID Foreign key từ table HopDong (HopDongID) |
| `DotChayHopDongChiTietThayDoi` | `HopDongThayDoiREF` | ID Foreign key từ table HopDongThayDoi (HopDongThayDoiID) |
| `DotChayHopDongChiTietThayDoi` | `HopDongChiTietREF` | ID Foreign key từ table HopDongChiTiet (HopDongChiTietID) |
| `DotChayHopDongChiTietThayDoi` | `ThoiGianBatDau` | Ngày bắt đầu của đợt chạy |
| `DotChayHopDongChiTietThayDoi` | `ThoiGianKetThuc` | Ngày kết thúc của đợt chạy |
| `DotChayHopDongChiTietThayDoi` | `BookingREF` | ID Booking |
| `HopDong` | `HopDongID` | ID primary key của table HopDong |
| `HopDong` | `DmMaHopDongREF` | ID foreign key từ table DmMaHopDong |
| `HopDong` | `TenMaHopDong` | Mã hợp đồng |
| `HopDong` | `NgayKyHopDong` | Ngày ký hợp đồng |
| `HopDong` | `NhanHopDong` | Nhãn hợp đồng |
| `HopDong` | `GiaTriHopDong` | Giá trị hợp đồng |
| `HopDong` | `SoHopDong` | Mã số hợp đồng |
| `HopDong` | `DmKhachHangREF` | ID foreign key từ table Customer |
| `HopDong` | `TenKhachHang` | Tên khách hàng |
| `HopDong` | `SysNhanVienREF` | ID foreign key từ table Nhansusoyeulylich |
| `HopDong` | `TenDangNhap` | tên đăng nhập của nhân viên sale |
| `HopDong` | `TenNhanVien` | Tên nhân viên sale |
| `HopDong` | `NgayDanhSoHopDong` | Ngày đánh số hợp đồng |
| `HopDong` | `NganhHang` | Ngành hàng |
| `HopDong` | `DmNhomREF` | ID foreign key từ table DmNhom |
| `HopDong` | `TrangThaiHopDong` | Trạng thái của hợp đồng |
| `HopDong` | `CreatedBy` | Người tạo bản ghi dữ liệu |
| `HopDong` | `CreatedAt` | Ngày tào bản ghi dữ liệu |
| `HopDong` | `LastModifiedBy` | Người sửa bản ghi dữ liệu |
| `HopDong` | `LastModifiedAt` | Ngày sửa bản ghi dữ liệu |
| `HopDong` | `DeletedStatus` | = 1 là bản ghi bị xóa, = 0 là bản ghi chưa xóa |
| `HopDong` | `RecordStatus` | Trạng thái bản ghi |
| `HopDongChiTiet` | `HopDongChiTietID` | ID primary key của table HopDongChiTiet |
| `HopDongChiTiet` | `HopDongFK` | ID foreign key của table HopDong |
| `HopDongChiTiet` | `DanhSachNhanHangREF` | ID foreign key của table nhãn hàng chi tiết của từng bản ghi trên table HopDongChiTiet |
| `HopDongChiTiet` | `NhanHang` | Tên nhãn hàng |
| `HopDongChiTiet` | `DmNhomNganhREF` | ID foreign key từ table DmNganhHang |
| `HopDongChiTiet` | `TenNhomNganh` | Tên ngành hàng |
| `HopDongChiTiet` | `DmLoaiREF` | ID foreign key DmHinhThucQuangCao |
| `HopDongChiTiet` | `TenLoai` | Tên của hình thức quảng cáo từ table DmHinhThucQuangCao |
| `HopDongChiTiet` | `DmNhomWebsiteREF` | ID của table DmNhomWebsite |
| `HopDongChiTiet` | `TenNhomWebsite` | Tên nhóm Website |
| `HopDongChiTiet` | `DmWebsiteREF` | ID foreign key của table DmWebsite |
| `HopDongChiTiet` | `TenWebsite` | Tên website từ table DmWebsite |
| `HopDongChiTiet` | `DmSanPhamREF` | ID foreign key từ table DmSanPham |
| `HopDongChiTiet` | `TenSanPham` | Tên sản phẩm từ table DmSanPham |
| `HopDongChiTiet` | `DmLoaiBannerREF` | ID của DmLoaiBanner |
| `HopDongChiTiet` | `TenLoaiBanner` | Tên loại banner |
| `HopDongChiTiet` | `DmChuyenMucREF` | ID của DmChuyenMuc |
| `HopDongChiTiet` | `TenChuyenMuc` | Tên của chuyên mục từ table DmChuyenMuc |
| `HopDongChiTiet` | `DmViTriREF` | ID từ table DmVitri |
| `HopDongChiTiet` | `TenViTri` | Tên vị trí quảng cáo trên site từ table DmViTri |
| `HopDongChiTiet` | `SoLuong` | Số lượng chi tiết của từng đơn hàng |
| `HopDongChiTiet` | `DonViTinhREF` | ID Foreign key của DmDonViTinh |
| `HopDongChiTiet` | `DonViTinh` | Mã đơn vị tính |
| `HopDongChiTiet` | `DonGia` | Đơn giá trên từng số lượng sản phẩm |
| `HopDongChiTiet` | `ChietKhau` | Chiết khấu |
| `HopDongChiTiet` | `IsKhuyenMai` | Thông tin HopDongChiTiet có khuyến mãi hay không , = 1 là chiết khấu = 100%, = 0 là không có chiết khấu. |
| `HopDongChiTiet` | `ThanhTien` | tổng thành tiến của HopDongChiTiet (phân bổ), đã bao gồm chiết khấu |
| `HopDongChiTiet` | `TK_AdMarket` | Tên tài khoản chạy trên các sản phẩm Adx, Viewplus |
| `HopDongChiTiet` | `TK_AdMarketID` | ID của tài khoản |
| `HopDongChiTietLog` | `HopDongChiTietLogID` | ID primary key của table HopDongChiTietLog phát sinh tự tăng trên table syn xử lý |
| `HopDongChiTietLog` | `HopDongChiTietREF` | ID Foreign key từ table HopDongChiTiet (HopDongChiTietID) |
| `HopDongChiTietLog` | `HopDongFK` | ID Foreign key từ table HopDong (HopDongID) |
| `HopDongChiTietLog` | `DanhSachNhanHangREF` | DanhSachNhanHangREF từ table HopDongChiTiet |
| `HopDongChiTietLog` | `contract_detail_log_id` | ID từ table nguồn Contract_details nghiệp vụ |
| `HopDongChiTietThayDoi` | `HopDongChiTietThayDoiID` | ID primary key của table HopDongChiTietThayDoi |
| `HopDongChiTietThayDoi` | `HopDongChiTietREF` | ID foreign từ table HopDongChiTiet (HopDongChiTietID) |
| `HopDongChiTietThayDoi` | `HopDongFK` | ID Foreign từ table HopDong (HopDongID) |
| `HopDongChiTietThayDoi` | `HopDongThayDoiREF` | ID Foreign key từ table HopDongThayDoi (HopDongThayDoiID) |
| `HopDongChiTietThayDoi` | `NhanHang` | Tên nhãn hàng |
| `HopDongChiTietThayDoi` | `DmNhomNganhREF` | ID của table DmNhomNganh |
| `HopDongChiTietThayDoi` | `TenNhomNganh` | Tên nhóm ngành |
| `HopDongChiTietThayDoi` | `DmLoaiREF` | ID từ DmHinhThucQuangCao (DmHinhThucQuangCaoID) |
| `HopDongChiTietThayDoi` | `TenLoai` | Tên hình thức quảng cáo |
| `HopDongChiTietThayDoi` | `DmNhomWebsiteREF` | ID từ table DmNhomWebsite |
| `HopDongChiTietThayDoi` | `TenNhomWebsite` | Tên nhóm website |
| `HopDongChiTietThayDoi` | `DmWebsiteREF` | ID  foreign key từ table DmWebiste |
| `HopDongChiTietThayDoi` | `TenWebsite` | Tên website |
| `HopDongChiTietThayDoi` | `DmSanPhamREF` | ID foreign key từ table DmSanPham (DmSanphamID) |
| `HopDongChiTietThayDoi` | `TenSanPham` | Tên sản phẩm |
| `HopDongChiTietThayDoi` | `DmLoaiBannerREF` | ID từ table DmLoaiBanner |
| `HopDongChiTietThayDoi` | `TenLoaiBanner` | Tên loại banner từ DmLoaiBanner |
| `HopDongChiTietThayDoi` | `DmChuyenMucREF` | ID từ table DmChuyenMuc |
| `HopDongChiTietThayDoi` | `TenChuyenMuc` | Tên chuyên mục từ table DmChuyenMuc |
| `HopDongChiTietThayDoi` | `DmViTriREF` | ID từ table DmViTri |
| `HopDongChiTietThayDoi` | `TenViTri` | Tên vị trí từ table DmViTri |
| `HopDongChiTietThayDoi` | `SoLuong` | Số lượng |
| `HopDongChiTietThayDoi` | `DonViTinh` | Đơn vị tính |
| `HopDongChiTietThayDoi` | `DonGia` | Đơn giá |
| `HopDongChiTietThayDoi` | `ChietKhau` | Chiết khấu |
| `HopDongChiTietThayDoi` | `IsKhuyenMai` | = 1 là phân bổ khuyến mại với chiết khấu = 100%, = 0 phân bổ không phải khuyến mại với chiết khấu <> 100% |
| `HopDongChiTietThayDoi` | `ThanhTien` | Thành tiền phân bổ sau chiết khấu |
| `HopDongThayDoi` | `HopDongThayDoiID` | ID primary key của table HopDongThayDoi |
| `HopDongThayDoi` | `HopDongFK` | ID Foreign key từ table HopDong (HopDongID) |
| `HopDongThayDoi` | `LoaiThayDoi` | Loại thay đổi |
| `HopDongThayDoi` | `NgayThayDoi` | Ngày thay đổi |
| `HopDongThayDoi` | `NganhHang` | Tên ngành hàng |
| `HopDongThayDoi` | `NhanHopDong` | tên nhãn hàng của hợp đồng |
| `HopDongThayDoi` | `GiaTriHopDong` | Giá trị hợp đồng |
| `ThucChayAdmarket_HopDong_online` | `data_type` | =1 du lieu khong co hd, = 2 dl hd da do day van co dl tc tra ve, =3 hop dong chua day nhung dl tr vuot qua gia tri hd |
| `ThucChayAdmarket_HopDong_online` | `confirm_money` | th data_type = 2 can confirm so tien chay cua hd den dau (lech do pp tinh cu va moi) |
| `ThucChayAdmarket_HopDong_online` | `trangthai` | = 0 chưa xử lý, =1 đã xử lý |
| `ThucChayDaTinh` | `ThucChayDaTinhID` | ID Primary key của table ThucChayDaTinh |
| `ThucChayDaTinh` | `HopDongID` | ID Foreign key từ table HopDong (HopDongID) |
| `ThucChayDaTinh` | `SoHopDong` | Số hợp đồng từ table HopDong(SoHopDong) |
| `ThucChayDaTinh` | `DmMaHopDongREF` | DmMaHopDongREF từ table HopDong (DmMaHopDongREF) |
| `ThucChayDaTinh` | `TenMaHopDong` | TenMaHopDong từ table HopDong |
| `ThucChayDaTinh` | `NgayDanhSoHopDong` | NgayDanhSoHopDong từ table HopDong |
| `ThucChayDaTinh` | `NgayKyHopDong` | NgayKyHopDong từ table HopDong |
| `ThucChayDaTinh` | `NhanHopDong` | NhanHopDong từ table HopDong |
| `ThucChayDaTinh` | `NgayNhanBanFax` | NgayNhanBanFax từ table HopDong |
| `ThucChayDaTinh` | `NgayNhanHopDongBanCung` | NgayNhanBanCung từ table HopDong |
| `ThucChayDaTinh` | `NgayChuyenHopDongChoKeToan` | NgayChuyenHopDongChoKeToan từ table HopDong |
| `ThucChayDaTinh` | `So` | So từ table HopDong |
| `ThucChayDaTinh` | `Thang` | Thang từ table HopDong |
| `ThucChayDaTinh` | `Nam` | Nam từ table HopDong |
| `ThucChayDaTinh` | `GiaTriHopDong` | GiaTriHopDong từ table HopDong |
| `ThucChayDaTinh` | `CongNo` | CongNo từ table HopDong |
| `ThucChayDaTinh` | `HopDongChiTietREF` | ID Foreign key từ table HopDongChiTiet (HopDongChiTietID) |
| `ThucChayDaTinh` | `DangSuDung` | DangSuDung từ table HopDong |
| `ThucChayDaTinh` | `IsGiayPhep` | IsGiayPhep từ table HopDong |
| `ThucChayDaTinh` | `TrangThaiHopDong` | TrangThaiHopDong từ table HopDong |
| `ThucChayDaTinh` | `IsBanCung` | IsBanCung từ table HopDong |
| `ThucChayDaTinh` | `DmPhongBanREF` | DmPhongBanREF từ table HopDong |
| `ThucChayDaTinh` | `TenPhongBan` | TenPhongBan từ table HopDong |
| `ThucChayDaTinh` | `DmBoPhanREF` | DmBoPhan từ table HopDong |
| `ThucChayDaTinh` | `TenBoPhan` | TenBoPhan từ table HopDong |
| `ThucChayDaTinh` | `DmNhomLamViecREF` | DmNhomLamViecREF từ table HopDong |
| `ThucChayDaTinh` | `TenNhomLamViec` | TenNhomLamViec từ table HopDong |
| `ThucChayDaTinh` | `DmDiaDiemLamViecREF` | DmDiaDiemLamViecREF từ table HopDong |
| `ThucChayDaTinh` | `TenDiaDiemLamViec` | TenDiaDiemLamViec từ table HopDong |
| `ThucChayDaTinh` | `SysNhanVienREF` | SysNhanVienREF từ table HopDong |
| `ThucChayDaTinh` | `TenDangNhap` | TenDangNhap từ table HopDong |
| `ThucChayDaTinh` | `TenNhanVien` | TenNhanVien từ table HopDong |
| `ThucChayDaTinh` | `TenKhachHang` | TenKhachHang từ table HopDong |
| `ThucChayDaTinh` | `NhanHang` | Chưa thông tin ID nhãn hang (NhanHangID) được lấy từ HopDongChiTiet hoặc ThucChayHopDongChiTiet hoặc từ table ThucChay |
| `ThucChayDaTinh` | `DmNhomNganhREF` | DmNhomNganhREF từ table HopDongChiTiet |
| `ThucChayDaTinh` | `TenNhomNganh` | TenNhomNganh từ table HopDongChiTiet |
| `ThucChayDaTinh` | `DmHinhThucQuangCao` | DmHinhThucQuangCao từ table HopDongChiTiet (DmLoaiREF) |
| `ThucChayDaTinh` | `TenHinhThucQuangCao` | TenHinhThucQuangCao từ table HopDongChiTiet (TenLoai) |
| `ThucChayDaTinh` | `DmSanPhamREF` | DmSanPhamREF từ table HopDongChiTiet |
| `ThucChayDaTinh` | `TenSanPham` | TenSanPham từ table HopDongChiTiet |
| `ThucChayDaTinh` | `DmNhomWebsiteREF` | DmNhomWebsiteREF từ table HopDongChiTiet |
| `ThucChayDaTinh` | `TenNhomWebsite` | TenNhomWebsite từ table HopDongChiTiet |
| `ThucChayDaTinh` | `DmChuyenMucREF` | DmChuyenMucREF từ table HopDongChiTiet |
| `ThucChayDaTinh` | `TenChuyenMuc` | từ table HopDongChiTiet |
| `ThucChayDaTinh` | `DmLoaiBannerREF` | từ table HopDongChiTiet |
| `ThucChayDaTinh` | `TenLoaiBanner` | từ table HopDongChiTiet |
| `ThucChayDaTinh` | `DmViTriREF` | từ table HopDongChiTiet ngoại trừ các sản phẩm Adx, ViewPlus, CPC Admarket thì lấy từ bên sản phẩm |
| `ThucChayDaTinh` | `TenViTri` | từ table HopDongChiTiet ngoại trừ các sản phẩm Adx, ViewPlus, CPC Admarket thì lấy từ bên sản phẩm |
| `ThucChayDaTinh` | `SoLuongDotChayHD` | Tổng số lượng ngày đợt chạy trên phân bổ tại ngày tính |
| `ThucChayDaTinh` | `SoLuongDotChayBooking` | Tổng số lượng ngày thực treo theo phân bổ |
| `ThucChayDaTinh` | `SoLuong` | Giá trị trường số lượng trên phân bổ |
| `ThucChayDaTinh` | `DonViTinh` | Đơn vị tính của số lượng thực chạy |
| `ThucChayDaTinh` | `DonGia` | Đơn giá trên phân bổ |
| `ThucChayDaTinh` | `DonGiaTheoDonVi` | Đơn giá được quy đổi theo đơn vị tính |
| `ThucChayDaTinh` | `ChietKhau` | Chiết khấu của table HopDongChiTiet hoặc ThucChayHopDongChiTiet hoặc ThucChayHopDongChiTietPR |
| `ThucChayDaTinh` | `ThanhTien` | ThanhTien từ HopDongChiTiet |
| `ThucChayDaTinh` | `IsKhuyenMai` | từ table HopDongChiTiet |
| `ThucChayDaTinh` | `SoLuongThucChay` | Số lượng thực chạy cần tính |
| `ThucChayDaTinh` | `NgayThucHien` | Ngày thực hiện ghi nhận doanh số thực chạy |
| `ThucChayDaTinh` | `GiaTriThayDoi` | Giá trị thay đổi phát sinh khi có sự thay đổi về giá trị tính của phân bổ hoặc có sự thay đổi về thuộc tính đã chốt |
| `ThucChayDaTinh` | `ThanhTienThucChayTruocTrietKhau` | Thành tiền thực chạy được tính chưa bao gồm Chiết khấu |
| `ThucChayDaTinh` | `GiaTriTrietKhauThucChay` | Gia trị chiết khấu của tiền thực chạy |
| `ThucChayDaTinh` | `ThanhTienSauTrietKhauThucChay` | Thành tiền thực chạy sau khi đã trừ giá trị chiết khấu (ThanhTienSauTrietKhauThucChay = ThanhTienThucChayTruocTrietKhau - GiaTriTrietKhauThucChay |
| `ThucChayDaTinh` | `ThanhTienThucThu` | Thành tiền thực thu = ThanhTienSauTrietKhauThucChay |
| `ThucChayDaTinh` | `ThanhTienKM` | Thành tiền thực chạy khuyến mại từ là thành tiền thực chạy với chiết khấu = 100 hoặc iskhuyenmai = 1 |
| `ThucChayDaTinh` | `SoLuongThucChayKM` | Số lượng thực chạy khuyến mại, tức là số lượng thực chạy với trường hợp Chietkhau = 100 hoặc iskhuyenmai = 1 |
| `ThucChayDaTinh` | `SoLuongThucChayLechTreoHa` | Số lượng thực chạy lệch treo hạ, tức là số lượng thực chạy khi vượt số lượng HopDongChiTiet, hoặc số lượng thực chạy quy đổi thành tiền vượt giá trị thanhtien trên HopDongChiTiet |
| `ThucChayDaTinh` | `ThanhTienLechTreoHa` | Thành tiền thực chạy lệch treo hạ, tức là thành tiền thực chạy khi vượt thanhtien của HopDongChiTiet |
| `ThucChayDaTinh` | `SoLuongThayDoi` | Số lượng thay đổi là số lượng phát sinh khi có sự thay đổi về giá trị của HopDongChiTiet hoặc có sự thay đổi về thông tin của HopDongChiTiet đã tính trước đó |
| `ThucChayDaTinh` | `SoLuongKMThayDoi` | Số lượng khuyến mại thay đổi là số lượng khuyến mại phát sinh khi có sự thay đổi về giá trị của HopDongChiTiet hoặc có sự thay đổi về thông tin của HopDongChiTiet đã tính trước đó |
| `ThucChayDaTinh` | `GiaTriKMThayDoi` | Giá trị khuyến mại thay đổi phát sinh khi có sự thay đổi về giá trị tính của phân bổ hoặc có sự thay đổi về thuộc tính đã chốt |
| `ThucChayDaTinh` | `GhiChu` | Ghi chú |
| `ThucChayHopDongChiTiet` | `ThucChayHopDongChiTietID` | ID Primary key của table ThucChayHopDongChiTiet |
| `ThucChayHopDongChiTiet` | `HopDongREF` | ID foreign key của table HopDong (HopDongID) |
| `ThucChayHopDongChiTiet` | `NhanHang` | Tên nhãn hàng chạy của phân bổ (HopDongChiTiet) |
| `ThucChayHopDongChiTiet` | `ThoiGianBatDau` | Ngày bắt đầu chạy của đợt chạy của banner |
| `ThucChayHopDongChiTiet` | `ThoiGianKetThuc` | Ngày kết thúc chạy của banner |
| `ThucChayHopDongChiTiet` | `Link` | Link thông tin site chạy thực tế |
| `ThucChayHopDongChiTiet` | `DmBannerREF` | ID của Banner |
| `ThucChayHopDongChiTiet` | `TenBanner` | Tên banner |
| `ThucChayHopDongChiTiet` | `ViTri` | Tên vị trí |
| `ThucChayHopDongChiTiet` | `BookingREF` | ID của Booking |
| `ThucChayHopDongChiTiet` | `HopDongChiTietREF` | ID Foreign key từ table HopDongChiTiet (HopDongChiTietID) |
| `ThucChayHopDongChiTiet` | `DmViTriREF` | ID của DmVitri |
| `ThucChayHopDongChiTiet` | `DmNhanHangREF` | ID Foreign key từ table NhanHang |
| `ThucChayHopDongChiTiet` | `SoLuongThucTreo` | Thông tin số lượng treo |
| `ThucChayHopDongChiTiet` | `SoLuongThucChay` | Thông tin số lượng chạy |
| `ThucChayHopDongChiTiet` | `DmDonViTinhREF` | ID Foreign key từ table DmDonvitinh |
| `ThucChayHopDongChiTiet` | `DonViTinh` | Mã đơn vị tính |
| `ThucChayHopDongChiTiet` | `DmHinhThucQuangCaoREF` | ID Foreign key từ table DmHinhThucQuangCao |
| `ThucChayHopDongChiTiet` | `TenHinhThucQuangCao` | Tên hình thức quảng cáo từ table DmHinhThucQuangCao |
| `ThucChayHopDongChiTiet` | `DmSanPhamREF` | ID Foreign key từ table DmSanPham |
| `ThucChayHopDongChiTiet` | `TenSanPham` | Tên sản phảm từ table DmSanPham |
| `ThucChayHopDongChiTiet` | `InputType` | Nguồn dữ liệu phát sinh từ treo trên nhóm chi phí hay treo trên các nhóm Media ( = 0 |
| `ThucChayHopDongChiTiet` | `DonGia` | Đơn giá của thực treo |
| `ThucChayHopDongChiTiet` | `ChietKhau` | Chiết khấu thực treo |
| `ThucChayHopDongChiTiet` | `ThanhTien` | Thành tiền sau chiết khấu của thực treo hoặc thực chạy |
| `ThucChayHopDongChiTiet` | `Id` | ID primary key tự tăng của table ThucChayHopDongChiTiet, ID phục vụ việc lấy dữ liệu của BI theo CDC |
| `ThucChayHopDongChiTiet` | `LoaiThucTreo` | Loại thực treo là "ChiPhi", hay là không phải ChiPhi |
| `ThucChayHopDongChiTiet` | `DmWebsiteREF` | ID Foreign key từ table DmWebsite |
| `ThucChayHopDongChiTiet` | `TenWebsite` | Tên website từ table DmWebsite |
| `ThucChayHopDongChiTiet` | `TrangThaiTreo` | Trạng thái nghiệp vụ của bản ghi thực treo |
| `ThucChayHopDongChiTietAndBanner` | `DaThucHienUpdateTiLe` | = 0 Chua thuc hien update ti le thuc chay cho HopDongChiTietID |
| `ThucChay_PerformanceBase_ThayDoi` | `LoaiGhiNhan` | 0: thuc chay điều chỉnh - chi ap dung voi Adx, Viewplus, CPC admarket. 1: thuc chay thang du giai phap - all san pham. |

---

## 2. Gợi ý Suy luận Liên kết Tự động (Heuristic Relations)

> AI tự động suy luận liên kết nếu cột có đuôi `ID`, `_ID` hoặc `REF` trùng với tên bảng khác.

| Bảng Hiện Tại | Cột | Dự đoán Tham Chiếu (Bảng Đích) |
|---------------|-----|--------------------------------|
| `DotChayHopDongChiTiet` | `HopDongREF` | ──→ `HopDong` |
| `DotChayHopDongChiTiet` | `HopDongChiTietREF` | ──→ `HopDongChiTiet` |
| `DotChayHopDongChiTiet` | `hopdongchitietREF` | ──→ `HopDongChiTiet` |
| `DotChayHopDongChiTietThayDoi` | `HopDongREF` | ──→ `HopDong` |
| `DotChayHopDongChiTietThayDoi` | `HopDongThayDoiREF` | ──→ `HopDongThayDoi` |
| `DotChayHopDongChiTietThayDoi` | `HopDongChiTietREF` | ──→ `HopDongChiTiet` |
| `HopDongChiTietLog` | `HopDongChiTietREF` | ──→ `HopDongChiTiet` |
| `HopDongChiTietThayDoi` | `HopDongChiTietREF` | ──→ `HopDongChiTiet` |
| `HopDongChiTietThayDoi` | `HopDongThayDoiREF` | ──→ `HopDongThayDoi` |
| `HopDongChiTiet_MuaNgoai` | `HopDongChiTietID` | ──→ `HopDongChiTiet` |
| `ThucChay` | `HopDongChiTietREF` | ──→ `HopDongChiTiet` |
| `ThucChayAdmarket_HopDong_online` | `HopDongChiTietREF` | ──→ `HopDongChiTiet` |
| `ThucChayDaTinh` | `HopDongID` | ──→ `HopDong` |
| `ThucChayDaTinh` | `HopDongChiTietREF` | ──→ `HopDongChiTiet` |
| `ThucChayDaTinh_MuaNgoai` | `HopDongREF` | ──→ `HopDong` |
| `ThucChayDaTinh_MuaNgoai` | `HopDongChiTietREF` | ──→ `HopDongChiTiet` |
| `ThucChayDaTinh_MuaNgoai` | `ThucChayMuaNgoaiChiTietREF` | ──→ `ThucChayMuaNgoaiChiTiet` |
| `ThucChayHopDongChiTiet` | `HopDongREF` | ──→ `HopDong` |
| `ThucChayHopDongChiTiet` | `HopDongChiTietREF` | ──→ `HopDongChiTiet` |
| `ThucChayHopDongChiTietAndBanner` | `ThucChayHopDongChiTietID` | ──→ `ThucChayHopDongChiTiet` |
| `ThucChayHopDongChiTietAndBanner` | `HopDongChiTietREF` | ──→ `HopDongChiTiet` |
| `ThucChayHopDongChiTietAndBanner` | `HopDongREF` | ──→ `HopDong` |
| `ThucChayHopDongChiTietAndBanner_Admatic` | `ThucChayHopDongChiTietID` | ──→ `ThucChayHopDongChiTiet` |
| `ThucChayHopDongChiTietAndBanner_Admatic` | `HopDongChiTietREF` | ──→ `HopDongChiTiet` |
| `ThucChayHopDongChiTietAndBanner_Admatic` | `HopDongREF` | ──→ `HopDong` |
| `ThucChayHopDongChiTietAndBanner_Native_Ads` | `ThucChayHopDongChiTietID` | ──→ `ThucChayHopDongChiTiet` |
| `ThucChayHopDongChiTietAndBanner_Native_Ads` | `HopDongChiTietREF` | ──→ `HopDongChiTiet` |
| `ThucChayHopDongChiTietAndBanner_Native_Ads` | `HopDongREF` | ──→ `HopDong` |
| `ThucChayHopDongChiTietLog` | `ThucChayHopDongChiTietID` | ──→ `ThucChayHopDongChiTiet` |
| `ThucChayHopDongChiTietLog` | `HopDongREF` | ──→ `HopDong` |
| `ThucChayHopDongChiTietLog` | `HopDongChiTietREF` | ──→ `HopDongChiTiet` |
| `ThucChayHopDongChiTietPR` | `HopDongREF` | ──→ `HopDong` |
| `ThucChayHopDongChiTietPR` | `HopDongChiTietREF` | ──→ `HopDongChiTiet` |
| `ThucChayHopDongChiTietPR` | `ThucChayHopDongChiTietPrREF` | ──→ `ThucChayHopDongChiTietPR` |
| `ThucChayMuaNgoaiChiTiet` | `HopDongREF` | ──→ `HopDong` |
| `ThucChayMuaNgoaiChiTiet` | `HopDongChiTietREF` | ──→ `HopDongChiTiet` |
| `ThucChay_PerformanceBase_ThayDoi` | `HopDongID` | ──→ `HopDong` |
| `ThucChay_PerformanceBase_ThayDoi` | `HopDongChiTietREF` | ──→ `HopDongChiTiet` |
| `ThucChay_ThanhTien_Admatic` | `HopDongChiTietREF` | ──→ `HopDongChiTiet` |