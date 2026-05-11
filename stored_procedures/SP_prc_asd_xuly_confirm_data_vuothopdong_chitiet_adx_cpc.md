# Stored Procedure: `prc_asd_xuly_confirm_data_vuothopdong_chitiet_adx_cpc`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-11 15:02:54.263000
- **Ngày sửa cuối**: 2017-09-11 15:02:54.330000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@SoHopDong_change` | `nvarchar(100)` | No |
| `@user_id` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(1000)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@TenViTri` | `nvarchar(1000)` | No |
| `@domain_name` | `nvarchar(1000)` | No |
| `@domain_money` | `money(8)` | No |
| `@domain_tt_click` | `int(4)` | No |
| `@domain_tt_view` | `int(4)` | No |
| `@confirm_money` | `money(8)` | No |
| `@data_type` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		DOANNV
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_asd_xuly_confirm_data_vuothopdong_chitiet_adx_cpc] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime,
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
	@data_type int 
	
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	declare @domain_ref int
	set @domain_ref = dbo.GetWebsiteIDByDomainName(@domain_name)
	----------------------------------------------------------------------------------------------

	declare @phanbo table
	(
		phanbo_id	int,
		hopdong_id	int,
		nhan_phanbo nvarchar(100),
		nhan_thucchay nvarchar(100),
		thanhtien_phanbo money,
		tk_id nvarchar(100),
		tk_name  nvarchar(100),
		stt int
	)

	declare @phanbo_change table
	(
		phanbo_id int,
		hopdong_id int,
		nhan_phanbo nvarchar(100),
		nhan_thucchay nvarchar(100),
		thanhtien_phanbo money,
		tk_id nvarchar(100),
		tk_name  nvarchar(100),
		stt int
	)
	----------------------------------------------------------------------------------------------

	
	insert into @phanbo
	select 
	b.hopdongchitietid,
	a.hopdongid,
	b.DanhSachNhanHangREF,
	'',
	b.thanhtien,
	tk_admarketid,
	tk_admarket,
	row_number() over(order by b.hopdongchitietid)
	from hopdong a inner join hopdongchitiet b on a.hopdongid = b.hopdongfk
	where a.sohopdong = @SoHopDong 
	and b.DmSanPhamREF = @DmSanPhamREF
	and b.tk_admarketid = @user_id

	-------------------------------------

	insert into @phanbo_change
	select 
	b.hopdongchitietid,
	a.hopdongid,
	b.DanhSachNhanHangREF,
	b.DanhSachNhanHangREF,
	b.thanhtien,
	tk_admarketid,
	tk_admarket,
	row_number() over(order by b.hopdongchitietid)
	from hopdong a inner join hopdongchitiet b on a.hopdongid = b.hopdongfk
	where a.sohopdong = @SoHopDong_change 
	and b.DmSanPhamREF = @DmSanPhamREF
	and b.tk_admarketid = @user_id
	---
	declare @nhan_thucchay nvarchar(500),@phanbo_thucchay int,@nhanhang_thucchay nvarchar(200),@ThanhTien_PhanBo money,@ThanhTienThucChay_PhanBo money,
	@GiaTri_TinhThucChay money, @SoLuong_Click_Tinh int, @SoLuongView_Tinh int,@Row_Index int = 1, @Row_count int
	set @nhan_thucchay = STUFF(( SELECT
                                                              ','
                                                              + CONVERT(NVARCHAR(100), a.dmnhanhang_id)
                                                              FROM
                                                              (
																select distinct

																dmnhanhang_id
															
																from [dbo].[ThucChayAdmarket_ViewPlus_NhanHang] 
																where ngaythuchien = @ngaythuchien
																	AND contract_number = @SoHopDong
																	AND DmSanPhamREF = @DmSanPhamREF
																	AND [user_id] = @user_id
															  ) a
                                                              GROUP BY a.dmnhanhang_id
                                                              FOR
                                                              XML
                                                              PATH('')
                                                              ), 1, 1, '')
    update @phanbo set nhan_thucchay = case when isnull(@nhan_thucchay,'') <> '' then @nhan_thucchay else nhan_phanbo end
	-----------------------------------------data_type = 4-----------------------------------------------------
	if @data_type =  4
	begin
	----------------------------
		declare @GiaTriChuyenSangHopDongKhac money, @TongGiaTriTraVe money,
				@SoLuong_Click_ChuyenSang int,@SoLuong_View_ChuyenSang int,
				@GiaTriTinhChoHopDong_Cu money, @SoLuong_Click_Cu int, @SoLuong_View_Cu int
				
				
				
	----------------------------
	set            @GiaTriTinhChoHopDong_Cu = @domain_money - @confirm_money;
	set			   @SoLuong_Click_Cu = (@domain_money - @confirm_money)/@domain_money  * @domain_tt_click;
	set			   @SoLuong_View_Cu = (@domain_money - @confirm_money)/@domain_money  * @domain_tt_view;
	

	set            @GiaTriChuyenSangHopDongKhac = @confirm_money;
	set			   @SoLuong_Click_Cu = @confirm_money/@domain_money  * @domain_tt_click;
	set			   @SoLuong_View_Cu = @confirm_money/@domain_money  * @domain_tt_view;
	
	----------------------------

	

	select @Row_count = count(1) from @phanbo

	while @Row_Index <= @Row_count
		begin
		select 
		@phanbo_thucchay = phanbo_id,
		@nhanhang_thucchay = nhan_phanbo,
		@thanhtien_phanbo = thanhtien_phanbo
		from @phanbo where stt = @Row_Index
		if @GiaTriTinhChoHopDong_Cu > 0
			begin
				select @ThanhTienThucChay_PhanBo = sum(isnull(thanhtiensautrietkhauthucchay,0))  from thucchaydatinhadmarket where sohopdong = @sohopdong and hopdongchitietref = @phanbo_thucchay;
			if @thanhtien_phanbo > @ThanhTienThucChay_PhanBo
				begin
					if @thanhtien_phanbo - @ThanhTienThucChay_PhanBo >= @GiaTriTinhChoHopDong_Cu set @GiaTri_TinhThucChay = @GiaTriTinhChoHopDong_Cu
					else set @GiaTri_TinhThucChay = @thanhtien_phanbo - @ThanhTienThucChay_PhanBo
					--- tinh so luong theo ty le thanh tien
					set @SoLuongView_Tinh = @GiaTri_TinhThucChay * @SoLuong_View_Cu /@GiaTriTinhChoHopDong_Cu
					set @SoLuong_Click_Tinh = @GiaTri_TinhThucChay * @SoLuong_Click_Cu /@GiaTriTinhChoHopDong_Cu
				exec [dbo].[prc_asd_ThucChayDaTinhAdmarket_InsertByPhanBoID]
													@ngaythuchien,
													@SoHopDong,
													@phanbo_thucchay,
													@DmSanPhamREF,
													@TenSanPham,
													@domain_ref,
													@domain_name,
													@SoLuongView_Tinh,
													@SoLuong_Click_Tinh,
													@SoLuong_Click_Tinh,
													@GiaTri_TinhThucChay,
													0,
													0,
													0,
													0,
													1,
													2,
													'Thuc_Chay_Admarket data_type = 4',
													@DmViTriREF,
													@TenviTri,
													@nhanhang_thucchay

			end
			set @GiaTriTinhChoHopDong_Cu = @GiaTriTinhChoHopDong_Cu - isnull(@GiaTri_TinhThucChay,0);
			set @SoLuong_View_Cu = @SoLuong_View_Cu - isnull(@SoLuongView_Tinh,0);
			set @SoLuong_Click_Cu = @SoLuong_Click_Cu - isnull(@SoLuong_Click_Tinh,0);
		end
		set @Row_Index +=1;
		
	end
	
	set @Row_Index = 1;
	select @Row_count = count(1) from @phanbo_change;

	while @Row_Index <= @Row_count
	begin
		select 
		@phanbo_thucchay = phanbo_id,
		@nhanhang_thucchay = nhan_phanbo,
		@thanhtien_phanbo = thanhtien_phanbo
		from @phanbo_change where stt = @Row_Index
		if @GiaTriChuyenSangHopDongKhac > 0
			begin
				select @ThanhTienThucChay_PhanBo = sum(isnull(thanhtiensautrietkhauthucchay,0))  from thucchaydatinhadmarket where sohopdong = @SoHopDong_change and hopdongchitietref = @phanbo_thucchay;
			if @thanhtien_phanbo > @ThanhTienThucChay_PhanBo
				begin
					if @thanhtien_phanbo - @ThanhTienThucChay_PhanBo >= @GiaTriChuyenSangHopDongKhac set @GiaTri_TinhThucChay = @GiaTriChuyenSangHopDongKhac
					else set @GiaTri_TinhThucChay = @thanhtien_phanbo - @ThanhTienThucChay_PhanBo
					--- tinh so luong theo ty le thanh tien
					set @SoLuongView_Tinh = @GiaTri_TinhThucChay * @SoLuong_View_ChuyenSang /@GiaTriChuyenSangHopDongKhac
					set @SoLuong_Click_Tinh = @GiaTri_TinhThucChay * @SoLuong_Click_ChuyenSang /@GiaTriChuyenSangHopDongKhac
				exec [dbo].[prc_asd_ThucChayDaTinhAdmarket_InsertByPhanBoID]
													@ngaythuchien,
													@SoHopDong_change,
													@phanbo_thucchay,
													@DmSanPhamREF,
													@TenSanPham,
													@domain_ref,
													@domain_name,
													@SoLuongView_Tinh,
													@SoLuong_Click_Tinh,
													@SoLuong_Click_Tinh,
													@GiaTri_TinhThucChay,
													0,
													0,
													0,
													0,
													1,
													2,
													'Thuc_Chay_Admarket data_type = 4',
													@DmViTriREF,
													@TenviTri,
													@nhanhang_thucchay

			end
		set @GiaTriChuyenSangHopDongKhac = @GiaTriChuyenSangHopDongKhac - isnull(@GiaTri_TinhThucChay,0);
		set @SoLuong_View_ChuyenSang = @SoLuong_View_ChuyenSang - isnull(@SoLuongView_Tinh,0);
		set @SoLuong_Click_ChuyenSang = @SoLuong_Click_ChuyenSang - isnull(@SoLuong_Click_Tinh,0);
		end

		set @Row_Index +=1;
	end 
	end
	---------------------------------------------------KetThuc data_type = 4-------------------------------------------
	---------------------------------------------------bat dau data_type = 2,3-------------------------------------------
	declare @ghichu nvarchar(200), @gitritinh_dodoitru money
	 
	if @data_type in (2,3)
	begin
	if @data_type = 2 set @ghichu = 'Doi tru data_type = 2'
	else set @ghichu = 'Doi tru data_type = 3'

	set @gitritinh_dodoitru = @confirm_money - @domain_money
	-- ghi am het toan bo du lieu da tinh thuc chay
	exec [dbo].[prc_asd_insert_thucchaydatinh_admarket_giatrithaydoi]  @SoHopDong,@ngaythuchien,@dmsanphamref,'Doi tru data_type = 2'
	
	-- tinh thuc chay gia tri moi (ngay thuc hien). gia tri confirm da bao gom gia tri ngay hien tai tinh thuc chay
	while @Row_Index <= @Row_count
		begin
		select 
		@phanbo_thucchay = phanbo_id,
		@nhanhang_thucchay = nhan_thucchay,
		@thanhtien_phanbo = thanhtien_phanbo
		from @phanbo where stt = @Row_Index
		if @domain_money > 0
			begin
				select @ThanhTienThucChay_PhanBo = sum(isnull(thanhtiensautrietkhauthucchay,0))  from thucchaydatinhadmarket where sohopdong = @sohopdong and hopdongchitietref = @phanbo_thucchay;
			if @thanhtien_phanbo > @ThanhTienThucChay_PhanBo
				begin
					if @thanhtien_phanbo - @ThanhTienThucChay_PhanBo >= @domain_money set @GiaTri_TinhThucChay = @domain_money
					else set @GiaTri_TinhThucChay = @thanhtien_phanbo - @ThanhTienThucChay_PhanBo
					--- tinh so luong theo ty le thanh tien
					set @SoLuongView_Tinh = @GiaTri_TinhThucChay * @domain_tt_view /@domain_money
					set @SoLuong_Click_Tinh = @GiaTri_TinhThucChay * @domain_tt_click /@domain_money
				exec [dbo].[prc_asd_ThucChayDaTinhAdmarket_InsertByPhanBoID]
													@ngaythuchien,
													@SoHopDong,
													@phanbo_thucchay,
													@DmSanPhamREF,
													@TenSanPham,
													@domain_ref,
													@domain_name,
													@SoLuongView_Tinh,
													@SoLuong_Click_Tinh,
													@SoLuong_Click_Tinh,
													@GiaTri_TinhThucChay,
													0,
													0,
													0,
													0,
													1,
													2,
													'Thuc_Chay_Admarket data_type in (2,3) ghi duong gia tri moi',
													@DmViTriREF,
													@TenviTri,
													@nhanhang_thucchay

			end
			set @domain_money = @domain_money - isnull(@GiaTri_TinhThucChay,0);
			set @domain_tt_view = @domain_tt_view - isnull(@SoLuongView_Tinh,0);
			set @domain_tt_click = @domain_tt_click - isnull(@SoLuong_Click_Tinh,0);
		end
		set @Row_Index +=1;
		
	end
	-- tinh thuc chay do bi doi tru di hoan toan
	while @Row_Index <= @Row_count
		begin
		select 
		@phanbo_thucchay = phanbo_id,
		@nhanhang_thucchay = nhan_phanbo,
		@thanhtien_phanbo = thanhtien_phanbo
		from @phanbo where stt = @Row_Index
		if @gitritinh_dodoitru > 0
			begin
				select @ThanhTienThucChay_PhanBo = sum(isnull(thanhtiensautrietkhauthucchay,0))  from thucchaydatinhadmarket where sohopdong = @sohopdong and hopdongchitietref = @phanbo_thucchay;
			if @thanhtien_phanbo > @ThanhTienThucChay_PhanBo
				begin
					if @thanhtien_phanbo - @ThanhTienThucChay_PhanBo >= @gitritinh_dodoitru set @GiaTri_TinhThucChay = @gitritinh_dodoitru
					else set @GiaTri_TinhThucChay = @thanhtien_phanbo - @ThanhTienThucChay_PhanBo
					--- tinh so luong theo ty le thanh tien
					set @SoLuongView_Tinh = 1
					set @SoLuong_Click_Tinh = 1
				exec [dbo].[prc_asd_ThucChayDaTinhAdmarket_InsertByPhanBoID]
													@ngaythuchien,
													@SoHopDong,
													@phanbo_thucchay,
													@DmSanPhamREF,
													@TenSanPham,
													826,
													'(Blanks)',
													@SoLuongView_Tinh,
													@SoLuong_Click_Tinh,
													@SoLuong_Click_Tinh,
													@GiaTri_TinhThucChay,
													0,
													0,
													0,
													0,
													1,
													2,
													'Thuc_Chay_Admarket data_type in (2,3) ghi duong gia tri cu',
													@DmViTriREF,
													@TenviTri,
													@nhanhang_thucchay

			end
			set @gitritinh_dodoitru = @gitritinh_dodoitru - isnull(@GiaTri_TinhThucChay,0);
		end
		set @Row_Index +=1;
		
	end


	end
	---------------------------------------------------KetThuc data_type = 2,3-------------------------------------------

END


```
