# Stored Procedure: `ThucChay_BaoCaoTheoSanPhamThoiGian`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-07 10:32:04.650000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.273000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ListSanPhamID` | `nvarchar(400)` | No |
| `@Tuan` | `int(4)` | No |
| `@Thang` | `int(4)` | No |
| `@Quy` | `int(4)` | No |
| `@Nam` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_BaoCaoTheoSanPhamThoiGian]
	@ListSanPhamID nvarchar(200),
	@Tuan int,
	@Thang int,
	@Quy int,
	@Nam int
AS
BEGIN
	DECLARE @SQLCommand nvarchar(4000)
	DECLARE @Fillter nvarchar(2000)
	DECLARE @FillterQuy varchar(2000)
		
	IF @ListSanPhamID <> '0'
		IF @Quy = 1 
			SET @FillterQuy = ' AND DATEPART( MONTH , NgayThucHien) BETWEEN 1 AND 3'
		ELSE IF @Quy = 2
			SET @FillterQuy = ' AND DATEPART( MONTH , NgayThucHien) BETWEEN 4 AND 6'
		ELSE IF @Quy = 3
			SET @FillterQuy = ' AND DATEPART( MONTH , NgayThucHien) BETWEEN 7 AND 9'
		ELSE IF @Quy = 4
			SET @FillterQuy = ' AND DATEPART( MONTH , NgayThucHien) BETWEEN 10 AND 12'
	ELSE
		IF @Quy = 1 
			SET @FillterQuy = ' DATEPART( MONTH , NgayThucHien) BETWEEN 1 AND 3'
		ELSE IF @Quy = 2
			SET @FillterQuy = ' DATEPART( MONTH , NgayThucHien) BETWEEN 4 AND 6'
		ELSE IF @Quy = 3
			SET @FillterQuy = ' DATEPART( MONTH , NgayThucHien) BETWEEN 7 AND 9'
		ELSE IF @Quy = 4
			SET @FillterQuy = ' DATEPART( MONTH , NgayThucHien) BETWEEN 10 AND 12'
		
	
	SET @SQLCommand = '
	SELECT
		DmSanPhamREF,
		TenSanPham,
		ISNULL(SUM(ThanhTienThucThu),0) AS ThanhTienThucThu
	FROM
		dbo.ThucChay_ViewBizAll
	'
	
	IF(@ListSanPhamID <> '0')
	Begin
		SET @Fillter = ' WHERE DmSanPhamREF IN (' + Convert(nvarchar(50),@ListSanPhamID)  + ')'
		
		IF @Tuan > 0 
			Begin
			SET @Fillter = @Fillter + ' AND DATEPART( Week , NgayThucHien) = ' +  Convert(nvarchar(50),@Tuan)
			SET @Fillter = @Fillter + ' AND DATEPART( YEAR , NgayThucHien) = YEAR(GETDATE())' 
			End
		ELSE IF @Thang > 0
			Begin
			SET @Fillter = @Fillter + ' AND DATEPART( MOnth , NgayThucHien) = ' +  Convert(nvarchar(50),@Thang)
			SET @Fillter = @Fillter + ' AND DATEPART( YEAR , NgayThucHien) = YEAR(GETDATE())' 
			End
		ELSE IF @Quy > 0 
			Begin
			SET @Fillter = @Fillter + @FillterQuy
			SET @Fillter = @Fillter + ' AND DATEPART( YEAR , NgayThucHien) = YEAR(GETDATE())' 
			End
		ELSE IF @Nam > 0
			SET @Fillter = @Fillter + ' AND DATEPART( YEAR , NgayThucHien) = ' +  Convert(nvarchar(50),@Nam)		
	End
	ELSE
	Begin
		SET @Fillter = ' WHERE '
		IF @Tuan > 0 
			Begin
			SET @Fillter = @Fillter + ' DATEPART( Week , NgayThucHien) = ' +  Convert(nvarchar(50),@Tuan)
			SET @Fillter = @Fillter + ' AND DATEPART( YEAR , NgayThucHien) = YEAR(GETDATE())' 
			End
		ELSE IF @Thang > 0
			Begin
			SET @Fillter = @Fillter + ' DATEPART( MOnth , NgayThucHien) = ' +  Convert(nvarchar(50),@Thang)
			SET @Fillter = @Fillter + ' AND DATEPART( YEAR , NgayThucHien) = YEAR(GETDATE())' 
			End
		ELSE IF @Quy > 0 
			Begin
			SET @Fillter = @Fillter + @FillterQuy
			SET @Fillter = @Fillter + ' AND DATEPART( YEAR , NgayThucHien) = YEAR(GETDATE())' 
			End
		ELSE IF @Nam > 0
			SET @Fillter = @Fillter + ' DATEPART( YEAR , NgayThucHien) = ' +  Convert(nvarchar(50),@Nam)
	End
	
			
	SET @SQLCommand = @SQLCommand + @Fillter
	
	SET @SQLCommand = @SQLCommand + '
	GROUP BY DmSanPhamREF, TenSanPham
	ORDER BY TenSanPham
	'
	
	print @SQLCommand
	EXEC(@SQLCommand)
	
END

```
