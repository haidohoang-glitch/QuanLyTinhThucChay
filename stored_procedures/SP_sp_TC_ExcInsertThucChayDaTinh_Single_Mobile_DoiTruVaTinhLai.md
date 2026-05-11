# Stored Procedure: `sp_TC_ExcInsertThucChayDaTinh_Single_Mobile_DoiTruVaTinhLai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-10-31 15:45:14.330000
- **Ngày sửa cuối**: 2022-12-01 16:37:37.050000

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
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
exec [dbo].[sp_TC_ExcInsertThucChayDaTinh_Single_Mobile] 519390, '2017-06-03', 'QC0190617', 105
--TH CÓ 01 BANNER GAN CHI VOI 01 HOPDONGCHITIET
*/
CREATE PROCEDURE [dbo].[sp_TC_ExcInsertThucChayDaTinh_Single_Mobile_DoiTruVaTinhLai]
	-- Add the parameters for the stored procedure here
    @DmBannerID INT ,
    @NgayThucHien DATETIME ,
    @SoHopDong NVARCHAR(50) ,
    @DmWebsiteID INT 
AS
    BEGIN
        DECLARE @ProductUnitName NVARCHAR(50) ,
			@HopDongID INT,
            @BannerType INT ,
            @TenWebsite NVARCHAR(50) ,
            @HopDongChiTietREF INT ,
            @TypeProduct INT ,
            @TongViewThucChay INT ,
            @TongClickThucChay INT ,
            @DmBannerREF INT
	
        DECLARE @HopDongChiTietID INT

		SET @HopDongID = (SELECT TOP (1) HopDongID FROM dbo.HopDong WHERE SoHopDong = @SoHopDong ORDER BY HopDongID)

		SET @HopDongChiTietID = 
		ISNULL(( SELECT TOP (1) hdct.HopDongChiTietID
        FROM    (
					SELECT tc.DmBannerID, tc.HopDongChiTietREF, tc.HopDongREF FROM dbo.ThucChayHopDongChiTietAndBanner tc 
					WHERE tc.HopDongREF = @HopDongID 
					AND (CONVERT(NVARCHAR(50),tc.DmBannerID )=  CONVERT(NVARCHAR(50), @DmBannerID))
					AND tc.DeletedStatus = 0
				)tc
                INNER JOIN 
				(
					SELECT hdct.HopDongChiTietID FROM dbo.HopDongChiTiet hdct 
					WHERE hdct.DmSanPhamREF = 342
					AND hdct.HopDongFK = @HopDongID
					AND NOT(hdct.DmLoaiREF IN (13,42) OR hdct.DmLoaiBannerREF = 18)
					AND hdct.DmLoaiNenTangREF <> 8 
					AND hdct.DeletedStatus = 0
				)hdct ON tc.HopDongChiTietREF = hdct.HopDongChiTietID
                INNER JOIN (SELECT hd.HopDongID, hd.SoHopDong FROM dbo.HopDong hd WHERE hd.HopDongID = @HopDongID) hd ON tc.HopDongREF = hd.HopDongID

		ORDER BY tc.HopDongChiTietREF ),0)

      	DECLARE Record_Cursor CURSOR FOR
                    SELECT  A.SoHopDong ,
                            A.TenWebsite ,
                            @HopDongChiTietID ,
                            A.TypeProduct ,
                            A.ProductUnitName ,
                            A.BannerType ,
                            A.DmBannerREF ,
                            ISNULL(SUM(A.TongViewThucChay), 0) TongViewThucChay ,
                            ISNULL(SUM(A.TongClickThucChay), 0) TongClickThucChay
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
	
        OPEN Record_Cursor

		-- Perform the first fetch.
                FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TenWebsite,
                    @HopDongChiTietREF, @TypeProduct, @ProductUnitName,
                    @BannerType, @DmBannerREF, @TongViewThucChay,
                    @TongClickThucChay			
                WHILE @@FETCH_STATUS = 0
                    BEGIN			
															  			
                        EXEC dbo.sp_TC_InsertThucChayDaTinh_Mobile_DoiTruVaTinhLai @NgayThucHien,
                            @SoHopDong, @TenWebsite, @HopDongChiTietREF,
                            @TypeProduct, @ProductUnitName, @BannerType,
                            @DmBannerREF, @TongViewThucChay,
                            @TongClickThucChay	
																	
                        FETCH NEXT FROM Record_Cursor INTO @SoHopDong,
                            @TenWebsite, @HopDongChiTietREF, @TypeProduct,
                            @ProductUnitName, @BannerType, @DmBannerREF,
                            @TongViewThucChay, @TongClickThucChay
                    END

        CLOSE Record_Cursor
        DEALLOCATE Record_Cursor

	END

```
