# Stored Procedure: `sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_Native_Ads`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-09-26 13:57:06.533000
- **Ngày sửa cuối**: 2024-08-21 10:38:29.820000

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
CREATE  PROCEDURE [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_Native_Ads] 
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

                DECLARE R_U_Cursor_NativeAds_HDTD CURSOR
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
								WHERE 1=1 AND hdcttd.DmSanPhamREF IN (821, 5133)
								AND NOT ( hdcttd.DmLoaiBannerREF IN (17,18) OR hdcttd.DmLoaiREF IN (13,42))
							 ) hdcttd ON hdtd.HopDongFK = hdcttd.HopDongFK
                    WHERE   1 = 1
					AND NOT EXISTS(SELECT top (1) iv.HopDongChiTietREF FROM DmThongTinHopDongBanInventory iv 
							WHERE iv.HopDongChiTietREF = hdcttd.HopDongChiTietREF 
							ORDER BY iv.HopDongChiTietREF
					)
					AND NOT EXISTS (SELECT top (1) tl.HopDongChiTietID FROM GhiNhanThanhLy tl 
							WHERE tl.HopDongChiTietID = hdcttd.HopDongChiTietREF 
							ORDER BY tl.HopDongChiTietID
					)--tuyetnta bổ sung loại những hợp đồng thanh lý ghi nhận tay khi tính theo giá làm tròn xuống
					
					ORDER BY hd.SoHopDong	
                OPEN R_U_Cursor_NativeAds_HDTD

				-- Perform the first fetch.
                FETCH NEXT FROM R_U_Cursor_NativeAds_HDTD INTO @HopDongREF, @SoHopDong,
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
                               	AND DmSanPhamREF IN (821, 5133)
								AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao IN (13,42))
								AND DotChayHopDong <> N'NGAY'

						--HAIDH COMMENT 2024-08-21 THEM THONG TIN SO LUONG THAY DOI VAO @SoLuongThucChayBF
                        SET @SoLuongThucChayBF = ( SELECT   SUM(ThucChayDaTinh.SoLuongThucChay + ThucChayDaTinh.Soluongthaydoi)
                                                   FROM     dbo.ThucChayDaTinh
                                                   WHERE    CONVERT(DATE, NgayThucHien) < @NgayThucHien
                                                            AND HopDongID = @HopDongREF
                                                            AND HopDongChiTietREF = @HopDongChiTietID
                                                           	AND DmSanPhamREF IN (821, 5133)
															AND NOT ( DmLoaiBannerREF IN (17, 18)OR DmHinhThucQuangCao IN (13, 42))
															AND DotChayHopDong <> N'NGAY'
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
                                    EXEC  [dbo].[sp_TC_CheckHopDongCoThayDoi_Native_Ads] 
										@HopDongREF = @HopDongREF,
										@SoHopDong = @SoHopDong,
										@DmSanPhamREF = @DmSanPhamREF,
										@HopDongChiTietID = @HopDongChiTietID,
										@NgayThucHien = @NgayThucHien
									
                                ELSE
									--CHECK HOPDONGCHITIET BI XOA
                                    EXEC [dbo].[sp_TC_CheckHopDongXoaPhanBo_Native_Ads]
									   @pSoHopDong = @SoHopDong
									  , @pHopDongChiTietID = @HopDongChiTietID
									  , @NgayTinh = @NgayThucHien
									
                            END
					
                        FETCH NEXT FROM R_U_Cursor_NativeAds_HDTD INTO @HopDongREF,
                            @SoHopDong, @DmSanPhamREF, @HopDongChiTietID
                    END
                CLOSE R_U_Cursor_NativeAds_HDTD
                DEALLOCATE R_U_Cursor_NativeAds_HDTD
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
            END
        --SELECT  2
    END

--EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPM] '2014-04-29', '2014-04-29'

```
