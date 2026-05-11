# Stored Procedure: `prc_asd_tinhthucchay_admarket_viewplus`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-11 15:02:52.900000
- **Ngày sửa cuối**: 2021-07-08 11:08:45.580000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:	doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--[dbo].[prc_asd_tinhthucchay_admarket_viewplus] '2017-06-06'
CREATE PROCEDURE [dbo].[prc_asd_tinhthucchay_admarket_viewplus]
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	-- dmsanpham = 628
	-- neu tinh lai xoa du lieu da tinh
	--------------------------------------------------------------------------------------------------
	declare @data_type int = 0, @trangthai int, @max_count int, @count_index int = 1;
	--------------------------------------------------------------------------------------------------
	DELETE FROM thucchaydatinh where ngaythuchien = @ngaythuchien and dmsanphamref = 628
	AND DmHinhThucQuangCao <> 42 --haidh them comment 08/07/2021
	and HopDongID not in (Select HopDongREF from DmThongTinHopDongBanInventory) -- tuyetnta thêm ngày 29/04/2020, loại hd inventory
	AND DotChayHopDong <> N'MUA NGOAI';
	DELETE FROM thucchaydatinhadmarket where ngaythuchien = @ngaythuchien and dmsanphamref = 628
	AND DmHinhThucQuangCao <> 42 --haidh them comment 08/07/2021
	and HopDongID not in (Select HopDongREF from DmThongTinHopDongBanInventory) -- tuyetnta thêm ngày 29/04/2020, loại hd inventory
	AND DotChayHopDong <> N'MUA NGOAI';
	--DELETE FROM ThucChayAdmarket_ViewPlus_HopDong_online where   ngaythuchien = @ngaythuchien;
	DELETE FROM ThucChayAdmarket_Error WHERE ngaythuchien = @ngaythuchien;
	--------------------------------------------------------------------------------------------------

	create table #ThucChayAdmarket_ViewPlus_HopDong_team
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
		[NgayThucHien] [datetime] NULL,
		stt int
	)

	insert into #ThucChayAdmarket_ViewPlus_HopDong_team 
	select 
		distinct
		[user_id] ,
		[username] ,
		[isnoibo],
		[contract_number],
		[promotion],
		[domain_name],
		sum(convert(int,domain_tt_click)),
		sum(convert(int,domain_tt_view)),
		sum(convert(money,domain_money)),
		sum(convert(money,domain_promotion)),
		[DmSanPhamREF],
		[TenSanPham],
		[NgayThucHien],
		row_number() over(order by [user_id])
	from ThucChayAdmarket_ViewPlus_HopDong where convert(date,NgayThucHien )= @ngaythuchien and [isnoibo] = 0 AND domain_money > 0
	-- tham khao y kien tuyetnta do khong co phan bo noi bo cho cac san pham nay
	group by	[user_id] ,
				[username] ,
				[isnoibo],
				[contract_number],
				[promotion],
				[domain_name],
				[DmSanPhamREF],
				[TenSanPham],
				[NgayThucHien]

	--select * from #ThucChayAdmarket_ViewPlus_HopDong_team
	--------------------------------------------------------------------------------------------------
	-- tong so luong ban ghi
	select @max_count = count(1) from #ThucChayAdmarket_ViewPlus_HopDong_team;
	--print @max_count
	--------------------------------------------------------------------------------------------------
	declare @user_id nvarchar(100) ,
			@username nvarchar(100) ,
			@isnoibo nvarchar(100) ,
			@contract_number nvarchar(100) ,
			@promotion nvarchar(100) ,
			@domain_name nvarchar(100) ,
			@domain_tt_click int ,
			@domain_tt_view int ,
			@domain_money money,
			@domain_promotion money,
			@DmSanPhamREF nvarchar(100) ,
			@TenSanPham nvarchar(100) ,
			@NgayTinh datetime 

	declare @giatrihopdong money, @thanhtienthucchayhopdong money, @giatrithucchaythua money,
			@tientinhthucchay money, @tiendovaoonline money = 0,
			@domain_tt_click_online int, @domain_tt_view_onlie int;

	while @count_index <= @max_count
	begin
		select 
				@user_id = [user_id] ,
				@username = username ,
				@isnoibo = isnoibo,
				@contract_number  = contract_number,
				@promotion = promotion,
				@domain_name = domain_name,
				@domain_tt_click = domain_tt_click,
				@domain_tt_view = domain_tt_view,
				@domain_money = domain_money/1.1,-- gia tri tra ve da bao gom vat
				@domain_promotion = domain_promotion,
				@DmSanPhamREF = DmSanPhamREF,
				@TenSanPham = TenSanPham,
				@NgayTinh = NgayThucHien
		from #ThucChayAdmarket_ViewPlus_HopDong_team where stt = @count_index and domain_money > 0;

		set @tientinhthucchay = @domain_money
		 
		-----set data_tye
		if isnull(@contract_number,'') = '' 
		begin
			set @data_type = 1;
			set @tiendovaoonline = @domain_money;
			set @domain_tt_click_online = @domain_tt_click;
			set @domain_tt_view_onlie = @domain_tt_view;
		end

		if isnull(@contract_number,'') <> ''
			begin
			    

				select @giatrihopdong = sum(isnull(ThanhTien,0)) from hopdongchitiet where 
				dmSanPhamREF in (628) and deletedstatus = 0 and TK_AdMarket = @username and
				hopdongfk = (select top 1 hopdongid from hopdong where  sohopdong = @contract_number);
				
				

				select @thanhtienthucchayhopdong = sum(isnull(thanhtiensautrietkhauthucchay,0))  from thucchaydatinhadmarket 
				where sohopdong = @contract_number and dmSanPhamREF in (628)
				and hopdongchitietref in (select hopdongchitietID from hopdongchitiet where dmSanPhamREF in (628) and deletedstatus = 0 and TK_AdMarket = @username and
				hopdongfk = (select top 1 hopdongid from hopdong where  sohopdong = @contract_number));

			--select * from thucchaydatinhadmarket

				set @giatrihopdong = isnull(@giatrihopdong,0)

				set @thanhtienthucchayhopdong = isnull(@thanhtienthucchayhopdong,0)

				--print @giatrihopdong;
				--print @thanhtienthucchayhopdong;
				--print @contract_number;
				--print @DmSanPhamREF;
				--print @user_id;
				--print '---------------'
				if @giatrihopdong - @thanhtienthucchayhopdong <=0 
				begin 
					set @data_type = 2 ;
					--print('da vao')
					set @tientinhthucchay = 0;
					set @tiendovaoonline = @domain_money;
					set @domain_tt_click_online = @domain_tt_click;
					set @domain_tt_view_onlie = @domain_tt_view;
				end 

				if @giatrihopdong - @thanhtienthucchayhopdong >0 and @giatrihopdong - @thanhtienthucchayhopdong - @domain_money <=0 
				begin
					set @data_type = 3;
					set @tientinhthucchay = 0;
					set @tiendovaoonline =  @domain_money + @thanhtienthucchayhopdong - @giatrihopdong;
					set @domain_tt_click_online = @domain_tt_click;
					set @domain_tt_view_onlie = @domain_tt_view; 
				end

				if @giatrihopdong - @thanhtienthucchayhopdong - @domain_money >=0
				begin
					set @data_type = 0;
					set @tiendovaoonline = 0;
				end

			end 
		------------------
		------ insert du lieu online
		if @tiendovaoonline > 0 
		begin
			-- insert bảng luu lại online
			exec prc_insert_ThucChayAdmarket_ViewPlus_HopDong_online    @user_id ,
																		@username ,
																		@isnoibo ,
																		@contract_number ,
																		@promotion ,
																		@domain_name ,
																		@domain_tt_click_online ,
																		@domain_tt_view_onlie ,
																		@tiendovaoonline ,
																		@domain_promotion ,
																		0 ,
																		@DmSanPhamREF ,
																		@TenSanPham,
																		@NgayThucHien  ,
																		@data_type 
								
		end ;

		-- luu dl canh bao dl tra ve vuot qua gt hop dong
		if @data_type in (2,3)
		begin
			exec [dbo].[prc_asd_insert_HopDong_CanhBaoThucChay_Admarket]	@NgayThucHien ,
																			@contract_number ,
																			@DmSanPhamREF ,
																			@TenSanPham ,
																			null,
																			null,
																			@giatrihopdong,
																			@thanhtienthucchayhopdong ,
																			@domain_money ,
																			'DOANNV'
		end
		-- luu dl khong so hd
		if @data_type in (1)
		begin
			exec [dbo].[prc_asd_insert_khongsohopdong_Admarket] @NgayThucHien ,
															@DmSanPhamREF ,
															@TenSanPham,
															null  ,
															null ,
															@domain_tt_view ,
															@domain_tt_click ,
															@domain_money ,
															'DOANNV' 
		end
		-------------------------------------
		--print @data_type
		--------------------------- th du lieu tra ve binh thuong---------------
		if @data_type not in (1,2)
		begin
		-- tinh thuc chay
		
		--print 'tinh'
			exec [dbo].[prc_asd_tinhthucchay_admarket_viewplus_chitiet] @user_id ,
																		@username ,
																		@isnoibo ,
																		@contract_number ,
																		@promotion ,
																		@domain_name ,
																		@domain_tt_click ,
																		@domain_tt_view ,
																		@domain_money ,
																		@domain_promotion ,
																		@DmSanPhamREF ,
																		@TenSanPham ,
																		@NgayTinh 
																	
		end
		------------------------------------------------------------------------
		set @count_index +=1;
	end
	--------------------------------------------------------------------------------------------------
	drop table #ThucChayAdmarket_ViewPlus_HopDong_team;
	--------------------------------------------------------------------------------------------------
END



```
