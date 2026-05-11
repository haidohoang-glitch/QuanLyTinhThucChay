# Function: `ThucChay_GenSQLCommandDetailBaoCaoLechTreoHa`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-11 16:01:40.410000
- **Ngày sửa cuối**: 2014-10-14 10:39:33.403000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar(8000)` | Yes |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@ListDmSanPhamREF` | `nvarchar(400)` | No |
| `@ListSoHopDong` | `nvarchar(4000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION dbo.ThucChay_GenSQLCommandDetailBaoCaoLechTreoHa
(
	-- Add the parameters for the function here
	@StartDate DATETIME,
	@EndDate DATETIME,
	@ListDmSanPhamREF NVARCHAR(200),
	@ListSoHopDong NVARCHAR(2000),
	@TenDangNhap NVARCHAR(50)
)
RETURNS VARCHAR(8000)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Sql NVARCHAR(4000)
	DECLARE @DauNhay NVARCHAR(50)
	DECLARE @StartDateString NVARCHAR(100)
	DECLARE @EndDateString NVARCHAR(100)
	DECLARE @FillterBySanPham NVARCHAR(200)
	DECLARE @FillterByHopDong NVARCHAR(200)
	DECLARE @ListSanPham NVARCHAR(50)
	
	SET @DauNhay = ''''
	SET @StartDateString = @DauNhay + CONVERT(NVARCHAR(50),@StartDate) + @DauNhay
	SET @EndDateString = @DauNhay + CONVERT(NVARCHAR(50),@EndDate) + @DauNhay
	
	SET @ListSanPham = dbo.GetListSanPhamByNhanVien(@TenDangNhap)
	
	IF @ListSanPham <> '' 
		SET @FillterBySanPham = '  AND DmSanPhamREF IN (' + @ListSanPham + ')'
	ELSE 
		SET @FillterBySanPham = '  AND DmSanPhamREF IN (231,238,240,339,370)'
	IF @ListSoHopDong <> '' 
		SET @FillterByHopDong = ' AND DmSanPhamREF IN (' + @ListSoHopDong + ')'
	ELSE
		SET @FillterByHopDong = ''

			SET @Sql = '
					SELECT
						A.DmSanPhamREF, A.TenSanPham, A.SoHopDong,A.HopDongChiTietREF, 
						B.NgayThucHien AS NgayLechTreoHa,
						A.TenDangNhap,
						SUM(A.TongViewThucChay) AS TongViewThucChay,
						ISNULL(MAX(CAST(A.SoLuong AS BIGINT)),0) AS TongViewHopDong,
						SUM(A.SoLuongThucChayLechTreoHa) AS TongViewLechTreoHa,
						ISNULL(SUM(A.ThanhTienSauTrietKhauThucChay),0) + SUM(A.ThanhTienKM) AS ThanhTienThucChay,
						SUM(A.ThanhTienLechTreoHa) AS ThanhTienLechTreoHa
					FROM ThucChayDaTinh A
						INNER JOIN ThucChay_TienLechTreoHaTheoSanPham B ON B.SoHopDong = A.SoHopDong
					WHERE 1=1 and CONVERT(DATE,A.NgayThucHien) Between ' + @StartDateString + ' AND ' + @EndDateString + '
						AND TrangThaiHopDong <> 3 '
			SET @Sql+= @FillterBySanPham
			SET @Sql+= @FillterByHopDong
			
			SET @Sql+= '
					GROUP BY 
						A.DmSanPhamREF, A.TenSanPham, A.SoHopDong,A.HopDongChiTietREF,B.NgayThucHien,A.TenDangNhap
			'
			
	-- Return the result of the function
	RETURN @Sql

END

```
