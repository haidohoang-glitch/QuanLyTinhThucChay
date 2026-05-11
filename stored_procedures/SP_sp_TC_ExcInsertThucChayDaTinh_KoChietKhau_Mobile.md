# Stored Procedure: `sp_TC_ExcInsertThucChayDaTinh_KoChietKhau_Mobile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-23 17:56:42.300000
- **Ngày sửa cuối**: 2023-09-22 15:46:06.007000

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
 
CREATE PROCEDURE [dbo].[sp_TC_ExcInsertThucChayDaTinh_KoChietKhau_Mobile]
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
            @ThanhTienThucChay FLOAT,
			@SoLuongLechTreoHa FLOAT

        DECLARE @HopDongChiTietID INT

        DECLARE icursor CURSOR
        FOR
            SELECT DISTINCT
                    hdct.HopDongChiTietID
            FROM    dbo.ThucChayHopDongChiTietAndBanner tc
                    INNER JOIN (SELECT * FROM dbo.HopDongChiTiet WHERE DeletedStatus = 0 AND DonViTinhREF <> 3 AND DmSanPhamREF = 342) hdct ON tc.HopDongChiTietREF = hdct.HopDongChiTietID
                    INNER JOIN (SELECT * FROM dbo.HopDong WHERE TrangThaiHopDong <> 3) hd ON tc.HopDongREF = hd.HopDongID
            WHERE   CONVERT(NVARCHAR(50), tc.DmBannerID) = CONVERT(NVARCHAR(50), @DmBannerID)
                    AND hd.SoHopDong = @SoHopDong
					AND tc.DeletedStatus = 0
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
						AND DotChayHopDong <> N'NGAY'
                GROUP BY DonViTinh


                IF ISNULL(@ThanhTienHDCT, 0) > ISNULL(@ThanhTienThucChay, 0)
                    BEGIN

                            SELECT  @SoHopDong = A.SoHopDong ,
                                    @TenWebsite = A.TenWebsite ,
                                    @TypeProduct = A.TypeProduct ,
                                    @ProductUnitName = A.ProductUnitName ,
                                    @BannerType = A.BannerType ,
                                    @DmBannerREF = A.DmBannerREF ,
                                    @TongViewThucChay = ISNULL(SUM(A.TongViewThucChay), 0)  ,
                                    @TongClickThucChay = ISNULL(SUM(A.TongClickThucChay), 0) 
                            FROM    dbo.ThucChay_MobileTemp A
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
	
                       	
																						  			
                                EXEC sp_TC_InsertThucChayDaTinh_KoChietKhau_Mobile @NgayThucHien,
                                    @SoHopDong, @TenWebsite,
                                    @HopDongChiTietID, @TypeProduct,
                                    @ProductUnitName, @BannerType,
                                    @DmBannerREF, @TongViewThucChay,
                                    @TongClickThucChay		







						DECLARE @v_DmWebsiteREF INT 
						SET @v_DmWebsiteREF = 0
	
						SET @v_DmWebsiteREF = ( SELECT TOP (1) DmWebsiteReportingdbID
												FROM    dbo.DmWebsiteReportingdb
												WHERE   DmWebsiteReportingdb.TenWebsite = @TenWebsite
												ORDER BY DmWebsiteReportingdbID
											)

						-- Xac dinh so luong lech treo ha
						SELECT @SoLuongLechTreoHa = SUM(tcdt.SoLuongThucChayLechTreoHa) 
						FROM dbo.ThucChayDaTinh tcdt 
						WHERE tcdt.NgayThucHien = @NgayThucHien
								AND tcdt.DmBannerREF = @DmBannerREF
								AND tcdt.DmWebsiteREF = @v_DmWebsiteREF
								AND tcdt.DmSanPhamREF = 342
								AND tcdt.DotChayHopDong <> N'NGAY'

				

						IF ISNULL(@SoLuongLechTreoHa, 0) = 0
							BEGIN
								BREAK
							END

						--BREAK

                    END
					SET @ThanhTienHDCT = 0
					SET @ThanhTienThucChay = 0
			 
                FETCH NEXT FROM icursor   
				INTO @HopDongChiTietID 
            END   
        CLOSE icursor;  
        DEALLOCATE icursor;  

    END
--ThucChayDaTinh_InsertThucChayMobileContractByContractNo_Banner '2015-01-21','QC3291214','afamily.vn','CLICK',4,70731

```
