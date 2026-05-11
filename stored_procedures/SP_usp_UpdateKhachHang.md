# Stored Procedure: `usp_UpdateKhachHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:20.013000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.660000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangID` | `int(4)` | No |
| `@MaKhachHang` | `nvarchar(100)` | No |
| `@ThongTinCaNhanREF` | `int(4)` | No |
| `@ThongTinToChucREF` | `int(4)` | No |
| `@DmHinhThucKhachHangREF` | `int(4)` | No |
| `@DmLoaiKhachHangREF` | `int(4)` | No |
| `@NguoiQuanLyREF` | `nvarchar(100)` | No |
| `@IsTruSoChinh` | `int(4)` | No |
| `@KhachHangREF` | `int(4)` | No |
| `@DmTrangThaiKhachHangREF` | `int(4)` | No |
| `@Level` | `int(4)` | No |
| `@QuyMoCongTy` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(8000)` | No |
| `@Active` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(2)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(2)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateKhachHang]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateKhachHang]
	@KhachHangID int,
	@MaKhachHang nvarchar(50),
	@ThongTinCaNhanREF int,
	@ThongTinToChucREF int,
	@DmHinhThucKhachHangREF int,
	@DmLoaiKhachHangREF int,
	@NguoiQuanLyREF nvarchar(50),
	@IsTruSoChinh int,
	@KhachHangREF int,
	@DmTrangThaiKhachHangREF int,
	@Level int,
	@QuyMoCongTy nvarchar(200),
	@GhiChu nvarchar(4000),
	@Active int,
	@CreatedBy nvarchar(1),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(1),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON

UPDATE [dbo].[KhachHang] SET
	[MaKhachHang] = @MaKhachHang,
	[ThongTinCaNhanREF] = @ThongTinCaNhanREF,
	[ThongTinToChucREF] = @ThongTinToChucREF,
	[DmHinhThucKhachHangREF] = @DmHinhThucKhachHangREF,
	[DmLoaiKhachHangREF] = @DmLoaiKhachHangREF,
	[NguoiQuanLyREF] = @NguoiQuanLyREF,
	[IsTruSoChinh] = @IsTruSoChinh,
	[KhachHangREF] = @KhachHangREF,
	[DmTrangThaiKhachHangREF] = @DmTrangThaiKhachHangREF,
	[Level] = @Level,
	[QuyMoCongTy] = @QuyMoCongTy,
	[GhiChu] = @GhiChu,
	[Active] = @Active,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[KhachHangID] = @KhachHangID

--endregion

```
