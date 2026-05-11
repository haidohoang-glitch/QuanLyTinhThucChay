# Stored Procedure: `sp_TC_ExcInsertThucChayDaTinh_KoChietKhau_Mobile_TruongHopTreoSauChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-24 11:06:51.180000
- **Ngày sửa cuối**: 2018-02-26 10:39:55.790000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmBannerID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmWebsiteID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-05-20
-- Description:	Insert ThucChayDaTinh doi voi san pham Mobile Ads
-- =============================================
--EXEC [ThucChay_ExcInsertThucChayDaTinhMobileBanner] '2015-01-21','QC3291214',70731
-- EXEC ThucChay_ExcInsertThucChayDaTinhMobile '2014-04-13','2014-04-13','QC220414'
 
CREATE PROCEDURE [dbo].[sp_TC_ExcInsertThucChayDaTinh_KoChietKhau_Mobile_TruongHopTreoSauChay]
    @DmBannerID INT ,
    @NgayThucHien DATETIME ,
    @SoHopDong NVARCHAR(50) ,
    @DmWebsiteID INT
AS
    BEGIN
        DECLARE @ProductUnitName NVARCHAR(50) ,
            @BannerType INT ,
            @TenWebsite NVARCHAR(50) ,
            @HopDongChiTietREF INT ,
            @TypeProduct INT ,
            @TongViewThucChay INT ,
            @TongClickThucChay INT ,
            @DmBannerREF INT ,
            @ThanhTienHDCT FLOAT ,
            @ThanhTienThucChay FLOAT
			
		
        DECLARE @HopDongChiTietID INT
		
        DECLARE icursor CURSOR
        FOR
            SELECT DISTINCT
                    hdct.HopDongChiTietID
            FROM    dbo.ThucChayHopDongChiTietAndBanner tc
                    INNER JOIN (SELECT * FROM dbo.HopDongChiTiet WHERE DeletedStatus = 0 AND DonViTinhREF <> 3)hdct ON tc.HopDongChiTietREF = hdct.HopDongChiTietID
                    INNER JOIN dbo.HopDong hd ON tc.HopDongREF = hd.HopDongID
            WHERE   CONVERT(NVARCHAR(50), tc.DmBannerID) = CONVERT(NVARCHAR(50), @DmBannerID)
                    AND hd.SoHopDong = @SoHopDong
            ORDER BY hdct.HopDongChiTietID
		
        OPEN icursor  
		
        FETCH NEXT FROM icursor   
		INTO @HopDongChiTietID
		
        WHILE @@FETCH_STATUS = 0
            BEGIN  
		    
                SELECT  @ThanhTienHDCT = SUM(hdct.SoLuong * hdct.DonGia)
                FROM    dbo.HopDongChiTiet hdct
                WHERE   hdct.HopDongChiTietID = @HopDongChiTietID
                GROUP BY hdct.DonViTinh


                SELECT  @ThanhTienThucChay = SUM(ThanhTienThucChayTruocTrietKhau)
                FROM    dbo.ThucChayDaTinh
                WHERE   HopDongChiTietREF = @HopDongChiTietID
                        AND DmSanPhamREF = 342
                        AND NgayThucHien <= @NgayThucHien
                        AND DmBannerREF = @DmBannerID
                GROUP BY DonViTinh


                IF ISNULL(@ThanhTienHDCT, 0) > ISNULL(@ThanhTienThucChay, 0)
                    BEGIN
                        DECLARE Record_Cursor CURSOR
                        FOR
                            SELECT  A.SoHopDong ,
                                    A.TenWebsite ,
                                    @HopDongChiTietID ,
                                    A.TypeProduct ,
                                    A.ProductUnitName ,
                                    A.BannerType ,
                                    A.DmBannerREF ,
                                    ISNULL(SUM(A.TongViewThucChay), 0) TongViewThucChay ,
                                    ISNULL(SUM(A.TongClickThucChay), 0) TongClickThucChay
                            FROM    ThucChay_MobileTemp A
                            WHERE   1 = 1
                                    AND A.NgayThucHien < @NgayThucHien
                                    AND A.DmBannerREF = @DmBannerID
                                    AND A.SoHopDong = @SoHopDong
                                    AND A.DmWebsiteREF = @DmWebsiteID
                            GROUP BY A.SoHopDong ,
                                    A.TenWebsite ,
                                    A.ProductUnitName ,
                                    A.HopDongChiTietREF ,
                                    A.TypeProduct ,
                                    A.ProductUnitName ,
                                    A.BannerType ,
                                    A.DmBannerREF
	
                        OPEN Record_Cursor

		-- Perform the first fetch.
                        FETCH NEXT FROM Record_Cursor INTO @SoHopDong,
                            @TenWebsite, @HopDongChiTietREF, @TypeProduct,
                            @ProductUnitName, @BannerType, @DmBannerREF,
                            @TongViewThucChay, @TongClickThucChay			
                        WHILE @@FETCH_STATUS = 0
                            BEGIN																	  			
                                EXEC sp_TC_InsertThucChayDaTinh_KoChietKhau_Mobile_TruongHopTreoSauChay @NgayThucHien,
                                    @SoHopDong, @TenWebsite,
                                    @HopDongChiTietREF, @TypeProduct,
                                    @ProductUnitName, @BannerType,
                                    @DmBannerREF, @TongViewThucChay,
                                    @TongClickThucChay		
					
																								
                                FETCH NEXT FROM Record_Cursor INTO @SoHopDong,
                                    @TenWebsite, @HopDongChiTietREF,
                                    @TypeProduct, @ProductUnitName,
                                    @BannerType, @DmBannerREF,
                                    @TongViewThucChay, @TongClickThucChay
                            END

                        CLOSE Record_Cursor
                        DEALLOCATE Record_Cursor
						BREAK
                    END

                FETCH NEXT FROM icursor   
		    INTO @HopDongChiTietID 
            END   
        CLOSE icursor;  
        DEALLOCATE icursor;  
	
    END
--ThucChayDaTinh_InsertThucChayMobileContractByContractNo_Banner '2015-01-21','QC3291214','afamily.vn','CLICK',4,70731
```
