# Stored Procedure: `prc_asd_tinhthucchay_admarket_adx_cpc_chitiet_test`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-05-04 18:18:56.690000
- **Ngày sửa cuối**: 2021-05-04 18:30:14.953000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@user_id` | `nvarchar(200)` | No |
| `@username` | `nvarchar(200)` | No |
| `@isnoibo` | `nvarchar(200)` | No |
| `@contract_number` | `nvarchar(200)` | No |
| `@promotion` | `nvarchar(200)` | No |
| `@domain_name` | `nvarchar(200)` | No |
| `@domain_tt_click` | `int(4)` | No |
| `@domain_tt_view` | `int(4)` | No |
| `@domain_money` | `money(8)` | No |
| `@domain_promotion` | `money(8)` | No |
| `@DmSanPhamREF` | `nvarchar(200)` | No |
| `@TenSanPham` | `nvarchar(200)` | No |
| `@DmViTriREF` | `nvarchar(200)` | No |
| `@TenViTri` | `nvarchar(200)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[prc_asd_tinhthucchay_admarket_adx_cpc_chitiet_test]
	-- Add the parameters for the stored procedure here
	@user_id nvarchar(100) ,
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
	@DmViTriREF nvarchar(100) ,
	@TenViTri nvarchar(100) ,
	@NgayThucHien datetime
AS
BEGIN
	SET NOCOUNT ON;
	-- hợp đồng có 1 phân bổ lấy nhãn theo bản nhãn trả về , ng lại lấy nhãn theo phân bổ.
	declare @nhan_thucchay nvarchar(max), @domain_ref int, @row_count int, @row_index int = 1

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

	declare @hopdong_viewplus_nhanhang table
	(
		sohopdong nvarchar(50),
		nhanhang_id nvarchar(100),
		dmsanpham_id int,
		ngaythuchien datetime,
		tk_id nvarchar(100),
		tk_name  nvarchar(100)
	)

	declare @phanbo table
	(
		phanbo_id int,
		hopdong_id int,
		nhan_phanbo nvarchar(max),
		nhan_thucchay nvarchar(max),
		thanhtien_phanbo money,
		tk_id nvarchar(100),
		tk_name  nvarchar(100),
		stt int
	)
	--------------------------------------------------------------------------------------------------
	insert into @hopdong_viewplus_nhanhang 
	select distinct
	contract_number,
	dmnhanhang_id ,
	dmsanphamref,
	ngaythuchien,
	[user_id],
	username
	from [dbo].ThucChayAdmarket_ADX_CPC_NhanHang
	where ngaythuchien = @ngaythuchien
		AND contract_number = @contract_number
		AND DmSanPhamREF = @DmSanPhamREF
	    AND [user_id] = @user_id
		AND dmnhanhang_id <> '0'
	--------------------------------------------------------------------------------------------------
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
	where a.sohopdong = @contract_number 
	and b.DmSanPhamREF = @DmSanPhamREF
	AND b.DmLoaiREF <> 42
	and tk_admarketid = @user_id
	and b.deletedStatus = 0
	-- update nhan thuc chay
	if (select count(1) from @phanbo ) = 1
	begin
	 print 'nhan'
		set @nhan_thucchay = STUFF(( SELECT
                                                              ','
                                                              + CONVERT(NVARCHAR(100), nhanhang_id)
                                                              FROM
                                                              @hopdong_viewplus_nhanhang
                                                              GROUP BY nhanhang_id
                                                              FOR
                                                              XML
                                                              PATH('')
                                                              ), 1, 1, '')
															  
		if isnull(@nhan_thucchay,'') =  ''
			update  @phanbo set nhan_thucchay = nhan_phanbo 
		else
			update  @phanbo set nhan_thucchay = @nhan_thucchay 
	end
	else
	begin
		update @phanbo set nhan_thucchay = nhan_phanbo 
	end
	--------------------------------------------------------------------------------------------------
	select @row_count = count(1) from @phanbo

	-- hop dồng không map đc với san phẩm hoặc tài khoản

	if @row_count = 0  
	begin
	print '@row_count = 0'
	exec [dbo].[prc_asd_insert_ThucChayAdmarket_Error]   @user_id  ,
																			@username  ,
																			@contract_number,
																			@domain_name  ,
																			@domain_tt_click  ,
																			@domain_tt_view  ,
																			@domain_money ,
																			@DmSanPhamREF ,
																			@TenSanPham  ,
																			@DmViTriREF ,
																			@TenViTri ,
																			@NgayThucHien 
	end
	declare @tong_view_thucchay int, 
			@tong_click_thucchay int, 
			@tongtien_thucchay money,
			@phanbo_thucchay int,
			@nhanhang_thucchay nvarchar(200),
			@thanhtien_phanbo money,
			@thanhtien_phanbo_thucchay money,
			@thanhtien_phanbo_tinh_thucchay money
	 
	while @row_index <= @row_count
	begin

	print '@row_index' + convert(nvarchar(50),@row_index)
	 --print '@domain_money = ' + convert(nvarchar(50),@domain_money)
	select 
	@phanbo_thucchay = phanbo_id,
	@nhanhang_thucchay = nhan_thucchay,
	@thanhtien_phanbo = thanhtien_phanbo
	from @phanbo where stt = @row_index

	    if @domain_money >0 
		begin
		 print '@domain_money = ' + convert(nvarchar(50),@domain_money)
			select @thanhtien_phanbo_thucchay = sum(isnull(thanhtiensautrietkhauthucchay,0)) + sum(isnull(GiaTriThayDoi,0))  from thucchaydatinhadmarket where sohopdong = @contract_number and hopdongchitietref = @phanbo_thucchay;
			set @thanhtien_phanbo_thucchay = isnull(@thanhtien_phanbo_thucchay,0);
			 print '@@thanhtien_phanbo_thucchay = ' + convert(nvarchar(50),@thanhtien_phanbo_thucchay)
			-- neu phan bo chua dc do day
			if @thanhtien_phanbo - @thanhtien_phanbo_thucchay > 0
			begin
			
				if @thanhtien_phanbo - @thanhtien_phanbo_thucchay >= @domain_money 
					set @thanhtien_phanbo_tinh_thucchay = @domain_money
				else 
					set @thanhtien_phanbo_tinh_thucchay = @thanhtien_phanbo - @thanhtien_phanbo_thucchay
				--- tinh so luong theo ty le thanh tien
				set @tong_view_thucchay = @thanhtien_phanbo_tinh_thucchay * @domain_tt_view /@domain_money
				set @tong_click_thucchay = @thanhtien_phanbo_tinh_thucchay * @domain_tt_click /@domain_money

				print  '@thanhtien_phanbo_tinh_thucchay = ' + convert(nvarchar(50),@thanhtien_phanbo_tinh_thucchay) 
				-- insert thuc chay admarket
				--exec [dbo].[prc_asd_ThucChayDaTinhAdmarket_InsertByPhanBoID]
				select 
				@ngaythuchien,
				@contract_number,
				@phanbo_thucchay,
				@DmSanPhamREF,
				@TenSanPham,
				@domain_ref,
				@domain_name,
				@tong_view_thucchay,
				@tong_click_thucchay,
				@tong_click_thucchay,
				@thanhtien_phanbo_tinh_thucchay,
				0,
				0,
				0,
				0,
				1,
				'CPC',
				'Thuc_Chay_Admarket',
				@DmViTriREF,
				@tenviTri,
				@nhanhang_thucchay
			end
			set @domain_money = @domain_money - isnull(@thanhtien_phanbo_tinh_thucchay,0);
			set @domain_tt_click = @domain_tt_click - isnull(@tong_click_thucchay,0);
			set @domain_tt_view = @domain_tt_view - isnull(@tong_view_thucchay,0);
		end
		set @row_index += 1;
	end
	
	--------------------------------------------------------------------------------------------------
END


```
