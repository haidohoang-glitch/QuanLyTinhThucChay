# Function: `ThucChay_GetSoLuongChuan_TinVIP`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-06-24 16:43:32.990000
- **Ngày sửa cuối**: 2014-10-14 10:39:31.737000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietID` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetSoLuongChuan_TinVIP]
(
	-- Add the parameters for the function here
	@NgayThucHien datetime,
	@HopDongChiTietID nvarchar(50)	
)
RETURNS INT
AS
BEGIN
	DECLARE @SoNgayTheoDonViTinh INT
	SET @SoNgayTheoDonViTinh = 0
	
	SET @SoNgayTheoDonViTinh = 
	(
		SELECT ISNULL(SUM(DATEDIFF (day, dchdct.ThoiGianBatDau, dchdct.ThoiGianKetThuc) + 1),0) 
		FROM ThucChayHopDongChiTiet dchdct
		INNER JOIN HopDongChiTiet hdct 
		ON	dchdct.HopDongChiTietREF = hdct.HopDongChiTietID
		WHERE dchdct.HopDongChiTietREF = @HopDongChiTietID
		AND hdct.DmSanPhamREF in (241,264,300,268,248,270,243,244,249)
		AND dchdct.DeletedStatus = 0
		AND dchdct.RecordStatus  = 0				

    )
	
	-- Return the result of the function
	RETURN @SoNgayTheoDonViTinh

END

```
