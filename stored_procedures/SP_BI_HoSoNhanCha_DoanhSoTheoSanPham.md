# Stored Procedure: `BI_HoSoNhanCha_DoanhSoTheoSanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-25 16:17:13.730000
- **Ngày sửa cuối**: 2015-06-25 16:17:13.730000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangChaID` | `int(4)` | No |
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [dbo].[BI_HoSoNhanCha_DoanhSoTheoSanPham] 1523,'2014-01-01','2015-01-01'

CREATE  PROCEDURE [dbo].[BI_HoSoNhanCha_DoanhSoTheoSanPham] 
( 
	@DmNhanHangChaID INT,
	@FromDate DATETIME,
	@ToDate DATETIME
)
AS
BEGIN
	DECLARE @TongDoanhSoHaiDau BIGINT
	SET @TongDoanhSoHaiDau = 
	(
		SELECT SUM(nh.DoanhSoHaiDau) 
		FROM HoSoNhan_DoanhSoChiTiet nh 
		WHERE nh.NhanHangGocID = @DmNhanHangChaID
	)
	SET @TongDoanhSoHaiDau = ISNULL(@TongDoanhSoHaiDau,1)
	
	SELECT A.DmSanPhamREF, A.TenSanPham 
	, A.DoanhSoKyHaiDau
	, A.DoanhSoThucChay
	, round(CONVERT(FLOAT,A.DoanhSoKyHaiDau)/CONVERT(FLOAT,@TongDoanhSoHaiDau)*100,3,3) Tile_Ds2Dau_TongDs
	, (
		CASE WHEN A.DoanhSoKyHaiDau = 0 THEN 0
			ELSE ROUND(CONVERT(FLOAT,A.DoanhSoThucChay)/CONVERT(FLOAT,A.DoanhSoKyHaiDau)*100,3,3) 
		END
	) Tile_DsTc_Ds2Dau
	, 0 IsDeleted
	 FROM
	(
		SELECT * FROM 
		(
			SELECT rnhtcf.DmSanPhamREF, rnhtcf.TenSanPham
			, SUM(rnhtcf.DoanhSoHaiDau)DoanhSoKyHaiDau
			, SUM(rnhtcf.ThucChay)DoanhSoThucChay
			  FROM HoSoNhan_DoanhSoChiTiet rnhtcf
			WHERE rnhtcf.NhanHangGocID = @DmNhanHangChaID
			GROUP BY rnhtcf.TenSanPham, rnhtcf.DmSanPhamREF	
		)A
		WHERE (A.DoanhSoKyHaiDau <>0 OR A.DoanhSoThucChay <> 0)
	)A
	WHERE (A.DoanhSoKyHaiDau <>0 OR A.DoanhSoThucChay <> 0)
	ORDER BY A.DoanhSoKyHaiDau DESC
END

--EXEC [dbo].[BI_HoSoNhanCha_DoanhSoTheoSanPham] 4152,'2015-01-01','2014-01-01'

```
