# Stored Procedure: `ThucChayCPM_Insert_Manual`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-10-19 11:29:17.230000
- **Ngày sửa cuối**: 2016-11-15 17:40:59.677000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayCPM_Insert_Manual]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	DELETE FROM dbo.ThucChayCPM
	WHERE 
	NgayThucHien <=@NgayThucHien

	DECLARE @SQLCommand NVARCHAR(4000)
	
	SET @SQLCommand = '
	INSERT INTO dbo.ThucChayCPM
	SELECT [F1]
		  ,[F2]
		  ,[F3]
		  ,[F4]
		  ,[F5]
		  ,[F6]
		  ,[F7]
		  ,[F8]
		  ,0
		  ,[F10]
		  ,[F11]
		  ,[F12]
		  ,[F13]
		  ,[F14]
	FROM ThucChayCPM.dbo.' + '['+ '''' + CONVERT(NVARCHAR(50),@NgayThucHien,112) + '$'''+ ']'
	PRINT @SQLCommand
	EXEC(@SQLCommand)
END

```
