# Stored Procedure: `ThucChay_TinhLaiGTTDThucChayDaTinh_CPD_DonViGoi_ByHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-10-10 15:48:26.327000
- **Ngày sửa cuối**: 2022-11-23 16:01:38.810000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChitietID` | `int(4)` | No |
| `@GhiChu` | `nvarchar(1000)` | No |
| `@ThucChayDaTinhID_op` | `nvarchar(1000)` | Yes |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE  PROCEDURE [dbo].[ThucChay_TinhLaiGTTDThucChayDaTinh_CPD_DonViGoi_ByHopDongChiTiet] 
	@NgayThucHien DATETIME,
	@HopDongChitietID INT,
	@GhiChu NVARCHAR(500),
	@ThucChayDaTinhID_op NVARCHAR(500) OUTPUT
AS
BEGIN

DECLARE  @NgayDanhSo_GioiHan DATETIME
	, @TongThanhTienThucChay FLOAT = 0
	SET @NgayDanhSo_GioiHan = '2022-01-01'

	DECLARE @Table_op TABLE(ThucChayDaTinhID NVARCHAR(100), HopDongChiTietID INT)
	INSERT INTO [dbo].[ThucChayDaTinh]
			([ThucChayDaTinhID]
			,[HopDongID]
			,[SoHopDong]
			,[DmMaHopDongREF]
			,[TenMaHopDong]
			,[NgayDanhSoHopDong]
			,[NgayKyHopDong]
			,[NhanHopDong]
			,[NgayNhanBanFax]
			,[NgayNhanHopDongBanCung]
			,[NgayChuyenHopDongChoKeToan]
			,[So]
			,[Thang]
			,[Nam]
			,[GiaTriHopDong]
			,[CongNo]
			,[HopDongChiTietREF]
			,[DangSuDung]
			,[IsGiayPhep]
			,[TrangThaiHopDong]
			,[IsBanCung]
			,[DmPhongBanREF]
			,[TenPhongBan]
			,[DmBoPhanREF]
			,[TenBoPhan]
			,[DmNhomLamViecREF]
			,[TenNhomLamViec]
			,[DmDiaDiemLamViecREF]
			,[TenDiaDiemLamViec]
			,[SysNhanVienREF]
			,[TenDangNhap]
			,[TenNhanVien]
			,[TenKhachHang]
			,[NhanHang]
			,[DmNhomNganhREF]
			,[TenNhomNganh]
			,[DmHinhThucQuangCao]
			,[TenHinhThucQuangCao]
			,[DmSanPhamREF]
			,[TenSanPham]
			,[DmNhomWebsiteREF]
			,[TenNhomWebsite]
			,[DmChuyenMucREF]
			,[TenChuyenMuc]
			,[DmLoaiBannerREF]
			,[TenLoaiBanner]
			,[DmViTriREF]
			,[TenViTri]
			,[DotChayHopDong]
			,[SoLuongDotChayHD]
			,[DotChayBooking]
			,[SoLuongDotChayBooking]
			,[SoLuong]
			,[DonViTinh]
			,[DonGia]
			,[DonGiaTheoDonVi]
			,[ChietKhau]
			,[GiamGia]
			,[ThanhTien]
			,[TiLeTuVan]
			,[ChiPhiTuVan]
			,[IsKhuyenMai]
			,[KhuyenMai]
			,[DmBannerREF]
			,[DmChienDichREF]
			,[DmWebsiteREF]
			,[TenWebsite]
			,[TongViewThucChay]
			,[TongClickThucChay]
			,[TongSoBaiViet]
			,[SoLuongThucChay]
			,[NgayThucHien]
			,[GiaTriThayDoi]
			,[ThanhTienThucChayTruocTrietKhau]
			,[GiaTriTrietKhauThucChay]
			,[ThanhTienSauTrietKhauThucChay]
			,[GiaTriHoaHongThucChay]
			,[ThanhTienThucThu]
			,[ThanhTienKM]
			,[SoLuongThucChayKM]
			,[SoLuongThucChayLechTreoHa]
			,[ThanhTienLechTreoHa]
			,[CreatedAt]
			,[LastModifiedAt]
			,[IsPheDuyet]
			,[PheDuyetBy]
			,[PheDuyetAt]
			,[SoLuongThayDoi]
			,[SoLuongKMThayDoi]
			,[GiaTriKMThayDoi]
			,[GhiChu])
    
		OUTPUT INSERTED.ThucChayDaTinhID, INSERTED.HopDongChiTietREF INTO  @Table_op

		SELECT TCDT.ThucChayDaTinhID
		,TCDT.HopDongID, TCDT.SoHopDong, 
		TCDT.DmMaHopDongREF,TCDT.TenMaHopDong, 
		TCDT.NgayDanhSoHopDong, TCDT.NgayKyHopDong, 
		TCDT.NhanHopDong, TCDT.NgayNhanBanFax, TCDT.NgayNhanHopDongBanCung, TCDT.NgayChuyenHopDongChoKeToan, 
		TCDT.So, TCDT.Thang, TCDT.Nam, 
		TCDT.GiaTriHopDong, TCDT.CongNo,
		TCDT.HopDongChiTietID,
		--Thong tin ve trang thai
		TCDT.DangSuDung, TCDT.IsGiayPhep, TCDT.TrangThaiHopDong,TCDT.IsBanCung, 
		--Thong tin ve Nhan vien kinh doanh
		TCDT.DmPhongBanREF, TCDT.TenPhongBan, 
		TCDT.DmBoPhanREF, TCDT.TenBoPhan, 
		TCDT.DmNhomLamViecREF,	TCDT.TenNhom, 
		TCDT.DmDiaDiemLamViecREF,	TCDT.TenDiaDiemLamViec, 
		TCDT.SysNhanVienREF, TCDT.TenDangNhap,  
		TCDT.TenNhanVien, 
		TCDT.TenKhachHang, 
		TCDT.NhanHang,
		TCDT.DmNhomNganhREF,TCDT.TenNhomNganh, 
		--Thong tin hinh thuc quang cao
		TCDT.DmHinhThucQuangCao, TCDT.TenHinhThucQuangCao, 
		--Thong tin San pham
		TCDT.DmSanPhamREF as DmSanPhamREF,	TCDT.TenSanPham,  
		TCDT.DmNhomWebsiteREF, TCDT.TenNhomWebsite, 
		TCDT.DmChuyenMucREF, TCDT.TenChuyenMuc,
		TCDT.DmLoaiBannerREF, TCDT.TenLoaiBanner, 
		TCDT.DmViTriREF, TCDT.TenViTri, 
		--Thong tin ve Tien
		TCDT.DotChayHopDong,
		TCDT.SoLuongDotChayHD,
		--Thong tin dot chay cua thuc treo ( vi tinh thuc chay theo dot chay va thuc treo hd)	
		TCDT.DotChayBooking,
		TCDT.SoLuongDotChayBooking,
		TCDT.SoLuong, 
		TCDT.DonViTinh,
		TCDT.DonGia, 
		TCDT.DonGiaTheoDonViTinh,
		TCDT.ChietKhau, TCDT.GiamGia, TCDT.ThanhTien,
		TCDT.TiLeTuVan,  TCDT.ChiPhiTuVan,
		TCDT.IsKhuyenMai,  
		TCDT.KhuyenMai,
		--Thuc chay
		TCDT.DmBannerREF,--A.DmBannerREF,
		TCDT.DmChienDichREF,--A.DmChienDichREF,
		TCDT.DmWebsiteREF,
		TCDT.TenWebsite,
		TCDT.TongViewThucChay,
		TCDT.TongClickThucChay,
		TCDT.TongSoBaiViet,
		0 SoLuongThucChay,
		--Thanh Tien Thuc Chay
		TCDT.NgayThucHien,
		TCDT.ThanhTienSauTrietKhauThucChay GiaTriThayDoi,
		0 ThanhTienThucChayTruocTrietKhau,
		0 GiaTriTrietKhauThucChay,
		0 ThanhTienSauTrietKhauThucChay,
		0 GiaTriHoaHongThucChay,
		0 ThanhTienThucThu,
		0 ThanhTienKM,
		0 SoLuongThucChayKM,
		0 SoLuongThucChayLechTreoHa,
		0 ThanhTienLechTreoHa,
		TCDT.CreatedAt,
		TCDT.LastModifiedAt,
		TCDT.IsPheDuyet,
		TCDT.PheDuyetBy,
		TCDT.PheDuyetAt,
		TCDT.SoLuongThucChay AS SoLuongThayDoi,
		TCDT.SoLuongThucChayKM AS SoLuongKMThayDoi,
		TCDT.ThanhTienKM AS GiaTriKMThayDoi,
		TCDT.GhiChu	
			FROM 
		(
		SELECT  NEWID() ThucChayDaTinhID, TD.*, 
		ISNULL((TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100,0) AS GiaTriTrietKhauThucChay,
		ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) AS ThanhTienSauTrietKhauThucChay,
		ISNULL(((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100,0) AS GiaTriHoaHongThucChay,
		ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100 - ((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS ThanhTienThucThu,
		(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then TD.ThanhTienThucChayTruocTrietKhau
			else 0
			END
		) as ThanhTienKM,
		(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_CPDDotChay(@NgayThucHien, TD.HopDongChiTietID),0)
			else 0
			END
		) as SoLuongThucChayKM,
		0 SoLuongThucChayLechTreoHa,
		0 ThanhTienLechTreoHa,
		GETDATE() CreatedAt,
		GETDATE() LastModifiedAt,
		0 IsPheDuyet,
		'' PheDuyetBy,
		'' PheDuyetAt,
		0 SoLuongThayDoi,
		0 SoLuongKMThayDoi,
		0 GiaTriKMThayDoi,
		@GhiChu AS GhiChu	
		FROM 
		(
		SELECT 
		--ID Hop Dong
		D.HopDongID, D.SoHopDong, 
		D.DmMaHopDongREF,D.TenMaHopDong, 
		--Thong tin ve thoi gian
		D.NgayDanhSoHopDong, D.NgayKyHopDong, 
		D.NhanHopDong, D.NgayNhanBanFax, D.NgayNhanHopDongBanCung, D.NgayChuyenHopDongChoKeToan, 
		D.So, D.Thang, D.Nam, 
		--Thong tin ve gia tri
		D.GiaTriHopDong, D.CongNo,
		--Thong tin chi tiet phan bo
		C.HopDongChiTietID,
		--Thong tin ve trang thai
		D.DangSuDung, D.IsGiayPhep, D.TrangThaiHopDong,D.IsBanCung, 
		--Thong tin ve Nhan vien kinh doanh
		D.DmPhongBanREF, ISNULL(D.TenPhongBan, '') AS TenPhongBan, 
		D.DmBoPhanREF, ISNULL(D.TenBoPhan,'') AS TenBoPhan, 
		D.DmNhomLamViecREF,	ISNULL(D.TenNhom, '') AS TenNhom, 
		D.DmDiaDiemLamViecREF,	D.TenDiaDiemLamViec, 
		D.SysNhanVienREF, ISNULL(D.TenDangNhap, '') AS TenDangNhap,  
		D.TenNhanVien, 
		D.TenKhachHang, 
		--C.NhanHang, 
		[dbo].[f_ReturnListConcatNhanHangREF_v2](C.HopDongChiTietID, @NgayThucHien) NhanHang,
		C.DmNhomNganhREF,C.TenNhomNganh, 
		--Thong tin hinh thuc quang cao
		C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
		--Thong tin San pham
		c.DmSanPhamREF as DmSanPhamREF,	C.TenSanPham,  
		C.DmNhomWebsiteREF, C.TenNhomWebsite, 
		C.DmChuyenMucREF, C.TenChuyenMuc,
		C.DmLoaiBannerREF, C.TenLoaiBanner, 
		C.DmViTriREF, C.TenViTri, 
		--Thong tin ve Tien
		dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'Y') DotChayHopDong,
		ISNULL(dbo.ThucChay_GetSoLuongChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,c.HopDongChiTietID),0)AS SoLuongDotChayHD,
		--Thong tin dot chay cua thuc treo ( vi tinh thuc chay theo dot chay va thuc treo hd)	
		N'' DotChayBooking,
		0 SoLuongDotChayBooking,
		C.SoLuong AS SoLuong, 
		dbo.FormatDonViTinh(C.DonViTinh) DonViTinh,
		C.DonGia as DonGia, 
		C.DonGia AS DonGiaTheoDonViTinh,
		C.ChietKhau, C.GiamGia, C.ThanhTien,
		C.TiLeTuVan,  C.ChiPhiTuVan,
		C.IsKhuyenMai,  
		C.KhuyenMai,
		--Thuc chay
		0 DmBannerREF,--A.DmBannerREF,
		0 DmChienDichREF,--A.DmChienDichREF,
		dbo.[GetDmWebsiteReportingdbIDByDmWebsiteID_CPD](C.DmWebsiteREF) DmWebsiteREF,
		dbo.[GetWebsiteLinkByDmWebsiteID_CPD](C.DmWebsiteREF,C.TenWebsite) TenWebsite,
		0 TongViewThucChay,
		0 TongClickThucChay,
		0 TongSoBaiViet,
		C.SoLuong as SoLuongThucChay,
		--Thanh Tien Thuc Chay
		@NgayThucHien AS NgayThucHien,
		0 as GiaTriThayDoi,
		C.SoLuong*C.DonGia as ThanhTienThucChayTruocTrietKhau
		FROM 
		(
			SELECT DISTINCT  hdct.* FROM HopDongChiTiet hdct INNER JOIN dbo.ThucChayHopDongChiTiet tc 
			ON hdct.HopDongChiTietID = tc.HopDongChiTietREF
			WHERE hdct.DmSanPhamREF in (140,228,564,549,5082)
			AND hdct.HopDongChiTietID = @HopDongChiTietID
			AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) = 5 --Đơn vị gói của hình thức CPD 
			AND hdct.DeletedStatus = 0
			AND tc.DeletedStatus = 0
			AND hdct.DmLoaiBannerREF NOT IN (17,18)
			AND hdct.DmLoaiREF <> 13 --Khong tinh thuc chay cho HTQC Mua Ngoai
			AND tc.RecordStatus = 0
		) C  
		INNER JOIN  
		( 
			SELECT * FROM HopDong hd  WHERE hd.TrangThaiHopDong <> 3
			AND hd.NgayDanhSoHopDong >= @NgayDanhSo_GioiHan
		) D on D.HopDongID = C.HopDongFK
		) TD
		WHERE 1=1
		) TCDT
		WHERE 1=1 
		AND (TCDT.SoLuongThucChay >0 OR TCDT.SoLuongThucChayKM >0 OR 
		TCDT.SoLuongThucChayLechTreoHa >0 OR TCDT.GiaTriThayDoi <> 0) 
	
	SET @ThucChayDaTinhID_op = ISNULL((SELECT TOP 1 ThucChayDaTinhID FROM @Table_op ),'')
END

```
