# Stored Procedure: `DmNhomGetListByBoPhanNghiepVu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-07 17:44:11.550000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.730000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@BoPhanNghiepVuID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[DmNhomGetListByBoPhanNghiepVu]
	@BoPhanNghiepVuID int
AS
BEGIN
	DECLARE @SQLCommand nvarchar(4000)
	DECLARE @Fillter nvarchar(2000)	
	SET @Fillter = ''	
	
	SET @SQLCommand = '
	SELECT
		A.[DmNhomID],
		A.TenNhom,
		A.[GhiChu],
		A.[DmBoPhanREF],
		B.[TenBoPhanNghiepVu],
		A.[CreatedBy],
		A.[CreatedAt],
		A.[LastModifiedBy],
		A.[LastModifiedAt],
		A.[DeletedStatus],
		A.[PrintStatus],
		A.[RecordStatus]
	FROM
		[dbo].[DmNhom] A
		LEFT JOIN [dbo].[DmBoPhanNghiepVu] B ON B.[DmBoPhanNghiepVuID] = A.[DmBoPhanREF]
	Where
		A.DeletedStatus <> 1
	'
	IF @BoPhanNghiepVuID > 0
		SET @Fillter = ' AND [DmBoPhanREF] = ' + Convert(nvarchar(50),@BoPhanNghiepVuID)
	
	SET @SQLCommand = @SQLCommand + @Fillter
	
	SET @SQLCommand = @SQLCommand + '
	ORDER BY A.[TenNhom]
	'
	
	print @SQLCommand
	EXEC(@SQLCommand)
	
END

```
