# Function: `ThucChay_GenSQLCommandBaoCaoLechTreoHa`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-08-01 12:09:57.860000
- **Ngày sửa cuối**: 2014-10-14 10:39:33.533000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@ListDmSanPhamREF` | `nvarchar(400)` | No |
| `@ListSoHopDong` | `nvarchar(4000)` | No |
| `@ListTenNhanVien` | `nvarchar(4000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@DmPhongBanREF` | `int(4)` | No |
| `@DmBoPhanREF` | `int(4)` | No |
| `@DmNhomlamViecREF` | `int(4)` | No |
| `@DmChucDanhREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GenSQLCommandBaoCaoLechTreoHa]
(
	-- Add the parameters for the function here
	@StartDate DATETIME,
	@EndDate DATETIME,
	@ListDmSanPhamREF NVARCHAR(200),
	@ListSoHopDong NVARCHAR(2000),
	@ListTenNhanVien NVARCHAR(2000),
	@TenDangNhap NVARCHAR(50),
	@DmPhongBanREF int,
	@DmBoPhanREF int,
	@DmNhomlamViecREF int,
	@DmChucDanhREF int
)
RETURNS NVARCHAR(4000)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ReturnValue NVARCHAR(4000)
	DECLARE @Sql NVARCHAR(4000)
	DECLARE @DauNhay NVARCHAR(50)
	DECLARE @FilterString VARCHAR(4000);
	DECLARE @StartDateString NVARCHAR(100)
	DECLARE @EndDateString NVARCHAR(100)
	DECLARE @FillterBySanPham NVARCHAR(200)
	DECLARE @FillterByHopDong NVARCHAR(200)
	DECLARE @ListSanPham NVARCHAR(50)
	DECLARE @DmWebsiteREFList NVARCHAR(200), @DmPhongBanREFList NVARCHAR(200), @DmBoPhanREFList NVARCHAR(200), @DmNhomLamViecREFList NVARCHAR(200),
			@DmHinhThucQuangCaoList NVARCHAR(200) = '', @DmBannerREFList NVARCHAR(200)=''

	SET @DauNhay = ''''
	
	SET @FilterString =  dbo.GetThucChayFilterString(
														@StartDate ,
														@EndDate ,
														@ListDmSanPhamREF ,
														@DmWebsiteREFList ,
														@ListSoHopDong ,
														@DmPhongBanREFList ,
														@DmBoPhanREFList ,
														@DmNhomLamViecREFList ,
														@ListTenNhanVien,
														@TenDangNhap,
														@DmPhongBanREF,
														@DmBoPhanREF,
														@DmNhomLamViecREF,
														@DmChucDanhREF,
														@DmHinhThucQuangCaoList,
														@DmBannerREFList 
													)	

	SET @Sql = '
			SELECT 
				A.DmSanPhamREF, A.TenSanPham,
				A.SoHopDong, A.HopDongChiTietREF,
				A.TenNhanVien, A.TenDangNhap, 
				MAX(A.NgayKyHopDong) AS NgayKyHopDong,
				--A.NgayThucHien AS NgayLechTreoHa,
				--SUM(A.TongViewThucChay) AS TongViewThucChay,
				--[dbo].[ThucChay_TongViewDenNgay_CPM](A.NgayThucHien,A.SoHopDong,A.DmSanPhamREF,A.HopDongChiTietREF) AS TongViewThucChay,
				(SELECT SUM(B.TongViewThucChay) FROM ThucChayDaTinh B WHERE B.SoHopDong = A.SoHopDong AND CONVERT(DATE, B.NgayThucHien) <= ' + @DauNhay + Convert(nvarchar(50),@EndDate) + @DauNhay + ')AS TongViewThucChay,
				MAX(A.SoLuong) AS TongViewHopDong,
				SUM(A.SoLuongThucChayLechTreoHa) AS TongViewLechTreoHa,
				--(SUM(A.ThanhTienSauTrietKhauThucChay) + SUM(A.ThanhTienKM) + SUM(A.ThanhTienLechTreoHa)) AS ThanhTienThucChay,
				--[dbo].[ThucChay_TongThanhTienThucChayDenNgay_CPM](A.NgayThucHien,A.SoHopDong,A.DmSanPhamREF,A.HopDongChiTietREF) AS ThanhTienThucChay,
				(SELECT SUM(B.ThanhTienSauTrietKhauThucChay + B.ThanhTienKM + B.ThanhTienLechTreoHa) FROM ThucChayDaTinh B WHERE B.SoHopDong = A.SoHopDong AND CONVERT(DATE, B.NgayThucHien) <= ' + @DauNhay + Convert(nvarchar(50),@EndDate) + @DauNhay + ')AS ThanhTienThucChay,
				SUM(A.ThanhTienLechTreoHa) AS ThanhTienLechTreoHa
			FROM ThucChayDaTinh A
			WHERE 
				A.SoLuongThucChayLechTreoHa > 0 AND 
			'
	SET @Sql = @Sql +@FilterString +
			'		
			GROUP BY A.DmSanPhamREF, A.TenSanPham,
				A.SoHopDong, A.HopDongChiTietREF, 
				A.TenNhanVien, A.TenDangNhap
			'

	-- Return the result of the function
	RETURN @Sql
	--RETURN @ListSanPham

END

```
