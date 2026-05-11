# Stored Procedure: `ThucChay_UpdateThucChayHopDongChiTietPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-01 08:35:16.590000
- **Ngày sửa cuối**: 2014-11-19 12:24:44.560000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuThuViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[ThucChay_UpdateThucChayHopDongChiTietPR]
	@NgayThucHien datetime
AS

BEGIN
	DECLARE @v_str_thuctreopr NVARCHAR(MAX)
	
	SET @v_str_thuctreopr = 
	(SELECT
		stuff(
		(
			SELECT cast(',' as varchar(max)) + Convert(nvarchar(20),ThucChayHopDongChiTietPRID)
			  FROM ThucChayHopDongChiTietPR
			WHERE (CASE when CreatedAt >= LastModifiedAt THEN Convert(date,CreatedAt) 
			else Convert(date,LastModifiedAt)
			END
			)  = @NgayThucHien
			AND RecordStatus = 0
			AND DeletedStatus <> 1
			AND HopDongChiTietREF <> 0
			AND HopDongREF NOT IN (SELECT HopDongID FROM HopDong hd WHERE hd.TrangThaiHopDong = 3)			
			for xml path('') 
		), 1, 1, '') AS DotChayBooking
	)
	
	UPDATE ThucChayHopDongChiTietPR
	SET RecordStatus = 1 
	WHERE ThucChayHopDongChiTietPRID IN (SELECT att.item FROM dbo.ArrayToTable(dbo.Array(@v_str_thuctreopr, ',') ) att)

END

	

--endregion


```
