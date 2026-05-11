# Stored Procedure: `usp_InsertThucChayAdmarket`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-20 13:09:49.823000
- **Ngày sửa cuối**: 2014-11-19 12:16:46.517000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@UserID` | `int(4)` | No |
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
| `@CreateDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_InsertThucChayAdmarket]
(
    @UserID        INT,
    @UserName      NVARCHAR(50),
    @FullName      NVARCHAR(50),
    @Email         NVARCHAR(50),
    @Phone         NVARCHAR(50),
    @GroupID       INT,
    @GroupName     NVARCHAR(50),
    @TTC           INT,
    @TTV           INT,
    @Money         FLOAT,
    @Promotion     NVARCHAR(50),
    @DmSanPhamREF  INT,
    @TenSanPham    NVARCHAR(50),
    @CreateDate    DATETIME
)
AS
BEGIN
	SET NOCOUNT ON
	DECLARE @ThucChayAdmarketIDParma INT
	SET @ThucChayAdmarketIDParma = 0
	SELECT @ThucChayAdmarketIDParma = [ThucChayAdmarketID]
	FROM   [dbo].[ThucChayAdmarket] A
	WHERE  ([CreateDate] = @CreateDate)
	       AND ([User_ID] = @UserID)
	       AND ([TTC] = @TTC)
	       AND ([TTV] = @TTV)
	       AND ([DmSanPhamREF] = @DmSanPhamREF)
	
	IF (@ThucChayAdmarketIDParma = 0)
	BEGIN
	    INSERT INTO [dbo].[ThucChayAdmarket]
	      (
	        [User_ID],
	        [UserName],
	        [FullName],
	        [Email],
	        [Phone],
	        [GroupID],
	        [GroupName],
	        [TTC],
	        [TTV],
	        [Money],
	        [Promotion],
	        [DmSanPhamREF],
	        [TenSanPham],
	        [CreateDate]
	      )
	    VALUES
	      (
	        @UserID,
	        @UserName,
	        @FullName,
	        @Email,
	        @Phone,
	        @GroupID,
	        @GroupName,
	        @TTC,
	        @TTV,
	        @Money,
	        @Promotion,
	        @DmSanPhamREF,
	        @TenSanPham,
	        @CreateDate
	      )
	END
	ELSE
	BEGIN
	    EXEC usp_UpdateThucChayAdmarket @ThucChayAdmarketIDParma,
	         @UserID,
	         @UserName,
	         @FullName,
	         @Email,
	         @Phone,
	         @GroupID,
	         @GroupName,
	         @TTC,
	         @TTV,
	         @Money,
	         @Promotion,
	         @DmSanPhamREF,
	         @TenSanPham
	END
END

```
