# Stored Procedure: `prc_admarket_xuly_tinh_hopdong_thanhly`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-12-15 10:34:15.297000
- **Ngày sửa cuối**: 2017-12-19 11:38:10.860000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_admarket_xuly_tinh_hopdong_thanhly]
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	declare @hopdongid int, @phanboid int, @user_name nvarchar(50), @giatri money, @sohopdong nvarchar(50),@chenh money 

	DECLARE db_cursor CURSOR FOR  
	select distinct
	hopdongid,phanboid,[user_name],giatrithucchaymongmuon,sohopdong,giatrichenhlech
	from Admarket_XuLy_HopDong_ThanhLy where ngaythuchien = @NgayThucHien  and dmsanphamid in (628,585,144)

	OPEN db_cursor   
	FETCH NEXT FROM db_cursor INTO @hopdongid , @phanboid , @user_name , @giatri ,@sohopdong ,@chenh

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
		   --------------  ghi âm --------------------
		   --exec  [dbo].[prc_admarket_xuly_doitru_by_phanbo_id] @ngaythuchien, @phanboid,''
		   --------------  ghi dương -----------------
		   --exec [dbo].[prc_admarket_xuly_ThucChayDaTinhAdmarket_InsertByPhanBoID] @ngaythuchien,@sohopdong,@phanboid,@giatri,N'tang do thanh ly'
		   --------------  lưu thông tin đã xử lý ----
		   exec [dbo].[prc_admarket_xuly_insert_hopdong_dathanhly] @hopdongid,@phanboid
		   --------------  Xu ly hop dong lien qun bi giam
		   exec [dbo].[prc_admarket_xuly_insert_hopdong_lienquan_thanhly] @ngaythuchien,@hopdongid,@user_name,@chenh

		   FETCH NEXT FROM db_cursor INTO @hopdongid , @phanboid , @user_name , @giatri ,@sohopdong ,@chenh 
	END   

	CLOSE db_cursor   
	DEALLOCATE db_cursor
	
END

```
