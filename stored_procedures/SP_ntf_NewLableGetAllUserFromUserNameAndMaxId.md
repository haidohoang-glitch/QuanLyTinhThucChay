# Stored Procedure: `ntf_NewLableGetAllUserFromUserNameAndMaxId`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-03-12 15:04:46.803000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.450000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ntf_NewLableGetAllUserFromUserNameAndMaxId]
(
	@DmNhanHangID INT,
	@CreatedBy NVARCHAR(50)
)
AS
BEGIN
	DECLARE @ThisDate DATETIME
	SET @ThisDate = DATEADD(DAY, -2, CONVERT(date, GETDATE()))
	
	SELECT TOP(30) [DmNhanHangID],
	       [TenNhanHang],
	       [Ghichu],
	       [CreatedBy],
	       [CreatedAt],
	       [FromSystem]	      
	FROM   [DmNhanHang]
	WHERE  ([RecordStatus] IS NOT NULL AND [RecordStatus] = 0) AND ([CreatedAt] > @ThisDate)
	       AND ([DmNhanHangID] > @DmNhanHangID) AND FromSystem = 'Booking' AND [CreatedBy] = @CreatedBy
	       
	SELECT COUNT(*) AS Total FROM [ABM_Data].[dbo].[DmNhanHang]
	WHERE  ([RecordStatus] IS NOT NULL AND [RecordStatus] = 0)
	       AND ([DmNhanHangID] > @DmNhanHangID) AND FromSystem = 'Booking'
END

```
