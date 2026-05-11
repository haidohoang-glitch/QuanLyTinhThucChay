# Stored Procedure: `ThucChayAdmarketUser_NhanHang_Insert_bk20160926`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-09-26 15:51:12.243000
- **Ngày sửa cuối**: 2016-09-26 15:51:12.243000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@domain` | `nvarchar(100)` | No |
| `@ttc` | `int(4)` | No |
| `@ttv` | `int(4)` | No |
| `@money` | `float(8)` | No |
| `@pro` | `float(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@IsNoiBo` | `int(4)` | No |
| `@username` | `nvarchar(100)` | No |
| `@userid` | `int(4)` | No |
| `@DmNhanHangREF` | `int(4)` | No |
| `@TenNhanHang` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: 2014-06-02
-- Description:	Insert ThucChayAdmarketUsers
-- =============================================



CREATE PROCEDURE [dbo].[ThucChayAdmarketUser_NhanHang_Insert_bk20160926] 
	-- Add the parameters for the stored procedure here
	@DmSanPhamREF	INT,
	@TenSanPham		NVARCHAR(50),
	@domain	NVARCHAR(50),
	@ttc	INT,
	@ttv	INT,
	@money	FLOAT,
	@pro	FLOAT,
	@NgayThucHien	DATETIME,
	@IsNoiBo int,
	@username NVARCHAR(50),
	@userid INT,
	@DmNhanHangREF INT ,
	@TenNhanHang NVARCHAR(200)

AS
BEGIN
	INSERT INTO [dbo].ThucChayAdmarketUser_NhanHang
           ([DmSanPhamREF]
           ,[username]
           ,[TenSanPham]
           ,[Domain]
           ,[ttc]
           ,[ttv]
           ,[money]
           ,[pro]
           ,[IsNoiBo]
           ,[NgayThucHien]
           ,[CreatedAt]
           ,[CreatedBy]
           ,[LastModifedAt]
           ,[LastModifiedBy]
           ,userid
           ,DmNhanHangREF
           ,TenNhanHang
           )
     VALUES
           (
				@DmSanPhamREF
				,@username
				,@TenSanPham
				,@domain
				,@ttc
				,@ttv
				,@money
				,@pro
				,@IsNoiBo
				,@NgayThucHien
				,GETDATE()
				,'asd'
				,GETDATE()
				,'asd'	
				,@userid
				,@DmNhanHangREF
				,@TenNhanHang
           )
END

```
