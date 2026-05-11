# Stored Procedure: `ThucChay_InsertGTTDThucChayDaTinhAdmarket_With_HopDong_NB_SH_KPI`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-12 09:35:46.520000
- **Ngày sửa cuối**: 2026-03-06 17:37:34.033000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ThucChay_PerformanceBase_ThayDoi_ID` | `int(4)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@Tk` | `nvarchar(100)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@TenViTri` | `nvarchar(200)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(400)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@TypeNB_SH_KPI` | `smallint(2)` | No |
| `@ThucChayDaTinhID_output` | `nvarchar(100)` | Yes |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*

*/
CREATE PROCEDURE [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_With_HopDong_NB_SH_KPI]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME, 
	@ThucChay_PerformanceBase_ThayDoi_ID INT,
	@HopDongID INT,
	@HopDongChiTietID INT, 
	@DmSanPhamREF INT, 
	@Tk NVARCHAR(50),
	@DmViTriREF INT,
	@TenViTri NVARCHAR(100),
	@DmWebsiteREF INT,
	@TenWebsite NVARCHAR(200),
	@GiaTriThayDoi FLOAT, 
	@GhiChu nvarchar(200),
	@TypeNB_SH_KPI SMALLINT,
	@ThucChayDaTinhID_output NVARCHAR(50) OUTPUT
AS
BEGIN
	 DECLARE @SoLuongThayDoi INT = 0, @DonViTinh NVARCHAR(100), @SoLuongThucChay INT = 0, @TenSanPham NVARCHAR(200)=''
	  , @DanhSachNhanHangREF NVARCHAR(200) = ''
	  , @GhiChuOnline NVARCHAR(500) = N''
	  , @GhiChu_TienThayDoi NVARCHAR(500) = N''
	  , @DmChienDichREF INT = 0
	  , @V_ChietKhau FLOAT = 0
	SET @DonViTinh = 'CPC'
	SET @TenSanPham =''
	
	IF(@TypeNB_SH_KPI = 2)
	BEGIN
		SET @DmChienDichREF = 2 --insert du lieu cho KPI
		SET @GhiChu = @GhiChu + '- KPI'
	END

	DECLARE @Table_thucchaydatinhAdmarket_id table(
	ThucChayDaTinhID NVARCHAR(50),
	HopDongREF INT
	)

	SELECT TOP 1 @DanhSachNhanHangREF = DanhSachNhanHangREF, @TenSanPham = TenSanPham 
	FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID

	
	SET @V_ChietKhau = 
	( SELECT A.ChietKhau FROM 
		(
			SELECT 
			hdl.ChietKhau,
			hdl.CreatedAt,
			-- Đánh số thứ tự riêng biệt cho từng SoHopDong
			ROW_NUMBER() OVER (
				PARTITION BY hdl.HopDongChiTietREF
				ORDER BY hdl.CreatedAt desc, HopDongChiTietLogID desc
			) AS OrderHopDongChiTietLog
			FROM dbo.HopDongChiTietLog hdl
			where hdl.HopDongChiTietREF = @HopDongChiTietID
			and hdl.ChietKhau <> 100
		) A WHERE A.OrderHopDongChiTietLog = 1
	)

	SET @V_ChietKhau = ISNULL(@V_ChietKhau,0)

	SET @GhiChu_TienThayDoi = @GhiChu + N', Tk:' +@Tk + ', HDCT: ' + Convert(nvarchar(100),@HopDongChiTietID)
	--SET @GhiChu = N'XulyConfirm_DoiTruOnline: ' + CONVERT(NVARCHAR(100),@DmSanPhamREF) + '_' + @Tk+ '_Bosung/Giamgiatri'
	 ------TANG GIA TRI HOPDONG-------
	INSERT INTO dbo.ThucChayDaTinhAdmarket
	(
	    ThucChayDaTinhID,
	    HopDongID,
	    SoHopDong,
	    DmMaHopDongREF,
	    TenMaHopDong,
	    NgayDanhSoHopDong,
	    NgayKyHopDong,
	    NhanHopDong,
	    NgayNhanBanFax,
	    NgayNhanHopDongBanCung,
	    NgayChuyenHopDongChoKeToan,
	    So,
	    Thang,
	    Nam,
	    GiaTriHopDong,
	    CongNo,
	    HopDongChiTietREF,
	    DangSuDung,
	    IsGiayPhep,
	    TrangThaiHopDong,
	    IsBanCung,
	    DmPhongBanREF,
	    TenPhongBan,
	    DmBoPhanREF,
	    TenBoPhan,
	    DmNhomLamViecREF,
	    TenNhomLamViec,
	    DmDiaDiemLamViecREF,
	    TenDiaDiemLamViec,
	    SysNhanVienREF,
	    TenDangNhap,
	    TenNhanVien,
	    TenKhachHang,
	    NhanHang,
	    DmNhomNganhREF,
	    TenNhomNganh,
	    DmHinhThucQuangCao,
	    TenHinhThucQuangCao,
	    DmSanPhamREF,
	    TenSanPham,
	    DmNhomWebsiteREF,
	    TenNhomWebsite,
	    DmChuyenMucREF,
	    TenChuyenMuc,
	    DmLoaiBannerREF,
	    TenLoaiBanner,
	    DmViTriREF,
	    TenViTri,
	    DotChayHopDong,
	    SoLuongDotChayHD,
	    DotChayBooking,
	    SoLuongDotChayBooking,
	    SoLuong,
	    DonViTinh,
	    DonGia,
	    DonGiaTheoDonVi,
	    ChietKhau,
	    GiamGia,
	    ThanhTien,
	    TiLeTuVan,
	    ChiPhiTuVan,
	    IsKhuyenMai,
	    KhuyenMai,
	    DmBannerREF,
	    DmChienDichREF,
	    DmWebsiteREF,
	    TenWebsite,
	    TongViewThucChay,
	    TongClickThucChay,
	    TongSoBaiViet,
	    SoLuongThucChay,
	    NgayThucHien,
	    GiaTriThayDoi,
	    ThanhTienThucChayTruocTrietKhau,
	    GiaTriTrietKhauThucChay,
	    ThanhTienSauTrietKhauThucChay,
	    GiaTriHoaHongThucChay,
	    ThanhTienThucThu,
	    ThanhTienKM,
	    SoLuongThucChayKM,
	    SoLuongThucChayLechTreoHa,
	    ThanhTienLechTreoHa,
	    CreatedAt,
	    LastModifiedAt,
	    IsPheDuyet,
	    PheDuyetBy,
	    PheDuyetAt,
	    SoLuongThayDoi,
	    SoLuongKMThayDoi,
	    GiaTriKMThayDoi,
	    GhiChu
	)
	OUTPUT INSERTED.ThucChayDaTinhID, INSERTED.HopDongID INTO @Table_thucchaydatinhAdmarket_id
	SELECT 
	NEWID() thucchaydatinhid,
	--ID Hop Dong
	D.HopDongID,
	--Thong tin ve ma so 
	D.SoHopDong, 
	D.DmMaHopDongREF, 
	D.TenMaHopDong, 
	--Thong tin ve thoi gian
	D.NgayDanhSoHopDong, D.NgayKyHopDong, 
	D.NhanHopDong, D.NgayNhanBanFax, D.NgayNhanHopDongBanCung, D.NgayChuyenHopDongChoKeToan, 
	D.So, D.Thang, D.Nam, 
	--Thong tin ve gia tri
	D.GiaTriHopDong, D.CongNo,
	--Thong tin chi tiet phan bo
	C.HopDongChiTietID,
	--Thong tin ve trang thai
	D.DangSuDung, D.IsGiayPhep, 2 TrangThaiHopDong,D.IsBanCung, 
	--Thong tin ve Nhan vien kinh doanh
	D.DmPhongBanREF, 
	ISNULL(D.TenPhongBan, '') AS TenPhongBan, 
	D.DmBoPhanREF, 
	ISNULL(D.TenBoPhan,'') AS TenBoPhan, 
	D.DmNhomLamViecREF, 
	ISNULL(D.TenNhom, '') AS TenNhom, 
	D.DmDiaDiemLamViecREF, 
	D.TenDiaDiemLamViec, 
	D.SysNhanVienREF, 
	ISNULL(D.TenDangNhap, '') AS TenDangNhap,  
	D.TenNhanVien, 
	D.TenKhachHang, 
	C.DanhSachNhanHangREF NhanHang, 
	C.DmNhomNganhREF, 
	C.TenNhomNganh, 
	C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
	c.DmSanPhamREF as DmSanPhamREF,
	C.TenSanPham,  
	C.DmNhomWebsiteREF, 
	C.TenNhomWebsite, 
	C.DmChuyenMucREF, 
	C.TenChuyenMuc,
	C.DmLoaiBannerREF, 
	C.TenLoaiBanner, 
	@DmViTriREF DmViTriREF, 
	@TenViTri TenViTri, 
	@Tk DotChayHopDong,
	0 AS SoLuongDotChayHD,
	@ThucChay_PerformanceBase_ThayDoi_ID DotChayBooking,
	@ThucChay_PerformanceBase_ThayDoi_ID AS SoLuongDotChayBooking, 
	C.SoLuong AS SoLuong, 
	@DonViTinh as DonViTinh, 
	C.DonGia as DonGia, 
	C.DonGia AS DonGiaTheoDonViTinh,
	C.ChietKhau, C.GiamGia, C.ThanhTien,
	C.TiLeTuVan,  C.ChiPhiTuVan,
	C.IsKhuyenMai,  
	C.KhuyenMai,
	0 DmBannerREF,
	@DmChienDichREF DmChienDichREF,
	@DmWebsiteREF DmWebsiteREF,
	@TenWebsite TenWebsite,
	0 TongViewThucChay,
	0 TongClickThucChay,
	0 TongSoBaiViet,
	@SoLuongThucChay SoLuongThucChay,
	@NgayThucHien AS NgayThucHien,
	@GiaTriThayDoi as GiaTriThayDoi,	 
	0 as ThanhTienThucChayTruocTrietKhau,
	0 AS GiaTriTrietKhauThucChay,
	0 AS ThanhTienSauTrietKhauThucChay,	
	0 AS GiaTriHoaHongThucChay,
	@GiaTriThayDoi AS ThanhTienThucThu,
	0 ThanhTienKM,
	0 as SoLuongThucChayKM,
	0 SoLuongLechTreoHa,
	0 ThanhTienLechTreoHa,
	GETDATE() createdat,
	GETDATE() lastmodifiedat,
	0 IsPheDuyet,
	'' PheDuyetBy,
	'' PheDuyetAt,
	@SoLuongThayDoi SoLuongThayDoi,
	0 SoLuongKMThayDoi,
	0 GiaTriKMThayDoi,
    @GhiChu_TienThayDoi GhiChu	
	
	FROM 
	(
		SELECT * FROM dbo.HopDongChiTiet 
			WHERE HopDongChiTietID = @HopDongChiTietID
						AND DmSanPhamREF = @DmSanPhamREF
						AND TK_AdMarket = @Tk
				AND RecordStatus = 0
	) C  
	INNER JOIN  
	 ( 
	 	SELECT * FROM dbo.HopDong hd 
	 	WHERE 1=1-- hd.TrangThaiHopDong <> 3	    
	       AND hd.HopDongID = @HopDongID
	       AND hd.DeletedStatus = 0
	 ) D on D.HopDongID = C.HopDongFK


	 SELECT top (1) @ThucChayDaTinhID_output = ISNULL(ThucChayDaTinhID,'') FROM @Table_thucchaydatinhAdmarket_id 

	 --GHI NHAN DONG THOI SANG TABLE dbo.ThucChayDaTinh

	 IF(@ThucChayDaTinhID_output <> '')
	 BEGIN
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

	SELECT 
		NEWID() thucchaydatinhid,
		--ID Hop Dong
		D.HopDongID,
		--Thong tin ve ma so 
		D.SoHopDong, 
		D.DmMaHopDongREF, 
		D.TenMaHopDong, 
		--Thong tin ve thoi gian
		D.NgayDanhSoHopDong, D.NgayKyHopDong, 
		D.NhanHopDong, D.NgayNhanBanFax, D.NgayNhanHopDongBanCung, D.NgayChuyenHopDongChoKeToan, 
		D.So, D.Thang, D.Nam, 
		--Thong tin ve gia tri
		D.GiaTriHopDong, D.CongNo,
		--Thong tin chi tiet phan bo
		C.HopDongChiTietID,
		--Thong tin ve trang thai
		D.DangSuDung, D.IsGiayPhep, 2 TrangThaiHopDong,D.IsBanCung, 
		--Thong tin ve Nhan vien kinh doanh
		D.DmPhongBanREF, 
		ISNULL(D.TenPhongBan, '') AS TenPhongBan, 
		D.DmBoPhanREF, 
		ISNULL(D.TenBoPhan,'') AS TenBoPhan, 
		D.DmNhomLamViecREF, 
		ISNULL(D.TenNhom, '') AS TenNhom, 
		D.DmDiaDiemLamViecREF, 
		D.TenDiaDiemLamViec, 
		D.SysNhanVienREF, 
		ISNULL(D.TenDangNhap, '') AS TenDangNhap,  
		D.TenNhanVien, 
		D.TenKhachHang, 
		C.DanhSachNhanHangREF NhanHang, 
		C.DmNhomNganhREF, 
		C.TenNhomNganh, 
		C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
		c.DmSanPhamREF as DmSanPhamREF,
		C.TenSanPham,  
		C.DmNhomWebsiteREF, 
		C.TenNhomWebsite, 
		C.DmChuyenMucREF, 
		C.TenChuyenMuc,
		C.DmLoaiBannerREF, 
		C.TenLoaiBanner, 
		@DmViTriREF DmViTriREF, 
		@TenViTri TenViTri, 
		@Tk DotChayHopDong,
		0 AS SoLuongDotChayHD,
		@ThucChay_PerformanceBase_ThayDoi_ID DotChayBooking,
		@ThucChay_PerformanceBase_ThayDoi_ID AS SoLuongDotChayBooking, 
		C.SoLuong AS SoLuong, 
		@DonViTinh as DonViTinh, 
		C.DonGia as DonGia, 
		C.DonGia AS DonGiaTheoDonViTinh,
		--C.ChietKhau,
		@V_ChietKhau AS ChietKhau,
		C.GiamGia, C.ThanhTien,
		C.TiLeTuVan,  C.ChiPhiTuVan,
		C.IsKhuyenMai,  
		C.KhuyenMai,
		0 DmBannerREF,
		@DmChienDichREF DmChienDichREF,
		@DmWebsiteREF DmWebsiteREF,
		@TenWebsite TenWebsite,
		0 TongViewThucChay,
		0 TongClickThucChay,
		0 TongSoBaiViet,
		@SoLuongThucChay SoLuongThucChay,
		@NgayThucHien AS NgayThucHien,
		@GiaTriThayDoi as GiaTriThayDoi,	 
		0 as ThanhTienThucChayTruocTrietKhau,
		0 AS GiaTriTrietKhauThucChay,
		0 AS ThanhTienSauTrietKhauThucChay,	
		0 AS GiaTriHoaHongThucChay,
		@GiaTriThayDoi AS ThanhTienThucThu,
		0 ThanhTienKM,
		0 as SoLuongThucChayKM,
		0 SoLuongLechTreoHa,
		0 ThanhTienLechTreoHa,
		GETDATE() createdat,
		GETDATE() lastmodifiedat,
		0 IsPheDuyet,
		'' PheDuyetBy,
		'' PheDuyetAt,
		@SoLuongThayDoi SoLuongThayDoi,
		0 SoLuongKMThayDoi,
		0 GiaTriKMThayDoi,
		@GhiChu_TienThayDoi GhiChu	
	
		FROM 
		(
			SELECT * FROM dbo.HopDongChiTiet 
				WHERE HopDongChiTietID = @HopDongChiTietID
							AND DmSanPhamREF = @DmSanPhamREF
							AND TK_AdMarket = @Tk
					AND RecordStatus = 0
		) C  
		INNER JOIN  
		 ( 
	 		SELECT * FROM dbo.HopDong hd 
	 		WHERE 1=1-- hd.TrangThaiHopDong <> 3	    
			   AND hd.HopDongID = @HopDongID
			   AND hd.DeletedStatus = 0
		 ) D on D.HopDongID = C.HopDongFK
	 END

	
END

```
