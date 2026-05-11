# Stored Procedure: `ThucChay_DashboardPhongBan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-18 14:17:42.527000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.550000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |
| `@ListSanPhamID` | `nvarchar(4000)` | No |
| `@ListWebsiteID` | `nvarchar(4000)` | No |
| `@ListSoHopDong` | `nvarchar(4000)` | No |
| `@ListPhongID` | `nvarchar(4000)` | No |
| `@ListBoPhanID` | `nvarchar(4000)` | No |
| `@ListNhomID` | `nvarchar(4000)` | No |
| `@ListUserName` | `nvarchar(4000)` | No |
| `@DonViThoiGian` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_DashboardPhongBan]
	@FromDate datetime, 
	@ToDate datetime,
	@ListSanPhamID nvarchar(2000),
	@ListWebsiteID nvarchar(2000),
	@ListSoHopDong nvarchar(2000),
	@ListPhongID nvarchar(2000),
	@ListBoPhanID nvarchar(2000),
	@ListNhomID nvarchar(2000),
	@ListUserName nvarchar(2000),
	@DonViThoiGian int
AS
BEGIN
	DECLARE @sql nvarchar(4000);
	DECLARE @DauNhay nvarchar(50)
	DECLARE @GroupBy nvarchar(2000)
	DECLARE @OrderBy nvarchar(2000)
	SET @DauNhay = ''''
	
	SET @sql ='
	SELECT
		A.TenNhanVien,
		A.TenPhongBan,
		A.TenBoPhan,
		A.TenNhomLamViec,
		SUM(A.ThanhTienThucChayTruocTrietKhau) AS ThanhTienThucChayTruocTrietKhau,
		SUM(A.GiaTriTrietKhauThucChay) AS GiaTriTrietKhauThucChay,
		SUM(A.ThanhTienSauTrietKhauThucChay) AS ThanhTienSauTrietKhauThucChay,
		SUM(A.GiaTriHoaHongThucChay) AS GiaTriHoaHongThucChay,
		SUM(A.ThanhTienThucThu) AS ThanhTienThucThu
	'
	IF @DonViThoiGian >= 0
		Begin
			SET @sql = @sql + ', dbo.GetDonViThoiGian(NgayThucHien,' + CONVERT(nvarchar(50), @DonViThoiGian) + ') AS ThoiGian '
			-- Set GroupBy
			SET @GroupBy = ' A.TenNhanVien,A.TenPhongBan,A.TenBoPhan,A.TenNhomLamViec,dbo.GetDonViThoiGian(NgayThucHien,' + CONVERT(nvarchar(50), @DonViThoiGian) + ')'
			-- Set OrderBy
			SET @OrderBy = ' dbo.GetDonViThoiGian(NgayThucHien,' + CONVERT(nvarchar(50), @DonViThoiGian) + '), A.TenNhanVien,A.TenPhongBan,A.TenBoPhan,A.TenNhomLamViec'
		End
	ELSE IF @DonViThoiGian = -1
		Begin 
			-- Set GroupBy
			SET @GroupBy = ' A.TenNhanVien,A.TenPhongBan,A.TenBoPhan,A.TenNhomLamViec '
			-- Set OrderBy
			SET @OrderBy = ' A.TenNhanVien,A.TenPhongBan,A.TenBoPhan,A.TenNhomLamViec '
		End
		
	SET @sql = @sql + '
	FROM dbo.ThucChayDaTinh A
	WHERE UPPER(TenMaHopDong) <> '+ @DauNhay + 'NB'+ @DauNhay +' AND IsKhuyenMai <> 1
		AND dbo.ThucChay_CheckLechTreoHa(NgayThucHien, HopDongChiTietREF, TenSanPham) > 0
	'
	IF (@FromDate <> '')
		SET @sql = @sql + ' AND CONVERT(DATE,A.NgayThucHien) >= '+ @DauNhay + CONVERT(nvarchar(200), @FromDate)+ @DauNhay
		
	IF (@ToDate <> '')
		SET @sql = @sql + ' AND CONVERT(DATE,A.NgayThucHien) <= '+ @DauNhay + CONVERT(nvarchar(200), @ToDate)+ @DauNhay
		
	IF (@ListSanPhamID <> '0')
		SET @sql = @sql + ' AND A.DmSanPhamREF IN (' + CONVERT(nvarchar(2000), @ListSanPhamID) + ')'
		
	IF (@ListWebsiteID <> '0')
		SET @sql = @sql + ' AND A.DmWebsiteREF IN (' + CONVERT(nvarchar(2000), @ListWebsiteID) + ')'
	
	IF (@ListSoHopDong <> '0')
		SET @sql = @sql + ' AND A.SoHopDong IN ('+ CONVERT(nvarchar(2000), @ListSoHopDong)+ ')'
		
	IF (@ListPhongID <> '0')
		SET @sql = @sql + ' AND A.DmPhongBanREF IN (' + CONVERT(nvarchar(2000), @ListPhongID) + ')'
	
	IF (@ListBoPhanID <> '0')
		SET @sql = @sql + ' AND A.DmBoPhanREF IN (' + CONVERT(nvarchar(2000), @ListBoPhanID) + ')'
		
	IF (@ListNhomID <> '0')
		SET @sql = @sql + ' AND A.DmNhomLamViecREF IN (' + CONVERT(nvarchar(2000), @ListNhomID) + ')'
		
	IF (@ListUserName <> '0')
		SET @sql = @sql + ' AND A.TenNhanVien IN (N' + CONVERT(nvarchar(2000), @ListUserName) + ')'
		
	SET @sql = @sql + '
	GROUP BY ' +
		@GroupBy + '
	ORDER BY ' +
		@OrderBy
	
	PRINT @sql;
	EXEC (@sql);
END

```
