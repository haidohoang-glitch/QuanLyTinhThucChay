# Stored Procedure: `ThucChayGoogleFacebook_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-08 10:00:22.113000
- **Ngày sửa cuối**: 2015-04-08 10:00:22.113000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TaiKhoan` | `nvarchar(100)` | No |
| `@SoNgayChay` | `int(4)` | No |
| `@Click` | `int(4)` | No |
| `@ThanhTien` | `float(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@LastModifiedBy` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ	
-- Create date: 2014-10-08
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayGoogleFacebook_Insert]
	-- Add the parameters for the stored procedure here
	@TaiKhoan	NVARCHAR(50),
	@SoNgayChay	INT,
	@Click		INT,
	@ThanhTien	FLOAT,
	@NgayThucHien	DATETIME,
	@CreatedBy	NVARCHAR(50),
	@LastModifiedBy	NVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    INSERT INTO [dbo].[ThucChayGoogleFacebook]
           ([ThucChayGoogleFacebookID]
           ,[TaiKhoan]
           ,[SoNgayChay]
           ,[Click]
           ,[ThanhTien]
           ,[NgayThucHien]
           ,[CreatedAt]
           ,[CreatedBy]
           ,[LastModifiedAt]
           ,[LastModifiedBy]
           ,[RecordStatus])
     VALUES
           (
           	NEWID()
           ,@TaiKhoan
           ,@SoNgayChay
           ,@Click
           ,@ThanhTien
           ,@NgayThucHien
           ,GETDATE()
           ,@CreatedBy
           ,GETDATE()
           ,@LastModifiedBy
           ,1
           )
END

```
