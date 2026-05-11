# Stored Procedure: `Delete_ThucChayDaTinhGG_FBByDate`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-10 15:46:24.780000
- **Ngày sửa cuối**: 2015-04-10 15:46:31.840000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
	EXEC [dbo].[Delete_ThucChayDaTinhGG_FBByDate] '2015-03-16'
*/
CREATE PROCEDURE [dbo].[Delete_ThucChayDaTinhGG_FBByDate]
-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	--XOA SAN PHAM CHINH CUAR GG VA FB
	delete FROM ThucChayDaTinh 
	WHERE DmSanPhamREF IN (306,423)
	AND NgayThucHien =@NgayThucHien

	--XOA DU LIEU CHI PHI
	delete FROM ThucChayDaTinh 
	WHERE DmSanPhamREF IN (535)
	AND NgayThucHien = @NgayThucHien
	AND TenWebsite IN ('google.com.vn','facebook.com')
	
	--UPDATE TRANG THAI DU LIEU ONLINE CUA NGAY THUC HIEN
	UPDATE ThucChayGoogleFacebookOnline
	SET	RecordStatus = 0
	WHERE CONVERT(DATE,LastModifiedAt) 	= @NgayThucHien
	
	--XOA DU LIEU ONLINE
	DELETE FROM ThucChayGoogleFacebookOnline
	WHERE CONVERT(DATE,NgayThucHien)= @NgayThucHien
		
END

```
