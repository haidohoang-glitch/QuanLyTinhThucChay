# Stored Procedure: `Temp_Get_List_Contract`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-07 14:18:31.453000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.090000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
--Temp_Get_List_Contract ''
--Temp_Get_List_Contract '162'
CREATE proc [dbo].[Temp_Get_List_Contract]
(
	@SoHopDong NVARCHAR(50)	
)
AS
BEGIN
	IF(@SoHopDong <> '')
		BEGIN
			SELECT TOP 20 * FROM (
				SELECT DISTINCT(A.HopDongID), A.SoHopDong FROM ThucChayDaTinh A					
				WHERE A.HopDongID > 0 AND A.SoHopDong LIKE '%' + @SoHopDong + '%'				
			) AS TBL
			ORDER BY SoHopDong			
		END
	ELSE
		BEGIN
			SELECT TOP 20 * FROM (
				SELECT DISTINCT(A.HopDongID), A.SoHopDong FROM ThucChayDaTinh A	
				WHERE A.HopDongID > 0
			) AS TBL		
			ORDER BY SoHopDong
		END		
END

```
