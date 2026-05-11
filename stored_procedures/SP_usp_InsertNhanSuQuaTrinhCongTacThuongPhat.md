# Stored Procedure: `usp_InsertNhanSuQuaTrinhCongTacThuongPhat`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:22.403000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.950000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuQuaTrinhCongTacThuongPhatID` | `int(4)` | No |
| `@NhanSuSoYeuLyLichREF` | `int(4)` | No |
| `@SoHieu` | `nvarchar(100)` | No |
| `@GhiChu` | `nvarchar(8000)` | No |
| `@Active` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_InsertNhanSuQuaTrinhCongTacThuongPhat]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_InsertNhanSuQuaTrinhCongTacThuongPhat]
	@NhanSuQuaTrinhCongTacThuongPhatID int,
	@NhanSuSoYeuLyLichREF int,
	@SoHieu nvarchar(50),
	@GhiChu nvarchar(4000),
	@Active int,
	@CreatedBy nvarchar(50),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(50),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON
IF(EXISTS(SELECT * FROM dbo.NhanSuQuaTrinhCongTacThuongPhat WHERE NhanSuQuaTrinhCongTacThuongPhatID = @NhanSuQuaTrinhCongTacThuongPhatID))
UPDATE [dbo].[NhanSuQuaTrinhCongTacThuongPhat] SET
	[NhanSuSoYeuLyLichREF] = @NhanSuSoYeuLyLichREF,
	[SoHieu] = @SoHieu,
	[GhiChu] = @GhiChu,
	[Active] = @Active,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[NhanSuQuaTrinhCongTacThuongPhatID] = @NhanSuQuaTrinhCongTacThuongPhatID
else
INSERT INTO [dbo].[NhanSuQuaTrinhCongTacThuongPhat] (
	[NhanSuQuaTrinhCongTacThuongPhatID],
	[NhanSuSoYeuLyLichREF],
	[SoHieu],
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
	@NhanSuQuaTrinhCongTacThuongPhatID,
	@NhanSuSoYeuLyLichREF,
	@SoHieu,
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
