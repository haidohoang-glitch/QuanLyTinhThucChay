# Stored Procedure: `prc_asd_tinhthucchay_sanphamadmarket_PhanBo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-02-06 10:57:43.093000
- **Ngày sửa cuối**: 2024-02-28 11:35:43.840000

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
CREATE PROCEDURE [dbo].[prc_asd_tinhthucchay_sanphamadmarket_PhanBo]
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	--------------------------------------------------------------------------------------------------
	declare @data_type int = 0, @trangthai int, @max_count int, @count_index int = 1;
	declare @DonViTinh nvarchar(50) = N'CPC'
	--------------------------------------------------------------------------------------------------
	
	DELETE FROM thucchaydatinh where ngaythuchien =@ngaythuchien and dmsanphamref in (585,144,628) AND DmHinhThucQuangCao <> 42 
	and HopDongID not in (Select HopDongREF from DmThongTinHopDongBanInventory) -- tuyetnta thêm ngày 29/04/2020, loại hd inventory
	AND DotChayHopDong <> N'MUA NGOAI'
	DELETE from thucchaydatinhadmarket where ngaythuchien = @ngaythuchien and dmsanphamref in (585,144) AND DmHinhThucQuangCao <> 42
	and HopDongID not in (Select HopDongREF from DmThongTinHopDongBanInventory) -- tuyetnta thêm ngày 29/04/2020, loại hd inventory;
	AND DotChayHopDong <> N'MUA NGOAI'
	------------------------------------------------------------------------------------------------
	--1. TH1: TINH CHO TH CO PHAN BO
	create table #ThucChayAdmarket_SanPham_HopDong_team
	(
		[user_id] [nvarchar](100) NULL,
		[username] [nvarchar](100) NULL,
		[isnoibo] [nvarchar](100) NULL,
		[contract_number] [nvarchar](100) NULL,
		[promotion] float NULL,
		[domain_name] [nvarchar](100) NULL,
		[domain_tt_click] [int] NULL,
		[domain_tt_view] [int] NULL,
		[domain_money] [float] NULL,
		[domain_promotion] [float] NULL,
		[HopDongChiTietREF] [int] NULL,
		[DmSanPhamREF] int NULL,
		[TenSanPham] [nvarchar](100) NULL,
		[DmViTriREF] [int] NULL,
		[TenViTri] [nvarchar](100) NULL,
		[NgayThucHien] [datetime] NULL,
		[NhanHang] [nvarchar](100) NULL,
		stt [int],
		status_record [smallint]
	)

	insert into #ThucChayAdmarket_SanPham_HopDong_team 
	SELECT 
		distinct
		[user_id] ,
		[username] ,
		[isnoibo],
		[contract_number],
		convert(float,[promotion]),
		[domain_name],
		sum(convert(int,domain_tt_click)),
		sum(convert(int,domain_tt_view)),
		sum(convert(float,domain_tt_money)),
		sum(convert(float,domain_tt_promotion)),
		convert(int,phanbo),
		convert(int,[DmSanPhamREF]),
		[TenSanPham],
		convert(int,[DmViTriREF]),
		[TenViTri],
		[NgayThucHien],
		[nhanhangid],
		row_number() over(order by [user_id]),
		0 status_record -- 0 trang thai chua duoc tinh, 1 trang thai da duoc tinh
	FROM dbo.ThucChayAdmarket_PhanBo
	WHERE convert(date,NgayThucHien )= @ngaythuchien
	AND domain_tt_money >0
	AND phanbo <> 0 --TINH CHO TH CÓ PHAN BO
	group by	[user_id] ,
				[username] ,
				[isnoibo],
				[contract_number],
				[promotion],
				[domain_name],
				[phanbo],
				[DmSanPhamREF],
				[TenSanPham],
				[DmViTriREF],
				[TenViTri],
				[NgayThucHien],
				[nhanhangid]

				--------------------------------------------------------------------------------------------------
	-- tong so luong ban ghi
	select @max_count = count(1) from #ThucChayAdmarket_SanPham_HopDong_team;
	
	--------------------------------------------------------------------------------------------------
	declare @user_id nvarchar(100) ,
			@username nvarchar(100) ,
			@isnoibo nvarchar(100) ,
			@contract_number nvarchar(100) ,
			@promotion float ,
			@domain_name nvarchar(100) ,
			@domain_tt_click int ,
			@domain_tt_view int ,
			@domain_money float,
			@domain_promotion float,
			@HopDongChiTietREF int,
			@DmSanPhamREF int ,
			@TenSanPham nvarchar(100) ,
			@DmViTriREF int ,
			@TenViTri nvarchar(100) ,
			@NgayTinh datetime ,
			@NhanHang nvarchar(100),
			@Status_record smallint

	declare @giatrihopdong float, @thanhtienthucchayhopdong float, @giatrithucchaythua float,
			@tientinhthucchay float, @tiendovaoonline float = 0,
			@domain_tt_click_online int, @domain_tt_view_onlie int;

	while @count_index <= @max_count
	begin
		--print @count_index
		select 
				@user_id = [user_id] ,
				@username = username ,
				@isnoibo = isnoibo,
				@contract_number  = contract_number,
				@promotion = promotion,
				@domain_name = domain_name,
				@domain_tt_click = domain_tt_click,
				@domain_tt_view = domain_tt_view,
				@domain_money = domain_money,-- gia tri tra ve khong bao gom vat
				@domain_promotion = domain_promotion,
				@HopDongChiTietREF = HopDongChiTietREF,
				@DmSanPhamREF = DmSanPhamREF,
				@TenSanPham = TenSanPham,
				@DmViTriREF = DmViTriREF,
				@TenViTri = TenViTri ,
				@NgayTinh = NgayThucHien,
				@NhanHang = nhanhang
		from #ThucChayAdmarket_SanPham_HopDong_team where stt = @count_index and domain_money >0;

		declare @GhiChu nvarchar(2000) = N'', @domain_ref int = 0,
			@DmMaHopDongREF int =0, @TenMaHopDong nvarchar(100) = N''
		
		IF((@isnoibo = 1) or (@contract_number like 'NB%' or @contract_number like 'SH%' or @contract_number like 'S-NB%'))
		BEGIN
			SET @DmMaHopDongREF = 310
			SET @TenMaHopDong = N'NB'
		END
		ELSE
		BEGIN
			SET @DmMaHopDongREF = 0
			SET @TenMaHopDong = ''
		END
		set @domain_ref = dbo.GetWebsiteIDByDomainName(@domain_name)

		IF isnull(@domain_ref,0)=0
		BEGIN
			INSERT INTO dbo.DmWebsiteReportingdb
				(
				TenWebsite,
				CreatedBy,
				CreatedAt,
				LastModifiedBy,
				LastModifiedAt,
				DeletedStatus,
				PrintStatus,
				RecordStatus,
				ID
				)
			VALUES
				(
				@domain_name,	-- TenWebsite - nvarchar(200)
				N'asd',	-- CreatedBy - nvarchar(50)
				GETDATE(),	-- CreatedAt - datetime
				N'asd',	-- LastModifiedBy - nvarchar(50)
				GETDATE(),	-- LastModifiedAt - datetime
				0,	-- DeletedStatus - int
				0,	-- PrintStatus - int
				0,	-- RecordStatus - int
				N'New' -- ID - nvarchar(50)
				)		
			SET @domain_ref = @@IDENTITY
		END	

		set @tientinhthucchay = @domain_money

		-----set data_type: 1: khong ton tai so hop dong , = 2 gia tri thucchaydatinh >= thanhtienphanbo
		--, = 3 gia tri thucchaydatinh < thanhtienphanbo
		-- 1.1 TH: KHONG TIN TAI SOHOPDONG
		if (isnull(@contract_number,'') = '' or @contract_number = N'BLANK')
		begin
			set @data_type = 1;
			set @tiendovaoonline = @domain_money;
			set @domain_tt_click_online = @domain_tt_click;
			set @domain_tt_view_onlie = @domain_tt_view;
		end
		--1.2 TH : TON TAI SOHOPDONG
		else
			--1.2.1 TH: CO SOHOPDONG NHUNG KHONG CO PHANBO CAN TINH
			if not exists(SELECT TOP (1) hd.HopDongID FROM dbo.HopDong hd 
						INNER JOIN dbo.HopDongChiTiet hdct ON hd.Hopdongid = hdct.HopDongFk
						WHERE hd.SoHopDong = @contract_number 
						AND hdct.HopDongChiTietID = @HopDongChiTietREF 
						AND hdct.DmSanPhamREF = @DmSanPhamREF
						AND hdct.tk_admarketid = @user_id
						AND hdct.deletedstatus = 0 ORDER BY hdct.HopDongChiTietID
			)
			begin
				set @data_type = 1;
				set @tiendovaoonline = @domain_money;
				set @domain_tt_click_online = @domain_tt_click;
				set @domain_tt_view_onlie = @domain_tt_view;
			end
			--1.2.2 TH: CO SOHOPDONG VA CO PHANBO CAN TINH
			else
			begin

				select top 1 @giatrihopdong = sum(isnull(ThanhTien,0)) from hopdongchitiet where 
				dmSanPhamREF = @DmSanPhamREF and deletedstatus = 0 and TK_AdMarket = @username and
				hopdongchitietid = @HopDongChiTietREF;

				select top 1 @thanhtienthucchayhopdong = sum(isnull(thanhtiensautrietkhauthucchay+GiaTriThayDoi,0))  
				from thucchaydatinhadmarket where sohopdong = @contract_number 
				and dmSanPhamREF = @DmSanPhamREF
				and HopDongChiTietREF = @HopDongChiTietREF

				set @thanhtienthucchayhopdong = isnull(@thanhtienthucchayhopdong,0);
				set @giatrihopdong = isnull(@giatrihopdong,0)

				--- TH: NEU GIA TRI THUCCHAYDATINH >= THANHTIENPHANBO
				if @giatrihopdong - @thanhtienthucchayhopdong <=0 
				begin 
					set @data_type = 2 ;
					set @tientinhthucchay = 0;
					set @tiendovaoonline = @domain_money;
					set @domain_tt_click_online = @domain_tt_click;
					set @domain_tt_view_onlie = @domain_tt_view;
				end 

				---TH: GIA TRI THUCCHAYDATINH < THANHTIENPHANBO VA GIATRITHUCCHAY KHONG DO DUOC FULL VAO PHANBO
				if @giatrihopdong - @thanhtienthucchayhopdong >0 and @giatrihopdong - @thanhtienthucchayhopdong - @domain_money <=0 
				begin
					set @data_type = 3;
					set @tientinhthucchay = 0;
					set @tiendovaoonline =  @domain_money + @thanhtienthucchayhopdong - @giatrihopdong;
					set @domain_tt_click_online = @domain_tt_click;
					set @domain_tt_view_onlie = @domain_tt_view; 
				end
				--- TH: GIATRITHUCCHAY DO FULL DUOC VAO PHANBO
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
			--print 'insert bảng luu lại dl cảnh báo và online'
			-- TH: @data_type = 1,2,3
			-- data_type = 2,3 phan thuc chay co phanbo nhung bi vuot gia tri
			-- data_type = 1 phanbo <> 0 khong phu hop do theo hopdong vao online
			
			-- B1: -- insert dl vao table canhbao [ThucChayAdmarket_HopDong_online] 
			exec [dbo].[prc_insert_ThucChayAdmarket_HopDong_online_PhanBo]     @user_id ,
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
																		@HopDongChiTietREF,
																		@DmSanPhamREF ,
																		@TenSanPham,
																		@DmViTriREF ,
																		@TenViTri,
																		@NgayThucHien  ,
																		@DonViTinh,
																		@NhanHang,
																		@data_type 
			
			--B2: Thuc hien insert dl thucchay online vao table ThucChayDaTinhAdmarket, DotChayHopDong = 'Thuc_Chay_Admarket_PhanBo_online', SoLuongDotChayHD = @HopDongChiTietREF, 
			-- SoLuongDotChayBooking =2,3: canh bao dl tra ve vuot qua gt hop dong; 1: Hopdong ko co phabo phu hop tinh, 0 online bt

			SET @GhiChu = N'Thuc_Chay_Admarket_PhanBo_online'
	
			exec [dbo].[ThucChayDaTinhAdmarket_InsertNoContractByProduct_PhanBo]
																		@DmSanPhamREF			= @DmSanPhamREF,
																		@TenSanPham				= @TenSanPham,
																		@DonViTinh				= @DonViTinh,
																		@DmWebsiteREF			= @domain_ref,
																		@TenWebsite				= @domain_name,
																		@NgayThucHien			= @NgayThucHien,
																		@SoLuongThucChay		= @domain_tt_click_online,
																		@SoLuongThhucChayKM		= 0,
																		@ThanhTienThucChay		= @tiendovaoonline,
																		@ThanhTienThucChayKM	= 0,
																		@DmMaHopDongREF			= @DmMaHopDongREF,
																		@TenMaHopDong			= @TenMaHopDong,
																		@GhiChu					= @GhiChu,
																		@GiaTriThayDoi			= 0,
																		@SoLuongThayDoi			= 0,
																		@DmViTriREF				= @DmViTriREF,
																		@TenViTri				= @TenViTri,
																		@NhanHang				= @NhanHang,
																		@HopDongChiTietREF		= @HopDongChiTietREF,	
																		@data_type				= @data_type
				
		end ;
		-- luu dl canh bao dl tra ve vuot qua gt hop dong
		if @data_type in (2,3)
		begin
			--print 'luu dl canh bao dl tra ve vuot qua gt hop dong'
			exec [dbo].[prc_asd_insert_HopDong_CanhBaoThucChay_Admarket_PhanBo]	@NgayThucHien ,
																			@contract_number ,
																			@HopDongChiTietREF,
																			@DmSanPhamREF ,
																			@TenSanPham ,
																			@DmviTriREF,
																			@TenViTri,
																			@giatrihopdong,
																			@thanhtienthucchayhopdong ,
																			@domain_money ,
																			'HAIDH'
		end
		-- luu dl canh bao phanbo khong co so hd hoac so hopdong khong ton tai phan bo
		if @data_type in (1)
		begin
			--print 'luu dl khong so hd'
			exec [dbo].[prc_asd_insert_khongsohopdong_Admarket_PhanBo] @NgayThucHien ,
															@HopDongChiTietREF,
															@DmSanPhamREF ,
															@TenSanPham,
															@DmviTriREF,
															@TenViTri,
															@domain_tt_view ,
															@domain_tt_click ,
															@domain_money ,
															'DOANNV' 
		end
		-------------------------------------
		------------------------- th du lieu tra ve binh thuong---------------
		if @data_type not in (1,2)
		begin
		-- tinh thuc chay
			--print 'th du lieu tra ve binh thuong'
			exec [dbo].[prc_asd_tinhthucchay_admarket_chitiet_PhanBo]
					@user_id = @user_id ,
					@username = @username ,
					@isnoibo = @isnoibo ,
					@contract_number = @contract_number ,
					@promotion = @promotion ,
					@domain_name = @domain_name ,
					@domain_tt_click = @domain_tt_click ,
					@domain_tt_view = @domain_tt_view ,
					@domain_money = @domain_money,
					@domain_promotion = @domain_promotion,
					@HopDongChiTietREF = @HopDongChiTietREF,
					@DmSanPhamREF = @DmSanPhamREF ,
					@TenSanPham = @TenSanPham ,
					@DmViTriREF = @DmviTriREF ,
					@TenViTri = @TenViTri ,
					@DonViTinh = @DonViTinh,
					@NhanHang = @NhanHang,
					@NgayThucHien = @NgayTinh,
					@GhiChu		= N''
			
													
		end
		------------------------------------------------------------------------
		--print 'end'
		set @count_index +=1;
	end
	--------------------------------------------------------------------------------------------------
	drop table #ThucChayAdmarket_SanPham_HopDong_team;
	--------------------------------------------------------------------------------------------------

	--2. TH2: TINH CHO KHONG CO PHAN BO SE DUOC XL KHI SU DUNG HAM CAN 
	--[ThucChayDaTinhAdmarket_InsertThucChayNoContract] 
	
END



```
