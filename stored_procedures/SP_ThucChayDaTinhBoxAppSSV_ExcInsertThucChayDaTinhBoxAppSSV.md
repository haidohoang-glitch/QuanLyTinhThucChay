# Stored Procedure: `ThucChayDaTinhBoxAppSSV_ExcInsertThucChayDaTinhBoxAppSSV`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-24 14:20:34.363000
- **Ngày sửa cuối**: 2014-11-19 12:17:00.197000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinhBoxAppSSV_ExcInsertThucChayDaTinhBoxAppSSV]
	-- Add the parameters for the stored procedure here
	@StartDate	DATETIME,
	@EndDate	DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @NgayThucHien DATETIME;
    DECLARE @DmSanPhamREF INT,
			@TenSanPham		NVARCHAR(50),
			@Domain			NVARCHAR(50),
			@UserName		NVARCHAR(50)
			
    
    -- Xoa du lieu truoc khi insert neu da ton tai
    --DELETE FROM ThucChayDaTinhAdmarket WHERE NgayThucHien BETWEEN @StartDate AND @EndDate AND DmSanPhamREF = 375 and DmHinhThucQuangCao = 26
    
    SET @NgayThucHien = @StartDate
    
    WHILE @NgayThucHien <= @EndDate
    BEGIN
    	DECLARE record_cursor CURSOR FOR
    	SELECT tcau.DmSanPhamREF, tcau.TenSanPham, tcau.Domain, tcau.username
    	FROM ThucChayAdmarketUsers AS tcau
    		INNER JOIN HopDongChiTiet AS hdct ON hdct.TK_AdMarket = tcau.username
    	WHERE tcau.NgayThucHien = @NgayThucHien
    		AND (tcau.[money] > 0 OR tcau.pro > 0)
    	
    	OPEN record_cursor
    	
    	FETCH NEXT FROM record_cursor INTO @DmSanPhamREF, @TenSanPham, @Domain, @UserName
    	WHILE @@FETCH_STATUS = 0
    	BEGIN
    		EXEC dbo.ThucChayDaTinh_InsertThucChayDaTinhAdmarket 
    			@NgayThucHien, 
    			@DmSanPhamREF, 
    			@UserName,
    			@Domain
    		
    		FETCH NEXT FROM record_cursor INTO @DmSanPhamREF, @TenSanPham, @Domain, @UserName
    	END
    	CLOSE record_cursor;
    	DEALLOCATE record_cursor;
    	
    	SET @NgayThucHien = DATEADD(d,1,@NgayThucHien);
    END
END

```
