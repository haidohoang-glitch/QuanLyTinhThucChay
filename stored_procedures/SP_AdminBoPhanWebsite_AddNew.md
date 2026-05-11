# Stored Procedure: `AdminBoPhanWebsite_AddNew`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 11:47:06.223000
- **Ngày sửa cuối**: 2014-11-19 12:16:49.153000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminBoPhanWebsiteID` | `int(4)` | No |
| `@NhanSuSoYeuLyLichID` | `int(4)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(100)` | No |
| `@DmLoaiDoiTuongREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-24
-- Description:	<Description,,>
-- =============================================

--
-- [dbo].[AdminBoPhanWebsite_AddNew] 0,946,'admin',531,N'CPM Multi',0,'',1
--
CREATE PROCEDURE [dbo].[AdminBoPhanWebsite_AddNew]
	-- Add the parameters for the stored procedure here
	@AdminBoPhanWebsiteID INT,
	@NhanSuSoYeuLyLichID int,
	@TenDangNhap nvarchar(50),
	@DmSanPhamREF int,
	@TenSanPham nvarchar(50),
	@DmWebsiteREF int,
	@TenWebsite nvarchar(50),
	@DmLoaiDoiTuongREF int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	IF EXISTS (SELECT TenDangNhap FROM AdminBoPhanWebsite A 
	           WHERE A.AdminBoPhanWebsiteID = @AdminBoPhanWebsiteID )
		UPDATE AdminBoPhanWebsite
		SET
			DmSanPhamREF = @DmSanPhamREF,
			TenSanPham = @TenSanPham,
			DmWebsiteREF = @DmWebsiteREF,
			TenWebsite = @TenWebsite,
			DmLoaiDoiTuongREF = @DmLoaiDoiTuongREF
		WHERE
			AdminBoPhanWebsiteID = @AdminBoPhanWebsiteID
	ELSE
		INSERT INTO [dbo].[AdminBoPhanWebsite]
			   ([NhanSuSoYeuLyLichID]
			   ,[TenDangNhap]
			   ,[DmSanPhamREF]
			   ,[TenSanPham]
			   ,[DmWebsiteREF]
			   ,[TenWebsite]
			   ,[DmLoaiDoiTuongREF])
		 VALUES
			   (@NhanSuSoYeuLyLichID
			   ,@TenDangNhap
			   ,@DmSanPhamREF
			   ,@TenSanPham
			   ,@DmWebsiteREF
			   ,@TenWebsite
			   ,@DmLoaiDoiTuongREF
			   )
END

```
