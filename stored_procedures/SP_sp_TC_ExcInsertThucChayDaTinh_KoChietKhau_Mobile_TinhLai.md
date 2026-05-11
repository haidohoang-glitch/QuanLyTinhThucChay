# Stored Procedure: `sp_TC_ExcInsertThucChayDaTinh_KoChietKhau_Mobile_TinhLai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-27 14:58:40.920000
- **Ngày sửa cuối**: 2018-02-26 10:35:36.410000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmBannerID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmWebsiteID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayTinhThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-05-20
-- Description:	Insert ThucChayDaTinh doi voi san pham Mobile Ads
-- =============================================
--EXEC [ThucChay_ExcInsertThucChayDaTinhMobileBanner] '2015-01-21','QC3291214',70731
-- EXEC ThucChay_ExcInsertThucChayDaTinhMobile '2014-04-13','2014-04-13','QC220414'
 
CREATE PROCEDURE [dbo].[sp_TC_ExcInsertThucChayDaTinh_KoChietKhau_Mobile_TinhLai]
    @DmBannerID INT ,
    @NgayThucHien DATETIME ,
    @SoHopDong NVARCHAR(50) ,
    @DmWebsiteID INT ,
    @HopDongChiTietID INT,
	@NgayTinhThucHien DATETIME
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
	
                DECLARE Record_CursorKCK CURSOR
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
                            AND A.NgayThucHien = @NgayThucHien
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
	
                OPEN Record_CursorKCK

		-- Perform the first fetch.
                FETCH NEXT FROM Record_CursorKCK INTO @SoHopDong, @TenWebsite,
                    @HopDongChiTietREF, @TypeProduct, @ProductUnitName,
                    @BannerType, @DmBannerREF, @TongViewThucChay,
                    @TongClickThucChay			
                WHILE @@FETCH_STATUS = 0
                    BEGIN																	  			
                        EXEC dbo.sp_TC_InsertThucChayDaTinh_KoChietKhau_Mobile_TinhLai @NgayThucHien,
                            @SoHopDong, @TenWebsite, @HopDongChiTietREF,
                            @TypeProduct, @ProductUnitName, @BannerType,
                            @DmBannerREF, @TongViewThucChay,
                            @TongClickThucChay		, @NgayTinhThucHien
					
																								
                        FETCH NEXT FROM Record_CursorKCK INTO @SoHopDong,
                            @TenWebsite, @HopDongChiTietREF, @TypeProduct,
                            @ProductUnitName, @BannerType, @DmBannerREF,
                            @TongViewThucChay, @TongClickThucChay
                    END

                CLOSE Record_CursorKCK
                DEALLOCATE Record_CursorKCK
  
            END

    END
--ThucChayDaTinh_InsertThucChayMobileContractByContractNo_Banner '2015-01-21','QC3291214','afamily.vn','CLICK',4,70731
```
