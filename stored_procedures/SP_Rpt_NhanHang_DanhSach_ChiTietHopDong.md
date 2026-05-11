# Stored Procedure: `Rpt_NhanHang_DanhSach_ChiTietHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:33.540000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.790000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@LabelId` | `int(4)` | No |

## Definition (Source Code)

```sql
--[Rpt_NhanHang_DanhSach_ChiTietHopDong] '2013-01-01', '2013-12-31', 1654
--SELECT [dbo].[Rpt_GetDoanhSoThucChayByNhanAndHopDongSanPham](2161,1525,225,'2013-01-01', '2013-12-31')
CREATE  PROC [dbo].[Rpt_NhanHang_DanhSach_ChiTietHopDong]
(
	@StartDate	DATETIME,
	@EndDate	DATETIME,
	@LabelId	INT		
)
AS
BEGIN	
	DECLARE @Length INT
	SET @Length = 2
	
	DECLARE @TongDoanhSoThucChay BIGINT
	SET @TongDoanhSoThucChay = 0
	
	SELECT A.TenNhanSu,
		   A.SoHopDong,
		   A.TenKhachHang,
		   A.HinhThucKy,
		   A.HinhThucSanPham,
		   A.TenSanPham,
		   A.TenKenh,
		   A.DoanhSoKyHaiDau,
		   [dbo].[Rpt_GetDoanhSoThucChayByNhanAndHopDongSanPham_v1](A.DmNhanHangREF,A.HopDongREF,A.DmSanPhamREF,A.DmKenhREF,@StartDate, @EndDate) DoanhSoThucChay,
		   (
		   	CASE WHEN A.DoanhSoKy2Dau = 0 THEN 0
				WHEN  ROUND((CONVERT(FLOAT,[dbo].[Rpt_GetDoanhSoThucChayByNhanAndHopDongSanPham_v1](A.DmNhanHangREF,A.HopDongREF,A.DmSanPhamREF,A.DmKenhREF,@StartDate, @EndDate)) / CONVERT(FLOAT, A.DoanhSoKy2Dau) * 100), @Length) > 100 THEN 100
				ELSE  ROUND((CONVERT(FLOAT,[dbo].[Rpt_GetDoanhSoThucChayByNhanAndHopDongSanPham_v1](A.DmNhanHangREF,A.HopDongREF,A.DmSanPhamREF,A.DmKenhREF,@StartDate, @EndDate)) / CONVERT(FLOAT, A.DoanhSoKy2Dau) * 100), @Length)				
			END
		   ) AS TyLeDSThucChay_DSKy2Dau			   	 
	FROM 
	(
		SELECT x.TenNhanSu,
			   x.DmNhanHangREF,
			   x.SoHopDong,
			   x.HopDongREF,
			   x.TenKhachHang,
			   x.HinhThucKy,
			   x.HinhThucSanPham,
			   x.TenSanPham,
			   x.DmSanPhamREF,
			   x.DmKenhREF,
			   x.TenKenh,
			   CONVERT(FLOAT, x.DoanhSoKyHaiDau) AS DoanhSoKyHaiDau,
			   SUM(CONVERT(BIGINT, DoanhSoKyHaiDau)) DoanhSoKy2Dau
		FROM   RptNhanHangThongTinChiTiet x
		WHERE  x.DmNhanHangREF = @LabelId AND CONVERT(DATE, x.NgayThucHien) BETWEEN @StartDate AND @EndDate
		GROUP BY
			   x.DmNhanHangREF,
			   x.TenNhanSu,
			   x.SoHopDong,
			   x.HopDongREF,
			   x.TenKhachHang,
			   x.HinhThucKy,
			   x.HinhThucSanPham,
			   x.TenSanPham,
			   x.DmSanPhamREF,
			   x.TenKenh,
			   x.DmKenhREF,
			   x.DoanhSoKyHaiDau
	) A	
END

```
