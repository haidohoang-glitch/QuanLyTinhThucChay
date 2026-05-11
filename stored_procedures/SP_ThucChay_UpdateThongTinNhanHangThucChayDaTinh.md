# Stored Procedure: `ThucChay_UpdateThongTinNhanHangThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:26:31.770000
- **Ngày sửa cuối**: 2016-03-17 16:10:16.163000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_UpdateThongTinNhanHangThucChayDaTinh] 
	@NgayThucHien DATETIME
AS
BEGIN
	--ThucChayDatinh
	UPDATE ThucChayDaTinh
	SET NhanHang=  ISNULL((
						SELECT hdct.DanhSachNhanHangREF FROM HopDongChiTiet hdct
						WHERE hdct.HopDongChiTietID = HopDongChiTietREF
					),'0')
	WHERE NgayThucHien = @NgayThucHien
	AND isnumeric(NhanHang) = 0
	
	--ThucChayDaTinhAdmarket
	UPDATE ThucChayDaTinhAdmarket
	SET NhanHang=  ISNULL((
						SELECT hdct.DanhSachNhanHangREF FROM HopDongChiTiet hdct
						WHERE hdct.HopDongChiTietID = HopDongChiTietREF
					),'0')
	WHERE NgayThucHien = @NgayThucHien
	AND isnumeric(NhanHang) = 0
	SELECT 2
END

--EXEC [ThucChay_UpdateThongTinNhanHangThucChayDaTinh] '2013-09-20'

```
