# Stored Procedure: `prc_asd_insert_khongsohopdong_Admarket_PhanBo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-02-06 10:59:50.467000
- **Ngày sửa cuối**: 2024-02-28 11:34:08.790000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(1000)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@TenViTri` | `nvarchar(1000)` | No |
| `@TongView` | `int(4)` | No |
| `@TongClick` | `int(4)` | No |
| `@GiaTriThucChay_TraVe` | `money(8)` | No |
| `@Created_By` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_asd_insert_khongsohopdong_Admarket_PhanBo]
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime,
	@HopDongChiTietREF int,
	@DmSanPhamREF int,
	@TenSanPham nvarchar(500),
	@DmViTriREF  int,
	@TenViTri nvarchar(500),
	@TongView int,
	@TongClick int,
	@GiaTriThucChay_TraVe money,
	@Created_By nvarchar(50)

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

INSERT INTO [dbo].[HopDong_CanhBaoThucChayKhongSoHopDong_Admarket_PhanBo]
           ([NgayThucHien]
		   ,HopDongChiTietREF
           ,[DmSanPhamREF]
           ,[TenSanPham]
		   ,DmViTriREF  
		   ,TenViTri 
           ,[TongView]
           ,[TongClick]
           ,[GiaTriThucChay]
           ,[Create_At]
           ,[Created_By])
     VALUES
           (
		    @NgayThucHien ,
			@HopDongChiTietREF,
			@DmSanPhamREF ,
			@TenSanPham ,
			@DmViTriREF  ,
			@TenViTri ,
			@TongView ,
			@TongClick ,
			@GiaTriThucChay_TraVe,
			getdate(),
			@Created_By
		   )
END




```
