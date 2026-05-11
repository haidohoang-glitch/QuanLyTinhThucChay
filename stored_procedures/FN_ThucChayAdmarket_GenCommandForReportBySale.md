# Function: `ThucChayAdmarket_GenCommandForReportBySale`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-12-25 17:19:23.893000
- **Ngày sửa cuối**: 2014-10-14 10:39:28.873000

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
CREATE FUNCTION [dbo].[ThucChayAdmarket_GenCommandForReportBySale]
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
			SELECT distinct
				TenDangNhap,
				TenNhanVien,
				DmPhongBanREF,
				DmBoPhanREF,
				DmNhomLamViecREF,
				dbo.AdmarketGetListIDViTriLamViecByNhanVien(DmPhongBanREF, DmBoPhanREF, DmNhomLamViecREF) AS PhongBoPhanNhomID,
				dbo.AdmarketGetViTriLamViecByNhanVien(TenPhongBan, TenBoPhan, TenNhomLamViec) AS PhongBoPhanNhom,
				DmSanPhamREF, TenSanPham,'
				+ @DauNhay + '' +@DauNhay + ' AS NgayKyHopDong,
				TongClick,
				TongView,
				TongTienThucChay, 
				TongTienKhuyenMai,
				NgayThucHien
			FROM ThucChayDaTinhAdmarketSale
			WHERE DmSanPhamREF IN (144,299,337) AND (TongClick <> 0 OR TongView <> 0 OR TongTienThucChay <> 0 OR TongTienKhuyenMai <> 0) AND ' + @SqlSecurityString + @SqlFilterString
	
	-- Return the result of the function
	RETURN @SqlComnand;

END

```
