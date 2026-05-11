# Stored Procedure: `ThucChay_UpdateLechTreoHaThucChayDaTinh_BySQLJobs`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-02 14:12:45.447000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.957000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_UpdateLechTreoHaThucChayDaTinh_BySQLJobs]
	-- Add the parameters for the stored procedure here

AS
BEGIN
	DECLARE @dtStart DATETIME, @dtEnd DATETIME
	
	SET @dtStart = (
					SELECT MAX(NgayThucHien) FROM dbo.ThucChayDaTinh
						WHERE DmSanPhamREF IN (231,238,339,342,337,240,370) 
					)
	
	SET @dtEnd = GETDATE()
	
	--Tinh LechTreoHaThucChayDaTinh - Thuc Chay CPM


	EXEC ThucChay_UpdateLechTreoHaThucChayDaTinh @dtStart,@dtEnd	

END

```
