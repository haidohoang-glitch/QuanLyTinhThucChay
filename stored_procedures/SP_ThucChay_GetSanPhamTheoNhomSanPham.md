# Stored Procedure: `ThucChay_GetSanPhamTheoNhomSanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-07-03 15:39:24.090000
- **Ngày sửa cuối**: 2014-11-19 12:16:56.237000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@NhomSanPham` | `int(4)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
--EXEC dbo.ThucChay_GetSanPhamTheoNhomSanPham
--@NhomSanPham = 1

-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-06-05
-- Description:	GetSanPhamTheoNhomSanPham
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_GetSanPhamTheoNhomSanPham] 
	-- Add the parameters for the stored procedure here
	@StartDate DATETIME,
	@EndDate DATETIME,
	@NhomSanPham INT, -- 0: all, 1: CPD, 2: CPM; 3: PR; 4: Admarket
	@TenDangNhap nvarchar(50)
AS
BEGIN
	
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
	DECLARE @QuaTrinhCongTacTemp TABLE
	(
	  NhanSuID int, 
	  PhongBanREF INT,
	  BoPhanREF INT,
	  NhomLamViecREF INT,
	  ChucDanhREF INT,
	  TuNgay DATETIME,
	  DenNgay DATETIME
	)
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
		
	SET @FilterString = 'NgayThucHien BETWEEN ' + @DauNhay + CONVERT(NVARCHAR(50),@StartDate) + @DauNhay + ' AND ' + @DauNhay + CONVERT(NVARCHAR(50),@EndDate) + @DauNhay
	
	IF @NhomSanPham <> '' AND @NhomSanPham <> '-1' 
		SET @FilterString += ' AND DmHinhThucQuangCao = ' + CONVERT(NVARCHAR(50), @NhomSanPham)
	
	-- PHAN QUYEN DU LIEU THEO CAP BAC	
	SET @FilterString += ' AND ('
	SET @FilterString += ' ('
	SET @FilterString += dbo.GetSecurityDataByTenDangNhap(@StartDate,@EndDate,@TenDangNhap,'NgayThucHien','TenDangNhap');
	SET @FilterString += ' )'
	
	-- PHAN QUYEN DU LIEU THEO CHIEU QUAN LY SAN PHAM, WEBSITE
	SET @FilterString += ' OR ('
	SET @FilterString += dbo.GetSecurityWebsiteProduct(@StartDate,@EndDate,@TenDangNhap,'NgayThucHien','TenDangNhap','DmSanPhamREF','DmWebsiteREF');
	SET @FilterString += ' )'
	
	SET @FilterString += ' )'

	SET @Sql = '
			SELECT DISTINCT 
					DmSanPhamREF AS ID, 
					TenSanPham AS Name
				FROM ThucChayDaTinh A
				WHERE ' + @FilterString + '
					AND (A.SoLuongThucChay <> 0 OR A.SoLuongThucChayKM <> 0 OR A.ThanhTienSauTrietKhauThucChay <> 0 OR A.ThanhTienKM <> 0 OR A.GiaTriThayDoi <> 0) 
			ORDER BY A.TenSanPham
		'
	
	PRINT @Sql;
	EXEC (@Sql);
END

```
