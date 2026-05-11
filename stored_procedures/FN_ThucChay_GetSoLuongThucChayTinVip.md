# Function: `ThucChay_GetSoLuongThucChayTinVip`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-05-29 11:10:02.677000
- **Ngày sửa cuối**: 2014-10-14 10:39:30.210000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetSoLuongThucChayTinVip] 
(
	-- Add the parameters for the function here
	@NgayThucHien DATETIME,
	@HopDongChiTietREF INT
)
RETURNS INT
AS
BEGIN
	DECLARE @Count INT	
	
	SET  @Count = 
			(
				SELECT count(dchdct.HopDongChiTietREF) 
				FROM ThucChayHopDongChiTiet dchdct INNER JOIN HopDongChiTiet hdct 
				ON dchdct.HopDongChiTietREF = hdct.HopDongChiTietID
				WHERE dchdct.HopDongChiTietREF = @HopDongChiTietREF
				--AND hdct.DmSanPhamREF in (241,264,300,268,248,270,243,244,249)	
				AND dchdct.DeletedStatus = 0
				AND hdct.DeletedStatus = 0
				AND CONVERT(DATE, dchdct.ThoiGianBatDau)  <= CONVERT(DATE,@NgayThucHien)
				AND CONVERT(DATE,dchdct.ThoiGianKetThuc) >= CONVERT(DATE,@NgayThucHien)		
				AND YEAR(dchdct.ThoiGianKetThuc) >= 2013		
			)	
							
	-- Return the result of the function
	RETURN @Count

END

```
