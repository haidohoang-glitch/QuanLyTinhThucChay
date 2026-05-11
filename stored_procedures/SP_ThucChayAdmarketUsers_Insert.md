# Stored Procedure: `ThucChayAdmarketUsers_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-02 17:15:33.173000
- **Ngày sửa cuối**: 2014-11-19 12:16:54.687000

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

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ	
-- Create date: 2014-06-02
-- Description:	Insert ThucChayAdmarketUsers
-- =============================================



CREATE PROCEDURE [dbo].[ThucChayAdmarketUsers_Insert] 
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
	@userid int

AS
BEGIN
	INSERT INTO [dbo].[ThucChayAdmarketUsers]
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
           )
END

```
