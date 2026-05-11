# Function: `GetSecurityDataByTenDangNhap`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-12-04 09:27:35.853000
- **Ngày sửa cuối**: 2015-07-17 12:22:55.007000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar(8000)` | Yes |
| `@ThoiGianBatDau` | `datetime(8)` | No |
| `@ThoiGianKetThuc` | `datetime(8)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@ThoiGianColumn` | `varchar(50)` | No |
| `@TenDangNhapColumn` | `varchar(50)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
-- PRINT dbo.GetSecurityDataByTenDangNhapTest('2013-06-01','2013-09-30','lananhphamthi','NgayThucHien','TenDangNhap')
CREATE FUNCTION [dbo].[GetSecurityDataByTenDangNhap] 
(
	--Thời gian thực hiện
	 @ThoiGianBatDau DATETIME
	,@ThoiGianKetThuc DATETIME
	,@TenDangNhap nvarchar(50)
	,@ThoiGianColumn VARCHAR(50)
	,@TenDangNhapColumn VARCHAR(50)
)
RETURNS varchar(8000)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @FilterSecurity varchar(8000);
	DECLARE @GroupPermision INT;
	DECLARE @DauNhay VARCHAR(10) = '''';
	DECLARE @ListWebsiteID VARCHAR(200), @ListSanPhamID VARCHAR(200);
	DECLARE @ExistsTenDangNhap INT;
	
	DECLARE @isInternalChanelVcc INT = 0
	
	SET @isInternalChanelVcc = dbo.ThucChay_CheckIsInternalChanelVcc(@TenDangNhap);
	
	IF (EXISTS(SELECT username FROM AdminUser A WHERE A.Username = @TenDangNhap))
	BEGIN
		
		DECLARE @QuaTrinhCongTacTemp TABLE
		(
		  NhanSuQuaTrinhCongTacID int, 
		  DmPhongBanREF INT,
		  DmBoPhanREF INT,
		  DmNhomLamViecREF INT,
		  DmChucDanhREF INT,
		  TuNgay DATETIME,
		  DenNgay DATETIME
		)
			
		SET @ListWebsiteID = dbo.GetListWebsiteByNhanVien(@TenDangNhap)
		SET @ListSanPhamID = dbo.GetListSanPhamByNhanVien(@TenDangNhap) 
		
		
		
		SET @GroupPermision = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap);

		-- Add the T-SQL statements to compute the return value here
		SET @FilterSecurity = '1=1'
		
		-- Neu co quyen xem full du lieu
		IF @GroupPermision = -1
		BEGIN
			SET @FilterSecurity += ' AND CONVERT(DATE,' + @ThoiGianColumn + ') BETWEEN ' + @DauNhay + CONVERT(VARCHAR(50),@ThoiGianBatDau) + @DauNhay + ' AND ' +  + @DauNhay + CONVERT(VARCHAR(50),@ThoiGianKetThuc) + @DauNhay;
		END		
		ELSE
		BEGIN
			SET @FilterSecurity = @FilterSecurity + ' AND ('
			
			DECLARE @QuaTrinhCongTacID INT, @PhongBanREF INT, @BoPhanREF INT, @NhomLamViecREF INT, @ChucDanhREF INT, 
					@TuNgay DATETIME, @DenNgay DATETIME, @MinDate DATETIME, @MaxDate DATETIME
			DECLARE @i INT = 0, @Count INT = 0;
			
			
			INSERT INTO @QuaTrinhCongTacTemp
			SELECT  
				A.NhanSuQuaTrinhCongTacID,A.DmPhongBanREF,A.DmBoPhanREF,A.DmNhomLamViecREF, A.DmChucDanhREF,
				A.NgayBatDauLamViec,ISNULL(ISNULL(A.NgayNghiViec, A.NgayKetThucLamViec) ,'3000-01-01') AS NgayNghiViec
			FROM dbo.NhanSuQuaTrinhCongTac A
			INNER JOIN dbo.AdminPermisionHDCN B ON A.NhanSuSoYeuLyLichREF = B.NhanSuSoYeuLyLichID
			WHERE
				B.TenDangNhap = @TenDangNhap
				AND 
				(
					(
						@ThoiGianBatDau BETWEEN CONVERT(DATE,A.NgayBatDauLamViec) AND  ISNULL(CONVERT(DATE,A.NgayNghiViec),'Jan  1 3000 12:00AM')
					) OR 
					(
						@ThoiGianKetThuc BETWEEN CONVERT(DATE,A.NgayBatDauLamViec) AND  ISNULL(CONVERT(DATE,A.NgayNghiViec),'Jan  1 3000 12:00AM')
					)
					OR 
					(
						CONVERT(DATE,A.NgayBatDauLamViec)  <= @ThoiGianKetThuc
							AND  ISNULL(CONVERT(DATE,A.NgayNghiViec),'Jan  1 3000 12:00AM') >= @ThoiGianBatDau
					)
					OR 
					(
						CONVERT(DATE,A.NgayBatDauLamViec) BETWEEN @ThoiGianBatDau AND @ThoiGianKetThuc
							
					)
				)
				
			SET @Count = (SELECT COUNT(*) FROM @QuaTrinhCongTacTemp);
			SET @MinDate = (SELECT MIN(TuNgay) FROM @QuaTrinhCongTacTemp);
			SET @MaxDate = (SELECT MAX(DenNgay) FROM @QuaTrinhCongTacTemp);
			
			IF @Count > 0 
			BEGIN
				DECLARE CursorData CURSOR FOR
					SELECT * FROM @QuaTrinhCongTacTemp
			
				OPEN CursorData;
				FETCH NEXT FROM CursorData INTO @QuaTrinhCongTacID,@PhongBanREF,@BoPhanREF,@NhomLamViecREF,@ChucDanhREF,@TuNgay,@DenNgay
				WHILE @@FETCH_STATUS = 0
				BEGIN 
	   				IF @i > 0
	   					SET @FilterSecurity = @FilterSecurity + ' OR '
	   				
	   				IF (@Count = 1)
	   				BEGIN
	   					IF @MinDate < @ThoiGianBatDau
	   						SET @TuNgay = @ThoiGianBatDau;
	   					IF @MaxDate > @ThoiGianKetThuc
	   						SET @DenNgay = @ThoiGianKetThuc;
	   				END 
	   				ELSE IF (@Count >1)
   					BEGIN
   						IF (@i = 0 AND @MinDate <  @ThoiGianBatDau)
   							SET @TuNgay = @ThoiGianBatDau;
   						IF (@DenNgay = '3000-01-01')
   							SET @DenNgay = @ThoiGianKetThuc;
   					END	
		   		
	   				SET @FilterSecurity += ' ('
		   		
	   				SET @FilterSecurity += ' CONVERT(DATE,' + @ThoiGianColumn + ') BETWEEN ' + @DauNhay + CONVERT(VARCHAR(50),@TuNgay) + @DauNhay + ' AND ' +  + @DauNhay + CONVERT(VARCHAR(50),@DenNgay) + @DauNhay;
		   			
	   				SET @FilterSecurity += ' AND (' + @TenDangNhapColumn + ' = ' + @DauNhay + @TenDangNhap + @DauNhay;
		   		
	   				-- Neu la Truong phong, Pho phong
	   				IF (@ChucDanhREF = 3 OR @ChucDanhREF = 6) 
	   					SET @FilterSecurity += ' OR ' + 'DmPhongBanREF = ' + CONVERT(VARCHAR(50),@PhongBanREF);
		   		
	   				-- Neu la Trưởng bộ phận	
	   				ELSE IF (@ChucDanhREF = 7) 
						SET @FilterSecurity += ' OR ' + 'DmBoPhanREF = ' + Convert(VARCHAR(50),@BoPhanREF)
				
					-- Neu la Truong nhóm
					ELSE IF (@ChucDanhREF = 1) 
						SET @FilterSecurity += ' OR ' +'DmNhomlamViecREF = ' + Convert(nvarchar(50),@NhomlamViecREF)
				
					SET @FilterSecurity += '))'
				
					SET @i += 1;
					FETCH NEXT FROM CursorData INTO @QuaTrinhCongTacID,@PhongBanREF,@BoPhanREF,@NhomLamViecREF,@ChucDanhREF,@TuNgay,@DenNgay
				END
				CLOSE CursorData;
				DEALLOCATE CursorData;
			END
			ELSE
				SET @FilterSecurity += ' TenDangNhap = ' + @DauNhay + @TenDangNhap + @DauNhay
			
			SET @FilterSecurity += ')'
		END
	END
	
	ELSE
		SET @FilterSecurity = ' 1 <> 1'

	-- Return the result of the function
	RETURN @FilterSecurity

END

```
