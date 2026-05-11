# Stored Procedure: `DmNghanhHang_GetByParentId`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:11:33.133000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.917000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ParentId` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[DmNghanhHang_GetByParentId]	
	@ParentId int
AS
BEGIN
	SELECT A.DmNghanhHangID, A.TenNghanhHang, A.DmNghanhHangREF,A.CreatedBy, convert(varchar, A.CreatedAt, 103) AS CreatedAt, A.LastModidfiedBy, convert(varchar, A.LastModifiedAt, 103) AS LastModifiedAt, A.DeletedStatus,A2.TenNghanhHang AS TenNghanhHangCha 
	FROM DmNghanhHang A
	LEFT JOIN DmNghanhHang A2
	ON A.DmNghanhHangREF =A2.DmNghanhHangID
	WHERE A.DmNghanhHangREF = @ParentId AND A.DeletedStatus = 0
	
	ORDER BY A.TenNghanhHang
END

```
