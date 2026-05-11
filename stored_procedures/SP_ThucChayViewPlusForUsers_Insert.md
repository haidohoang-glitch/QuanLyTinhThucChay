# Stored Procedure: `ThucChayViewPlusForUsers_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-05-13 18:13:43.490000
- **Ngày sửa cuối**: 2015-06-25 17:26:48.283000

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

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[ThucChayViewPlusForUsers_Insert] 
	-- Add the parameters for the stored procedure here
    @DmSanPhamREF INT ,
    @TenSanPham NVARCHAR(50) ,
    @domain NVARCHAR(50) ,
    @ttc INT ,
    @ttv INT ,
    @money FLOAT ,
    @pro FLOAT ,
    @NgayThucHien DATETIME ,
    @IsNoiBo INT ,
    @username NVARCHAR(50) ,
    @userid INT ,
    @DonViTinh NVARCHAR(50)
AS 
    BEGIN
		
		SET @DonViTinh = 'CPC';--chưa xác định
		-- delete dữ liêu đã có 
		--DELETE FROM [dbo].[ThucChayViewPlusForUsers]
		--WHERE username = @username AND userid = @userid AND CONVERT(DATE,NgayThucHien) = @NgayThucHien
		--AND DmSanPhamREF = @DmSanPhamREF AND DonViTinh = @DonViTinh
        INSERT  INTO [dbo].[ThucChayViewPlusForUsers]
                ( [DmSanPhamREF] ,
                  [username] ,
                  [TenSanPham] ,
                  [Domain] ,
                  [ttc] ,
                  [ttv] ,
                  [money] ,
                  [pro] ,
                  [IsNoiBo] ,
                  [NgayThucHien] ,
                  [CreatedAt] ,
                  [CreatedBy] ,
                  [LastModifedAt] ,
                  [LastModifiedBy] ,
                  userid ,
                  DonViTinh 
                )
        VALUES  ( @DmSanPhamREF ,
                  @username ,
                  @TenSanPham ,
                  @domain ,
                  @ttc ,
                  @ttv ,
                  @money ,
                  @pro ,
                  @IsNoiBo ,
                  @NgayThucHien ,
                  GETDATE() ,
                  'asd' ,
                  GETDATE() ,
                  'asd' ,
                  @userid ,
                  @DonViTinh
                )
    END


```
