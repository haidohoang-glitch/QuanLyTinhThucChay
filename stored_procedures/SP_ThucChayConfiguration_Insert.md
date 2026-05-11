# Stored Procedure: `ThucChayConfiguration_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-01-02 11:29:37.453000
- **Ngày sửa cuối**: 2015-01-02 11:30:58.830000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@namThucChay` | `int(4)` | No |
| `@ghiChu` | `nvarchar(510)` | No |
| `@actionUser` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 20145-01-02
-- Description:	<Description,,>
-- =============================================
/*
	EXEC dbo.ThucChayConfiguration_Insert 2014, '', 'nhatmq'
*/
CREATE PROCEDURE dbo.ThucChayConfiguration_Insert
	-- Add the parameters for the stored procedure here
	@namThucChay	INT,
	@ghiChu			NVARCHAR(255),
	@actionUser		NVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    INSERT INTO [dbo].[ThucChayConfiguration]
           ([ThucChayConfigurationID]
           ,[NamThucChay]
           ,[GhiChu]
           ,[CreatedAt]
           ,[CreatedBy]
           ,[LastModifiedAt]
           ,[LastModifiedBy]
           ,[DeletedStatus]
           ,[RecordStatus]
           ,[PrintStatus])
     VALUES
           (NEWID() 
           ,@namThucChay 
           ,@ghiChu	
           ,GETDATE() 
           ,@actionUser 
           ,GETDATE() 
           ,@actionUser 
           ,0 
           ,1 
           ,0 )
END

```
