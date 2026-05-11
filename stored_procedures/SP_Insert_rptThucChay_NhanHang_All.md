# Stored Procedure: `Insert_rptThucChay_NhanHang_All`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-31 11:21:10.057000
- **Ngày sửa cuối**: 2015-03-31 11:21:10.057000

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
--EXEC [dbo].[Insert_rptThucChay_NhanHang_All] '2013-01-01','2013-01-31'
CREATE PROCEDURE [dbo].[Insert_rptThucChay_NhanHang_All]
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
			EXEC dbo.Insert_rptThucChay_NhanHang_Ngay @NgayThucHien,@NgayThucHien
			EXEC dbo.Insert_rptThucChay_NhanHang_Thang @NgayThucHien
			EXEC dbo.Insert_rptThucChay_NhanHang_Quy @NgayThucHien
			EXEC dbo.Insert_rptThucChay_NhanHang_Nam @NgayThucHien
			SET @NgayThucHien = DATEADD(DAY,1,@NgayThucHien)
		END
END



```
