# Stored Procedure: `NhomQuyenChucNang_Delete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-15 03:16:04
- **Ngày sửa cuối**: 2015-03-15 03:16:04

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhomQuyenChucNangID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- ==========================================================================================
-- Entity Name: NhomQuyenChucNang_Delete
-- Author:  NhatMQ
-- Create date: 3/15/2015 3:15:27 AM
-- Description: This SP delete specify row from NhomQuyenChucNang table
-- ==========================================================================================


CREATE PROCEDURE NhomQuyenChucNang_Delete
    @NhomQuyenChucNangID int
AS
BEGIN

    UPDATE NhomQuyenChucNang 
    SET
        [RecordStatus] = 1
    WHERE 
        [NhomQuyenChucNangID] = @NhomQuyenChucNangID

END


```
