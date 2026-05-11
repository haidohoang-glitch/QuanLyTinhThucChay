# Stored Procedure: `DotChayHopDongChiTietThayDoi_GetMaxID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-10-08 11:50:07.027000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.510000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[DotChayHopDongChiTietThayDoi_GetMaxID] 
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	DECLARE @MaxID INT
	
	SET @MaxID = (
				SELECT MAX(DotChayHopDongChiTietThayDoiID) FROM dbo.DotChayHopDongChiTietThayDoi
				)
	IF(@MaxID IS NULL) SET @MaxID = 0
	
	SELECT @MaxID
	

END

```
