# Function: `Fn_GetDSTenNhanHangByDsNhanREF`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-02-12 13:34:03.860000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.657000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(100)` | Yes |
| `@DsNhanRef` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[Fn_GetDSTenNhanHangByDsNhanREF]
(
	-- Add the parameters for the function here
	@DsNhanRef NVARCHAR(50)
)
RETURNS nvarchar(50)
AS
BEGIN
	DECLARE @result NVARCHAR(50)
	SET @result = ''
	--SET @DsNhanRef = ISNULL(@DsNhanRef,'')
	IF(@DsNhanRef <> '')
	BEGIN
		SET @result =
	    (
        SELECT STUFF(
                   (
                       SELECT isnull(U.TenNhanHang,'') + CAST('||' AS VARCHAR(MAX)) 
                       FROM   dmNhanHang U
                       WHERE  convert(nvarchar(50),U.DmNhanHangID) IN (@DsNhanRef)
                              AND U.RecordStatus = 1
                       ORDER BY
                              U.TenNhanHang
                              FOR XML PATH('')
                   ),
                   1,
                   0,
                   ''
               ) AS TenNhanHang
	    )
	END
	SET @result = ISNULL(@result,'')
	-- Return the result of the function
	RETURN @result

END

```
