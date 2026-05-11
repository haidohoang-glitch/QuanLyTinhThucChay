# Stored Procedure: `ThucChay_GetLogGiatriThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-12-11 15:22:50.500000
- **Ngày sửa cuối**: 2014-12-08 15:59:29.433000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREFList` | `nvarchar(8000)` | No |
| `@DmWebsiteREFList` | `nvarchar(8000)` | No |
| `@SoHopDongList` | `nvarchar(8000)` | No |
| `@DmPhongBanREFList` | `nvarchar(8000)` | No |
| `@DmBoPhanREFList` | `nvarchar(8000)` | No |
| `@DmNhomLamViecREFList` | `nvarchar(8000)` | No |
| `@TenNhanVienList` | `nvarchar(8000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(510)` | No |
| `@DmBannerREFList` | `nvarchar(510)` | No |
| `@DonViTinhList` | `nvarchar(510)` | No |
| `@LogType` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_GetLogGiatriThayDoi]
	-- Add the parameters for the stored procedure here
	@StartDate datetime,
	@EndDate datetime,
	@DmSanPhamREFList nvarchar(4000),
	@DmWebsiteREFList nvarchar(4000),
	@SoHopDongList nvarchar(4000),
	@DmPhongBanREFList nvarchar(4000),
	@DmBoPhanREFList nvarchar(4000),
	@DmNhomLamViecREFList nvarchar(4000),
	@TenNhanVienList nvarchar(4000),
	@TenDangNhap nvarchar(50),
	@DmHinhThucQuangCaoList	NVARCHAR(255),
	@DmBannerREFList		NVARCHAR(255),
	@DonViTinhList			NVARCHAR(255),
	@LogType				INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	DECLARE @SqlCommand NVARCHAR(MAX),
			@SqlSelectString NVARCHAR(MAX),
			@SqlSecurityString NVARCHAR(MAX),
			@SqlFilterString NVARCHAR(MAX);
    DECLARE @DauNhay NVARCHAR(50);
    Declare @FilterString nvarchar(4000);
	DECLARE @GroupPermission INT;
	DECLARE @ListWebsiteID nvarchar(200), @ListSanPhamID nvarchar(200);
	DECLARE @StartDateString NVARCHAR(50) = CONVERT(NVARCHAR(50),@StartDate);
	DECLARE @EndDateString NVARCHAR(50) = CONVERT(NVARCHAR(50),@EndDate);
	
	DECLARE @Params NVARCHAR(MAX)
	SET @Params = N'@StartDateParam					datetime,
					@EndDateParam					datetime,
					@DmSanPhamREFListParam			nvarchar(512),
					@DmWebsiteREFListParam			nvarchar(512),
					@SoHopDongListParam				nvarchar(512),
					@DmPhongBanREFListParam			nvarchar(512),
					@DmBoPhanREFListParam			nvarchar(512),
					@DmNhomLamViecREFListParam		nvarchar(512),
					@TenNhanVienListParam			nvarchar(512),
					@TenDangNhapParam				nvarchar(512),
					@DmHinhThucQuangCaoListParam	nvarchar(512),
					@DmBannerREFListParam			nvarchar(512),
					@DonViTinhListParam				nvarchar(512),
					@LogTypeParam					int'	
	
	SET @DauNhay=''''
	
	SET @SqlSecurityString  ='';	
	
	SET @SqlFilterString = '
			AND A.NgayThucHien BETWEEN ' + @DauNhay + CONVERT(NVARCHAR(50),@StartDate) + @DauNhay + ' AND ' + @DauNhay + CONVERT(NVARCHAR(50),@EndDate) + @DauNhay + ' 
			AND B.NgayThucHien BETWEEN ' + @DauNhay + CONVERT(NVARCHAR(50),@StartDate) + @DauNhay + ' AND ' + @DauNhay + CONVERT(NVARCHAR(50),@EndDate) + @DauNhay + '
	';
	SET @SqlFilterString += dbo.ThucChay_GenCommandFilterString(@DmSanPhamREFList ,
																@DmWebsiteREFList,
																@SoHopDongList,
																@DmPhongBanREFList, 
																@DmBoPhanREFList, 
																@DmNhomLamViecREFList, 
																@TenNhanVienList,
																@DmHinhThucQuangCaoList,
																@DmBannerREFList,
																@DonViTinhList);
																
	IF @LogType = 1 -- for noi bo
		SET @SqlFilterString += ' AND (B.SoHopDong LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' OR B.SoHopDong LIKE ' + @DauNhay + 'SH%' + @DauNhay + ' OR B.SoHopDong LIKE ' + @DauNhay + 'soha%' + @DauNhay + ')';
	ELSE
		SET @SqlFilterString += ' AND (B.SoHopDong NOT LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' AND B.SoHopDong NOT LIKE ' + @DauNhay + 'SH%' + @DauNhay + ' AND B.SoHopDong NOT LIKE ' + @DauNhay + 'soha%' + @DauNhay + ')';
	SET @SqlSelectString = '
		SELECT DISTINCT CONVERT(NVARCHAR(50),A.NgayThucHien) AS NgayThucHien,
			A.SoHopDong,
			B.TenSanPham,
			A.NoiDungLog AS NoiDungLog
		FROM ThucChay_LogNNTinhGiaTriThayDoi A
			INNER JOIN ThucChayDaTinh B ON A.HopDongREF = B.HopDongID AND B.GiaTriThayDoi <> 0
		WHERE 1 = 1 
		UNION ALL
		SELECT DISTINCT CONVERT(NVARCHAR(50),A.NgayThucHien) AS NgayThucHien,
			A.SoHopDong,
			B.TenSanPham,
			A.NoiDungLog AS NoiDungLog
		FROM ThucChay_LogNNTinhGiaTriThayDoi A
			INNER JOIN ThucChayDaTinhAdmarket B ON A.HopDongREF = B.HopDongID AND B.GiaTriThayDoi <> 0
		WHERE 1 = 1 ';
	
	
	SET @SqlCommand = @SqlSelectString + @SqlSecurityString + @SqlFilterString;		
	
	SET @SqlCommand = '
		SELECT 
			T.NgayThucHien + ' + @DauNhay + ' - ' + @DauNhay + ' + 
			T.SoHopDong + ' + @DauNhay + ' - ' + @DauNhay + ' + 
			T.TenSanPham + ' + @DauNhay + ' - ' + @DauNhay + ' +
			T.NoiDungLog as NoiDungLog
		FROM 
		(' 
			+ @SqlCommand + 
		')T'									
    
    PRINT @SqlFilterString;
    PRINT @SqlCommand;
    
    EXECUTE sp_executesql @SqlCommand, @Params, 
		@StartDateParam					= @StartDate,
		@EndDateParam					= @EndDate,
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
		@DonViTinhListParam				= @DonViTinhList ,
		@LogTypeParam					= @LogType
    
END

```
