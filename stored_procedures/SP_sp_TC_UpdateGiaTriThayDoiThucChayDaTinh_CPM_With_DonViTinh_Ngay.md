# Stored Procedure: `sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_CPM_With_DonViTinh_Ngay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-03-01 09:31:10.653000
- **Ngày sửa cuối**: 2020-06-12 14:16:51.867000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_CPM_With_DonViTinh_Ngay] 
	-- Add the parameters for the stored procedure here
    '2020-05-23' ,
   '2020-06-11'
*/
CREATE  PROCEDURE [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_CPM_With_DonViTinh_Ngay] 
	-- Add the parameters for the stored procedure here
    @StartDate DATETIME ,
    @EndDate DATETIME
AS
    BEGIN
        DECLARE @HopDongREF INT ,
            @SoHopDong NVARCHAR(50) ,
            @HopDongChiTietID INT
        DECLARE @DmSanPhamREF INT
        DECLARE @NgayThucHien DATETIME ,
            @count_HDCT INT ,
            @SoLuongThucChayBF INT 
        SET @NgayThucHien = @EndDate

        SET @count_HDCT = 0
        SET @SoLuongThucChayBF = 0
        DECLARE Record_Cursor CURSOR
        FOR
            SELECT DISTINCT
                    hd.HopDongID ,
                    hd.SoHopDong ,
                    hdcttd.HopDongChiTietREF 
            FROM    dbo.HopDong hd
                    INNER JOIN dbo.HopDongThayDoi hdtd ON hd.HopDongID = hdtd.HopDongFK
                                                        AND hd.TrangThaiHopDong <> 3
                    INNER JOIN dbo.HopDongChiTietThayDoi hdcttd ON hdtd.HopDongFK = hdcttd.HopDongFK
                                                        AND hdcttd.DmSanPhamREF IN (
                                                        231, 238, 339,
                                                        240, 370, 598,
                                                        613, 735, 342, 821 )
            WHERE   1 = 1 AND NOT ( hdcttd.DmLoaiREF IN ( 13, 42 ) OR hdcttd.DmLoaiBannerREF = 18)--Khong update gia tri thay doi cho HTQC Mua Ngoai 
                    AND CONVERT(DATE, hdtd.NgayThayDoi) BETWEEN @StartDate AND @EndDate
                    AND ( ( [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0,hdcttd.DonViTinh) = 1 ))--DON VI TINH NGAY CUA SAN PHAM CPM
  					
            ORDER BY hd.SoHopDong	
		
        OPEN Record_Cursor

		-- Perform the first fetch.
        FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong, @HopDongChiTietID
        WHILE @@FETCH_STATUS = 0
            BEGIN
				--UPDATE GIA TRI THAY DOI CUA THUCCHAYDATINH = 0, RESET GIA TRI TRUOC KHI CHECK VA TINH
                --PRINT @SoHopDong
                UPDATE  dbo.ThucChayDaTinh
                SET     GiaTriThayDoi = 0
                WHERE   CONVERT(DATE, NgayThucHien) = @EndDate
                        AND HopDongID = @HopDongREF
                        AND SoHopDong = @SoHopDong
                        AND HopDongChiTietREF = @HopDongChiTietID
						AND DotChayHopDong = N'NGAY'
 			
                SET @SoLuongThucChayBF = ( SELECT   SUM(ThucChayDaTinh.SoLuongThucChay)
                                            FROM     dbo.ThucChayDaTinh
                                            WHERE    CONVERT(DATE, NgayThucHien) < @EndDate
                                                    AND HopDongID = @HopDongREF
                                                    AND HopDongChiTietREF = @HopDongChiTietID
                                                    AND DmSanPhamREF IN (
                                                    231, 238, 339, 240,
                                                    370, 598, 613, 735, 342, 821 )
													AND NOT ( DmHinhThucQuangCao IN ( 13, 42 ) OR DmLoaiBannerREF = 18)--Khong update gia tri thay doi cho HTQC Mua Ngoai 
													AND DotChayHopDong = N'NGAY'
                                            )	
                SET @count_HDCT = ( SELECT  COUNT(hdct.HopDongChiTietID)
                                    FROM    dbo.HopDongChiTiet hdct
                                    WHERE   hdct.HopDongChiTietID = @HopDongChiTietID
                                            AND hdct.DeletedStatus = 0
											AND NOT ( hdct.DmLoaiREF IN ( 13, 42 )OR hdct.DmLoaiBannerREF = 18)--Khong update gia tri thay doi cho HTQC Mua Ngoai 
											AND hdct.DonViTinhREF in (3,4)
                                    )	
                IF ( @SoLuongThucChayBF > 0 )
                    BEGIN
                        IF ( @count_HDCT > 0 )
							--CHECK VA UPDATE NEU HD CT CO THAY DOI THONG TIN VE GIA, SL, CK
							begin
		
                            EXEC [dbo].[sp_TC_CheckHopDongCoThayDoi_CPM_With_DonViTinh_Ngay] 
										@HopDongREF = @HopDongREF,
										@DmSanPhamREF = @DmSanPhamREF,
										@HopDongChiTietID = @HopDongChiTietID,
										@NgayThucHien = @EndDate
							end
                        ELSE--THUC HIEN DOI TRU TOAN BO DO HDCT BI HUY
						begin
						
                            EXEC [dbo].[sp_TC_UpdateGiaTriThayDoi_DoiTruToanBo_CPM_With_DonViTinh_Ngay]
									   @HopDongID = @HopDongREF
									  , @HopDongChiTietID = @HopDongChiTietID
									  , @NgayTinh = @EndDate
							
						end
                    END
					
                FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong, @HopDongChiTietID
            END
        CLOSE Record_Cursor
        DEALLOCATE Record_Cursor
        --SELECT  2
    END

--EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPM] '2014-04-29', '2014-04-29'

```
