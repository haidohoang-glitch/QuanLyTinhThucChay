# Stored Procedure: `prc_admarket_xuly_insert_hopdong_lienquan_thanhly`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-12-15 11:44:34.733000
- **Ngày sửa cuối**: 2017-12-15 15:07:29.607000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ngaythuchien` | `datetime(8)` | No |
| `@hopdongid` | `int(4)` | No |
| `@user_name` | `nvarchar(100)` | No |
| `@chenhlech` | `money(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_admarket_xuly_insert_hopdong_lienquan_thanhly]
	-- Add the parameters for the stored procedure here
	@ngaythuchien datetime,
	-- hopdong huy
	@hopdongid int,
	-- tai khoan
	@user_name nvarchar(50),

	@chenhlech money
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	truncate table Admarket_xuly_hopdong_lienquan_thanhly
    -- Insert statements for procedure here
	declare @giatridatinhcuacachopdongkhac money

	set @giatridatinhcuacachopdongkhac  =
	isnull(
	(
	select sum(giatrithaydoi+ThanhTienSauTrietKhauThucChay) from ThucChayDaTinhAdmarket where HopDongChiTietREF in 
	(
	select 
	hd.HopDongChiTietID
	from HopDong h inner join hopdongchitiet hd on h.HopDongID = hd.HopDongFK
	where 1=1
	AND h.HopDongID <>  @hopdongid
	AND h.HopDongID in      (select hopdongid from Admarket_XuLy_HopDong_2017)
	AND hd.HopDongChiTietID in (select phanboid from Admarket_XuLy_HopDong_2017)
	AND hd.HopDongChiTietID not in  (select phanboid from Admarket_XuLy_HopDong_DaThanhLy)
	AND hd.HopDongChiTietID not in  (select phanboid from Admarket_XuLy_HopDong_ThanhLy)
	AND hd.DmSanPhamREF in (628,144,585)
	AND hd.TK_AdMarket = @user_name
	)),0)
	set @giatridatinhcuacachopdongkhac = isnull(@giatridatinhcuacachopdongkhac,0)

	if @giatridatinhcuacachopdongkhac >= @chenhlech
	begin
	insert into Admarket_xuly_hopdong_lienquan_thanhly
	select 
	distinct
	h.HopDongID,
	h.SoHopDong,
	hd.HopDongChiTietID,
	hd.TK_AdMarketID,
	hd.TK_AdMarket,
	hd.DmSanPhamREF,
	hd.TenSanPham,
	(select sum(giatrithaydoi+ThanhTienSauTrietKhauThucChay) from ThucChayDaTinhAdmarket where HopDongChiTietREF = hd.HopDongChiTietID),
	(select sum(giatrithaydoi+ThanhTienSauTrietKhauThucChay) from ThucChayDaTinhAdmarket where HopDongChiTietREF = hd.HopDongChiTietID) - 
	(select sum(giatrithaydoi+ThanhTienSauTrietKhauThucChay) from ThucChayDaTinhAdmarket where HopDongChiTietREF = hd.HopDongChiTietID)/@giatridatinhcuacachopdongkhac * @chenhlech,
	(select sum(giatrithaydoi+ThanhTienSauTrietKhauThucChay) from ThucChayDaTinhAdmarket where HopDongChiTietREF = hd.HopDongChiTietID)/@giatridatinhcuacachopdongkhac * @chenhlech,
	@hopdongid,
	@NgayThucHien,
	@giatridatinhcuacachopdongkhac
	from HopDong h inner join hopdongchitiet hd on h.HopDongID = hd.HopDongFK
	where 1=1
	AND h.HopDongID <>  @hopdongid
	AND h.HopDongID in      (select hopdongid from Admarket_XuLy_HopDong_2017)
	AND hd.HopDongChiTietID in (select phanboid from Admarket_XuLy_HopDong_2017)
	AND hd.HopDongChiTietID not in  (select phanboid from Admarket_XuLy_HopDong_DaThanhLy)
	AND hd.HopDongChiTietID not in  (select phanboid from Admarket_XuLy_HopDong_ThanhLy)
	AND hd.DmSanPhamREF in (628,144,585)
	AND hd.TK_AdMarket = @user_name
	end
	--else 
	--begin
	--print '2'
	--insert into Admarket_xuly_hopdong_lienquan_thanhly
	--select 
	--distinct
	--h.HopDongID,
	--h.SoHopDong,
	--hd.TK_AdMarketID,
	--hd.TK_AdMarket,
	--hd.DmSanPhamREF,
	--hd.TenSanPham,
	--(select sum(giatrithaydoi+ThanhTienSauTrietKhauThucChay) from ThucChayDaTinhAdmarket where HopDongChiTietREF = hd.HopDongChiTietID),
	--(select sum(giatrithaydoi+ThanhTienSauTrietKhauThucChay) from ThucChayDaTinhAdmarket where HopDongChiTietREF = hd.HopDongChiTietID),
	--0,
	--@hopdongid,
	--@NgayThucHien,
	--@giatridatinhcuacachopdongkhac
	--from HopDong h inner join hopdongchitiet hd on h.HopDongID = hd.HopDongFK
	--where 1=1
	--AND h.HopDongID <>  @hopdongid
	--AND h.HopDongID in      (select hopdongid from Admarket_XuLy_HopDong_2017)
	--AND hd.HopDongChiTietID in (select phanboid from Admarket_XuLy_HopDong_2017)
	--AND h.HopDongID not in  (select hopdongid from Admarket_XuLy_HopDong_DaThanhLy)
	--AND h.HopDongID not in  (select hopdongid from Admarket_XuLy_HopDong_ThanhLy)
	--AND hd.DmSanPhamREF in (628,144,585)
	--AND hd.TK_AdMarket = @user_name
	--end
END

```
