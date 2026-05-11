# Stored Procedure: `ThucChayGoogleFacebook_UpdateStatusByDay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-08 10:00:22.083000
- **Ngày sửa cuối**: 2015-04-08 10:00:22.083000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@Action` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-10-10
-- Description:	Update status records
-- =============================================

CREATE PROCEDURE [dbo].[ThucChayGoogleFacebook_UpdateStatusByDay]
	-- Add the parameters for the stored procedure here
	@StartDate	DATETIME,
	@EndDate	DATETIME,
	@DmSanPhamREF	INT,	
	@Action			NVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	IF @Action = 'DELETE'
	BEGIN
		IF @DmSanPhamREF <> -1
		BEGIN
    		UPDATE ThucChayGoogleFacebook
    		SET
    			DeletedStatus = 1
    		WHERE NgayThucHien BETWEEN @StartDate AND @EndDate
    			AND DmSanPhamREF = @DmSanPhamREF   
    			AND RecordStatus = 0 		
		END
		ELSE
		BEGIN
    		UPDATE ThucChayGoogleFacebook
    		SET
    			DeletedStatus = 1
    		WHERE NgayThucHien BETWEEN @StartDate AND @EndDate
    			AND RecordStatus = 0
		END
	END
	ELSE -- Update
	BEGIN
		IF @DmSanPhamREF <> -1
		BEGIN
    		UPDATE ThucChayGoogleFacebook
    		SET
    			RecordStatus = 1
    		WHERE NgayThucHien BETWEEN @StartDate AND @EndDate
    			AND DmSanPhamREF = @DmSanPhamREF   
    			AND RecordStatus = 0
    			AND DeletedStatus = 0 		
		END
		ELSE
		BEGIN
    		UPDATE ThucChayGoogleFacebook
    		SET
    			RecordStatus = 1
    		WHERE NgayThucHien BETWEEN @StartDate AND @EndDate
    			AND RecordStatus = 0
    			AND DeletedStatus = 0
		END
	END
END

```
