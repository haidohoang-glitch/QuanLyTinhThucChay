# Stored Procedure: `usp_UpdateKhachHangThongTinLamViec`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:21.587000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.113000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangThongTinLamViecID` | `int(4)` | No |
| `@NgayLamViec` | `datetime(8)` | No |
| `@ThongTinCaNhanREF` | `int(4)` | No |
| `@KhachHangNguoiLienHeREF` | `int(4)` | No |
| `@MucDichCongViec` | `nvarchar(400)` | No |
| `@TieuDe` | `nvarchar(400)` | No |
| `@NoiDungLamViec` | `nvarchar(8000)` | No |
| `@DmMucDoUuTienREF` | `int(4)` | No |
| `@DmLoaiThongTinLamViecREF` | `int(4)` | No |
| `@DmLinhVucLamViecREF` | `int(4)` | No |
| `@DmTinhTrangLamViecREF` | `int(4)` | No |
| `@KetQua` | `nvarchar(400)` | No |
| `@NgayLamViecKeTiep` | `datetime(8)` | No |
| `@AttachFilename` | `nvarchar(400)` | No |
| `@AttachFilenameEncode` | `nvarchar(400)` | No |
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
-- Stored Procedure Name: [dbo].[usp_UpdateKhachHangThongTinLamViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateKhachHangThongTinLamViec]
	@KhachHangThongTinLamViecID int,
	@NgayLamViec datetime,
	@ThongTinCaNhanREF int,
	@KhachHangNguoiLienHeREF int,
	@MucDichCongViec nvarchar(200),
	@TieuDe nvarchar(200),
	@NoiDungLamViec nvarchar(4000),
	@DmMucDoUuTienREF int,
	@DmLoaiThongTinLamViecREF int,
	@DmLinhVucLamViecREF int,
	@DmTinhTrangLamViecREF int,
	@KetQua nvarchar(200),
	@NgayLamViecKeTiep datetime,
	@AttachFilename nvarchar(200),
	@AttachFilenameEncode nvarchar(200),
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

UPDATE [dbo].[KhachHangThongTinLamViec] SET
	[NgayLamViec] = @NgayLamViec,
	[ThongTinCaNhanREF] = @ThongTinCaNhanREF,
	[KhachHangNguoiLienHeREF] = @KhachHangNguoiLienHeREF,
	[MucDichCongViec] = @MucDichCongViec,
	[TieuDe] = @TieuDe,
	[NoiDungLamViec] = @NoiDungLamViec,
	[DmMucDoUuTienREF] = @DmMucDoUuTienREF,
	[DmLoaiThongTinLamViecREF] = @DmLoaiThongTinLamViecREF,
	[DmLinhVucLamViecREF] = @DmLinhVucLamViecREF,
	[DmTinhTrangLamViecREF] = @DmTinhTrangLamViecREF,
	[KetQua] = @KetQua,
	[NgayLamViecKeTiep] = @NgayLamViecKeTiep,
	[AttachFilename] = @AttachFilename,
	[AttachFilenameEncode] = @AttachFilenameEncode,
	[GhiChu] = @GhiChu,
	[Active] = @Active,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[KhachHangThongTinLamViecID] = @KhachHangThongTinLamViecID

--endregion

```
