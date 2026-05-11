# Stored Procedure: `Admarket_InsertThucChayDaTinhAdMarket`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-11 15:05:29.367000
- **Ngày sửa cuối**: 2016-08-29 12:09:34.953000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@UserName` | `nvarchar(100)` | No |
| `@GhiChu` | `nvarchar(510)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@DmNhanHangREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: 2016-03-11
-- Description:	<Description,,>
-- =============================================
-- Don vi tinh co dinh la cpc hoac CLICK
--EXEC [dbo].[Admarket_InsertThucChayDaTinhAdMarket] '2016-03-18',585,'hongngoc123','',1,0
CREATE PROCEDURE [dbo].[Admarket_InsertThucChayDaTinhAdMarket]
-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@DmSanPhamREF INT,
	@UserName NVARCHAR(50),
	@GhiChu NVARCHAR(255),
	@DmViTriREF INT,
	@DmNhanHangREF INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	-- Ngay gioi han tinh toan dl
	DECLARE @NgayGioiHanTinh DATETIME = '2013-01-01'
	-- Thong tin thuc ch?y
	DECLARE @TongClickThucChay INT 
	DECLARE @TongTienThucChay FLOAT
	DECLARE @TongTienKhuyenMaiThucChay FLOAT
	DECLARE @TongClickThucChay_NhanHang INT
	DECLARE @TongTienThucChay_NhanHang FLOAT
	DECLARE @TongTienKMThucChay_NhanHang FLOAT
	DECLARE @DonGia FLOAT
	DECLARE @MaxValue FLOAT
	DECLARE @GiaTriInsertVaoThucChayChoPhanBo FLOAT = 0
	DECLARE @SlInsertVaoThucChayChoPhanBo FLOAT = 0
	DECLARE @TypeInsert INT 
	DECLARE @SoNgayThauChi INT = 0
	DECLARE @DmNhanHangChuan NVARCHAR(200)
	-- Thong Tin Hop Dong 
	DECLARE @HopDongID INT
	DECLARE @SoHopDong NVARCHAR(50)
	-- Thông tin phân b?
	DECLARE @PhanBoID INT
	DECLARE @ThanhTienPhanBo FLOAT
	DECLARE @SoLuongPhanBo INT 
	DECLARE @ThanhTienThucChayPhanBo FLOAT
	DECLARE @TenSanPham NVARCHAR(200)
	DECLARE @SoLuongThucChayPhanBo INT 
	-- Th?u chi
	DECLARE @TienThauChi FLOAT = 0
	DECLARE @SoLuongThauChi INT = 0
	DECLARE @TienThauChiPhanBo FLOAT = 0
	DECLARE @NgayBatDauThauChi DATETIME
	-- Insert statements for procedure here
	-- t?ng s? lu?ng click theo chi?u user
	SET @TongClickThucChay = (
	        SELECT SUM(A.ttc)
	        FROM   ThucChaySelfServingUsers A
	        WHERE  A.NgayThucHien = @NgayThucHien
	               AND A.DmSanPhamREF = @DmSanPhamREF
	               AND A.username = @UserName
	               AND A.DmViTriREF = @DmViTriREF
	    )
	-- t?ng ti?n theo chi?u user
	SET @TongTienThucChay = (
	        SELECT SUM(B.ThanhTien)
	        FROM   (
	                   SELECT CASE 
	                               WHEN A.IsNoiBo = 0 THEN A.[money] / 1.1
	                               ELSE A.[money] / 1.1 + A.pro / 1.1
	                          END ThanhTien
	                   FROM   ThucChaySelfServingUsers A
	                   WHERE  A.NgayThucHien = @NgayThucHien
	                          AND A.DmSanPhamREF = @DmSanPhamREF
	                          AND A.username = @UserName
	                          AND A.DmViTriREF = @DmViTriREF
	               )B
	    ) 
	-- T?ng ti?n theo user nhãn hàng
	SET @TongTienThucChay_NhanHang = (
	        SELECT SUM(B.ThanhTien)
	        FROM   (
	                   SELECT CASE 
	                               WHEN A.IsNoiBo = 0 THEN A.[money] / 1.1
	                               ELSE A.[money] / 1.1 + A.pro / 1.1
	                          END ThanhTien
	                   FROM   ThucChaySelfServingUsers_NhanHang A
	                   WHERE  A.NgayThucHien = @NgayThucHien
	                          AND A.DmSanPhamREF = @DmSanPhamREF
	                          AND A.username = @UserName
	                          AND A.DmNhanHangREF = @DmNhanHangREF
	                          AND A.DmViTriREF = @DmViTriREF
	               )B
	    ) 
	
	PRINT '@user: ' + CONVERT(NVARCHAR(50), @UserName);
	PRINT '@SanPham: ' + CONVERT(NVARCHAR(50), @DmSanPhamREF);
	-- T?ng s? lu?ng theo user - nhãn hàng
	SET @TongClickThucChay_NhanHang = @TongClickThucChay
	
	SET @DonGia = 0
	--- tính toán th?c ch?y
	DECLARE db_cursor_tc CURSOR  
	FOR
	    SELECT DISTINCT
	           hdct.HopDongFK,
	           hd.SoHopDong,
	           hdct.HopDongChiTietID,
	           hdct.TenSanPham,
	           hdct.ThanhTien,
	           hdct.SoLuong
	    FROM   HopDongChiTiet AS hdct
	           INNER JOIN HopDong AS hd
	                ON  hd.HopDongID = hdct.HopDongFK
	           INNER JOIN ThucChaySelfServingUsers_NhanHang AS tcau
	                ON  hdct.TK_AdMarket = tcau.username
	    WHERE  tcau.NgayThucHien = @NgayThucHien
	           AND hdct.CreatedAt >= @NgayGioiHanTinh
	           AND tcau.username = @UserName
	           AND tcau.DmNhanHangREF = @DmNhanHangREF
	           AND hd.TrangThaiHopDong <> 3
	           AND hdct.DeletedStatus = 0
	           AND hdct.DmSanPhamREF = @DmSanPhamREF
	           AND hdct.ChietKhau <> 100
	           AND hdct.DmLoaiBannerREF <> 17
	           AND dbo.fn_CheckIsDmLoaiHopDongNoiBo(hd.DmMaHopDongREF, hd.NgayDanhSoHopDong) = 
	               0
	    ORDER BY
	           hdct.HopDongChiTietID
	
	OPEN db_cursor_tc 
	FETCH NEXT FROM db_cursor_tc INTO @HopDongID,@SoHopDong,@PhanBoID,@TenSanPham,
	@ThanhTienPhanBo,@SoLuongPhanBo
	
	WHILE @@FETCH_STATUS = 0
	BEGIN
	    PRINT '@PhanBo1: ' + CONVERT(NVARCHAR(50), @PhanBoID)
	    -- c?p nh?t c?nh báo
	    EXEC [dbo].[Admarket_CapNhatCanhBao] @userName,
	         @DmSanPhamREF,
	         @NgayThucHien
	    -- ki?m tra tình tr?ng th?u chi
	    IF [dbo].[Admarket_fn_CheckThauChi](@userName, @DmSanPhamREF, @NgayThucHien) 
	       > 0
	    BEGIN
	        SET @SoNgayThauChi = DATEDIFF(
	                dd,
	                ISNULL(
	                    (
	                        SELECT MIN(NgayThucHien)
	                        FROM   HopDongAdmarketCanhBao_NhanHang
	                        WHERE  TK_Admarket = @UserName
	                               AND DmSanPhamREF = @DmSanPhamREF
	                               AND DeletedStatus = 0
	                    ),
	                    @NgayThucHien
	                ),
	                @NgayThucHien
	            ) + 1
	    END
	    -- chuan hoa nhan hang 
	    IF @DmNhanHangREF = 0
	    BEGIN
	        SELECT @DmNhanHangChuan = DanhSachNhanHangREF
	        FROM   HopDongChiTiet
	        WHERE  HopDongChiTietID = @PhanBoID
	               AND DeletedStatus = 0
	    END
	    ELSE
	        SET @DmNhanHangChuan = CONVERT(NVARCHAR(50), @DmNhanHangREF)
	    -- neu khong phai qua han thau chi
	    PRINT '@SoNgayThauChi: ' + CONVERT(NVARCHAR(50), @SoNgayThauChi)
	    IF @TongTienThucChay_NhanHang > 0
	       AND @SoNgayThauChi <= dbo.fn_GetSoNgayDuocPhepChayThauChi()
	    BEGIN
	        PRINT '@PhanBo2: ' + CONVERT(NVARCHAR(50), @PhanBoID)
	        -- giá tr? l?n nh?t có th? tính th?c ch?y cho phân b? v?i dl tr? v? ngày hi?n t?i  
	        IF @TongTienThucChay_NhanHang > @ThanhTienPhanBo
	            SET @MaxValue = @ThanhTienPhanBo
	        ELSE
	            SET @MaxValue = @TongTienThucChay_NhanHang
	        -- Thành ti?n th?c ch?y phân b?
	        SELECT @SoLuongThucChayPhanBo = SUM(A.SoLuongThucChay),
	               @ThanhTienThucChayPhanBo = SUM(A.ThanhTienSauTrietKhauThucChay + A.GiaTriThayDoi)
	        FROM   ThucChayDaTinhAdmarket A
	        WHERE  A.HopDongChiTietREF = @PhanBoID
	               AND A.DmSanPhamREF = @DmSanPhamREF
	               AND A.HopDongID = @HopDongID
	               AND A.NgayThucHien <= @NgayThucHien
	        
	        SET @ThanhTienThucChayPhanBo = ISNULL(@ThanhTienThucChayPhanBo, 0)
	        SET @SoLuongThucChayPhanBo = ISNULL(@SoLuongThucChayPhanBo, 0)
	        PRINT '@ThanhTienThucChayPhanBo: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChayPhanBo);
	        PRINT '@TongTienThucChay_NhanHang: ' + CONVERT(NVARCHAR(50), @TongTienThucChay_NhanHang); 
	        PRINT '@PhanBo: ' + CONVERT(NVARCHAR(50), @PhanBoID)
	        
	        -- ki?m tra thành ti?n th?c ch?y phân b? nh? hon thành ti?n phân b? không. n?u nh? hon thì ti?p t?c tính th?c ch?y
	        IF @ThanhTienThucChayPhanBo < @ThanhTienPhanBo
	        BEGIN
	            IF @ThanhTienPhanBo - @ThanhTienThucChayPhanBo > @TongTienThucChay_NhanHang
	            BEGIN
	                SET @GiaTriInsertVaoThucChayChoPhanBo = @TongTienThucChay_NhanHang
	                SET @SlInsertVaoThucChayChoPhanBo = @TongClickThucChay_NhanHang
	            END
	            ELSE
	            BEGIN
	                SET @GiaTriInsertVaoThucChayChoPhanBo = @ThanhTienPhanBo - @ThanhTienThucChayPhanBo
	                SET @SlInsertVaoThucChayChoPhanBo = @SoLuongPhanBo - @SoLuongThucChayPhanBo
	            END
	            --Admarket_ThucChayDaTinhAdmarket_NhanHang_InsertByPhanBoID	
	            PRINT '@GiaTriInsertVaoThucChayChoPhanBo: ' + CONVERT(NVARCHAR(50), @GiaTriInsertVaoThucChayChoPhanBo); 
	            
	            
	            --INSERT Vào Th?c ch?y admarket
	            SET @TongClickThucChay_NhanHang = isnull(@TongClickThucChay_NhanHang,0)
	            SET @SlInsertVaoThucChayChoPhanBo = isnull(@SlInsertVaoThucChayChoPhanBo,0)
	            EXEC dbo.Admarket_ThucChayDaTinhAdmarket_NhanHang_InsertByPhanBoID 
	                 @NgayThucHien,
	                 @SoHopDong,
	                 @PhanBoID,
	                 @DmSanPhamREF,
	                 @TenSanPham,
	                 0 --@DmWebsiteREF
	                 ,
	                 '' --@TenWebsite
	                 ,
	                 0,
	                 @TongClickThucChay_NhanHang,
	                 @SlInsertVaoThucChayChoPhanBo,
	                 @GiaTriInsertVaoThucChayChoPhanBo,
	                 0,
	                 0,
	                 0,
	                 0,
	                 @TypeInsert,
	                 'CPC',
	                 @GhiChu,
	                 @DmViTriREF,
	                 '',
	                 @DmNhanHangChuan
	            -- N?u là ch?y th?u chi thì insert vào c?nh báo
	            IF @SoNgayThauChi > 0
	            BEGIN
	                EXEC [dbo].[Admarket_InsertHopDongAdmarketCanhBao_NhanHang]
	                     @HopDongID,
	                     @SoHopDong,
	                     @PhanBoID,
	                     @DmSanPhamREF,
	                     @TenSanPham,
	                     @UserName,
	                     @DmViTriREF,
	                     0,
	                     '',
	                     '',
	                     @NgayThucHien,
	                     @SlInsertVaoThucChayChoPhanBo,
	                     @GiaTriInsertVaoThucChayChoPhanBo
	            END
	            
	            -- Sau m?t l?n l?p gi?m giá tr? tính th?c ch?y (tr? di cái dã tính)	
	            SET @TongTienThucChay_NhanHang = @TongTienThucChay_NhanHang - @GiaTriInsertVaoThucChayChoPhanBo
	            SET @TongClickThucChay_NhanHang = @TongClickThucChay_NhanHang - 
	                @SlInsertVaoThucChayChoPhanBo
	        END
	        ELSE
	        BEGIN
	            IF @ThanhTienThucChayPhanBo > @ThanhTienPhanBo
	            BEGIN
	                DECLARE @QuaGiaTriPhanBo FLOAT = @ThanhTienThucChayPhanBo -@ThanhTienPhanBo 
	                EXEC dbo.Admarket_ThucChayDaTinhAdmarket_NhanHang_InsertByPhanBoID_GTTD 
	                     @NgayThucHien,
	                     @SoHopDong,
	                     @PhanBoID,
	                     @DmSanPhamREF,
	                     @TenSanPham,
	                     0 --@DmWebsiteREF
	                     ,
	                     '' --@TenWebsite
	                     ,
	                     0,
	                     0,
	                     0,
	                     @QuaGiaTriPhanBo,
	                     0,
	                     0,
	                     0,
	                     0,
	                     @TypeInsert,
	                     'CPC',
	                     @GhiChu,
	                     @DmViTriREF,
	                     '',
	                     @DmNhanHangChuan
	                ---- insert online
	                SET @TongTienThucChay_NhanHang = @TongTienThucChay_NhanHang 
	                    + @QuaGiaTriPhanBo
	            END
	        END
	    END
	    -- n?u quá 3 ngày th?u chi
	    IF @SoNgayThauChi = dbo.fn_GetSoNgayDuocPhepChayThauChi() + 1
	    BEGIN
	        SET @NgayBatDauThauChi = DATEADD(dd, -3, @NgayThucHien)
	        
	        SET @TienThauChi = @TienThauChi + ISNULL(
	                (
	                    SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)
	                    FROM   ThucChayDaTinhAdmarket
	                    WHERE  HopDongID = @HopDongID
	                           AND HopDongChiTietREF = @PhanBoID
	                           AND NhanHang = CONVERT(NVARCHAR(20), @DmNhanHangREF)
	                           AND CONVERT(Date, NgayThucHien) >= CONVERT(date, @NgayBatDauThauChi)
	                           AND CONVERT(Date, NgayThucHien) < @NgayThucHien
	                ),
	                0
	            )
	        -- tien theo nhan
	        SET @TienThauChiPhanBo = ISNULL(
	                (
	                    SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)
	                    FROM   ThucChayDaTinhAdmarket
	                    WHERE  HopDongID = @HopDongID
	                           AND HopDongChiTietREF = @PhanBoID
	                           AND NhanHang = CONVERT(NVARCHAR(20), @DmNhanHangREF)
	                           AND CONVERT(Date, NgayThucHien) >= CONVERT(date, @NgayBatDauThauChi)
	                           AND CONVERT(Date, NgayThucHien) < @NgayThucHien
	                ),
	                0
	            )
	        
	        SET @SoLuongThauChi = ISNULL(
	                (
	                    SELECT SUM(SoLuongThucChay)
	                    FROM   ThucChayDaTinhAdmarket
	                    WHERE  HopDongID = @HopDongID
	                           AND HopDongChiTietREF = @PhanBoID
	                           AND NhanHang = CONVERT(NVARCHAR(20), @DmNhanHangREF)
	                           AND CONVERT(Date, NgayThucHien) >= CONVERT(date, @NgayBatDauThauChi)
	                           AND CONVERT(Date, NgayThucHien) < @NgayThucHien
	                ),
	                0
	            )
	        SET @SoLuongThauChi = ISNULL(@SoLuongThauChi,0)
	        EXEC dbo.Admarket_ThucChayDaTinhAdmarket_NhanHang_InsertByPhanBoID_GTTD 
	             @NgayThucHien,
	             @SoHopDong,
	             @PhanBoID,
	             @DmSanPhamREF,
	             @TenSanPham,
	             0 --@DmWebsiteREF
	             ,
	             '' --@TenWebsite
	             ,
	             0,
	             0,
	             @SoLuongThauChi,
	             @TienThauChiPhanBo,
	             0,
	             0,
	             0,
	             0,
	             @TypeInsert,
	             'CPC',
	             @GhiChu,
	             @DmViTriREF,
	             '',
	             @DmNhanHangChuan
	    END
	    
	    FETCH NEXT FROM db_cursor_tc INTO @HopDongID,@SoHopDong,@PhanBoID,@TenSanPham,
	    @ThanhTienPhanBo,@SoLuongPhanBo
	END 

	CLOSE db_cursor_tc 
	DEALLOCATE db_cursor_tc
	-- n?u th?a ti?n insert vào online m?c dích ngày ti?p theo l?y s? ti?n này c?ng l?i
		--- Sau mooi lan lap
	IF @TongTienThucChay_NhanHang > 1
	BEGIN
	    INSERT INTO dbo.ThucChayAdmarketUser_NhanHang_Online
	    SELECT NEWID(),
	           [username],
	           [DmSanPhamREF],
	           [TenSanPham],
	           [Domain],
	           [ttc],
	           [ttv],
	           @TongTienThucChay_NhanHang,
	           0,
	           [IsNoiBo],
	           [NgayThucHien],
	           [CreatedAt],
	           [CreatedBy],
	           [LastModifedAt],
	           [LastModifiedBy],
	           [userid],
	           [DmNhanHangREF],
	           [TenNhanHang]
	    FROM   [dbo].ThucChaySelfServingUsers_NhanHang
	    WHERE  [username] = @UserName
	           AND DmSanPhamREF = @DmSanPhamREF
	           AND DmNhanHangREF = @DmNhanHangREF
	END
	-- insert vào online giá tr? dã c?p nh?t l?i th?u chi
	IF @SoNgayThauChi = dbo.fn_GetSoNgayDuocPhepChayThauChi() + 1
	   AND @TienThauChi > 0
	BEGIN
	    INSERT INTO dbo.ThucChayAdmarketUser_NhanHang_Online
	    SELECT NEWID(),
	           [username],
	           [DmSanPhamREF],
	           [TenSanPham],
	           [Domain],
	           [ttc],
	           [ttv],
	           @TienThauChi,
	           0,
	           [IsNoiBo],
	           [NgayThucHien],
	           [CreatedAt],
	           [CreatedBy],
	           [LastModifedAt],
	           [LastModifiedBy],
	           [userid],
	           [DmNhanHangREF],
	           [TenNhanHang]
	    FROM   [dbo].ThucChaySelfServingUsers_NhanHang
	    WHERE  [username] = @UserName
	           AND DmSanPhamREF = @DmSanPhamREF
	           AND DmNhanHangREF = @DmNhanHangREF
	END
END

```
