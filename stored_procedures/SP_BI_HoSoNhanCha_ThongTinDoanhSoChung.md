# Stored Procedure: `BI_HoSoNhanCha_ThongTinDoanhSoChung`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-25 16:17:14.823000
- **Ngày sửa cuối**: 2015-06-25 16:17:14.823000

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

--EXEC [dbo].[BI_HoSoNhanCha_ThongTinDoanhSoChung] 2905,'2014-01-01','2014-12-31'

CREATE  PROCEDURE [dbo].[BI_HoSoNhanCha_ThongTinDoanhSoChung] 
( 
	@DmNhanHangChaID INT,
	@FromDate DATETIME,
	@ToDate DATETIME
)
AS
BEGIN
	SELECT  SUM(d.DoanhSoHaiDau) DoanhSoKyHaiDau, SUM(d.ThucChay) ThucChay
	, (CASE WHEN SUM(d.DoanhSoHaiDau) = 0 THEN 0
		ELSE (CONVERT(FLOAT,SUM(d.ThucChay))/Convert(float,SUM(d.DoanhSoHaiDau)))*100
		END 
	)TiLeDSThucChay_HaiDau
	,SUM(CASE WHEN d.HopDongREF <> 0 THEN 1
		ELSE 0
		END
	) SoLuongHD
	,SUM(CASE WHEN d.SoHopDong LIKE 'HT%' THEN 1
		ELSE 0
		END
	) SoLuongHDHopTac
	, '' ViTriNhanTrongNganh
	, '' TenNganhHang
	, '' VitriNhanTrongAdmirco
	
	FROM (
		SELECT SUM(hsn.DoanhSoHaiDau)DoanhSoHaiDau
		, SUM(hsn.ThucChay)ThucChay
		, hsn.SoHopDong
		, hsn.HopDongREF 
		, hsn.NhanHangGocID
		FROM	dbo.HoSoNhan_DoanhSoChiTiet hsn
		GROUP BY hsn.SoHopDong
		, hsn.HopDongREF
		, hsn.NhanHangGocID
	) d
	WHERE d.NhanHangGocID = @DmNhanHangChaID
END

--EXEC [dbo].[BI_HoSoNhanCha_ThongTinDoanhSoChung] 4152,'2015-01-01','2014-01-01'

```
