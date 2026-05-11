# Stored Procedure: `Insert_DoanhSoThucChayNhanHangCore`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-09-26 16:00:10.267000
- **Ngày sửa cuối**: 2016-09-26 16:00:10.267000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [Insert_DoanhSoThucChayNhanHangCore] '2016-09-20', '2016-09-20'

CREATE PROCEDURE [dbo].[Insert_DoanhSoThucChayNhanHangCore]
	@FromDate DATETIME,
	@ToDate DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @FromDate
	
	DELETE 
	FROM   DoanhSoThucChayNhanHangCore
	WHERE  NgayThucHien BETWEEN @FromDate AND @ToDate
	--AND HopDongID=42813
	
	WHILE (@NgayThucHien <= @ToDate)
	BEGIN
	    --INSERT DOANH SO THUC THU, KHUYEN MAI
	    EXEC dbo.Insert_DoanhSoThucChayNhanHangCore_ThucThuKhuyenMai @NgayThucHien
	    EXEC dbo.Insert_DoanhSoThucChayNhanHangCore_ThucThuKhuyenMai_BySanPham @NgayThucHien
	    ----INSERT DOANH SO NOI BO	
	    EXEC [Insert_DoanhSoThucChayNhanHangCore_NoiBo] @NgayThucHien
	    EXEC [Insert_DoanhSoThucChayNhanHangCore_NoiBo_BySanPham] @NgayThucHien
	    ----INSERT DOANH SO NHAN HANG KHONG HOP DONG
	    ----GET DOANH SO CUA NHANKHONG HOP DONG BEN THUCCHAYDATINH VOI SAN PHAM KHONGPHAI LA ADMARKET VA THUCCHAYDATINHADMARKET SAN PHAM LA ADMARKET
	    EXEC dbo.Insert_DoanhSoThucChayNhanHangCore_ThucThuKhuyenMai_KhongHD @NgayThucHien
	    EXEC dbo.Insert_DoanhSoThucChayNhanHangCore_NoiBo_KhongHD @NgayThucHien
	    PRINT @NgayThucHien
	    SET @NgayThucHien = DATEADD(DAY, 1, @NgayThucHien)
	END
	SELECT '2'
END

--EXEC [Insert_DoanhSoThucChayNhanHangCore] '2013-12-31', '2014-01-01'

```
