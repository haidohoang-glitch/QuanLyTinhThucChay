# Stored Procedure: `ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket_doannv`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-19 16:27:28.720000
- **Ngày sửa cuối**: 2015-06-20 10:14:03.367000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@TaiKhoan` | `nvarchar(100)` | No |
| `@DmSanPhamREFin` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--
/*	
	EXEC dbo.[ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket_haidh] '2015-06-16', '2015-06-16'
	
*/

CREATE PROCEDURE [dbo].[ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket_doannv]
	-- Add the parameters for the stored procedure here
	@StartDate datetime,
	@EndDate DATETIME,
	@TaiKhoan NVARCHAR(50),
	@DmSanPhamREFin INT 
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
			
    SET @NgayThucHien = @StartDate
    -- xóa dữ liêu
    --DELETE FROM ThucChayAdmarketOnline WHERE Convert(date,NgayThucHien) = @NgayThucHien
    --DELETE FROM ThucChayDaTinhAdmarket WHERE Convert(date,NgayThucHien) = @NgayThucHien AND DmHinhThucQuangCao <> 13
    --DELETE FROM HopDongAdmarketCanhBao WHERE Convert(date,NgayThucHien) = @NgayThucHien
    WHILE @NgayThucHien <= @EndDate
    BEGIN			
		PRINT 'NgayThucHien: ==='
		PRINT 'NgayThucHien: ' + convert(nvarchar(50),@NgayThucHien)
		PRINT 'NgayThucHien: ==='
		
		-- Backup online data before canculate 
		EXEC dbo.ThucChayAdmarketOnlineHistory_StoreHistoryByNgayThucHien @NgayThucHien
		
		-- Update trang thai hop dong canh bao
		--***HAIHD PHAI VIET LAI SP NAY VOI VIEC CHECK BALANCE USER
		EXEC dbo.ThucChayDaTinhAdmarket_UpdateHopDongCanhBao_haidh @NgayThucHien;
		
		--Insert data to ThucChaySelfServingUsers table
		--EXEC dbo.ThucChaySelfServingUsers_Insert_haidh @NgayThucHien, @NgayThucHien 
		
    	DECLARE record_cursor CURSOR FOR
   	
    	--//HAIDH MODIFIED
    	SELECT DISTINCT
    		tcau.DmSanPhamREF, tcau.TenSanPham, tcau.username, tcau.DonViTinh, tcau.DmViTriREF, tcau.TenViTri
    	FROM ThucChaySelfServingUsers tcau
    	INNER JOIN
    	(	
    		SELECT distinct hdct.TK_AdMarket FROM HopDong hd
    		INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
    		WHERE 1=1
    		AND hd.DeletedStatus = 0
    		AND hdct.DeletedStatus = 0
    		AND hd.TrangThaiHopDong <> 3
    		AND hdct.CreatedAt >= @NgayGioiHanTinh
    		AND CONVERT(DATE, hdct.CreatedAt) <= @NgayThucHien
    	)hd ON tcau.username = hd.TK_AdMarket AND tcau.DmSanPhamREF = tcau.DmSanPhamREF
    	WHERE tcau.NgayThucHien = @NgayThucHien
   		AND (tcau.[money] > 0 OR tcau.pro > 0)
   		AND tcau.username = @TaiKhoan
   		AND tcau.DmSanPhamREF = @DmSanPhamREFin
    		
    	
    	OPEN record_cursor
    	
    	-- Tinh Thuc chay theo tung tai khoan
    	FETCH NEXT FROM record_cursor INTO @DmSanPhamREF, @TenSanPham, @UserName, @DonViTinh, @DmViTriREF, @TenViTri
    	WHILE @@FETCH_STATUS = 0
    	BEGIN
    		
    		EXEC dbo.ThucChayDaTinh_InsertThucChayDaTinhAdmarket_haidh 
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
    	
    	
    	
    	-- Update gia tri thay doi
    	EXEC [dbo].[ThucChayDaTinhAdmarket_UpdateGiaTriThayDoi_doannv] @NgayThucHien,@TaiKhoan,@DmSanPhamREFin
    	
    	-- Chay khi phat sinh phan bo 
		EXEC dbo.ThucChayDaTinh_ExcReInsertThucChayDaTinhAdmarket_doannv @NgayThucHien,@TaiKhoan,@DmSanPhamREFin
		
		--Quet lai du lieu trong bang thuc chay online
		PRINT 'NgayThucHien***: ' + convert(nvarchar(50),@NgayThucHien)
		EXEC dbo.ThucChayDaTinh_ExcReInsertThucChayDaTinhAdmarketFromOnlineData_doannv @NgayThucHien,@TaiKhoan,@DmSanPhamREFin
		
		
		-- Insert data no contract
    	EXEC dbo.ThucChayDaTinhAdmarket_InsertThucChayNoContract_doannv @NgayThucHien,@TaiKhoan,@DmSanPhamREFin;
		-- Update gia tri thay doi
		--EXEC [dbo].[ThucChayDaTinhAdmarket_UpdateGiaTriThayDoi_haidh] @NgayThucHien
		---- Chay khi phat sinh phan bo 
		--EXEC dbo.ThucChayDaTinh_ExcReInsertThucChayDaTinhAdmarket_haidh @NgayThucHien
		---- Insert data no contract
		--EXEC dbo.ThucChayDaTinhAdmarket_InsertThucChayNoContract @NgayThucHien;
		
		-- Update ten san pham trong truong hop ten san pham null
		
		UPDATE ThucChayAdmarketOnline
		SET TenSanPham = CASE DmSanPhamREF 
								WHEN 144 THEN 'CPC Admarket' 
								WHEN 585 THEN 'AdX' 
								WHEN 628 THEN 'Viewplus'
						 END
		WHERE NgayThucHien = @NgayThucHien
			AND TenSanPham IS NULL
    	
    	SET @NgayThucHien = DATEADD(d,1,@NgayThucHien);
    END
END



```
