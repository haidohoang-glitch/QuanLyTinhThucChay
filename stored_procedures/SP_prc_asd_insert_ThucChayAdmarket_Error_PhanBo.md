# Stored Procedure: `prc_asd_insert_ThucChayAdmarket_Error_PhanBo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-02-06 11:00:14.567000
- **Ngày sửa cuối**: 2024-02-28 11:34:18.937000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@user_id` | `nvarchar(200)` | No |
| `@user_name` | `nvarchar(200)` | No |
| `@contract_number` | `nvarchar(200)` | No |
| `@domain_name` | `nvarchar(200)` | No |
| `@domain_tt_click` | `int(4)` | No |
| `@domain_tt_view` | `int(4)` | No |
| `@domain_money` | `money(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@dm_sanpham_ref` | `int(4)` | No |
| `@ten_san_pham` | `nvarchar(1000)` | No |
| `@dm_vitri_ref` | `int(4)` | No |
| `@ten_vi_tri` | `nvarchar(1000)` | No |
| `@ngaythuchien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_asd_insert_ThucChayAdmarket_Error_PhanBo]
	-- Add the parameters for the stored procedure here
	@user_id nvarchar(100) ,
	@user_name nvarchar(100) ,
	@contract_number nvarchar(100) ,
	@domain_name nvarchar(100) ,
	@domain_tt_click int ,
	@domain_tt_view int ,
	@domain_money money ,
	@HopDongChiTietREF int,
	@dm_sanpham_ref int ,
	@ten_san_pham nvarchar(500) ,
	@dm_vitri_ref int ,
	@ten_vi_tri nvarchar(500) ,
	@ngaythuchien datetime 



AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	INSERT INTO [dbo].[ThucChayAdmarket_Error_PhanBo]
           ([user_id]
           ,[user_name]
           ,[contract_number]
           ,[domain_name]
           ,[domain_tt_click]
           ,[domain_tt_view]
           ,[domain_money]
		   ,HopDongChiTietREF
           ,[dm_sanpham_ref]
           ,[ten_san_pham]
           ,[dm_vitri_ref]
           ,[ten_vi_tri]
           ,[ngaythuchien])
     VALUES
           (
		    @user_id ,
			@user_name,
			@contract_number,
			@domain_name,
			@domain_tt_click,
			@domain_tt_view ,
			@domain_money,
			@HopDongChiTietREF,
			@dm_sanpham_ref,
			@ten_san_pham ,
			@dm_vitri_ref ,
			@ten_vi_tri ,
			@ngaythuchien  
		   )
END


```
