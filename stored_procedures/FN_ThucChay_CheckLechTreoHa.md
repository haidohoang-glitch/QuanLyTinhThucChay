# Function: `ThucChay_CheckLechTreoHa`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-18 14:37:59.610000
- **Ngày sửa cuối**: 2014-10-14 10:39:34.010000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE  FUNCTION [dbo].[ThucChay_CheckLechTreoHa]
(
	-- Add the parameters for the function here
	@NgayThucHien datetime,
	@HopDongChiTietREF INT,
	@TenSanPham NVARCHAR(50)
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Count int
	Set @Count = 0
	IF((@TenSanPham = N'Banner - CPD') or (@TenSanPham = N'Box App CPD'))
		BEGIN
			SET  @Count = 
			(
				SELECT COUNT(*)
				FROM (
					SELECT MAX(A.ThoiGianKetThuc) NgayKetThuc, MIN(ThoigianBatDau) NgayBatDau  
					FROM DOTCHAYHOPDONGCHITIET A
					WHERE HopDongChiTietREF = @HopDongChiTietREF
					AND A.DeletedStatus = 0
				)A
				WHERE CONVERT(DATE,A.NgayBatDau)  <= CONVERT(DATE,@NgayThucHien)
				AND CONVERT(DATE,A.NgayKetThuc) >= CONVERT(DATE,@NgayThucHien)
			)
		END
	ELSE 
		SET @Count = 1
	
		
	RETURN @Count

END

```
