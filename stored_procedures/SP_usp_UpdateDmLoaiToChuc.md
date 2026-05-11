# Stored Procedure: `usp_UpdateDmLoaiToChuc`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:08.310000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.303000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmLoaiToChucID` | `int(4)` | No |
| `@MaLoaiToChuc` | `nvarchar(100)` | No |
| `@TenLoaiToChuc` | `nvarchar(400)` | No |
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
-- Stored Procedure Name: [dbo].[usp_UpdateDmLoaiToChuc]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateDmLoaiToChuc]
	@DmLoaiToChucID int,
	@MaLoaiToChuc nvarchar(50),
	@TenLoaiToChuc nvarchar(200),
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

UPDATE [dbo].[DmLoaiToChuc] SET
	[MaLoaiToChuc] = @MaLoaiToChuc,
	[TenLoaiToChuc] = @TenLoaiToChuc,
	[GhiChu] = @GhiChu,
	[Active] = @Active,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[DmLoaiToChucID] = @DmLoaiToChucID

--endregion

```
