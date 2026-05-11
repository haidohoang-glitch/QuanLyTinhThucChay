# Stored Procedure: `GetAllBoPhanNghiepVuByDmPhongBanFK`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-07 09:31:57.090000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.280000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmPhongBanFK` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[GetAllBoPhanNghiepVuByDmPhongBanFK]
	-- Add the parameters for the stored procedure here
	@DmPhongBanFK int
AS
BEGIN
	select * from dbo.DmBoPhanNghiepVu where DmPhongBanFK= @DmPhongBanFK and DeletedStatus <> 1
END


--exec [GetAllTableForComboBox] 'DmNgonNgu','','TenNgonNgu'

```
