# Stored Procedure: `sp_ThucChayDaTinh_ReInsertByHopDong_ByHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-10-04 16:59:44.543000
- **Ngày sửa cuối**: 2018-04-27 15:26:12.053000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@i_HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong_ByHopDongChiTiet] '2018-04-26', 507249
CREATE PROCEDURE [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong_ByHopDongChiTiet]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME	, 
	@i_HopDongChiTietID INT

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
	@HinhThucQuangCaoREF_new INT, @TenDangNhap_new NVARCHAR(50),
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
	WHERE 1=1
	--AND	 CONVERT(DATE,hd.LastModifiedAt) = CONVERT(DATE,@NgayThucHien)
	AND hdct.HopDongChiTietID = @i_HopDongChiTietID

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

		SELECT @GiaTriThucChay = SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) FROM ThucChayDaTinh tcdt WHERE tcdt.HopDongID = @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChiTietID AND tcdt.NgayThucHien < @NgayThucHien
		SELECT @GiaTriThucChayAd = SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) FROM ThucChayDaTinhAdmarket tcdt WHERE tcdt.HopDongID = @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChiTietID AND tcdt.NgayThucHien < @NgayThucHien

		SET @GiaTriThucChay = isnull(ROUND(@GiaTriThucChay,0),0)
		SET @GiaTriThucChayAd = isnull(ROUND(@GiaTriThucChayAd,0),0)

		SELECT @IsExistData = COUNT(HopDongID) FROM ThucChayDaTinh tcdt WHERE tcdt.HopDongID = @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChiTietID AND tcdt.NgayThucHien <@NgayThucHien
		SELECT @IsExistData1 = COUNT(HopDongID) FROM ThucChayDaTinhAdmarket tcdt WHERE tcdt.HopDongID = @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChiTietID AND tcdt.NgayThucHien <@NgayThucHien
		
		--SELECT @IsThayDoi

		IF(@IsThayDoi <> 0 AND (isnull(@GiaTriThucChay,0) <>0 OR isnull(@GiaTriThucChayAd,0) <> 0) AND (@IsExistData > 0 OR @IsExistData1 > 0))
		BEGIN
			if @IsThayDoi = 1 SET @Note = 'THAY DOI THONG TIN HOP DONG'
			if @IsThayDoi = 2 SET @Note = 'PHAN BO BI XOA'
			if @IsThayDoi = 3 SET @Note = 'THAY DOI DANH SACH NHAN HANG'
			if @IsThayDoi = 4 SET @Note = 'HUY HOP DONG'
			--SELECT @GiaTriThucChay
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
