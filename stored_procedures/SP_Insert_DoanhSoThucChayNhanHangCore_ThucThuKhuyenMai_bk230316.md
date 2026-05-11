# Stored Procedure: `Insert_DoanhSoThucChayNhanHangCore_ThucThuKhuyenMai_bk230316`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-09-26 16:00:09.817000
- **Ngày sửa cuối**: 2016-09-26 16:00:09.817000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [Insert_DoanhSoThucChayNhanHangCore_ThucThuKhuyenMai_SanPhamPR] '2016-01-12'

CREATE PROCEDURE [dbo].[Insert_DoanhSoThucChayNhanHangCore_ThucThuKhuyenMai_bk230316]
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @Result BIGINT
	       ,@SoHopDong NVARCHAR(50)
	       ,@HopDongFK INT
	       ,@HopDongChiTietID INT
	
	DECLARE @TenSanPham NVARCHAR(100)
	       ,@DmSanPhamREF INT
	       ,@LstDmNhanHangREF NVARCHAR(200)
	       ,@LstNhanHangThucChayDaTinhREF NVARCHAR(3000)
	
	DECLARE @DoanhSoThucChay BIGINT
	       ,@CheckHopDongChiTietTcID INT
	
	DECLARE @DmNhanHangREF INT
	       ,@TenNhanHang NVARCHAR(200)
	       ,@SoluongHDCT INT
	       ,@SoLuongNhan INT
	
	DECLARE @v_count_checkthucchay INT
	DECLARE @DsNganhHangREF NVARCHAR(50)
	       ,@TenNhanVien NVARCHAR(300)
	       ,@DmNhanVienREF INT
	
	DECLARE @DsTenNganhHang         NVARCHAR(200)
	       ,@v_IsNumber             INT
	       ,@DmHinhThucQuangcaoREF  INT
	       ,@DmLoaiBannerREF        INT
	       ,@DotChayBooking NVARCHAR(100)
	
	SET @DsTenNganhHang = ''
	SET @Result = 0
	SET @SoluongHDCT = 1
	SET @v_count_checkthucchay = 0
	SET @DsNganhHangREF = ''
	SET @LstNhanHangThucChayDaTinhREF = ''
	SET @DotChayBooking=''
	SET @LstDmNhanHangREF=''
	DECLARE Record_Cursor1 CURSOR  
	FOR
	     SELECT DISTINCT tcdt.SoHopDong
	          ,tcdt.HopDongID
	          ,a.TenNhanVien
	          ,a.SysNhanVienREF
	          ,tcdt.HopDongChiTietREF
	          ,tcdt.TenSanPham
	          ,tcdt.DmSanPhamREF
	          ,ISNULL(a.DanhSachNhanHangREF ,'')DanhSachNhanHangREF
	          ,tcdt.NhanHang
	          ,ISNULL(a.DmLoaiREF ,0) DmHinhThucQuangCaoREF
	          ,ISNULL(a.DmLoaiBannerREF ,0) DmLoaiBannerREF
	          ,ISNULL(tcdt.DotChayBooking,'') 
	    FROM   (
	               SELECT DISTINCT hd.SoHopDong
	                     ,hd.HopDongID
	                     ,hdct.HopDongChiTietID
	                     ,hdct.DanhSachNhanHangREF
	                     ,hd.TenNhanVien
	                     ,hd.SysNhanVienREF
	                     ,hdct.DmLoaiREF
	                     ,hdct.DmLoaiBannerREF
	               FROM   hopdong hd
	                      INNER JOIN HopDongChiTiet hdct
	                           ON  hd.HopDongID = hdct.HopDongFK
	               WHERE  [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](hd.DmMaHopDongREF ,@NgayThucHien) = 
	                      0
	           )a
	           RIGHT JOIN (
	                    SELECT DISTINCT A.SoHopDong
	                          ,A.HopDongID
	                          ,A.HopDongChiTietREF
	                          ,A.DmSanPhamREF
	                          ,A.TenSanPham
	                          ,A.NhanHang
	                          ,A.DotChayBooking
	                    FROM   (
	                               SELECT DISTINCT tcdt.SoHopDong
	                                     ,tcdt.HopDongID
	                                     ,tcdt.HopDongChiTietREF
	                                     ,tcdt.DmSanPhamREF
	                                     ,tcdt.TenSanPham
	                                     ,tcdt.TenNhanVien
	                                     ,tcdt.SysNhanVienREF
	                                     ,CASE WHEN tcdt.DmSanPhamREF IN (141 ,305 ,637) AND (tcdt.DmHinhThucQuangCao<>13 AND tcdt.DmLoaiBannerREF<>18) THEN tcdt.NhanHang ELSE '' END NhanHang
	                                    ,CASE WHEN tcdt.DmSanPhamREF IN (141 ,305 ,637) AND (tcdt.DmHinhThucQuangCao<>13 AND tcdt.DmLoaiBannerREF<>18) THEN tcdt.DotChayBooking ELSE '' END DotChayBooking
	                               FROM   ThucChayDaTinh tcdt
	                               WHERE  1 = 1
	                               AND    (
	                                          tcdt.DmSanPhamREF NOT IN (299 ,337 ,299 ,144 ,585 ,628)
	                                      AND NOT(tcdt.DmSanPhamREF = 375 AND YEAR(tcdt.NgayThucHien) = 2013)
	                                      )
	                               AND    tcdt.HopDongID <> 0
	                               AND    tcdt.HopDongChiTietREF <> 0
	                               AND    tcdt.TrangThaiHopDong <> 3
	                               AND    [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](tcdt.DmMaHopDongREF ,@NgayThucHien) = 
	                                      0
	                               AND    CONVERT(date ,tcdt.NgayThucHien) = @NgayThucHien
	                               UNION
	                               SELECT DISTINCT tcdt.SoHopDong
	                                     ,tcdt.HopDongID
	                                     ,tcdt.HopDongChiTietREF
	                                     ,tcdt.DmSanPhamREF
	                                     ,tcdt.TenSanPham
	                                     ,tcdt.TenNhanVien
	                                     ,tcdt.SysNhanVienREF
	                                     ,CASE WHEN tcdt.DmSanPhamREF IN (141 ,305 ,637) AND (tcdt.DmHinhThucQuangCao<>13 AND tcdt.DmLoaiBannerREF<>18) THEN tcdt.NhanHang ELSE '' END NhanHang
	                                     ,CASE WHEN tcdt.DmSanPhamREF IN (141 ,305 ,637) AND (tcdt.DmHinhThucQuangCao<>13 AND tcdt.DmLoaiBannerREF<>18) THEN tcdt.DotChayBooking ELSE '' END DotChayBooking
	                               FROM   ThucChayDaTinhAdmarket tcdt
	                               WHERE  1 = 1
	                               AND    tcdt.DmSanPhamREF IN (299 ,337 ,299 ,144 ,585 ,375 ,628)
	                               AND    tcdt.HopDongID <> 0
	                               AND    tcdt.HopDongChiTietREF <> 0
	                               AND    tcdt.TrangThaiHopDong <> 3
	                               AND    [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](tcdt.DmMaHopDongREF ,@NgayThucHien) = 
	                                      0
	                               AND    CONVERT(date ,tcdt.NgayThucHien) = @NgayThucHien
	                           )A
	                ) tcdt
	                ON  tcdt.HopDongID = a.HopDongID
	    AND             a.HopDongChiTietID = tcdt.HopDongChiTietREF
	    WHERE  1 = 1-- AND a.HopDongID=35676
	OPEN Record_Cursor1
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor1 INTO @SoHopDong, @HopDongFK, @TenNhanVien, @DmNhanVienREF, 
	@HopDongChiTietID, @TenSanPham, @DmSanPhamREF, @LstDmNhanHangREF, @LstNhanHangThucChayDaTinhREF
	, @DmHinhThucQuangcaoREF, @DmLoaiBannerREF,@DotChayBooking
	WHILE @@FETCH_STATUS = 0
	BEGIN
	    --Check hop dong, san pham co thuc chay ngay
	    BEGIN
	    	IF (
	    	       @DmSanPhamREF IN (141 ,305 ,637)
	    	   AND (@DmHinhThucQuangcaoREF <> 13 AND @DmLoaiBannerREF <> 18)
	    	   )
	    	BEGIN
	    	    SET @LstDmNhanHangREF = @LstNhanHangThucChayDaTinhREF
	    	        --PRINT @LstNhanHangThucChayDaTinhREF
	    	END
	    	--PRINT @LstDmNhanHangREF	
	    	SET @DmNhanHangREF = 0
	    	SET @TenNhanHang = ''
	    	SELECT @SoLuongNhan = COUNT(a.DmNhanHang)
	    	FROM   (
	    	           SELECT DISTINCT(
	    	                      CASE 
	    	                           WHEN ISNUMERIC(fss.splitdata) = 0 THEN 0
	    	                           ELSE splitdata
	    	                      END
	    	                  ) DmNhanHang
	    	           FROM   dbo.fnSplitString(@LstDmNhanHangREF ,',')fss
	    	       )a
	    	PRINT @SoLuongNhan
	    	IF (@SoLuongNhan > 0)
	    	BEGIN
	    	    DECLARE Record_Cursor2 CURSOR  
	    	    FOR
	    	        --SELECT distinct dbo.FormatString(item) DmNhanHang
	    	        --FROM dbo.ArrayToTable(dbo.Array(@LstDmNhanHangREF,','))
	    	        
	    	        SELECT DISTINCT(
	    	                   CASE 
	    	                        WHEN ISNUMERIC(fss.splitdata) = 0 THEN 0
	    	                        ELSE splitdata
	    	                   END
	    	               ) DmNhanHang
	    	        FROM   dbo.fnSplitString(@LstDmNhanHangREF ,',')fss
	    	    
	    	    OPEN Record_Cursor2 
	    	    FETCH NEXT FROM Record_Cursor2 INTO @DmNhanHangREF
	    	    WHILE @@FETCH_STATUS = 0
	    	    BEGIN
	    	        SET @DoanhSoThucChay = 0
	    	        
	    	        SELECT @TenNhanHang = dnh.TenNhanHang
	    	              ,@DsNganhHangREF = dnh.DmNghanhHangREF
	    	        FROM   DmNhanHang dnh
	    	        WHERE  dnh.DmNhanHangID = @DmNhanHangREF
	    	        
	    	        SET @TenNhanHang = ISNULL(@TenNhanHang ,'')
	    	        SET @DsNganhHangREF = ISNULL(@DsNganhHangREF ,'')
	    	        
	    	        PRINT @TenNhanHang
	    	        
	    	        
	    	        IF 1 = 1--(@CheckHopDongChiTietTcID = 0)--Neu HopDongChiTietID <> 0
	    	        BEGIN
	    	            PRINT 'vao 1'
	    	            --INSERT DU LIEU CHO TABLE DOANHSOTHUCCHAYNHANHANGCORE
	    	            INSERT INTO DoanhSoThucChayNhanHangCore
	    	            SELECT A.NgayThucHien
	    	                  ,A.DmNhanHangREF
	    	                  ,A.TenNhanHang
	    	                  ,A.DsNganhHangREF
	    	                  ,A.DsTenNganhHang
	    	                  ,A.HopDongID
	    	                  ,A.SoHopDong
	    	                  ,A.TenNhanVien
	    	                  ,A.SysNhanVienREF
	    	                  ,A.HopDongChiTietREF
	    	                  ,A.TenSanPham
	    	                  ,A.DmSanPhamREF
	    	                  ,A.TenWebsite
	    	                  ,A.DmWebsiteREF
	    	                  ,0 ThucThuPhatSinhDauKy
	    	                  ,SUM(A.ThucThuPhatSinhTrongKy)
	    	                   ThucThuPhatSinhTrongKy
	    	                  ,0 ThucThuPhatSinhCuoiKy
	    	                  ,SUM(A.KhuyenMaiPhatSinhTrongKy) 
	    	                   KhuyenMaiPhatSinhTrongKy
	    	                  ,0 KhuyenMaiPhatSinhDauKy
	    	                  ,0 KhuyenMaiPhatSinhCuoiKy
	    	                  ,0 NoiBoPhatSinhDauKy
	    	                  ,0 NoiBoPhatSinhTrongKy
	    	                  ,0 NoiBoPhatSinhCuoiKy
	    	                  ,0 SoLuongPhatSinhDauKy
	    	                  ,SUM(A.SoLuongPhatSinhTrongKy) 
	    	                   SoLuongPhatSinhTrongKy
	    	                  ,0 SoLuongPhatSinhCuoiKy
	    	                  ,0 SoLuongKhuyenMaiPhatSinhDauKy
	    	                  ,SUM(A.SoLuongKMPhatSinh) 
	    	                   SoLuongKhuyenMaiPhatSinhTrongKy
	    	                  ,0 SoLuongKhuyenMaiPhatSinhCuoiKy
	    	                  ,0 SoLuongNoiBoPhatSinhDauKy
	    	                  ,0 SoLuongNoiBoPhatSinhTrongKy
	    	                  ,0 SoLuongNoiBoPhatSinhCuoiKy
	    	                  ,'' DienGiai
	    	                  ,'ASD' CreatedBy
	    	                  ,GETDATE() CreatedAt
	    	                  ,'ASD' LastModifiedBy
	    	                  ,GETDATE() LastModifiedAt
	    	                  ,0 DeletedStatus
	    	                  ,0 PrintStatus
	    	                  ,0 RecordStatus
	    	                  ,A.TenDangNhap
	    	                  ,A.DmPhongBanREF
	    	                  ,A.DmBoPhanREF
	    	                  ,A.DmNhomLamViecREF
	    	                  ,A.Nam
	    	                  ,A.Quy
	    	                  ,A.Thang
	    	                  ,A.NgayDanhSoHopDong
	    	                  ,A.DmDiaDiemLamViecREF
	    	                  ,A.TenDiaDiemLamViec
	    	                  ,0 DmKhachHangREF
	    	                  ,'' TenKhachHang
	    	            FROM   (
	    	                       SELECT @NgayThucHien NgayThucHien
	    	                             ,@DmNhanHangREF DmNhanHangREF
	    	                             ,@TenNhanHang TenNhanHang
	    	                             ,@DsNganhHangREF DsNganhHangREF
	    	                             ,@DsTenNganhHang DsTenNganhHang
	    	                             ,tcdt.HopDongID
	    	                             ,tcdt.SoHopDong
	    	                             ,tcdt.TenNhanVien
	    	                             ,tcdt.SysNhanVienREF
	    	                             ,tcdt.HopDongChiTietREF 
	    	                              HopDongChiTietREF
	    	                             ,tcdt.TenSanPham
	    	                             ,tcdt.DmSanPhamREF
	    	                             ,tcdt.TenWebsite
	    	                             ,tcdt.DmWebsiteREF
	    	                             ,tcdt.TenDangNhap
	    	                             ,tcdt.DmPhongBanREF
	    	                             ,tcdt.DmBoPhanREF
	    	                             ,tcdt.DmNhomLamViecREF
	    	                             ,YEAR(@NgayThucHien) Nam
	    	                             ,MONTH(@NgayThucHien) Thang
	    	                             ,DATEPART(QQ ,@NgayThucHien) Quy
	    	                             ,0 AS ThucThuPhatSinhDauKy
	    	                             ,SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)
	    	                              / @SoLuongNhan AS 
	    	                              ThucThuPhatSinhTrongKy
	    	                             ,0 AS ThucThuPhatSinhCuoiKy
	    	                             ,0 AS KhuyenMaiPhatSinhDauKy
	    	                             ,SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi)
	    	                              / @SoLuongNhan AS 
	    	                              KhuyenMaiPhatSinhTrongKy
	    	                             ,0 AS KhuyenMaiPhatSinhCuoiKy
	    	                             ,SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi)
	    	                              / @SoLuongNhan AS 
	    	                              SoLuongPhatSinhTrongKy
	    	                             ,SUM(tcdt.SoLuongThucChayKM + tcdt.SoLuongKMThayDoi)
	    	                              / @SoLuongNhan AS SoLuongKMPhatSinh
	    	                             ,tcdt.DmDiaDiemLamViecREF
	    	                             ,tcdt.TenDiaDiemLamViec
	    	                             ,tcdt.NgayDanhSoHopDong
	    	                             
	    	                       FROM   ThucChayDaTinh tcdt
	    	                       WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietID
	    	                       AND    (
	    	                                  tcdt.DmSanPhamREF NOT IN (299 ,337 ,299 ,144 ,585 ,628)
	    	                              AND NOT(tcdt.DmSanPhamREF = 375 AND YEAR(tcdt.NgayThucHien) = 2013)
	    	                              )
	    	                       AND    tcdt.DmSanPhamREF = @DmSanPhamREF
	    	                       AND    CONVERT(date ,tcdt.NgayThucHien) = @NgayThucHien
	    	                       AND    CASE WHEN tcdt.DmSanPhamREF IN (141 ,305 ,637) AND (tcdt.DmHinhThucQuangCao<>13 AND tcdt.DmLoaiBannerREF<>18) THEN tcdt.DotChayBooking ELSE '' END = @DotChayBooking
	    	                       AND    CASE WHEN tcdt.DmSanPhamREF IN (141 ,305 ,637) AND (tcdt.DmHinhThucQuangCao<>13 AND tcdt.DmLoaiBannerREF<>18) THEN tcdt.NhanHang ELSE @LstNhanHangThucChayDaTinhREF END = @LstNhanHangThucChayDaTinhREF
	    	                        GROUP BY
	    	                              tcdt.HopDongID
	    	                             ,tcdt.SoHopDong
	    	                             ,tcdt.TenNhanVien
	    	                             ,tcdt.SysNhanVienREF
	    	                             ,tcdt.HopDongChiTietREF
	    	                             ,tcdt.TenSanPham
	    	                             ,tcdt.DmSanPhamREF
	    	                             ,tcdt.TenWebsite
	    	                             ,tcdt.DmWebsiteREF
	    	                             ,tcdt.TenDangNhap
	    	                             ,tcdt.DmPhongBanREF
	    	                             ,tcdt.DmBoPhanREF
	    	                             ,tcdt.DmNhomLamViecREF
	    	                             ,tcdt.DmDiaDiemLamViecREF
	    	                             ,tcdt.TenDiaDiemLamViec
	    	                             ,tcdt.NgayDanhSoHopDong
	    	                             ,tcdt.NhanHang
	    	                             ,tcdt.DotChayBooking
	    	                       UNION
	    	                       SELECT @NgayThucHien NgayThucHien
	    	                             ,@DmNhanHangREF DmNhanHangREF
	    	                             ,@TenNhanHang TenNhanHang
	    	                             ,@DsNganhHangREF DsNganhHangREF
	    	                             ,@DsTenNganhHang DsTenNganhHang
	    	                             ,tcdt.HopDongID
	    	                             ,tcdt.SoHopDong
	    	                             ,tcdt.TenNhanVien
	    	                             ,tcdt.SysNhanVienREF
	    	                             ,tcdt.HopDongChiTietREF 
	    	                              HopDongChiTietREF
	    	                             ,tcdt.TenSanPham
	    	                             ,tcdt.DmSanPhamREF
	    	                             ,tcdt.TenWebsite
	    	                             ,tcdt.DmWebsiteREF
	    	                             ,tcdt.TenDangNhap
	    	                             ,tcdt.DmPhongBanREF
	    	                             ,tcdt.DmBoPhanREF
	    	                             ,tcdt.DmNhomLamViecREF
	    	                             ,YEAR(@NgayThucHien) Nam
	    	                             ,MONTH(@NgayThucHien) Thang
	    	                             ,DATEPART(QQ ,@NgayThucHien) Quy
	    	                             ,0 AS ThucThuPhatSinhDauKy
	    	                             ,SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)
	    	                              / @SoLuongNhan AS 
	    	                              ThucThuPhatSinhTrongKy
	    	                             ,0 AS ThucThuPhatSinhCuoiKy
	    	                             ,0 AS KhuyenMaiPhatSinhDauKy
	    	                             ,SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi)
	    	                              / @SoLuongNhan AS 
	    	                              KhuyenMaiPhatSinhTrongKy
	    	                             ,0 AS KhuyenMaiPhatSinhCuoiKy
	    	                             ,SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi)
	    	                              / @SoLuongNhan AS 
	    	                              SoLuongPhatSinhTrongKy
	    	                             ,SUM(tcdt.SoLuongThucChayKM + tcdt.SoLuongKMThayDoi)
	    	                              / @SoLuongNhan AS SoLuongKMPhatSinh
	    	                             ,tcdt.DmDiaDiemLamViecREF
	    	                             ,tcdt.TenDiaDiemLamViec
	    	                             ,tcdt.NgayDanhSoHopDong
	    	                             
	    	                       FROM   ThucChayDaTinhAdmarket tcdt
	    	                       WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietID
	    	                       AND    tcdt.DmSanPhamREF IN (299 ,337 ,299 ,144 ,585 ,375 ,628)
	    	                       AND    tcdt.DmSanPhamREF = @DmSanPhamREF
	    	                       AND    CONVERT(date ,tcdt.NgayThucHien) = @NgayThucHien
	    	                       AND    CASE WHEN tcdt.DmSanPhamREF IN (141 ,305 ,637) AND (tcdt.DmHinhThucQuangCao<>13 AND tcdt.DmLoaiBannerREF<>18) THEN tcdt.DotChayBooking ELSE '' END = @DotChayBooking
	    	                       AND    CASE WHEN tcdt.DmSanPhamREF IN (141 ,305 ,637) AND (tcdt.DmHinhThucQuangCao<>13 AND tcdt.DmLoaiBannerREF<>18) THEN tcdt.NhanHang ELSE @LstNhanHangThucChayDaTinhREF END = @LstNhanHangThucChayDaTinhREF
	    	                       GROUP BY
	    	                              tcdt.HopDongID
	    	                             ,tcdt.SoHopDong
	    	                             ,tcdt.TenNhanVien
	    	                             ,tcdt.SysNhanVienREF
	    	                             ,tcdt.HopDongChiTietREF
	    	                             ,tcdt.TenSanPham
	    	                             ,tcdt.DmSanPhamREF
	    	                             ,tcdt.TenWebsite
	    	                             ,tcdt.DmWebsiteREF
	    	                             ,tcdt.TenDangNhap
	    	                             ,tcdt.DmPhongBanREF
	    	                             ,tcdt.DmBoPhanREF
	    	                             ,tcdt.DmNhomLamViecREF
	    	                             ,tcdt.DmDiaDiemLamViecREF
	    	                             ,tcdt.TenDiaDiemLamViec
	    	                             ,tcdt.NgayDanhSoHopDong
	    	                             ,tcdt.NhanHang
	    	                             ,tcdt.DotChayBooking
	    	                             
	    	                   )A
	    	            WHERE  (
	    	                       ROUND(A.ThucThuPhatSinhTrongKy ,0) <> 0
	    	                   OR  ROUND(A.KhuyenMaiPhatSinhTrongKy ,0) <> 0
	    	                   )
	    	            GROUP BY
	    	                   A.NgayThucHien
	    	                  ,A.DmNhanHangREF
	    	                  ,A.TenNhanHang
	    	                  ,A.DsNganhHangREF
	    	                  ,A.DsTenNganhHang
	    	                  ,A.HopDongID
	    	                  ,A.SoHopDong
	    	                  ,A.TenNhanVien
	    	                  ,A.SysNhanVienREF
	    	                  ,A.HopDongChiTietREF
	    	                  ,A.TenSanPham
	    	                  ,A.DmSanPhamREF
	    	                  ,A.TenWebsite
	    	                  ,A.DmWebsiteREF
	    	                  ,A.TenDangNhap
	    	                  ,A.DmPhongBanREF
	    	                  ,A.DmBoPhanREF
	    	                  ,A.DmNhomLamViecREF
	    	                  ,A.Nam
	    	                  ,A.Quy
	    	                  ,A.Thang
	    	                  ,A.DmDiaDiemLamViecREF
	    	                  ,A.TenDiaDiemLamViec
	    	                  ,A.NgayDanhSoHopDong
	    	        END
	    	        
	    	        FETCH NEXT FROM Record_Cursor2 INTO @DmNhanHangREF
	    	    END
	    	    CLOSE Record_Cursor2
	    	    DEALLOCATE Record_Cursor2
	    	END
	    	ELSE
	    	BEGIN
	    	    PRINT 'vao 2'
	    	    INSERT INTO DoanhSoThucChayNhanHangCore
	    	    SELECT A.NgayThucHien
	    	          ,A.DmNhanHangREF
	    	          ,A.TenNhanHang
	    	          ,A.DsNganhHangREF
	    	          ,A.DsTenNganhHang
	    	          ,A.HopDongID
	    	          ,A.SoHopDong
	    	          ,A.TenNhanVien
	    	          ,A.SysNhanVienREF
	    	          ,A.HopDongChiTietREF
	    	          ,A.TenSanPham
	    	          ,A.DmSanPhamREF
	    	          ,A.TenWebsite
	    	          ,A.DmWebsiteREF
	    	          ,0 ThucThuPhatSinhDauKy
	    	          ,SUM(A.ThucThuPhatSinhTrongKy)ThucThuPhatSinhTrongKy
	    	          ,0 ThucThuPhatSinhCuoiKy
	    	          ,0 KhuyenMaiPhatSinhDauKy
	    	          ,SUM(A.KhuyenMaiPhatSinhTrongKy) KhuyenMaiPhatSinhTrongKy
	    	          ,0 KhuyenMaiPhatSinhCuoiKy
	    	          ,0 NoiBoPhatSinhDauKy
	    	          ,0 NoiBoPhatSinhTrongKy
	    	          ,0 NoiBoPhatSinhCuoiKy
	    	          ,0 SoLuongPhatSinhDauKy
	    	          ,SUM(A.SoLuongPhatSinhTrongKy) SoLuongPhatSinhTrongKy
	    	          ,0 SoLuongPhatSinhCuoiKy
	    	          ,0 SoLuongKhuyenMaiPhatSinhDauKy
	    	          ,SUM(A.SoLuongKMPhatSinh) SoLuongKhuyenMaiPhatSinhTrongKy
	    	          ,0 SoLuongKhuyenMaiPhatSinhCuoiKy
	    	          ,0 SoLuongNoiBoPhatSinhDauKy
	    	          ,0 SoLuongNoiBoPhatSinhTrongKy
	    	          ,0 SoLuongNoiBoPhatSinhCuoiKy
	    	          ,'' DienGiai
	    	          ,'ASD' CreatedBy
	    	          ,GETDATE() CreatedAt
	    	          ,'ASD' LastModifiedBy
	    	          ,GETDATE() LastModifiedAt
	    	          ,0 DeletedStatus
	    	          ,0 PrintStatus
	    	          ,0 RecordStatus
	    	          ,A.TenDangNhap
	    	          ,A.DmPhongBanREF
	    	          ,A.DmBoPhanREF
	    	          ,A.DmNhomLamViecREF
	    	          ,A.Nam
	    	          ,A.Quy
	    	          ,A.Thang
	    	          ,A.NgayDanhSoHopDong
	    	          ,A.DmDiaDiemLamViecREF
	    	          ,A.TenDiaDiemLamViec
	    	          ,0 DmKhachHangREF
	    	          ,'' TenKhachHang
	    	    FROM   (
	    	               SELECT @NgayThucHien NgayThucHien
	    	                     ,@DmNhanHangREF DmNhanHangREF
	    	                     ,@TenNhanHang TenNhanHang
	    	                     ,@DsNganhHangREF DsNganhHangREF
	    	                     ,@DsTenNganhHang DsTenNganhHang
	    	                     ,tcdt.HopDongID
	    	                     ,tcdt.SoHopDong
	    	                     ,tcdt.TenNhanVien
	    	                     ,tcdt.SysNhanVienREF
	    	                     ,tcdt.HopDongChiTietREF HopDongChiTietREF
	    	                     ,tcdt.TenSanPham
	    	                     ,tcdt.DmSanPhamREF
	    	                     ,tcdt.TenWebsite
	    	                     ,tcdt.DmWebsiteREF
	    	                     ,tcdt.TenDangNhap
	    	                     ,tcdt.DmPhongBanREF
	    	                     ,tcdt.DmBoPhanREF
	    	                     ,tcdt.DmNhomLamViecREF
	    	                     ,YEAR(@NgayThucHien) Nam
	    	                     ,MONTH(@NgayThucHien) Thang
	    	                     ,DATEPART(QQ ,@NgayThucHien) Quy
	    	                     ,0 AS ThucThuPhatSinhDauKy
	    	                     ,SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS 
	    	                      ThucThuPhatSinhTrongKy
	    	                     ,0 AS ThucThuPhatSinhCuoiKy
	    	                     ,0 AS KhuyenMaiPhatSinhDauKy
	    	                     ,SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) AS 
	    	                      KhuyenMaiPhatSinhTrongKy
	    	                     ,0 AS KhuyenMaiPhatSinhCuoiKy
	    	                     ,SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) AS 
	    	                      SoLuongPhatSinhTrongKy
	    	                     ,SUM(tcdt.SoLuongThucChayKM + tcdt.SoLuongKMThayDoi) AS 
	    	                      SoLuongKMPhatSinh
	    	                     ,tcdt.DmDiaDiemLamViecREF
	    	                     ,tcdt.TenDiaDiemLamViec
	    	                     ,tcdt.NgayDanhSoHopDong
	    	               FROM   ThucChayDaTinh tcdt
	    	               WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietID
	    	               AND    (
	    	                          tcdt.DmSanPhamREF NOT IN (299 ,337 ,299 ,144 ,585 ,628)
	    	                      AND NOT(tcdt.DmSanPhamREF = 375 AND YEAR(tcdt.NgayThucHien) = 2013)
	    	                      )
	    	               AND    tcdt.DmSanPhamREF = @DmSanPhamREF
	    	               AND    CONVERT(date ,tcdt.NgayThucHien) = @NgayThucHien
	    	               AND    CASE WHEN tcdt.DmSanPhamREF IN (141 ,305 ,637) AND (tcdt.DmHinhThucQuangCao<>13 AND tcdt.DmLoaiBannerREF<>18) THEN tcdt.DotChayBooking ELSE '' END = @DotChayBooking
	    	                       AND    CASE WHEN tcdt.DmSanPhamREF IN (141 ,305 ,637) AND (tcdt.DmHinhThucQuangCao<>13 AND tcdt.DmLoaiBannerREF<>18) THEN tcdt.NhanHang ELSE @LstNhanHangThucChayDaTinhREF END = @LstNhanHangThucChayDaTinhREF
	    	                       GROUP BY
	    	                      tcdt.HopDongID
	    	                     ,tcdt.SoHopDong
	    	                     ,tcdt.TenNhanVien
	    	                     ,tcdt.SysNhanVienREF
	    	                     ,tcdt.HopDongChiTietREF
	    	                     ,tcdt.TenSanPham
	    	                     ,tcdt.DmSanPhamREF
	    	                     ,tcdt.TenWebsite
	    	                     ,tcdt.DmWebsiteREF
	    	                     ,tcdt.TenDangNhap
	    	                     ,tcdt.DmPhongBanREF
	    	                     ,tcdt.DmBoPhanREF
	    	                     ,tcdt.DmNhomLamViecREF
	    	                     ,tcdt.DmDiaDiemLamViecREF
	    	                     ,tcdt.TenDiaDiemLamViec
	    	                     ,tcdt.NgayDanhSoHopDong
	    	                     ,tcdt.NhanHang
	    	                     ,tcdt.DotChayBooking
	    	               UNION
	    	               SELECT @NgayThucHien NgayThucHien
	    	                     ,@DmNhanHangREF DmNhanHangREF
	    	                     ,@TenNhanHang TenNhanHang
	    	                     ,@DsNganhHangREF DsNganhHangREF
	    	                     ,@DsTenNganhHang DsTenNganhHang
	    	                     ,tcdt.HopDongID
	    	                     ,tcdt.SoHopDong
	    	                     ,tcdt.TenNhanVien
	    	                     ,tcdt.SysNhanVienREF
	    	                     ,tcdt.HopDongChiTietREF HopDongChiTietREF
	    	                     ,tcdt.TenSanPham
	    	                     ,tcdt.DmSanPhamREF
	    	                     ,tcdt.TenWebsite
	    	                     ,tcdt.DmWebsiteREF
	    	                     ,tcdt.TenDangNhap
	    	                     ,tcdt.DmPhongBanREF
	    	                     ,tcdt.DmBoPhanREF
	    	                     ,tcdt.DmNhomLamViecREF
	    	                     ,YEAR(@NgayThucHien) Nam
	    	                     ,MONTH(@NgayThucHien) Thang
	    	                     ,DATEPART(QQ ,@NgayThucHien) Quy
	    	                     ,0 AS ThucThuPhatSinhDauKy
	    	                     ,SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS 
	    	                      ThucThuPhatSinhTrongKy
	    	                     ,0 AS ThucThuPhatSinhCuoiKy
	    	                     ,0 AS KhuyenMaiPhatSinhDauKy
	    	                     ,SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) AS 
	    	                      KhuyenMaiPhatSinhTrongKy
	    	                     ,0 AS KhuyenMaiPhatSinhCuoiKy
	    	                     ,SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) AS 
	    	                      SoLuongPhatSinhTrongKy
	    	                     ,SUM(tcdt.SoLuongThucChayKM + tcdt.SoLuongKMThayDoi) AS 
	    	                      SoLuongKMPhatSinh
	    	                     ,tcdt.DmDiaDiemLamViecREF
	    	                     ,tcdt.TenDiaDiemLamViec
	    	                     ,tcdt.NgayDanhSoHopDong
	    	               FROM   ThucChayDaTinhAdmarket tcdt
	    	               WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietID
	    	               AND    tcdt.DmSanPhamREF IN (299 ,337 ,299 ,144 ,585 ,375 ,628)
	    	               AND    tcdt.DmSanPhamREF = @DmSanPhamREF
	    	               AND    CONVERT(date ,tcdt.NgayThucHien) = @NgayThucHien
	    	               AND    CASE WHEN tcdt.DmSanPhamREF IN (141 ,305 ,637) AND (tcdt.DmHinhThucQuangCao<>13 AND tcdt.DmLoaiBannerREF<>18) THEN tcdt.DotChayBooking ELSE '' END = @DotChayBooking
	    	                       AND    CASE WHEN tcdt.DmSanPhamREF IN (141 ,305 ,637) AND (tcdt.DmHinhThucQuangCao<>13 AND tcdt.DmLoaiBannerREF<>18) THEN tcdt.NhanHang ELSE @LstNhanHangThucChayDaTinhREF END = @LstNhanHangThucChayDaTinhREF
	    	               GROUP BY
	    	                      tcdt.HopDongID
	    	                     ,tcdt.SoHopDong
	    	                     ,tcdt.TenNhanVien
	    	                     ,tcdt.SysNhanVienREF
	    	                     ,tcdt.HopDongChiTietREF
	    	                     ,tcdt.TenSanPham
	    	                     ,tcdt.DmSanPhamREF
	    	                     ,tcdt.TenWebsite
	    	                     ,tcdt.DmWebsiteREF
	    	                     ,tcdt.TenDangNhap
	    	                     ,tcdt.DmPhongBanREF
	    	                     ,tcdt.DmBoPhanREF
	    	                     ,tcdt.DmNhomLamViecREF
	    	                     ,tcdt.DmDiaDiemLamViecREF
	    	                     ,tcdt.TenDiaDiemLamViec
	    	                     ,tcdt.NgayDanhSoHopDong
	    	                     ,tcdt.DotChayBooking
	    	                     ,tcdt.NhanHang
	    	           )A
	    	    WHERE  (
	    	               ROUND(A.ThucThuPhatSinhTrongKy ,0) <> 0
	    	           OR  ROUND(A.KhuyenMaiPhatSinhTrongKy ,0) <> 0
	    	           )
	    	    GROUP BY
	    	           A.NgayThucHien
	    	          ,A.DmNhanHangREF
	    	          ,A.TenNhanHang
	    	          ,A.DsNganhHangREF
	    	          ,A.DsTenNganhHang
	    	          ,A.HopDongID
	    	          ,A.SoHopDong
	    	          ,A.TenNhanVien
	    	          ,A.SysNhanVienREF
	    	          ,A.HopDongChiTietREF
	    	          ,A.TenSanPham
	    	          ,A.DmSanPhamREF
	    	          ,A.TenWebsite
	    	          ,A.DmWebsiteREF
	    	          ,A.TenDangNhap
	    	          ,A.DmPhongBanREF
	    	          ,A.DmBoPhanREF
	    	          ,A.DmNhomLamViecREF
	    	          ,A.Nam
	    	          ,A.Quy
	    	          ,A.Thang
	    	          ,A.DmDiaDiemLamViecREF
	    	          ,A.TenDiaDiemLamViec
	    	          ,A.NgayDanhSoHopDong
	    	END
	    END
	    FETCH NEXT FROM Record_Cursor1 INTO @SoHopDong, @HopDongFK, @TenNhanVien, 
	    @DmNhanVienREF, @HopDongChiTietID, @TenSanPham, @DmSanPhamREF, @LstDmNhanHangREF, 
	    @LstNhanHangThucChayDaTinhREF, @DmHinhThucQuangcaoREF, @DmLoaiBannerREF,@DotChayBooking
	END
	
	CLOSE Record_Cursor1
	DEALLOCATE Record_Cursor1
	--SELECT '1'
END

--EXEC [Insert_DoanhSoThucChayCoreNhanHang_ThucThu] '2013-12-31'

```
