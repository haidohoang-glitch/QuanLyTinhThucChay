# Stored Procedure: `prc_asd_tinhthucchay_admarket_chitiet_PhanBo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-02-06 11:03:29.063000
- **Ngày sửa cuối**: 2024-02-28 11:35:20.447000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@user_id` | `nvarchar(200)` | No |
| `@username` | `nvarchar(200)` | No |
| `@isnoibo` | `nvarchar(200)` | No |
| `@contract_number` | `nvarchar(200)` | No |
| `@promotion` | `float(8)` | No |
| `@domain_name` | `nvarchar(200)` | No |
| `@domain_tt_click` | `int(4)` | No |
| `@domain_tt_view` | `int(4)` | No |
| `@domain_money` | `float(8)` | No |
| `@domain_promotion` | `float(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(200)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@TenViTri` | `nvarchar(200)` | No |
| `@DonViTinh` | `nvarchar(40)` | No |
| `@NhanHang` | `nvarchar(200)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@GhiChu` | `nvarchar(2000)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[prc_asd_tinhthucchay_admarket_chitiet_PhanBo]
	-- Add the parameters for the stored procedure here
	@user_id nvarchar(100) ,
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
	@DonViTinh nvarchar(20),
	@NhanHang nvarchar(100),
	@NgayThucHien datetime,
	@GhiChu		nvarchar(1000)
AS
BEGIN
	SET NOCOUNT ON;
	-- hợp đồng có 1 phân bổ lấy nhãn theo bản nhãn trả về , ng lại lấy nhãn theo phân bổ.
	--HAIDH COMMENT 06/10/2022 neu nhanphanbo = 0 or '' thi lay nhanthucchay
	declare @nhan_thucchay nvarchar(max), @domain_ref int, @row_count int, @row_index int = 1
		, @nhan_phanbo nvarchar(200), @v_GhiChu NVARCHAR(2000)
	declare @tong_view_thucchay int, 
			@tong_click_thucchay int, 
			@phanbo_thucchay int,
			@nhanhang_thucchay nvarchar(200),
			@thanhtien_phanbo money,
			@thanhtien_phanbo_thucchay money,
			@thanhtien_phanbo_tinh_thucchay money

	
	set @tong_view_thucchay = @domain_tt_view
	set @tong_click_thucchay = @domain_tt_click

	select top 1
	@phanbo_thucchay = hdct.HopDongChiTietID,
	@thanhtien_phanbo = hdct.ThanhTien
	from HopDongChitiet hdct where hdct.HopDongChiTietID = @HopDongChiTietREF
	and hdct.dmsanphamref = @DmSanPhamREF

	set @nhanhang_thucchay = isnull(@NhanHang,'')

	SET @v_GhiChu = N'Thuc_Chay_Admarket_PhanBo' + @GhiChu

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


	if @domain_money >0 
	begin
		select @thanhtien_phanbo_thucchay = sum(isnull(thanhtiensautrietkhauthucchay,0)) + sum(isnull(GiaTriThayDoi,0))  
		from thucchaydatinhadmarket where sohopdong = @contract_number and hopdongchitietref = @phanbo_thucchay;
		set @thanhtien_phanbo_thucchay = isnull(@thanhtien_phanbo_thucchay,0);
		-- neu phan bo chua dc do day
		if @thanhtien_phanbo - @thanhtien_phanbo_thucchay > 0
		begin
			if @thanhtien_phanbo - @thanhtien_phanbo_thucchay >= @domain_money set @thanhtien_phanbo_tinh_thucchay = @domain_money
			else set @thanhtien_phanbo_tinh_thucchay = @thanhtien_phanbo - @thanhtien_phanbo_thucchay
			--- tinh so luong theo ty le thanh tien
			set @tong_view_thucchay = @thanhtien_phanbo_tinh_thucchay * @domain_tt_view /@domain_money
			set @tong_click_thucchay = @thanhtien_phanbo_tinh_thucchay * @domain_tt_click /@domain_money
			-- insert thuc chay admarket

			exec [dbo].[prc_asd_ThucChayDaTinhAdmarket_InsertTCDT_PhanBo]
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
			@DonViTinh,
			@v_GhiChu,
			@DmViTriREF,
			@tenviTri,
			@nhanhang_thucchay

		end
		set @domain_money = @domain_money - isnull(@thanhtien_phanbo_tinh_thucchay,0);
		set @domain_tt_click = @domain_tt_click - isnull(@tong_click_thucchay,0);
		set @domain_tt_view = @domain_tt_view - isnull(@tong_view_thucchay,0);
	end

	
	--------------------------------------------------------------------------------------------------
END


```
