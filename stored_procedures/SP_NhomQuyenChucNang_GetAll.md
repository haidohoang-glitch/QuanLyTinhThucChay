# Stored Procedure: `NhomQuyenChucNang_GetAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-15 03:16:02.520000
- **Ngày sửa cuối**: 2015-03-15 03:16:02.520000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Keyword` | `nvarchar(1024)` | No |

## Definition (Source Code)

```sql

-- ==========================================================================================
-- Entity Name: NhomQuyenChucNang_GetAll
-- Author:  NhatMQ
-- Create date: 3/15/2015 3:15:27 AM
-- Description: Select all rows form NhomQuyenChucNang
-- ==========================================================================================



CREATE PROCEDURE NhomQuyenChucNang_GetAll
    @Keyword NVARCHAR(512)
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
        [DeletedStatus] = 0 
        AND [TenNhomQuyen] LIKE @Keyword + '%'

END


```
