# Function: `ThucChay_GetDonGiaTheoBaoGiaSanPham`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-06-02 14:29:54.707000
- **Ngày sửa cuối**: 2017-05-04 15:03:09.747000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@BannerType` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-06-02
-- Description:	Get UnitPrice by Product, BannerType, Date
-- =============================================
--
-- PRINT dbo.ThucChay_GetDonGiaTheoBaoGiaSanPham('2014-06-01', 342, 4, 2)
--
CREATE FUNCTION [dbo].[ThucChay_GetDonGiaTheoBaoGiaSanPham] 
(
	-- Add the parameters for the function here
	@NgayThucHien	DATETIME,
	@DmSanPhamREF	INT,
	@BannerType		INT,
	@DonViTinh		NVARCHAR(50)
	
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ResultValue INT
	DECLARE @DefaultDate DATETIME
	SET @DefaultDate = '3000-12-31' 

	SET @ResultValue = 0;
	
	IF @DonViTinh = 'CLICK' SET @DonViTinh = 'CPC'
	ELSE IF @DonViTinh = 'VIEW' SET @DonViTinh = 'CPM'
	
	SET @ResultValue = (
		SELECT TOP 1 A.DonGia
		FROM BangGiaSanPham A
		WHERE 1=1
			AND A.DmSanPhamREF		= @DmSanPhamREF
			AND A.DmBannerREF		= @BannerType
			AND A.DonViTinh	= @DonViTinh
			AND @NgayThucHien BETWEEN A.NgayHieuLuc AND ISNULL(A.NgayHetHieuLuc,@DefaultDate)
	)

	SET @ResultValue = (SELECT CASE WHEN @DonViTinh = 'CPC' THEN @ResultValue
								when @DonViTinh  = 'CPM' then @ResultValue/1000 
								ELSE 0
							END
		)
	-- Return the result of the function
	SET @ResultValue = ISNULL(@ResultValue,0)
	RETURN @ResultValue

END

```
