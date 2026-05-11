# Stored Procedure: `sp_Notify_CheckThucTreoKhongDungVoiPhanBo_PR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-09-06 14:45:04.277000
- **Ngày sửa cuối**: 2018-09-06 14:45:04.277000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
create PROCEDURE [dbo].[sp_Notify_CheckThucTreoKhongDungVoiPhanBo_PR]
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

--select * from [ABM_Data_ThucChay].dbo.ThucChayHopDongChiTietPR [192.168.5.38,48030].ABM_Data_ThucChay

        DECLARE @DanhSachKoDuocTinh TABLE
            (
              ThucChayHopDongChiTietPRID INT,
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
            FROM    [ABM_Data_ThucChay].dbo.ThucChayHopDongChiTietPR
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
            FROM    [ABM_Data_ThucChay].dbo.ThucChayHopDongChiTietPR PR
                    INNER JOIN [ABM_Data_ThucChay].dbo.HopDong hd ON PR.HopDongREF = hd.HopDongID
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
                                              FROM      [ABM_Data_ThucChay].dbo.HopDongChiTiet hdct
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
                                                      FROM    [ABM_Data_ThucChay].dbo.HopDongChiTiet hdct
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
                                                      FROM    [ABM_Data_ThucChay].dbo.HopDongChiTiet hdct
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
                                                              FROM [ABM_Data_ThucChay].dbo.HopDongChiTiet hdct
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
                                                      FROM    [ABM_Data_ThucChay].dbo.HopDongChiTiet hdct
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
                                                              FROM [ABM_Data_ThucChay].dbo.HopDongChiTiet hdct
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
                                                      FROM    [ABM_Data_ThucChay].dbo.HopDongChiTiet hdct
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
                                                              FROM [ABM_Data_ThucChay].dbo.HopDongChiTiet hdct
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
                                                      FROM    [ABM_Data_ThucChay].dbo.HopDongChiTiet hdct
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
                                                              FROM [ABM_Data_ThucChay].dbo.HopDongChiTiet hdct
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
                                                      FROM    [ABM_Data_ThucChay].dbo.HopDongChiTiet hdct
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
																      FROM [ABM_Data_ThucChay].dbo.HopDongChiTiet hdct
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
                            FROM    [ABM_Data_ThucChay].dbo.ThucChayHopDongChiTietPR tchdctp
                            WHERE   tchdctp.ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID


							
                            SELECT  @ThanhTienThucChay = ISNULL(SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0)
                                                              + ISNULL(tcdt.GiaTriThayDoi,0)), 0)
                            FROM    [ABM_Data_ThucChay].dbo.ThucChayDaTinh tcdt
                            WHERE   tcdt.HopDongChiTietREF = @HDCTID
			


                            SET @ThanhTienThucTreo = ISNULL(@ThanhTienThucTreo,
                                                            0)
                            SET @ThanhTienThucChay = ISNULL(@ThanhTienThucChay,
                                                            0)


                            DECLARE @ThanhTienHDCT FLOAT

                            SELECT  @ThanhTienHDCT = hdct.ThanhTien
                            FROM    [ABM_Data_ThucChay].dbo.HopDongChiTiet hdct
                            WHERE   hdct.HopDongChiTietID = @HDCTID



                            IF @ThanhTienHDCT < @ThanhTienThucChay
                                + @ThanhTienThucTreo
                                BEGIN
									IF NOT EXISTS (SELECT * 
													FROM [ABM_Data_ThucChay].dbo.ThucChayDaTinh
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


		SELECT DISTINCT
				tchdctp.HopDongREF HopDongID,
				HD.SoHopDong,
				HT.TenHinhThucQuangCao HTQC,
				SP.TenSanPham SanPham ,
				tchdctp.GiaTien DonGia,
                tchdctp.ChietKhau ,
                tchdctp.TenWebsite ,
				tchdctp.NhanHang,
				l.GhiChu NguyenNhanKhongDuocTinh,
				tchdctp.Link LinkThucTreo,
				HD.SysNhanVienREF,
				sale.email_official as Mail, 			
				Cc = null
				INTO #tempData
        FROM    @List l
                INNER JOIN [ABM_Data_ThucChay].dbo.ThucChayHopDongChiTietPR tchdctp ON l.ThucChayHopDongChiTietPRID = tchdctp.ThucChayHopDongChiTietPRID
				INNER JOIN [ABM_Data_ThucChay].dbo.HopDong HD ON HD.HopDongID = tchdctp.HopDongREF
				LEFT JOIN [ABM_Data_ThucChay].dbo.ThucTreoKhongDuocTinh_PR TT ON l.ThucChayHopDongChiTietPRID = TT.ThucChayHopDongChiTietPRID
				LEFT JOIN [ABM_Data_ThucChay].dbo.DmSanPham SP ON tchdctp.DmSanPhamREF = SP.DmSanPhamID
				LEFT JOIN [ABM_Data_ThucChay].dbo.DmHinhThucQuangCao HT ON HT.DmHinhThucQuangCaoID = tchdctp.DmHinhThucQuangCaoREF
				LEFT JOIN [HRM].[dbo].[vw_employees] AS sale ON sale.ID = HD.SysNhanVienREF
		WHERE TT.ThucChayHopDongChiTietPRID IS NULL
				AND	l.ID IN (SELECT MIN(ID) FROM @List GROUP BY ThucChayHopDongChiTietPRID)

		-- Kiểm tra data trả về có dữ liệu thì đưa vào bảng tạm, không có dữ liệu nào thì xóa dữ liệu trong bảng tạm
		IF EXISTS (SELECT TOP 1 * FROM #tempData) 
		BEGIN

			INSERT INTO Tmp_TanSuatCanhBaoThucTreoKhongDung_PR
			SELECT HopDongID,SoHopDong,SysNhanVienREF,Mail,GETDATE() AS TimeSendMail, 0 as SendNumber 
			FROM #tempData
			WHERE 
				HopDongID NOT IN(SELECT HopDongID FROM Tmp_TanSuatCanhBaoThucTreoKhongDung_PR)
				AND SysNhanVienREF NOT IN (SELECT SysNhanVienREF FROM Tmp_TanSuatCanhBaoThucTreoKhongDung_PR)
		END
		ELSE
		BEGIN
			DELETE  FROM Tmp_TanSuatCanhBaoThucTreoKhongDung_PR 
		END

		-- Select những bản ghi phát sinh thực chạy và chưa tồn tại trong bảng tạm
		SELECT a.HopDongID,a.SoHopDong,a.HTQC,a.SanPham,a.DonGia,a.ChietKhau,a.TenWebsite,a.NhanHang,a.NguyenNhanKhongDuocTinh,a.LinkThucTreo,a.Mail,a.Cc
		INTO #tmpGuiLan1
		FROM #tempData AS a
			LEFT JOIN Tmp_TanSuatCanhBaoThucTreoKhongDung_PR AS b
				ON a.HopDongID = b.HopDongID
		WHERE 
			b.SendNumber = 0

		-- Update những bản ghi có trong #tmpGuiLan1 lên trạng thái được gửi lần đầu	  
        IF EXISTS (SELECT TOP 1 * FROM #tmpGuiLan1)
			BEGIN 
				UPDATE Tmp_TanSuatCanhBaoThucTreoKhongDung_PR SET SendNumber = 1 
					WHERE EXISTS (SELECT HopDongID,SoHopDong,SysNhanVienREF,Mail FROM #tmpGuiLan1)
			END
		
		-- Nhắc lại lần 2 sau 9 Ngày
		SELECT a.HopDongID,a.SoHopDong,a.HTQC,a.SanPham,a.DonGia,a.ChietKhau,a.TenWebsite,a.NhanHang,a.NguyenNhanKhongDuocTinh,a.LinkThucTreo,a.Mail,a.Cc
		INTO #tmpGuiLan2
		FROM #tempData AS a
				LEFT JOIN Tmp_TanSuatCanhBaoThucTreoKhongDung_PR AS b
					ON a.HopDongID = b.HopDongID
					AND a.SysNhanVienREF = b.SysNhanVienREF
		WHERE 
				b.SendNumber <> 0 AND b.SendNumber <> 2
				AND DATEDIFF (Day,CONVERT(datetime, b.TimeSendMail), GETDATE()) = 9

		-- Update những bản ghi có trong #tmpGuiLan2 lên trạng thái được gửi lần 2	  
        IF EXISTS (SELECT TOP 1 * FROM #tmpGuiLan2)
			BEGIN 
				UPDATE Tmp_TanSuatCanhBaoThucTreoKhongDung_PR SET SendNumber = 2 
					WHERE HopDongID IN (SELECT HopDongID FROM #tmpGuiLan2) AND 
						  SysNhanVienREF IN (SELECT SysNhanVienREF FROM #tmpGuiLan2)
			END

		-- Nhắc lại lần 3 sau 19 ngày
		SELECT a.HopDongID,a.SoHopDong,a.HTQC,a.SanPham,a.DonGia,a.ChietKhau,a.TenWebsite,a.NhanHang,a.NguyenNhanKhongDuocTinh,a.LinkThucTreo,a.Mail,a.Cc
		INTO #tmpGuiLan3
		FROM #tempData AS a
				LEFT JOIN Tmp_TanSuatCanhBaoThucTreoKhongDung_PR AS b
					ON a.HopDongID = b.HopDongID
					AND a.SysNhanVienREF = b.SysNhanVienREF
		WHERE 
				b.SendNumber <> 0 AND b.SendNumber <> 3
				AND DATEDIFF (Day,CONVERT(datetime, b.TimeSendMail), GETDATE()) = 19		

		-- Update những bản ghi có trong #tmpGuiLan3 lên trạng thái được gửi lần 3	  
        IF EXISTS (SELECT TOP 1 * FROM #tmpGuiLan3)
			BEGIN 
				UPDATE Tmp_TanSuatCanhBaoThucTreoKhongDung_PR SET SendNumber = 3 
					WHERE HopDongID IN (SELECT HopDongID FROM #tmpGuiLan3) AND 
						  SysNhanVienREF IN (SELECT SysNhanVienREF FROM #tmpGuiLan3)
			END

		-- Nhắc lại lần 4 sau 29 ngày
		SELECT a.HopDongID,a.SoHopDong,a.HTQC,a.SanPham,a.DonGia,a.ChietKhau,a.TenWebsite,a.NhanHang,a.NguyenNhanKhongDuocTinh,a.LinkThucTreo,a.Mail,a.Cc
		INTO #tmpGuiLan4
		FROM #tempData AS a
				LEFT JOIN Tmp_TanSuatCanhBaoThucTreoKhongDung_PR AS b
					ON a.HopDongID = b.HopDongID
					AND a.SysNhanVienREF = b.SysNhanVienREF
		WHERE 
				b.SendNumber <> 0 AND b.SendNumber <> 4
				AND DATEDIFF (Day,CONVERT(datetime, b.TimeSendMail), GETDATE()) = 29

		-- Update những bản ghi có trong #tmpGuiLan4 lên trạng thái được gửi lần 4	  
        IF EXISTS (SELECT TOP 1 * FROM #tmpGuiLan4)
			BEGIN 
				UPDATE Tmp_TanSuatCanhBaoThucTreoKhongDung_PR SET SendNumber = 4 
					WHERE HopDongID IN (SELECT HopDongID FROM #tmpGuiLan4) AND 
						  SysNhanVienREF IN (SELECT SysNhanVienREF FROM #tmpGuiLan4)
			END
		-- Tổng hợp các bản ghi chưa được gửi và những bản ghi đã có trong bảng tạm được gửi nhắc lại theo thời gian		
			SELECT * FROM #tmpGuiLan1
		UNION ALL
			-- Nhắc lại lần 2 sau 9 Ngày
			SELECT * FROM #tmpGuiLan2	
		UNION ALL
			-- Nhắc lại lần 3 sau 19 ngày
			SELECT * FROM #tmpGuiLan3
		UNION ALL
			-- Nhắc lại lần 4 sau 29 ngày
			SELECT * FROM #tmpGuiLan4

		INSERT INTO [ABM_Data_ThucChay].dbo.ThucTreoKhongDuocTinh_PR
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
				tchdctp.Link LinkThucTreo
				, l.ThucChayHopDongChiTietPRID
				, GETDATE()
                --tchdctp.DmDonViTinhREF ,
                --ThucChayHopDongChiTietPrREF ,
                --tchdctp.*
        FROM    @List l
                INNER JOIN [ABM_Data_ThucChay].dbo.ThucChayHopDongChiTietPR tchdctp ON l.ThucChayHopDongChiTietPRID = tchdctp.ThucChayHopDongChiTietPRID
				INNER JOIN [ABM_Data_ThucChay].dbo.HopDong HD ON HD.HopDongID = tchdctp.HopDongREF
				LEFT JOIN [ABM_Data_ThucChay].dbo.ThucTreoKhongDuocTinh_PR TT ON l.ThucChayHopDongChiTietPRID = TT.ThucChayHopDongChiTietPRID
		WHERE TT.ThucChayHopDongChiTietPRID IS NULL
				AND	l.ID IN (SELECT MIN(ID) FROM @List GROUP BY ThucChayHopDongChiTietPRID)
        --ORDER BY l.ThucChayHopDongChiTietPRID
		DROP TABLE #tempData

    END
	
	-- sp_Notify_CheckThucTreoKhongDungVoiPhanBo_PR
```
