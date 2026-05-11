# Stored Procedure: `ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarketByAccountFixNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-09 18:07:55.757000
- **Ngày sửa cuối**: 2015-04-07 12:38:03.960000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@account` | `nvarchar(100)` | No |
| `@sanPhamId` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@TenViTri` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--
/*
	EXEC dbo.ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarketByAccountFixNgayThucHien 
		'2015-03-27',
		'2015-03-31', 		
		'sand',
		585,
		'2015-04-03',
		1,
		''
		
		
	--EXEC dbo.ThucChayDaTinhAdmarket_InsertThucChayNoContract '2014-12-31';

*/

CREATE PROCEDURE [dbo].[ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarketByAccountFixNgayThucHien]
	-- Add the parameters for the stored procedure here
	@StartDate datetime,
	@EndDate datetime,
	@account nvarchar(50),
	@sanPhamId	int,
	@NgayThucHien	DATETIME,
	@DmViTriREF		INT,
	@TenViTri		NVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE 
			@NgayGioiHanTinh	DATETIME
    DECLARE @DmSanPhamREF INT,
			@TenSanPham		NVARCHAR(50),
			@UserName		NVARCHAR(50),
			@DonViTinh		NVARCHAR(50),
			@GhiChu			NVARCHAR(255)
			--@DmViTriREF		INT,
			--@TenViTri		NVARCHAR(50)
			
	SET @GhiChu = '';
			
	SET @NgayGioiHanTinh = '2013-01-01'
			
    
     --Xoa du lieu truoc khi insert neu da ton tai
     --DELETE FROM ThucChayDaTinhAdmarket WHERE NgayThucHien BETWEEN @StartDate AND @EndDate AND DmSanPhamREF IN (144, 299, 337, 585) --AND DangSuDung IN (5001, 5002, 5003)
    --DELETE FROM ThucChayDaTinhAdmarket WHERE NgayThucHien BETWEEN @StartDate AND @EndDate AND DmSanPhamREF IN (144, 299, 337)
    
    -- --Insert data to ThucChaySelfServingUsers table
    --EXEC dbo.ThucChaySelfServingUsers_Insert @StartDate, @EndDate 
    
    --SET @NgayThucHien = @StartDate
    
    --WHILE @NgayThucHien <= @EndDate
    BEGIN
		PRINT 'NgayThucHien: ==='
		PRINT 'NgayThucHien: ' + convert(nvarchar(50),@NgayThucHien)
		PRINT 'NgayThucHien: ==='
		
		--Insert data to ThucChaySelfServingUsers table
		EXEC dbo.ThucChaySelfServingUsers_InsertByAccountAndProduct
			@startDate,
			@endDate, 
			@NgayThucHien,
			@account,
			@sanPhamId,
			@DmViTriREF,
			@TenViTri
		
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
    	
  --  	-- Update gia tri thay doi
  --  	EXEC [dbo].[ThucChayDaTinhAdmarket_UpdateGiaTriThayDoi] @NgayThucHien
    	
  --  	-- Chay khi phat sinh phan bo 
		--EXEC dbo.ThucChayDaTinh_ExcReInsertThucChayDaTinhAdmarket @NgayThucHien
		
		---- Quet lai du lieu trong bang thuc chay online
		--PRINT 'NgayThucHien***: ' + convert(nvarchar(50),@NgayThucHien)
		--EXEC dbo.ThucChayDaTinh_ExcReInsertThucChayDaTinhAdmarketFromOnlineData @NgayThucHien
		
		---- Update ten san pham trong truong hop ten san pham null
		
		UPDATE ThucChayAdmarketOnline
		SET TenSanPham = CASE DmSanPhamREF 
								WHEN 144 THEN 'CPC Admarket' 
								WHEN 585 THEN 'AdX' 
						 END
		WHERE NgayThucHien = @NgayThucHien
			AND TenSanPham IS NULL
    	
    	SET @NgayThucHien = DATEADD(d,1,@NgayThucHien);
    END
END

```
