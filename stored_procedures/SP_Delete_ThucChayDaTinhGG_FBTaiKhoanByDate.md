# Stored Procedure: `Delete_ThucChayDaTinhGG_FBTaiKhoanByDate`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-10 15:33:55.383000
- **Ngày sửa cuối**: 2015-04-22 12:04:43.393000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@TaiKhoan` | `nvarchar(400)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
	EXEC [dbo].[Delete_ThucChayDaTinhGG_FBTaiKhoanByDate] '2015-04-13', 'Vietjet_Dai Loan'
*/
CREATE PROCEDURE [dbo].[Delete_ThucChayDaTinhGG_FBTaiKhoanByDate]
-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@TaiKhoan NVARCHAR(200),
	@DmSanPhamREF INT
AS
BEGIN
	--XOA SAN PHAM CHINH CUAR GG VA FB
	DELETE ThucChayDaTinh	 FROM ThucChayDaTinh 
	INNER JOIN HopDongChiTiet ON ThucChayDaTinh.HopDongChiTietREF = HopDongChiTiet.HopDongChiTietID
	WHERE ThucChayDaTinh.DmSanPhamREF = @DmSanPhamREF
	AND ThucChayDaTinh.NgayThucHien =@NgayThucHien
	AND HopDongChiTiet.TK_AdMarket = @TaiKhoan


	--XOA DU LIEU CHI PHI
	DELETE ThucChayDaTinh	 FROM ThucChayDaTinh 
	INNER JOIN HopDongChiTiet ON ThucChayDaTinh.HopDongChiTietREF = HopDongChiTiet.HopDongChiTietID
	WHERE ThucChayDaTinh.DmSanPhamREF IN (535)
	AND ThucChayDaTinh.NgayThucHien =@NgayThucHien
	AND HopDongChiTiet.TK_AdMarket = @TaiKhoan
	AND ThucChayDaTinh.TenWebsite IN ('google.com.vn','facebook.com')
	
	--UPDATE TRANG THAI DU LIEU ONLINE CUA NGAY THUC HIEN
	UPDATE ThucChayGoogleFacebookOnline
	SET	RecordStatus = 0
	WHERE CONVERT(DATE,LastModifiedAt) 	= @NgayThucHien
	AND TaiKhoan = @TaiKhoan
	AND DmSanPhamREF = @DmSanPhamREF
	
	--XOA DU LIEU ONLINE
	DELETE FROM ThucChayGoogleFacebookOnline
	WHERE CONVERT(DATE,NgayThucHien)= @NgayThucHien
	AND TaiKhoan = @TaiKhoan
	AND DmSanPhamREF = @DmSanPhamREF
		
END

```
