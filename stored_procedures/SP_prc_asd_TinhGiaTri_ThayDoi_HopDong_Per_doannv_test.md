# Stored Procedure: `prc_asd_TinhGiaTri_ThayDoi_HopDong_Per_doannv_test`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-11-04 11:02:54.277000
- **Ngày sửa cuối**: 2017-11-04 11:17:12.660000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDong_ID` | `int(4)` | No |
| `@PhanBo_ID` | `int(4)` | No |
| `@DmSanPham_ID` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(400)` | No |
| `@GiaTriTaiThoiDiemTinhThucChay` | `money(8)` | No |
| `@GiaTriGanNhatThayDoi` | `money(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>

-- =============================================
--exec [dbo].[prc_asd_TinhGiaTri_ThayDoi_HopDong_Per_doannv_test]	 '2017-11-02',502883,506732,585,'ADX',31298364,46600000
CREATE PROCEDURE [dbo].[prc_asd_TinhGiaTri_ThayDoi_HopDong_Per_doannv_test]
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime,
	@HopDong_ID int,
	@PhanBo_ID int,
	@DmSanPham_ID int,
	@TenSanPham nvarchar(200),
	@GiaTriTaiThoiDiemTinhThucChay money,
	@GiaTriGanNhatThayDoi money
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	declare @SoHopDong nvarchar(50),@GiaTriOnline money,@User_id nvarchar(50), @User_Name nvarchar(100)
	declare @Domain_id int, @Domain_Name nvarchar(500)
	select @SoHopDong = SoHopDong from HopDong Where HopDongID = @HopDong_ID
	declare @GiaTriThucChayPhanBo money = isnull((select SUM(isnull(GiaTriThayDoi,0)+isnull(ThanhTienSauTrietKhauThucChay,0)) 
	from ThucChayDaTinhAdmarket
	where 
	HopDongChiTietREF = @PhanBo_ID and DmSanPhamREF = @DmSanPham_ID and ngaythuchien < @ngaythuchien),0)
	--- san pham la view plus
	if @DmSanPham_ID = 628
	begin
			select @User_id = TK_AdMarketID,@User_Name = TK_AdMarket from HopDongChiTiet where HopDongChiTietID = @PhanBo_ID
			select top 1 @Domain_Name = domain_name  
			from [dbo].[ThucChayAdmarket_ViewPlus_HopDong_online] where contract_number = @SoHopDong and trangthai = 0
			
			set @Domain_id = dbo.GetWebsiteIDByDomainName(@Domain_Name)
			select @GiaTriOnline = SUM(convert(money,domain_money)) from [dbo].[ThucChayAdmarket_ViewPlus_HopDong_online] 
			where contract_number = @SoHopDong 
			and trangthai = 0
			and user_id = @User_id
			set @GiaTriOnline = isnull(@GiaTriOnline,0)
		-- Nếu tăng giá trị
	    if @GiaTriTaiThoiDiemTinhThucChay > @GiaTriGanNhatThayDoi  
		begin
		    if @GiaTriOnline > 0
			begin
			declare @Online nvarchar(50) =  convert(nvarchar(50),@GiaTriOnline - @GiaTriTaiThoiDiemTinhThucChay + @GiaTriGanNhatThayDoi)
			-- nhan hang
			declare @nhanhang_thucchay nvarchar(500) = (select top 1 DanhSachNhanHangREF from HopDongChiTiet where HopDongChiTietID = @PhanBo_ID)
			-- update đã sử dụng dl online
			update [dbo].[ThucChayAdmarket_ViewPlus_HopDong_online] set trangthai = 1 where contract_number = @SoHopDong and user_id = @User_id
			-- để phần thừa vào online
			if @GiaTriOnline > (@GiaTriTaiThoiDiemTinhThucChay - @GiaTriGanNhatThayDoi)
			begin
			exec prc_insert_ThucChayAdmarket_ViewPlus_HopDong_online 
																@User_id,
																@User_Name,
																'0',
																@SoHopDong,
																'0',
																'',
																'0',
																'0',
																@Online,
																'0',
																'0',
																@DmSanPham_ID,
																'',
																@NgayThucHien,
																0
			-- insert thực chạy
			declare @GiaTriTinhThucChay float = @GiaTriTaiThoiDiemTinhThucChay - @GiaTriGanNhatThayDoi
			
			exec [dbo].[prc_asd_ThucChayDaTinhAdmarket_InsertByPhanBoID_ThayDoiHopDong]
				@ngaythuchien,
				@SoHopDong,
				@PhanBo_ID,
				@DmSanPham_ID,
				@TenSanPham,
				@Domain_id,
				@domain_name,
				0,
				0,
				0,
				@GiaTriTinhThucChay,
				0,
				0,
				0,
				0,
				1,
				'CPC',
				N'Thuc_Chay_Admarket Đổ online tăng gt hợp đồng 1',
				0,
				'',
				@nhanhang_thucchay
			end
			else
			begin
				declare @GiaTriTinhThucChay1 float = @GiaTriOnline
				
				exec [dbo].[prc_asd_ThucChayDaTinhAdmarket_InsertByPhanBoID_ThayDoiHopDong]
					@ngaythuchien,
					@SoHopDong,
					@PhanBo_ID,
					@DmSanPham_ID,
					@TenSanPham,
					@Domain_id,
					@domain_name,
					0,
					0,
					0,
					@GiaTriTinhThucChay1,
					0,
					0,
					0,
					0,
					1,
					'CPC',
					N'Thuc_Chay_Admarket Đổ online tăng gt hợp đồng 2',
					0,
					'',
					@nhanhang_thucchay
			end
			end
		end
		-- giá trị hợp đồng giảm
		else 
		begin
		print 1
		print @GiaTriGanNhatThayDoi
		print @GiaTriTaiThoiDiemTinhThucChay
		    declare @GiaTriBiGiam money =   @GiaTriThucChayPhanBo - @GiaTriTaiThoiDiemTinhThucChay
			if @GiaTriThucChayPhanBo >= @GiaTriTaiThoiDiemTinhThucChay
			exec dbo.prc_asd_TinhGiaTri_ThayDoi_HopDong_Giam_Per 
							@NgayThucHien,
							@PhanBo_ID ,
							@DmSanPham_ID ,
							@TenSanPham ,
							@GiaTriBiGiam
		-- luu lại online
		exec [dbo].[prc_asd_insert_HopDong_CanhBaoThucChay_Admarket]	    @NgayThucHien ,
																			@SoHopDong ,
																			@DmSanPham_ID ,
																			@TenSanPham ,
																			null,
																			null,
																			@GiaTriTaiThoiDiemTinhThucChay,
																			@GiaTriThucChayPhanBo ,
																			@GiaTriBiGiam ,
																			'DOANNV'					
		end
	end

	if @DmSanPham_ID = 585 or @DmSanPham_ID = 144 
	begin
			select @User_id = TK_AdMarketID,@User_Name = TK_AdMarket from HopDongChiTiet where HopDongChiTietID = @PhanBo_ID
			select top 1 @Domain_Name = domain_name  from [dbo].ThucChayAdmarket_ADX_CPC_HopDong_online where contract_number = @SoHopDong and trangthai = 0
			set @Domain_id = dbo.GetWebsiteIDByDomainName(@Domain_Name)
			select @GiaTriOnline = SUM(convert(money,domain_money)) 
			from [dbo].ThucChayAdmarket_ADX_CPC_HopDong_online 
			where contract_number = @SoHopDong 
			and trangthai = 0 
			and DmSanPhamREF = @DmSanPham_ID
			and user_id = @User_id
			set @GiaTriOnline = isnull(@GiaTriOnline,0)
		-- Nếu tăng giá trị
	    if @GiaTriTaiThoiDiemTinhThucChay > @GiaTriGanNhatThayDoi 
		begin
		 if @GiaTriOnline > 0
			begin
		    print N'vào tăng'
			declare @Online1 nvarchar(50) =  convert(nvarchar(50),@GiaTriOnline - @GiaTriTaiThoiDiemTinhThucChay + @GiaTriGanNhatThayDoi)
			-- nhan hang
			declare @nhanhang_thucchay1 nvarchar(500) = (select top 1 DanhSachNhanHangREF from HopDongChiTiet where HopDongChiTietID = @PhanBo_ID)
			
			end
		end
		-- giá trị hợp đồng giảm
		else 
		begin
			declare @GiaTriGiam1 money =   @GiaTriThucChayPhanBo - @GiaTriTaiThoiDiemTinhThucChay
			if @GiaTriThucChayPhanBo >= @GiaTriTaiThoiDiemTinhThucChay
			select 'vao giam'
			select 		@GiaTriGiam1
			--exec dbo.prc_asd_TinhGiaTri_ThayDoi_HopDong_Giam_Per 
			--				@NgayThucHien,
			--				@PhanBo_ID ,
			--				@DmSanPham_ID ,
			--				@TenSanPham ,
			--				@GiaTriGiam1
			-- luu lại online
		    --exec [dbo].[prc_asd_insert_HopDong_CanhBaoThucChay_Admarket]	@NgayThucHien ,
						--													@SoHopDong ,
						--													@DmSanPham_ID ,
						--													@TenSanPham ,
						--													null,
						--													null,
						--													@GiaTriTaiThoiDiemTinhThucChay,
						--													@GiaTriThucChayPhanBo ,
						--													@GiaTriGiam1 ,
						--													'DOANNV'
		end
	end
END

```
