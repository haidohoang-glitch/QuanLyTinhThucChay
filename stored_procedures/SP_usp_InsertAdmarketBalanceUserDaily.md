# Stored Procedure: `usp_InsertAdmarketBalanceUserDaily`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-25 14:31:05.200000
- **Ngày sửa cuối**: 2015-07-08 11:48:05.230000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Code` | `nvarchar(100)` | No |
| `@UserID` | `int(4)` | No |
| `@UserName` | `nvarchar(100)` | No |
| `@DateCreated` | `datetime(8)` | No |
| `@UserBalance` | `bigint(8)` | No |
| `@UserPromotion` | `bigint(8)` | No |
| `@EchargeMoney` | `bigint(8)` | No |
| `@SpentBalance` | `bigint(8)` | No |
| `@SpentPromotion` | `bigint(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_InsertAdmarketBalanceUserDaily]
(
	@Code NVARCHAR(50),
	@UserID int,
	@UserName nvarchar(50),
	@DateCreated datetime,
	@UserBalance bigint,
	@UserPromotion BIGINT,
	@EchargeMoney BIGINT,
	@SpentBalance BIGINT,
	@SpentPromotion BIGINT,
	@NgayThucHien datetime
)
AS

SET NOCOUNT ON
BEGIN
	DECLARE @DmSanPhamREF INT, @TenSanPham NVARCHAR(100)
	
	SET @DmSanPhamREF = 0
	SET @TenSanPham = ''
	
	IF(@Code = 'cpc')
	BEGIN
		SET @DmSanPhamREF = 144
		SET @TenSanPham = 'CPC Admarket' 
	END
	ELSE IF(@Code IN ('adx','ecomx','mobx'))
	BEGIN
		SET @DmSanPhamREF = 585
		SET @TenSanPham = 'AdX'
	END
	ELSE if(@Code = 'viewplus')
	SET @DmSanPhamREF = 628
	
	IF EXISTS(SELECT [UserID]
          FROM dbo.admarketBalanceUserDaily  
          WHERE
			CONVERT(Date,[NgayThucHien]) = CONVERT(Date,@NgayThucHien) 
			AND [UserID] = @UserID
			AND [UserName] = @UserName
			AND [Code] = @Code)
			
	  UPDATE [dbo].[AdmarketBalanceUserDaily]
	   SET [Code] = @Code
		  ,[DateCreated] = @DateCreated
		  ,[UserBalance] = @UserBalance
		  ,[UserPromotion] = @UserPromotion
		  ,[EchargeMoney] = @EchargeMoney
		  ,[SpentBalance] = @SpentBalance
		  ,[SpentPromotion] = @SpentPromotion
		  ,[LastModifiedBy] = 'WebService Admarket Update' 
		  ,[LastModifiedAt] = GETDATE()
		WHERE
			CONVERT(Date,[NgayThucHien]) = CONVERT(Date,@NgayThucHien)
			AND [UserID] = @UserID
			AND [UserName] = @UserName
			AND [Code] = @Code
	ELSE
		INSERT INTO [dbo].[AdmarketBalanceUserDaily]
			   ([Code]
			   ,[DmSanPhamREF]
			   ,[TenSanPham]
			   ,[UserID]
			   ,[UserName]
			   ,[DateCreated]
			   ,[UserBalance]
			   ,[UserPromotion]
			   ,[EchargeMoney]
			   ,[SpentBalance]
			   ,[SpentPromotion]
			   ,[NgayThucHien]
			   ,[CreatedBy]
			   ,[CreatedAt]
			   ,[LastModifiedBy]
			   ,[LastModifiedAt]
			   ,[RecordStatus]
			   ,[DeletedStatus])
		 VALUES
			   (@Code
			   ,@DmSanPhamREF
			   ,@TenSanPham
			   ,@UserID
			   ,@UserName
			   ,@DateCreated
			   ,@UserBalance
			   ,@UserPromotion
			   ,@EchargeMoney
			   ,@SpentBalance
			   ,@SpentPromotion
			   ,@NgayThucHien
			   ,'WebService Admarket' 
			   ,GETDATE()
			   ,'WebService Admarket'
			   ,GETDATE()
			   ,0
			   ,0)


END


```
