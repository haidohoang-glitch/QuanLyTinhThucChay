# Function: `ThucChay_GetSoLuongNgayThucTreo`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-03-01 10:35:53.340000
- **Ngày sửa cuối**: 2019-04-04 14:58:47.193000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@HopDongChiTietID` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[ThucChay_GetSoLuongNgayThucTreo]
(
	-- Add the parameters for the function here
	--@SoLuong INT, 
	--@DonViTinh nvarchar(50),
	@HopDongChiTietID NVARCHAR(50)
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here	
	DECLARE @SoNgayTheoDonViTinh INT	
	SET @SoNgayTheoDonViTinh = 
	(
		SELECT ISNULL(sum(DATEDIFF(day, tchdct.ThoiGianBatDau, tchdct.ThoiGianKetThuc) + 1),0)
		FROM dbo.ThucChayHopDongChiTiet tchdct
		INNER JOIN dbo.HopDongChiTiet hdct ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
		WHERE
		tchdct.RecordStatus = 0		
		AND hdct.DmSanPhamREF IN (385,5005 ,5006,5007,5082 ) 	 
		AND hdct.HopDongChiTietID = @HopDongChiTietID
	)
	-- Return the result of the function
	RETURN @SoNgayTheoDonViTinh
END

```
