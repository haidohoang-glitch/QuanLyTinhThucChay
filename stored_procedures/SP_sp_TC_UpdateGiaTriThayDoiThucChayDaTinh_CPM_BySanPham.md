# Stored Procedure: `sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_CPM_BySanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-18 16:38:14.287000
- **Ngày sửa cuối**: 2017-09-18 16:38:14.287000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@pSoHopDong` | `nvarchar(100)` | No |
| `@pDmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE  PROCEDURE [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_CPM_BySanPham] 
	-- Add the parameters for the stored procedure here
    @StartDate DATETIME ,
    @EndDate DATETIME ,
    @pSoHopDong NVARCHAR(50) ,
    @pDmSanPhamREF INT
AS
    BEGIN
        DECLARE @HopDongREF INT ,
            @SoHopDong NVARCHAR(50) ,
            @HopDongChiTietID INT
        DECLARE @SoLuongDotChayHD INT ,
            @ThanhTienHDCT FLOAT ,
            @DmWebsiteREF INT ,
            @DmSanPhamREF INT
        DECLARE @NgayThucHien DATETIME ,
            @count_HDCT INT ,
            @SoLuongThucChayBF INT ,
            @DmBannerID INT
        SET @NgayThucHien = @StartDate

        WHILE ( CONVERT(DATE, @NgayThucHien) <= CONVERT(DATE, @EndDate) )
            BEGIN
                PRINT CONVERT(NVARCHAR(20), @NgayThucHien)
                SET @count_HDCT = 0
                SET @SoLuongThucChayBF = 0
                DECLARE Record_Cursor CURSOR
                FOR
                    SELECT DISTINCT
                            hd.HopDongID ,
                            hd.SoHopDong ,
                            hdcttd.DmSanPhamREF ,
                            hdcttd.HopDongChiTietREF
                    FROM    HopDong hd
                            INNER JOIN HopDongThayDoi hdtd ON hd.HopDongID = hdtd.HopDongFK
                                                              AND hd.TrangThaiHopDong <> 3
                            INNER JOIN HopDongChiTietThayDoi hdcttd ON hdtd.HopDongFK = hdcttd.HopDongFK
                                                              AND hdcttd.DmSanPhamREF = @pDmSanPhamREF
                    WHERE   1 = 1
                            AND NOT ( hdcttd.DmLoaiREF IN ( 13, 42 )
                                      OR DmLoaiBannerREF = 18
                                    )--Khong update gia tri thay doi cho HTQC Mua Ngoai 
                            AND CONVERT(DATE, hdtd.NgayThayDoi) = @NgayThucHien
                            AND ( ( [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0,
                                                              hdcttd.DonViTinh) = 3 )
                                  OR ( hdcttd.DonViTinh = 'CPV' )
                                ) --Đơn vị của hình thức CPM
                            AND [dbo].[ThucChay_CheckSanPhamBoxAppSelfServing](hdcttd.DmSanPhamREF,
                                                              ISNULL(hdcttd.TenViTri,
                                                              '')) = 0
                            AND ( @pSoHopDong IS NULL
                                  OR hd.SoHopDong = @pSoHopDong
                                )
							AND hdcttd.DmSanPhamREF = @pDmSanPhamREF
                    ORDER BY hd.SoHopDong	
		
                OPEN Record_Cursor

		-- Perform the first fetch.
                FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong,
                    @DmSanPhamREF, @HopDongChiTietID
			
                WHILE @@FETCH_STATUS = 0
                    BEGIN
				--UPDATE GIA TRI THAY DOI CUA THUCCHAYDATINH = 0
                        PRINT @SoHopDong
                        UPDATE  ThucChayDaTinh
                        SET     GiaTriThayDoi = 0
                        WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                AND HopDongID = @HopDongREF
                                AND SoHopDong = @SoHopDong
                                AND HopDongChiTietREF = @HopDongChiTietID
                                AND DmSanPhamREF = @pDmSanPhamREF
				
                        SET @SoLuongThucChayBF = ( SELECT   SUM(ThucChayDaTinh.SoLuongThucChay)
                                                   FROM     ThucChayDaTinh
                                                   WHERE    CONVERT(DATE, NgayThucHien) < @NgayThucHien
                                                            AND HopDongID = @HopDongREF
                                                            AND HopDongChiTietREF = @HopDongChiTietID
                                                            AND DmSanPhamREF = @pDmSanPhamREF
                                                            AND NOT ( DmHinhThucQuangCao IN (
                                                              13, 42 )
                                                              OR DmLoaiBannerREF = 18
                                                              )--Khong update gia tri thay doi cho HTQC Mua Ngoai 
                                                 )	
                        SET @count_HDCT = ( SELECT  COUNT(hdct.HopDongChiTietID)
                                            FROM    HopDongChiTiet hdct
                                            WHERE   hdct.HopDongChiTietID = @HopDongChiTietID
                                                    AND hdct.DeletedStatus = 0
                                                    AND NOT ( hdct.DmLoaiREF IN (
                                                              13, 42 )
                                                              OR hdct.DmLoaiBannerREF = 18
                                                            )--Khong update gia tri thay doi cho HTQC Mua Ngoai 
                                          )	
                        IF ( @SoLuongThucChayBF > 0 )
                            BEGIN
                                IF ( @count_HDCT > 0 )
					--CHECK VA UPDATE NEU HD CT CO THAY DOI THONG TIN VE GIA, SL, CK
                                    EXEC sp_TC_CheckHopDongCoThayDoi_CPM_BySanPham @HopDongREF,
                                        @SoHopDong, @DmSanPhamREF,
                                        @HopDongChiTietID, @NgayThucHien
                                ELSE
                                    EXEC sp_TC_CheckHopDongXoaPhanBo_CPM_BySanPham @HopDongREF,
                                        @SoHopDong, @DmSanPhamREF,
                                        @HopDongChiTietID, @NgayThucHien	
                            END
					
                        FETCH NEXT FROM Record_Cursor INTO @HopDongREF,
                            @SoHopDong, @DmSanPhamREF, @HopDongChiTietID
                    END
                CLOSE Record_Cursor
                DEALLOCATE Record_Cursor
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
            END
        SELECT  2
    END

--EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPM] '2014-04-29', '2014-04-29'

```
