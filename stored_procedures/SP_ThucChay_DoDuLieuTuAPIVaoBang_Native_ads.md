# Stored Procedure: `ThucChay_DoDuLieuTuAPIVaoBang_Native_ads`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-07-27 11:17:35.117000
- **Ngày sửa cuối**: 2023-07-01 16:49:29.240000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@TypeProduct` | `int(4)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuThuViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================
--EXEC [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_Native_ads] '2018-08-20', 19
CREATE PROCEDURE [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_Native_ads] 
	 @NgayThucHien DATETIME,
	 @TypeProduct INT
AS
BEGIN
		DECLARE @ID INT
		DECLARE @Count INT= 0
        DECLARE @slsite INT = 0
        DECLARE @v_TenWebsite NVARCHAR(1000)
		DECLARE @v_CampaignID BIGINT = 0
		DECLARE @NgayApDungVAT8 DATETIME
		DECLARE @NgayKTApDungVAT8 DATETIME

		SET @NgayApDungVAT8 = '2022-04-01'
		SET @NgayKTApDungVAT8 = '2023-01-01'
		SET @v_CampaignID = 100000000 --1313078--ID CAMPAIGN BAT DAU AP DUNG VAT = 8%

		SET @ID = @TypeProduct

		IF @NgayThucHien IS NULL
			BEGIN
			    SET @NgayThucHien = DATEADD(dd, -1, GETDATE())	

				SET @NgayThucHien = CONVERT(DATE, @NgayThucHien)
			END

            IF NOT EXISTS ( SELECT TOP (1) TypeProduct
                            FROM    dbo.ThucChay_Native_Ads
                            WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                    AND TypeProduct = @ID 
									--AND CreatedBy LIKE N'From API'
								ORDER BY TypeProduct
							)
            BEGIN

                    SET @Count = 0
                    SET @slsite = 0
                    SET @v_TenWebsite =''

                    SET @slsite = ( SELECT  COUNT(DISTINCT a.TenWebsite)
                                    FROM    ( SELECT    [dbo].[GetWebsiteIDByDomainName](TenWebsite) DmWebsiteREF ,
                                                        TenWebsite
                                                FROM      dbo.DataThucchay_Native_Ads
                                                WHERE     CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                                        AND TypeProduct = @ID
                                            ) a
                                    WHERE   a.DmWebsiteREF IS NULL
                                    )
                    IF ( @slsite > 0 )
                        WHILE @Count < @slsite
                            BEGIN
                                SET @v_TenWebsite = ( SELECT TOP (1) TenWebsite FROM
                                                        ( SELECT
                                                            [dbo].[GetWebsiteIDByDomainName](TenWebsite) DmWebsiteREF ,
                                                            TenWebsite
                                                            FROM dbo.DataThucchay_Native_Ads
                                                            WHERE CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                                            AND TypeProduct = @ID
                                                        ) a
                                                        WHERE a.DmWebsiteREF IS NULL
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


                    INSERT  INTO dbo.ThucChay_Native_Ads
                    (
                        ThucChay_Native_AdsID,
                        SoHopDong,
                        TypeProduct,
                        DmSanPhamREF,
                        TenSanPham,
                        TenNhanHang,
                        DmNhanHangREF,
                        DmBannerID,
                        DmWebsiteID,
                        TenWebsite,
                        DmViTriBannerSanPhamID,
                        TenViTriBannerSanPham,
                        SoLuongThucChay,
                        SoLuongThucChayKM,
                        DonViTinh,
                        ThanhTienThucChaySauCK,
                        ThanhTienThucChayKM,
                        NgayThucHien,
                        CreatedAt,
                        CreatedBy,
                        LastModifiedAt,
                        LastModifiedBy,
                        DeletedStatus
                    )
                  
                           
				SELECT 0 ThuChay_Native_ads_ID
					  ,[SoHopDong]
					  ,CONVERT(INT,[TypeProduct]) AS [TypeProduct]
					  ,[dbo].[GetProductIDByTypeProduct](TypeProduct) AS DmSanPhamREF
					  ,[TenSanPham]
					  ,[TenNhanHang]
					  ,CONVERT(INT,ISNULL([NhanHangID],0)) AS [NhanHangID]
					  ,CONVERT(INT,ISNULL([DmBannerID],0)) AS [DmBannerID]
					  ,ISNULL(dbo.GetWebsiteIDByDomainName(TenWebsite),0) AS [DmWebsiteID]
					  ,[TenWebsite]
					  ,CONVERT(INT,ISNULL([DmViTriREF],0)) AS [DmViTriREF]
					  ,[TenViTri]
					  ,CONVERT(BIGINT,ISNULL([SoLuongThucChay],0)) AS [SoLuongThucChay]
					  ,CONVERT(BIGINT,ISNULL([SoLuongThucChayKhuyenMai],0)) AS  [SoLuongThucChayKhuyenMai]
					  ,[DonViTinh]
					  ,(CASE WHEN (NgayThucHien >= @NgayApDungVAT8) AND (NgayThucHien < @NgayKTApDungVAT8) THEN CONVERT(FLOAT,ISNULL([ThanhTienThucChay],0))/1.08
						WHEN (NgayThucHien >= '2023-07-01') THEN CONVERT(FLOAT,ISNULL([ThanhTienThucChay],0))/(1+CONVERT(FLOAT,ISNULL(vat,0))/100 ) -- tu ngay 01-07-2023 Tinh theo VAT san pham tra --Duongnt add	01-07-2023															
						ELSE CONVERT(FLOAT,ISNULL([ThanhTienThucChay],0))/1.1
					  END) AS [ThanhTienThucChay_TruocVAT]
					  ,(CASE WHEN (NgayThucHien >= @NgayApDungVAT8) AND (NgayThucHien < @NgayKTApDungVAT8) THEN CONVERT(FLOAT,ISNULL([ThanhTienThucChaykhuyenMai],0))/1.08
							WHEN (NgayThucHien >= '2023-07-01') THEN CONVERT(FLOAT,ISNULL([ThanhTienThucChaykhuyenMai],0))/(1+CONVERT(FLOAT,ISNULL(vat,0))/100 ) -- tu ngay 01-07-2023 Tinh theo VAT san pham tra --Duongnt add	01-07-2023															
						ELSE CONVERT(FLOAT,ISNULL([ThanhTienThucChaykhuyenMai],0))/1.1
					  END) AS [ThanhTienThucChaykhuyenMai_TruocVAT]
					  ,[NgayThucHien]
					  , GETDATE() AS [createdAt]
					  , [createdBy] 
					  , GETDATE() AS LastModifiedAt
					  , [createdBy] AS LastModifiedBy
					  , 0 AS DeletedStatus

				  FROM [dbo].[DataThucchay_Native_Ads]
				  WHERE NgayThucHien = @NgayThucHien
				  AND TypeProduct = @ID

        END

END




```
