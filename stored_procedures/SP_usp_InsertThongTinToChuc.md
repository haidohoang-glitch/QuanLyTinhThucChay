# Stored Procedure: `usp_InsertThongTinToChuc`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:25.437000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.703000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThongTinToChucID` | `int(4)` | No |
| `@MaThongTinToChuc` | `nvarchar(100)` | No |
| `@TenToChuc` | `nvarchar(400)` | No |
| `@GiayPhepKinhDoanh` | `nvarchar(100)` | No |
| `@NgayThanhLap` | `datetime(8)` | No |
| `@NoiCapGiayPhepKinhDoanh` | `nvarchar(400)` | No |
| `@MaSoThue` | `nvarchar(100)` | No |
| `@DienThoai` | `nvarchar(100)` | No |
| `@Fax` | `nvarchar(100)` | No |
| `@Email` | `nvarchar(400)` | No |
| `@Website` | `nvarchar(400)` | No |
| `@DmLoaiToChucREF` | `int(4)` | No |
| `@DiaChiREF` | `int(4)` | No |
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
-- Stored Procedure Name: [dbo].[usp_InsertThongTinToChuc]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_InsertThongTinToChuc]
	@ThongTinToChucID int,
	@MaThongTinToChuc nvarchar(50),
	@TenToChuc nvarchar(200),
	@GiayPhepKinhDoanh nvarchar(50),
	@NgayThanhLap datetime,
	@NoiCapGiayPhepKinhDoanh nvarchar(200),
	@MaSoThue nvarchar(50),
	@DienThoai nvarchar(50),
	@Fax nvarchar(50),
	@Email nvarchar(200),
	@Website nvarchar(200),
	@DmLoaiToChucREF int,
	@DiaChiREF int,
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

INSERT INTO [dbo].[ThongTinToChuc] (
	[ThongTinToChucID],
	[MaThongTinToChuc],
	[TenToChuc],
	[GiayPhepKinhDoanh],
	[NgayThanhLap],
	[NoiCapGiayPhepKinhDoanh],
	[MaSoThue],
	[DienThoai],
	[Fax],
	[Email],
	[Website],
	[DmLoaiToChucREF],
	[DiaChiREF],
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
	@ThongTinToChucID,
	@MaThongTinToChuc,
	@TenToChuc,
	@GiayPhepKinhDoanh,
	@NgayThanhLap,
	@NoiCapGiayPhepKinhDoanh,
	@MaSoThue,
	@DienThoai,
	@Fax,
	@Email,
	@Website,
	@DmLoaiToChucREF,
	@DiaChiREF,
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
