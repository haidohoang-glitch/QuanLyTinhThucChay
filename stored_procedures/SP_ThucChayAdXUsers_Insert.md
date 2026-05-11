# Stored Procedure: `ThucChayAdXUsers_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:54:00.440000
- **Ngày sửa cuối**: 2015-02-04 18:45:57.230000

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
| `@DonViTinh` | `nvarchar(100)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@TenViTri` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ	
-- Create date: 2014-06-02
-- Description:	Insert ThucChayAdXUsers
-- =============================================



CREATE PROCEDURE [dbo].[ThucChayAdXUsers_Insert] 
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
	@userid int,
	@DonViTinh nvarchar(50),
	@DmViTriREF INT,
	@TenViTri NVARCHAR(50)
AS
BEGIN
	INSERT INTO [dbo].[ThucChayAdXUsers]
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
           ,DonViTinh 
           ,DmViTriREF
           ,TenViTri
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
				,@DonViTinh
				,@DmViTriREF
				,@TenViTri				
           )
END



```
