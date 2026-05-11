# Stored Procedure: `PhanQuyenNhanHang_Search_TotalRow`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-22 17:22:26.360000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.960000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `nvarchar(8000)` | No |
| `@OxUserID` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<SonVM>
-- Create date: <22,05,2014>
-- Description:	<Description,,>
-- =============================================
-- PhanQuyenNhanHang_Search_TotalRow '', ''
CREATE PROCEDURE [dbo].[PhanQuyenNhanHang_Search_TotalRow]	
	@DmNhanHangID	NVARCHAR(4000),
	@OxUserID		NVARCHAR(4000)
AS
BEGIN	   
	DECLARE @Sql        NVARCHAR(4000) = '',				
			@Filter		NVARCHAR(4000) = '1=1',			
			@Params		NVARCHAR(4000),						
			@MaxRecords	INT												
    
    -- 1.1 Filter --	
    --====================================================================================================================================--							
    -- 1.1 DeleteStatus = 0 --	
    SET @Filter += ' AND A.DeletedStatus = 0'
    
    -- 1.2 DmNhanHangId --	
	IF (@DmNhanHangID IS NOT NULL AND @DmNhanHangID <> '')
		SET @Filter += ' AND B.DmNhanHangREF IN (' + @DmNhanHangID + ')'   
	
	-- 1.2 OxUserREF --	
	IF (@OxUserID IS NOT NULL AND @OxUserID <> '')
		SET @Filter += ' AND B.OxUserREF IN (' + @OxUserID + ')'
		 
	-- 2 Execute Query --		
	--====================================================================================================================================--							
	SELECT @Sql = '					
					SELECT @MaxRecords = COUNT(*) 
					FROM DmNhanHang A
					INNER JOIN PhanQuyenNhanHang B
						ON A.DmNhanHangID = B.DmNhanHangREF
					INNER JOIN AdminUser C
						ON B.OxUserREF = C.OxUserREF
					WHERE ' + @Filter																												
					
	PRINT (@Sql) 				
					  
	EXEC sp_executesql @Sql, @Params = N'@MaxRecords INT OUTPUT', @MaxRecords = @MaxRecords OUTPUT
    SELECT @MaxRecords AS MaxRecords								   
END

```
