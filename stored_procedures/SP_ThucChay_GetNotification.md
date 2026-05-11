# Stored Procedure: `ThucChay_GetNotification`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-31 16:17:25.323000
- **Ngày sửa cuối**: 2014-11-19 12:16:55.087000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@UserName` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-07-31
-- Description:	Get notification 
-- [ThucChay_GetNotification] 'sonvuminh'
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_GetNotification]
	-- Add the parameters for the stored procedure here
	@UserName	NVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @Message			NVARCHAR(MAX) = '';
    DECLARE @MaxDate			NVARCHAR(50);
    DECLARE @Span				NVARCHAR(50)  = '<span style="line-height: 32px;">';
    
    DECLARE @StarDateActive		NVARCHAR(50),
			@EndDateActive		NVARCHAR(50),
			@MaxNgayThucHien	NVARCHAR(50);
    
    SELECT @MaxDate = dbo.FormatDate(MAX(NgayThucHien)) FROM ThucChayDaTinh
    
    SET @Message = N'Dữ liệu thực chạy trên hệ thống được cập nhật đến ngày: <b>';
    
    SET @Message += (
		SELECT dbo.FormatDate(MAX(NgayThucHien)) FROM ThucChayDaTinh	
    )            
    
    SET @Message += '</b>';
    
    IF EXISTS(SELECT UserName FROM AdminPermisionUsersByTime A WHERE A.UserName = @UserName AND A.RecordStatus = 1)
	BEGIN
		SELECT 
			@StarDateActive = dbo.FormatDate(StartDateActive),
			@EndDateActive  = dbo.FormatDate(EndDateActive)
		FROM AdminPermisionUsersByTime
		WHERE 
			UserName			= @UserName
			AND RecordStatus	= 1
		
		SET @Message += '</br>';
		SET @Message += N'Bạn chỉ được xem dữ liệu trong khoảng thời gian: <b>' + @StarDateActive + ' - ' + @EndDateActive + '</b></span>';
		
		SET @Span = '<span style="line-height: 20px;">';		
	END
    
    SELECT @MaxDate AS MaxDate, @Span + @Message AS MessageNotification;
END

```
