# Stored Procedure: `SYN_ThucChay_PerformanceBase_Current_ReAdd`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-04-16 14:35:54.203000
- **Ngày sửa cuối**: 2018-06-06 11:50:59.440000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql


CREATE PROCEDURE [dbo].[SYN_ThucChay_PerformanceBase_Current_ReAdd]
AS
BEGIN
	DECLARE   @NgayThucHien DATETIME 
	SET @NgayThucHien = CONVERT(DATE,DATEADD(DAY,-1,GETDATE()))
	EXEC [dbo].[SYN_ThucChay_PerformanceBase_CURRENTDAY] @NgayThucHien = @NgayThucHien 
	EXEC [dbo].[SYN_ThucChay_PerformanceBase_ReAddDAY]  @NgayThucHien = @NgayThucHien 
END



```
