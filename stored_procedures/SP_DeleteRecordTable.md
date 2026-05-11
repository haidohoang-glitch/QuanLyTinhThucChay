# Stored Procedure: `DeleteRecordTable`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-23 08:49:43.557000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.987000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TableName` | `nvarchar(100)` | No |
| `@IDValue` | `nvarchar(100)` | No |
| `@DeletedValue` | `nvarchar(100)` | No |
| `@LastModifiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[DeleteRecordTable]
	-- Add the parameters for the stored procedure here
	@TableName nvarchar(50),
	@IDValue nvarchar(50),
	@DeletedValue nvarchar(50),
	@LastModifiedBy nvarchar(50),
	@LastModifiedAt nvarchar(50)
AS
BEGIN
	Declare @SQLCommand nvarchar(4000)
	Declare @DauNhay nvarchar(50)
	set @DauNhay = ''''
	set @SQLCommand = 'Update ' + @TableName + ' Set LastModifiedAt = '+@DauNhay+@LastModifiedAt+@DauNhay+',LastModifiedBy = '+@DauNhay+@LastModifiedBy+@DauNhay+',DeletedStatus = '+@DeletedValue+' Where '+ @TableName + 'ID ='
	set @SQLCommand = @SQLCommand + @DauNhay + @IDValue + @DauNhay
	exec(@SQLCommand)

	select '0'
END

--exec [DeleteRecordTable] 'DmNgonNgu','e1c37f44-c5e8-4ae3-bb67-d65fb52b04c9','1','phuongld','2010-11-22 14:04:37.800'

```
