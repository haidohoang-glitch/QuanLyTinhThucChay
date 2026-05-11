# Stored Procedure: `prc_admarket_xuly_insert_hopdong_dathanhly`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-12-15 10:09:36.330000
- **Ngày sửa cuối**: 2017-12-15 15:05:12.190000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@hopdong_id` | `int(4)` | No |
| `@phanboid` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_admarket_xuly_insert_hopdong_dathanhly] 
	-- Add the parameters for the stored procedure here
	@hopdong_id int = null,
	@phanboid int = null
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
    -- Insert statements for procedure here
	if @hopdong_id is not null and @phanboid is not null
	insert into Admarket_XuLy_HopDong_DaThanhLy (hopdongid,phanboid)
	select @hopdong_id,@phanboid
	else
	begin
	truncate table Admarket_XuLy_HopDong_DaThanhLy
	insert into Admarket_XuLy_HopDong_DaThanhLy (hopdongid,phanboid)
	select distinct HopDongID,HopDongChiTietREF from thucchaydatinhadmarket where Giatrithaydoi <> 0 and Ghichu like N'%mail%' and NgayThuchien >='2017-09-11'
	end

END

```
