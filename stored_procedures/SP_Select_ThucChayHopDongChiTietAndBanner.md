# Stored Procedure: `Select_ThucChayHopDongChiTietAndBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-18 11:54:06.827000
- **Ngày sửa cuối**: 2015-08-26 10:48:53.090000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@pThucChayHopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [Select_ThongTinSuKienKhuyenMai]

CREATE PROCEDURE [dbo].[Select_ThucChayHopDongChiTietAndBanner]
	@pThucChayHopDongChiTietID INT 
AS
BEGIN
    SELECT * FROM ThucChayHopDongChiTietAndBanner tchdctab
    WHERE 
    1=1
    and tchdctab.DeletedStatus = 0
    AND tchdctab.DaThucHienUpdateTiLe = 1
    AND tchdctab.ThucChayHopDongChiTietID >= @pThucChayHopDongChiTietID

    
    ORDER BY tchdctab.ThucChayHopDongChiTietID
    
END

--EXEC [dbo].[Insert_ThongTinSuKienKhuyenMai] '2013-12-31'

```
