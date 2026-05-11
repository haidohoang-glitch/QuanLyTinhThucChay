# Stored Procedure: `usp_InsertAdmarketUserLastRecharge`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-25 14:31:05.157000
- **Ngày sửa cuối**: 2015-04-25 14:31:05.157000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Code` | `nvarchar(100)` | No |
| `@UserID` | `int(4)` | No |
| `@UserName` | `nvarchar(400)` | No |
| `@LastDateRecharge` | `datetime(8)` | No |
| `@RechargeMoney` | `bigint(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_InsertAdmarketUserLastRecharge]
(
	@Code NVARCHAR(50)
	  ,@UserID INT
      ,@UserName NVARCHAR(200)
      ,@LastDateRecharge DATETIME
      ,@RechargeMoney BIGINT
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
	
	IF EXISTS(SELECT [UserID]
          FROM AdmarketUserLastRecharge  
          WHERE
			CONVERT(Date,LastDateRecharge) = CONVERT(Date,@LastDateRecharge) 
			AND [UserID] = @UserID
			AND [UserName] = @UserName
			AND [Code] = @Code)
			
  UPDATE [dbo].[AdmarketUserLastRecharge]
   SET [UserID] = @UserID
      ,[UserName] = @UserName
      ,[LastDateRecharge] = @LastDateRecharge
      ,[RechargeMoney] = @RechargeMoney
      ,[LastModifiedBy] = 'ASD'
      ,[LastModifiedAt] = GETDATE()
  WHERE
		CONVERT(Date,LastDateRecharge) = CONVERT(Date,@LastDateRecharge) 
		AND [UserID] = @UserID
		AND [UserName] = @UserName
		AND [Code] = @Code

ELSE
	INSERT INTO [dbo].[AdmarketUserLastRecharge]
           (
           	[DmSanPhamREF]
           ,[TenSanPham]	
           ,[Code]
           ,[UserID]
           ,[UserName]
           ,[LastDateRecharge]
           ,[RechargeMoney]
           ,[CreatedBy]
           ,[CreatedAt]
           ,[LastModifiedBy]
           ,[LastModifiedAt]
           ,[RecordStatus]
           ,[DeletedStatus])
     VALUES
           (
           	@DmSanPhamREF
           ,@TenSanPham
           ,@Code
           ,@UserID
           ,@UserName
           ,@LastDateRecharge
           ,@RechargeMoney
           ,'ASD'
           ,GETDATE()
           ,'ASD'
           ,GETDATE()
           ,0
           ,0)

END







```
