# Stored Procedure: `prc_admarket_xuly_insert_hopdong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-12-15 10:03:40.960000
- **Ngày sửa cuối**: 2017-12-15 13:17:42.647000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_admarket_xuly_insert_hopdong]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	truncate table Admarket_XuLy_HopDong_2017
	insert into Admarket_XuLy_HopDong_2017
	select distinct
	hopdongid,
	sohopdong,
	HopDongChiTietREF
	from 
	(
	select
	distinct
	hopdongid,
	sohopdong,
	HopDongChiTietREF
	from thucchaydatinhadmarket t
	where 1=1
	AND DmSanPhamREF in (585,628,144)
	AND year(NgayThucHien) >= 2017
	AND hopdongid <> 0
	AND  isnull(
	(select sum(giatrithaydoi+ThanhTienSauTrietKhauThucChay) 
	from ThucChayDaTinhAdmarket tc where  tc.DmSanPhamREF in (585,628,144)
	AND year(tc.NgayThucHien) >= 2017 and tc.HopDongChiTietREF = t.HopDongChiTietREF),0) > 10
	) A
END



```
