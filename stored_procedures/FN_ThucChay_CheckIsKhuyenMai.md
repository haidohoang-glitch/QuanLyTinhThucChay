# Function: `ThucChay_CheckIsKhuyenMai`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-11-13 10:47:37.213000
- **Ngày sửa cuối**: 2014-10-14 10:39:34.050000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-11-13
-- Description:	Check phân bổ là khuyến mại hay không
-- =============================================
CREATE FUNCTION dbo.ThucChay_CheckIsKhuyenMai 
(
	@HopDongChiTietREF INT
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @IsKhuyenMai INT
	DECLARE @ThanhTienKM FLOAT
	
	SET @ThanhTienKM = (SELECT ISNULL(SUM(A.ThanhTienKM),0) FROM ThucChayDaTinh A WHERE A.HopDongChiTietREF = @HopDongChiTietREF)
	
	SET @IsKhuyenMai = (CASE @ThanhTienKM
							WHEN 0 THEN 0
							ELSE 1
						END)
	

	-- Return the result of the function
	RETURN @IsKhuyenMai

END

```
