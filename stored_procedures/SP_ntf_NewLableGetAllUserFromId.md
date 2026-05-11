# Stored Procedure: `ntf_NewLableGetAllUserFromId`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-03-11 14:02:00.183000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.453000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ntf_NewLableGetAllUserFromId]
(
	@DmNhanHangID INT
)
AS
BEGIN
	DECLARE @ThisDate DATETIME
	SET @ThisDate = DATEADD(DAY, -2, CONVERT(date, GETDATE()))
	
	SELECT DISTINCT       
	       [CreatedBy]	      
	FROM   [DmNhanHang]
	WHERE  ([RecordStatus] IS NOT NULL AND [RecordStatus] = 0) AND ([CreatedAt] > @ThisDate)
	       AND ([DmNhanHangID] > @DmNhanHangID) AND FromSystem = 'Booking'
	       
	SELECT MAX([DmNhanHangID]) AS MAXID FROM [ABM_Data].[dbo].[DmNhanHang]
	WHERE  ([RecordStatus] IS NOT NULL AND [RecordStatus] = 0) AND ([CreatedAt] > @ThisDate)
	       AND ([DmNhanHangID] > @DmNhanHangID) AND FromSystem = 'Booking'
END

```
