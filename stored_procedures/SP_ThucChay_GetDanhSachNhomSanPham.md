# Stored Procedure: `ThucChay_GetDanhSachNhomSanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-20 17:39:16.703000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.910000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-11-16
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_GetDanhSachNhomSanPham]
	@StartDate datetime,
	@EndDate datetime,
	@TenDangNhap nvarchar(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @Sql VARCHAR(MAX);
    DECLARE @DauNhay NVARCHAR(50);
    Declare @GroupByFildID nvarchar(4000);
	Declare @GroupByFild nvarchar(4000);
	Declare @FilterString nvarchar(4000);
	DECLARE @GroupPermission INT;
	DECLARE @PhongID INT, @BoPhanID INT, @NhomLamViecID INT, @ChucDanhID INT
	DECLARE @TuNgay DATETIME, @DenNgay DATETIME	
	DECLARE @MinDate DATETIME, @MaxDate DATETIME
	DECLARE @SqlCommand VARCHAR(MAX);
	DECLARE @Count int
	
	DECLARE @ToUserName NVARCHAR(50)
	
	DECLARE @OrderByField NVARCHAR(50)
	DECLARE @Function NVARCHAR(50)
	DECLARE @SortColum nvarchar(50)

	DECLARE @DmSanPhamREFList nvarchar(4000) = N'',
			@DmWebsiteREFList nvarchar(4000) = N'',
			@SoHopDongList nvarchar(4000) = N'',
			@DmPhongBanREFList nvarchar(4000) = N'',
			@DmBoPhanREFList nvarchar(4000) = N'',
			@DmNhomLamViecREFList nvarchar(4000) = N'',
			@TenNhanVienList nvarchar(4000) = N''
	
	
    SET @DauNhay = '''';
    SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)
    
    SET @ToUserName = (SELECT ToUserName FROM MappingUser A WHERE A.FromUserName = @TenDangNhap)
	
	IF @ToUserName IS NOT NULL
		SET @TenDangNhap = @ToUserName   

	IF OBJECT_ID('tempdb..#TableResult') IS NOT NULL
		BEGIN
			DROP TABLE #TableResult
		END
			
	CREATE TABLE #TableResult
	(
		ID int,
		Name nvarchar(50)
	)

	INSERT INTO #TableResult(ID,Name) VALUES(-1, N'-- Tất cả --')
	
	SET @Sql = '
			SELECT DISTINCT 
				DmHinhThucQuangCao,
				TenHinhThucQuangCao
			FROM ThucChayDaTinh A
			WHERE 1=1
				AND A.NgayThucHien BETWEEN ' + @DauNhay + CONVERT(NVARCHAR(30),@StartDate) + @DauNhay + ' AND ' + @DauNhay + CONVERT(NVARCHAR(30),@EndDate) + @DauNhay + '
				
			ORDER BY A.TenHinhThucQuangCao
		'
	
	PRINT @Sql;
		
	INSERT INTO #TableResult(ID,Name)
	EXEC (@Sql)

	SELECT DISTINCT
		ID, Name
	FROM #TableResult
	ORDER BY Name

	DROP TABLE #TableResult
END

```
