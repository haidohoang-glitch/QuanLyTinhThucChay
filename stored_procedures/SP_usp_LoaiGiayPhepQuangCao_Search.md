# Stored Procedure: `usp_LoaiGiayPhepQuangCao_Search`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-22 09:41:51.077000
- **Ngày sửa cuối**: 2014-11-19 12:16:46.160000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenLoaiGiayPhep` | `nvarchar(510)` | No |
| `@PageIndex` | `int(4)` | No |
| `@PageSize` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_LoaiGiayPhepQuangCao_Search]
	@TenLoaiGiayPhep NVARCHAR(255),
	@PageIndex INT = 1,
	@PageSize INT = 2	
AS
BEGIN
	WITH cte AS (
				SELECT 
				ROW_NUMBER() OVER(ORDER BY [LastModifiedAt] DESC) AS [RowNumber]
				,DmLoaiGiayPhepID
				,TenLoaiGiayPhep
				,Ghichu
				,CONVERT(VARCHAR(10), LastModifiedAt, 103) AS  LastModifiedAt
				,LastModifiedBy
                FROM   DmLoaiGiayPhepQuangCao
				WHERE DeletedStatus <> 1 AND TenLoaiGiayPhep COLLATE  SQL_Latin1_General_CP1_CI_AI LIKE N'%'+@TenLoaiGiayPhep+'%'                
	)

	SELECT *,(SELECT COUNT(RowNumber) FROM cte) AS 'TotalRows' FROM cte c 
	WHERE RowNumber BETWEEN ((@PageIndex -1) * @PageSize + 1)  AND (@PageIndex * @PageSize);
END

```
