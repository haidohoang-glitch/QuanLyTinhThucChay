# Stored Procedure: `ThucChay_DoDuLieuTuAPIVaoBang_ThucChay_ThanhTien_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-06-16 10:26:44.380000
- **Ngày sửa cuối**: 2025-09-26 16:53:53.697000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuThuViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

--EXEC [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_ThucChay_ThanhTien_Admatic_Dev] '2025-09-24', 240
CREATE PROCEDURE [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_ThucChay_ThanhTien_Admatic] 
	 @NgayThucHien DATETIME,
	 @DmSanPhamREF INT
AS
BEGIN
		DECLARE @ID INT
		DECLARE @Count INT= 0
        DECLARE @slsite INT = 0
        DECLARE @v_TenWebsite NVARCHAR(1000)
		DECLARE @V_Campaign_id BIGINT = 0
		DECLARE @NgayThucHien_VAT10 DATETIME = '2023-01-01'

		SET @V_Campaign_id = 26829--1000000--26840 --Bat dau tu chien dich ap dung phuong thuc tinh thue VAT = 8%

	
		IF @NgayThucHien IS NULL
			BEGIN
			    SET @NgayThucHien = DATEADD(dd, -1, GETDATE())	

				SET @NgayThucHien = CONVERT(DATE, @NgayThucHien)
			END

            IF NOT EXISTS ( SELECT TOP (1) DmSanPhamREF
                            FROM    dbo.[ThucChay_ThanhTien_Admatic]
                            WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                    AND DmSanPhamREF = @DmSanPhamREF 
								
								ORDER BY DmSanPhamREF
							)
            BEGIN

                    SET @Count = 0
                    SET @slsite = 0
                    SET @v_TenWebsite =''

                    SET @slsite = ( SELECT  COUNT(DISTINCT a.domain_name)
                                    FROM    ( SELECT    [dbo].[GetWebsiteIDByDomainName](domain_name) DmWebsiteREF ,
                                                        domain_name
                                                FROM      dbo.DataThucChay_Admatic_v2
                                                WHERE     CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                                          AND DmSanPhamREF = @DmSanPhamREF
                                            ) a
                                    WHERE   a.DmWebsiteREF IS NULL
                                    )
                    IF ( @slsite > 0 )
                        WHILE @Count < @slsite
                            BEGIN
                                SET @v_TenWebsite = ( SELECT TOP (1) domain_name FROM
                                                        ( SELECT
                                                            [dbo].[GetWebsiteIDByDomainName](domain_name) DmWebsiteREF ,
                                                            domain_name
                                                            FROM dbo.DataThucChay_Admatic_v2
                                                            WHERE CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                                            AND DmSanPhamREF = @DmSanPhamREF
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


                    INSERT  INTO dbo.[ThucChay_ThanhTien_Admatic]
                    (
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
                        [ThanhTienThucChaySauCK_ChuaVAT],
                        ThanhTienThucChayKM,
                        NgayThucHien,
                        CreatedAt,
                        CreatedBy,
                        LastModifiedAt,
                        LastModifiedBy,
                        DeletedStatus,
						vat,
						HopDongChiTietREF
                    )
                  
                           
				SELECT contract_number AS [SoHopDong]
					  ,CONVERT(INT,DmSanPhamREF) AS [TypeProduct]
					  ,CONVERT(INT,DmSanPhamREF) AS DmSanPhamREF
					  ,[TenSanPham]
					  ,NhanHang
					  ,CONVERT(INT,ISNULL(NhanHangID,0)) AS [NhanHangID]
					  ,CONVERT(INT,ISNULL(banner_id,0)) AS [DmBannerID]
					  ,ISNULL(dbo.GetWebsiteIDByDomainName(domain_name),0) AS [DmWebsiteID]
					  ,domain_name AS [TenWebsite]
					  ,CONVERT(INT,ISNULL(DmViTriREF,0)) AS [DmViTriREF]
					  ,TenViTri
					  ,(CASE WHEN ProductUnitName = N'CPM' and ((convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) = 0) 
																or (convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) <> 0))   
							THEN  CONVERT(BIGINT,ISNULL(domain_tt_view,0)) 
						WHEN ProductUnitName = N'CPC' and ((convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) = 0)  
														or (convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) <> 0))
							THEN CONVERT(BIGINT,ISNULL(domain_tt_click,0)) 
						WHEN ProductUnitName = N'TRUEVIEW' and ((convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) = 0)   
														or (convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) <> 0))
							THEN  CONVERT(BIGINT,ISNULL(domain_tt_view,0)) 
						WHEN ProductUnitName = N'TRUE VIEW' and ((convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) = 0)
														or   (convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) <> 0) )
							THEN  CONVERT(BIGINT,ISNULL(domain_tt_view,0)) 
						ELSE 0--CONVERT(BIGINT,ISNULL(domain_tt_view,0)) --tuyetnta cf
					  END ) AS [SoLuongThucChay]
					  ,(CASE WHEN ProductUnitName = N'CPM' and (convert(float,domain_tt_money)  = 0 and convert(float,domain_tt_promotion) <> 0) THEN  CONVERT(BIGINT,ISNULL(domain_tt_view,0)) 
						WHEN ProductUnitName = N'CPC' and (convert(float,domain_tt_money)  = 0 and convert(float,domain_tt_promotion) <> 0) THEN CONVERT(BIGINT,ISNULL(domain_tt_click,0)) 
						WHEN ProductUnitName = N'TRUEVIEW' and (convert(float,domain_tt_money)  = 0 and convert(float,domain_tt_promotion) <> 0) THEN  CONVERT(BIGINT,ISNULL(domain_tt_view,0)) 
						WHEN ProductUnitName = N'TRUE VIEW' and (convert(float,domain_tt_money)  = 0 and convert(float,domain_tt_promotion) <> 0) THEN  CONVERT(BIGINT,ISNULL(domain_tt_view,0)) 
						ELSE 0
					  END ) AS  [SoLuongThucChayKhuyenMai]
					  ,(CASE WHEN ProductUnitName =  N'CPM' THEN N'VIEW'
						WHEN ProductUnitName = N'CPC' THEN N'CLICK'
						WHEN ProductUnitName =  N'TRUEVIEW' THEN N'TRUE VIEW'
						WHEN ProductUnitName =  N'TRUE VIEW' THEN N'TRUE VIEW'
						ELSE N''
					  END) AS [DonViTinh]
					  --domain_tt_money da bao gom chietkhau va sau VAT
					  --,(CASE WHEN (ISNULL(CONVERT(BIGINT,Campaign_id),0) >= @V_Campaign_id) AND ([NgayThucHien] < @NgayThucHien_VAT10) THEN CONVERT(FLOAT,ISNULL(domain_tt_money,0))/1.08
							--ELSE CONVERT(FLOAT,ISNULL(domain_tt_money,0))/1.1
					  --END)  AS [ThanhTienThucChaySauCK_ChuaVAT] --Haidh 2022-08-04, COMMENT them viec chia cho 1.1 cua km
					  , CONVERT(FLOAT,ISNULL(domain_tt_money,0))/((CONVERT(FLOAT,ISNULL(vat,0)) + 100)/100)  AS [ThanhTienThucChaySauCK_ChuaVAT]

					  --,(CASE WHEN (ISNULL(CONVERT(BIGINT,Campaign_id),0) >= @V_Campaign_id) AND ([NgayThucHien] < @NgayThucHien_VAT10) THEN CONVERT(FLOAT,ISNULL(domain_tt_promotion,0))/1.08
							--ELSE CONVERT(FLOAT,ISNULL(domain_tt_promotion,0))/1.1
					  --END)  AS [ThanhTienThucChayKM] --Haidh 2021-08-04, COMMENT them viec chia cho 1.1 cua km
					  , CONVERT(FLOAT,ISNULL(domain_tt_promotion,0))/((CONVERT(FLOAT,ISNULL(vat,0)) + 100)/100) AS [ThanhTienThucChayKM] 
					  ,[NgayThucHien]
					  , GETDATE() AS [createdAt]
					  , [createdBy] 
					  , GETDATE() AS LastModifiedAt
					  , [createdBy] AS LastModifiedBy
					  , 0 AS DeletedStatus
					  , VAT
					  , IIF(CONVERT(INT,DmSanPhamREF) = 817,CONVERT(INT,isnull(mktFeeAllocationId,0)), CONVERT(INT,isnull(allocationId,0))) AS HopDongChiTietREF
					  
				  FROM [dbo].DataThucChay_Admatic_v2
				  WHERE NgayThucHien = @NgayThucHien
				  AND DmSanPhamREF = @DmSanPhamREF

        END

END




```
