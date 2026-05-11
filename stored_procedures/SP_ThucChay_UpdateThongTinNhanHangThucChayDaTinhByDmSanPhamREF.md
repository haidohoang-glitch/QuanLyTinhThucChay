# Stored Procedure: `ThucChay_UpdateThongTinNhanHangThucChayDaTinhByDmSanPhamREF`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-18 14:42:16.020000
- **Ngày sửa cuối**: 2016-03-18 14:42:16.020000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_UpdateThongTinNhanHangThucChayDaTinhByDmSanPhamREF] 
	@NgayThucHien DATETIME,
	@DmSanPhamREF INT
AS
BEGIN
	--ThucChayDatinh
	IF @DmSanPhamREF NOT IN (144,628,585,420,337)
	BEGIN
			UPDATE ThucChayDaTinh
	SET NhanHang=  ISNULL((
						SELECT hdct.DanhSachNhanHangREF FROM HopDongChiTiet hdct
						WHERE hdct.HopDongChiTietID = HopDongChiTietREF
					),'0')
	WHERE NgayThucHien = @NgayThucHien
	AND isnumeric(NhanHang) = 0
	AND DmSanPhamREF = @DmSanPhamREF
	END

	ELSE
	BEGIN
	--ThucChayDaTinhAdmarket
	UPDATE ThucChayDaTinhAdmarket
	SET NhanHang=  ISNULL((
						SELECT hdct.DanhSachNhanHangREF FROM HopDongChiTiet hdct
						WHERE hdct.HopDongChiTietID = HopDongChiTietREF
					),'0')
	WHERE NgayThucHien = @NgayThucHien
	AND isnumeric(NhanHang) = 0
	AND dbo.ThucChayDaTinhAdmarket.DmSanPhamREF = @DmSanPhamREF
	END
	SELECT 2
END

--EXEC [ThucChay_UpdateThongTinNhanHangThucChayDaTinh] '2013-09-20'

```
