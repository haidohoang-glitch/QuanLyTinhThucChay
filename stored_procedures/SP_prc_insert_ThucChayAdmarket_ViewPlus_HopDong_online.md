# Stored Procedure: `prc_insert_ThucChayAdmarket_ViewPlus_HopDong_online`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-11 15:02:54.500000
- **Ngày sửa cuối**: 2017-09-11 15:02:54.527000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@user_id` | `nvarchar(200)` | No |
| `@username` | `nvarchar(200)` | No |
| `@isnoibo` | `nvarchar(200)` | No |
| `@contract_number` | `nvarchar(200)` | No |
| `@promotion` | `nvarchar(200)` | No |
| `@domain_name` | `nvarchar(200)` | No |
| `@domain_tt_click` | `nvarchar(200)` | No |
| `@domain_tt_view` | `nvarchar(200)` | No |
| `@domain_money` | `nvarchar(200)` | No |
| `@domain_promotion` | `nvarchar(200)` | No |
| `@campaign_id` | `nvarchar(200)` | No |
| `@DmSanPhamREF` | `nvarchar(200)` | No |
| `@TenSanPham` | `nvarchar(200)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@data_type` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_insert_ThucChayAdmarket_ViewPlus_HopDong_online]
	-- Add the parameters for the stored procedure here
	@user_id nvarchar(100) ,
	@username nvarchar(100) ,
	@isnoibo nvarchar(100) ,
	@contract_number nvarchar(100) ,
	@promotion nvarchar(100) ,
	@domain_name nvarchar(100) ,
	@domain_tt_click nvarchar(100) ,
	@domain_tt_view nvarchar(100) ,
	@domain_money nvarchar(100) ,
	@domain_promotion nvarchar(100) ,
	@campaign_id nvarchar(100) ,
	@DmSanPhamREF nvarchar(100) ,
	@TenSanPham nvarchar(100) ,
	@NgayThucHien datetime ,
	@data_type int 
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	declare @giatrihopdong money

	select @giatrihopdong = sum (a.thanhtien)
	from hopdongchitiet a inner join hopdong b on a.hopdongfk = b.hopdongid
	where a.deletedstatus = 0 
	and b.sohopdong = @contract_number
	and a.dmsanphamref = @DmSanPhamREF
	and a.tk_admarketid = @user_id

    -- Insert statements for procedure here
	INSERT INTO [dbo].[ThucChayAdmarket_ViewPlus_HopDong_online]
           ([user_id]
           ,[username]
           ,[isnoibo]
           ,[contract_number]
           ,[tt_click]
           ,[tt_view]
           ,[money]
           ,[promotion]
           ,[domain_name]
           ,[domain_tt_click]
           ,[domain_tt_view]
           ,[domain_money]
           ,[domain_promotion]
           ,[campaign_id]
           ,[DmSanPhamREF]
           ,[TenSanPham]
           ,[NgayThucHien]
           ,[createdBy]
           ,[createdAt]
           ,[contract_number_change]
           ,[data_type]
           ,[confirm_money]
		   ,giatrihopdong
           ,[trangthai]
		   ,confirm_date
		   ,confirm_status)
     VALUES
	 (
		@user_id ,
		@username ,
		@isnoibo,
		@contract_number ,
		0,
		0,
		0,
		@promotion ,
		@domain_name ,
		@domain_tt_click ,
		@domain_tt_view ,
		@domain_money,
		@domain_promotion ,
		@campaign_id  ,
		@DmSanPhamREF  ,
		@TenSanPham ,
		@NgayThucHien  ,
		'asd',
		getdate(),
		'', --[contract_number_change],
		@data_type  ,
		@giatrihopdong,
		0,
		case when @data_type =3 then 1 else 0 end,
		null,
		0
	 )
END


```
