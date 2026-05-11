# Stored Procedure: `prc_admarket_xuly_insert_hopdong_thanhly`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-12-15 10:23:25.047000
- **Ngày sửa cuối**: 2017-12-15 15:06:20.333000

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
CREATE PROCEDURE [dbo].[prc_admarket_xuly_insert_hopdong_thanhly]
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	truncate table  Admarket_XuLy_HopDong_ThanhLy

	insert into Admarket_XuLy_HopDong_ThanhLy
	select distinct
	a.HopDongID,
	a.SoHopDong,
	c.HopDongChiTietID,
	c.TK_AdMarketID,
	c.TK_AdMarket,
	c.DmSanPhamREF,
	c.TenSanPham,
	isnull((select sum(giatrithaydoi+ThanhTienSauTrietKhauThucChay) from ThucChayDaTinhAdmarket tc where tc.HopDongChiTietREF = c.HopDongChiTietID),0),
	c.ThanhTien,
	c.ThanhTien - isnull((select sum(giatrithaydoi+ThanhTienSauTrietKhauThucChay) from ThucChayDaTinhAdmarket tc where tc.HopDongChiTietREF = c.HopDongChiTietID),0),
	@NgayThucHien
	from Hopdong a 
	inner join HopDongAttachFile b on a.HopDongID = b.HopDongREF
	inner join HopDongChiTiet c on a.HopDongID = c.HopDongFK
	where 1=1
	AND a.HopDongID in      (select hopdongid from Admarket_XuLy_HopDong_2017)
	AND c.HopDongChiTietID in (select phanboid from Admarket_XuLy_HopDong_2017)
	AND c.HopDongChiTietID not in  (select phanboid from Admarket_XuLy_HopDong_DaThanhLy)
	AND c.HopDongChiTietID not in  (select phanboid from Admarket_XuLy_HopDong_ThanhLy)
	AND b.FileTypeREF = 7
	AND b.DeletedStatus = 0
	AND ABS (c.ThanhTien - isnull((select sum(giatrithaydoi+ThanhTienSauTrietKhauThucChay) from ThucChayDaTinhAdmarket tc where tc.HopDongChiTietREF = c.HopDongChiTietID),0)) >=100
	AND isnull((select sum(giatrithaydoi+ThanhTienSauTrietKhauThucChay) from ThucChayDaTinhAdmarket tc where tc.HopDongChiTietREF = c.HopDongChiTietID),0) > 10

END

```
