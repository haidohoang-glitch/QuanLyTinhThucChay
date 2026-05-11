# Stored Procedure: `InFo_KiemSoat_DataThucChay_ThayDoi_KhiTinhThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-07-24 13:53:53.317000
- **Ngày sửa cuối**: 2018-07-24 13:53:57.737000

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
EXEC dbo.[InFo_KiemSoat_DataThucChay_ThayDoi_KhiTinhThucChay]  @TypeProduct = 10
 
*/
CREATE PROCEDURE [dbo].[InFo_KiemSoat_DataThucChay_ThayDoi_KhiTinhThucChay]
	@TypeProduct INT
AS
BEGIN
	DECLARE @NgayKiemSoat DATETIME
	SET @NgayKiemSoat =  CONVERT(DATE,DATEADD(DAY,-1,GETDATE()))

	SELECT SoHopDong_TC
	, SoHopDong_TCKS
	, TypeProduct, TenSanPham
	, TongViewThucChay_Lech
	, TongClickThucChay_Lech 
	, NgayThucHien FROM dbo.KiemSoat_DataThucChay_ThayDoi
	WHERE CONVERT(DATE,NgayThucHien) = @NgayKiemSoat
	
END


```
