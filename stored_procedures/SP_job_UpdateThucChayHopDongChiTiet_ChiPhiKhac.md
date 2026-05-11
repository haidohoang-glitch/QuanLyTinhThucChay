# Stored Procedure: `job_UpdateThucChayHopDongChiTiet_ChiPhiKhac`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-10-31 15:06:08.560000
- **Ngày sửa cuối**: 2016-10-31 15:09:56.220000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuThuViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================
--EXEC [dbo].[job_UpdateThucChayHopDongChiTiet_ChiPhiKhac]
CREATE PROCEDURE [dbo].[job_UpdateThucChayHopDongChiTiet_ChiPhiKhac]
	@StartDate datetime,
	@EndDate datetime
AS
BEGIN
DECLARE @NgayThucHien DATETIME, @NgayGioiHanTinh DATETIME
set @NgayThucHien = Convert(date,@StartDate)
SET @NgayGioiHanTinh = '2013-01-01'
	WHILE(@NgayThucHien <= @EndDate)
	BEGIN
		EXEC [ThucChay_UpdateThucChayHopDongChiTiet_ChiPhiKhac] @NgayThucHien
		SET @NgayThucHien = dateadd(d,1,@NgayThucHien)
	END 
END




```
