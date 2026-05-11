# Stored Procedure: `AdminPermisionUsersByTime_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 17:07:58.113000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.347000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@UserName` | `nvarchar(100)` | No |
| `@StartDateActive` | `datetime(8)` | No |
| `@EndDateActive` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-07-30
-- Description:	Danh sach nhung user duoc quyen xem du lieu trong khoang thoi gian nhat dinh.
-- =============================================
--
-- EXEC dbo.AdminPermisionUsersByTime_Insert 'hiennt', '2014-01-01', '2014-12-31'

CREATE PROCEDURE [dbo].[AdminPermisionUsersByTime_Insert] 
	-- Add the parameters for the stored procedure here
	@UserName			NVARCHAR(50),
	@StartDateActive	DATETIME,
	@EndDateActive		DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	IF NOT EXISTS (SELECT UserName FROM AdminPermisionUsersByTime WHERE UserName = @UserName AND RecordStatus = 1)
		INSERT INTO dbo.AdminPermisionUsersByTime
		(
    		AdminPermisionUsersByTimeID,
    		UserName,
    		Note,
    		StartDateActive,
    		EndDateActive,
    		CreatedAt,
    		CreatedBy,
    		LastModifiedAt,
    		LastModifiedBy,
    		DeletedStatus,
    		PrintStatus,
    		RecordStatus
		)
		VALUES
		(
    		NEWID(),
    		@UserName,
    		'',
    		@StartDateActive,
    		@EndDateActive,
    		GETDATE(),
    		'asd',
    		GETDATE(),
    		'asd',
    		0,
    		0,
    		1
		)
END

```
