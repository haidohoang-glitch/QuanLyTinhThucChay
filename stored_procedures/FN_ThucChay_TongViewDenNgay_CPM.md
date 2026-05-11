# Function: `ThucChay_TongViewDenNgay_CPM`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-07-13 09:07:22.577000
- **Ngày sửa cuối**: 2014-10-14 10:39:29.067000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmSanPham` | `int(4)` | No |
| `@DmHopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_TongViewDenNgay_CPM]
(
	@NgayThucHien DATETIME,
	@SoHopDong NVARCHAR(50),
	@DmSanPham INT,
	@DmHopDongChiTietID INT
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here

	DECLARE @TongViewThucChay BigINT
	SET @TongViewThucChay = (
			SELECT CONVERT(BIGINT,SUM(isnull(TongViewThucChay,0))) FROM ThucChayDaTinh
			WHERE SoHopDong = @SoHopDong
			AND DmSanPhamREF = @DmSanPham
			AND HopDongChiTietREF = @DmHopDongChiTietID
			AND Convert(date,NgayThucHien) <=@NgayThucHien
	)

	RETURN @TongViewThucChay;

END

```
