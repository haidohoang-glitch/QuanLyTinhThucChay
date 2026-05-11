# Stored Procedure: `usp_PhanQuyenNhanHang_Delete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-29 16:38:50.587000
- **Ngày sửa cuối**: 2014-11-19 12:16:46.573000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmPhanQuyenID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_PhanQuyenNhanHang_Delete]
	@DmPhanQuyenID	INT
AS
BEGIN	
	DELETE FROM PhanQuyenNhanHang
	WHERE DmPhanQuyenID = @DmPhanQuyenID		
END

```
