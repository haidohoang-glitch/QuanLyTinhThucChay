# Stored Procedure: `prc_asd_xuly_confirm_data_vuothopdong_adx_cpc`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-11 15:02:53.170000
- **Ngày sửa cuối**: 2017-09-11 15:02:53.210000

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
CREATE PROCEDURE [dbo].[prc_asd_xuly_confirm_data_vuothopdong_adx_cpc] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	----------------------------------------------------------------------------------------------
	create table #ThucChayAdmarket_adx_cpc_HopDongVuotGiaTri_team
	(
		[user_id] [nvarchar](100) NULL,
		[username] [nvarchar](100) NULL,
		[isnoibo] [nvarchar](100) NULL,
		[contract_number] [nvarchar](100) NULL,
		[promotion] [nvarchar](100) NULL,
		[domain_name] [nvarchar](100) NULL,
		[domain_tt_click] [int] NULL,
		[domain_tt_view] [int] NULL,
		[domain_money] [money] NULL,
		[domain_promotion] [money] NULL,
		[DmSanPhamREF] [nvarchar](100) NULL,
		[TenSanPham] [nvarchar](100) NULL,
		[DmViTriREF] [nvarchar](100) NULL,
		[TenViTri] [nvarchar](100) NULL,
		[NgayThucHien] [datetime] NULL,
		[contract_number_change] [nvarchar](100) NULL,
		[data_type] int,
		[confirm_money] money,
		[stt] [int] NULL,
	)
	----------------------------------------------------------------------------------------------
	insert into #ThucChayAdmarket_adx_cpc_HopDongVuotGiaTri_team
	select 
		[user_id],
		[username] ,
		[isnoibo],
		[contract_number],
		[promotion],
		[domain_name],
		[domain_tt_click],
		[domain_tt_view],
		[domain_money],
		[domain_promotion],
		[DmSanPhamREF],
		[TenSanPham],
		[DmViTriREF] ,
		[TenViTri] ,
		[NgayThucHien],
		[contract_number_change],
		case when isnull([contract_number_change],'') = '' then [data_type] else 4 end,
		[confirm_money],
		row_number() over(order by [user_id])
	from [dbo].ThucChayAdmarket_ADX_CPC_HopDong_online 
	where 1=1
	and isnull([trangthai],0) = 0 
	and isnull([confirm_status],0) = 1
	and convert(date,ngaythuchien) = @NgayThucHien
	----------------------------------------------------------------------------------------------
	-- cap nhat trang thai da xu ly
	update [dbo].ThucChayAdmarket_ADX_CPC_HopDong_online 
	set [trangthai] = 1
	from [dbo].[ThucChayAdmarket_ViewPlus_HopDong_online] a 
	inner join #ThucChayAdmarket_adx_cpc_HopDongVuotGiaTri_team b
	on a.[contract_number] = b.[contract_number] and a.[user_id] = b.[user_id] and convert(date,a.ngaythuchien) = @NgayThucHien
	----------------------------------------------------------------------------------------------
	
	----------------------------------------------------------------------------------------------
	declare 
			@SoHopDong nvarchar(50),
			@SoHopDong_change nvarchar(50),
			@user_id nvarchar(50), 
			@DmSanPhamREF int,
			@TenSanPham nvarchar(500),
			@DmViTriREF int,
			@TenViTri nvarchar(500),
			@domain_name nvarchar(500),
			@domain_money money,
			@domain_tt_click int,
			@domain_tt_view int,
			@confirm_money money,
			@data_type int ,
			@giatrilech money
	DECLARE db_cursor_xuly_viewplus_vuot_hopdong_adx_cpc CURSOR FOR  
	SELECT 
			 [contract_number],
			 [contract_number_change],
			 [user_id],
			 [DmSanPhamREF],
			 [TenSanPham],
			 [DmViTriREF],
			 [TenViTri],
			 [domain_name],
			 [domain_money],
			 [domain_tt_click],
			 [domain_tt_view],
			 [data_type]
	FROM #ThucChayAdmarket_adx_cpc_HopDongVuotGiaTri_team
	WHERE domain_money > 0

	OPEN db_cursor_xuly_viewplus_vuot_hopdong_adx_cpc   
	FETCH NEXT FROM db_cursor_xuly_viewplus_vuot_hopdong_adx_cpc INTO   @SoHopDong ,
																@SoHopDong_change ,
																@user_id , 
																@DmSanPhamREF ,
																@TenSanPham ,
																@DmViTriREF,
																@TenViTri,
																@domain_name ,
																@domain_money ,
																@domain_tt_click ,
																@domain_tt_view ,
																@confirm_money ,
																@data_type    

	WHILE @@FETCH_STATUS = 0   
	BEGIN  
		   ---------insert phan lech confirm voi gt thuc te vao online
		   set @giatrilech = @domain_money - @confirm_money
		   exec prc_insert_ThucChayAdmarket_ADX_CPC_HopDong_online     @user_id ,
																		'' ,
																		'' ,
																		@SoHopDong ,
																		'' ,
																		@domain_name ,
																		'1' ,
																		'1' ,
																		@giatrilech,
																		'0' ,
																		'0' ,
																		@DmSanPhamREF ,
																		@TenSanPham,
																		@DmViTriREF,
																		@TenViTri,
																		@NgayThucHien  ,
																		4 
	       --------------------------------------------------------------------------------- 
		   exec [dbo].[prc_asd_xuly_confirm_data_vuothopdong_chitiet_adx_cpc] @SoHopDong ,
																@SoHopDong_change ,
																@user_id , 
																@DmSanPhamREF ,
																@TenSanPham ,
																@domain_name ,
																@domain_money ,
																@domain_tt_click ,
																@domain_tt_view ,
																@confirm_money ,
																@data_type 

		   FETCH NEXT FROM db_cursor_xuly_viewplus_vuot_hopdong_adx_cpc INTO	@SoHopDong ,
																			@SoHopDong_change ,
																			@user_id , 
																			@DmSanPhamREF ,
																			@TenSanPham ,
																			@DmViTriREF,
																			@TenViTri,
																			@domain_name ,
																			@domain_money ,
																			@domain_tt_click ,
																			@domain_tt_view ,
																			@confirm_money ,
																			@data_type      
	END   

	CLOSE db_cursor_xuly_viewplus_vuot_hopdong_adx_cpc   
	DEALLOCATE db_cursor_xuly_viewplus_vuot_hopdong_adx_cpc
	----------------------------------------------------------------------------------------------
	drop table #ThucChayAdmarket_adx_cpc_HopDongVuotGiaTri_team
	
	
	----------------------------------------------------------------------------------------------
END


```
