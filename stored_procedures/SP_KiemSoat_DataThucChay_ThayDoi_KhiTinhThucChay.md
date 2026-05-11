# Stored Procedure: `KiemSoat_DataThucChay_ThayDoi_KhiTinhThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-07-24 11:49:38.990000
- **Ngày sửa cuối**: 2018-07-24 14:13:02.363000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TypeProduct` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC [dbo].[KiemSoat_DataThucChay_ThayDoi_KhiTinhThucChay] 
	@TypeProduct = 10
 
*/
CREATE PROCEDURE [dbo].[KiemSoat_DataThucChay_ThayDoi_KhiTinhThucChay] 
	@TypeProduct INT
AS
BEGIN
	DECLARE @NgayThucHien DATETIME 
	SET @NgayThucHien = CONVERT(DATE,DATEADD(DAY,-1,GETDATE()))

	INSERT INTO dbo.KiemSoat_DataThucChay_ThayDoi

	SELECT ISNULL(tc.SoHopDong,'-') SoHopDong_TC
	, ISNULL(tcks.SoHopDong,'-') SoHopDong_TCKS
	, tc.TypeProduct, tc.TenSanPham
	, (ISNULL(tc.TongViewThucChay,0) - ISNULL(tcks.TongViewThucChay,0))TongViewThucChay_Lech
	, (ISNULL(tc.TongClickThucChay,0) - ISNULL(tcks.TongClickThucChay,0))TongClickThucChay_Lech 
	, tc.NgayThucHien

	FROM
	(
		SELECT SoHopDong,
			TypeProduct,
			TenSanPham,
			SUM(CONVERT(BIGINT,TongViewThucChay))TongViewThucChay,
			SUM(CONVERT(BIGINT,TongClickThucChay))TongClickThucChay,
			NgayThucHien  
		FROM dbo.DataThucChay_2
		WHERE NgayThucHien = @NgayThucHien
		AND TypeProduct = @TypeProduct
		GROUP BY SoHopDong, TypeProduct, TenSanPham, NgayThucHien
	)tcks
	FULL JOIN
	(
		SELECT SoHopDong,
			TypeProduct,
			TenSanPham,
			SUM(CONVERT(BIGINT,TongViewThucChay))TongViewThucChay,
			SUM(CONVERT(BIGINT,TongClickThucChay))TongClickThucChay,
			NgayThucHien  
		FROM dbo.DataThucChay
		WHERE NgayThucHien = @NgayThucHien
		AND TypeProduct = @TypeProduct
		GROUP BY SoHopDong, TypeProduct, TenSanPham, NgayThucHien
	)tc ON tc.SoHopDong = tcks.SoHopDong AND tc.TypeProduct = tcks.TypeProduct AND tc.NgayThucHien = tcks.NgayThucHien
	WHERE ((ISNULL(tc.TongViewThucChay,0) - ISNULL(tcks.TongViewThucChay,0)) <> 0 OR (ISNULL(tc.TongClickThucChay,0) - ISNULL(tcks.TongClickThucChay,0)) <> 0)
END

--SELECT * FROM dbo.KiemSoat_ThucChayDaTinh_Website

```
