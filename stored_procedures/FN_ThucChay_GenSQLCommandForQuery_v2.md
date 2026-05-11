# Function: `ThucChay_GenSQLCommandForQuery_v2`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-18 14:46:59.847000
- **Ngày sửa cuối**: 2014-10-14 10:39:33.130000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar` | Yes |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREFList` | `nvarchar(8000)` | No |
| `@DmWebsiteREFList` | `nvarchar(8000)` | No |
| `@SoHopDongList` | `nvarchar(8000)` | No |
| `@DmPhongBanREFList` | `nvarchar(8000)` | No |
| `@DmBoPhanREFList` | `nvarchar(8000)` | No |
| `@DmNhomLamViecREFList` | `nvarchar(8000)` | No |
| `@TenNhanVienList` | `nvarchar(8000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@DmPhongREF` | `int(4)` | No |
| `@DmBoPhanREF` | `int(4)` | No |
| `@DmNhomLamViecREF` | `int(4)` | No |
| `@DmChucDanhREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-09-02
-- Description:	ThucChay_GenSQLCommandForQuery 
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GenSQLCommandForQuery_v2] 
(
	@StartDate datetime,
	@EndDate datetime,
	@DmSanPhamREFList nvarchar(4000),
	@DmWebsiteREFList nvarchar(4000),
	@SoHopDongList nvarchar(4000),
	@DmPhongBanREFList nvarchar(4000),
	@DmBoPhanREFList nvarchar(4000),
	@DmNhomLamViecREFList nvarchar(4000),
	@TenNhanVienList nvarchar(4000),
	@TenDangNhap NVARCHAR(50),
	@DmPhongREF int,
	@DmBoPhanREF int,
	@DmNhomLamViecREF int,
	@DmChucDanhREF int
)
RETURNS VARCHAR(MAX)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Sql VARCHAR(MAX)
	DECLARE @DauNhay VARCHAR(50)
	DECLARE @FilterString VARCHAR(4000);
	DECLARE @ChucDanhID INT
	DECLARE @GroupPermission INT;
	
	SET @DauNhay = ''''
	SET @ChucDanhID = dbo.NhanSuGetChucDanhByNhanVien(@TenDangNhap)
	SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)
	
	--IF @GroupPermission <> -1
	--BEGIN
	--	IF @DmSanPhamREFList = '' 
	--	SET @DmSanPhamREFList = dbo.GetListSanPhamByNhanVien(@TenDangNhap)
		
	--	IF @DmWebsiteREFList = ''
	--		SET @DmWebsiteREFList = dbo.GetListWebsiteByNhanVien(@TenDangNhap)	
		
	--	IF @DmSanPhamREFList = ''
	--	BEGIN	
	--		IF @TenNhanVienList = ''
	--			SET @TenNhanVienList = dbo.Fn_NhanSu_GetListNhanVienByChucDanh(@TenDangNhap)
				
	--		IF @TenNhanVienList = ''
	--			SET @TenNhanVienList = dbo.Fn_NhanSu_GetListNhanVienByChucDanh(@TenDangNhap)
				
	--		IF @TenNhanVienList = ''
	--			SET @TenNhanVienList = dbo.Fn_NhanSu_GetListNhanVienByChucDanh(@TenDangNhap)

	--		IF @TenNhanVienList = ''
	--			SET @TenNhanVienList = dbo.Fn_NhanSu_GetListNhanVienByChucDanh(@TenDangNhap)
	--	END
	--END
	
	
	
	SET @FilterString =  dbo.GetThucChayFilterString_v2(
														@StartDate ,
														@EndDate ,
														@DmSanPhamREFList ,
														@DmWebsiteREFList ,
														@SoHopDongList ,
														@DmPhongBanREFList ,
														@DmBoPhanREFList ,
														@DmNhomLamViecREFList ,
														@TenNhanVienList,
														@TenDangNhap,
														@DmPhongREF,
														@DmBoPhanREF,
														@DmNhomLamViecREF,
														@DmChucDanhREF
													)	

	-- Add the T-SQL statements to compute the return value here
	SET @Sql = '
		SELECT
			A.DmSanPhamREF, A.TenSanPham, A.SoHopDong,A.HopDongChiTietREF, A.NgayThucHien, A.DonViTinh,A.isKhuyenMai, A.LechBooking,
			A.TenWebsite,A.DmWebsiteREF, A.TenPhongBan, A.DmPhongBanREF, A.TenBoPhan, A.DmBoPhanREF, A.TenNhomLamViec, A.DmNhomLamViecREF,
			A.SysNhanVienREF, A.TenDangNhap,TenNhanVien,
			A.SoLuongHopDongNoiBo, A.SoLuongHopDongKhuyenMai,A.SoLuongHopDongThucThu,
			A.SoLuongThucChayNoiBo, A.SoLuongThucChayKhuyenMai, A.SoLuongThucChayThucThu,
			A.ThanhTienThucChayNoiBo, A.ThanhTienThucChayKhuyenMai, A.ThanhTienThucChaySauChietKhau,
			A.ThanhTienThucThu AS ThanhTienThucChayThucThu
		FROM
		(
			SELECT
				DmSanPhamREF, TenSanPham, SoHopDong,HopDongChiTietREF, MAX(NgayThucHien) AS NgayThucHien,
				TenWebsite, DmWebsiteREF, TenPhongBan, DmPhongBanREF, TenBoPhan, DmBoPhanREF, TenNhomLamViec, DmNhomLamViecREF,
				SysNhanVienREF,TenDangNhap,TenNhanVien,
				dbo.FormatDonViTinh(DonViTinh) AS DonViTinh,isKhuyenMai,
				CASE WHEN SoLuongDotChayHD <> SoLuongDotChayBooking THEN ' + @DauNhay + 'True' + @DauNhay + '
								ELSE ' + @DauNhay + 'False' + @DauNhay + ' 
				END AS LechBooking,
				CASE WHEN UPPER(TenMaHopDong) LIKE ' + @DauNhay +'NB%' + @DauNhay +' THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
					ELSE 0
				END AS SoLuongHopDongNoiBo,
				CASE WHEN ThanhTienKM > 0 THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
					ELSE 0
				END AS SoLuongHopDongKhuyenMai,
				CASE WHEN (ThanhTienKM = 0 AND UPPER(TenMaHopDong) NOT LIKE '+ @DauNhay + 'NB%'+ @DauNhay +') THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
					ELSE 0
				END AS SoLuongHopDongThucThu,
				CASE WHEN UPPER(TenMaHopDong) LIKE '+ @DauNhay +'NB%'+ @DauNhay +' THEN ISNULL(SUM(SoLuongThucChay),0) 
					ELSE 0
				END AS SoLuongThucChayNoiBo,
				ISNULL(SUM(SoLuongThucChayKM),0) AS SoLuongThucChayKhuyenMai,
				CASE WHEN UPPER(TenMaHopDong) NOT LIKE '+ @DauNhay +'NB%'+ @DauNhay +' THEN ISNULL(SUM(CAST(SoLuongThucChay AS BIGINT)),0) 
					ELSE 0
				END AS SoLuongThucChayThucThu,
				CASE WHEN UPPER(TenMaHopDong) LIKE '+ @DauNhay +'NB%'+ @DauNhay +' THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
					ELSE 0
				END AS ThanhTienThucChayNoiBo,
				ISNULL(SUM(ThanhTienKM),0) AS ThanhTienThucChayKhuyenMai,			
				ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) AS ThanhTienThucChaySauChietKhau,
				CASE WHEN UPPER(TenMaHopDong) NOT LIKE '+ @DauNhay +'NB%'+ @DauNhay +' THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
					ELSE 0
				END AS ThanhTienThucThu
			FROM ThucChayDaTinh 
			WHERE 1=1'
	SET @Sql += @FilterString
	SET @Sql += '
				AND TrangThaiHopDong <> 3
			GROUP BY DmSanPhamREF,TenSanPham,SoHopDong,HopDongChiTietREF,dbo.FormatDonViTinh(DonViTinh),TenMaHopDong,ThanhTienKM,
				isKhuyenMai,SoLuongDotChayHD,SoLuongDotChayBooking,TenWebsite,DmWebsiteREF,TenPhongBan,DmPhongBanREF,
				TenBoPhan, DmBoPhanREF, TenNhomLamViec, DmNhomLamViecREF, SysNhanVienREF, TenDangNhap,TenNhanVien,NgayThucHien
		)A
		WHERE  SoLuongThucChayNoiBo <> 0 OR SoLuongThucChayKhuyenMai <> 0 OR SoLuongThucChayThucThu <> 0 
						OR ThanhTienThucChayNoiBo <> 0 OR ThanhTienThucChayKhuyenMai <> 0 OR ThanhTienThucChaySauChietKhau <> 0 
	'

	-- Return the result of the function
	RETURN @Sql

END

```
