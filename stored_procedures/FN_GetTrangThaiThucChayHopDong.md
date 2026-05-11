# Function: `GetTrangThaiThucChayHopDong`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-27 18:30:29.777000
- **Ngày sửa cuối**: 2014-10-14 10:39:35.077000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@HopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetTrangThaiThucChayHopDong]
(
	-- Add the parameters for the function here
	@HopDongID INT
)
RETURNS INT
AS
BEGIN
	
	DECLARE 
	@TrangThai INT
	,@RecordCount INT
	,@RecordCountKhongXacDinh INT 
	,@RecordCountChuaChay INT 	
	,@RecordCountDangChay INT 
	,@RecordCountKetThucChay INT 
		
	
	
	SET @RecordCount = (
							SELECT COUNT(*) FROM dbo.HopDongChiTiet A
							WHERE 
							A.HopDongFK = @HopDongID
						)
							
	SET @RecordCountChuaChay = (
							SELECT COUNT(*) FROM ThucChayTheoDoiHopDongChiTiet A
							WHERE 
							A.HopDongFK = @HopDongID
							AND A.TrangThaiHopDongChiTietThucChay = 0
						)

							
	SET @RecordCountDangChay = (
							SELECT COUNT(*) FROM ThucChayTheoDoiHopDongChiTiet A
							WHERE 
							A.HopDongFK = @HopDongID
							AND A.TrangThaiHopDongChiTietThucChay = 1
						)	
	
	SET @RecordCountKetThucChay = (
							SELECT COUNT(*) FROM ThucChayTheoDoiHopDongChiTiet A
							WHERE 
							A.HopDongFK = @HopDongID
							AND A.TrangThaiHopDongChiTietThucChay =2
						)
	--Trang Thai khong xac dinh
	SET @TrangThai = -1
	
	IF(@RecordCount = @RecordCountKetThucChay AND @RecordCountKetThucChay>0) SET @TrangThai = 2
	ELSE
	IF(@RecordCountDangChay >0 OR @RecordCountKetThucChay > 0) SET @TrangThai = 1
	ELSE
	IF(@RecordCount = @RecordCountKetThucChay AND @RecordCountChuaChay >0) SET @TrangThai = 0
					
	-- Return the result of the function
	RETURN @TrangThai

END

```
