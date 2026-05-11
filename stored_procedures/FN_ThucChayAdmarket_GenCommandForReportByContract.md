# Function: `ThucChayAdmarket_GenCommandForReportByContract`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-04-08 19:39:02.140000
- **Ngày sửa cuối**: 2014-10-14 10:39:28.903000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar` | Yes |
| `@SqlSecurityString` | `nvarchar` | No |
| `@SqlFilterString` | `nvarchar` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChayAdmarket_GenCommandForReportByContract]
(
	@SqlSecurityString nvarchar(max),
	@SqlFilterString nvarchar(max)
)
RETURNS nvarchar(max)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @SqlComnand nvarchar(max);
	DECLARE @DauNhay nvarchar(50) = '''';

	SET @SqlComnand = '
			SELECT DISTINCT
				SoHopDong AS Id,
				SoHopDong,
				NgayKyHopDong,
				DmPhongBanREF,
				DmBoPhanREF,
				DmNhomLamViecREF,			
				DmSanPhamREF, TenSanPham,
				DonViTinh,
				TongClick,
				TongView,
				CASE WHEN DmSanPhamREF = 337 THEN TongView
					ELSE TongClick
				END as SoLuongThucChay,
				TongTienThucChay, 
				TongTienKhuyenMai,
				NgayThucHien
			FROM ThucChayDaTinhAdmarketHopDong
			WHERE ' + @SqlSecurityString + @SqlFilterString + '
				AND DmSanPhamREF IN (144,299,337)
				AND (TongClick <> 0 OR TongTienThucChay <> 0 OR TongTienKhuyenmai <> 0) 
			'
	
	-- Return the result of the function
	RETURN @SqlComnand;

END


```
