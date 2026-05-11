# Stored Procedure: `usp_UpdateThucChayAdmarket`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-20 13:09:49.670000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.593000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayAdmarketID` | `int(4)` | No |
| `@User_ID` | `int(4)` | No |
| `@UserName` | `nvarchar(100)` | No |
| `@FullName` | `nvarchar(100)` | No |
| `@Email` | `nvarchar(100)` | No |
| `@Phone` | `nvarchar(100)` | No |
| `@GroupID` | `int(4)` | No |
| `@GroupName` | `nvarchar(100)` | No |
| `@TTC` | `int(4)` | No |
| `@TTV` | `int(4)` | No |
| `@Money` | `float(8)` | No |
| `@Promotion` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_UpdateThucChayAdmarket]
(
    @ThucChayAdmarketID  INT,
    @User_ID             INT,
    @UserName            NVARCHAR(50),
    @FullName            NVARCHAR(50),
    @Email               NVARCHAR(50),
    @Phone               NVARCHAR(50),
    @GroupID             INT,
    @GroupName           NVARCHAR(50),
    @TTC                 INT,
    @TTV                 INT,
    @Money               FLOAT,
    @Promotion           NVARCHAR(50),
    @DmSanPhamREF        INT,
    @TenSanPham          NVARCHAR(50)
)
AS
BEGIN
	SET NOCOUNT ON
	
	UPDATE [dbo].[ThucChayAdmarket]
	SET    [User_ID]             = @User_ID,
	       [UserName]            = @UserName,
	       [FullName]            = @FullName,
	       [Email]               = @Email,
	       [Phone]               = @Phone,
	       [GroupID]             = @GroupID,
	       [GroupName]           = @GroupName,
	       [TTC]                 = @TTC,
	       [TTV]                 = @TTV,
	       [Money]               = @Money,
	       [Promotion]           = @Promotion,
	       [DmSanPhamREF]        = @DmSanPhamREF,
	       [TenSanPham]          = @TenSanPham
	WHERE  [ThucChayAdmarketID]  = @ThucChayAdmarketID
END

```
