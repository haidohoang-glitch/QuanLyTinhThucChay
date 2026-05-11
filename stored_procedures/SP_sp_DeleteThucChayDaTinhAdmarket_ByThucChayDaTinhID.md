# Stored Procedure: `sp_DeleteThucChayDaTinhAdmarket_ByThucChayDaTinhID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-03-16 17:12:57.393000
- **Ngày sửa cuối**: 2021-03-16 17:21:20.093000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayDaTinhID` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_DeleteThucChayDaTinhAdmarket_ByThucChayDaTinhID]
	-- Add the parameters for the stored procedure here
	@ThucChayDaTinhID nvarchar(50),
	@NgayThucHien datetime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	Delete from ThucChayDaTinhAdmarket 
	where ThucChayDaTinhID = @ThucChayDaTinhID and NgayThucHien = @NgayThucHien
	and year(NgayThucHien) = year(getdate())
	and DATEPART (HOUR, createdat) >='14'
	and HopDongID = 0
END

```
