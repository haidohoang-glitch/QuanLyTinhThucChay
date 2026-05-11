# Stored Procedure: `Rpt_ViewNhanHangThongTinChung`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:34.207000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.497000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmNhanHangREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- Rpt_ViewNhanHangThongTinChung '2013-01-01', '2013-12-31', 2516
CREATE  PROCEDURE [dbo].[Rpt_ViewNhanHangThongTinChung]
	@StartDate DATETIME,
	@EndDate DATETIME,
	@DmNhanHangREF INT
AS
BEGIN
	DECLARE @ViTriNhanInNganh NVARCHAR(500), @DmNganhHangREF NVARCHAR(100), @ViTriTrongAdmicro NVARCHAR(200)
	DECLARE @TongSoLuongHD INT, @TongSoLuongHDHT INT , @TongSoLuongHDKT INT, @TinhTrangNhanHang NVARCHAR(100), @TongThongTinChiTiet NVARCHAR(100)
	DECLARE @TongDoanhSoThucChayNhanHang BIGINT	
	
	SET @ViTriNhanInNganh =''
	SET @ViTriTrongAdmicro = ''
	SET @TongDoanhSoThucChayNhanHang = 0
	SET @DmNganhHangREF =
	(
		SELECT distinct dnh.DmNghanhHangREF FROM DmNhanHang dnh
		WHERE dnh.DmNhanHangID = @DmNhanHangREF
	)
	
	--1. tinh trang nhan
	SET @TinhTrangNhanHang = [dbo].[Rpt_GetTinhTrangNhanHang](@DmNhanHangREF,@StartDate,@EndDate) 
	--2. vi tri nhan trong nganh
	SET @ViTriNhanInNganh = dbo.[Rpt_ViTriNhanTrongNganhHang](@DmNhanHangREF, @StartDate, @EndDate, @DmNganhHangREF)
	--3. vi tri nhan trong all
	SET @ViTriTrongAdmicro = dbo.[Rpt_ViTriNhanTrongNganhHang](@DmNhanHangREF, @StartDate, @EndDate, '0')
	--4. lon hon bao nhieu phan tram so voi trung binh nganh
	SET @TongSoLuongHD = 
	(
		SELECT COUNT(DISTINCT rnhttct.SoHopDong) FROM RptNhanHangThongTinChiTiet rnhttct
		WHERE rnhttct.DmNhanHangREF = @DmNhanHangREF
		AND CONVERT(date,rnhttct.NgayThucHien) BETWEEN @StartDate AND @EndDate
	)
	SET @TongSoLuongHDHT =
	(
		SELECT COUNT(DISTINCT rnhttct.SoHopDong) FROM RptNhanHangThongTinChiTiet rnhttct
		WHERE rnhttct.DmNhanHangREF = @DmNhanHangREF
		AND CONVERT(date,rnhttct.NgayThucHien) BETWEEN @StartDate AND @EndDate
		AND rnhttct.SoHopDong LIKE '%HT%'
	)
	PRINT @TongSoLuongHD
	SET @TongSoLuongHDKT = ISNULL(@TongSoLuongHD,0) - ISNULL(@TongSoLuongHDHT,0)
	----5. soluong hop dong, so luong hop dong hop tac, so luong hop dong kinh te
		
	----6. Tong Doanh so thuc chay
	SET @TongDoanhSoThucChayNhanHang =	[dbo].[Rpt_GetDoanhSoThucChayByNhan](@DmNhanHangREF,@StartDate ,@EndDate)
	PRINT 'tong doanh so thuc chay'
	SELECT rnhttc.DmNhanHangREF, rnhttc.TenNhanHang, @TinhTrangNhanHang TinhTrangNhanHang
	, max(isnull(rnhttc.KhachHangSoHuuREF,0)) KhachHangSoHuuREF, max(isnull(rnhttc.TenKhachHangSoHuu,'')) TenKhachHangSoHuu, max(isnull(rnhttc.MaSoThue,'')) MaSoThue, max(isnull(rnhttc.DiaChi,''))DiaChi
	, max(isnull(rnhttc.SoDienThoai,''))SoDienThoai, dbo.FormatNumber(SUM(rnhttc.TongDoanhSoKyHaiDau)) TongDoanhSoKyHaiDau,
	@ViTriNhanInNganh vitrinhantrongnganh, @ViTriTrongAdmicro vitrinhantrongall, '' doanhsotbnganh,
	@TongSoLuongHD soluonghopdong, @TongSoLuongHDHT slhopdonghoptac, @TongSoLuongHDKT slhopdongkinhte
	, 
	(
	CASE WHEN SUM(rnhttc.TongDoanhSoKyHaiDau) = 0 THEN 0
		WHEN ROUND((CONVERT(FLOAT,@TongDoanhSoThucChayNhanHang) / convert(float,SUM(rnhttc.TongDoanhSoKyHaiDau))) * 100,2,2) >100 THEN 100
		ELSE ROUND((CONVERT(FLOAT,@TongDoanhSoThucChayNhanHang) / convert(float,SUM(rnhttc.TongDoanhSoKyHaiDau))) * 100,2,2)
	--@TongDoanhSoThucChayNhanHang/SUM(rnhttc.TongDoanhSoKyHaiDau) *100
	END 
	) tiledoanhsothucchay_ky
	  FROM RptNhanHangThongTinChung rnhttc
	WHERE rnhttc.DmNhanHangREF = @DmNhanHangREF
	AND convert(date,rnhttc.NgayThucHien) BETWEEN @StartDate AND @EndDate
	GROUP BY rnhttc.DmNhanHangREF, rnhttc.TenNhanHang
END

--EXEC Rpt_ViewNhanHangThongTinChung '2013-01-01', '2014-01-16', 1772

```
