# Stored Procedure: `sp_Insert_ThongTinNgayChotThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-03-19 09:50:49.963000
- **Ngày sửa cuối**: 2021-03-19 09:54:19.473000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@F_NgayThucHien` | `datetime(8)` | No |
| `@E_NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_Insert_ThongTinNgayChotThucChay]
	@F_NgayThucHien DATETIME
	,@E_NgayThucHien DATETIME
AS
BEGIN
	IF( NOT EXISTS(SELECT TOP (1) c.ID FROM [dbo].[ThongTinNgayChotThucChay] c
		WHERE c.F_NgayThucHien = @F_NgayThucHien AND c.E_NgayThucHien = @E_NgayThucHien
		AND c.DeletedStatus = 0 ORDER BY c.ID))
	INSERT INTO [dbo].[ThongTinNgayChotThucChay]
           ([F_NgayThucHien]
           ,[E_NgayThucHien]
           ,[TrangThaiChot]
           ,[CreatedAt]
           ,[CreatedBy]
           ,[LastModifiedAt]
           ,[LastModifiedBy]
           ,[DeletedStatus])
     VALUES
           (
           @F_NgayThucHien
           ,@E_NgayThucHien
           ,1
           ,GETDATE()
           ,CURRENT_USER
           ,GETDATE()
           ,CURRENT_USER
           ,0)
END

```
