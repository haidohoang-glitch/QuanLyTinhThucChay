# Stored Procedure: `GetDistinctBookingIDFromThucChaySystem`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-25 17:01:10.620000
- **Ngày sửa cuối**: 2014-11-19 12:16:59.010000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@dtStart` | `datetime(8)` | No |
| `@dtEnd` | `datetime(8)` | No |
| `@SoHopDongList` | `nvarchar(8000)` | No |
| `@DmBookingREFList` | `nvarchar(8000)` | No |
| `@DmBannerREFList` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC GetDistinctBookingIDFromThucChaySystem '2013-09-01','2013-09-25','QC230913,QC230915'

CREATE PROCEDURE [dbo].[GetDistinctBookingIDFromThucChaySystem]
	-- Add the parameters for the stored procedure here
	@dtStart DATETIME,
	@dtEnd DATETIME,
	@SoHopDongList NVARCHAR(4000),
	@DmBookingREFList NVARCHAR(4000),
	@DmBannerREFList NVARCHAR(4000)
AS
BEGIN
	
DECLARE @ThucChay TABLE ([DmBookingREF] [varchar](4000), [ID] [varchar](4000))

Declare @DanhsachDmBookingREF NVARCHAR(4000)


DECLARE Record_Cursor CURSOR FOR 
	SELECT  DISTINCT DanhsachDmBookingREF 
	FROM [dbo].[GetThucChayByFullCondition](@dtStart,@dtEnd,@DmBookingREFList,@DmBannerREFList,@SoHopDongList)
	WHERE 
	DanhsachDmBookingREF IS NOT NULL 
	AND dbo.FormatString(DanhsachDmBookingREF) <> ''
	
OPEN Record_Cursor
-- Perform the first fetch.
FETCH NEXT FROM Record_Cursor into @DanhsachDmBookingREF
WHILE @@FETCH_STATUS = 0
BEGIN
	INSERT INTO @ThucChay
		SELECT item AS Name, item AS ID FROM dbo.ArrayToTable(dbo.Array(@DanhsachDmBookingREF ,','))
		WHERE item <> '' AND item IS NOT NULL	
		
	FETCH NEXT FROM Record_Cursor into @DanhsachDmBookingREF
END
	
CLOSE Record_Cursor
DEALLOCATE Record_Cursor

SELECT DISTINCT DmBookingREF AS [value], DmBookingREF AS [text] FROM @ThucChay

END

```
