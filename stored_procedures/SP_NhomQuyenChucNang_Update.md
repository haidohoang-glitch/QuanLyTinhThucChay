# Stored Procedure: `NhomQuyenChucNang_Update`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-15 03:16:03.790000
- **Ngày sửa cuối**: 2015-03-15 03:16:03.790000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhomQuyenChucNangID` | `int(4)` | No |
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
| `@LastModifiedBy` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- ==========================================================================================
-- Entity Name: NhomQuyenChucNang_Update
-- Author:  NhatMQ
-- Create date: 3/15/2015 3:15:27 AM
-- Description: This SP updates NhomQuyenChucNang table rows.
-- ==========================================================================================


CREATE PROCEDURE NhomQuyenChucNang_Update
    @NhomQuyenChucNangID int,
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
    @LastModifiedBy nvarchar(50) = NULL
AS
BEGIN

UPDATE NhomQuyenChucNang 
SET 
    [DmNhomQuyenREF] = @DmNhomQuyenREF,
    [TenNhomQuyen] = @TenNhomQuyen,
    [DmMenuREF] = @DmMenuREF,
    [TenMenu] = @TenMenu,
    [DmChucNangREFList] = @DmChucNangREFList,
    [TenChucNangList] = @TenChucNangList,
    [GhiChu] = @GhiChu,
    [RecordStatus] = @RecordStatus,
    [DeletedStatus] = @DeletedStatus,
    [PrintStatus] = @PrintStatus,
    [LastModifiedAt] = GETDATE(),
    [LastModifiedBy] = @LastModifiedBy 
WHERE 
    [NhomQuyenChucNangID] = @NhomQuyenChucNangID

END


```
