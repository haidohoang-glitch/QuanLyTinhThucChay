# Stored Procedure: `ntf_NewLable`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-03-10 16:28:29.487000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.007000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ntf_NewLable]
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
	FROM   [ABM_Data].[dbo].[DmNhanHang]
	WHERE  ([RecordStatus] IS NOT NULL AND [RecordStatus] = 0)
	       AND ([CreatedAt] > @ThisDate)
	ORDER BY
	       [CreatedAt] DESC
END

```
