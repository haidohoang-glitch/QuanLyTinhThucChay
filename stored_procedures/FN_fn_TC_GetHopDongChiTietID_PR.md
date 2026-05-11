# Function: `fn_TC_GetHopDongChiTietID_PR`

- **Loại**: SQL_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2017-05-08 10:47:52.390000
- **Ngày sửa cuối**: 2018-10-15 16:36:37.453000

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
| `@DonGia` | `bigint(8)` | No |
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
CREATE FUNCTION [dbo].[fn_TC_GetHopDongChiTietID_PR]
    (
      @ThucChayHopDongChiTietPRID INT ,
      @HopDongREF INT ,
      @ChietKhau FLOAT ,
      @ThucChayHopDongChiTietPrREF INT ,
      @HopDongChiTietREF INT ,
      @DmHinhThucQuangCaoREF INT ,
      @DmSanPhamREF INT ,
      @DmWebsiteREF INT ,
      @DonGia BIGINT ,
      @SoLuong INT
    )
RETURNS @ListID TABLE
    (
      HopDongChiTietID INT ,
      ThucChayHopDongChiTietPRID INT
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
              ThanhTien FLOAT ,
              ThanhTienThucChay FLOAT
            );

        DECLARE @ListThanhTienThucChay_HDCT TABLE
            (
              HopDongChiTietID INT ,
              ThanhTienThucChay FLOAT
            )


        DECLARE @ThanhTienThucTreo FLOAT

        SELECT  @ThanhTienThucTreo = ROUND(ISNULL(tchdctp.GiaTien, 0)
                * ISNULL(tchdctp.SoLuong, 0) * ( CONVERT(FLOAT, ( 100
                                                              - tchdctp.ChietKhau ))
                                                 / 100 ), 2)
        FROM    dbo.ThucChayHopDongChiTietPR tchdctp
        WHERE   tchdctp.ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID


        INSERT  INTO @ListThanhTienThucChay_HDCT
                SELECT  tcdt.HopDongChiTietREF ,
                        ISNULL(SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay, 0)
                            + ISNULL(tcdt.GiaTriThayDoi, 0)), 0) ThanhTienThucChay
                FROM    dbo.ThucChayDaTinh tcdt
                WHERE   tcdt.HopDongID = @HopDongREF
                GROUP BY tcdt.HopDongChiTietREF
			
		

        SET @ThanhTienThucTreo = ISNULL(@ThanhTienThucTreo, 0)


        --1. FULL DIEU KIEN TINH HTQC, SANPHAM, CHIETKHAU, KHONGMUANGOAI, WEBSITE, DONGIA, CHIPHI HOAC KHONG
        INSERT  INTO @ListHopDongChiTietID
                SELECT TOP 1 T2.*
                FROM    ( SELECT *
                          FROM      ( SELECT    hdct.HopDongChiTietID ,
                                                @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                hdct.HopDongFK ,
                                                hdct.DmSanPhamREF ,
                                                hdct.ThanhTien ,
                                                SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,
                                                           0)
                                                    + ISNULL(tcdt.GiaTriThayDoi,
                                                             0)) ThanhTienThucChay
                                      FROM      ThucChayDaTinh tcdt
                                                RIGHT JOIN HopDongChiTiet hdct ON hdct.HopDongFK = tcdt.HopDongID
                                                              AND hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
                                      WHERE     hdct.HopDongFK = @HopDongREF
                                                AND hdct.DmSanPhamREF IN ( 141,
                                                              245, 250, 637,
                                                              305 ) --PR
                                                AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
                                                AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                AND hdct.DeletedStatus = 0
                                                AND hdct.ChietKhau = @ChietKhau
                                                AND NOT ( hdct.DmLoaiREF = 13
                                                          OR hdct.DmLoaiBannerREF = 18
                                                        )--Mua ngoai
                                                AND hdct.DmWebsiteREF = @DmWebsiteREF
                                                AND hdct.DonGia = @DonGia
                                                AND ( ( ISNULL(@ThucChayHopDongChiTietPrREF,
                                                              0) <> 0
                                                        AND hdct.DmLoaiBannerREF = 17
                                                      )
                                                      OR ( ISNULL(@ThucChayHopDongChiTietPrREF,
                                                              0) = 0
                                                           AND hdct.DmLoaiBannerREF <> 17
                                                         )
                                                    )
                                                AND hdct.HopDongChiTietID NOT IN (
                                                SELECT  HopDongChiTietID
                                                FROM    @ListHopDongChiTietID )
                                      GROUP BY  hdct.HopDongFK ,
                                                hdct.HopDongChiTietID ,
                                                hdct.DmSanPhamREF ,
                                                hdct.ThanhTien
                                    ) T
                        ) T2
                        LEFT JOIN @ListThanhTienThucChay_HDCT ltttch ON T2.HopDongChiTietID = ltttch.HopDongChiTietID
                WHERE   ( ThanhTien - (ISNULL(ltttch.ThanhTienThucChay, 0)
                          + @ThanhTienThucTreo) ) >= 0
                ORDER BY  T2.HopDongChiTietID

        --2. CUNG HTQC, SANPHAM, CHIETKHAU, KHONGMUANGOAI, WEBSITE, DONGIA
        IF NOT EXISTS ( SELECT  *
                        FROM    @ListHopDongChiTietID lhdcti )
            BEGIN
                INSERT  INTO @ListHopDongChiTietID
                        SELECT TOP 1 T2.*
                        FROM    ( SELECT 
                                            *
                                  FROM      ( SELECT    hdct.HopDongChiTietID ,
                                                        @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                        hdct.HopDongFK ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.ThanhTien ,
                                                        SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,
                                                              0)
                                                            + ISNULL(tcdt.GiaTriThayDoi,
                                                              0)) ThanhTienThucChay
                                              FROM      ThucChayDaTinh tcdt
                                                        RIGHT JOIN HopDongChiTiet hdct ON hdct.HopDongFK = tcdt.HopDongID
                                                              AND hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
                                              WHERE     hdct.HopDongFK = @HopDongREF
                                                        AND hdct.DmSanPhamREF IN (
                                                        141, 245, 250, 637,
                                                        305 ) --PR
                                                        AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
                                                        AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                        AND hdct.DeletedStatus = 0
                                                        AND hdct.ChietKhau = @ChietKhau
                                                        AND NOT ( hdct.DmLoaiREF = 13
                                                              OR hdct.DmLoaiBannerREF = 18
                                                              )--Mua ngoai
                                                        AND hdct.DmWebsiteREF = @DmWebsiteREF
                                                        AND hdct.DonGia = @DonGia
                                              GROUP BY  hdct.HopDongFK ,
                                                        hdct.HopDongChiTietID ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.ThanhTien
                                            ) T
                                ) T2
                                LEFT JOIN @ListThanhTienThucChay_HDCT ltttch ON T2.HopDongChiTietID = ltttch.HopDongChiTietID
                        WHERE   ( ThanhTien - (ISNULL(ltttch.ThanhTienThucChay, 0)
                                  + @ThanhTienThucTreo) ) >= 0
						ORDER BY  T2.HopDongChiTietID

            END
		--3. CUNG HTQC, SANPHAM, CHIETKHAU, WEBSITE, KHAC DONGIA
        IF NOT EXISTS ( SELECT  *
                        FROM    @ListHopDongChiTietID lhdcti )
            BEGIN
                INSERT  INTO @ListHopDongChiTietID
                        SELECT TOP 1 T2.*
                        FROM    ( SELECT 
                                            *
                                  FROM      ( SELECT    hdct.HopDongChiTietID ,
                                                        @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                        hdct.HopDongFK ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.ThanhTien ,
                                                        SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,
                                                              0)
                                                            + ISNULL(tcdt.GiaTriThayDoi,
                                                              0)) ThanhTienThucChay
                                              FROM      ThucChayDaTinh tcdt
                                                        RIGHT JOIN HopDongChiTiet hdct ON hdct.HopDongFK = tcdt.HopDongID
                                                              AND hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
                                              WHERE     hdct.HopDongFK = @HopDongREF
                                                        AND hdct.DmSanPhamREF IN (
                                                        141, 245, 250, 637,
                                                        305 ) --PR
                                                        AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
                                                        AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                        AND hdct.DeletedStatus = 0
                                                        AND hdct.ChietKhau = @ChietKhau
                                                        AND NOT ( hdct.DmLoaiREF = 13
                                                              OR hdct.DmLoaiBannerREF = 18
                                                              )--Mua ngoai
                                                        AND hdct.DmWebsiteREF = @DmWebsiteREF
                                                        AND hdct.DonGia <> @DonGia
                                                        AND ( ( ISNULL(@ThucChayHopDongChiTietPrREF,
                                                              0) <> 0
                                                              AND hdct.DmLoaiBannerREF = 17
                                                              )
                                                              OR ( ISNULL(@ThucChayHopDongChiTietPrREF,
                                                              0) = 0
                                                              AND hdct.DmLoaiBannerREF <> 17
                                                              )
                                                            )
                                              GROUP BY  hdct.HopDongFK ,
                                                        hdct.HopDongChiTietID ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.ThanhTien
                                            ) T
                                ) T2
                                LEFT JOIN @ListThanhTienThucChay_HDCT ltttch ON T2.HopDongChiTietID = ltttch.HopDongChiTietID
                        WHERE   ( T2.ThanhTien - (ISNULL(ltttch.ThanhTienThucChay, 0)
                                  + @ThanhTienThucTreo) ) >= 0
						ORDER BY  T2.HopDongChiTietID

            END
		--4. CUNG HTQC, SANPHAM, CHIETKHAU, SITE BLANK, DONGIA, CUNG CHIPHI HOAC KHONG, KHONGMUANGOAI
        IF NOT EXISTS ( SELECT  *
                        FROM    @ListHopDongChiTietID lhdcti )
            BEGIN
                INSERT  INTO @ListHopDongChiTietID
                        SELECT TOP 1 T2.*
                        FROM    ( SELECT 
                                            *
                                  FROM      ( SELECT    hdct.HopDongChiTietID ,
                                                        @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                        hdct.HopDongFK ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.ThanhTien ,
                                                        SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,
                                                              0)
                                                            + ISNULL(tcdt.GiaTriThayDoi,
                                                              0)) ThanhTienThucChay
                                              FROM      ThucChayDaTinh tcdt
                                                        RIGHT JOIN HopDongChiTiet hdct ON hdct.HopDongFK = tcdt.HopDongID
                                                              AND hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
                                              WHERE     hdct.HopDongFK = @HopDongREF
                                                        AND hdct.DmSanPhamREF IN (
                                                        141, 245, 250, 637,
                                                        305 ) --PR
                                                        AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
                                                        AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                        AND hdct.DeletedStatus = 0
                                                        AND hdct.ChietKhau = @ChietKhau
                                                        AND NOT ( hdct.DmLoaiREF = 13
                                                              OR hdct.DmLoaiBannerREF = 18
                                                              )--Mua ngoai
                                                        AND ( hdct.DmWebsiteREF = 265
                                                              OR hdct.DmWebsiteREF IS NULL
                                                            )
														AND hdct.DonGia = @DonGia --HAIDH COMMENT SUA CHO NAY VI CO CHI PHI CUNG DONGIA NHUNG SITE BLANK
                                                        AND ( ( ISNULL(@ThucChayHopDongChiTietPrREF,
                                                              0) <> 0
                                                              AND hdct.DmLoaiBannerREF = 17
                                                              )
                                                              OR ( ISNULL(@ThucChayHopDongChiTietPrREF,
                                                              0) = 0
                                                              AND hdct.DmLoaiBannerREF <> 17
                                                              )
                                                            )
                                              GROUP BY  hdct.HopDongFK ,
                                                        hdct.HopDongChiTietID ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.ThanhTien
                                            ) T
                                ) T2
                                LEFT JOIN @ListThanhTienThucChay_HDCT ltttch ON T2.HopDongChiTietID = ltttch.HopDongChiTietID
                        WHERE   ( T2.ThanhTien - (ISNULL(ltttch.ThanhTienThucChay, 0)
                                  + @ThanhTienThucTreo) ) >= 0
						ORDER BY  T2.HopDongChiTietID

            END
		--5. HTQC, SANPHAM, CHIETKHAU, SITE BLANK, CUNG CHIPHI HOAC KHONG, KHONG MUA NGOAI
        IF NOT EXISTS ( SELECT  *
                        FROM    @ListHopDongChiTietID lhdcti )
            BEGIN
                INSERT  INTO @ListHopDongChiTietID
                        SELECT TOP 1 T2.*
                        FROM    ( SELECT 
                                            *
                                  FROM      ( SELECT    hdct.HopDongChiTietID ,
                                                        @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                        hdct.HopDongFK ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.ThanhTien ,
                                                        SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,
                                                              0)
                                                            + ISNULL(tcdt.GiaTriThayDoi,
                                                              0)) ThanhTienThucChay
                                              FROM      dbo.ThucChayDaTinh tcdt
                                                        RIGHT JOIN HopDongChiTiet hdct ON hdct.HopDongFK = tcdt.HopDongID
                                                              AND hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
                                              WHERE     hdct.HopDongFK = @HopDongREF
                                                        AND hdct.DmSanPhamREF IN (
                                                        141, 245, 250, 637,
                                                        305 ) --PR
                                                        AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
                                                        AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                        AND hdct.DeletedStatus = 0
                                                        AND hdct.ChietKhau = @ChietKhau
                                                        AND NOT ( hdct.DmLoaiREF = 13
                                                              OR hdct.DmLoaiBannerREF = 18
                                                              )--Mua ngoai
                                                        AND ( hdct.DmWebsiteREF = 265
                                                              OR hdct.DmWebsiteREF IS NULL
                                                            )
                                            --AND hdct.DonGia = @DonGia
                                                        AND ( ( ISNULL(@ThucChayHopDongChiTietPrREF,
                                                              0) <> 0
                                                              AND hdct.DmLoaiBannerREF = 17
                                                              )
                                                              OR ( ISNULL(@ThucChayHopDongChiTietPrREF,
                                                              0) = 0
                                                              AND hdct.DmLoaiBannerREF <> 17
                                                              )
                                                              )
                                              GROUP BY  hdct.HopDongFK ,
                                                        hdct.HopDongChiTietID ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.ThanhTien
                                            ) T
                                ) T2
                                LEFT JOIN @ListThanhTienThucChay_HDCT ltttch ON T2.HopDongChiTietID = ltttch.HopDongChiTietID
                        WHERE   ( T2.ThanhTien - (ISNULL(ltttch.ThanhTienThucChay, 0)
                                  + @ThanhTienThucTreo) ) >= 0
						ORDER BY  T2.HopDongChiTietID

            END
		--6. HTQC, SANPHAM, CHIETKHAU, SITE BLANK, CUNG CHIPHI HOAC KHONG, KHONG MUA NGOAI, DONVITINH = GOI
        IF NOT EXISTS ( SELECT  *
                        FROM    @ListHopDongChiTietID lhdcti )
            BEGIN
                INSERT  INTO @ListHopDongChiTietID
                        SELECT TOP 1 T2.*
                        FROM    ( SELECT 
                                            *
                                  FROM      ( SELECT    hdct.HopDongChiTietID ,
                                                        @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                        hdct.HopDongFK ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.ThanhTien ,
                                                        SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,
                                                              0)
                                                            + ISNULL(tcdt.GiaTriThayDoi,
                                                              0)) ThanhTienThucChay
                                              FROM      dbo.ThucChayDaTinh tcdt
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
                                                        AND NOT ( hdct.DmLoaiREF = 13
                                                              OR hdct.DmLoaiBannerREF = 18
                                                              )--Mua ngoai
                                                        AND ( hdct.DmWebsiteREF = 265
                                                              OR hdct.DmWebsiteREF IS NULL
                                                            )
                                                       
                                              GROUP BY  hdct.HopDongFK ,
                                                        hdct.HopDongChiTietID ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.ThanhTien
                                            ) T
                                ) T2
                                LEFT JOIN @ListThanhTienThucChay_HDCT ltttch ON T2.HopDongChiTietID = ltttch.HopDongChiTietID
                        WHERE   ( T2.ThanhTien - (ISNULL(ltttch.ThanhTienThucChay, 0)
                                  + @ThanhTienThucTreo) ) >= 0
						ORDER BY  T2.HopDongChiTietID
            END

		--7. HTQC, SANPHAM, CHIETKHAU, SITE,  KHONG MUA NGOAI, DONVITINH = GOI
		IF NOT EXISTS ( SELECT  *
                        FROM    @ListHopDongChiTietID lhdcti )
            BEGIN
                INSERT  INTO @ListHopDongChiTietID
                        SELECT TOP 1 T2.*
                        FROM    ( SELECT 
                                            *
                                  FROM      ( SELECT    hdct.HopDongChiTietID ,
                                                        @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                        hdct.HopDongFK ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.ThanhTien ,
                                                        SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,
                                                              0)
                                                            + ISNULL(tcdt.GiaTriThayDoi,
                                                              0)) ThanhTienThucChay
                                              FROM      ThucChayDaTinh tcdt
                                                        RIGHT JOIN HopDongChiTiet hdct ON hdct.HopDongFK = tcdt.HopDongID
                                                              AND hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
                                              WHERE     hdct.HopDongFK = @HopDongREF
                                                        AND hdct.DmSanPhamREF IN (
                                                        141, 245, 250, 637,
                                                        305 ) --PR
                                                        AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
                                                        AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                        AND hdct.DeletedStatus = 0
                                                        AND hdct.ChietKhau = @ChietKhau
                                                        AND NOT ( hdct.DmLoaiREF = 13
                                                              OR hdct.DmLoaiBannerREF = 18
                                                              )--Mua ngoai
                                                        AND hdct.DmWebsiteREF = @DmWebsiteREF
                                                        AND hdct.DonViTinhREF = 10
                                              GROUP BY  hdct.HopDongFK ,
                                                        hdct.HopDongChiTietID ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.ThanhTien
                                            ) T
                                ) T2
                                LEFT JOIN @ListThanhTienThucChay_HDCT ltttch ON T2.HopDongChiTietID = ltttch.HopDongChiTietID
                        WHERE   ( T2.ThanhTien - (ISNULL(ltttch.ThanhTienThucChay, 0)
                                  + @ThanhTienThucTreo) ) >= 0
						ORDER BY  T2.HopDongChiTietID
            END


				
		IF NOT EXISTS ( SELECT  *
                        FROM    @ListHopDongChiTietID lhdcti )
            BEGIN
                INSERT  INTO @ListHopDongChiTietID
                        SELECT TOP 1 T2.*
                        FROM    ( SELECT 
                                            *
                                  FROM      ( SELECT    hdct.HopDongChiTietID ,
                                                        @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                        hdct.HopDongFK ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.ThanhTien ,
                                                        SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,
                                                              0)
                                                            + ISNULL(tcdt.GiaTriThayDoi,
                                                              0)) ThanhTienThucChay
                                              FROM      ThucChayDaTinh tcdt
                                                        RIGHT JOIN HopDongChiTiet hdct ON hdct.HopDongFK = tcdt.HopDongID
                                                              AND hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
                                              WHERE     hdct.HopDongFK = @HopDongREF
                                                        AND hdct.DmSanPhamREF IN (
                                                        141, 245, 250, 637,
                                                        305 ) --PR
                                                        AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
                                                        AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                        AND hdct.DeletedStatus = 0
                                                        AND hdct.ChietKhau = @ChietKhau
                                                        AND NOT ( hdct.DmLoaiREF = 13
                                                              OR hdct.DmLoaiBannerREF = 18
                                                              )--Mua ngoai
                                                        AND hdct.DonGia = @DonGia
                                                        AND ( ( ISNULL(@ThucChayHopDongChiTietPrREF,
                                                              0) <> 0
                                                              AND hdct.DmLoaiBannerREF = 17
                                                              )
                                                            )
                                              GROUP BY  hdct.HopDongFK ,
                                                        hdct.HopDongChiTietID ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.ThanhTien
                                            ) T
                                ) T2
                                LEFT JOIN @ListThanhTienThucChay_HDCT ltttch ON T2.HopDongChiTietID = ltttch.HopDongChiTietID
                        WHERE   ( ThanhTien - (ISNULL(ltttch.ThanhTienThucChay, 0)
                                  + @ThanhTienThucTreo) ) >= 0
						ORDER BY  T2.HopDongChiTietID
            END
                  

        INSERT  INTO @ListID
                SELECT DISTINCT
                        HopDongChiTietID ,
                        ThucChayHopDongChiTietPRID
                FROM    @ListHopDongChiTietID

        RETURN;
    END;


```
