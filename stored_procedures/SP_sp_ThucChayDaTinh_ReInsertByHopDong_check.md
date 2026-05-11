# Stored Procedure: `sp_ThucChayDaTinh_ReInsertByHopDong_check`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-05-18 17:05:59.993000
- **Ngày sửa cuối**: 2017-05-18 17:14:03.303000

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

--EXEC [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong_check] '2017-05-17'
CREATE PROCEDURE [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong_check]
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
	@HinhThucQuangCaoREF_new INT, @TenDangNhap_new NVARCHAR(50),@NoiDungThayDoi NVARCHAR(MAX) = '',
	@MaSoHopDong_new INT , @Note NVARCHAR(50), @IsThayDoi INT,@GiaTriThucChay FLOAT,@GiaTriThucChayAd FLOAT, @IsExistData INT ,@IsExistData1 INT  ;
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
		hd.TenDangNhap
	FROM HopDong hd INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
	WHERE CONVERT(DATE,hd.LastModifiedAt) = CONVERT(DATE,@NgayThucHien)
	AND hdct.DmLoaiREF NOT IN (42)
	AND hdct.HopDongChiTietID = 91496
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
	@TenDangNhap_new

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
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
		PRINT 'check'
		PRINT  @NgayThucHien
		PRINT @HopDongID
		PRINT @HopDongChiTietID 
		PRINT @SoHopDong_new 
		PRINT @NgayDanhSo_new 
		PRINT @DmNhanVienREF_new 
		PRINT	@DmKhachHangREF_new 
		PRINT @DmSanPhamREF_new 
		PRINT @DsNhanHangREF_new 
		PRINT @HinhThucQuangCaoREF_new 
		PRINT @MaSoHopDong_new
		PRINT @TenDangNhap_new 
		PRINT 'end check'
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

		SELECT @GiaTriThucChay = SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) FROM ThucChayDaTinh tcdt WHERE tcdt.HopDongID = @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChiTietID AND tcdt.NgayThucHien < @NgayThucHien
		SELECT @GiaTriThucChayAd = SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) FROM ThucChayDaTinhAdmarket tcdt WHERE tcdt.HopDongID = @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChiTietID AND tcdt.NgayThucHien < @NgayThucHien

		SET @GiaTriThucChay = isnull(ROUND(@GiaTriThucChay,0),0)
		SET @GiaTriThucChayAd = isnull(ROUND(@GiaTriThucChayAd,0),0)

		SELECT @IsExistData = COUNT(HopDongID) FROM ThucChayDaTinh tcdt WHERE tcdt.HopDongID = @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChiTietID AND tcdt.NgayThucHien <@NgayThucHien
		SELECT @IsExistData1 = COUNT(HopDongID) FROM ThucChayDaTinhAdmarket tcdt WHERE tcdt.HopDongID = @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChiTietID AND tcdt.NgayThucHien <@NgayThucHien
		
		--SELECT @IsThayDoi

		PRINT @IsThayDoi

		IF(@IsThayDoi <> 0 AND (isnull(@GiaTriThucChay,0) <>0 OR isnull(@GiaTriThucChayAd,0) <> 0) AND (@IsExistData > 0 OR @IsExistData1 > 0))
		BEGIN
			if @IsThayDoi = 1 SET @Note = 'THAY DOI THONG TIN HOP DONG ' + @NoiDungThayDoi
			if @IsThayDoi = 2 SET @Note = 'PHAN BO BI XOA ' + @NoiDungThayDoi
			if @IsThayDoi = 3 SET @Note = 'THAY DOI DANH SACH NHAN HANG ' + @NoiDungThayDoi
			if @IsThayDoi = 4 SET @Note = 'HUY HOP DONG ' + @NoiDungThayDoi

			----CAI NAY DUNG CHO CHOT CUOI NAM 2016
			--SET @Note = 'GTTD_2016 ' + @Note
				PRINT @NgayThucHien 
					PRINT @HopDongID 
					PRINT @HopDongChiTietID 
					PRINT @SoHopDong_new 
					PRINT @NgayDanhSo_new 
					PRINT @DmNhanVienREF_new 
					PRINT @DmKhachHangREF_new 
					PRINT @DmSanPhamREF_new 
					PRINT @DsNhanHangREF_new 
					PRINT @HinhThucQuangCaoREF_new 
					PRINT @TenDangNhap_new 
					PRINT @MaSoHopDong_new  
					PRINT @Note 
					PRINT @IsThayDoi 
					PRINT @GiaTriThucChay 
					PRINT @GiaTriThucChayAd 
					PRINT @IsExistData  
					PRINT @IsExistData1   
			--EXEC [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong]
			--		-- Add the parameters for the stored procedure here
			--		@NgayThucHien ,
			--		@HopDongID ,
			--		@HopDongChiTietID ,
			--		@SoHopDong_new ,
			--		@NgayDanhSo_new ,
			--		@DmNhanVienREF_new ,
			--		@DmKhachHangREF_new ,
			--		@DmSanPhamREF_new ,
			--		@DsNhanHangREF_new ,
			--		@HinhThucQuangCaoREF_new , 
			--		@TenDangNhap_new ,
			--		@MaSoHopDong_new  , 
			--		@Note , 
			--		@IsThayDoi ,
			--		@GiaTriThucChay ,
			--		@GiaTriThucChayAd ,
			--		@IsExistData  ,
			--		@IsExistData1   
			---- 2. Thuc chay da tinh admarket
			--EXEC [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong_Admarket]
			--	-- Add the parameters for the stored procedure here
			--	@NgayThucHien ,
			--	@HopDongID ,
			--	@HopDongChiTietID ,
			--	@SoHopDong_new ,
			--	@NgayDanhSo_new ,
			--	@DmNhanVienREF_new ,
			--	@DmKhachHangREF_new ,
			--	@DmSanPhamREF_new ,
			--	@DsNhanHangREF_new ,
			--	@HinhThucQuangCaoREF_new , 
			--	@TenDangNhap_new ,
			--	@MaSoHopDong_new  , 
			--	@Note , 
			--	@IsThayDoi ,
			--	@GiaTriThucChay ,
			--	@GiaTriThucChayAd , 
			--	@IsExistData  ,
			--	@IsExistData1   

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
	@TenDangNhap_new  
	END   

	CLOSE db_cursor   
	DEALLOCATE db_cursor
	
END



```
