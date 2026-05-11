# Stored Procedure: `HopDongChiTiet_SelectTaiKhoanAdmarket`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-29 11:10:25.863000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.757000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[HopDongChiTiet_SelectTaiKhoanAdmarket]
	-- Add the parameters for the stored procedure here
	@HopDongChiTietID int
AS
BEGIN

select 

c.HopDongChiTietID as ID
,rtrim(ltrim(c.TK_AdMarket)) as TK_AdMarket
,getdate() as LasModifiedAt
from Data20140830.dbo.HopDongChiTiet  c 
where
1=1
and c.DmSanPhamREF = 420
and rtrim(ltrim(c.TK_AdMarket)) <> ''
and c.TK_AdMarket is not null

order by 
c.HopDongChiTietID 



 
END

```
