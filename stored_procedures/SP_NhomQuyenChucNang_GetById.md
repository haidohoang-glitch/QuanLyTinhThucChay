# Stored Procedure: `NhomQuyenChucNang_GetById`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-15 03:16:03.117000
- **Ngày sửa cuối**: 2015-03-15 03:16:03.117000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhomQuyenChucNangID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- ==========================================================================================
-- Entity Name: NhomQuyenChucNang_GetById
-- Author:  NhatMQ
-- Create date: 3/15/2015 3:15:27 AM
-- Description: This SP select a specify row from NhomQuyenChucNang
-- ==========================================================================================


CREATE PROCEDURE NhomQuyenChucNang_GetById
    @NhomQuyenChucNangID int
AS
BEGIN

    SELECT 
        [NhomQuyenChucNangID],
        [DmNhomQuyenREF],
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
        [LastModifiedBy] 
    FROM NhomQuyenChucNang 
    WHERE 
        [NhomQuyenChucNangID] = @NhomQuyenChucNangID 
        AND [DeletedStatus] = 0

END


```
