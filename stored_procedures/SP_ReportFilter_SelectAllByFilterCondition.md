# Stored Procedure: `ReportFilter_SelectAllByFilterCondition`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-30 09:36:58.033000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.970000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FilterCondition` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<SonVM>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ReportFilter_SelectAllByFilterCondition]
	@FilterCondition NVARCHAR(4000)
AS
BEGIN
	DECLARE @SQLCommand nvarchar(4000)
	
	SET @SQLCommand = 'SELECT TenTruong, MoTa, KieuDuLieu, IsDefault, MaChucNang FROM ReportFilter WHERE 1=1 '		
	SET @SQLCommand = @SQLCommand + @FilterCondition	
	SET @SQLCommand = @SQLCommand + ' ORDER BY DoUuTien ASC'

	PRINT @SQLCommand
	EXEC(@SQLCommand)
END

```
