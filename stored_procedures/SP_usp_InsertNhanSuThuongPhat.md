# Stored Procedure: `usp_InsertNhanSuThuongPhat`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:22.880000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.477000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuThuongPhatID` | `int(4)` | No |
| `@DmNhanSuLoaiThuongPhat` | `int(4)` | No |
| `@SoHieu` | `nvarchar(100)` | No |
| `@NgayDuyet` | `datetime(8)` | No |
| `@NguoiDuyet` | `nvarchar(100)` | No |
| `@NgayBanHanh` | `datetime(8)` | No |
| `@QuyetDinhFileName` | `nvarchar(400)` | No |
| `@QuyetDinhFIleNameEncode` | `nvarchar(400)` | No |
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
-- Stored Procedure Name: [dbo].[usp_InsertNhanSuThuongPhat]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_InsertNhanSuThuongPhat]
	@NhanSuThuongPhatID int,
	@DmNhanSuLoaiThuongPhat int,
	@SoHieu nvarchar(50),
	@NgayDuyet datetime,
	@NguoiDuyet nvarchar(50),
	@NgayBanHanh datetime,
	@QuyetDinhFileName nvarchar(200),
	@QuyetDinhFIleNameEncode nvarchar(200),
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

INSERT INTO [dbo].[NhanSuThuongPhat] (
	[NhanSuThuongPhatID],
	[DmNhanSuLoaiThuongPhat],
	[SoHieu],
	[NgayDuyet],
	[NguoiDuyet],
	[NgayBanHanh],
	[QuyetDinhFileName],
	[QuyetDinhFIleNameEncode],
	[GhiChu],
	[Active],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
) VALUES (
	@NhanSuThuongPhatID,
	@DmNhanSuLoaiThuongPhat,
	@SoHieu,
	@NgayDuyet,
	@NguoiDuyet,
	@NgayBanHanh,
	@QuyetDinhFileName,
	@QuyetDinhFIleNameEncode,
	@GhiChu,
	@Active,
	@CreatedBy,
	@CreatedAt,
	@LastModifiedBy,
	@LastModifiedAt,
	@DeletedStatus,
	@PrintStatus,
	@RecordStatus
)

--endregion

```
