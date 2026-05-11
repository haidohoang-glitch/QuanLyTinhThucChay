# Function: `Fn_GetQuaTrinhCongTacByNhanVien_v01`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-11-30 12:18:19.660000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.547000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
-- PRINT dbo.Fn_GetQuaTrinhCongTacByNhanVien('thunga','2013-11-22','2013-11-22')
CREATE FUNCTION [dbo].[Fn_GetQuaTrinhCongTacByNhanVien_v01]
(
	-- Add the parameters for the function here
	@TenDangNhap nvarchar(50),
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
	
	DECLARE @ChucDanhREFList NVARCHAR(50) = '3,6,7,1'
	
	SET @DauNhay=''''
	
	SET @MaxDate = (
					SELECT TOP 1 A.NgayNghiViec FROM NhanSuQuaTrinhCongTac A
					INNER JOIN dbo.AdminPermisionHDCN B ON A.NhanSuSoYeuLyLichREF = B.NhanSuSoYeuLyLichID
					WHERE 
					A.NgayNghiViec >= @EndDate
					AND B.TenDangNhap = @TenDangNhap
					
					ORDER BY A.NgayNghiViec ASC					
					) 
	IF @MaxDate IS NULL SET @MaxDate = '3000-01-01'
	
	SET @sql = '
		DECLARE @IsHavePositon INT = 0;
		DECLARE @IsManageWebsite INT = 0;
		DECLARE @FilterString NVARCHAR(MAX);
	
		DECLARE @TempTable AS TABLE (
			NhanSuQuaTrinhCongTacID INT,
			DmPhongBanREF INT,
			DmBoPhanREF INT,
			DmNhomLamViecREF INT,
			DmChucDanhREF INT,
			NgayBatDauLamViec DATETIME,
			NgayNghiViec DATETIME
		)
		'
		SET @sql += '
		DECLARE CursorData CURSOR FOR		
			SELECT DISTINCT A.NhanSuQuaTrinhCongTacID,A.DmChucDanhREF 
			FROM dbo.NhanSuQuaTrinhCongTac A
			INNER JOIN dbo.AdminPermisionHDCN B ON A.NhanSuSoYeuLyLichREF = B.NhanSuSoYeuLyLichID
			WHERE 
			(
				(
					B.TenDangNhap = ' + @DauNhay + @TenDangNhap + @DauNhay + '
					AND ' + @DauNhay + CONVERT(NVARCHAR(50),@StartDate) + @DauNhay + ' BETWEEN CONVERT(DATE,A.NgayBatDauLamViec) AND  ISNULL(CONVERT(DATE,A.NgayNghiViec),' + @DauNhay + CONVERT(NVARCHAR(50),@MaxDate) + @DauNhay +')
				) OR 
				(
					' + @DauNhay + CONVERT(NVARCHAR(50),@EndDate) + @DauNhay + ' BETWEEN CONVERT(DATE,A.NgayBatDauLamViec) AND  ISNULL(CONVERT(DATE,A.NgayNghiViec),' + @DauNhay + CONVERT(NVARCHAR(50),@MaxDate) + @DauNhay +')
					AND B.TenDangNhap = ' + @DauNhay + @TenDangNhap + @DauNhay + '
				)
				OR 
				(
					CONVERT(DATE,A.NgayBatDauLamViec)  <= ' + @DauNhay + CONVERT(NVARCHAR(50),@EndDate) + @DauNhay + ' 
						AND  ISNULL(CONVERT(DATE,A.NgayNghiViec),' + @DauNhay + CONVERT(NVARCHAR(50),@MaxDate) + @DauNhay +') >= '  + @DauNhay + CONVERT(NVARCHAR(50),@StartDate) + @DauNhay +'
					AND B.TenDangNhap = ' + @DauNhay + @TenDangNhap + @DauNhay + '
				)
				OR 
				(
					CONVERT(DATE,A.NgayBatDauLamViec) >= ' + @DauNhay + CONVERT(NVARCHAR(50),@StartDate) + @DauNhay + ' 
						AND  CONVERT(DATE,A.NgayBatDauLamViec) <= '  + @DauNhay + CONVERT(NVARCHAR(50),@EndDate) + @DauNhay +'
					AND B.TenDangNhap = ' + @DauNhay + @TenDangNhap + @DauNhay + '
				)
			)
		OPEN CursorData;
		DECLARE @ChucDanhID INT;
		DECLARE @QuaTrinhCongTacID INT
		FETCH NEXT FROM CursorData INTO @QuaTrinhCongTacID,@ChucDanhID
		WHILE @@FETCH_STATUS = 0
		BEGIN
			INSERT INTO @TempTable
			SELECT TOP 1 
				A.NhanSuQuaTrinhCongTacID,
				A.DmPhongBanREF,
				A.DmBoPhanREF,
				A.DmNhomLamViecREF,
				A.DmChucDanhREF,
				(A.NgayBatDauLamViec) AS NgayBatDauLamViec,
				ISNULL((A.NgayNghiViec),' + @DauNhay + CONVERT(NVARCHAR(50),@MaxDate) + @DauNhay +') AS NgayNghiViec
				FROM dbo.NhanSuQuaTrinhCongTac A
				INNER JOIN dbo.AdminPermisionHDCN B ON A.NhanSuSoYeuLyLichREF = B.NhanSuSoYeuLyLichID
			WHERE 
				(
					(
						B.TenDangNhap = ' + @DauNhay + @TenDangNhap + @DauNhay + '
						AND ' + @DauNhay + CONVERT(NVARCHAR(50),@StartDate) + @DauNhay + ' BETWEEN CONVERT(DATE,A.NgayBatDauLamViec) AND  ISNULL(CONVERT(DATE,A.NgayNghiViec),' + @DauNhay + CONVERT(NVARCHAR(50),@MaxDate) + @DauNhay +')
					) OR 
					(
						' + @DauNhay + CONVERT(NVARCHAR(50),@EndDate) + @DauNhay + ' BETWEEN CONVERT(DATE,A.NgayBatDauLamViec) AND  ISNULL(CONVERT(DATE,A.NgayNghiViec),' + @DauNhay + CONVERT(NVARCHAR(50),@MaxDate) + @DauNhay +')
						AND B.TenDangNhap = ' + @DauNhay + @TenDangNhap + @DauNhay + '
					)
					OR 
					(
						CONVERT(DATE,A.NgayBatDauLamViec)  <= ' + @DauNhay + CONVERT(NVARCHAR(50),@EndDate) + @DauNhay + ' 
							AND  ISNULL(CONVERT(DATE,A.NgayNghiViec),' + @DauNhay + CONVERT(NVARCHAR(50),@MaxDate) + @DauNhay +') >= '  + @DauNhay + CONVERT(NVARCHAR(50),@StartDate) + @DauNhay +'
						AND B.TenDangNhap = ' + @DauNhay + @TenDangNhap + @DauNhay + '
					)
					OR 
					(
						CONVERT(DATE,A.NgayBatDauLamViec) >= ' + @DauNhay + CONVERT(NVARCHAR(50),@StartDate) + @DauNhay + ' 
							AND  CONVERT(DATE,A.NgayBatDauLamViec) <= '  + @DauNhay + CONVERT(NVARCHAR(50),@EndDate) + @DauNhay +'
						AND B.TenDangNhap = ' + @DauNhay + @TenDangNhap + @DauNhay + '
					)
				)
				AND A.DmChucDanhREF = @ChucDanhID
			
			
			FETCH NEXT FROM CursorData INTO @QuaTrinhCongTacID,@ChucDanhID;
		END
		CLOSE CursorData;
		DEALLOCATE CursorData;
		
		'
		
		SET @Sql += '
		IF (EXISTS (SELECT * FROM @TempTable WHERE DmChucDanhREF IN (6))
			AND 
		   EXISTS (SELECT A.TenDangNhap
	             FROM AdminBoPhanWebsite A WHERE A.TenDangNhap = ' + @DauNhay + @TenDangNhap + @DauNhay +' AND A.DmLoaiDoiTuongREF = 1
	        ))
	        
	        SELECT * FROM @TempTable WHERE DmChucDanhREF <> 36 AND DmPhongBanREF <> 14
	     ELSE IF 
			(EXISTS (SELECT * FROM @TempTable WHERE DmChucDanhREF IN (1,3,7))
			AND 
		   EXISTS (SELECT A.TenDangNhap
	             FROM AdminBoPhanWebsite A WHERE A.TenDangNhap = ' + @DauNhay + @TenDangNhap + @DauNhay +' AND A.DmLoaiDoiTuongREF = 1
	        ))
	        
	        SELECT * FROM @TempTable WHERE DmChucDanhREF <> 36
	     ELSE
	     	SELECT * FROM @TempTable'		
		
	RETURN @Sql

END

```
