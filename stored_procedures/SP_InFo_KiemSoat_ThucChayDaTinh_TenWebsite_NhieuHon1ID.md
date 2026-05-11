# Stored Procedure: `InFo_KiemSoat_ThucChayDaTinh_TenWebsite_NhieuHon1ID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-07-24 10:21:31.563000
- **Ngày sửa cuối**: 2021-06-02 16:02:11.273000

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
EXEC dbo.InFo_KiemSoat_ThucChayDaTinh_TenWebsite_NhieuHon1ID 
 
*/
CREATE PROCEDURE [dbo].[InFo_KiemSoat_ThucChayDaTinh_TenWebsite_NhieuHon1ID] 
AS
BEGIN
	DECLARE @NgayKiemSoat DATETIME
	SET @NgayKiemSoat =  CONVERT(DATE,GETDATE())

	SELECT TenWebsite, SoLuongSiteLech, TienSiteLech, FromDate, ToDate, createdAt 
	FROM dbo.KiemSoat_ThucChayDaTinh_Website
	WHERE CONVERT(DATE,createdAt) = @NgayKiemSoat
	and not (rtrim(TenWebsite) ='tinmoi.vn' and SoLuongSiteLech = 2)

END

--SELECT * FROM dbo.KiemSoat_ThucChayDaTinh_Website

```
