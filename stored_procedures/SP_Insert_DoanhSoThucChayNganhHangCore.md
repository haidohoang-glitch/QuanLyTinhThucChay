# Stored Procedure: `Insert_DoanhSoThucChayNganhHangCore`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-31 11:21:12.037000
- **Ngày sửa cuối**: 2015-03-31 11:21:12.037000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [Insert_DoanhSoThucChayNganhHangCore] '2013-12-01', '2014-03-01'

CREATE  PROCEDURE [dbo].[Insert_DoanhSoThucChayNganhHangCore] 
	@FromDate DATETIME,
	@ToDate DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @FromDate
	
	DELETE FROM DoanhSoThucChayNganhHangCore
	WHERE NgayThucHien BETWEEN @FromDate AND @ToDate
	
	WHILE(@NgayThucHien <= @ToDate)
	BEGIN
	--INSERT DOANH SO THUC THU, KHUYEN MAI
	EXEC [Insert_DoanhSoThucChayNganhHangCore_ThucThuKhuyenMai] @NgayThucHien
	EXEC [Insert_DoanhSoThucChayNganhHangCore_ThucThuKhuyenMai_BySanPham] @NgayThucHien
	--INSERT DOANH SO NOI BO	
	EXEC Insert_DoanhSoThucChayNganhHangCore_NoiBo @NgayThucHien
	EXEC Insert_DoanhSoThucChayNganhHangCore_NoiBo_BySanPham @NgayThucHien
	--INSERT DOANH SO THUC THU VA KHUYEN MAI NGANH HANG HOP DONG ONLINE
	EXEC [Insert_DoanhSoThucChayNganhHangCore_ThucThuKhuyenMai_KhongHD] @NgayThucHien
	EXEC [Insert_DoanhSoThucChayNganhHangCore_NoiBo_KhongHD] @NgayThucHien
	PRINT @NgayThucHien
	SET @NgayThucHien = DATEADD(DAY,1,@NgayThucHien)
	END
	SELECT '2'
END

--EXEC [Insert_DoanhSoThucChayNganhHangCore] '2013-12-31', '2014-01-01'

```
