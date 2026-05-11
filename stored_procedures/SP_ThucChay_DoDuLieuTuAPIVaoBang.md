# Stored Procedure: `ThucChay_DoDuLieuTuAPIVaoBang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-13 16:01:22.043000
- **Ngày sửa cuối**: 2022-12-06 09:33:39.117000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ID` | `int(4)` | No |
| `@Case` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuThuViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================
/*
EXEC [ThucChay_DoDuLieuTuAPIVaoBang] -3,1,'2019-08-16'
*/
CREATE PROCEDURE [dbo].[ThucChay_DoDuLieuTuAPIVaoBang] 
-- Add the parameters for the stored procedure here
    @ID INT, @Case INT, @NgayThucHien DATETIME
AS
    BEGIN

	PRINT '[ThucChay_DoDuLieuTuAPIVaoBang]'
	PRINT @ID
		IF @NgayThucHien IS NULL
			BEGIN
			    SET @NgayThucHien = DATEADD(dd, -1, GETDATE())	

				SET @NgayThucHien = CONVERT(DATE, @NgayThucHien)
			END
        

		DECLARE @Count INT= 0
        DECLARE @slsite INT = 0
        DECLARE @v_TenWebsite NVARCHAR(1000)

	
--------------------------------- 1


        IF @Case = 1
            BEGIN
                IF NOT EXISTS ( SELECT  *
                                FROM    dbo.ThucChay
                                WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                        AND TypeProduct = @ID 
										AND CreatedBy LIKE N'From API')
                    BEGIN

                        SET @Count = 0
                        SET @slsite = 0
                        SET @v_TenWebsite =''

                        SET @slsite = ( SELECT  COUNT(DISTINCT a.TenWebsite)
                                        FROM    ( SELECT    [dbo].[GetWebsiteIDByDomainName](TenWebsite) DmWebsiteREF ,
                                                            TenWebsite
                                                  FROM      dbo.DataThucChay
                                                  WHERE     CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                                            AND TypeProduct = @ID
                                                ) a
                                        WHERE   a.DmWebsiteREF IS NULL
                                      )
                        IF ( @slsite > 0 )
                            WHILE @Count < @slsite
                                BEGIN
                                    SET @v_TenWebsite = ( SELECT TOP (1)
                                                              TenWebsite
                                                          FROM
                                                              ( SELECT
                                                              [dbo].[GetWebsiteIDByDomainName](TenWebsite) DmWebsiteREF ,
                                                              TenWebsite
                                                              FROM
                                                              dbo.DataThucChay
                                                              WHERE
                                                              CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                                              AND TypeProduct = @ID
                                                              ) a
                                                          WHERE
                                                              a.DmWebsiteREF IS NULL
															  ORDER BY a.DmWebsiteREF
                                                        )
									
									IF @v_TenWebsite IS NOT NULL
										BEGIN
										    INSERT  INTO dbo.DmWebsiteReportingdb
													( TenWebsite ,
													  CreatedBy ,
													  CreatedAt ,
													  LastModifiedBy ,
													  LastModifiedAt ,
													  DeletedStatus ,
													  PrintStatus ,
													  RecordStatus ,
													  ID
													)
											VALUES  ( @v_TenWebsite ,	-- TenWebsite - nvarchar(200)
													  N'asd' ,	-- CreatedBy - nvarchar(50)
													  GETDATE() ,	-- CreatedAt - datetime
													  N'asd' ,	-- LastModifiedBy - nvarchar(50)
													  GETDATE() ,	-- LastModifiedAt - datetime
													  0 ,	-- DeletedStatus - int
													  0 ,	-- PrintStatus - int
													  0 ,	-- RecordStatus - int
													  N'New' -- ID - nvarchar(50)
													)	
										END
                                    

                                    SET @Count = @Count + 1
                                END


                        INSERT  INTO dbo.ThucChay
                                ( ThucChayID ,
                                  SoHopDong ,
                                  DanhsachDmBookingREF ,
                                  DmSanPhamREF ,
                                  TenSanPham ,
                                  DmNhomWebsiteREF ,
                                  TenNhomWebsite ,
                                  DmWebsiteREF ,
                                  TenWebsite ,
                                  DmChienDichREF ,
                                  TenChienDich ,
                                  DmBannerREF ,
                                  TenBanner ,
                                  NgayThucHien ,
                                  TongViewThucChay ,
                                  TongClickThucChay ,
                                  CreatedBy ,
                                  CreatedAt ,
                                  LastModifiedBy ,
                                  LastModifiedAt ,
                                  DeletedStatus ,
                                  PrintStatus ,
                                  RecordStatus ,
                                  TongSoBaiViet ,
                                  SoThuTuTheoNgay ,
                                  TypeProduct ,
                                  BannerType ,
                                  UserName ,
                                  SaleName ,
                                  Email ,
                                  LastTimeCalc ,
                                  sys_date ,
                                  IsReady ,
                                  ProductUnitID ,
                                  ProductUnitName ,
                                  BannerTypeName ,
                                  HopDongChiTietREF ,
                                  CampainStatus ,
                                  BannerStatus ,
                                  IsNoiBo
                                )
                                SELECT  ThucChayID ,
                                        SoHopDong ,
                                        DanhsachDmBookingREF ,
                                        [dbo].[GetProductIDByTypeProduct](TypeProduct) as DmSanPhamREF  ,
                                        TenSanPham ,
                                        DmNhomWebsiteREF ,
                                        TenNhomWebsite ,
                                        ISNULL(dbo.GetWebsiteIDByDomainName(TenWebsite),
                                               0) ,
                                        TenWebsite ,
                                        DmChienDichREF ,
                                        TenChienDich ,
                                        DmBannerREF ,
                                        TenBanner ,
                                        NgayThucHien ,
                                        TongViewThucChay ,
                                        TongClickThucChay ,
                                        N'From API' ,
                                        GETDATE() createdAt ,
                                        N'From API' ,
                                        GETDATE() createdAt ,
                                        0 ,
                                        0 ,
                                        0 ,
                                        TongSoBaiViet ,
                                        SoThuTuTheoNgay ,
                                        TypeProduct ,
                                        bannertype ,
                                        username ,
                                        salename ,
                                        email ,
                                        GETDATE() LastTimeCalc ,
                                        GETDATE() sys_date ,
                                        IsReady ,
                                        ProductUnitID ,
                                        ProductUnitName ,
                                        BannerTypeName ,
                                        HopDongChiTietREF ,
                                        CampainStatus ,
                                        BannerStatus ,
                                        IsNoiBo
                                FROM    dbo.DataThucChay
                                WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                        AND TypeProduct = @ID
                    END
            END

  
  --------------------------------------- 2      
  --THUC CHAY UV CHO DON VI TINH CPR
        IF @Case = 2
            BEGIN
                IF NOT EXISTS ( SELECT  *
                                FROM    dbo.ThucChayCPR
                                WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                        AND typeproduct = @ID AND CONVERT(INT,ISNULL(uv,0)) >0)
                    BEGIN
                        INSERT  INTO dbo.ThucChayCPR
                                ( bannerid ,
                                  uvNgay ,
                                  uv ,
                                  typeproduct ,
                                  ProductName ,
                                  NgayThucHien ,
                                  ThoiGianTao ,
                                  uvhour ,
                                  TVDenNgay ,
                                  TCDenNgay
                                )
                                SELECT  tc.bannerid ,
                                        (tc.uv -
										ISNULL((
											SELECT TOP 1 CONVERT(INT,ISNULL(dc.uv,0)) FROM dbo.DataThucChayCPR dc
											WHERE dc.bannerid = tc.bannerid
											AND dc.NgayThucHien < tc.NgayThucHien
											AND dc.typeproduct = tc.typeproduct
											ORDER BY dc.NgayThucHien desc
										),0))uvngay ,
                                        tc.uv ,
                                        tc.typeproduct ,
                                        tc.ProductName ,
                                        tc.NgayThucHien ,
                                        GETDATE() ,
                                        '' ,
                                        NULL ,
                                        NULL
                                FROM    dbo.DataThucChayCPR tc
                                WHERE   CONVERT(DATE, tc.NgayThucHien) = @NgayThucHien
                                        AND tc.typeproduct = @ID
										AND CONVERT(INT,ISNULL(tc.uv,0)) >0

                    END
            END

		-------------------------------- 3

        IF @Case = 3
            BEGIN
                IF NOT EXISTS ( SELECT  *
                                FROM    dbo.ThucChayCPV
                                WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien )
                    BEGIN
                        INSERT  INTO dbo.ThucChayCPV
                                ( typeproduct ,
                                  ProductName ,
                                  bannerid ,
                                  totalview ,
                                  percent_rate ,
                                  CPV ,
                                  NgayThucHien
                                )
                                SELECT  typeproduct ,
                                        ProductName ,
                                        bannerid ,
                                        totalview ,
                                        percent_rate ,
                                        CPV ,
                                        NgayThucHien
                                FROM    dbo.DataThucChayCPV_TVC
                                WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien
                    END
			    
            END

		--------------------------------- 4

			
        IF @Case = 4
            BEGIN
                IF NOT EXISTS ( SELECT  *
                                FROM    dbo.ThucChayTrueView
                                WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien )
                    BEGIN

                        SET @Count = 0
                        SET @slsite = 0
                        SET @v_TenWebsite =''

                        SET @slsite = ( SELECT  COUNT(DISTINCT a.TenWebsite)
                                        FROM    ( SELECT    [dbo].[GetWebsiteIDByDomainName](SiteName) DmWebsiteREF ,
                                                            SiteName TenWebsite
                                                  FROM      dbo.DataThucChay_TrueView
                                                  WHERE     CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                                ) a
                                        WHERE   a.DmWebsiteREF IS NULL
                                      )
                        IF ( @slsite > 0 )
                            WHILE @Count < @slsite
                                BEGIN
                                    SET @v_TenWebsite = ( SELECT TOP 1
                                                              TenWebsite
                                                          FROM
                                                              ( SELECT
                                                              [dbo].[GetWebsiteIDByDomainName](SiteName) DmWebsiteREF ,
                                                              SiteName TenWebsite
                                                              FROM
                                                              dbo.DataThucChay_TrueView
                                                              WHERE
                                                              CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                                              ) a
                                                          WHERE
                                                              a.DmWebsiteREF IS NULL
                                                        )

									IF @v_TenWebsite IS NOT NULL
										BEGIN
										    INSERT  INTO dbo.DmWebsiteReportingdb
													( TenWebsite ,
														CreatedBy ,
														CreatedAt ,
														LastModifiedBy ,
														LastModifiedAt ,
														DeletedStatus ,
														PrintStatus ,
														RecordStatus ,
														ID
													)
											VALUES  ( @v_TenWebsite ,	-- TenWebsite - nvarchar(200)
														N'asd' ,	-- CreatedBy - nvarchar(50)
														GETDATE() ,	-- CreatedAt - datetime
														N'asd' ,	-- LastModifiedBy - nvarchar(50)
														GETDATE() ,	-- LastModifiedAt - datetime
														0 ,	-- DeletedStatus - int
														0 ,	-- PrintStatus - int
														0 ,	-- RecordStatus - int
														N'New' -- ID - nvarchar(50)
													)	
										END
                                    

                                    SET @Count = @Count + 1
                                END


                        INSERT  INTO dbo.ThucChayTrueView
                                ( SoHopDong ,
                                  TypeProduct ,
                                  DmSanPhamREF ,
                                  TenSanPham ,
                                  campaignid ,
                                  bannerid ,
                                  SiteName ,
                                  SiteID ,
                                  True_View ,
                                  [Views] ,
                                  Clicks ,
                                  NgayThucHien ,
                                  CreatedBy ,
                                  CreatedAt ,
                                  LastModifiedBy ,
                                  LastModifiedAt ,
                                  DeletedStatus,
								  FormatName
                                )
                                SELECT  SoHopDong ,
                                        TypeProduct ,
                                        DmSanPhamREF ,
                                        TenSanPham ,
                                        campaignid ,
                                        bannerid ,
                                        SiteName ,
                                        ISNULL(dbo.GetWebsiteIDByDomainName(SiteName),
                                               0) ,
                                        True_View ,
                                        [Views] ,
                                        Clicks ,
                                        NgayThucHien ,
                                        createdBy ,
                                        createdAt ,
                                        createdBy ,
                                        createdAt ,
                                        0,
										FormatName
                                FROM    dbo.DataThucChay_TrueView
                                WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien
                    END
            END



---------------------------------------------- 5


        IF @Case = 5
            BEGIN
                IF NOT EXISTS ( SELECT  *
                                FROM    dbo.ThucChayBoxAppSSVOnline
                                WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien )
                    BEGIN

                        SET @Count = 0
                        SET @slsite = 0
                        SET @v_TenWebsite =''

                        SET @slsite = ( SELECT  COUNT(DISTINCT a.TenWebsite)
                                        FROM    ( SELECT    [dbo].[GetWebsiteIDByDomainName](domain) DmWebsiteREF ,
                                                            domain TenWebsite
                                                  FROM      dbo.DataThucChay_Boxapp_ssv
                                                  WHERE     CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                                ) a
                                        WHERE   a.DmWebsiteREF IS NULL
                                      )
                        IF ( @slsite > 0 )
                            WHILE @Count < @slsite
                                BEGIN
                                    SET @v_TenWebsite = ( SELECT TOP 1
                                                              TenWebsite
                                                          FROM
                                                              ( SELECT
                                                              [dbo].[GetWebsiteIDByDomainName](domain) DmWebsiteREF ,
                                                              domain TenWebsite
                                                              FROM
                                                              dbo.DataThucChay_Boxapp_ssv
                                                              WHERE
                                                              CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                                              ) a
                                                          WHERE
                                                              a.DmWebsiteREF IS NULL
                                                        )

									IF @v_TenWebsite IS NOT NULL
										BEGIN
										    INSERT  INTO dbo.DmWebsiteReportingdb
													( TenWebsite ,
													  CreatedBy ,
													  CreatedAt ,
													  LastModifiedBy ,
													  LastModifiedAt ,
													  DeletedStatus ,
													  PrintStatus ,
													  RecordStatus ,
													  ID
													)
											VALUES  ( @v_TenWebsite ,	-- TenWebsite - nvarchar(200)
													  N'asd' ,	-- CreatedBy - nvarchar(50)
													  GETDATE() ,	-- CreatedAt - datetime
													  N'asd' ,	-- LastModifiedBy - nvarchar(50)
													  GETDATE() ,	-- LastModifiedAt - datetime
													  0 ,	-- DeletedStatus - int
													  0 ,	-- PrintStatus - int
													  0 ,	-- RecordStatus - int
													  N'New' -- ID - nvarchar(50)
													)	
										END
                                    

                                    SET @Count = @Count + 1
                                END

                        INSERT  INTO dbo.ThucChayBoxAppSSVOnline
                                ( ThucChayBoxAppSSVOnlineID ,
                                  SoHopDong ,
                                  DmSanPhamREF ,
                                  TenSanPham ,
                                  DmWebsiteREF ,
                                  TenWebsite ,
                                  DonViTinh ,
                                  SoLuongThucChay ,
                                  ThanhTienThucChay ,
                                  SoLuongKhuyenMai ,
                                  ThanhTienKhuyenMai ,
                                  NgayThucHien ,
                                  GhiChu ,
                                  CreatedAt ,
                                  CreatedBy ,
                                  LastModfiedAt ,
                                  LastModifiedBy ,
                                  RecordStatus
                                )
                                SELECT  NEWID() ,
                                        [contract] ,
                                        DmSanPhamREF ,
                                        TenSanPham ,
                                        ISNULL(dbo.GetWebsiteIDByDomainName(domain),
                                               0) ,
                                        domain ,
                                        N'View' ,
                                        ttc ,
                                        [money] ,
                                        ttv ,
                                        tienkm ,
                                        NgayThucHien ,
                                        N'' ,
                                        createdAt ,
                                        createdBy ,
                                        createdAt ,
                                        createdBy ,
                                        1
                                FROM    dbo.DataThucChay_Boxapp_ssv
                                WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien
	    
                    END
            END



    END




```
