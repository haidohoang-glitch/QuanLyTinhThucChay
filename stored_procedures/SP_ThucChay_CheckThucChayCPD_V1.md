# Stored Procedure: `ThucChay_CheckThucChayCPD_V1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-17 13:01:37.900000
- **Ngày sửa cuối**: 2014-11-19 12:16:59.103000

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
--EXEC [dbo].[ThucChay_CheckThucChayCPD_V1] '2014-05-23', '2014-05-25'
CREATE PROCEDURE [dbo].[ThucChay_CheckThucChayCPD_V1]
	@StartDate DATETIME, 
	@EndDate DATETIME
AS
BEGIN
	DECLARE @table TABLE 
        (
            [HopDongID] [int] NOT NULL,
            [SoHopDong] [nvarchar](50) NOT NULL,	            
            [GiaTriHopDong] [float] NULL,
            [CongNo] [float] NOT NULL,
            [HopDongChiTietREF] [int] NULL,	            
            [DmSanPhamREF] [int] NULL,
            [TenSanPham] [nvarchar](100) NULL,	
            DotChayHD NVARCHAR(100) NULL,     
            SoLuongHD [int] NULL,
            [SoLuongDotChay] [int] NULL,
            [DonViTinh] [nvarchar](50) NULL,
            [DonGia] [float] NULL,
            [DonGiaTheoDonVi] [float] NULL,
            [ChietKhau] [float] NULL,
            [GiamGia] [float] NULL,
            [ThanhTien] [float] NULL,                        
            [DmWebsiteREF] [int] NULL,
            [TenWebsite] [nvarchar](255) NULL,            
            [SoLuongThucChay] [float] NULL,
            [NgayThucHien] [datetime] NULL,            
            [ThanhTienThucChayTruocTrietKhau] [float] NULL,
            [GiaTriTrietKhauThucChay] [float] NULL,
            [ThanhTienSauTrietKhauThucChay] [float] NULL            
        )

	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @StartDate

	WHILE (@NgayThucHien <= @EndDate)
	BEGIN
	    INSERT INTO @table
	    SELECT 
	           TD.*
	           , ISNULL((TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau) / 100,0) 
						AS GiaTriTrietKhauThucChay
	           , ISNULL((TD.ThanhTienThucChayTruocTrietKhau -(TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/ 100),0) 
						AS ThanhTienSauTrietKhauThucChay
	    FROM   (
	               SELECT --ID Hop Dong
	                      D.HopDongID,
	                      --Thong tin ve ma so 
	                      D.SoHopDong,	                      
	                      --Thong tin ve gia tri
	                      D.GiaTriHopDong,
	                      D.CongNo,
	                      --Thong tin chi tiet phan bo
	                      C.HopDongChiTietID,
	                     --Thong tin San pham
	                      c.DmSanPhamREF AS DmSanPhamREF,
	                      C.TenSanPham,	                      
	                      --Thong tin ve Tien
	                      '' AS DotChayHD,
	                      ISNULL(dbo.ThucChay_GetSoLuong_DonViTinh(C.SoLuong, C.DonViTinh),0) AS SoLuongHD,
	                      isnull(dbo.ThucChay_GetSoLuongNgayDotChayHopDongChiTiet(C.SoLuong, C.DonViTinh, C.HopDongChiTietID),0) AS SoLuongDotChay,
	                      dbo.FormatDonViTinh(C.DonViTinh) DonViTinh,
	                      dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien, c.HopDongChiTietID, C.DonGia) AS DonGia,
	                      ISNULL(
	                      	dbo.ThucChay_GetDonGiaChuanTheoDonViTinh_BK(
									  C.SoLuong,
									  C.DonViTinh,
									  C.DonGia,
									  --D.NgayKyHopDong,
									  @NgayThucHien,
									  c.HopDongChiTietID
	                          ),0) AS DonGiaTheoDonViTinh,
	                      C.ChietKhau,
	                      C.GiamGia,
	                      C.ThanhTien,	                     
	                      --Thuc chay	                      
	                      C.DmWebsiteREF,	--A.DmWebsiteREF,
	                      c.TenWebsite,
	                      --A.SoHopDong,	                      
	                      ISNULL(dbo.ThucChay_GetSoLuongThucChayCPD_Test_V1(@NgayThucHien, C.HopDongChiTietID),0) 
								AS SoLuongThucChay,
	                      --Thanhuc Tien Thuc Chay
	                      @NgayThucHien AS NgayThucHien,	                      
	                      ISNULL(
	                          dbo.[ThucChay_GetThanhTienChuanThucChay_CPD_Test_V1](
	                              C.SoLuong,
	                              C.DonViTinh,
	                              C.DonGia,
	                              --D.NgayKyHopDong,
	                              @NgayThucHien,
	                              c.HopDongChiTietID
	                          ),0) 
								AS ThanhTienThucChayTruocTrietKhau
	               FROM   (
	                          SELECT *
	                          FROM   HopDongChiTiet
	                          WHERE  DmSanPhamREF IN (140, 228,241, 564, 549, 385)
	                          --AND DmLoaiREF = 5	                          
	                          AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, DonViTinh) = 1
	                          
	                      ) C
	                      INNER JOIN (
	                               SELECT *
	                               FROM   HopDong hd
	                               WHERE  hd.TrangThaiHopDong != 3
	                           ) D
	                           ON  D.HopDongID = C.HopDongFK
				--INNER JOIN DmSanPham E
				--ON  E.DmSanPhamID = C.DmSanPhamREF
				WHERE dbo.ThucChay_GetSoLuongThucChayCPD_Test_V1(@NgayThucHien, C.HopDongChiTietID) > 0
				) TD

	    SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
	END 
	SELECT a.HopDongID,
	       a.SoHopDong,
	       a.HopDongChiTietREF AS PhanBoID,
	       --a.DonGiaTheoDonVi,
	       b.sohopdong AS sohd_tcdt,
	       b.hopdongchitietref AS pbid_tcdt,
	       a.SoLuongHD AS SLHD,
	       a.SoLuongDotChay AS SLDotChay,	 
	       ISNULL(b.SoLuong, 0) sl_tcdt, 
	       (a.SoLuongHD - ISNULL(b.SoLuong, 0)) AS SLLech,     
	       a.ThanhTienSauCK AS tttc_hd,	  	       	       
	       ISNULL(b.ThanhTienSauCK, 0) ttsauck_tcdt,
	       (a.ThanhTienSauCK - ISNULL(b.ThanhTienSauCK, 0)) AS ttlech
	FROM   (
	           SELECT 
					HopDongID,
					SoHopDong,
	                  HopDongChiTietREF,
	                  DonGiaTheoDonVi,
	                  ISNULL(SoLuongHD, 0) SoLuongHD,
	                  ISNULL(SoLuongDotChay, 0) AS SoLuongDotChay,
	                  ISNULL(SUM(SoLuongThucChay), 0) SoLuongThucChay,
	                  ISNULL(SUM(ThanhTienSauTrietKhauThucChay), 0) AS 
	                  ThanhTienSauCK
	           FROM   @table
	           GROUP BY
	           HopDongID,
	                  SoHopDong,
	                  HopDongChiTietREF,
	                  SoLuongHD,
	                  SoLuongDotChay,
	                  DonGiaTheoDonVi
	                  
	       ) A
	       FULL OUTER JOIN (
	                SELECT --tcdt.NgayThucHien, 
	                       tcdt.sohopdong,
	                       tcdt.hopdongchitietref,
	                       ISNULL(tcdt.Soluong, 0) Soluong,	                       
	                       ISNULL(SUM(tcdt.SoLuongThucChay), 0) SoLuongThucChay,
	                       ISNULL(SUM(tcdt.SoLuongThucChayKM),0) SoLuongThucChayKM,
	                       ISNULL(SUM(tcdt.thanhtiensautrietkhauthucchay), 0) ThanhTienSauCK
	                FROM   ThucChayDaTinh tcdt
	                WHERE  CONVERT(date, ngaythuchien) BETWEEN @StartDate AND @EndDate
	                       AND tcdt.DmSanPhamREF IN (140, 228,241, 564, 549, 385)
	                       AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, DonViTinh) = 1
	                       --AND tcdt.DmHinhThucQuangCao = 5
	                       --AND tcdt.DonViTinh = N'NGÀY' 
	                GROUP BY
	                       tcdt.sohopdong,
	                       tcdt.hopdongchitietref,
	                       tcdt.Soluong	    
	            ) B
	            ON  (
	                    a.SoHopDong = b.SoHopDong
	                    AND a.HopDongChiTietREF = b.hopdongchitietref
	            )
	--WHERE
	--(a.ThanhTienSauCK - ISNULL(b.ThanhTienSauCK, 0)) <> 0
	--OR 
	--(a.ThanhTienSauCK - ISNULL(b.ThanhTienSauCK, 0)) IS NULL	 
	ORDER BY
	       --b.NgayThucHien, 
	       a.SoHopDong,
	       a.HopDongChiTietREF
END

```
