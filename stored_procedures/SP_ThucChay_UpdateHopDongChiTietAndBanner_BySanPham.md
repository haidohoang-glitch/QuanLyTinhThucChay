# Stored Procedure: `ThucChay_UpdateHopDongChiTietAndBanner_BySanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-07-09 15:43:56.513000
- **Ngày sửa cuối**: 2018-08-20 11:09:57.107000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_BySanPham] @DmSanPhamREF INT
AS
    BEGIN

--Update HopDongChiTietREF Tu Viec Thuc HIen Ket Noi Bang Tay Giua BannerID & Phan Bo Hop Dong
        DECLARE @BannerID NVARCHAR(50)
        DECLARE @TileThucChayHDCTVaBanner FLOAT ,
            @TongViewHD BIGINT ,
            @TongGoi INT = 0


        DECLARE Record_Cursor CURSOR
        FOR
            SELECT DISTINCT
                    tchdctab.DmBannerID
            FROM    dbo.ThucChayHopDongChiTietAndBanner tchdctab
                    INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tchdctab.HopDongChiTietREF
					INNER JOIN (SELECT hd.HopDongID FROM dbo.HopDong hd WHERE hd.DeletedStatus = 0 AND hd.TrangThaiHopDong NOT IN(0,3)) hd
					ON hd.HopDongID = hdct.HopDongFK
            WHERE   tchdctab.DaThucHienUpdateTiLe = 0
                    AND tchdctab.DeletedStatus = 0
                    AND hdct.DeletedStatus = 0
                    AND hdct.DmSanPhamREF = @DmSanPhamREF
                    AND ( ( [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF,
                                                              hdct.DonViTinh) <> 1 )
                          OR hdct.DmSanPhamREF = 680
                        ) --Đơn vị của hình thức not CPD and PR
        OPEN Record_Cursor

-- Perform the first fetch.
        FETCH NEXT FROM Record_Cursor INTO @BannerID
		
        WHILE @@FETCH_STATUS = 0
            BEGIN
		--1. Tinh tong view
                SET @TongViewHD = ( SELECT  SUM(CONVERT(BIGINT, ISNULL(T.SoLuong,
                                                              0)) * 1000)
                                    FROM    ( SELECT  DISTINCT
                                                        hdct.* --sum(convert(bigint,ISNULL(hdct.SoLuong,0))*1000)
                                              FROM      dbo.ThucChayHopDongChiTietAndBanner tchdctab
                                                        INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tchdctab.HopDongChiTietREF
														INNER JOIN (SELECT hd.HopDongID FROM dbo.HopDong hd WHERE hd.DeletedStatus = 0 AND hd.TrangThaiHopDong NOT IN(0,3)) hd
														ON hd.HopDongID = hdct.HopDongFK
                                              WHERE     tchdctab.DmBannerID = CONVERT(NVARCHAR(100), @BannerID)
                                                        AND tchdctab.DeletedStatus = 0
                                                        AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                        AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF,
                                                              hdct.DonViTinh) <> 1
                                            ) T
                                  )
                SET @TongViewHD = ISNULL(@TongViewHD, 0)
                PRINT @TongViewHD;
                IF ( @TongViewHD != 0 )
                    BEGIN
                        UPDATE  dbo.ThucChayHopDongChiTietAndBanner
                        SET     ThucChayHopDongChiTietAndBanner.TiLeThucChayHDCTSoVoiBanner = ( ( CONVERT(FLOAT, SoLuong)
                                                              * 1000 )
                                                              / CONVERT(FLOAT, @TongViewHD)
                                                              * 100 ) ,
                                DaThucHienUpdateTiLe = 1
                        FROM    dbo.ThucChayHopDongChiTietAndBanner
                                INNER JOIN dbo.HopDongChiTiet ON HopDongChiTiet.HopDongChiTietID = ThucChayHopDongChiTietAndBanner.HopDongChiTietREF
								INNER JOIN (SELECT hd.HopDongID FROM dbo.HopDong hd WHERE hd.DeletedStatus = 0 AND hd.TrangThaiHopDong NOT IN(0,3)) hd
								ON hd.HopDongID = HopDongChiTiet.HopDongFK
                        WHERE   ThucChayHopDongChiTietAndBanner.DmBannerID = CONVERT(NVARCHAR(100), @BannerID)
                                AND ThucChayHopDongChiTietAndBanner.DeletedStatus = 0
                                AND HopDongChiTiet.DmSanPhamREF = @DmSanPhamREF
                                AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](HopDongChiTiet.DonViTinhREF,
                                                              HopDongChiTiet.DonViTinh) <> 1
                    END
                ELSE
                    BEGIN
                        UPDATE  dbo.ThucChayHopDongChiTietAndBanner
                        SET     ThucChayHopDongChiTietAndBanner.TiLeThucChayHDCTSoVoiBanner = 100 ,
                                DaThucHienUpdateTiLe = 1
                        FROM    dbo.ThucChayHopDongChiTietAndBanner
                                INNER JOIN dbo.HopDongChiTiet ON HopDongChiTiet.HopDongChiTietID = ThucChayHopDongChiTietAndBanner.HopDongChiTietREF
								INNER JOIN (SELECT hd.HopDongID FROM dbo.HopDong hd WHERE hd.DeletedStatus = 0 AND hd.TrangThaiHopDong NOT IN(0,3)) hd
								ON hd.HopDongID = HopDongChiTiet.HopDongFK
                        WHERE   ThucChayHopDongChiTietAndBanner.DmBannerID = @BannerID
                                AND ThucChayHopDongChiTietAndBanner.DeletedStatus = 0
                                AND HopDongChiTiet.DmSanPhamREF = @DmSanPhamREF
                                AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](HopDongChiTiet.DonViTinhREF,
                                                              HopDongChiTiet.DonViTinh) <> 1
                    END

				--Ap dung cho cac san pham CPR chay voi don vi tinh la goi
                SET @TongGoi = ( SELECT SUM(CONVERT(BIGINT, ISNULL(T.SoLuong,
                                                              0)) * 1000)
                                 FROM   ( SELECT  DISTINCT
                                                    hdct.* --sum(convert(bigint,ISNULL(hdct.SoLuong,0))*1000)
                                          FROM      dbo.ThucChayHopDongChiTietAndBanner tchdctab
                                                    INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tchdctab.HopDongChiTietREF
													INNER JOIN (SELECT hd.HopDongID FROM dbo.HopDong hd WHERE hd.DeletedStatus = 0 AND hd.TrangThaiHopDong NOT IN(0,3)) hd
													ON hd.HopDongID = hdct.HopDongFK
                                          WHERE     tchdctab.DmBannerID = CONVERT(NVARCHAR(100), @BannerID)
                                                    AND tchdctab.DeletedStatus = 0
                                                    AND hdct.DmSanPhamREF IN (
                                                    680 )
                                        ) T
                               )
                IF ( @TongGoi != 0 )
                    BEGIN
                        UPDATE  dbo.ThucChayHopDongChiTietAndBanner
                        SET     ThucChayHopDongChiTietAndBanner.TiLeThucChayHDCTSoVoiBanner = ( ROUND(( CONVERT(FLOAT, SoLuong)
                                                              * 1000 )
                                                              / CONVERT(FLOAT, @TongGoi),
                                                              5) * 100 ) ,
                                DaThucHienUpdateTiLe = 1
                        FROM    dbo.ThucChayHopDongChiTietAndBanner
                                INNER JOIN dbo.HopDongChiTiet ON HopDongChiTiet.HopDongChiTietID = ThucChayHopDongChiTietAndBanner.HopDongChiTietREF
								INNER JOIN (SELECT hd.HopDongID FROM dbo.HopDong hd WHERE hd.DeletedStatus = 0 AND hd.TrangThaiHopDong NOT IN(0,3)) hd
								ON hd.HopDongID = HopDongChiTiet.HopDongFK
                        WHERE   ThucChayHopDongChiTietAndBanner.DmBannerID = CONVERT(NVARCHAR(100), @BannerID)
                                AND ThucChayHopDongChiTietAndBanner.DeletedStatus = 0
                                AND HopDongChiTiet.DmSanPhamREF IN ( 680 )
                    END
                ELSE
                    BEGIN
                        UPDATE  dbo.ThucChayHopDongChiTietAndBanner
                        SET     ThucChayHopDongChiTietAndBanner.TiLeThucChayHDCTSoVoiBanner = 100 ,
                                DaThucHienUpdateTiLe = 1
                        FROM    dbo.ThucChayHopDongChiTietAndBanner
                                INNER JOIN HopDongChiTiet ON HopDongChiTiet.HopDongChiTietID = ThucChayHopDongChiTietAndBanner.HopDongChiTietREF
								INNER JOIN (SELECT hd.HopDongID FROM dbo.HopDong hd WHERE hd.DeletedStatus = 0 AND hd.TrangThaiHopDong NOT IN(0,3)) hd
								ON hd.HopDongID = HopDongChiTiet.HopDongFK
                        WHERE   ThucChayHopDongChiTietAndBanner.DmBannerID = @BannerID
                                AND ThucChayHopDongChiTietAndBanner.DeletedStatus = 0
                                AND HopDongChiTiet.DmSanPhamREF IN ( 680 )
                    END

                PRINT @TongViewHD
                FETCH NEXT FROM Record_Cursor INTO @BannerID
            END

        CLOSE Record_Cursor
        DEALLOCATE Record_Cursor

        SELECT  '1'

    END

--EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner]

```
