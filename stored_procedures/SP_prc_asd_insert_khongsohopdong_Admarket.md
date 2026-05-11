# Stored Procedure: `prc_asd_insert_khongsohopdong_Admarket`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-11 15:02:51.520000
- **Ngày sửa cuối**: 2017-09-11 15:02:51.563000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
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
CREATE PROCEDURE [dbo].[prc_asd_insert_khongsohopdong_Admarket]
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime,
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

INSERT INTO [dbo].[HopDong_CanhBaoThucChayKhongSoHopDong_Admarket]
           ([NgayThucHien]
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
