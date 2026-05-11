# Function: `Fn_GetQuaTrinhCongTacByNhanVienTest`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-11-29 17:34:53.187000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.520000

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
-- PRINT dbo.Fn_GetQuaTrinhCongTacByNhanVienTest('trangphamthithu','2013-01-01','2013-11-28')
CREATE FUNCTION [dbo].[Fn_GetQuaTrinhCongTacByNhanVienTest]
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
	DECLARE @StartDateString NVARCHAR(50) = @DauNhay + CONVERT(NVARCHAR(50),@StartDate) + @DauNhay;
	DECLARE @EndDateString NVARCHAR(50) = @DauNhay + CONVERT(NVARCHAR(50),@EndDate) + @DauNhay;
	
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
		
		DECLARE @ChucDanhTempTable AS TABLE (
			ChucDanhID INT,
			NgayHieuLuc DATETIME	
		)
	
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
		
		INSERT INTO @ChucDanhTempTable(ChucDanhID,NgayHieuLuc)
		SELECT A.DmChucDanhREF, A.NgayBatDauLamViec 
		FROM dbo.NhanSuQuaTrinhCongTac A
				INNER JOIN dbo.AdminPermisionHDCN B ON A.NhanSuSoYeuLyLichREF = B.NhanSuSoYeuLyLichID
		WHERE B.TenDangNhap=' + @DauNhay  + @TenDangNhap + @DauNhay + '
			--AND CONVERT(Date,A.NgayBatDauLamViec) <= ' + @DauNhay + CONVERT(NVARCHAR(50),@EndDate) + @DauNhay +'
		
		INSERT INTO @ChucDanhTempTable(ChucDanhID,NgayHieuLuc)	
		SELECT * 
		FROM
		(
			SELECT A.DmChucDanhREF, ISNULL((A.NgayNghiViec),' + @DauNhay + CONVERT(NVARCHAR(50),@MaxDate) + @DauNhay +') NgayNghiViec
			FROM dbo.NhanSuQuaTrinhCongTac A
					INNER JOIN dbo.AdminPermisionHDCN B ON A.NhanSuSoYeuLyLichREF = B.NhanSuSoYeuLyLichID
			WHERE B.TenDangNhap=' + @DauNhay  + @TenDangNhap + @DauNhay + '
		)T
		--WHERE 
			--CONVERT(Date,T.NgayNghiViec) >= ' + @DauNhay + CONVERT(NVARCHAR(50),@StartDate) + @DauNhay + '
		
		SELECT DISTINCT A.ChucDanhID, A.NgayHieuLuc 
		FROM @ChucDanhTempTable A
		ORDER BY A.NgayHieuLuc;

		SELECT * FROM @ChucDanhTempTable A 
		WHERE CONVERT(Date,A.NgayHieuLuc) BETWEEN ' + @DauNhay + CONVERT(NVARCHAR(50),@StartDate) + @DauNhay + ' AND ' + @DauNhay + CONVERT(NVARCHAR(50),@EndDate) + @DauNhay + '
		ORDER BY A.NgayHieuLuc;
		
		DECLARE CursorData CURSOR FOR		
			SELECT DISTINCT A.ChucDanhID
			FROM @ChucDanhTempTable A
			
		OPEN CursorData;
		DECLARE @ChucDanhID INT
		FETCH NEXT FROM CursorData INTO @ChucDanhID
		WHILE @@FETCH_STATUS = 0
		BEGIN
			INSERT INTO @TempTable
			SELECT 
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
				B.TenDangNhap = ' + @DauNhay + @TenDangNhap + @DauNhay + '
				AND A.DmChucDanhREF = @ChucDanhID
			
			
			FETCH NEXT FROM CursorData INTO @ChucDanhID;
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
	        
	        SELECT * FROM @TempTable WHERE DmChucDanhREF <> 36 AND DmPhongBanREF <> 14 ORDER BY NgayBatDauLamViec
	     ELSE IF 
			(EXISTS (SELECT * FROM @TempTable WHERE DmChucDanhREF IN (1,3,7))
			AND 
		   EXISTS (SELECT A.TenDangNhap
	             FROM AdminBoPhanWebsite A WHERE A.TenDangNhap = ' + @DauNhay + @TenDangNhap + @DauNhay +' AND A.DmLoaiDoiTuongREF = 1
	        ))
	        
	        SELECT * FROM @TempTable WHERE DmChucDanhREF <> 36 ORDER BY NgayBatDauLamViec
	     ELSE
	     	SELECT * FROM @TempTable ORDER BY NgayBatDauLamViec'		
		
	RETURN @Sql

END

```
