# Stored Procedure: `ThucChay_UpdateThucChayHopDongChiTiet_ByHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-02-26 17:39:23.580000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.573000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongREF` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChay_UpdateThucChayHopDongChiTiet_ByHopDong]
	@NgayThucHien DATETIME,
	@HopDongREF INT
AS

BEGIN
	DECLARE @v_str_thuctreopr NVARCHAR(MAX)
	SET @v_str_thuctreopr = 
	(SELECT
		stuff(
		(
			SELECT cast(',' as varchar(max)) + Convert(nvarchar(20),ThucChayHopDongChiTietID)
			  FROM ThucChayHopDongChiTiet
			WHERE (CASE when CreatedAt >= LastModifiedAt THEN Convert(date,CreatedAt) 
			else Convert(date,LastModifiedAt)
			END
			)  = @NgayThucHien
			AND HopDongREF = @HopDongREF
			AND RecordStatus = 0
			AND HopDongChiTietREF <> 0 
			for xml path('') 
		), 1, 1, '') AS DotChayBooking
	)

	UPDATE ThucChayHopDongChiTiet
	SET RecordStatus = 1 
	WHERE ThucChayHopDongChiTietID IN (SELECT att.item FROM dbo.ArrayToTable(dbo.Array(@v_str_thuctreopr, ',') ) att)

END

```
