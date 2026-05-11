# Function: `Fn_GetQuaTrinhCongTacByNhanVien`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-25 17:01:10.410000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.630000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar` | Yes |
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
CREATE FUNCTION [dbo].[Fn_GetQuaTrinhCongTacByNhanVien]
(
	-- Add the parameters for the function here
	@TenDangNhap nvarchar(50),
	@StartDate datetime,
	@EndDate datetime
)
RETURNS varchar(MAX)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Sql varchar(MAX);
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
				1=1
				AND A.NhanSuQuaTrinhCongTacID = @QuaTrinhCongTacID
			
			
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
	     BEGIN
			PRINT ' + @DauNhay + 'Case: 1' + @DauNhay + '
	        SELECT * FROM @TempTable WHERE DmChucDanhREF <> 36 AND DmPhongBanREF <> 14
	     END
	     
	     ELSE IF (EXISTS (SELECT * FROM @TempTable WHERE DmChucDanhREF IN (7))
			AND 
		   EXISTS (SELECT A.TenDangNhap
	             FROM AdminBoPhanWebsite A WHERE A.TenDangNhap = ' + @DauNhay + @TenDangNhap + @DauNhay +' AND A.DmLoaiDoiTuongREF = 1
		   ) AND EXISTS(SELECT * FROM @TempTable  WHERE DmChucDanhREF=7 AND DmPhongBanREF=14))
	     BEGIN
			PRINT ' + @DauNhay + 'Case: 2' + @DauNhay + '   
	        SELECT MIN(NhanSuQuaTrinhCongTacID) NhanSuQuaTrinhCongTacID,
				MIN(DmPhongBanREF) DmPhongBanREF,
     			MIN(DmBoPhanREF) DmBoPhanREF,
     			MIN(DmNhomLamViecREF) DmNhomLamViecREF,
     			(DmChucDanhREF) DmChucDanhREF,
     			MIN(NgayBatDauLamViec) NgayBatDauLamViec,
     			MAX(NgayNghiViec) NgayNghiViec
	        FROM @TempTable 
	        WHERE 1 =1 AND DmChucDanhREF <> 36-- AND DmPhongBanREF <> 14
	        GROUP BY DmChucDanhREF
	     END   
	     
	     ELSE IF (EXISTS (SELECT * FROM @TempTable WHERE DmChucDanhREF IN (7))
			AND 
		   EXISTS (SELECT A.TenDangNhap
	             FROM AdminBoPhanWebsite A WHERE A.TenDangNhap = ' + @DauNhay + @TenDangNhap + @DauNhay +' AND A.DmLoaiDoiTuongREF = 1
		   ))
	     BEGIN
			PRINT ' + @DauNhay + 'Case: 3' + @DauNhay + '   
	        SELECT MIN(NhanSuQuaTrinhCongTacID) NhanSuQuaTrinhCongTacID,
				MIN(DmPhongBanREF) DmPhongBanREF,
     			MIN(DmBoPhanREF) DmBoPhanREF,
     			MIN(DmNhomLamViecREF) DmNhomLamViecREF,
     			(DmChucDanhREF) DmChucDanhREF,
     			MIN(NgayBatDauLamViec) NgayBatDauLamViec,
     			MAX(NgayNghiViec) NgayNghiViec
	        FROM @TempTable 
	        WHERE 1 =1 AND DmChucDanhREF <> 36-- AND DmPhongBanREF <> 14
	        GROUP BY DmChucDanhREF
		END
			                         
	     ELSE IF 
			(EXISTS (SELECT * FROM @TempTable WHERE DmChucDanhREF IN (1,3))
			AND 
		   EXISTS (SELECT A.TenDangNhap
	             FROM AdminBoPhanWebsite A WHERE A.TenDangNhap = ' + @DauNhay + @TenDangNhap + @DauNhay +' AND A.DmLoaiDoiTuongREF = 1
	        ))
	     BEGIN
			PRINT ' + @DauNhay + 'Case: 4' + @DauNhay + '   
	        SELECT * FROM @TempTable WHERE DmChucDanhREF <> 36
	     END
	     ELSE
	     BEGIN
			PRINT ' + @DauNhay + 'Case: 5' + @DauNhay + '
	     	SELECT 
				MIN(NhanSuQuaTrinhCongTacID) NhanSuQuaTrinhCongTacID,
				MIN(DmPhongBanREF) DmPhongBanREF,
     			MIN(DmBoPhanREF) DmBoPhanREF,
     			MIN(DmNhomLamViecREF) DmNhomLamViecREF,
     			(DmChucDanhREF) DmChucDanhREF,
     			MIN(NgayBatDauLamViec) NgayBatDauLamViec,
     			MAX(NgayNghiViec) NgayNghiViec
			 FROM @TempTable
			 GROUP BY DmChucDanhREF
		  END'		
		
	RETURN @Sql;

END

```
