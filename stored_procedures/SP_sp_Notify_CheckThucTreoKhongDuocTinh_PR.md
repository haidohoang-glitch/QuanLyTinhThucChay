# Stored Procedure: `sp_Notify_CheckThucTreoKhongDuocTinh_PR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-10-18 09:44:25.660000
- **Ngày sửa cuối**: 2019-05-14 15:22:55.310000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[sp_Notify_CheckThucTreoKhongDuocTinh_PR]
AS
    BEGIN
        
        DECLARE @NgayThucHien DATETIME
        SET @NgayThucHien = GETDATE()
        SET @NgayThucHien = DATEADD(dd, -1, @NgayThucHien)	
        SET @NgayThucHien = CONVERT(DATE, @NgayThucHien)

        DECLARE @ThucChayHopDongChiTietPRID INT ,
            @HopDongREF INT ,
            @ChietKhau FLOAT ,
            @ThucChayHopDongChiTietPrREF INT ,
            @HopDongChiTietREF INT ,
            @DmHinhThucQuangCaoREF INT ,
            @DmSanPhamREF INT ,
            @DmWebsiteREF INT ,
            @DonGia INT ,
            @SoLuong INT



        DECLARE @DanhSachKoDuocTinh TABLE
            (
              ThucChayHopDongChiTietPRID INT ,
              GhiChu NVARCHAR(500)
            );


        DECLARE @List TABLE
            (
              ID INT IDENTITY(1,1) ,
			  ThucChayHopDongChiTietPRID INT ,
              GhiChu NVARCHAR(500)
            );




        DECLARE icursor CURSOR
        FOR
            SELECT  ThucChayHopDongChiTietPRID ,
                    HopDongREF ,
                    ChietKhau ,
                    ThucChayHopDongChiTietPrREF ,
                    HopDongChiTietREF ,
                    DmHinhThucQuangCaoREF ,
                    DmSanPhamREF ,
                    DmWebsiteREF ,
                    GiaTien ,
                    SoLuong
            FROM     dbo.ThucChayHopDongChiTietPR
            WHERE   DeletedStatus <> 1
                    AND RecordStatus = 0
                    AND DmHinhThucQuangCaoREF <> 0
                    AND DmSanPhamREF <> 0
                    AND ThoiGianBatDau >= '2014-01-01'
                    AND ( CASE WHEN CreatedAt >= LastModifiedAt
                               THEN CONVERT(DATE, CreatedAt)
                               ELSE CONVERT(DATE, LastModifiedAt)
                          END ) = @NgayThucHien
					--AND ThucChayHopDongChiTietPRID = 76384
            UNION
            SELECT  ThucChayHopDongChiTietPRID ,
                    HopDongREF ,
                    ChietKhau ,
                    ThucChayHopDongChiTietPrREF ,
                    HopDongChiTietREF ,
                    DmHinhThucQuangCaoREF ,
                    DmSanPhamREF ,
                    DmWebsiteREF ,
                    GiaTien ,
                    SoLuong
            FROM     dbo.ThucChayHopDongChiTietPR PR
                    INNER JOIN  dbo.HopDong hd ON PR.HopDongREF = hd.HopDongID
            WHERE   PR.DeletedStatus <> 1
                    AND PR.RecordStatus = 0
                    AND PR.DmHinhThucQuangCaoREF <> 0
                    AND PR.DmSanPhamREF <> 0
                    AND PR.ThoiGianBatDau >= '2014-01-01'
                    AND CONVERT(DATE, hd.LastModifiedAt) = @NgayThucHien
					AND PR.CreatedAt < @NgayThucHien

        OPEN icursor;  

        FETCH NEXT FROM icursor   
				INTO @ThucChayHopDongChiTietPRID, @HopDongREF, @ChietKhau,
            @ThucChayHopDongChiTietPrREF, @HopDongChiTietREF,
            @DmHinhThucQuangCaoREF, @DmSanPhamREF, @DmWebsiteREF, @DonGia,
            @SoLuong

        WHILE @@FETCH_STATUS = 0
            BEGIN  
                BEGIN



                    DECLARE @ThanhTien FLOAT;
                    DECLARE @ThanhTienThucChay FLOAT;
                    DECLARE @HDCTID INT = NULL

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


			
        
                    IF NOT EXISTS ( SELECT TOP 1
                                            *
                                    FROM    ( SELECT    hdct.HopDongChiTietID ,
                                                        @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                        hdct.HopDongFK ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.ThanhTien
                                              FROM       dbo.HopDongChiTiet hdct
                                              WHERE     hdct.HopDongFK = @HopDongREF
                                                        AND hdct.DmSanPhamREF IN (141, 245, 250, 637,305 ) --PR
                                                        AND NOT ( hdct.DmLoaiREF = 13
                                                              OR hdct.DmLoaiBannerREF = 18
                                                              )--Mua ngoai
                                                        AND hdct.DeletedStatus = 0
                                              GROUP BY  hdct.HopDongFK ,
                                                        hdct.HopDongChiTietID ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.ThanhTien
                                            ) T
                                    ORDER BY HopDongChiTietID )
                        BEGIN
                            INSERT  INTO @List
                            VALUES  ( @ThucChayHopDongChiTietPRID,
                                      N'Ko tồn tại hợp đồng chi tiết nào của hợp đồng này' )
                        END



                    IF NOT EXISTS ( SELECT  *
                                    FROM    @List
                                    WHERE   ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID )
                        BEGIN
                            IF NOT EXISTS ( SELECT TOP 1
                                                    *
                                            FROM    ( SELECT  hdct.HopDongChiTietID ,
                                                              @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                              hdct.HopDongFK ,
                                                              hdct.DmSanPhamREF ,
                                                              hdct.ThanhTien
                                                      FROM     dbo.HopDongChiTiet hdct
                                                      WHERE   hdct.HopDongFK = @HopDongREF
                                                              AND hdct.DmSanPhamREF IN (141, 245, 250,637, 305 ) --PR
                                                              AND NOT ( hdct.DmLoaiREF = 13
																		OR hdct.DmLoaiBannerREF = 18
																	  )--Mua ngoai
                                                              AND hdct.DeletedStatus = 0
                                                              AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
                                                              AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                              AND hdct.ChietKhau = @ChietKhau

                                                      GROUP BY hdct.HopDongFK ,
                                                              hdct.HopDongChiTietID ,
                                                              hdct.DmSanPhamREF ,
                                                              hdct.ThanhTien
                                                    ) T
                                            ORDER BY HopDongChiTietID )
                                BEGIN
                                    INSERT  INTO @List
                                    VALUES  ( @ThucChayHopDongChiTietPRID,
                                              N'Ko tồn tại hợp đồng chi tiết trùng HTQC + SP + CK' )
                                END
                        END


                    IF NOT EXISTS ( SELECT  *
                                    FROM    @List
                                    WHERE   ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID )
                        BEGIN
                            IF NOT EXISTS ( SELECT TOP 1
                                                    *
                                            FROM    ( SELECT  hdct.HopDongChiTietID ,
                                                              @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                              hdct.HopDongFK ,
                                                              hdct.DmSanPhamREF ,
                                                              hdct.ThanhTien
                                                      FROM     dbo.HopDongChiTiet hdct
                                                      WHERE   hdct.HopDongFK = @HopDongREF
                                                              AND hdct.DmSanPhamREF IN (141, 245, 250,637, 305 ) --PR
                                                              AND NOT ( hdct.DmLoaiREF = 13
																		OR hdct.DmLoaiBannerREF = 18
																	  )--Mua ngoai
                                                              AND hdct.DeletedStatus = 0
                                                              AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
                                                              AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                              AND hdct.ChietKhau = @ChietKhau
                                                              AND hdct.DmWebsiteREF = @DmWebsiteREF
                                                              AND hdct.DonGia = @DonGia
                                                      GROUP BY hdct.HopDongFK ,
                                                              hdct.HopDongChiTietID ,
                                                              hdct.DmSanPhamREF ,
                                                              hdct.ThanhTien
                                                    ) T
                                            ORDER BY HopDongChiTietID )
                                BEGIN
                                    INSERT  INTO @List
                                    VALUES  ( @ThucChayHopDongChiTietPRID,
                                              N'Ko tồn tại hợp đồng chi tiết trùng Website + ĐG' )
                                END
                            ELSE
                                BEGIN
                                    SET @HDCTID = ( SELECT TOP 1
                                                            HopDongChiTietID
                                                    FROM    ( SELECT
																  hdct.HopDongChiTietID ,
																  @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
																  hdct.HopDongFK ,
																  hdct.DmSanPhamREF ,
																  hdct.ThanhTien
                                                              FROM  dbo.HopDongChiTiet hdct
                                                              WHERE hdct.HopDongFK = @HopDongREF
																	AND hdct.DmSanPhamREF IN (141, 245, 250, 637, 305 ) --PR
																	AND NOT ( hdct.DmLoaiREF = 13
																			 OR hdct.DmLoaiBannerREF = 18
																			)--Mua ngoai
																	AND hdct.DeletedStatus = 0
																	AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
																	AND hdct.DmSanPhamREF = @DmSanPhamREF
																	AND hdct.ChietKhau = @ChietKhau
																	AND hdct.DmWebsiteREF = @DmWebsiteREF
																	AND hdct.DonGia = @DonGia
                                                              GROUP BY hdct.HopDongFK ,
																	  hdct.HopDongChiTietID ,
																	  hdct.DmSanPhamREF ,
																	  hdct.ThanhTien
                                                            ) T
                                                    ORDER BY HopDongChiTietID
                                                  )
                                END
                        END





                    IF EXISTS ( SELECT  *
                                FROM    @List
                                WHERE   ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID
                                        AND GhiChu = N'Ko tồn tại hợp đồng chi tiết trùng Website + ĐG' )
                        BEGIN
                            IF NOT EXISTS ( SELECT TOP 1
                                                    *
                                            FROM    ( SELECT  hdct.HopDongChiTietID ,
                                                              @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                              hdct.HopDongFK ,
                                                              hdct.DmSanPhamREF ,
                                                              hdct.ThanhTien
                                                      FROM     dbo.HopDongChiTiet hdct
                                                      WHERE   hdct.HopDongFK = @HopDongREF
                                                              AND hdct.DmSanPhamREF IN (141, 245, 250,637, 305 ) --PR
                                                              AND NOT ( hdct.DmLoaiREF = 13
																		OR hdct.DmLoaiBannerREF = 18
																	  )--Mua ngoai
                                                              AND hdct.DeletedStatus = 0
                                                              AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
                                                              AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                              AND hdct.ChietKhau = @ChietKhau
                                                              AND hdct.DmWebsiteREF = @DmWebsiteREF
                                                              AND hdct.DonGia <> @DonGia
                                                              AND ( ( ISNULL(@ThucChayHopDongChiTietPrREF, 0) <> 0
																		AND hdct.DmLoaiBannerREF = 17)
																	OR ( ISNULL(@ThucChayHopDongChiTietPrREF,0) = 0
																			AND hdct.DmLoaiBannerREF <> 17
																		)
																	)
                                                      GROUP BY hdct.HopDongFK ,
                                                              hdct.HopDongChiTietID ,
                                                              hdct.DmSanPhamREF ,
                                                              hdct.ThanhTien
                                                    ) T
                                            ORDER BY HopDongChiTietID )
                                BEGIN
                                    INSERT  INTO @List
                                    VALUES  ( @ThucChayHopDongChiTietPRID,
                                              N'Ko tồn tại hợp đồng chi tiết trùng Website + CPhi nhưng khác ĐG' )
                                END
                            ELSE
                                BEGIN
                                    DELETE  FROM @List
                                    WHERE   ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID

                                    IF @HDCTID IS NULL
                                        BEGIN
                                            SET @HDCTID = ( SELECT TOP 1
                                                              HopDongChiTietID
                                                            FROM
                                                              ( SELECT
																	  hdct.HopDongChiTietID ,
																	  @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
																	  hdct.HopDongFK ,
																	  hdct.DmSanPhamREF ,
																	  hdct.ThanhTien
                                                              FROM  dbo.HopDongChiTiet hdct
                                                              WHERE hdct.HopDongFK = @HopDongREF
																	AND hdct.DmSanPhamREF IN (141, 245, 250,637, 305 ) --PR
																	AND NOT ( hdct.DmLoaiREF = 13
																				OR hdct.DmLoaiBannerREF = 18
																			  )--Mua ngoai
                                                              AND hdct.DeletedStatus = 0
                                                              AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
                                                              AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                              AND hdct.ChietKhau = @ChietKhau
                                                              AND hdct.DmWebsiteREF = @DmWebsiteREF
                                                              AND hdct.DonGia <> @DonGia
                                                              AND ( ( ISNULL(@ThucChayHopDongChiTietPrREF,0) <> 0
																	  AND hdct.DmLoaiBannerREF = 17
																	  )
																	OR ( ISNULL(@ThucChayHopDongChiTietPrREF,0) = 0
																			AND hdct.DmLoaiBannerREF <> 17
																		)
                                                              )
                                                              GROUP BY hdct.HopDongFK ,
																	  hdct.HopDongChiTietID ,
																	  hdct.DmSanPhamREF ,
																	  hdct.ThanhTien
                                                              ) T
                                                            ORDER BY HopDongChiTietID
                                                          )
                                        END
                            
                                END
                        END




                    IF EXISTS ( SELECT  *
                                FROM    @List
                                WHERE   ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID
                                        AND GhiChu = N'Ko tồn tại hợp đồng chi tiết trùng Website + ĐG' )
                        OR EXISTS ( SELECT  *
                                    FROM    @List
                                    WHERE   ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID
                                            AND GhiChu = N'Ko tồn tại hợp đồng chi tiết trùng Website + CPhi nhưng khác ĐG' )
                        BEGIN
                            IF NOT EXISTS ( SELECT TOP 1
                                                    *
                                            FROM    ( SELECT  hdct.HopDongChiTietID ,
                                                              @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                              hdct.HopDongFK ,
                                                              hdct.DmSanPhamREF ,
                                                              hdct.ThanhTien
                                                      FROM     dbo.HopDongChiTiet hdct
                                                      WHERE   hdct.HopDongFK = @HopDongREF
                                                              AND hdct.DmSanPhamREF IN (141, 245, 250,637, 305 ) --PR
                                                              AND NOT ( hdct.DmLoaiREF = 13
																		OR hdct.DmLoaiBannerREF = 18
																	  )--Mua ngoai
                                                              AND hdct.DeletedStatus = 0
                                                              AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
                                                              AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                              AND hdct.ChietKhau = @ChietKhau
                                                              AND ( hdct.DmWebsiteREF = 265
																		OR hdct.DmWebsiteREF IS NULL
																	)
                                                      GROUP BY hdct.HopDongFK ,
                                                              hdct.HopDongChiTietID ,
                                                              hdct.DmSanPhamREF ,
                                                              hdct.ThanhTien
                                                    ) T
                                            ORDER BY HopDongChiTietID )
                                BEGIN
                                    INSERT  INTO @List
                                    VALUES  ( @ThucChayHopDongChiTietPRID,
                                              N'Ko tồn tại hợp đồng chi tiết có Website blank' )
                                END
                            ELSE
                                BEGIN
                                    DELETE  FROM @List
                                    WHERE   ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID

                                    IF @HDCTID IS NULL
                                        BEGIN
                                            SET @HDCTID = ( SELECT TOP 1
                                                              HopDongChiTietID
                                                            FROM
                                                              ( SELECT
																	  hdct.HopDongChiTietID ,
																	  @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
																	  hdct.HopDongFK ,
																	  hdct.DmSanPhamREF ,
																	  hdct.ThanhTien
                                                              FROM  dbo.HopDongChiTiet hdct
                                                              WHERE hdct.HopDongFK = @HopDongREF
																	AND hdct.DmSanPhamREF IN (141, 245, 250,637, 305 ) --PR
																	AND NOT ( hdct.DmLoaiREF = 13
																				OR hdct.DmLoaiBannerREF = 18
																			)--Mua ngoai
																	AND hdct.DeletedStatus = 0
																	AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
																	AND hdct.DmSanPhamREF = @DmSanPhamREF
																	AND hdct.ChietKhau = @ChietKhau
																	AND ( hdct.DmWebsiteREF = 265
																			OR hdct.DmWebsiteREF IS NULL
																			)
                                                              GROUP BY hdct.HopDongFK ,
																  hdct.HopDongChiTietID ,
																  hdct.DmSanPhamREF ,
																  hdct.ThanhTien
                                                              ) T
                                                            ORDER BY HopDongChiTietID
                                                          )
                                        END
                            
                                END
                        END



					IF EXISTS ( SELECT  *
                                FROM    @List
                                WHERE   ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID
                                        AND GhiChu = N'Ko tồn tại hợp đồng chi tiết trùng Website + ĐG' )
                        OR EXISTS ( SELECT  *
                                    FROM    @List
                                    WHERE   ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID
                                            AND GhiChu = N'Ko tồn tại hợp đồng chi tiết trùng Website + CPhi nhưng khác ĐG' )
						OR EXISTS ( SELECT  *
                                    FROM    @List
                                    WHERE   ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID
                                            AND GhiChu = N'Ko tồn tại hợp đồng chi tiết có Website blank' )
                        BEGIN
                            IF NOT EXISTS ( SELECT TOP 1
                                                    *
                                            FROM    ( SELECT  hdct.HopDongChiTietID ,
                                                              @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                              hdct.HopDongFK ,
                                                              hdct.DmSanPhamREF ,
                                                              hdct.ThanhTien
                                                      FROM     dbo.HopDongChiTiet hdct
                                                      WHERE   hdct.HopDongFK = @HopDongREF
                                                              AND hdct.DmSanPhamREF IN (141, 245, 250,637, 305 ) --PR
                                                              AND NOT ( hdct.DmLoaiREF = 13
																		OR hdct.DmLoaiBannerREF = 18
																	  )--Mua ngoai
                                                              AND hdct.DeletedStatus = 0
                                                              AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
                                                              AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                              AND hdct.ChietKhau = @ChietKhau
                                                              AND hdct.DmWebsiteREF = @DmWebsiteREF
															  AND DonViTinhREF = 10
                                                      GROUP BY hdct.HopDongFK ,
                                                              hdct.HopDongChiTietID ,
                                                              hdct.DmSanPhamREF ,
                                                              hdct.ThanhTien
                                                    ) T
                                            ORDER BY HopDongChiTietID )
                                BEGIN
                                    INSERT  INTO @List
                                    VALUES  ( @ThucChayHopDongChiTietPRID,
                                              N'Ko tồn tại hợp đồng chi tiết ký gói trùng website' )
                                END
                            ELSE
                                BEGIN
                                    DELETE  FROM @List
                                    WHERE   ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID

                                    IF @HDCTID IS NULL
                                        BEGIN
                                            SET @HDCTID = ( SELECT TOP 1
                                                              HopDongChiTietID
                                                            FROM
                                                              ( SELECT
																	  hdct.HopDongChiTietID ,
																	  @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
																	  hdct.HopDongFK ,
																	  hdct.DmSanPhamREF ,
																	  hdct.ThanhTien
                                                              FROM  dbo.HopDongChiTiet hdct
                                                              WHERE hdct.HopDongFK = @HopDongREF
																	AND hdct.DmSanPhamREF IN (141, 245, 250,637, 305 ) --PR
																	AND NOT ( hdct.DmLoaiREF = 13
																				OR hdct.DmLoaiBannerREF = 18
																			)--Mua ngoai
																	AND hdct.DeletedStatus = 0
																	AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
																	AND hdct.DmSanPhamREF = @DmSanPhamREF
																	AND hdct.ChietKhau = @ChietKhau
																	AND hdct.DmWebsiteREF = @DmWebsiteREF
																	AND DonViTinhREF = 10
                                                              GROUP BY hdct.HopDongFK ,
																  hdct.HopDongChiTietID ,
																  hdct.DmSanPhamREF ,
																  hdct.ThanhTien
                                                              ) T
                                                            ORDER BY HopDongChiTietID
                                                          )
                                        END
                            
                                END
                        END




						IF EXISTS ( SELECT  *
                                FROM    @List
                                WHERE   ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID
                                        AND GhiChu = N'Ko tồn tại hợp đồng chi tiết trùng Website + ĐG' )
                        OR EXISTS ( SELECT  *
                                    FROM    @List
                                    WHERE   ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID
                                            AND GhiChu = N'Ko tồn tại hợp đồng chi tiết trùng Website + CPhi nhưng khác ĐG' )
						OR EXISTS ( SELECT  *
                                    FROM    @List
                                    WHERE   ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID
                                            AND GhiChu = N'Ko tồn tại hợp đồng chi tiết có Website blank' )
						OR EXISTS ( SELECT  *
                                    FROM    @List
                                    WHERE   ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID
                                            AND GhiChu = N'Ko tồn tại hợp đồng chi tiết ký gói trùng website' )
                        BEGIN
                            IF NOT EXISTS ( SELECT TOP 1
                                                    *
                                            FROM    ( SELECT  hdct.HopDongChiTietID ,
                                                              @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
                                                              hdct.HopDongFK ,
                                                              hdct.DmSanPhamREF ,
                                                              hdct.ThanhTien
                                                      FROM     dbo.HopDongChiTiet hdct
                                                      WHERE   hdct.HopDongFK = @HopDongREF
                                                              AND hdct.DmSanPhamREF IN (141, 245, 250,637, 305 ) --PR
                                                              AND NOT ( hdct.DmLoaiREF = 13
																		OR hdct.DmLoaiBannerREF = 18
																	  )--Mua ngoai
                                                              AND hdct.DeletedStatus = 0
                                                              AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
                                                              AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                              AND hdct.ChietKhau = @ChietKhau
                                                              AND hdct.DonGia = @DonGia
                                                              AND ( ( ISNULL(@ThucChayHopDongChiTietPrREF, 0) <> 0
																		AND hdct.DmLoaiBannerREF = 17)
																	)
                                                      GROUP BY hdct.HopDongFK ,
                                                              hdct.HopDongChiTietID ,
                                                              hdct.DmSanPhamREF ,
                                                              hdct.ThanhTien
                                                    ) T
                                            ORDER BY HopDongChiTietID )
                                BEGIN
                                    INSERT  INTO @List
                                    VALUES  ( @ThucChayHopDongChiTietPRID,
                                              N'Ko tồn tại hợp đồng chi tiết là chi phí và cùng đơn giá + CK' )
                                END
                            ELSE
                                BEGIN
                                    DELETE  FROM @List
                                    WHERE   ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID

                                    IF @HDCTID IS NULL
                                        BEGIN
                                            SET @HDCTID = ( SELECT TOP 1
                                                              HopDongChiTietID
                                                            FROM
                                                              ( SELECT
																	  hdct.HopDongChiTietID ,
																	  @ThucChayHopDongChiTietPRID ThucChayHopDongChiTietPRID ,
																	  hdct.HopDongFK ,
																	  hdct.DmSanPhamREF ,
																	  hdct.ThanhTien
                                                              FROM  dbo.HopDongChiTiet hdct
                                                              WHERE hdct.HopDongFK = @HopDongREF
																	AND hdct.DmSanPhamREF IN (141, 245, 250,637, 305 ) --PR
																	AND NOT ( hdct.DmLoaiREF = 13
																				OR hdct.DmLoaiBannerREF = 18
																			)--Mua ngoai
																	AND hdct.DeletedStatus = 0
																	AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
																	AND hdct.DmSanPhamREF = @DmSanPhamREF
																	AND hdct.ChietKhau = @ChietKhau
																	AND hdct.DonGia = @DonGia
																	AND ( ( ISNULL(@ThucChayHopDongChiTietPrREF, 0) <> 0
																			AND hdct.DmLoaiBannerREF = 17)
																		)
                                                              GROUP BY hdct.HopDongFK ,
																  hdct.HopDongChiTietID ,
																  hdct.DmSanPhamREF ,
																  hdct.ThanhTien
                                                              ) T
                                                            ORDER BY HopDongChiTietID
                                                          )
                                        END
                            
                                END
                        END




                    IF NOT EXISTS ( SELECT  *
                                    FROM    @List
                                    WHERE   ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID )
                        AND @HDCTID IS NOT NULL
                        BEGIN
					
                            DECLARE @ThanhTienThucTreo FLOAT

                            SELECT  @ThanhTienThucTreo = ROUND(ISNULL(tchdctp.GiaTien,
                                                              0)
                                    * ISNULL(tchdctp.SoLuong, 0)
                                    * ( CONVERT(FLOAT, ( 100
                                                         - tchdctp.ChietKhau ))
                                        / 100 ), 0)
                            FROM     dbo.ThucChayHopDongChiTietPR tchdctp
                            WHERE   tchdctp.ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID


							
                            SELECT  @ThanhTienThucChay = ISNULL(SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0)
                                                              + ISNULL(tcdt.GiaTriThayDoi,0)), 0)
                            FROM     dbo.ThucChayDaTinh tcdt
                            WHERE   tcdt.HopDongChiTietREF = @HDCTID
			


                            SET @ThanhTienThucTreo = ISNULL(@ThanhTienThucTreo,
                                                            0)
                            SET @ThanhTienThucChay = ISNULL(@ThanhTienThucChay,
                                                            0)


                            DECLARE @ThanhTienHDCT FLOAT

                            SELECT  @ThanhTienHDCT = hdct.ThanhTien
                            FROM     dbo.HopDongChiTiet hdct
                            WHERE   hdct.HopDongChiTietID = @HDCTID



                            IF @ThanhTienHDCT < @ThanhTienThucChay
                                + @ThanhTienThucTreo
                                BEGIN
									IF NOT EXISTS (SELECT * 
													FROM  dbo.ThucChayDaTinh
													WHERE CONVERT(DATE, NgayThucHien) < '2017-07-01'
															AND DmSanPhamREF IN ( 141, 245, 250, 637, 305 )
															AND NOT ( DmHinhThucQuangCao = 13
																	  OR DmLoaiBannerREF = 18
																	)
															AND HopDongChiTietREF = @HDCTID
													)
									BEGIN
									    INSERT  INTO @List
										VALUES  ( @ThucChayHopDongChiTietPRID,
												  N'HĐCT: '
												  + CONVERT(NVARCHAR(50), @HDCTID)
												  + N' - Tiền thực chạy đã vượt HĐCT' )
									END
                                END


                    
                        END








                END;
						
                MoveNext:
                FETCH NEXT FROM icursor   
						INTO @ThucChayHopDongChiTietPRID, @HopDongREF,
                    @ChietKhau, @ThucChayHopDongChiTietPrREF,
                    @HopDongChiTietREF, @DmHinhThucQuangCaoREF, @DmSanPhamREF,
                    @DmWebsiteREF, @DonGia, @SoLuong
            END;   
        CLOSE icursor;  
        DEALLOCATE icursor; 
		

		INSERT INTO  dbo.ThucTreoKhongDuocTinh_PR
        SELECT DISTINCT
				tchdctp.HopDongREF HopDongID,
				HD.SoHopDong,
                tchdctp.DmHinhThucQuangCaoREF HTQC,
                tchdctp.DmSanPhamREF SanPham,
                tchdctp.ChietKhau ,
				tchdctp.GiaTien DonGia,
                --tchdctp.DmWebsiteREF ,
                tchdctp.TenWebsite ,
				tchdctp.NhanHang,
				l.GhiChu NguyenNhanKhongDuocTinh,
				(CASE WHEN ISNULL(tchdctp.ThucChayHopDongChiTietPrREF,0) = 0 THEN tchdctp.Link 
				ELSE ISNULL((SELECT TOP (1) tc.Link FROM  dbo.ThucChayHopDongChiTietPR tc
													WHERE tc.ThucChayHopDongChiTietPRID = tchdctp.ThucChayHopDongChiTietPrREF
				      ORDER BY l.ThucChayHopDongChiTietPRID),'')
				END)LinkThucTreo
				, tchdctp.ThucChayHopDongChiTietPrREF
				, GETDATE()
                --tchdctp.DmDonViTinhREF ,
                ,(CASE WHEN ISNULL(tchdctp.ThucChayHopDongChiTietPrREF,0) <> 0 THEN 'ChiPhi' 
				ELSE 'KhongChiPhi'
				END)LoaiThucTreo
                --tchdctp.*
        FROM    @List l
                INNER JOIN  dbo.ThucChayHopDongChiTietPR tchdctp ON l.ThucChayHopDongChiTietPRID = tchdctp.ThucChayHopDongChiTietPRID
				INNER JOIN  dbo.HopDong HD ON HD.HopDongID = tchdctp.HopDongREF
				LEFT JOIN  dbo.ThucTreoKhongDuocTinh_PR TT ON l.ThucChayHopDongChiTietPRID = TT.ThucChayHopDongChiTietPRID
		WHERE TT.ThucChayHopDongChiTietPRID IS NULL
				AND	l.ID IN (SELECT MIN(ID) FROM @List GROUP BY ThucChayHopDongChiTietPRID)
        --ORDER BY l.ThucChayHopDongChiTietPRID


		SELECT 
				[HopDongID],
				[SoHopDong],
				[HTQC],
                [SanPham] ,
				[DonGia],
                [ChietKhau] ,
                [TenWebsite] ,
				[NhanHang],
				[NguyenNhanKhongDuocTinh],
				[LinkThucTreo],
				ISNULL([LoaiThucTreo],'')LoaiThucTreo
	  FROM  dbo.ThucTreoKhongDuocTinh_PR t
		WHERE CONVERT(DATE,t.Create_at) = CONVERT(DATE,GETDATE())
		AND t.NguyenNhanKhongDuocTinh NOT LIKE N'%Tiền thực chạy đã vượt HĐCT'

    END

	select * from ThucTreoKhongDuocTinh_PR where HopDongID = 1013459
```
