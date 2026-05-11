# Stored Procedure: `ThucChayDaTinhAdmarket_CanDoiOnline`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-07-09 14:49:15.237000
- **Ngày sửa cuối**: 2015-07-11 11:29:36.960000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TaiKhoan` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
-- ThucChayDaTinhAdmarket_CanDoiOnline 'gapit1',585
CREATE PROCEDURE [dbo].[ThucChayDaTinhAdmarket_CanDoiOnline]
	-- Add the parameters for the stored procedure here
	@TaiKhoan NVARCHAR(50),
	@DmSanPhamREF INT 
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	DECLARE @NgayGioiHanTinh DATETIME
	SET @NgayGioiHanTinh = '2014-01-01'
	DECLARE @HopDongID INT, @HopDongChiTietID INT, @SoHopDong NVARCHAR(50)
	-- theo san pham 144 chua quan tam den vi tri 
	DECLARE @ThucChay144DaTinh  FLOAT =0, @SoLuong144DaTinh INT =0
	DECLARE @ThucChay144User FLOAT =0, @SoLuong144User INT =0
	DECLARE @ThucChay144Online FLOAT =0, @SoLuong144Online INT =0
	
	DECLARE @ThucChay144DaTinhKM  FLOAT =0, @SoLuong144DaTinhKM INT =0
	DECLARE @ThucChay144UserKM FLOAT =0, @SoLuong144UserKM INT =0
	DECLARE @ThucChay144OnlineKM FLOAT =0, @SoLuong144OnlineKM INT =0
	-- 585
	DECLARE @ThucChay585DaTinh FLOAT =0, @SoLuong585DaTinh INT=0
	DECLARE @ThucChay585User FLOAT=0, @SoLuong585User INT=0
	DECLARE @ThucChay585Online FLOAT=0, @SoLuong585Online INT=0
	-- 628
	DECLARE @ThucChay628DaTinh FLOAT=0, @SoLuong628DaTinh INT=0
	DECLARE @ThucChay628User FLOAT=0, @SoLuong628User INT=0
	DECLARE @ThucChay628Online FLOAT=0, @SoLuong628Online INT=0
	
	DECLARE @ThucChay628DaTinhKM FLOAT=0, @SoLuong628DaTinhKM INT=0
	DECLARE @ThucChay628UserKM FLOAT=0, @SoLuong628UserKM INT=0
	DECLARE @ThucChay628OnlineKM FLOAT=0, @SoLuong628OnlineKM INT=0
    -- Insert statements for procedure here
    -- Thuc chay 144
    IF(@DmSanPhamREF = 144)
    BEGIN
    	
    SET @ThucChay144User = (SELECT isnull(sum(tcau.[money])/1.1,0)
                            FROM ThucChayAdmarketUsers tcau 
                            WHERE tcau.username = @TaiKhoan
    AND tcau.DmSanPhamREF = 144)
    PRINT('ThucChay theo user tra ve -'+ @TaiKhoan+'-144-'+  convert(CHAR(100),@ThucChay144User))
    
	SET @SoLuong144User = (SELECT isnull(sum(tcau.ttc/(tcau.[money] + tcau.pro) * tcau.[money]),0)
                            FROM ThucChayAdmarketUsers tcau 
                            WHERE tcau.username = @TaiKhoan
    AND tcau.DmSanPhamREF = 144 
	AND (tcau.[money] > 0 OR tcau.pro > 0))
     PRINT('SoLuong theo user tra ve -'+ @TaiKhoan+'-144-'+  convert(CHAR(100),@SoLuong144User))
    
    SET @ThucChay144DaTinh = (SELECT SUM(tcdta.ThanhTienSauTrietKhauThucChay + tcdta.GiaTriThayDoi) 
                              FROM ThucChayDaTinhAdmarket tcdta INNER JOIN HopDong hd
                              ON hd.HopDongID = tcdta.HopDongID
                              WHERE tcdta.DmSanPhamREF = 144 
                              AND hd.Nam >=2014
                              AND tcdta.NgayThucHien >=@NgayGioiHanTinh
                              AND tcdta.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID
                                                                FROM HopDongChiTiet hdct WHERE hdct.TK_AdMarket = @TaiKhoan
																AND hdct.DmSanPhamREF = 144
                              AND hdct.ChietKhau <> 100))
     PRINT('ThucChay da tinh tra ve -'+ @TaiKhoan+'-144-'+  convert(CHAR(100),@ThucChay144DaTinh))
    SET @SoLuong144DaTinh = (SELECT SUM(tcdta.SoLuongThucChay + tcdta.SoLuongThayDoi) 
                              FROM ThucChayDaTinhAdmarket tcdta INNER JOIN HopDong hd
                              ON hd.HopDongID= tcdta.HopDongID
                              WHERE tcdta.DmSanPhamREF = 144 
                              AND hd.Nam>=2014
                              AND tcdta.NgayThucHien >=@NgayGioiHanTinh
                              AND tcdta.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID
                                                                FROM HopDongChiTiet hdct WHERE hdct.TK_AdMarket = @TaiKhoan
																AND hdct.DmSanPhamREF = 144
																AND hdct.ChietKhau <> 100))    
     PRINT('SoLuong da tinh tra ve -'+ @TaiKhoan+'-144-'+  convert(CHAR(100),@SoLuong144DaTinh))      
     IF(round(@ThucChay144User - @ThucChay144DaTinh,-1)>0 OR round(@SoLuong144User - @SoLuong144DaTinh,-1) > 0)                         
    BEGIN
    UPDATE ThucChayAdmarketOnline  SET RecordStatus = 1 
    WHERE TaiKhoan = @TaiKhoan
    AND DmSanPhamREF = 144 AND TienThucChay > 0
    AND RecordStatus =0
    PRINT 'Insert thuc chay online';		
		INSERT INTO [dbo].[ThucChayAdmarketOnline]
			   ([ThucChayAdmarketOnlineID]
			   ,[DmSanPhamREF]
			   ,[TenSanPham]
			   ,[TaiKhoan]
			   ,[TotalView]
			   ,[TotalClick]
			   ,[SoLuong]
			   ,[DonViTinh]
			   ,[TienThucChay]
			   ,[TienKhuyenMai]
			   ,[NgayThucHien]
			   ,[IsNoiBo]
			   ,[GhiChu]
			   ,[RecordStatus]
			   ,[CreatedAt]
			   ,[CreatedBy]
			   ,[LastModifiedAt]
			   ,[LastModifiedBy]
			   ,[DmViTriREF]
			   ,[TenViTri])
		 VALUES
			   (
				NEWID()
			   ,144
			   ,'CPC Admarket'
			   ,@TaiKhoan
			   ,0
			   ,0
			   ,@SoLuong144User - @SoLuong144DaTinh
			   ,'CLICK'
			   ,@ThucChay144User - @ThucChay144DaTinh
			   ,0
			   ,GETDATE()
			   ,0
			   ,''
			   ,0
			   ,GETDATE()
			   ,'asd'
			   ,GETDATE()
			   ,'asd'
			   ,1
			   ,''
			   )   
			       	
    END
     -- Khuyen mai 144
    SET @ThucChay144UserKM = (SELECT isnull(sum(tcau.pro)/1.1,0)
                            FROM ThucChayAdmarketUsers tcau 
                            WHERE tcau.username = @TaiKhoan
    AND tcau.DmSanPhamREF = 144)
    PRINT('Khuyen mai theo user tra ve -'+ @TaiKhoan+'-144-'+  convert(CHAR(100),@ThucChay144UserKM))
    
	SET @SoLuong144UserKM = (SELECT isnull(sum(tcau.ttc/(tcau.[money] + tcau.pro) * tcau.pro),0)
                            FROM ThucChayAdmarketUsers tcau 
                            WHERE tcau.username = @TaiKhoan
    AND tcau.DmSanPhamREF = 144 
	AND (tcau.[money] > 0 OR tcau.pro > 0))
     PRINT('SoLuong km theo user tra ve -'+ @TaiKhoan+'-144-'+  convert(CHAR(100),@SoLuong144UserKM))
    
    SET @ThucChay144DaTinhKM = (SELECT SUM(tcdta.ThanhTienKM + tcdta.GiaTriKMThayDoi) 
                              FROM ThucChayDaTinhAdmarket tcdta INNER JOIN HopDong hd
                              ON hd.HopDongID = tcdta.HopDongID
                              WHERE tcdta.DmSanPhamREF = 144 
                              AND hd.Nam >=2014
                              AND tcdta.NgayThucHien >=@NgayGioiHanTinh
                              AND tcdta.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID
                                                                FROM HopDongChiTiet hdct WHERE hdct.TK_AdMarket = @TaiKhoan
																AND hdct.DmSanPhamREF = 144
                              AND hdct.ChietKhau <> 100))
     PRINT('ThucChayKM da tinh tra ve -'+ @TaiKhoan+'-144-'+  convert(CHAR(100),@ThucChay144DaTinhKM))
    SET @SoLuong144DaTinhKM = (SELECT SUM(tcdta.SoLuongThucChayKM + tcdta.SoLuongKMThayDoi) 
                              FROM ThucChayDaTinhAdmarket tcdta INNER JOIN HopDong hd
                              ON hd.HopDongID= tcdta.HopDongID
                              WHERE tcdta.DmSanPhamREF = 144 
                              AND hd.Nam>=2014
                              AND tcdta.NgayThucHien >=@NgayGioiHanTinh
                              AND tcdta.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID
                                                                FROM HopDongChiTiet hdct WHERE hdct.TK_AdMarket = @TaiKhoan
																AND hdct.DmSanPhamREF = 144
																AND hdct.ChietKhau <> 100))    
     PRINT('SoLuongKM da tinh tra ve -'+ @TaiKhoan+'-144-'+  convert(CHAR(100),@SoLuong144DaTinh))      
     IF(round(@ThucChay144UserKM - @ThucChay144DaTinhKM,-1)>0 OR round(@SoLuong144UserKM - @SoLuong144DaTinhKM,-1) > 0)                         
    BEGIN
    UPDATE ThucChayAdmarketOnline  SET RecordStatus = 1 
    WHERE TaiKhoan = @TaiKhoan
    AND DmSanPhamREF = 144 AND TienKhuyenMai > 0
    AND RecordStatus =0
    PRINT 'Insert thuc chay online';		
		INSERT INTO [dbo].[ThucChayAdmarketOnline]
			   ([ThucChayAdmarketOnlineID]
			   ,[DmSanPhamREF]
			   ,[TenSanPham]
			   ,[TaiKhoan]
			   ,[TotalView]
			   ,[TotalClick]
			   ,[SoLuong]
			   ,[DonViTinh]
			   ,[TienThucChay]
			   ,[TienKhuyenMai]
			   ,[NgayThucHien]
			   ,[IsNoiBo]
			   ,[GhiChu]
			   ,[RecordStatus]
			   ,[CreatedAt]
			   ,[CreatedBy]
			   ,[LastModifiedAt]
			   ,[LastModifiedBy]
			   ,[DmViTriREF]
			   ,[TenViTri])
		 VALUES
			   (
				NEWID()
			   ,144
			   ,'CPC Admarket'
			   ,@TaiKhoan
			   ,0
			   ,0
			   ,@SoLuong144UserKM - @SoLuong144DaTinhKM
			   ,'CLICK'
			   ,0
			   ,@ThucChay144UserKM - @ThucChay144DaTinhKM
			   ,GETDATE()
			   ,0
			   ,''
			   ,0
			   ,GETDATE()
			   ,'asd'
			   ,GETDATE()
			   ,'asd'
			   ,1
			   ,''
			   )   
			       	
    END
    END
    IF(@DmSanPhamREF = 628)
    BEGIN
    	
	-- Thuc chay 628
    SET @ThucChay628User = (SELECT isnull(sum(tcau.[money]/1.1),0)
                            FROM ThucChayViewPlusForUsers tcau 
                            WHERE tcau.username = @TaiKhoan
    AND tcau.DmSanPhamREF = 628)
    PRINT('ThucChay theo user tra ve -'+ @TaiKhoan+'-628-'+  convert(CHAR(100),@ThucChay628User))
    
	SET @SoLuong628User = (SELECT isnull(sum(tcau.ttc/(tcau.[money] + tcau.pro) * tcau.[money]),0)
                            FROM ThucChayViewPlusForUsers tcau 
                            WHERE tcau.username = @TaiKhoan
    AND tcau.DmSanPhamREF = 628 
	AND (tcau.[money] > 0 OR tcau.pro > 0))
     PRINT('SoLuong theo user tra ve -'+ @TaiKhoan+'-628-'+  convert(CHAR(100),@SoLuong628User))
    
    SET @ThucChay628DaTinh = (SELECT SUM(tcdta.ThanhTienSauTrietKhauThucChay + tcdta.GiaTriThayDoi) 
                              FROM ThucChayDaTinhAdmarket tcdta INNER JOIN HopDong hd
                              ON hd.HopDongID = tcdta.HopDongID
                              WHERE tcdta.DmSanPhamREF = 628 
                              AND hd.Nam >=2014
                              AND tcdta.NgayThucHien >=@NgayGioiHanTinh
                              AND tcdta.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID
                                                                FROM HopDongChiTiet hdct WHERE hdct.TK_AdMarket = @TaiKhoan
																AND hdct.DmSanPhamREF = 628
																AND hdct.ChietKhau <> 100))
     PRINT('ThucChay da tinh tra ve -'+ @TaiKhoan+'-628-'+  convert(CHAR(100),@ThucChay628DaTinh))
    SET @SoLuong628DaTinh = (SELECT SUM(tcdta.SoLuongThucChay + tcdta.SoLuongThayDoi) 
                              FROM ThucChayDaTinhAdmarket tcdta INNER JOIN HopDong hd
                              ON hd.HopDongID= tcdta.HopDongID
                              WHERE tcdta.DmSanPhamREF = 628 
                              AND hd.Nam>=2014
                              AND tcdta.NgayThucHien >=@NgayGioiHanTinh
                              AND tcdta.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID
                                                                FROM HopDongChiTiet hdct WHERE hdct.TK_AdMarket = @TaiKhoan
																AND hdct.DmSanPhamREF = 628
																AND hdct.ChietKhau <> 100))    
     PRINT('SoLuong da tinh tra ve -'+ @TaiKhoan+'-628-'+  convert(CHAR(100),@SoLuong628DaTinh))      
     IF(round(@ThucChay628User - @ThucChay628DaTinh,-1)>0 OR round(@SoLuong628User - @SoLuong628DaTinh,-1) > 0)                         
    BEGIN
    UPDATE ThucChayAdmarketOnline  SET RecordStatus = 1 
    WHERE TaiKhoan = @TaiKhoan
    AND DmSanPhamREF = 628 AND TienThucChay > 0
    AND RecordStatus =0
    PRINT 'Insert thuc chay online';		
		INSERT INTO [dbo].[ThucChayAdmarketOnline]
			   ([ThucChayAdmarketOnlineID]
			   ,[DmSanPhamREF]
			   ,[TenSanPham]
			   ,[TaiKhoan]
			   ,[TotalView]
			   ,[TotalClick]
			   ,[SoLuong]
			   ,[DonViTinh]
			   ,[TienThucChay]
			   ,[TienKhuyenMai]
			   ,[NgayThucHien]
			   ,[IsNoiBo]
			   ,[GhiChu]
			   ,[RecordStatus]
			   ,[CreatedAt]
			   ,[CreatedBy]
			   ,[LastModifiedAt]
			   ,[LastModifiedBy]
			   ,[DmViTriREF]
			   ,[TenViTri])
		 VALUES
			   (
				NEWID()
			   ,628
			   ,'ViewPlus'
			   ,@TaiKhoan
			   ,0
			   ,0
			   ,@SoLuong628User - @SoLuong628DaTinh
			   ,'CLICK'
			   ,@ThucChay628User - @ThucChay628DaTinh
			   ,0
			   ,GETDATE()
			   ,0
			   ,''
			   ,0
			   ,GETDATE()
			   ,'asd'
			   ,GETDATE()
			   ,'asd'
			   ,1
			   ,''
			   )   
    END
    -- Khuyen mai 628 
    SET @ThucChay628UserKM = (SELECT isnull(sum(tcau.pro/1.1),0)
                            FROM ThucChayViewPlusForUsers tcau 
                            WHERE tcau.username = @TaiKhoan
    AND tcau.DmSanPhamREF = 628)
    PRINT('Khuyen mai theo user tra ve -'+ @TaiKhoan+'-628-'+  convert(CHAR(100),@ThucChay628UserKM))
    
	SET @SoLuong628UserKM = (SELECT isnull(sum(tcau.ttc/(tcau.[money] + tcau.pro) * tcau.pro),0)
                            FROM ThucChayViewPlusForUsers tcau 
                            WHERE tcau.username = @TaiKhoan
    AND tcau.DmSanPhamREF = 628 
	AND (tcau.[money] > 0 OR tcau.pro > 0))
     PRINT('SoLuong k m theo user tra ve -'+ @TaiKhoan+'-628-'+  convert(CHAR(100),@SoLuong628UserKM))
    
    SET @ThucChay628DaTinhKM = (SELECT SUM(tcdta.ThanhTienKM + tcdta.GiaTriKMThayDoi) 
                              FROM ThucChayDaTinhAdmarket tcdta INNER JOIN HopDong hd
                              ON hd.HopDongID = tcdta.HopDongID
                              WHERE tcdta.DmSanPhamREF = 628 
                              AND hd.Nam >=2014
                              AND tcdta.NgayThucHien >=@NgayGioiHanTinh
                              AND tcdta.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID
                                                                FROM HopDongChiTiet hdct WHERE hdct.TK_AdMarket = @TaiKhoan
																AND hdct.DmSanPhamREF = 628
																AND hdct.ChietKhau <> 100))
     PRINT('km da tinh tra ve -'+ @TaiKhoan+'-628-'+  convert(CHAR(100),@ThucChay628DaTinh))
    SET @SoLuong628DaTinhKM = (SELECT SUM(tcdta.SoLuongKMThayDoi + tcdta.SoLuongThucChayKM) 
                              FROM ThucChayDaTinhAdmarket tcdta INNER JOIN HopDong hd
                              ON hd.HopDongID= tcdta.HopDongID
                              WHERE tcdta.DmSanPhamREF = 628 
                              AND hd.Nam>=2014
                              AND tcdta.NgayThucHien >=@NgayGioiHanTinh
                              AND tcdta.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID
                                                                FROM HopDongChiTiet hdct WHERE hdct.TK_AdMarket = @TaiKhoan
																AND hdct.DmSanPhamREF = 628
																AND hdct.ChietKhau <> 100))    
     PRINT('SoLuong km da tinh tra ve -'+ @TaiKhoan+'-628-'+  convert(CHAR(100),@SoLuong628DaTinh))      
     IF(round(@ThucChay628UserKM - @ThucChay628DaTinhKM,-1)>0 OR round(@SoLuong628UserKM - @SoLuong628DaTinhKM,-1) > 0)                         
    BEGIN
	UPDATE ThucChayAdmarketOnline  SET RecordStatus = 1 
    WHERE TaiKhoan = @TaiKhoan
    AND DmSanPhamREF = 628 AND TienKhuyenMai > 0
    AND RecordStatus =0
    PRINT 'Insert thuc chay online';		
		INSERT INTO [dbo].[ThucChayAdmarketOnline]
			   ([ThucChayAdmarketOnlineID]
			   ,[DmSanPhamREF]
			   ,[TenSanPham]
			   ,[TaiKhoan]
			   ,[TotalView]
			   ,[TotalClick]
			   ,[SoLuong]
			   ,[DonViTinh]
			   ,[TienThucChay]
			   ,[TienKhuyenMai]
			   ,[NgayThucHien]
			   ,[IsNoiBo]
			   ,[GhiChu]
			   ,[RecordStatus]
			   ,[CreatedAt]
			   ,[CreatedBy]
			   ,[LastModifiedAt]
			   ,[LastModifiedBy]
			   ,[DmViTriREF]
			   ,[TenViTri])
		 VALUES
			   (
				NEWID()
			   ,628
			   ,'ViewPlus'
			   ,@TaiKhoan
			   ,0
			   ,0
			   ,@SoLuong628UserKM - @SoLuong628DaTinhKM
			   ,'CLICK'
			   ,0
			   ,@ThucChay628UserKM - @ThucChay628DaTinhKM
			   ,GETDATE()
			   ,0
			   ,''
			   ,0
			   ,GETDATE()
			   ,'asd'
			   ,GETDATE()
			   ,'asd'
			   ,1
			   ,''
			   )   
    END
    END
    IF(@DmSanPhamREF =585)
    BEGIN
    	
    -- san pham 585 khac biet do vitri 
    DECLARE @DmViTriREF INT, @TenViTri NVARCHAR(50)
    DECLARE db_cursor CURSOR FOR  
	SELECT distinct hdct.DmViTriREF,hdct.TenViTri FROM ThucChayAdXForUsers hdct
	WHERE hdct.username = @TaiKhoan
	AND hdct.DmSanPhamREF = @DmSanPhamREF
	AND hdct.CreatedAt >='2014-01-01'

	OPEN db_cursor   
	FETCH NEXT FROM db_cursor INTO @DmviTriREF,@TenViTri   

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
	-- Thuc chay 585
    SET @ThucChay585User = (SELECT isnull(sum(tcau.[money])/1.1,0)
                            FROM ThucChayAdXForUsers tcau 
                            WHERE tcau.username = @TaiKhoan
    AND tcau.DmSanPhamREF = 585
    AND tcau.DmViTriREF = @DmViTriREF)
    PRINT('ThucChay theo user tra ve -'+ @TaiKhoan+'-585-'+  convert(CHAR(100),@ThucChay585User))
    
	SET @SoLuong585User = (SELECT isnull(sum(tcau.ttc/(tcau.[money] + tcau.pro) * tcau.[money]),0)
                            FROM ThucChayAdXForUsers tcau 
                            WHERE tcau.username = @TaiKhoan
    AND tcau.DmSanPhamREF = 585 
    AND tcau.DmViTriREF = @DmViTriREF
	AND (tcau.[money] > 0 OR tcau.pro > 0))
     PRINT('SoLuong theo user tra ve -'+ @TaiKhoan+'-585-'+  convert(CHAR(100),@SoLuong585User))
    
    SET @ThucChay585DaTinh = (SELECT SUM(tcdta.ThanhTienSauTrietKhauThucChay + tcdta.GiaTriThayDoi) 
                              FROM ThucChayDaTinhAdmarket tcdta INNER JOIN HopDong hd
                              ON hd.HopDongID = tcdta.HopDongID
                              WHERE tcdta.DmSanPhamREF = 585 
                              AND hd.Nam >=2014
                              AND tcdta.DmViTriREF = @DmViTriREF
                              AND tcdta.NgayThucHien >=@NgayGioiHanTinh
                              AND tcdta.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID
                                                                FROM HopDongChiTiet hdct WHERE hdct.TK_AdMarket = @TaiKhoan
																AND hdct.DmSanPhamREF = 585
                              AND hdct.ChietKhau <> 100))
     PRINT('ThucChay da tinh tra ve -'+ @TaiKhoan+'-585-'+  convert(CHAR(100),@ThucChay144DaTinh))
    SET @SoLuong585DaTinh = (SELECT SUM(tcdta.SoLuongThucChay + tcdta.SoLuongThayDoi) 
                              FROM ThucChayDaTinhAdmarket tcdta INNER JOIN HopDong hd
                              ON hd.HopDongID= tcdta.HopDongID
                              WHERE tcdta.DmSanPhamREF = 585 
                              AND hd.Nam>=2014
                              AND tcdta.DmViTriREF = @DmViTriREF
                              AND tcdta.NgayThucHien >=@NgayGioiHanTinh
                              AND tcdta.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID
                                                                FROM HopDongChiTiet hdct WHERE hdct.TK_AdMarket = @TaiKhoan
																AND hdct.DmSanPhamREF = 585
																AND hdct.ChietKhau <> 100))    
     PRINT('SoLuong da tinh tra ve -'+ @TaiKhoan+'-585-'+  convert(CHAR(100),@SoLuong585DaTinh))      
     IF(round(@ThucChay585User - @ThucChay585DaTinh,-1)>0 OR round(@SoLuong585User - @SoLuong585DaTinh,-1) > 0)                         
    BEGIN
    UPDATE ThucChayAdmarketOnline  SET RecordStatus = 1 
    WHERE TaiKhoan = @TaiKhoan
    AND DmSanPhamREF = 585 AND TienThucChay > 0
    AND DmViTriREF = @DmViTriREF
    AND RecordStatus =0	
    PRINT 'Insert thuc chay online';		
		INSERT INTO [dbo].[ThucChayAdmarketOnline]
			   ([ThucChayAdmarketOnlineID]
			   ,[DmSanPhamREF]
			   ,[TenSanPham]
			   ,[TaiKhoan]
			   ,[TotalView]
			   ,[TotalClick]
			   ,[SoLuong]
			   ,[DonViTinh]
			   ,[TienThucChay]
			   ,[TienKhuyenMai]
			   ,[NgayThucHien]
			   ,[IsNoiBo]
			   ,[GhiChu]
			   ,[RecordStatus]
			   ,[CreatedAt]
			   ,[CreatedBy]
			   ,[LastModifiedAt]
			   ,[LastModifiedBy]
			   ,[DmViTriREF]
			   ,[TenViTri])
		 VALUES
			   (
				NEWID()
			   ,585
			   ,'AdX'
			   ,@TaiKhoan
			   ,0
			   ,0
			   ,@SoLuong585User - @SoLuong585DaTinh
			   ,'CLICK'
			   ,@ThucChay585User - @ThucChay585DaTinh
			   ,0
			   ,GETDATE()
			   ,0
			   ,''
			   ,0
			   ,GETDATE()
			   ,'asd'
			   ,GETDATE()
			   ,'asd'
			   ,@DmViTriREF
			   ,@TenViTri
			   )   
			       	
    END	 
 

	FETCH NEXT FROM db_cursor INTO @DmviTriREF,@TenViTri      
	END   

	CLOSE db_cursor   
	DEALLOCATE db_cursor
 END 
END

```
