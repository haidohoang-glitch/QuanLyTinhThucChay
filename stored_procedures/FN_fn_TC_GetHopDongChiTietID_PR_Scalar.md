# Function: `fn_TC_GetHopDongChiTietID_PR_Scalar`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2017-06-13 13:34:26.683000
- **Ngày sửa cuối**: 2017-06-14 16:44:07.167000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@ThucChayHopDongChiTietPRID` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@ChietKhau` | `int(4)` | No |
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
CREATE FUNCTION [dbo].[fn_TC_GetHopDongChiTietID_PR_Scalar]
    (
      @ThucChayHopDongChiTietPRID INT ,
      @HopDongREF INT ,
      @ChietKhau INT ,
      @ThucChayHopDongChiTietPrREF INT ,
      @HopDongChiTietREF INT ,
      @DmHinhThucQuangCaoREF INT ,
      @DmSanPhamREF INT ,
      @DmWebsiteREF INT ,
      @DonGia INT ,
      @SoLuong INT
    )
RETURNS INT 

    BEGIN
        DECLARE @ThanhTien FLOAT;
        DECLARE @ThanhTienThucChay FLOAT;

        DECLARE @ListHopDongChiTietID TABLE
            (
              HopDongChiTietID INT ,
              ThucChayHopDongChiTietPRID INT ,
              HopDongID INT ,
              DmSanPhamREF INT ,
              ThanhTien FLOAT 
            );

        DECLARE @ListThanhTienThucChay_HDCT TABLE
            (
              HopDongChiTietID INT ,
              ThanhTienThucChay FLOAT
            )


        DECLARE @ThanhTienThucTreo FLOAT

        SELECT  @ThanhTienThucTreo = ISNULL(tchdctp.GiaTien, 0)
                * ISNULL(tchdctp.SoLuong, 0) * ( CONVERT(FLOAT, ( 100
                                                              - tchdctp.ChietKhau ))
                                                 / 100 )
        FROM    dbo.ThucChayHopDongChiTietPR tchdctp
        WHERE   tchdctp.ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID


        INSERT  INTO @ListThanhTienThucChay_HDCT
                SELECT  tcdt.HopDongChiTietREF ,
                        ISNULL(SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay, 0)
                            + ISNULL(tcdt.GiaTriThayDoi, 0)), 0) ThanhTienThucChay
                FROM    dbo.ThucChayDaTinh tcdt (NOLOCK)
                WHERE   tcdt.HopDongID = @HopDongREF
                GROUP BY tcdt.HopDongChiTietREF
			
		

        SET @ThanhTienThucTreo = ISNULL(@ThanhTienThucTreo, 0)


        
        INSERT  INTO @ListHopDongChiTietID
                SELECT  T2.*
                FROM    ( SELECT TOP 1
                                    *
                          FROM      ( SELECT    hdct.HopDongChiTietID ,
                                                @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                hdct.HopDongFK ,
                                                hdct.DmSanPhamREF ,
                                                hdct.ThanhTien 
                                      FROM      HopDongChiTiet hdct 
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
                          ORDER BY  HopDongChiTietID
                        ) T2
                        LEFT JOIN @ListThanhTienThucChay_HDCT ltttch ON T2.HopDongChiTietID = ltttch.HopDongChiTietID
                WHERE   ( ThanhTien - (ISNULL(ltttch.ThanhTienThucChay, 0)
                          + @ThanhTienThucTreo) ) >= 0
                

        
        IF NOT EXISTS ( SELECT  *
                        FROM    @ListHopDongChiTietID lhdcti )
            BEGIN
                INSERT  INTO @ListHopDongChiTietID
                        SELECT  T2.*
                        FROM    ( SELECT TOP 1
                                            *
                                  FROM      ( SELECT    hdct.HopDongChiTietID ,
                                                        @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                        hdct.HopDongFK ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.ThanhTien 
                                              FROM      HopDongChiTiet hdct 
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
                                  ORDER BY  HopDongChiTietID
                                ) T2
                                LEFT JOIN @ListThanhTienThucChay_HDCT ltttch ON T2.HopDongChiTietID = ltttch.HopDongChiTietID
                        WHERE   ( ThanhTien - (ISNULL(ltttch.ThanhTienThucChay, 0)
                                  + @ThanhTienThucTreo) ) >= 0

            END

        IF NOT EXISTS ( SELECT  *
                        FROM    @ListHopDongChiTietID lhdcti )
            BEGIN
                INSERT  INTO @ListHopDongChiTietID
                        SELECT  T2.*
                        FROM    ( SELECT TOP 1
                                            *
                                  FROM      ( SELECT    hdct.HopDongChiTietID ,
                                                        @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                        hdct.HopDongFK ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.ThanhTien 
                                              FROM      HopDongChiTiet hdct
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
                                  ORDER BY  HopDongChiTietID
                                ) T2
                                LEFT JOIN @ListThanhTienThucChay_HDCT ltttch ON T2.HopDongChiTietID = ltttch.HopDongChiTietID
                        WHERE   ( ThanhTien - (ISNULL(ltttch.ThanhTienThucChay, 0)
                                  + @ThanhTienThucTreo) ) >= 0
            END

        IF NOT EXISTS ( SELECT  *
                        FROM    @ListHopDongChiTietID lhdcti )
            BEGIN
                INSERT  INTO @ListHopDongChiTietID
                        SELECT  T2.*
                        FROM    ( SELECT TOP 1
                                            *
                                  FROM      ( SELECT    hdct.HopDongChiTietID ,
                                                        @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                        hdct.HopDongFK ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.ThanhTien 
                                              FROM      HopDongChiTiet hdct 
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
                                  ORDER BY  HopDongChiTietID
                                ) T2
                                LEFT JOIN @ListThanhTienThucChay_HDCT ltttch ON T2.HopDongChiTietID = ltttch.HopDongChiTietID
                        WHERE   ( ThanhTien - (ISNULL(ltttch.ThanhTienThucChay, 0)
                                  + @ThanhTienThucTreo) ) >= 0
            END

        IF NOT EXISTS ( SELECT  *
                        FROM    @ListHopDongChiTietID lhdcti )
            BEGIN
                INSERT  INTO @ListHopDongChiTietID
                        SELECT  T2.*
                        FROM    ( SELECT TOP 1
                                            *
                                  FROM      ( SELECT    hdct.HopDongChiTietID ,
                                                        @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                        hdct.HopDongFK ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.ThanhTien 
                                              FROM      HopDongChiTiet hdct 
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
                                                        AND NOT ( ( ISNULL(@ThucChayHopDongChiTietPrREF,
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
                                  ORDER BY  HopDongChiTietID
                                ) T2
                                LEFT JOIN @ListThanhTienThucChay_HDCT ltttch ON T2.HopDongChiTietID = ltttch.HopDongChiTietID
                        WHERE   ( ThanhTien - (ISNULL(ltttch.ThanhTienThucChay, 0)
                                  + @ThanhTienThucTreo) ) >= 0
            END

        IF NOT EXISTS ( SELECT  *
                        FROM    @ListHopDongChiTietID lhdcti )
            BEGIN
                INSERT  INTO @ListHopDongChiTietID
                        SELECT  T2.*
                        FROM    ( SELECT TOP 1
                                            *
                                  FROM      ( SELECT    hdct.HopDongChiTietID ,
                                                        @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                        hdct.HopDongFK ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.ThanhTien 
                                              FROM      HopDongChiTiet hdct
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
                                                        AND DonViTinhREF = 10
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
                                  ORDER BY  HopDongChiTietID
                                ) T2
                                LEFT JOIN @ListThanhTienThucChay_HDCT ltttch ON T2.HopDongChiTietID = ltttch.HopDongChiTietID
                        WHERE   ( ThanhTien - (ISNULL(ltttch.ThanhTienThucChay, 0)
                                  + @ThanhTienThucTreo) ) >= 0
            END

                  
		DECLARE @id INT
        
                SET @id = (SELECT TOP 1
                        HopDongChiTietID 
                FROM    @ListHopDongChiTietID)

        RETURN @id;
    END;


```
