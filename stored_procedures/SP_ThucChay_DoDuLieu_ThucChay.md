# Stored Procedure: `ThucChay_DoDuLieu_ThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-07-08 17:03:01.683000
- **Ngày sửa cuối**: 2021-07-08 17:44:05.197000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuThuViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================
/*
EXEC [ThucChay_DoDuLieu_ThucChay] '2021-01-01', '2021-01-31'
*/
CREATE PROCEDURE [dbo].[ThucChay_DoDuLieu_ThucChay] 
	@FromDate DATETIME
	, @ToDate DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME 
	SET @NgayThucHien = CONVERT(DATE,@FromDate)
	WHILE (@NgayThucHien <= @ToDate)
	BEGIN
		EXEC [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_job_Branding_NgayThucHien] @NgayThucHien = @NgayThucHien
		SET @NgayThucHien = DATEADD(DAY,1,@NgayThucHien)
    END

END




```
