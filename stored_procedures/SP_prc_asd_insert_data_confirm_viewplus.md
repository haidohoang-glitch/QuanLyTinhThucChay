# Stored Procedure: `prc_asd_insert_data_confirm_viewplus`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-11 15:02:51.337000
- **Ngày sửa cuối**: 2017-09-11 15:02:51.373000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ngaythuchien` | `datetime(8)` | No |
| `@sohopdong` | `nvarchar(100)` | No |
| `@sanpham` | `int(4)` | No |
| `@sotien` | `money(8)` | No |
| `@sohopdong_change` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--exec [dbo].[prc_asd_insert_data_confirm]  
CREATE PROCEDURE [dbo].[prc_asd_insert_data_confirm_viewplus] 
	-- Add the parameters for the stored procedure here
	@ngaythuchien DATETIME,
	@sohopdong NVARCHAR(50),
	@sanpham INT,
	@sotien MONEY,
	@sohopdong_change NVARCHAR(50) = ''
	--@vitri INT = 0
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	

    -- Insert statements for procedure here
	UPDATE [dbo].[ThucChayAdmarket_ViewPlus_HopDong_online]
	SET confirm_money = @sotien,
	confirm_status = 1,
	@sohopdong_change = @sohopdong_change,
	data_type= CASE WHEN @sohopdong_change = '' THEN data_type ELSE 4 END
    WHERE contract_number = @sohopdong
	AND NgayThucHien = @ngaythuchien
	AND DmSanPhamREF = @sanpham

END


```
