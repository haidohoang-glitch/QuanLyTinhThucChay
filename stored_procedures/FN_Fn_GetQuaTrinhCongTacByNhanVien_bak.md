# Function: `Fn_GetQuaTrinhCongTacByNhanVien_bak`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-11-26 10:05:41.313000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.603000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@TenDanNhap` | `nvarchar(100)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[Fn_GetQuaTrinhCongTacByNhanVien_bak]
(
	-- Add the parameters for the function here
	@TenDanNhap nvarchar(50),
	@StartDate datetime,
	@EndDate datetime
)
RETURNS nvarchar(4000)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Sql nvarchar(4000);
	DECLARE @DauNhay nvarchar(50);
	DECLARE @MaxDate DATETIME;
	DECLARE @FixDate DATETIME = '3000-01-01';
	DECLARE @IsHavePositon INT = 0;
	DECLARE @IsManageWebsite INT = 0;
	DECLARE @FilterString NVARCHAR(MAX);
	
	SET @DauNhay=''''
	
	--DECLARE @StartDate datetime,@EndDate DATETIME, @TenDanNhap nvarchar(50)
	
	--SET @StartDate = '2013-08-01'
	--SET @EndDate = '2013-08-30'
	--SET @TenDanNhap = 'lananhphamthi'
	
	SET @MaxDate = (
					SELECT TOP 1 A.NgayNghiViec FROM NhanSuQuaTrinhCongTac A
					INNER JOIN dbo.AdminPermisionHDCN B ON A.NhanSuSoYeuLyLichREF = B.NhanSuSoYeuLyLichID
					WHERE 
					A.NgayNghiViec >= @EndDate
					AND B.TenDangNhap = @TenDanNhap
					
					ORDER BY A.NgayNghiViec ASC					
					) 
	IF @MaxDate IS NULL SET @MaxDate = '3000-01-01'
	
	IF EXISTS(
		SELECT
			A.NhanSuQuaTrinhCongTacID,
			A.DmPhongBanREF,
			A.DmBoPhanREF,
			A.DmNhomLamViecREF,
			A.DmChucDanhREF,
			A.NgayBatDauLamViec,
			ISNULL(A.NgayNghiViec,@MaxDate) AS NgayNghiViec
			FROM dbo.NhanSuQuaTrinhCongTac A
			INNER JOIN dbo.AdminPermisionHDCN B ON A.NhanSuSoYeuLyLichREF = B.NhanSuSoYeuLyLichID
			WHERE 
			(
				(
					B.TenDangNhap = @TenDanNhap
					AND @StartDate BETWEEN CONVERT(DATE,A.NgayBatDauLamViec) AND  ISNULL(CONVERT(DATE,A.NgayNghiViec),@MaxDate)
				) OR 
				(
					@EndDate BETWEEN CONVERT(DATE,A.NgayBatDauLamViec) AND  ISNULL(CONVERT(DATE,A.NgayNghiViec),@MaxDate)
					AND B.TenDangNhap = @TenDanNhap
				)
			) 
			AND A.DmChucDanhREF IN (3,6,7,1)	
	)
		SET @IsHavePositon = 1;
		
	IF EXISTS (SELECT A.TenDangNhap
	             FROM AdminBoPhanWebsite A WHERE A.TenDangNhap = @TenDanNhap AND A.DmLoaiDoiTuongREF = 1)
		SET @IsManageWebsite = 1;
		
	SET @FilterString = 
	'
		((
			B.TenDangNhap = '+ @DauNhay + @TenDanNhap + @DauNhay +'
			AND ' + @DauNhay + CONVERT(nvarchar(50),@StartDate)+ @DauNhay+' BETWEEN CONVERT(DATE,A.NgayBatDauLamViec) AND  ISNULL(CONVERT(DATE,A.NgayNghiViec),'+@DauNhay + CONVERT(nvarchar(50),@MaxDate) + @DauNhay + ')
		)
		
		OR 
		
		(
			' + @DauNhay + CONVERT(nvarchar(50),@MaxDate)+ @DauNhay+' BETWEEN CONVERT(DATE,A.NgayBatDauLamViec) AND  ISNULL(CONVERT(DATE,A.NgayNghiViec),'+@DauNhay + CONVERT(nvarchar(50),@MaxDate) + @DauNhay + ')
			AND B.TenDangNhap = '+ @DauNhay + @TenDanNhap + @DauNhay +'
		))
	'
	
	IF (@IsHavePositon = 1 AND @IsManageWebsite = 1)
		SET @FilterString += ' AND A.DmChucDanhREF <> 36'
	
	SET @Sql = 'SELECT 
		A.NhanSuQuaTrinhCongTacID,
		A.DmPhongBanREF,
		A.DmBoPhanREF,
		A.DmNhomLamViecREF,
		A.DmChucDanhREF,
		A.NgayBatDauLamViec,
		ISNULL(A.NgayNghiViec,' + @DauNhay + CONVERT(nvarchar(50),@MaxDate)+ @DauNhay + ') AS NgayNghiViec
		
		FROM dbo.NhanSuQuaTrinhCongTac A
		INNER JOIN dbo.AdminPermisionHDCN B ON A.NhanSuSoYeuLyLichREF = B.NhanSuSoYeuLyLichID
		WHERE ' + @FilterString + '
		ORDER BY A.NgayBatDauLamViec ASC'
		
	RETURN @Sql

END

```
