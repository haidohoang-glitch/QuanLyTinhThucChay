# Stored Procedure: `DmBoPhanNghiepVuGetListByPhongBan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-07 17:32:08.640000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.260000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PhongBanID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[DmBoPhanNghiepVuGetListByPhongBan]
	@PhongBanID int
AS
BEGIN
	DECLARE @SQLCommand nvarchar(4000)
	DECLARE @Fillter nvarchar(2000)	
	SET @Fillter = ''	
	
	SET @SQLCommand = '
	SELECT
		A.[DmBoPhanNghiepVuID],
		A.[DmPhongBanFK],
		B.[TenPhongBan],
		A.[TenBoPhanNghiepVu],
		A.[DmNgonNguREF],
		A.[GhiChu],
		A.[CreatedBy],
		A.[CreatedAt],
		A.[LastModifiedBy],
		A.[LastModifiedAt],
		A.[DeletedStatus],
		A.[PrintStatus],
		A.[RecordStatus]
	FROM
		[dbo].[DmBoPhanNghiepVu] A,
		[dbo].[DmPhongBan] B
	Where
		B.[DmPhongBanID] = A.[DmPhongBanFK] 
		AND A.DeletedStatus <> 1
	'
	IF @PhongBanID > 0
		SET @Fillter = ' AND [DmPhongBanFK] = ' + Convert(nvarchar(50),@PhongBanID)
	
	SET @SQLCommand = @SQLCommand + @Fillter
	
	SET @SQLCommand = @SQLCommand + '
	ORDER BY [TenBoPhanNghiepVu]
	'
	
	print @SQLCommand
	EXEC(@SQLCommand)
	
END

```
