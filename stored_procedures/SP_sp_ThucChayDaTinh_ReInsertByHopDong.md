# Stored Procedure: `sp_ThucChayDaTinh_ReInsertByHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-09-18 14:32:16.933000
- **Ngày sửa cuối**: 2021-03-15 16:28:48.427000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong] '2020-05-24'
CREATE PROCEDURE [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
    declare 
	@HopDongID INT,
	@HopDongChiTietID INT,
	@SoHopDong_new NVARCHAR(50),
	@NgayDanhSo_new DATETIME,
	@DmNhanVienREF_new INT,
	@DmKhachHangREF_new NVARCHAR(200),
	@DmSanPhamREF_new INT,
	@DsNhanHangREF_new NVARCHAR(200),
	@HinhThucQuangCaoREF_new INT, @TenDangNhap_new NVARCHAR(50), @DmLoaiBannerREF_new INT = 0,@NoiDungThayDoi NVARCHAR(MAX) = '',
	@MaSoHopDong_new INT , @Note NVARCHAR(50), @IsThayDoi INT,@GiaTriThucChay FLOAT,@GiaTriThucChayAd FLOAT, @IsExistData INT ,@IsExistData1 INT 
	, @DmLoaiREF INT
	, @Is_GGFB SMALLINT = 0

	DECLARE @out NVARCHAR(2000);

	DECLARE db_cursor CURSOR FOR  
	SELECT DISTINCT
		hd.HopDongID,
		hdct.HopDongChiTietID,
		hd.SoHopDong,
		hd.NgayDanhSoHopDong,
		hd.SysNhanVienREF, 
		hd.TenKhachHang,
		hdct.DmSanPhamREF,
		hdct.DanhSachNhanHangREF,
		hdct.DmLoaiREF,
		hd.DmMaHopDongREF,
		hd.TenDangNhap,
		hdct.DmLoaiBannerREF
	FROM dbo.HopDong hd INNER JOIN dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
	WHERE 1=1 
	AND ( CONVERT(DATE,hd.LastModifiedAt) = CONVERT(DATE,@NgayThucHien)
			OR  CONVERT(DATE,hdct.LastModifiedAt) = CONVERT(DATE,@NgayThucHien)
		)

	-- rem code: 21/11/2017 - chạy cho admatic
	-- AND hdct.DmLoaiREF NOT IN (42)
	AND YEAR(hd.NgayDanhSoHopDong) >= (YEAR(GETDATE()) - 2) --2017-03-15 HAIDH COMMENT KHONG BAT NHUNG HOP DONG THAY DOI SAU NGAY HIEN TAI 02 NAM

	OPEN db_cursor   
	FETCH NEXT FROM db_cursor INTO @HopDongID,
	@HopDongChiTietID ,
	@SoHopDong_new ,
	@NgayDanhSo_new ,
	@DmNhanVienREF_new ,
	@DmKhachHangREF_new ,
	@DmSanPhamREF_new ,
	@DsNhanHangREF_new ,
	@HinhThucQuangCaoREF_new ,
	@MaSoHopDong_new ,
	@TenDangNhap_new,
	@DmLoaiBannerREF_new

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
		SET @Is_GGFB = 0
		SET @IsThayDoi = [dbo].[fn_ThucChay_CheckHopDongThayDoi](   @NgayThucHien,
																	@HopDongID,
																	@HopDongChiTietID ,
																	@SoHopDong_new ,
																	@NgayDanhSo_new ,
																	@DmNhanVienREF_new ,
																	@DmKhachHangREF_new ,
																	@DmSanPhamREF_new ,
																	@DsNhanHangREF_new ,
																	@HinhThucQuangCaoREF_new ,
																	@MaSoHopDong_new,
																	@TenDangNhap_new )

		SET @NoiDungThayDoi = [dbo].[fn_ThucChay_CheckHopDongThayDoi_noidungthaydoi](   @NgayThucHien,
																	@HopDongID,
																	@HopDongChiTietID ,
																	@SoHopDong_new ,
																	@NgayDanhSo_new ,
																	@DmNhanVienREF_new ,
																	@DmKhachHangREF_new ,
																	@DmSanPhamREF_new ,
																	@DsNhanHangREF_new ,
																	@HinhThucQuangCaoREF_new ,
																	@MaSoHopDong_new,
																	@TenDangNhap_new )


		--1. XAC DINH DIEU KIEN DE TINH GIA TRI THAY DOI CHO CHO THUCCHAYDATINH, THUCCHAYDATINHADMARKET
		SELECT @GiaTriThucChay = SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) FROM dbo.ThucChayDaTinh tcdt WHERE tcdt.HopDongID = @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChiTietID AND tcdt.NgayThucHien < @NgayThucHien
		SELECT @GiaTriThucChayAd = SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) FROM dbo.ThucChayDaTinhAdmarket tcdt WHERE tcdt.HopDongID = @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChiTietID AND tcdt.NgayThucHien < @NgayThucHien

		SET @GiaTriThucChay = isnull(ROUND(@GiaTriThucChay,0),0)
		SET @GiaTriThucChayAd = isnull(ROUND(@GiaTriThucChayAd,0),0)

		SELECT @IsExistData = COUNT(HopDongID) FROM dbo.ThucChayDaTinh tcdt WHERE tcdt.HopDongID = @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChiTietID AND tcdt.NgayThucHien <@NgayThucHien
		SELECT @IsExistData1 = COUNT(HopDongID) FROM dbo.ThucChayDaTinhAdmarket tcdt WHERE tcdt.HopDongID = @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChiTietID AND tcdt.NgayThucHien <@NgayThucHien
		
		--SELECT @IsThayDoi

		IF(@IsThayDoi <> 0 AND (isnull(@GiaTriThucChay,0) <>0 OR isnull(@GiaTriThucChayAd,0) <> 0) AND (@IsExistData > 0 OR @IsExistData1 > 0))
		BEGIN
			if @IsThayDoi = 1 SET @Note = 'THAY DOI THONG TIN HOP DONG ' + @NoiDungThayDoi
			if @IsThayDoi = 2 SET @Note = 'PHAN BO BI XOA ' + @NoiDungThayDoi
			if @IsThayDoi = 3 SET @Note = 'THAY DOI DANH SACH NHAN HANG ' + @NoiDungThayDoi
			if @IsThayDoi = 4 SET @Note = 'HUY HOP DONG ' + @NoiDungThayDoi
			if @IsThayDoi = 5 SET @Note = 'Admatic Thay Doi Thong Tin HD ' + @NoiDungThayDoi

			----CAI NAY DUNG CHO CHOT CUOI NAM 2016
			--SET @Note = 'GTTD_2016 ' + @Note

			EXEC [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong]
					-- Add the parameters for the stored procedure here
					@NgayThucHien ,
					@HopDongID ,
					@HopDongChiTietID ,
					@SoHopDong_new ,
					@NgayDanhSo_new ,
					@DmNhanVienREF_new ,
					@DmKhachHangREF_new ,
					@DmSanPhamREF_new ,
					@DsNhanHangREF_new ,
					@HinhThucQuangCaoREF_new , 
					@TenDangNhap_new ,
					@MaSoHopDong_new  , 
					@Note , 
					@IsThayDoi ,
					@GiaTriThucChay ,
					@GiaTriThucChayAd ,
					@IsExistData  ,
					@IsExistData1   
			-- 2. Thuc chay da tinh admarket
			EXEC [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong_Admarket]
				-- Add the parameters for the stored procedure here
				@NgayThucHien ,
				@HopDongID ,
				@HopDongChiTietID ,
				@SoHopDong_new ,
				@NgayDanhSo_new ,
				@DmNhanVienREF_new ,
				@DmKhachHangREF_new ,
				@DmSanPhamREF_new ,
				@DsNhanHangREF_new ,
				@HinhThucQuangCaoREF_new , 
				@TenDangNhap_new ,
				@MaSoHopDong_new  , 
				@Note , 
				@IsThayDoi ,
				@GiaTriThucChay ,
				@GiaTriThucChayAd , 
				@IsExistData  ,
				@IsExistData1   

		END
		
		IF(EXISTS(
			SELECT TOP (1) hdct.HopDongChiTietID FROM dbo.HopDongChiTiet hdct
			WHERE hdct.HopDongChiTietID = @HopDongChiTietID
			AND (hdct.DmSanPhamREF in (306,423)	OR hdct.DmViTriREF in (100093,100478) )
			AND hdct.DeletedStatus = 0
			ORDER BY hdct.HopDongChiTietID
		))
		BEGIN
			SET @Is_GGFB = 1
			print ''
		END

		--2. XAC DINH DIEU KIEN DE TINH GIA TRI THAY DOI CHO THUCCHAYDATINH_MUANGOAI
		IF(@HinhThucQuangCaoREF_new = 13 OR @DmLoaiBannerREF_new = 18 OR @Is_GGFB = 1 )
		BEGIN
				DECLARE @GiaTriThucChayLaiMuaNgoai FLOAT = 0
			, @IsExistDataLaiMuaNgoai INT = 0

			SET @GiaTriThucChayLaiMuaNgoai = 
			ISNULL(
				(SELECT SUM(tcdtm.ThanhTienLaiThucChaySauCK + GiaTriThayDoiLaiSauCK) 
					FROM dbo.ThucChayDaTinh_MuaNgoai tcdtm 
					WHERE tcdtm.HopDongREF = @HopDongID AND tcdtm.HopDongChiTietREF = @HopDongChiTietID 
					AND tcdtm.NgayThucHien <= @NgayThucHien
				) ,0)

			SET @IsExistDataLaiMuaNgoai = (SELECT COUNT(tcdtm.HopDongChiTietREF)
					FROM dbo.ThucChayDaTinh_MuaNgoai tcdtm 
					WHERE tcdtm.HopDongREF = @HopDongID AND tcdtm.HopDongChiTietREF = @HopDongChiTietID 
					AND tcdtm.NgayThucHien <= @NgayThucHien
				)

		
			IF(@IsThayDoi <> 0 AND @GiaTriThucChayLaiMuaNgoai <> 0 AND @IsExistDataLaiMuaNgoai <> 0)
			BEGIN
				DECLARE @Note_MuaNgoai Nvarchar(max) = '';
				if @IsThayDoi = 1 SET @Note_MuaNgoai = 'TCDT_Muangoai THAY DOI THONG TIN HOP DONG ' + @NoiDungThayDoi
				if @IsThayDoi = 2 SET @Note_MuaNgoai = 'TCDT_Muangoai PHAN BO BI XOA ' + @NoiDungThayDoi
				if @IsThayDoi = 3 SET @Note_MuaNgoai = 'TCDT_Muangoai THAY DOI DANH SACH NHAN HANG ' + @NoiDungThayDoi
				if @IsThayDoi = 4 SET @Note_MuaNgoai = 'TCDT_Muangoai HUY HOP DONG ' + @NoiDungThayDoi
				if @IsThayDoi = 5 SET @Note_MuaNgoai = 'TCDT_Muangoai Admatic Thay Doi Thong Tin HD ' + @NoiDungThayDoi

				EXEC [dbo].[sp_Insert_ThucChayDaTinh_MuaNgoai_ReInsertByHopDong]
				-- Add the parameters for the stored procedure here
				@NgayThucHien = @NgayThucHien,
				@HopDongID = @HopDongID,
				@HopDongChiTietID = @HopDongChiTietID,
				@SoHopDong_new  = @SoHopDong_new,
				@NgayDanhSo_new = @NgayDanhSo_new,
				@DmNhanVienREF_new = @DmNhanVienREF_new,
				@DmKhachHangREF_new = @DmKhachHangREF_new,
				@DmSanPhamREF_new = @DmSanPhamREF_new,
				@DsNhanHangREF_new = @DsNhanHangREF_new,
				@HinhThucQuangCaoREF_new  = @HinhThucQuangCaoREF_new, 
				@TenDangNhap_new  = @TenDangNhap_new,
				@MaSoHopDong_new  = @MaSoHopDong_new , 
				@Note = @Note_MuaNgoai, 
				@IsThayDoi = @IsThayDoi,
				@GiaTriThucChay  = @GiaTriThucChayLaiMuaNgoai,
				@IsExistData  = @IsExistDataLaiMuaNgoai 
		
			END
		END
	


	FETCH NEXT FROM db_cursor INTO @HopDongID,
	@HopDongChiTietID ,
	@SoHopDong_new ,
	@NgayDanhSo_new ,
	@DmNhanVienREF_new ,
	@DmKhachHangREF_new ,
	@DmSanPhamREF_new ,
	@DsNhanHangREF_new ,
	@HinhThucQuangCaoREF_new ,
	@MaSoHopDong_new  ,
	@TenDangNhap_new  ,
	@DmLoaiBannerREF_new
	END   

	CLOSE db_cursor   
	DEALLOCATE db_cursor
	
END



```
