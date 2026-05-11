# Stored Procedure: `ThucChayAdmarketTotalInsertOrUpdate`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 00:41:46.647000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.477000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@TongClick` | `bigint(8)` | No |
| `@TongView` | `bigint(8)` | No |
| `@TongTienThucChay` | `float(8)` | No |
| `@TongTienKhuyenMai` | `float(8)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DataType` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-01-24
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayAdmarketTotalInsertOrUpdate] 
(
	@NgayThucHien		DateTime,
	@DmSanPhamREF		int,
	@TenSanPham			nvarchar(50),
	@TongClick			bigint,
	@TongView			bigint,
	@TongTienThucChay	float,
	@TongTienKhuyenMai	float,
	@GhiChu				nvarchar(200),
	@CreatedBy			nvarchar(50),
	@CreatedAt			datetime,
	@LastModifiedBy		nvarchar(50),
	@LastModifiedAt		datetime,
	@DataType			int
)
	
AS
BEGIN
	IF EXISTS(SELECT * FROM ThucChayAdmarketTotal A WHERE A.NgayThucHien = @NgayThucHien AND A.DmSanPhamREF = @DmSanPhamREF)
		UPDATE [dbo].[ThucChayAdmarketTotal]
		   SET 
			  [NgayThucHien]		= @NgayThucHien
			  ,[DmSanPhamREF]		= @DmSanPhamREF
			  ,[TenSanPham]			= @TenSanPham
			  ,[TongClick]			= @TongClick
			  ,[TongView]			= @TongView
			  ,[TongTienThucChay]	= @TongTienThucChay
			  ,[TongTienKhuyenMai]	= @TongTienKhuyenMai
			  ,[GhiChu]				= @GhiChu
			  ,[DaTaType]			= @DataType
			  ,[LastModifiedBy]		= @LastModifiedBy
			  ,[LastModifiedAt]		= @LastModifiedAt
		 WHERE NgayThucHien = @NgayThucHien 
			AND DmSanPhamREF = @DmSanPhamREF
	ELSE
		INSERT INTO [dbo].[ThucChayAdmarketTotal]
			   (
			   [NgayThucHien]
			   ,[DmSanPhamREF]
			   ,[TenSanPham]
			   ,[TongClick]
			   ,[TongView]
			   ,[TongTienThucChay]
			   ,[TongTienKhuyenMai]
			   ,[GhiChu]
			   ,[DaTaType]
			   ,[CreatedBy]
			   ,[CreatedAt]
			   ,[LastModifiedBy]
			   ,[LastModifiedAt])
		 VALUES
			   (@NgayThucHien,
				@DmSanPhamREF,
				@TenSanPham,
				@TongClick,
				@TongView,
				@TongTienThucChay,
				@TongTienKhuyenMai,
				@GhiChu,
				@DataType,
				@CreatedBy,
				@CreatedAt,
				@LastModifiedBy,
				@LastModifiedAt)
END

```
