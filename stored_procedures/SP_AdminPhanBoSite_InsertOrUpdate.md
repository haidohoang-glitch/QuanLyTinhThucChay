# Stored Procedure: `AdminPhanBoSite_InsertOrUpdate`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 11:47:06.660000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.973000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuSoYeuLyLichID` | `int(4)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(200)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(200)` | No |
| `@DmLoaiDoiTuongREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-11-04
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[AdminPhanBoSite_InsertOrUpdate] 
	-- Add the parameters for the stored procedure here
	@NhanSuSoYeuLyLichID INT, 
	@TenDangNhap NVARCHAR(50),
	@DmSanPhamREF INT,
	@TenSanPham NVARCHAR(100),
	@DmWebsiteREF INT,
	@TenWebsite NVARCHAR(100),
	@DmLoaiDoiTuongREF INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	IF EXISTS (SELECT A.TenDangNhap FROM AdminBoPhanWebsite A WHERE A.TenDangNhap = @TenDangNhap 
																AND A.DmSanPhamREF = @DmSanPhamREF
																AND A.DmWebsiteREF = @DmWebsiteREF
																AND A.DmLoaiDoiTuongREF = @DmLoaiDoiTuongREF
				)
		UPDATE AdminBoPhanWebsite
		SET
			NhanSuSoYeuLyLichID = @NhanSuSoYeuLyLichID,
			TenDangNhap = @TenDangNhap,
			DmSanPhamREF = @DmSanPhamREF,
			TenSanPham = @TenSanPham,
			DmWebsiteREF = @DmWebsiteREF,
			TenWebsite = @TenWebsite,
			DmLoaiDoiTuongREF = @DmLoaiDoiTuongREF
	ELSE
		INSERT INTO AdminBoPhanWebsite
		 (
 			NhanSuSoYeuLyLichID,
 			TenDangNhap,
 			DmSanPhamREF,
 			TenSanPham,
 			DmWebsiteREF,
 			TenWebsite,
 			DmLoaiDoiTuongREF
		 )
		 VALUES
		 (
 			@NhanSuSoYeuLyLichID,
 			@TenDangNhap,
 			@DmSanPhamREF,
 			@TenSanPham,
 			@DmWebsiteREF,
 			@TenWebsite,
 			@DmLoaiDoiTuongREF
		 )
	 
END

```
