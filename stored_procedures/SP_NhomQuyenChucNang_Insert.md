# Stored Procedure: `NhomQuyenChucNang_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-15 03:16:03.363000
- **Ngày sửa cuối**: 2015-03-15 03:16:03.363000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhomQuyenREF` | `int(4)` | No |
| `@TenNhomQuyen` | `nvarchar(100)` | No |
| `@DmMenuREF` | `int(4)` | No |
| `@TenMenu` | `nvarchar(100)` | No |
| `@DmChucNangREFList` | `int(4)` | No |
| `@TenChucNangList` | `nvarchar(512)` | No |
| `@GhiChu` | `nvarchar(1024)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@LastModifiedBy` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- ==========================================================================================
-- Entity Name: NhomQuyenChucNang_Insert
-- Author:  NhatMQ
-- Create date: 3/15/2015 3:15:27 AM
-- Description: This SP Inserts value to NhomQuyenChucNang table
-- ==========================================================================================


CREATE PROCEDURE NhomQuyenChucNang_Insert
    @DmNhomQuyenREF int,
    @TenNhomQuyen nvarchar(50) = NULL,
    @DmMenuREF int,
    @TenMenu nvarchar(50) = NULL,
    @DmChucNangREFList int,
    @TenChucNangList nvarchar(256) = NULL,
    @GhiChu nvarchar(512) = NULL,
    @RecordStatus int,
    @DeletedStatus int,
    @PrintStatus int,
    @CreatedBy nvarchar(50) = NULL,
    @LastModifiedBy nvarchar(50) = NULL
AS
BEGIN

    INSERT INTO NhomQuyenChucNang
        ([DmNhomQuyenREF],
        [TenNhomQuyen],
        [DmMenuREF],
        [TenMenu],
        [DmChucNangREFList],
        [TenChucNangList],
        [GhiChu],
        [RecordStatus],
        [DeletedStatus],
        [PrintStatus],
        [CreatedAt],
        [CreatedBy],
        [LastModifiedAt],
        [LastModifiedBy])
    VALUES
        (@DmNhomQuyenREF,
        @TenNhomQuyen,
        @DmMenuREF,
        @TenMenu,
        @DmChucNangREFList,
        @TenChucNangList,
        @GhiChu,
        0,
        0,
        0,
        GETDATE(),
        @CreatedBy,
        GETDATE(),
        @LastModifiedBy)
END


```
