# Function: `GetDotDaChayHopDongChiTiet`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-28 16:15:41.407000
- **Ngày sửa cuối**: 2014-10-14 10:39:36.383000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetDotDaChayHopDongChiTiet]
(
	-- Add the parameters for the function here
	@HopDongChiTietID INT	
)
RETURNS NVARCHAR(4000)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result NVARCHAR(4000), @NgayThucHien DATETIME, @DateTemp DATETIME, @StartDate DATETIME, @Flat INT, @RecordCount INT, @i INT
	
	SET @RecordCount = (SELECT COUNT(*) FROM dbo.ThucChayDaTinh A WHERE A.HopDongChiTietREF = @HopDongChiTietID)
	
	
	DECLARE Record_Cursor CURSOR FOR        
 		SELECT A.NgayThucHien FROM dbo.ThucChayDaTinh A
		WHERE A.HopDongChiTietREF = @HopDongChiTietID	
		ORDER BY A.NgayThucHien ASC       
		
	OPEN Record_Cursor

	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor into @NgayThucHien	
	
	SET @Result = ''
	
	SET @DateTemp = @NgayThucHien
	SET @StartDate = @NgayThucHien
	
	SET @i+=1 
	
	WHILE @@FETCH_STATUS = 0
	BEGIN	
	SET @Flat = 1
	SET @i+=1
	SET @DateTemp = DATEADD(dd,1,@DateTemp)
	FETCH NEXT FROM Record_Cursor into @NgayThucHien	
	IF(@DateTemp <> @NgayThucHien)
		BEGIN
			SET @Result = @Result + CONVERT(NVARCHAR(50),@StartDate,103) + '-->' + CONVERT(NVARCHAR(50),DATEADD(dd,-1,@DateTemp),103) + ';'
			SET @StartDate = @NgayThucHien
			SET @DateTemp = @NgayThucHien
			IF(@i = @RecordCount) 
				SET @Flat = 1
			ELSE 
				SET @Flat = 0
		END	
	END
	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor
	
	IF(@Flat = 1)
	BEGIN
		IF(@DateTemp > @StartDate)
			SET @Result = @Result + CONVERT(NVARCHAR(50),@StartDate,103) + '-->' + CONVERT(NVARCHAR(50),@DateTemp,103)
		ELSE
			SET @Result = @Result + CONVERT(NVARCHAR(50),@StartDate,103)			
	END
	
	IF(@Result IS NULL) SET @Result = 'NA'
	-- Return the result of the function
	RETURN @Result

END

```
