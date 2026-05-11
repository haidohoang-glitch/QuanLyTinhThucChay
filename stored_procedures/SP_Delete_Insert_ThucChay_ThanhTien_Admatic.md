# Stored Procedure: `Delete_Insert_ThucChay_ThanhTien_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-06-01 15:36:34.250000
- **Ngày sửa cuối**: 2022-06-01 15:53:02.007000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@pBannerID` | `nvarchar` | No |
| `@SanPhamID` | `int(4)` | No |

## Definition (Source Code)

```sql
/*
EXEC Delete_Insert_ThucChay_ThanhTien_Admatic '86339,86340,86647', 240
*/

CREATE PROCEDURE [dbo].[Delete_Insert_ThucChay_ThanhTien_Admatic] 	
	 @pBannerID NVARCHAR(MAX)
	,@SanPhamID INT=0
AS
BEGIN
	DELETE ThucChay_ThanhTien_Admatic WHERE DmBannerID IN (SELECT * FROM STRING_SPLIT(@pBannerID)) AND DmSanPhamREF= @SanPhamID


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
                        DeletedStatus
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
					  ,CONVERT(FLOAT,ISNULL(domain_tt_money,0))/1.08 AS [ThanhTienThucChaySauCK_ChuaVAT]
					  ,CONVERT(FLOAT,ISNULL(domain_tt_promotion,0))/1.08 AS [ThanhTienThucChayKM]
					  ,[NgayThucHien]
					  , GETDATE() AS [createdAt]
					  , [createdBy] 
					  , GETDATE() AS LastModifiedAt
					  , [createdBy] AS LastModifiedBy
					  , 0 AS DeletedStatus
					 
				  FROM [dbo].DataThucChay_Admatic_v2_test
				 --SELECT * from DataThucChay_Admatic_v2_test
				  --WHERE 1=1  and banner_id in (85003, 85004, 84862, 84864) and CONVERT(date,NgayThucHien) BETWEEN '2022-03-02' AND '2022-03-09'
				  WHERE 1=1  AND banner_id IN (SELECT * FROM STRING_SPLIT(@pBannerID)) AND DmSanPhamREF= @SanPhamID
END;
```
