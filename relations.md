# Database Relations

> File này được sinh tự động từ SQL Server. Bạn có thể chỉnh sửa thủ công mà không lo bị ghi đè khi gen lại bảng.

*(Không có khóa ngoại (Foreign Keys) cứng nào được định nghĩa trên Database)*

---

## Virtual Relations (Liên kết logic dựa trên mô tả)

> Hệ thống không dùng FK cứng. Các liên kết được mô tả qua Property `MS_Description` của từng cột.

| Bảng | Cột | Ý nghĩa / Liên kết |
|------|-----|--------------------|
| `AdmaticDonGiaBanner` | `AdmaticBannerID` | Banner core cua Admatic |
| `AdmaticDonGiaBanner` | `AdmaticProductID` | TYPEPRODUCT<br>-- 1: Adx Mobile<br>-- 2: Admicro AdExchange Adx<br>-- 3: adx Ecom<br>-- 4: Adx CTA<br>-- 5: Admarket CPC<br>-- 6: CPM kingsize<br>-- 7: CPM Stick<br>-- 8: TVC Online<br>-- 9: Balloon<br>--10: BrandPage<br>--11: Mobile |
| `AdmaticDonGiaBanner` | `DmBannerID` | Banner cua san pham core |
| `AdmaticDonGiaBanner` | `DonGiaBanner_VAT` | Don gia banner da bao gom VAT |
| `AdmaticDonGiaBanner` | `LoaiDonGiaTheoDVT` | Loai don gia theo don vi tinh:<br>--1: CPC<br>--2: CPM<br>--3: CPM |
| `ADS_Operating_Result_Quantity` | `Status` | 1: thêm mới, 2: chốt, 3: hủy |
| `ADX_Job_UpdateStatusThayDoiThucChay` | `Status` | 1: Cần chạy Job, 2: Đã chạy, 3: Chạy lỗi |
| `AppKetQuaVanHanh_CreatorContent` | `TrangThai` | 1- Mới<br>2- Gửi duyệt (gửi leader duyệt)<br>3- Duyệt KQVH (leader duyệt)<br>4- Từ chối duyệt TC<br>5- Gửi duyệt TT: Gửi kế toán duyệt TT<br>6- Duyệt TT: Kế toán duyệt TT<br>7- Từ chối duyệt TT |
| `BangGiaSanPham` | `DmDonViTinhREF` | 1: CPC; 2: CPM |
| `Booking` | `DonViTinh` | WEEK = 1, THANG = 2, NGAY = 3, CPM = 4 |
| `Booking` | `HinhThucSP` | Hình Thức sản phẩm: <br>=1 CPD<br>=2 CPM<br>= 3 PR |
| `Booking` | `MaSanPham` | MaSanPham: <br>when 1 then  N'Banner - CPD'<br>when 2 then  N'Box App CPD'<br>when 3 then  N'CPM 7000 - CPM'<br>when 4 then  N'CPM Mass - CPM'<br>when 5 then  N'Balloon Ads - CPM'<br>when 6 then  N'CPM mobile - CPM'<br>when 7 then  N'CPM Admarket - CPM'<br>when 8 then  N'TVC Online - CPM'<br>when 9 then  N'Box App CPM' |
| `BookingUserFull` | `NhanSuSoYeuLyLichREF` | Lay id cua bang hdcn_nv_soyeulylich o db: hdcn |
| `BookingUserFull` | `TenDangNhap` | lay username o bang ox_users o db: reportingdb |
| `BookingUserFull` | `IsAdmin` | =0 sales;<br>=1 admin |
| `BookingUserFull` | `TypeTool` | 1=hd.admicro.vn<br>2=hdcn.admicro.vn(TMDT) |
| `BookingUserFull` | `TypeLook` | =0 mac dinh<br>=1 system lock |
| `CauHinhNhomTinhDoanhSoThucChay` | `NhomTinhDoanhSoThucChay` | NhomTinhDoanhSoThucChay: 1- Nhom san pham Chi Phi, 2: Branding, 3: PR, 4: Admatic, 5: Performance Base |
| `DataLog_QLTC_XuLylaiDuLieu` | `Status` | 0: mới, 1: đang chạy, 2:thành công, 3:thất bại |
| `DotChayChiTietHopDongChiTiet` | `DotChayChiTietHopDongChiTietID` | ID primary key của table DotChayHopDongChiTietThayDoi |
| `DotChayChiTietHopDongChiTiet` | `DotChayHopDongChitietREF` | ID Foreign key từ table DotChayHopDongChiTiet (DotChayHopDongChiTietID) |
| `DotChayChiTietHopDongChiTiet` | `BookingREF` | ID Của Booking |
| `DotChayChiTietHopDongChiTiet` | `SoLuong` | Số lượng đợt chạy |
| `DotChayChiTietHopDongChiTiet` | `ThoiGianBatDau` | Ngày bắt đầu |
| `DotChayChiTietHopDongChiTiet` | `ThoiGianKetThuc` | Ngày kết thúc |
| `DotChayChiTietHopDongChiTiet` | `VungMienID` | ID Vùng miền từ table VungMien |
| `DotChayChiTietHopDongChiTiet` | `TenVungMien` | Tên vùng miền từ table VungMien |
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
| `Job_desc` | `JOB_TYPE_NAME` | = 0 là job lấy dữ liệu đầu vào cho tính toán, =1 job thực hiện tính toán thực chạy để đổ vào các table ThucChayDaTinh, ThucChayDaTinhAdmarket,.. |
| `KhachHangThongTinChung` | `DmHinhThucKhachHangREF` | 1: NB, 2: Ca nhan, 3: DaiLy, 4: Doanh Nghiep |
| `Log_MaxNgayThucHien` | `NhomSanPham` | 1: Nhom san pham CPM, 2 : Mobile, 3: Admatic, 4: CPD, |
| `ThongTinRaSoatThucChayDaTinh` | `TrangThaiXuLy` | 0: Chua xu ly; 1 Da xu ly; 2 pending |
| `ThucChay_CheckThucChayCPDDaily` | `CheckedStatus` | =0 chua check, = 1 da check |
| `ThucChay_CheckThucChayCPDDaily` | `Status` | =0 true, = 1 false, = 2 warning,pending |
| `ThucChay_PerformanceBase_ThayDoi` | `LoaiGhiNhan` | 0: thuc chay điều chỉnh - chi ap dung voi Adx, Viewplus, CPC admarket. 1: thuc chay thang du giai phap - all san pham. |
| `ThucChay_PerformanceBase_ThayDoi_HopDong` | `LoaiGhiNhan` | 0: thuc chay điều chỉnh - chi ap dung voi Adx, Viewplus, CPC admarket, 1: thuc chay thang du giai phap - all san pham |
| `ThucChayAdmarket_ADX_CPC_HopDong_online` | `data_type` | =1 du lieu khong co hd, = 2 dl hd da do day van co dl tc tra ve, =3 hop dong chua day nhung dl tr vuot qua gia tri hd |
| `ThucChayAdmarket_ADX_CPC_HopDong_online` | `confirm_money` | th data_type = 2 can confirm so tien chay cua hd den dau (lech do pp tinh cu va moi) |
| `ThucChayAdmarket_ADX_CPC_HopDong_online` | `trangthai` | = 0 chưa xử lý, =1 đã xử lý |
| `ThucChayAdmarket_HopDong_online` | `data_type` | =1 du lieu khong co hd, = 2 dl hd da do day van co dl tc tra ve, =3 hop dong chua day nhung dl tr vuot qua gia tri hd |
| `ThucChayAdmarket_HopDong_online` | `confirm_money` | th data_type = 2 can confirm so tien chay cua hd den dau (lech do pp tinh cu va moi) |
| `ThucChayAdmarket_HopDong_online` | `trangthai` | = 0 chưa xử lý, =1 đã xử lý |
| `ThucChayAdmarket_ViewPlus_HopDong_online` | `data_type` | =1 du lieu khong co hd, = 2 dl hd da do day van co dl tc tra ve, =3 hop dong chua day nhung dl tr vuot qua gia tri hd, =4 khi chạy thừa và muốn chuyên giá trị thừa sang hợp đồng khác,= 5 TH tra ve vuot khong dang ke confirm du lieu de = du lieu tra ve asd lam |
| `ThucChayAdmarket_ViewPlus_HopDong_online` | `confirm_money` | th data_type = 2 can confirm so tien chay cua hd den dau (lech do pp tinh cu va moi) |
| `ThucChayAdmarket_ViewPlus_HopDong_online` | `trangthai` | = 0 chưa xử lý, =1 đã xử lý |
| `ThucChayAdmarketTotal` | `DataType` | =1: Theo Domain;<br>=2: Theo HopDong;<br>=3: Theo Sale; |
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
| `ThucChayDaTinh_Temp` | `SoLuongDotChayHD` | Tổng số lượng ngày đợt chạy trên phân bổ tại ngày tính |
| `ThucChayDaTinh_Temp` | `SoLuongDotChayBooking` | Tổng số lượng ngày thực treo theo phân bổ |
| `ThucChayDaTinh_Temp` | `SoLuong` | Giá trị trường số lượng trên phân bổ |
| `ThucChayDaTinh_Temp` | `DonViTinh` | Đơn vị tính của số lượng thực chạy |
| `ThucChayDaTinhMobile` | `SoLuongDotChayHD` | Tổng số lượng ngày đợt chạy trên phân bổ tại ngày tính |
| `ThucChayDaTinhMobile` | `SoLuongDotChayBooking` | Tổng số lượng ngày thực treo theo phân bổ |
| `ThucChayDaTinhMobile` | `SoLuong` | Giá trị trường số lượng trên phân bổ |
| `ThucChayDaTinhMobile` | `DonViTinh` | Đơn vị tính của số lượng thực chạy |
| `ThucChayDaTinhMobileBanner` | `SoLuongDotChayHD` | Tổng số lượng ngày đợt chạy trên phân bổ tại ngày tính |
| `ThucChayDaTinhMobileBanner` | `SoLuongDotChayBooking` | Tổng số lượng ngày thực treo theo phân bổ |
| `ThucChayDaTinhMobileBanner` | `SoLuong` | Giá trị trường số lượng trên phân bổ |
| `ThucChayDaTinhMobileBanner` | `DonViTinh` | Đơn vị tính của số lượng thực chạy |
| `ThucChayDaTinhProblem` | `SoLuongDotChayHD` | Tổng số lượng ngày đợt chạy trên phân bổ tại ngày tính |
| `ThucChayDaTinhProblem` | `SoLuongDotChayBooking` | Tổng số lượng ngày thực treo theo phân bổ |
| `ThucChayDaTinhProblem` | `SoLuong` | Giá trị trường số lượng trên phân bổ |
| `ThucChayDaTinhProblem` | `DonViTinh` | Đơn vị tính của số lượng thực chạy |
| `ThucChayDaTinhSponsorBanner` | `SoLuongDotChayHD` | Tổng số lượng ngày đợt chạy trên phân bổ tại ngày tính |
| `ThucChayDaTinhSponsorBanner` | `SoLuongDotChayBooking` | Tổng số lượng ngày thực treo theo phân bổ |
| `ThucChayDaTinhSponsorBanner` | `SoLuong` | Giá trị trường số lượng trên phân bổ |
| `ThucChayDaTinhSponsorBanner` | `DonViTinh` | Đơn vị tính của số lượng thực chạy |
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
| `ThucChayHopDongChiTietAndBanner` | `DaThucHienUpdateTiLe` | = 0 Chua thuc hien update ti le thuc chay cho HopDongChiTietID<br>= 1 Da Thuc hien update ti le thuc chay cho HopDongChiTietID |
| `ThucChayHopDongChiTietAndBanner_Test` | `DaThucHienUpdateTiLe` | = 0 Chua thuc hien update ti le thuc chay cho HopDongChiTietID<br>= 1 Da Thuc hien update ti le thuc chay cho HopDongChiTietID |
| `ThucChayMobileTemp` | `UnitName` | 1: Click<br>2: View |
| `ThucChaySponsorTemp` | `UnitName` | 1: Click<br>2: View |
| `ThucTreoHopDongChiTietTrinhDuyet` | `DmHinhThucQuangCaoREF` | 'Hinh thuc quang cao id' |
| `ThucTreoHopDongChiTietTrinhDuyet` | `TenNhanHang` | 'Ten nhan hang', |
| `ThucTreoHopDongChiTietTrinhDuyet` | `Soluong` | 'So luong treo', |
| `ThucTreoHopDongChiTietTrinhDuyet` | `TongTien` | 'thanh tien sau chiet khau', |
| `ThucTreoHopDongChiTietTrinhDuyet` | `NgayBatDau` | 'Thoi gian bat dau chay', |
| `ThucTreoHopDongChiTietTrinhDuyet` | `NgayKetThuc` | 'thoi gian ket thuc', |
| `ThucTreoHopDongChiTietTrinhDuyet` | `TrangThai` | 'trang thai: 0 = luu nhap, 1 = trinh duyet, 2 = da duyet, 3 = tu choi', |