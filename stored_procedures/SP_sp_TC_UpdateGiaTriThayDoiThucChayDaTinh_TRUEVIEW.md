# Stored Procedure: `sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_TRUEVIEW`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-09-24 16:07:42.850000
- **Ngày sửa cuối**: 2023-08-21 17:38:08.767000

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
CREATE  PROCEDURE [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_TRUEVIEW] 
	-- Add the parameters for the stored procedure here
    @StartDate DATETIME ,
    @EndDate DATETIME
AS
    BEGIN
        DECLARE @HopDongREF INT , @SoHopDong NVARCHAR(50) , @HopDongChiTietID INT
        DECLARE @DmSanPhamREF INT
        DECLARE @NgayThucHien DATETIME , @count_HDCT INT , @SoLuongThucChayBF INT         
		SET @NgayThucHien = @StartDate

        WHILE ( CONVERT(DATE, @NgayThucHien) <= CONVERT(DATE, @EndDate) )
            BEGIN
                --PRINT CONVERT(NVARCHAR(20), @NgayThucHien)
                SET @count_HDCT = 0
                SET @SoLuongThucChayBF = 0
                DECLARE Record_Cursor CURSOR
                FOR
                    SELECT DISTINCT hd.HopDongID , hd.SoHopDong ,
                            hdcttd.DmSanPhamREF , hdcttd.HopDongChiTietREF 
                    FROM    dbo.HopDong hd
                            INNER JOIN
							(	SELECT * FROM dbo.HopDongThayDoi hdtd WHERE 1=1 
								AND CONVERT(DATE, hdtd.NgayThayDoi) = @NgayThucHien
							)hdtd ON hd.HopDongID = hdtd.HopDongFK AND hd.TrangThaiHopDong <> 3
                            INNER JOIN
							(
								SELECT hdcttd.* FROM dbo.HopDongChiTietThayDoi hdcttd 
								WHERE hdcttd.DmSanPhamREF IN ( 240,733 ) 
								AND UPPER(hdcttd.DonViTinh) IN ('TRUE VIEW','TRUE REACH')
								AND NOT ( hdcttd.DmLoaiREF IN ( 13, 42 ) OR hdcttd.DmLoaiBannerREF = 18 )--Khong update gia tri thay doi cho HTQC Mua Ngoai 
							 ) hdcttd ON hdtd.HopDongFK = hdcttd.HopDongFK
                    WHERE   1 = 1

                    ORDER BY hd.SoHopDong	
                OPEN Record_Cursor

				-- Perform the first fetch.
                FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong,
                    @DmSanPhamREF, @HopDongChiTietID
			
                WHILE @@FETCH_STATUS = 0
                    BEGIN
						--UPDATE GIA TRI THAY DOI CUA THUCCHAYDATINH = 0
                        --PRINT @SoHopDong
                        UPDATE  dbo.ThucChayDaTinh
                        SET     GiaTriThayDoi = 0
                        WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                AND HopDongID = @HopDongREF
                                AND SoHopDong = @SoHopDong
                                AND HopDongChiTietREF = @HopDongChiTietID
                                AND DmSanPhamREF IN (240 )
								AND DonViTinh IN  ('TRUE VIEW','TRUE REACH')
				
                        SET @SoLuongThucChayBF = ( SELECT   SUM(ThucChayDaTinh.SoLuongThucChay)
                                                   FROM     dbo.ThucChayDaTinh
                                                   WHERE    CONVERT(DATE, NgayThucHien) < @NgayThucHien
                                                            AND HopDongID = @HopDongREF
                                                            AND HopDongChiTietREF = @HopDongChiTietID
                                                            AND DmSanPhamREF IN (240 )
															AND NOT ( DmHinhThucQuangCao IN ( 13, 42 ) OR DmLoaiBannerREF = 18)--Khong update gia tri thay doi cho HTQC Mua Ngoai 
															AND DonViTinh IN ('TRUE VIEW','TRUE REACH')
                                                 )	
                        SET @count_HDCT = ( SELECT  COUNT(hdct.HopDongChiTietID)
                                            FROM    dbo.HopDongChiTiet hdct
                                            WHERE   hdct.HopDongChiTietID = @HopDongChiTietID
                                                    AND hdct.DeletedStatus = 0
													AND NOT ( hdct.DmLoaiREF IN ( 13, 42 ) OR hdct.DmLoaiBannerREF = 18 )--Khong update gia tri thay doi cho HTQC Mua Ngoai 
                                          )	
                        IF ( @SoLuongThucChayBF > 0 )
                            BEGIN
                                IF ( @count_HDCT > 0 )
									--CHECK VA UPDATE NEU HD CT CO THAY DOI THONG TIN VE GIA, SL, CK
                                    EXEC  [dbo].[sp_TC_CheckHopDongCoThayDoi_TRUEVIEW] 
											@HopDongREF = @HopDongREF,
											@SoHopDong = @SoHopDong,
											@DmSanPhamREF = @DmSanPhamREF,
											@HopDongChiTietID = @HopDongChiTietID,
											@NgayThucHien = @NgayThucHien
                                ELSE
									--CHECK HOPDONGCHITIET BI XOA
                                    EXEC [dbo].[sp_TC_CheckHopDongXoaPhanBo_TrueView]
										   @pSoHopDong = @SoHopDong
										  , @pHopDongChiTietID = @HopDongChiTietID
										  , @NgayTinh = @NgayThucHien	
                            END
					
                        FETCH NEXT FROM Record_Cursor INTO @HopDongREF,
                            @SoHopDong, @DmSanPhamREF, @HopDongChiTietID
                    END
                CLOSE Record_Cursor
                DEALLOCATE Record_Cursor
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
            END
        --SELECT  2
    END

--EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPM] '2014-04-29', '2014-04-29'

```
