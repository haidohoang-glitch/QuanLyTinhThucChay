# Stored Procedure: `prc_ADX_Job_UpdateStatusThayDoiThucChay_Update_Status`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-03-25 17:47:26.463000
- **Ngày sửa cuối**: 2021-03-25 17:47:26.463000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Status` | `int(4)` | No |
| `@RequestKeyError` | `nvarchar(4000)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[prc_ADX_Job_UpdateStatusThayDoiThucChay_Update_Status]
	@Status INT,
	@RequestKeyError NVARCHAR(2000) = ''
AS
BEGIN
	UPDATE dbo.ADX_Job_UpdateStatusThayDoiThucChay
	SET Status = @Status,
		RequestKeyError = @RequestKeyError
	WHERE IsDeleted = 0 AND Status = 1

	SELECT 1
END


```
