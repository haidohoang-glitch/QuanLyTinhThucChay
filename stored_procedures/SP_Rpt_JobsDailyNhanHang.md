# Stored Procedure: `Rpt_JobsDailyNhanHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:36.287000
- **Ngày sửa cuối**: 2014-11-19 12:16:59.533000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE  PROCEDURE [dbo].[Rpt_JobsDailyNhanHang]
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = convert(date,DATEADD(DAY,-1,GETDATE()))
	
	EXEC [dbo].[Rpt_UpdateNhanHangDaily] @NgayThucHien
END

```
