# Function: `fn_TC_Get_ThuThu_HopDongChiTietID_PR_KM`

- **Loại**: SQL_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2019-04-22 15:28:21.390000
- **Ngày sửa cuối**: 2019-10-15 15:38:40.173000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayHopDongChiTietPRID` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@ChietKhau` | `float(8)` | No |
| `@ThucChayHopDongChiTietPrREF` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmHinhThucQuangCaoREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@DonGia` | `int(4)` | No |
| `@SoLuong` | `int(4)` | No |

## Definition (Source Code)

```sql
/*
select  [dbo].[fn_Get_HopDongChiTietID_For_PR_v2]
(
	@HopDongREF ,
	@ChietKhau ,
	@ThucChayHopDongChiTietPRID ,
	@HopDongChiTietREF ,
	@DmHinhThucQuangCaoREF ,
	@DmSanPhamREF ,
	@DmWebsiteREF ,
	@DonGia 
)

*/
CREATE FUNCTION [dbo].[fn_TC_Get_ThuThu_HopDongChiTietID_PR_KM]
    (
      @ThucChayHopDongChiTietPRID INT ,
      @HopDongREF INT ,
      @ChietKhau FLOAT ,
      @ThucChayHopDongChiTietPrREF INT ,
      @HopDongChiTietREF INT ,
      @DmHinhThucQuangCaoREF INT ,
      @DmSanPhamREF INT ,
      @DmWebsiteREF INT ,
      @DonGia INT ,
      @SoLuong INT
    )
RETURNS @ListID TABLE
    (
      HopDongChiTietID INT ,
      ThucChayHopDongChiTietPRID INT,
	  vitri INT
    )
AS
    BEGIN
        DECLARE @ThanhTien FLOAT;
        DECLARE @ThanhTienThucChay FLOAT;

        DECLARE @ListHopDongChiTietID TABLE
            (
              HopDongChiTietID INT ,
              ThucChayHopDongChiTietPRID INT ,
              HopDongID INT ,
              DmSanPhamREF INT ,
              ThanhTienTrươcCK FLOAT ,
              ThanhTienThucChayKM FLOAT,
			  Vitri INT
            );

        DECLARE @ListThanhTienThucChay_HDCT TABLE
            (
              HopDongChiTietID INT ,
              ThanhTienThucChayKM FLOAT
            )


        DECLARE @ThanhTienThucTreo FLOAT

        SELECT  @ThanhTienThucTreo = ROUND(ISNULL(tchdctp.GiaTien, 0)
                * ISNULL(tchdctp.SoLuong, 0), 2)

        FROM    dbo.ThucChayHopDongChiTietPR tchdctp
        WHERE   tchdctp.ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID


        INSERT  INTO @ListThanhTienThucChay_HDCT
                SELECT  tcdt.HopDongChiTietREF ,
                        ISNULL(SUM(ISNULL(tcdt.ThanhTienKM, 0)
                            + ISNULL(tcdt.GiaTriKMThayDoi, 0)), 0) ThanhTienThucChay
                FROM    dbo.ThucChayDaTinh tcdt
                WHERE   tcdt.HopDongID = @HopDongREF
                GROUP BY tcdt.HopDongChiTietREF
			
		

        SET @ThanhTienThucTreo = ISNULL(@ThanhTienThucTreo, 0)


        --1. FULL DIEU KIEN TINH HTQC, SANPHAM, CHIETKHAU, KHONGMUANGOAI, WEBSITE, DONGIA, CHIPHI HOAC KHONG
        INSERT  INTO @ListHopDongChiTietID
                SELECT TOP (1) T2.*,1 AS Vitri
                FROM    ( SELECT *
                          FROM      ( SELECT    hdct.HopDongChiTietID ,
                                                @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                hdct.HopDongFK ,
                                                hdct.DmSanPhamREF ,
                                                hdct.DonGia*hdct.SoLuong AS ThanhTienKM ,
                                                SUM(tcdt.ThanhTienThucChay) AS ThanhTienThucChay
                                      FROM      (SELECT tcdt.HopDongID, tcdt.HopDongChiTietREF
												, SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay, 0) + ISNULL(tcdt.GiaTriThayDoi, 0))ThanhTienThucChay  
													FROM dbo.ThucChayDaTinh tcdt 
													WHERE  tcdt.HopDongID = @HopDongREF
													  AND tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCaoREF 
													  AND DmSanPhamREF = @DmSanPhamREF
													  GROUP BY tcdt.HopDongID, tcdt.HopDongChiTietREF, tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF
												)tcdt
                                                RIGHT JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongFK = tcdt.HopDongID
                                                              AND hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
                                      WHERE     hdct.HopDongFK = @HopDongREF
                                                AND hdct.DmSanPhamREF IN ( 141, 245, 250, 637, 305 ) --PR
                                                AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
                                                AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                AND hdct.DeletedStatus = 0
                                                AND hdct.ChietKhau = @ChietKhau
												AND hdct.ChietKhau = 100
                                                AND NOT ( hdct.DmLoaiREF = 13
                                                          OR hdct.DmLoaiBannerREF = 18
                                                        )--Mua ngoai
                                                AND ((hdct.DmWebsiteREF = @DmWebsiteREF)
												OR (hdct.DmWebsiteREF = 119 AND @DmWebsiteREF IN (5131,5132))) --hdct: Dan tri, tt: Dân trí - Mua Ngoài/Dân trí - Khuyến học
                                                AND hdct.DonGia = @DonGia
                                                AND ( ( ISNULL(@ThucChayHopDongChiTietPrREF, 0) <> 0 AND hdct.DmLoaiBannerREF = 17 )
                                                      OR ( ISNULL(@ThucChayHopDongChiTietPrREF, 0) = 0 AND hdct.DmLoaiBannerREF <> 17 )
                                                    )
                                                AND EXISTS(SELECT  HopDongChiTietID FROM @ListHopDongChiTietID WHERE HopDongChiTietID = hdct.HopDongChiTietID )
                                      GROUP BY  hdct.HopDongFK ,
                                                hdct.HopDongChiTietID ,
                                                hdct.DmSanPhamREF ,
                                                hdct.DonGia,
												hdct.SoLuong
                                    ) T
                        ) T2
                        LEFT JOIN @ListThanhTienThucChay_HDCT ltttch ON T2.HopDongChiTietID = ltttch.HopDongChiTietID
                WHERE   ( T2.ThanhTienKM - (ISNULL(ltttch.ThanhTienThucChayKM, 0)
                          + @ThanhTienThucTreo) ) >= 0
                ORDER BY  T2.HopDongChiTietID

        --2. CUNG: HTQC, SANPHAM, CHIETKHAU, KHONGMUANGOAI, WEBSITE, DONGIA -- KHAC: CUNG CHI PHI
        IF NOT EXISTS ( SELECT * FROM @ListHopDongChiTietID lhdcti WHERE lhdcti.Vitri = 1)
            BEGIN
                INSERT  INTO @ListHopDongChiTietID
                        SELECT TOP (1) T2.*,2 AS Vitri
                        FROM    ( SELECT 
                                            *
                                  FROM      ( SELECT    hdct.HopDongChiTietID ,
                                                        @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                        hdct.HopDongFK ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.DonGia*hdct.SoLuong AS ThanhTienKM ,
                                                        SUM(tcdt.ThanhTienThucChay) AS ThanhTienThucChay
											 FROM      (SELECT tcdt.HopDongID, tcdt.HopDongChiTietREF
															, SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay, 0) + ISNULL(tcdt.GiaTriThayDoi, 0))ThanhTienThucChay  
																FROM dbo.ThucChayDaTinh tcdt 
																WHERE  tcdt.HopDongID = @HopDongREF
																  AND tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCaoREF 
																  AND DmSanPhamREF = @DmSanPhamREF
																  GROUP BY tcdt.HopDongID, tcdt.HopDongChiTietREF, tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF
												)tcdt
                                                        RIGHT JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongFK = tcdt.HopDongID
                                                              AND hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
                                              WHERE     hdct.HopDongFK = @HopDongREF
                                                        AND hdct.DmSanPhamREF IN ( 141, 245, 250, 637, 305 ) --PR
                                                        AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
                                                        AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                        AND hdct.DeletedStatus = 0
                                                        AND hdct.ChietKhau = @ChietKhau
														AND hdct.ChietKhau = 100
                                                        AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )--Mua ngoai
                                                        AND ((hdct.DmWebsiteREF = @DmWebsiteREF)
														OR (hdct.DmWebsiteREF = 119 AND @DmWebsiteREF IN (5131,5132))) --hdct: Dan tri, tt: Dân trí - Mua Ngoài/Dân trí - Khuyến học
                                                        AND hdct.DonGia = @DonGia
                                              GROUP BY  hdct.HopDongFK ,
                                                        hdct.HopDongChiTietID ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.DonGia,
														hdct.SoLuong
                                            ) T
                                ) T2
                                LEFT JOIN @ListThanhTienThucChay_HDCT ltttch ON T2.HopDongChiTietID = ltttch.HopDongChiTietID
                        WHERE   ( T2.ThanhTienKM - (ISNULL(ltttch.ThanhTienThucChayKM, 0)
                                  + @ThanhTienThucTreo) ) >= 0
						ORDER BY  T2.HopDongChiTietID

            END
		--3. CUNG: HTQC, SANPHAM, CHIETKHAU, WEBSITE , CUNG CHI PHI HOAC KHONG -- KHAC: DONGIA
        IF NOT EXISTS ( SELECT  *
                        FROM    @ListHopDongChiTietID lhdcti WHERE lhdcti.Vitri IN(1, 2))
            BEGIN
                INSERT  INTO @ListHopDongChiTietID
                        SELECT TOP (1) T2.*,3 AS Vitri
                        FROM    ( SELECT 
                                            *
                                  FROM      ( SELECT    hdct.HopDongChiTietID ,
                                                        @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                        hdct.HopDongFK ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.DonGia*hdct.SoLuong AS ThanhTienKM ,
                                                        SUM(tcdt.ThanhTienThucChay) AS ThanhTienThucChay
											 FROM      (SELECT tcdt.HopDongID, tcdt.HopDongChiTietREF
															, SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay, 0) + ISNULL(tcdt.GiaTriThayDoi, 0))ThanhTienThucChay  
																FROM dbo.ThucChayDaTinh tcdt 
																WHERE  tcdt.HopDongID = @HopDongREF
																  AND tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCaoREF 
																  AND DmSanPhamREF = @DmSanPhamREF
																  GROUP BY tcdt.HopDongID, tcdt.HopDongChiTietREF, tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF
												)tcdt
                                                        RIGHT JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongFK = tcdt.HopDongID
                                                              AND hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
                                              WHERE     hdct.HopDongFK = @HopDongREF
                                                        AND hdct.DmSanPhamREF IN ( 141, 245, 250, 637, 305 ) --PR
                                                        AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
                                                        AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                        AND hdct.DeletedStatus = 0
                                                        AND hdct.ChietKhau = @ChietKhau
														AND hdct.ChietKhau = 100
                                                        AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )--Mua ngoai
                                                        AND ((hdct.DmWebsiteREF = @DmWebsiteREF)
														OR (hdct.DmWebsiteREF = 119 AND @DmWebsiteREF IN (5131,5132))) --hdct: Dan tri, tt: Dân trí - Mua Ngoài/Dân trí - Khuyến học
                                                        AND hdct.DonGia <> @DonGia
                                                        AND ( ( ISNULL(@ThucChayHopDongChiTietPrREF, 0) <> 0 AND hdct.DmLoaiBannerREF = 17 )
                                                              OR ( ISNULL(@ThucChayHopDongChiTietPrREF, 0) = 0 AND hdct.DmLoaiBannerREF <> 17 )
                                                            )
                                              GROUP BY  hdct.HopDongFK ,
                                                        hdct.HopDongChiTietID ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.DonGia,
														hdct.SoLuong
                                            ) T
                                ) T2
                                LEFT JOIN @ListThanhTienThucChay_HDCT ltttch ON T2.HopDongChiTietID = ltttch.HopDongChiTietID
                        WHERE   ( T2.ThanhTienKM - (ISNULL(ltttch.ThanhTienThucChayKM, 0)
                                  + @ThanhTienThucTreo) ) >= 0
						ORDER BY  T2.HopDongChiTietID

            END

		--4. CUNG: HTQC, SANPHAM, CHIETKHAU, WEBSITE  -- KHAC: DONGIA, KHONG CUNG CHI PHI HOAC KHONG
        IF NOT EXISTS ( SELECT  *
                        FROM    @ListHopDongChiTietID lhdcti WHERE lhdcti.Vitri IN(1,2,3))
            BEGIN
                INSERT  INTO @ListHopDongChiTietID
                        SELECT TOP (1) T2.*,4 AS Vitri
                        FROM    ( SELECT 
                                            *
                                  FROM      ( SELECT    hdct.HopDongChiTietID ,
                                                        @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                        hdct.HopDongFK ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.DonGia*hdct.SoLuong AS ThanhTienKM ,
                                                        SUM(tcdt.ThanhTienThucChay) AS ThanhTienThucChay
											 FROM      (SELECT tcdt.HopDongID, tcdt.HopDongChiTietREF
															, SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay, 0) + ISNULL(tcdt.GiaTriThayDoi, 0))ThanhTienThucChay  
																FROM dbo.ThucChayDaTinh tcdt 
																WHERE  tcdt.HopDongID = @HopDongREF
																  AND tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCaoREF 
																  AND DmSanPhamREF = @DmSanPhamREF
																  GROUP BY tcdt.HopDongID, tcdt.HopDongChiTietREF, tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF
												)tcdt
                                                        RIGHT JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongFK = tcdt.HopDongID
                                                              AND hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
                                              WHERE     hdct.HopDongFK = @HopDongREF
                                                        AND hdct.DmSanPhamREF IN ( 141, 245, 250, 637, 305 ) --PR
                                                        AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
                                                        AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                        AND hdct.DeletedStatus = 0
                                                        AND hdct.ChietKhau = @ChietKhau
														AND hdct.ChietKhau = 100
                                                        AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )--Mua ngoai
                                                        AND ((hdct.DmWebsiteREF = @DmWebsiteREF)
														OR (hdct.DmWebsiteREF = 119 AND @DmWebsiteREF IN (5131,5132))) --hdct: Dan tri, tt: Dân trí - Mua Ngoài/Dân trí - Khuyến học
                                                        AND hdct.DonGia <> @DonGia
                                              GROUP BY  hdct.HopDongFK ,
                                                        hdct.HopDongChiTietID ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.DonGia,
														hdct.SoLuong
                                            ) T
                                ) T2
                                LEFT JOIN @ListThanhTienThucChay_HDCT ltttch ON T2.HopDongChiTietID = ltttch.HopDongChiTietID
                        WHERE   ( T2.ThanhTienKM - (ISNULL(ltttch.ThanhTienThucChayKM, 0)
                                  + @ThanhTienThucTreo) ) >= 0
						ORDER BY  T2.HopDongChiTietID

            END
		--5. CUNG: HTQC, SANPHAM, CHIETKHAU, DONGIA, CUNG CHIPHI HOAC KHONG -- KHAC: SITE BLANK,
        IF NOT EXISTS ( SELECT  *
                        FROM    @ListHopDongChiTietID lhdcti WHERE lhdcti.Vitri IN(1, 2,3,4))
            BEGIN
                INSERT  INTO @ListHopDongChiTietID
                        SELECT TOP (1) T2.*,5 AS Vitri
                        FROM    ( SELECT 
                                            *
                                  FROM      ( SELECT    hdct.HopDongChiTietID ,
                                                        @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                        hdct.HopDongFK ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.DonGia*hdct.SoLuong AS ThanhTienKM ,
														SUM(tcdt.ThanhTienThucChay) AS ThanhTienThucChay
											 FROM      (SELECT tcdt.HopDongID, tcdt.HopDongChiTietREF
															, SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay, 0) + ISNULL(tcdt.GiaTriThayDoi, 0))ThanhTienThucChay  
																FROM dbo.ThucChayDaTinh tcdt 
																WHERE  tcdt.HopDongID = @HopDongREF
																  AND tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCaoREF 
																  AND DmSanPhamREF = @DmSanPhamREF
																  GROUP BY tcdt.HopDongID, tcdt.HopDongChiTietREF, tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF
												)tcdt
                                                        RIGHT JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongFK = tcdt.HopDongID
                                                              AND hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
                                              WHERE     hdct.HopDongFK = @HopDongREF
                                                        AND hdct.DmSanPhamREF IN ( 141, 245, 250, 637, 305 ) --PR
                                                        AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
                                                        AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                        AND hdct.DeletedStatus = 0
                                                        AND hdct.ChietKhau = @ChietKhau
														AND hdct.ChietKhau = 100
                                                        AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )--Mua ngoai
                                                        AND ( hdct.DmWebsiteREF = 265 OR hdct.DmWebsiteREF IS NULL ) --SITE BLANK
														AND hdct.DonGia = @DonGia --HAIDH COMMENT SUA CHO NAY VI CO CHI PHI CUNG DONGIA NHUNG SITE BLANK
                                                        AND ( ( ISNULL(@ThucChayHopDongChiTietPrREF, 0) <> 0 AND hdct.DmLoaiBannerREF = 17 )
                                                              OR ( ISNULL(@ThucChayHopDongChiTietPrREF, 0) = 0 AND hdct.DmLoaiBannerREF <> 17 )
                                                            )
                                              GROUP BY  hdct.HopDongFK ,
                                                        hdct.HopDongChiTietID ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.DonGia,
														hdct.SoLuong
                                            ) T
                                ) T2
                                LEFT JOIN @ListThanhTienThucChay_HDCT ltttch ON T2.HopDongChiTietID = ltttch.HopDongChiTietID
                        WHERE   ( T2.ThanhTienKM - (ISNULL(ltttch.ThanhTienThucChayKM, 0)
                                  + @ThanhTienThucTreo) ) >= 0
						ORDER BY  T2.HopDongChiTietID

            END
		--6. CUNG: HTQC, SANPHAM, CHIETKHAU, DONGIA -- KHAC:  SITE BLANK, KHONG CUNG CHIPHI HOAC KHONG
        IF NOT EXISTS ( SELECT  *
                        FROM    @ListHopDongChiTietID lhdcti WHERE lhdcti.Vitri IN(1, 2,3,4,5))
            BEGIN
                INSERT  INTO @ListHopDongChiTietID
                        SELECT TOP (1) T2.*,6 AS Vitri
                        FROM    ( SELECT 
                                            *
                                  FROM      ( SELECT    hdct.HopDongChiTietID ,
                                                        @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                        hdct.HopDongFK ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.DonGia*hdct.SoLuong AS ThanhTienKM ,
                                                        SUM(tcdt.ThanhTienThucChay) AS ThanhTienThucChay
											 FROM      (SELECT tcdt.HopDongID, tcdt.HopDongChiTietREF
															, SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay, 0) + ISNULL(tcdt.GiaTriThayDoi, 0))ThanhTienThucChay  
																FROM dbo.ThucChayDaTinh tcdt 
																WHERE  tcdt.HopDongID = @HopDongREF
																  AND tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCaoREF 
																  AND DmSanPhamREF = @DmSanPhamREF
																  GROUP BY tcdt.HopDongID, tcdt.HopDongChiTietREF, tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF
														)tcdt
                                                        RIGHT JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongFK = tcdt.HopDongID
                                                              AND hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
                                              WHERE     hdct.HopDongFK = @HopDongREF
                                                        AND hdct.DmSanPhamREF IN ( 141, 245, 250, 637,305 ) --PR
                                                        AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
                                                        AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                        AND hdct.DeletedStatus = 0
                                                        AND hdct.ChietKhau = @ChietKhau
														AND hdct.ChietKhau = 100
                                                        AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )--Mua ngoai
                                                        AND ( hdct.DmWebsiteREF = 265 OR hdct.DmWebsiteREF IS NULL ) -- site blank
														AND hdct.DonGia = @DonGia 
                                              GROUP BY  hdct.HopDongFK ,
                                                        hdct.HopDongChiTietID ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.DonGia,
														hdct.SoLuong
                                            ) T
                                ) T2
                                LEFT JOIN @ListThanhTienThucChay_HDCT ltttch ON T2.HopDongChiTietID = ltttch.HopDongChiTietID
                        WHERE   ( T2.ThanhTienKM - (ISNULL(ltttch.ThanhTienThucChayKM, 0)
                                  + @ThanhTienThucTreo) ) >= 0
						ORDER BY  T2.HopDongChiTietID

            END
		--7. HTQC, SANPHAM, CHIETKHAU -- KHAC: SITE BLANK, DONGIA, KHONG CUNG CHIPHI HOAC KHONG
        IF NOT EXISTS ( SELECT  *
                        FROM    @ListHopDongChiTietID lhdcti WHERE lhdcti.Vitri IN(1, 2,3,4,5,6))
            BEGIN
                INSERT  INTO @ListHopDongChiTietID
                        SELECT TOP (1) T2.*,7 AS Vitri
                        FROM    ( SELECT 
                                            *
                                  FROM      ( SELECT    hdct.HopDongChiTietID ,
                                                        @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                        hdct.HopDongFK ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.DonGia*hdct.SoLuong AS ThanhTienKM ,
                                                        SUM(tcdt.ThanhTienThucChay) AS ThanhTienThucChay
											 FROM      (SELECT tcdt.HopDongID, tcdt.HopDongChiTietREF
															, SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay, 0) + ISNULL(tcdt.GiaTriThayDoi, 0))ThanhTienThucChay  
																FROM dbo.ThucChayDaTinh tcdt 
																WHERE  tcdt.HopDongID = @HopDongREF
																  AND tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCaoREF 
																  AND DmSanPhamREF = @DmSanPhamREF
																  GROUP BY tcdt.HopDongID, tcdt.HopDongChiTietREF, tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF
												)tcdt
                                                        RIGHT JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongFK = tcdt.HopDongID
                                                              AND hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
                                              WHERE     hdct.HopDongFK = @HopDongREF
                                                        AND hdct.DmSanPhamREF IN (141, 245, 250, 637,305 ) --PR
                                                        AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
                                                        AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                        AND hdct.DeletedStatus = 0
                                                        AND hdct.ChietKhau = @ChietKhau
														AND hdct.ChietKhau = 100
                                                        AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )--Mua ngoai
                                                        AND ( hdct.DmWebsiteREF = 265 OR hdct.DmWebsiteREF IS NULL )
                                              GROUP BY  hdct.HopDongFK ,
                                                        hdct.HopDongChiTietID ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.DonGia,
														hdct.SoLuong
                                            ) T
                                ) T2
                                LEFT JOIN @ListThanhTienThucChay_HDCT ltttch ON T2.HopDongChiTietID = ltttch.HopDongChiTietID
                        WHERE   ( T2.ThanhTienKM - (ISNULL(ltttch.ThanhTienThucChayKM, 0)
                                  + @ThanhTienThucTreo) ) >= 0
						ORDER BY  T2.HopDongChiTietID
            END

		--8. HTQC, SANPHAM, CHIETKHAU, SITE, DONVI GOI
		IF NOT EXISTS ( SELECT  *
                        FROM    @ListHopDongChiTietID lhdcti WHERE lhdcti.Vitri IN(1, 2,3,4,5,6,7))
            BEGIN
                INSERT  INTO @ListHopDongChiTietID
                        SELECT TOP (1) T2.*,8 AS Vitri
                        FROM    ( SELECT 
                                            *
                                  FROM      ( SELECT    hdct.HopDongChiTietID ,
                                                        @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                        hdct.HopDongFK ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.DonGia*hdct.SoLuong AS ThanhTienKM ,
                                                        SUM(tcdt.ThanhTienThucChay) AS ThanhTienThucChay
											 FROM      (SELECT tcdt.HopDongID, tcdt.HopDongChiTietREF
															, SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay, 0) + ISNULL(tcdt.GiaTriThayDoi, 0))ThanhTienThucChay  
																FROM dbo.ThucChayDaTinh tcdt 
																WHERE  tcdt.HopDongID = @HopDongREF
																  AND tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCaoREF 
																  AND DmSanPhamREF = @DmSanPhamREF
																  GROUP BY tcdt.HopDongID, tcdt.HopDongChiTietREF, tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF
												)tcdt
                                                        RIGHT JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongFK = tcdt.HopDongID
                                                              AND hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
                                              WHERE     hdct.HopDongFK = @HopDongREF
                                                        AND hdct.DmSanPhamREF IN (
                                                        141, 245, 250, 637,
                                                        305 ) --PR
                                                        AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
                                                        AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                        AND hdct.DeletedStatus = 0
                                                        AND hdct.ChietKhau = @ChietKhau
														AND hdct.ChietKhau = 100
                                                        AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )--Mua ngoai
                                                        AND ((hdct.DmWebsiteREF = @DmWebsiteREF)
														OR (hdct.DmWebsiteREF = 119 AND @DmWebsiteREF IN (5131,5132))) --hdct: Dan tri, tt: Dân trí - Mua Ngoài/Dân trí - Khuyến học
                                                        AND hdct.DonViTinhREF = 10
                                              GROUP BY  hdct.HopDongFK ,
                                                        hdct.HopDongChiTietID ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.DonGia,
														hdct.SoLuong
                                            ) T
                                ) T2
                                LEFT JOIN @ListThanhTienThucChay_HDCT ltttch ON T2.HopDongChiTietID = ltttch.HopDongChiTietID
                        WHERE   ( T2.ThanhTienKM - (ISNULL(ltttch.ThanhTienThucChayKM, 0)
                                  + @ThanhTienThucTreo) ) >= 0
						ORDER BY  T2.HopDongChiTietID
            END


		--9. HTQC, SANPHAM, CHIETKHAU, DONGIA, CUNG CHIPHI HOAC KHONG, KHONG MUA NGOAI		
		IF NOT EXISTS ( SELECT  *
                        FROM    @ListHopDongChiTietID lhdcti WHERE lhdcti.Vitri IN(1, 2,3,4,5,6,7,8))
            BEGIN
                INSERT  INTO @ListHopDongChiTietID
                        SELECT TOP (1) T2.*,9 AS Vitri
                        FROM    ( SELECT 
                                            *
                                  FROM      ( SELECT    hdct.HopDongChiTietID ,
                                                        @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                        hdct.HopDongFK ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.DonGia*hdct.SoLuong AS ThanhTienKM ,
                                                        SUM(tcdt.ThanhTienThucChay) AS ThanhTienThucChay
											 FROM      (SELECT tcdt.HopDongID, tcdt.HopDongChiTietREF
															, SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay, 0) + ISNULL(tcdt.GiaTriThayDoi, 0))ThanhTienThucChay  
																FROM dbo.ThucChayDaTinh tcdt 
																WHERE  tcdt.HopDongID = @HopDongREF
																  AND tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCaoREF 
																  AND DmSanPhamREF = @DmSanPhamREF
																  GROUP BY tcdt.HopDongID, tcdt.HopDongChiTietREF, tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF
												)tcdt
                                                        RIGHT JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongFK = tcdt.HopDongID
                                                              AND hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
                                              WHERE     hdct.HopDongFK = @HopDongREF
                                                        AND hdct.DmSanPhamREF IN ( 141, 245, 250, 637, 305 ) --PR
                                                        AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
                                                        AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                        AND hdct.DeletedStatus = 0
                                                        AND hdct.ChietKhau = @ChietKhau
														AND hdct.ChietKhau = 100
                                                        AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )--Mua ngoai
                                                        AND hdct.DonGia = @DonGia
														AND ((hdct.DmWebsiteREF = @DmWebsiteREF)
														OR (hdct.DmWebsiteREF = 119 AND @DmWebsiteREF IN (5131,5132))) --hdct: Dan tri, tt: Dân trí - Mua Ngoài/Dân trí - Khuyến học
                                                        AND ( ( ISNULL(@ThucChayHopDongChiTietPrREF, 0) <> 0 AND hdct.DmLoaiBannerREF = 17)
																OR ( ISNULL(@ThucChayHopDongChiTietPrREF, 0) = 0 AND hdct.DmLoaiBannerREF <> 17 ) )
                                              GROUP BY  hdct.HopDongFK ,
                                                        hdct.HopDongChiTietID ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.DonGia,
														hdct.SoLuong
                                            ) T
                                ) T2
                                LEFT JOIN @ListThanhTienThucChay_HDCT ltttch ON T2.HopDongChiTietID = ltttch.HopDongChiTietID
                        WHERE   ( T2.ThanhTienKM - (ISNULL(ltttch.ThanhTienThucChayKM, 0)
                                  + @ThanhTienThucTreo) ) >= 0
						ORDER BY  T2.HopDongChiTietID
            END
                  

        INSERT  INTO @ListID
                SELECT DISTINCT
                        HopDongChiTietID ,
                        ThucChayHopDongChiTietPRID,
						Vitri
                FROM    @ListHopDongChiTietID

        RETURN;
    END;


```
