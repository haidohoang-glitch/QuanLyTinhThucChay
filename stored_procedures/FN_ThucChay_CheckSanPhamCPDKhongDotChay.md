# Function: `ThucChay_CheckSanPhamCPDKhongDotChay`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-07-01 09:36:20.887000
- **Ngày sửa cuối**: 2014-10-14 10:39:33.840000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-11-13
-- Description:	Check phân bổ là khuyến mại hay không
-- =============================================


CREATE FUNCTION [dbo].[ThucChay_CheckSanPhamCPDKhongDotChay] 
(
	@HopDongChiTietREF INT,
	@NgayThucHien DATETIME
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @IsKhongDotChay INT
	DECLARE @countDotChay INT, @countThucTreo INT
	
	SET @IsKhongDotChay = 0
	SET @countDotChay = 0
	SET @countThucTreo = 0
	
	SET @countThucTreo = 
	(
		SELECT COUNT(tchdct.HopDongChiTietREF) 
		FROM ThucChayHopDongChiTiet tchdct
		WHERE tchdct.HopDongChiTietREF = @HopDongChiTietREF
		AND tchdct.DeletedStatus = 0
		--AND (@NgayThucHien BETWEEN convert(date,tchdct.ThoiGianBatDau) AND convert(date,tchdct.ThoiGianKetThuc))
	)
	
	IF(@countThucTreo >0)
	BEGIN
		SET @countDotChay =
		(
			SELECT COUNT(dchdct.HopDongChiTietREF) 
			FROM DotChayHopDongChiTiet dchdct
			WHERE dchdct.HopDongChiTietREF = @HopDongChiTietREF
			AND dchdct.DeletedStatus = 0	
		)
		IF(@countDotChay = 0)
			SET @IsKhongDotChay =1
		ELSE 
			SET @IsKhongDotChay = 0	 
	END

	-- Return the result of the function
	RETURN @IsKhongDotChay

END

```
