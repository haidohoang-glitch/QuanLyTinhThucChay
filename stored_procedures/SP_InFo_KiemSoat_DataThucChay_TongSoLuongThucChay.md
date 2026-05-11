# Stored Procedure: `InFo_KiemSoat_DataThucChay_TongSoLuongThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-08-10 10:19:11.700000
- **Ngày sửa cuối**: 2018-08-10 10:19:41.850000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC dbo.InFo_KiemSoat_DataThucChay_TongSoLuongThucChay
*/
CREATE PROCEDURE dbo.InFo_KiemSoat_DataThucChay_TongSoLuongThucChay
	
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = CONVERT(DATE,DATEADD(DAY,-1,GETDATE()))

	SELECT tc.TenSanPham, tc.TypeProduct
	, tc.TongViewThucChay AS TongViewThucChay_thucchay
	, tct.TongViewThucChay AS TongViewThucChay
	, tc.TongClickThucChay AS TongClickThucChay_thucchay
	, tct.TongClickThucChay AS TongClickThucChay
	 FROM
	(
		SELECT TenSanPham, TypeProduct, SUM(CONVERT(BIGINT,ISNULL(TongViewThucChay,0)))TongViewThucChay
		,  SUM(CONVERT(BIGINT,ISNULL(TongClickThucChay,0)))TongClickThucChay
		 FROM dbo.DataThucChay
		WHERE NgayThucHien = @NgayThucHien
		AND TypeProduct > 0
		AND SoHopDong <> N'TONGSANPHAM'
		GROUP BY TenSanPham, TypeProduct
	)tc
	INNER JOIN
	(
		SELECT TenSanPham, TypeProduct,  SUM(CONVERT(BIGINT,ISNULL(TongViewThucChay,0)))TongViewThucChay
		,  SUM(CONVERT(BIGINT,ISNULL(TongClickThucChay,0)))TongClickThucChay
		 FROM dbo.DataThucChay
		WHERE NgayThucHien = @NgayThucHien
		AND TypeProduct > 0
		AND SoHopDong = N'TONGSANPHAM'
		GROUP BY TenSanPham, TypeProduct
	)tct ON tc.TypeProduct = tct.TypeProduct
	WHERE abs(tc.TongViewThucChay - tct.TongViewThucChay) <2
	AND ABS(tc.TongClickThucChay - tct.TongClickThucChay)<2
END


```
