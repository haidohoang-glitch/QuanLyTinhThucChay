# Stored Procedure: `ThucChayDaTinhOther_GetByID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-16 13:39:42.970000
- **Ngày sửa cuối**: 2014-12-16 13:39:42.970000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@id` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-12-13
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinhOther_GetByID]
	-- Add the parameters for the stored procedure here
	@id		NVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    SELECT *
    FROM ThucChayDaTinhOther A
    WHERE A.ThucChayDaTinhOtherID = @id;
END

```
