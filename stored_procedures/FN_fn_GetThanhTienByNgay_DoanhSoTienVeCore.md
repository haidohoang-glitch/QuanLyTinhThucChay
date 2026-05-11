# Function: `fn_GetThanhTienByNgay_DoanhSoTienVeCore`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-06-12 10:46:56.113000
- **Ngày sửa cuối**: 2015-06-12 10:46:56.113000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@NgayThucHien` | `date(3)` | No |
| `@HopDongID` | `int(4)` | No |
| `@ThongTinTienVeID` | `int(4)` | No |
| `@ThanhTien` | `float(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================

CREATE FUNCTION [dbo].[fn_GetThanhTienByNgay_DoanhSoTienVeCore]
(
	-- Add the parameters for the function here
	@NgayThucHien Date,
	@HopDongID INT,
	@ThongTinTienVeID INT,
	@ThanhTien FLOAT
)
RETURNS float
AS
BEGIN
	-- Declare the return variable here
	
	DECLARE @ThanhTienResult FLOAT
	DECLARE @TongTien FLOAT
	DECLARE @TongTienTienVe FLOAT 
	SET @ThanhTienResult = 0
	-- Add the T-SQL statements to compute the return value here
	SET @TongTien = 
			(
				SELECT SUM(ThanhTien)  FROM HopDongChiTiet hd WHERE hd.HopDongFK = @HopDongID AND hd.DeletedStatus = 0
			
			)
	IF @TongTien > 0
	BEGIN 
	SET @TongTienTienVe =
	(
		SELECT SUM(tthd.GiaTri) FROM ThongTinTienve tthd
		WHERE tthd.ThongTinTienVeID = @ThongTinTienVeID
		
		AND tthd.DeletedStatus <> 1
	)
	
	SET @ThanhTienResult = (@TongTienTienVe/ @TongTien) * @ThanhTien	
	END 
	ELSE
		SET @ThanhTienResult = 0
	-- Return the result of the function
	SET @ThanhTienResult = ISNULL(@ThanhTienResult,0)
	RETURN @ThanhTienResult

END

```
