# Stored Procedure: `ThucChay_GetDistinctDanhMuc`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-19 17:36:05.330000
- **Ngày sửa cuối**: 2014-11-19 12:16:58.463000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@GroupFieldName` | `nvarchar(100)` | No |
| `@StartDate` | `date(3)` | No |
| `@EndDate` | `date(3)` | No |
| `@DmSanPhamREFList` | `nvarchar(8000)` | No |
| `@DmWebsiteREFList` | `nvarchar(8000)` | No |
| `@SoHopDongList` | `nvarchar(8000)` | No |
| `@DmPhongBanREFList` | `nvarchar(8000)` | No |
| `@DmBoPhanREFList` | `nvarchar(8000)` | No |
| `@DmNhomLamViecREFList` | `nvarchar(8000)` | No |
| `@TenNhanVienList` | `nvarchar(8000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_GetDistinctDanhMuc]
--	-- Add the parameters for the stored procedure here
--	@GroupFieldName = 'TenSanPham',
--	@StartDate = '1/1/0001 12:00:00 AM',
--	@EndDate = '1/1/0001 12:00:00 AM',
--	@DmSanPhamREFList ='',
--	@DmWebsiteREFList ='',
--	@SoHopDongList ='',
--	@DmPhongBanREFList ='',
--	@DmBoPhanREFList ='',
--	@DmNhomLamViecREFList ='',
--	@TenNhanVienList =''

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_GetDistinctDanhMuc]
	-- Add the parameters for the stored procedure here
	@GroupFieldName nvarchar(50),
	@StartDate date,
	@EndDate date,
	@DmSanPhamREFList nvarchar(4000),
	@DmWebsiteREFList nvarchar(4000),
	@SoHopDongList nvarchar(4000),
	@DmPhongBanREFList nvarchar(4000),
	@DmBoPhanREFList nvarchar(4000),
	@DmNhomLamViecREFList nvarchar(4000),
	@TenNhanVienList nvarchar(4000)
	,@TenDangNhap nvarchar(50)
AS
BEGIN
	DECLARE @sql VARCHAR(8000) ='';

	DECLARE @DmSanPhamREFFilter NVARCHAR(4000)='';
	DECLARE @DmWebsiteREFFilter NVARCHAR(4000)='';
	DECLARE @DmSoHopDongFilter NVARCHAR(4000)='';
	DECLARE @DmPhongBanREFFilter NVARCHAR(4000)='';
	DECLARE @DmBoPhanREFFilter NVARCHAR(4000)='';
	DECLARE @DmNhomLamViecREFFilter NVARCHAR(4000)='';
	DECLARE @TenNhanVienFilter NVARCHAR(4000)='';
	
	Declare @DauNhay nvarchar(50)
	Declare @GroupByFildID nvarchar(50)
	Declare @GroupByFild nvarchar(50)
	Declare @FilterString nvarchar(4000);
	DECLARE @GroupPermission INT;
	
	DECLARE @MinDateTime NVARCHAR(200)
	
	DECLARE @PhongID INT, @BoPhanID INT, @NhomLamViecID INT, @ChucDanhID INT
	DECLARE @TuNgay DATETIME, @DenNgay DATETIME	
	DECLARE @MinDate DATETIME, @MaxDate DATETIME
	DECLARE @SqlCommand varchar(8000)
	DECLARE @Count INT
	
	DECLARE @DmHinhThucQuangCaoList NVARCHAR(200) = '';
	DECLARE @DmBannerREFList NVARCHAR(200) = '';
	
	
    SET @DauNhay = '''';
    
	
	SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)
	
	
	IF UPPER(@GroupFieldName) = 'TENSANPHAM'
	Begin
		SET @GroupByFild = 'DmSanPhamREF'
		SET @GroupByFildID = 'DmSanPhamREF AS ID' 
	End
	ELSE IF UPPER(@GroupFieldName) = 'TENWEBSITE'
		Begin
			SET @GroupByFild = 'DmWebsiteREF'
			SET @GroupByFildID = 'DmWebsiteREF AS ID' 
		End
	ELSE IF UPPER(@GroupFieldName) = 'TENPHONGBAN'
		Begin
			SET @GroupByFild = 'DmPhongBanREF'
			SET @GroupByFildID = 'DmPhongBanREF AS ID' 			
		End
	ELSE IF UPPER(@GroupFieldName) = 'TENBOPHAN'
		Begin
			SET @GroupByFild = 'DmBoPhanREF'
			SET @GroupByFildID = 'DmBoPhanREF AS ID' 			
		End
	ELSE IF UPPER(@GroupFieldName) = 'TENNHOMLAMVIEC'
		Begin
			SET @GroupByFild = 'DmNhomLamViecREF'
			SET @GroupByFildID = 'DmNhomLamViecREF AS ID' 			
		END
	ELSE IF UPPER(@GroupFieldName) = 'SOHOPDONG'
		Begin
			SET @GroupByFild = 'SoHopDong'
			SET @GroupByFildID = 'SoHopDong AS ID' 
		END
	ELSE IF UPPER(@GroupFieldName) = 'TenNhanVien'
		Begin
			SET @GroupByFild = 'TenDangNhap'
			SET @GroupByFildID = 'TenDangNhap AS ID' 					
		End		
		
	
	DECLARE @TempTable TABLE
	(
		Name nvarchar(50),
		ID nvarchar(50)
	)	
	
	SET @PhongID = 0;
	SET @BoPhanID = 0;
	SET @NhomLamViecID = 0;
	SET @ChucDanhID = 0;

	SET @sql = 'SELECT DISTINCT '
						+ @GroupFieldName+' as Name,'+@GroupByFildID+'
				FROM
				('
					+ dbo.ThucChay_GenSQLCommandForDistinctListQuery(@StartDate,
														@EndDate,
														@DmSanPhamREFList ,
														@DmWebsiteREFList ,
														@SoHopDongList ,
														@DmPhongBanREFList ,
														@DmBoPhanREFList ,
														@DmNhomLamViecREFList ,
														@TenNhanVienList,
														@TenDangNhap,
														@PhongID,
														@BoPhanID,
														@NhomLamViecID,
														@ChucDanhID,
														@DmHinhThucQuangCaoList,
														@DmBannerREFList) +
				')T
				'
	--IF (@GroupFieldName = 'TenNhanVien' OR @GroupFieldName = 'SoHopDong')
	--	SET @sql += '
	--            WHERE T.DmSanPhamREF NOT IN (5001,5003,5003) 
	--	'
	
	SET @sql += '
	        ORDER BY ' + @GroupFieldName + ' ASC'
				
	print @sql;
		
	INSERT INTO @TempTable
	EXEC (@sql);
	
	--DECLARE	@sqlAdmarket NVARCHAR(MAX),
	--		@sqlAdmarketSecurityString NVARCHAR(MAX),
	--		@sqlAdmarketFilterString NVARCHAR(MAX);
	
	--SET @sqlAdmarketSecurityString = '(';
	--	SET @sqlAdmarketSecurityString += dbo.GetSecurityDataByTenDangNhap(@StartDate,
	--															@EndDate,
	--															@TenDangNhap,
	--															'NgayThucHien',
	--															'TenDangNhap');

	--	SET @sqlAdmarketSecurityString += ' OR (' + dbo.GetSecurityWebsiteProductAdmarket(@StartDate,
	--																			@EndDate,@TenDangNhap,
	--																			'NgayThucHien',
	--																			'TenDangNhap',
	--																			'DmSanPhamREF',
	--																			'DmWebsiteREF') + 
	--											')';
	--	SET @sqlAdmarketSecurityString += ')';	
		
	--	SET @SqlAdmarketFilterString = '';
	--	SET @SqlAdmarketFilterString += dbo.ThucChayAdmarket_GetCommandFilterString(@GroupFieldName,
	--																				@DmSanPhamREFList,
	--																				@DmWebsiteREFList,
	--																				@SoHopDongList,
	--																				@DmPhongBanREFList, 
	--																				@DmBoPhanREFList, 
	--																				@DmNhomLamViecREFList, 
	--																				@TenNhanVienList);
																					
	--IF @GroupFieldName = 'TenNhanVien'													
	--BEGIN
	--	SET @sqlAdmarket = '
	--		SELECT DISTINCT 
	--			TenNhanVien,
	--			TenDangNhap				
	--		FROM ThucChayDaTinhAdmarketSale 
	--		WHERE ' + @sqlAdmarketSecurityString + @sqlAdmarketFilterString + '
	--			AND (TongClick > 0 OR TongTienThucChay > 0 OR TongTienKhuyenmai > 0 OR SoLuongThucChay > 0) 
	--		';
		
	--	INSERT INTO @TempTable
	--	EXEC(@sqlAdmarket);	
	--END
	--ELSE IF @GroupFieldName = 'SoHopDong'
	--BEGIN
	--	SET @sqlAdmarket = '
	--		SELECT DISTINCT
	--			SoHopDong,
	--			SoHopDong AS ID
	--		FROM ThucChayDaTinhAdmarketHopDong
	--		WHERE ' + @sqlAdmarketSecurityString + @sqlAdmarketFilterString + '
	--			AND (TongClick > 0 OR TongTienThucChay > 0 OR TongTienKhuyenmai > 0) 
	--		';
			
	--	INSERT INTO @TempTable
	--	EXEC(@sqlAdmarket);	
		
	--	PRINT @sqlAdmarket;
	--END			
	
	SELECT DISTINCT
		ID, Name
	FROM @TempTable
	ORDER BY Name;
END

```
