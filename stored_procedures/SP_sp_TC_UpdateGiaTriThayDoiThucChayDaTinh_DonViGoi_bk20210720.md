# Stored Procedure: `sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_DonViGoi_bk20210720`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-07-20 15:44:45.120000
- **Ngày sửa cuối**: 2021-07-20 15:44:45.120000

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
CREATE  PROCEDURE [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_DonViGoi_bk20210720] 
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

                DECLARE R_U_Cursor_DonViGoi_HDTD CURSOR
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
								WHERE hdcttd.DonViTinh = N'GÓi' --Don Vi Goi
								AND hdcttd.DmSanPhamREF IN (339, 240, 598, 342, 5056)
								AND NOT (hdcttd.DmLoaiBannerREF = 18 OR hdcttd.DmLoaiREF IN (42,13))
								AND hdcttd.DeletedStatus = 0
							 ) hdcttd ON hdtd.HopDongFK = hdcttd.HopDongFK
                    WHERE   1 = 1
					AND NOT EXISTS(SELECT top (1) iv.HopDongChiTietREF FROM DmThongTinHopDongBanInventory iv 
							WHERE iv.HopDongChiTietREF = hdcttd.HopDongChiTietREF 
							ORDER BY iv.HopDongChiTietREF
					)
					AND NOT EXISTS (SELECT top (1) tl.HopDongChiTietID FROM GhiNhanThanhLy tl 
							WHERE tl.HopDongChiTietID = hdcttd.HopDongChiTietREF 
							ORDER BY tl.HopDongChiTietID
					)
					
					ORDER BY hd.SoHopDong	
                OPEN R_U_Cursor_DonViGoi_HDTD

				-- Perform the first fetch.
                FETCH NEXT FROM R_U_Cursor_DonViGoi_HDTD INTO @HopDongREF, @SoHopDong,
                    @DmSanPhamREF, @HopDongChiTietID
			
                WHILE @@FETCH_STATUS = 0
                    BEGIN
						--PRINT ''
						----UPDATE GIA TRI THAY DOI CUA THUCCHAYDATINH = 0
                        --PRINT @SoHopDong

                        UPDATE  dbo.ThucChayDaTinh
                        SET     GiaTriThayDoi = 0
                        WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                AND HopDongID = @HopDongREF
                                AND SoHopDong = @SoHopDong
                                AND HopDongChiTietREF = @HopDongChiTietID
								AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao IN (13,42))
								AND DmSanPhamREF IN (339, 240, 598, 342, 5056)
								AND DotChayHopDong = N'CPM_DonViGoi'

                        SET @SoLuongThucChayBF = ISNULL(( SELECT   SUM(ThucChayDaTinh.SoLuongThucChay + thucChayDaTinh.SoLuongThayDoi)
                                                   FROM     dbo.ThucChayDaTinh
                                                   WHERE    CONVERT(DATE, NgayThucHien) < @NgayThucHien
                                                            AND HopDongID = @HopDongREF
                                                            AND HopDongChiTietREF = @HopDongChiTietID
															AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao IN (13,42))
															AND DmSanPhamREF IN (339, 240, 598, 342, 5056)
															AND DotChayHopDong = N'CPM_DonViGoi'
                                                 ),0)

                        SET @count_HDCT = ISNULL(( SELECT  COUNT(hdct.HopDongChiTietID)
                                            FROM    dbo.HopDongChiTiet hdct
                                            WHERE hdct.DeletedStatus = 0
											AND hdct.HopDongChiTietID = @HopDongChiTietID
											AND hdct.DonViTinhREF = 10 --Don Vi Goi
											AND hdct.DmSanPhamREF IN (339, 240, 598, 342, 5056)
											AND NOT (hdct.DmLoaiBannerREF = 18 OR hdct.DmLoaiREF IN (42,13))
											AND hdct.DeletedStatus = 0
                                          )	,0)

                        IF ( @SoLuongThucChayBF > 0)
                            BEGIN
                                IF ( @count_HDCT > 0 )
									--CHECK VA UPDATE NEU HD CT CO THAY DOI THONG TIN VE GIA, SL, CK
                                    EXEC  [dbo].[sp_TC_CheckHopDongCoThayDoi_DonViGoi] 
										@HopDongREF = @HopDongREF,
										@SoHopDong = @SoHopDong,
										@DmSanPhamREF = @DmSanPhamREF,
										@HopDongChiTietID = @HopDongChiTietID,
										@NgayThucHien = @NgayThucHien
									
                                ELSE
									--CHECK HOPDONGCHITIET BI XOA
                                    EXEC [dbo].[sp_TC_CheckHopDongXoaPhanBo_DonViGoi]
									   @pHopDongID = @HopDongREF
									  , @pHopDongChiTietID = @HopDongChiTietID
									  , @pDmSanPhamREF = @DmSanPhamREF
									  , @pNgayThucHien = @NgayThucHien
									
                            END
					
                        FETCH NEXT FROM R_U_Cursor_DonViGoi_HDTD INTO @HopDongREF,
                            @SoHopDong, @DmSanPhamREF, @HopDongChiTietID
                    END
                CLOSE R_U_Cursor_DonViGoi_HDTD
                DEALLOCATE R_U_Cursor_DonViGoi_HDTD
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
            END
        --SELECT  2
    END



```
