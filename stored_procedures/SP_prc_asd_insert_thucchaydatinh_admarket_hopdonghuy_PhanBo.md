# Stored Procedure: `prc_asd_insert_thucchaydatinh_admarket_hopdonghuy_PhanBo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-02-06 11:01:20.827000
- **Ngày sửa cuối**: 2024-02-28 11:34:37.183000

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
CREATE PROCEDURE [dbo].[prc_asd_insert_thucchaydatinh_admarket_hopdonghuy_PhanBo]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	declare @HopDongID int, @GhiChu NVARCHAR(1000) = N'HopDongHuy'

	DECLARE db_cursor_huy CURSOR FOR  
	select  HopDongID from hopdong where trangthaihopdong = 3 and convert(date,NgayHuyHopDong) = convert(date,@NgayThucHien)

	OPEN db_cursor_huy   
	FETCH NEXT FROM db_cursor_huy INTO @HopDongID   

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
		   exec [dbo].[prc_asd_insert_thucchaydatinh_admarket_hopdonghuy_chitiet_PhanBo] @HopDongID,@NgayThucHien, @GhiChu

		   FETCH NEXT FROM db_cursor_huy INTO @HopDongID   
	END   

	CLOSE db_cursor_huy   
	DEALLOCATE db_cursor_huy

	
	
END


```
