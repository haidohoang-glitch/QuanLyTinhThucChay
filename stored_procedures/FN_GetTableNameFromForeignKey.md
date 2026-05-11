# Function: `GetTableNameFromForeignKey`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-05-23 08:52:30.833000
- **Ngày sửa cuối**: 2014-10-14 10:39:35.523000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(100)` | Yes |
| `@FieldName` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetTableNameFromForeignKey] 
(
	@FieldName nvarchar(50)
)
RETURNS nvarchar(50)
AS
BEGIN
	
Declare @Index int,@TableName nvarchar(50)



set @Index = Charindex('REF',@FieldName)
if(@Index>0)
	set @TableName = Substring(@FieldName,1,@Index-1)

set @Index = Charindex('FK',@FieldName)
if(@Index>0)
	set @TableName = Substring(@FieldName,1,@Index-1)

set @Index = Charindex('ID',@FieldName)
if(@Index>0)
	set @TableName = Substring(@FieldName,1,@Index-1)

return @TableName

END

```
