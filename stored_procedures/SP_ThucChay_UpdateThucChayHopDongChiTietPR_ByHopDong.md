# Stored Procedure: `ThucChay_UpdateThucChayHopDongChiTietPR_ByHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-12 16:27:33.507000
- **Ngày sửa cuối**: 2016-01-05 18:20:52.267000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuThuViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[ThucChay_UpdateThucChayHopDongChiTietPR_ByHopDong]
	@NgayThucHien DATETIME,
	@HopDongREF INT,
	@HopDongChiTietREF INT
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
			AND HopDongREF = @HopDongREF
			AND HopDongChiTietREF = @HopDongChiTietREF
			AND RecordStatus = 0
			AND HopDongChiTietREF <> 0 
			for xml path('') 
		), 1, 1, '') AS DotChayBooking
	)
	
	UPDATE ThucChayHopDongChiTietPR
	SET RecordStatus = 1 
	WHERE ThucChayHopDongChiTietPRID IN (SELECT att.item FROM dbo.ArrayToTable(dbo.Array(@v_str_thuctreopr, ',') ) att)

END

	

--endregion


```
