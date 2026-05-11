# Stored Procedure: `prc_insert_ThucChayAdmarket_HopDong_online_PhanBo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-02-06 11:05:11.817000
- **Ngày sửa cuối**: 2024-02-28 11:35:53.700000

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
| `@campaign_id` | `nvarchar(200)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(200)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@TenViTri` | `nvarchar(200)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@NhanHang` | `nvarchar(200)` | No |
| `@data_type` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_insert_ThucChayAdmarket_HopDong_online_PhanBo]
	-- Add the parameters for the stored procedure here
	@user_id nvarchar(100) ,
	@username nvarchar(100) ,
	@isnoibo nvarchar(100) ,
	@contract_number nvarchar(100) ,
	@promotion float ,
	@domain_name nvarchar(100) ,
	@domain_tt_click int ,
	@domain_tt_view int ,
	@domain_money float ,
	@domain_promotion float ,
	@campaign_id nvarchar(100) ,
	@HopDongChiTietREF int,
	@DmSanPhamREF int ,
	@TenSanPham nvarchar(100) ,
	@DmViTriREF int ,
	@TenViTri nvarchar(100) ,
	@NgayThucHien datetime ,
	@DonViTinh nvarchar(50),
	@NhanHang nvarchar(100),
	@data_type int 
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	declare @giatrihopdong money, @domain_ref int = 0

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

	select @giatrihopdong = sum (a.thanhtien)
	from hopdongchitiet a inner join hopdong b on a.hopdongfk = b.hopdongid
	where a.deletedstatus = 0 
	and b.sohopdong = @contract_number
	and a.dmsanphamref = @DmSanPhamREF
	and a.tk_admarketid = @user_id

	-- 0. Cap nhap trang thai confirm_status = -1 ban ghi truoc do neu bi trung
	UPDATE [dbo].[ThucChayAdmarket_HopDong_online]
	SET confirm_status = -1
	WHERE [user_id] = @user_id 
	AND [isnoibo] = @isnoibo
	AND [contract_number] = @contract_number
	AND [HopDongChiTietREF] = @HopDongChiTietREF
	AND [DmSanPhamREF] = @DmSanPhamREF
	AND [domain_name] = @domain_name 
	AND DmViTriREF = @DmViTriREF
	AND [NgayThucHien] = @NgayThucHien

    -- 1. Insert dl cảnh báo phanbo <> 0 nhung bị ghi nhan vao online
	INSERT INTO [dbo].[ThucChayAdmarket_HopDong_online]
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
		   ,[HopDongChiTietREF]
           ,[DmSanPhamREF]
           ,[TenSanPham]
		   ,DmViTriREF
		   ,TenViTri
           ,[NgayThucHien]
           ,[createdBy]
           ,[createdAt]
           ,[contract_number_change]
           ,[data_type]
           ,[confirm_money]
		   ,giatrihopdong
           ,[trangthai]
		   ,confirm_date
		   ,confirm_status
		   ,NhanHang)
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
		@domain_money, --tien thua do vao online
		@domain_promotion ,
		@campaign_id  ,
		@HopDongChiTietREF,
		@DmSanPhamREF  ,
		@TenSanPham ,
		@DmViTriREF  ,
		@TenViTri ,
		@NgayThucHien  ,
		'asd',
		getdate(),
		'', --[contract_number_change],
		@data_type  ,
		@giatrihopdong,
		0,
		0, -- trang thai 0: chua xu ly, 1: da xu ly
		null,--ngay confirm
		0,-- trang thai confirm, -1 Huy ban ghi
		@NhanHang
	 )

	
END


```
