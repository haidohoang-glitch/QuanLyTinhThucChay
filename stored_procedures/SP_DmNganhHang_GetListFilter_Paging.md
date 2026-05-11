# Stored Procedure: `DmNganhHang_GetListFilter_Paging`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:11:33.887000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.507000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenNghanhHang` | `nvarchar(100)` | No |
| `@NganhHangChaId` | `int(4)` | No |
| `@PageIndex` | `int(4)` | No |
| `@PageSize` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[DmNganhHang_GetListFilter_Paging] 

 @TenNghanhHang NVARCHAR(50) = '', 
 @NganhHangChaId INT =0, 
 @PageIndex INT =1,
 @PageSize INT 

AS
BEGIN

DECLARE @lbound INT, @ubound INT    
  
SET @PageIndex = ABS(@PageIndex)
SET @PageSize = ABS(@PageSize)

IF @PageIndex < 1 SET @PageIndex = 1
IF @PageSize  < 1 SET @PageSize = 1

SET @lbound = ((@PageIndex - 1) * @PageSize)
SET @ubound = @lbound + @PageSize

	SELECT * FROM(
	SELECT ROW_NUMBER() OVER(ORDER BY A.DmNghanhHangID DESC) AS TT, A.DmNghanhHangID, A.TenNghanhHang, A.DmNghanhHangREF,A.CreatedBy, convert(varchar, A.CreatedAt, 103) AS CreatedAt, A.LastModidfiedBy, convert(varchar, A.LastModifiedAt, 103) AS LastModifiedAt, A.DeletedStatus,A2.TenNghanhHang AS TenNghanhHangCha
	FROM DmNghanhHang A
	LEFT JOIN DmNghanhHang A2
	ON A.DmNghanhHangREF =A2.DmNghanhHangID
	WHERE 
	(@TenNghanhHang = ''  OR A.DmNghanhHangID IN (SELECT * FROM   dbo.Split(@TenNghanhHang, ',')))
	
	AND ((@NganhHangChaId =0) OR A.DmNghanhHangREF =@NganhHangChaId )
	AND A.DeletedStatus = 0 AND A.DmNghanhHangREF = 0
	
	)as TT 
 
	WHERE TT.tt BETWEEN @lbound AND @ubound 
	ORDER BY TT.TenNghanhHang
END

```
