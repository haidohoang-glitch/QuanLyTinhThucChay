# Function: `GetTrangThaiThucChayHopDongChiTiet`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-30 17:34:07.273000
- **Ngày sửa cuối**: 2014-10-14 10:39:35.043000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetTrangThaiThucChayHopDongChiTiet]
(
	-- Add the parameters for the function here
	@HopDongChiTietID INT
)
RETURNS INT
AS
BEGIN
	
	DECLARE 
	@TrangThai INT
	,@RecordCountChuaChay INT 	
	,@RecordCountDangChay INT 
	,@RecordCountKetThucChay INT 
		
	
							
	SET @RecordCountChuaChay = (
							SELECT COUNT(*) FROM ThucChayTheoDoiHopDongChiTiet A
							WHERE 
							A.HopDongChiTietID = @HopDongChiTietID
							AND A.SoLuongDaChay = 0
						)

							
	SET @RecordCountDangChay = (
							SELECT COUNT(*) FROM ThucChayTheoDoiHopDongChiTiet A
							WHERE 
							A.HopDongChiTietID = @HopDongChiTietID
							AND A.SoLuongDaChay > 0 AND SoLuongChuaChay > 0
						)	
	
	SET @RecordCountKetThucChay = (
							SELECT COUNT(*) FROM ThucChayTheoDoiHopDongChiTiet A
							WHERE 
							A.HopDongChiTietID = @HopDongChiTietID
							AND A.SoLuongDaChay > 0 AND SoLuongChuaChay <= 0
						)
	--Trang Thai khong xac dinh
	SET @TrangThai = -1
	
	IF(@RecordCountKetThucChay>0) SET @TrangThai = 2
	ELSE
	IF(@RecordCountDangChay >0) SET @TrangThai = 1
	ELSE
	IF(@RecordCountChuaChay >0) SET @TrangThai = 0
					
	-- Return the result of the function
	RETURN @TrangThai

END


--UPDATE dbo.ThucChayTheoDoiHopDongChiTiet
--SET RecordStatus = dbo.[dbo].[GetTrangThaiThucChayHopDongChiTiet](HopDongChiTietID)
```
