# Stored Procedure: `Insert_rptThucChay_LoaiNenTang_All`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-07 12:18:51.917000
- **Ngày sửa cuối**: 2015-03-07 12:18:51.917000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[Insert_rptThucChay_LoaiNenTang_All]
	-- Add the parameters for the stored procedure here
	 @FromDate DATETIME
	,@ToDate DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @FromDate
	WHILE(@NgayThucHien <= @ToDate)
		BEGIN
			EXEC dbo.Insert_rptThucChay_LoaiNenTang_Ngay @NgayThucHien,@NgayThucHien
			EXEC dbo.Insert_rptThucChay_LoaiNenTang_Thang @NgayThucHien
			EXEC dbo.Insert_rptThucChay_LoaiNenTang_Quy @NgayThucHien
			EXEC dbo.Insert_rptThucChay_LoaiNenTang_Nam @NgayThucHien
			SET @NgayThucHien = DATEADD(DAY,1,@NgayThucHien)
		END
END

```
