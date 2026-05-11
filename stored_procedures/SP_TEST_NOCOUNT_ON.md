# Stored Procedure: `TEST_NOCOUNT_ON`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-10-01 09:01:58.853000
- **Ngày sửa cuối**: 2016-10-01 09:22:40.937000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: 01/12/2015
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[TEST_NOCOUNT_ON] 
AS
BEGIN
	
	--SELECT 
	--FROM dbo.DmSanPham

	
	

		declare @start datetime2
	set @start = SYSDATETIME()
	
	
	--SELECT * FROM ( 
	--  SELECT *, ROW_NUMBER() OVER (ORDER BY HopDongID) as row FROM dbo.ThucChayDaTinh
	-- ) a WHERE row >= 1 and row <= 200


		SELECT  *
	FROM     dbo.ThucChayDaTinh
	ORDER BY HopDongID 
	OFFSET  1 ROWS 
	FETCH NEXT 200 ROWS ONLY 

	select datediff(ms,@start, sysdatetime()) as 'insert into memory-optimized table using native compilation (in ms)'
	--SELECT * FROM dbo.DmSanPham LIMIT 10,20

	--	SELECT  *
	--FROM     dbo.ThucChayDaTinh
	--ORDER BY HopDongID 
	--OFFSET  1 ROWS 
	--FETCH NEXT 200 ROWS ONLY 
END

```
