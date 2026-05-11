# Stored Procedure: `prc_admarket_xuly`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-12-15 11:49:05.687000
- **Ngày sửa cuối**: 2017-12-15 14:04:51.370000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [prc_admarket_xuly]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	declare @ngaythuchien datetime = getdate()
	-- các hợp đ có thực chạy năm 2017 table name : Admarket_XuLy_HopDong_2017
	exec [dbo].[prc_admarket_xuly_insert_hopdong]
	-- các hợp đồng đã chốt table: Admarket_XuLy_HopDong_DaThanhLy
	exec [dbo].[prc_admarket_xuly_insert_hopdong_dathanhly] 
	-- các hợp đồng thanh lý table name : Admarket_XuLy_HopDong_ThanhLy (giatrithuchay)
	exec [dbo].[prc_admarket_xuly_insert_hopdong_thanhly] @ngaythuchien
	-- các hợp đòng bị ảnh hưởng vì thanh lý table: Admarket_xuly_hopdong_lienquan_thanhly
	exec [dbo].[prc_admarket_xuly_tinh_hopdong_thanhly] @ngaythuchien

END

```
