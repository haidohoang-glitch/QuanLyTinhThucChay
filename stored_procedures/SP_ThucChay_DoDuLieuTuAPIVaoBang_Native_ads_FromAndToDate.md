# Stored Procedure: `ThucChay_DoDuLieuTuAPIVaoBang_Native_ads_FromAndToDate`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-07-31 10:59:38.263000
- **Ngày sửa cuối**: 2018-07-31 11:01:49.533000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |
| `@TypeProduct` | `int(4)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuThuViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================
--EXEC [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_Native_ads_FromAndToDate] '2018-07-18','2018-07-30', 19
CREATE PROCEDURE [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_Native_ads_FromAndToDate] 
	 @FromDate DATETIME,
	 @ToDate DATETIME,
	 @TypeProduct INT
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @FromDate

	WHILE(@NgayThucHien <= @ToDate)
	BEGIN
		EXEC [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_Native_ads] 
		 @NgayThucHien = @NgayThucHien,
		 @TypeProduct = @TypeProduct

		SET @NgayThucHien = DATEADD(d,1,@NgayThucHien)
	END

END




```
