# Stored Procedure: `prc_asd_insert_thucchaydatinh_admarket_hopdonghuy`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-11 15:02:51.837000
- **Ngày sửa cuối**: 2021-06-24 14:55:08.480000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		DOANNV
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_asd_insert_thucchaydatinh_admarket_hopdonghuy]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	declare @HopDongID int

	DECLARE db_cursor_huy CURSOR FOR  
	select  HopDongID from hopdong where trangthaihopdong = 3 and convert(date,NgayHuyHopDong) = convert(date,@NgayThucHien)

	OPEN db_cursor_huy   
	FETCH NEXT FROM db_cursor_huy INTO @HopDongID   

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
		   exec [dbo].[prc_asd_insert_thucchaydatinh_admarket_hopdonghuy_chitiet] @HopDongID,@NgayThucHien,N'HopDongHuy'

		   FETCH NEXT FROM db_cursor_huy INTO @HopDongID   
	END   

	CLOSE db_cursor_huy   
	DEALLOCATE db_cursor_huy

	
	
END


```
