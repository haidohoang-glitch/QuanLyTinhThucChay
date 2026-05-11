# Function: `ThucChay_GetDonViTinhMobileByHopDongChiTietID`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-10-01 15:50:52.543000
- **Ngày sửa cuối**: 2014-11-19 12:17:40.443000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(100)` | Yes |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetDonViTinhMobileByHopDongChiTietID]
(
	-- Add the parameters for the function here
	@HopDongChiTietID INT,
	@NgayThucHien DATETIME
)
RETURNS NVARCHAR(50)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ResultValue NVARCHAR(50)

	DECLARE @IsKhuyenMai INT,
			@DonViTinh NVARCHAR(50),
			@ProductUnitName NVARCHAR(50);
	
	SELECT @DonViTinh   = hdct.DonViTinh 		   
	FROM HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = @HopDongChiTietID
	
	SELECT @ProductUnitName = (SELECT TOP 1 ProductUnitName 
								FROM ThucChay_MobileTemp tcmt 
								WHERE tcmt.HopDongChiTietREF = @HopDongChiTietID 
									 AND tcmt.NgayThucHien = @NgayThucHien
								ORDER BY tcmt.ProductUnitName
	                          )
	SET @ResultValue = (CASE WHEN @DonViTinh IN ('CPC','CPM','CPV') THEN @DonViTinh
									ELSE @ProductUnitName
							   END
							   ) 
	-- Return the result of the function
	RETURN @ResultValue;

END

```
