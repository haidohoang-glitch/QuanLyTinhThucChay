# Stored Procedure: `BaoCaoThucChayHopDongTheoThang_GetList`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-01 13:35:44.573000
- **Ngày sửa cuối**: 2014-11-19 12:16:50.873000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@TuThang` | `int(4)` | No |
| `@TuNam` | `int(4)` | No |
| `@DenThang` | `int(4)` | No |
| `@DenNam` | `int(4)` | No |
| `@DmSanPhamREFList` | `nvarchar(8000)` | No |
| `@DmWebsiteREFList` | `nvarchar(8000)` | No |
| `@SoHopDongList` | `nvarchar(8000)` | No |
| `@DmPhongBanREFList` | `nvarchar(8000)` | No |
| `@DmBoPhanREFList` | `nvarchar(8000)` | No |
| `@DmNhomLamViecREFList` | `nvarchar(8000)` | No |
| `@TenNhanVienList` | `nvarchar(8000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(400)` | No |
| `@DmBannerREFList` | `nvarchar(400)` | No |
| `@DonViTinhList` | `nvarchar(400)` | No |
| `@TypeCondition` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-08-01
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[BaoCaoThucChayHopDongTheoThang_GetList]
	-- Add the parameters for the stored procedure here
	@PageIndex				INT = 1,
	@RecordCount			INT = 10,
	@TuThang					INT,
	@TuNam					INT,
	@DenThang					INT,
	@DenNam					INT,
	@DmSanPhamREFList		nvarchar(4000),
	@DmWebsiteREFList		nvarchar(4000),
	@SoHopDongList			nvarchar(4000),
	@DmPhongBanREFList		nvarchar(4000),
	@DmBoPhanREFList		nvarchar(4000),
	@DmNhomLamViecREFList	nvarchar(4000),
	@TenNhanVienList		nvarchar(4000),
	@TenDangNhap			nvarchar(50),
	@DmHinhThucQuangCaoList NVARCHAR(200),
	@DmBannerREFList		NVARCHAR(200),
	@DonViTinhList			NVARCHAR(200),
	@TypeCondition			INT			-- 1: Theo thuc chay, 2: Theo Hop dong
		
AS
BEGIN
	SET NOCOUNT ON;

    DECLARE @SqlString		NVARCHAR(MAX),
			@FilterString	NVARCHAR(MAX),
			@DauNhay		NVARCHAR(10);
    DECLARE @MonthList		NVARCHAR(MAX);
    
    DECLARE @ThangColumn	NVARCHAR(255),
			@NamColumn		NVARCHAR(255);	
    
    DECLARE @Pamrams NVARCHAR(MAX);
	SET @Pamrams = N'@PageIndexParam int,
					@RecordCountParam int,
					@TuThangParam int, 
					@DenThangParam int,
					@TuNamParam int, 
					@DenNamParam int,
					@DmSanPhamREFListParam nvarchar(4000), 
					@DmWebsiteREFListParam nvarchar(4000), 
					@SoHopDongListParam nvarchar(4000), 
					@DmPhongBanREFListParam nvarchar(4000), 
					@DmBoPhanREFListParam nvarchar(4000), 
					@DmNhomLamViecREFListParam nvarchar(4000), 
					@TenNhanVienListParam nvarchar(4000),
					@TenDangNhapParam nvarchar(50), 
					@DmHinhThucQuangCaoListParam NVARCHAR(200), 
					@DmBannerREFListParam NVARCHAR(200), 
					@DonViTinhListParam NVARCHAR(200),
					@TypeConditionPraram	int';
    
    SET @DauNhay = ''''
    
    SET @MonthList = dbo.GenSQLCommand_GetMonthListByMonthYear(@TuThang, @TuNam, @DenThang, @DenNam);
    
    SET @FilterString = '';
    IF (@TuNam = @DenNam) 
		SET @FilterString += ' AND ThangThucChay BETWEEN ' + CONVERT(NVARCHAR(10),@TuThang) + ' AND ' 
														   + CONVERT(NVARCHAR(10),@DenThang) + ' 
							   AND NamThucChay = ' + CONVERT(NVARCHAR(10),@TuNam);
	ELSE
	BEGIN
		SET @FilterString += ' AND ((ThangThucChay BETWEEN ' + CONVERT(NVARCHAR(10),@TuThang) + ' AND ' 
														   + CONVERT(NVARCHAR(10),12) + ' 
							   AND NamThucChay = ' + CONVERT(NVARCHAR(10),@TuNam) + ')';
							   
		SET @FilterString += ' OR (ThangThucChay BETWEEN ' + CONVERT(NVARCHAR(10),1) + ' AND ' 
														   + CONVERT(NVARCHAR(10),@DenThang) + ' 
							   AND NamThucChay = ' + CONVERT(NVARCHAR(10),@DenNam) + '))';
	END
														   
    SET @SqlString = '
		SELECT T1.*
		FROM
		(
			SELECT ROW_NUMBER() OVER (ORDER BY SoHopDong ASC) AS num, HopDongID, SoHopDong, ' + @MonthList + ' 
			FROM 
				 (
					SELECT HopDongID, SoHopDong, (CONVERT(NVARCHAR(10),ThangThucChay) + ' + @DauNhay + '-' + @DauNhay + ' + CONVERT(NVARCHAR(10),NamThucChay)) ThangNam, ThanhTienThucChayThucThu
					FROM rptThucChaySanPhamThang
					WHERE 1 = 1 ' 
						+ @FilterString + ' 
						AND ThanhTienThucChayThucThu > 0 
				) T
				PIVOT 
				(
					SUM(ThanhTienThucChayThucThu)
					FOR ThangNam IN (' + @MonthList + ')
				) P 
		)T1
		WHERE T1.num BETWEEN ' + CONVERT(NVARCHAR(20),((@PageIndex-1)*@RecordCount + 1)) + ' AND ' + CONVERT(NVARCHAR(20),(@PageIndex*@RecordCount))
    
    PRINT @SqlString;
    --EXEC(@SqlString);
    
    EXECUTE sp_executesql @SqlString, @Pamrams, 
		@PageIndexParam					= @PageIndex,
		@RecordCountParam				= @RecordCount,		
		@TuThangParam					= @TuThang,
		@DenThangParam					= @DenThang,
		@TuNamParam						= @TuNam,
		@DenNamParam					= @DenNam,
		@DmSanPhamREFListParam			= @DmSanPhamREFList,
		@DmWebsiteREFListParam			= @DmWebsiteREFList,
		@SoHopDongListParam				= @SoHopDongList,
		@DmPhongBanREFListParam			= @DmPhongBanREFList,
		@DmBoPhanREFListParam			= @DmBoPhanREFList,
		@DmNhomLamViecREFListParam		= @DmNhomLamViecREFList,
		@TenNhanVienListParam			= @TenNhanVienList,
		@TenDangNhapParam				= @TenDangNhap,
		@DmHinhThucQuangCaoListParam	= @DmHinhThucQuangCaoList,
		@DmBannerREFListParam			= @DmBannerREFList,
		@DonViTinhListParam				= @DonViTinhList,
		@TypeConditionPraram			= @TypeCondition;
	
END

```
