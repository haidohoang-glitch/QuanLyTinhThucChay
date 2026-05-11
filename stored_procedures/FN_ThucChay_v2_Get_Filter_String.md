# Function: `ThucChay_v2_Get_Filter_String`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-05-14 09:53:14.267000
- **Ngày sửa cuối**: 2014-10-14 10:39:29.003000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@AdvertisingType` | `nvarchar(8000)` | No |
| `@LstProduct` | `nvarchar(8000)` | No |
| `@LstBanner` | `nvarchar(8000)` | No |
| `@LstContract` | `nvarchar(8000)` | No |
| `@LstCustomer` | `nvarchar(8000)` | No |
| `@LstUnit` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<SonVM>
-- Create date: <14, 05 ,2014>
-- Description:	<Trả về chuỗi điều kiện tìm kiếm>
-- Example	  : SELECT dbo.ThucChay_v2_Get_Filter_String('2014-05-10', '2014-05-10', NULL, NULL, NULL, NULL, NULL)
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_v2_Get_Filter_String] 
(
	@StartDate			DATETIME,
	@EndDate			DATETIME,
	@AdvertisingType	NVARCHAR(4000) = NULL,
	@LstProduct			NVARCHAR(4000) = NULL,
	@LstBanner			NVARCHAR(4000) = NULL,
	@LstContract		NVARCHAR(4000) = NULL,
	@LstCustomer		NVARCHAR(4000) = NULL,
	@LstUnit			NVARCHAR(4000) = NULL
)
RETURNS NVARCHAR(4000)
AS
BEGIN	
	DECLARE @Filter		NVARCHAR(4000)	= '',			
			@Sign		NVARCHAR(10)	= ''''				
	
	-- 1.1 Thời gian --
	Set @Filter += 'CONVERT(DATE, A.NgayThucHien) Between ' + 
						@Sign + CONVERT(NVARCHAR(30), @StartDate) + @Sign + ' AND ' + 
						@Sign + CONVERT(NVARCHAR(30), @EndDate)+ @Sign
							
	-- 1.2 Hình thức quảng cáo --	
	IF (@AdvertisingType IS NOT NULL AND @AdvertisingType <> '' AND @AdvertisingType <> '-1')
		SET @Filter += ' AND A.DmHinhThucQuangCao IN (' + @AdvertisingType + ')'
	
	-- 1.3 Sản phẩm --	
	IF (@LstProduct IS NOT NULL AND @LstProduct <> '')
		SET @Filter += ' AND A.DmSanPhamREF IN (' + @LstProduct + ')'	
		
	-- 1.4 Banner --		
	IF (@LstBanner IS NOT NULL AND @LstBanner <> '')
		SET @Filter += ' AND A.DmViTriREF IN (' + @LstBanner + ')'	
		
	-- 1.5 Số hợp đồng --	
	IF (@LstContract IS NOT NULL AND @LstContract <> '')
		SET @Filter += ' AND A.HopDongId IN (' + @LstContract + ')'
		
	-- 1.6 Khách hàng --	
	IF (@LstCustomer IS NOT NULL AND @LstCustomer <> '')
		SET @Filter += ' AND B.DmKhachHangREF IN (' + @LstCustomer + ')'
	
	-- 1.7 Ngành --	
	
	-- 1.8 Đơn vị --	
	IF (@LstUnit IS NOT NULL AND @LstUnit <> '')
		SET @Filter += ' AND A.DonViTinh IN (' + @LstUnit + ')'
	
	-- Return the result of the function
	RETURN @Filter	
END

```
