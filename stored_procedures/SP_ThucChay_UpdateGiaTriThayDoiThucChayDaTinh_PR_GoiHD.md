# Stored Procedure: `ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_PR_GoiHD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-01-27 09:40:54.583000
- **Ngày sửa cuối**: 2016-01-27 09:42:00.740000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_ExcInsertThucChayDaTinh_CPR] '2015-09-13','2015-09-13'

CREATE PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_PR_GoiHD] 
	@StartDate datetime,
	@EndDate datetime
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @ThoiGianBDTinh DATETIME
				
	SET @NgayThucHien = @StartDate
	SET @ThoiGianBDTinh = '2014-01-01'
	
	WHILE(@NgayThucHien <= @EndDate)
	BEGIN
		EXEC [ThucChay_CheckThucTreoThayDoi_PR_GoiHD]	@NgayThucHien ,	@ThoiGianBDTinh
		SET @NgayThucHien = dateadd(d,1,@NgayThucHien) 
	END 
	SELECT '1'
END


--EXEC [ThucChay_ExcInsertThucChayDaTinh_CPR] '2014-06-03','2014-06-03'

```
