# Stored Procedure: `ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-10 18:18:37.923000
- **Ngày sửa cuối**: 2015-06-10 18:18:37.923000

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
--
/*	
	EXEC dbo.ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket '2015-03-24', '2015-03-24'
	
	EXEC dbo.ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket '2015-01-01', '2015-01-10'
	EXEC dbo.ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket '2015-01-11', '2015-01-20'
	EXEC dbo.ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket '2015-01-21', '2015-01-31'

	 EXEC dbo.ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket '2014-06-20', '2014-06-30'
	 EXEC dbo.ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket '2014-07-01', '2014-07-31'
	 EXEC dbo.ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket '2014-08-01', '2014-08-31'
	 EXEC dbo.ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket '2014-09-01', '2014-09-30'
	 EXEC dbo.ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket '2014-10-01', '2014-10-31'
	 EXEC dbo.ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket '2014-11-01', '2014-11-30'
	 EXEC dbo.ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket '2014-12-01', '2014-12-31'
	 
	 -- Insert data no contract
	 EXEC dbo.ThucChayDaTinhAdmarket_InsertThucChayNoContract '2015-01-02'
	
	 -- Update gia tri thay doi
	 EXEC [dbo].[ThucChayDaTinhAdmarket_UpdateGiaTriThayDoi] '2015-01-02'
	 
	 EXEC dbo.ThucChayDaTinh_ExcReInsertThucChayDaTinhAdmarket '2015-01-02'
	 
	 EXEC dbo.ThucChayDaTinh_ExcReInsertThucChayDaTinhAdmarketFromOnlineData '2015-01-02'
*/

CREATE PROCEDURE [dbo].[ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket1]
	-- Add the parameters for the stored procedure here
	@StartDate datetime,
	@EndDate datetime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @NgayThucHien		DATETIME,
			@NgayGioiHanTinh	DATETIME
    DECLARE @DmSanPhamREF INT,
			@TenSanPham		NVARCHAR(50),
			@UserName		NVARCHAR(50),
			@DonViTinh		NVARCHAR(50),
			@GhiChu			NVARCHAR(255),
			@DmViTriREF		INT,
			@TenViTri		NVARCHAR(50)
			
	SET @GhiChu = '';
			
	SET @NgayGioiHanTinh = '2013-01-01'
			
    
     --Xoa du lieu truoc khi insert neu da ton tai
     --DELETE FROM ThucChayDaTinhAdmarket WHERE NgayThucHien BETWEEN @StartDate AND @EndDate AND DmSanPhamREF IN (144, 299, 337, 585) --AND DangSuDung IN (5001, 5002, 5003)
    --DELETE FROM ThucChayDaTinhAdmarket WHERE NgayThucHien BETWEEN @StartDate AND @EndDate AND DmSanPhamREF IN (144, 299, 337)
    
    -- --Insert data to ThucChaySelfServingUsers table
    --EXEC dbo.ThucChaySelfServingUsers_Insert @StartDate, @EndDate 
    
    SET @NgayThucHien = @StartDate
    
    WHILE @NgayThucHien <= @EndDate
    BEGIN
		PRINT 'NgayThucHien: ==='
		PRINT 'NgayThucHien: ' + convert(nvarchar(50),@NgayThucHien)
		PRINT 'NgayThucHien: ==='
		
		-- Backup online data before canculate 
		EXEC dbo.ThucChayAdmarketOnlineHistory_StoreHistoryByNgayThucHien @NgayThucHien
		
		--Insert data to ThucChaySelfServingUsers table
		EXEC dbo.ThucChaySelfServingUsers_Insert @NgayThucHien, @NgayThucHien 
		
    	DECLARE record_cursor CURSOR FOR
    	SELECT DISTINCT
    		tcau.DmSanPhamREF, tcau.TenSanPham, tcau.username, tcau.DonViTinh, tcau.DmViTriREF, tcau.TenViTri
    	FROM ThucChaySelfServingUsers AS tcau
    		INNER JOIN HopDongChiTiet AS hdct ON hdct.TK_AdMarket = tcau.username
    		INNER JOIN HopDong AS hd ON hd.HopDongID = hdct.HopDongFK
    	WHERE tcau.NgayThucHien = @NgayThucHien
    		AND hdct.CreatedAt >= @NgayGioiHanTinh
    		AND CONVERT(DATE, hdct.CreatedAt) <= @NgayThucHien
    		AND hdct.DmSanPhamREF = tcau.DmSanPhamREF
    		AND (tcau.[money] > 0 OR tcau.pro > 0)
    	
    	OPEN record_cursor
    	
    	-- Tinh Thuc chay theo tung tai khoan
    	FETCH NEXT FROM record_cursor INTO @DmSanPhamREF, @TenSanPham, @UserName, @DonViTinh, @DmViTriREF, @TenViTri
    	WHILE @@FETCH_STATUS = 0
    	BEGIN
    		
    		EXEC dbo.ThucChayDaTinh_InsertThucChayDaTinhAdmarket 
    			@NgayThucHien, 
    			@DmSanPhamREF, 
    			@UserName,
    			@DonViTinh,
    			@GhiChu,
    			@DmViTriREF,
    			@TenViTri
    		
    		FETCH NEXT FROM record_cursor INTO @DmSanPhamREF, @TenSanPham, @UserName, @DonViTinh, @DmViTriREF, @TenViTri
    	END
    	CLOSE record_cursor;
    	DEALLOCATE record_cursor;
    	
    	-- Insert data no contract
    	EXEC dbo.ThucChayDaTinhAdmarket_InsertThucChayNoContract @NgayThucHien;
    	
    	-- Update gia tri thay doi
    	EXEC [dbo].[ThucChayDaTinhAdmarket_UpdateGiaTriThayDoi] @NgayThucHien
    	
    	-- Update Hop dong Huy trong ngay
    	EXEC dbo.ThucChayDaTinhAdmarket_UpdateHopDongHuy @NgayThucHien
    	
    	-- Chay khi phat sinh phan bo 
		EXEC dbo.ThucChayDaTinh_ExcReInsertThucChayDaTinhAdmarket @NgayThucHien
		
		-- Quet lai du lieu trong bang thuc chay online
		PRINT 'NgayThucHien***: ' + convert(nvarchar(50),@NgayThucHien)
		EXEC dbo.ThucChayDaTinh_ExcReInsertThucChayDaTinhAdmarketFromOnlineData @NgayThucHien
		
		-- Update ten san pham trong truong hop ten san pham null
		
		UPDATE ThucChayAdmarketOnline
		SET TenSanPham = CASE DmSanPhamREF 
								WHEN 144 THEN 'CPC Admarket' 
								WHEN 585 THEN 'AdX' 
						 END
		WHERE NgayThucHien = @NgayThucHien
			AND TenSanPham IS NULL
    	
    	SET @NgayThucHien = DATEADD(d,1,@NgayThucHien);
    END
    
    ---- Insert data no contract
    --EXEC dbo.ThucChayDaTinhAdmarket_InsertThucChayNoContract @StartDate, @EndDate
    
    --
  --  SET @NgayThucHien = @StartDate
    
  --  WHILE @NgayThucHien <= @EndDate
  --  BEGIN
		---- Chay khi phat sinh phan bo 
		--EXEC dbo.ThucChayDaTinh_ExcReInsertThucChayDaTinhAdmarket @NgayThucHien
		
		---- Quet lai du lieu trong bang thuc chay online
		--EXEC dbo.ThucChayDaTinh_ExcReInsertThucChayDaTinhAdmarketFromOnlineData @NgayThucHien
		
		---- Update ten san pham trong truong hop ten san pham null
		
		--UPDATE ThucChayAdmarketOnline
		--SET TenSanPham = CASE DmSanPhamREF 
		--						WHEN 144 THEN 'CPC Admarket' 
		--						WHEN 585 THEN 'AdX' 
		--				 END
		--WHERE NgayThucHien = @NgayThucHien
		--	AND TenSanPham IS NULL
		
		--SET @NgayThucHien = DATEADD(d,1,@NgayThucHien);
  --  END
    
    
    -- Update gia tri thay doi
    --EXEC [dbo].[ThucChayDaTinhAdmarket_UpdateGiaTriThayDoi] @StartDate, @EndDate
END

```
