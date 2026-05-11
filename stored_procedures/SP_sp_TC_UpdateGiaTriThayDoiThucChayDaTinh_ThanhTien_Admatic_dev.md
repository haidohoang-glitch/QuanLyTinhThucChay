# Stored Procedure: `sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_ThanhTien_Admatic_dev`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-05-19 15:38:01.677000
- **Ngày sửa cuối**: 2022-12-21 14:26:04.630000

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
CREATE  PROCEDURE [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_ThanhTien_Admatic_dev] 
	-- Add the parameters for the stored procedure here
    @StartDate DATETIME ,
    @EndDate DATETIME
AS
    BEGIN
        DECLARE @HopDongREF INT , @SoHopDong NVARCHAR(50) , @HopDongChiTietID INT
        DECLARE @DmSanPhamREF INT
        DECLARE @NgayThucHien DATETIME , @count_HDCT INT , @SoLuongThucChayBF INT    
		DECLARE @NgayDanhSoGioiHan DATETIME 
		SET @NgayDanhSoGioiHan = '2020-07-20'     
		SET @NgayThucHien = @StartDate

        WHILE ( CONVERT(DATE, @NgayThucHien) <= CONVERT(DATE, @EndDate) )
            BEGIN
                PRINT CONVERT(NVARCHAR(20), @NgayThucHien)
                SET @count_HDCT = 0
                SET @SoLuongThucChayBF = 0

                DECLARE R_U_Cursor_TT_Admatic_HDTD CURSOR
                FOR
                    SELECT DISTINCT hd.HopDongID , hd.SoHopDong ,
                            hdcttd.DmSanPhamREF , hdcttd.HopDongChiTietREF 
                    FROM    dbo.HopDong hd
                            INNER JOIN
							(	SELECT hdtd.* FROM dbo.HopDongThayDoi hdtd 
								INNER JOIN dbo.HopDong hd on hd.HopDongID = hdtd.HopDongFK
								WHERE 1=1 
								AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan --2020-07-20
								AND CONVERT(DATE, hdtd.NgayThayDoi) = @NgayThucHien
								
							)hdtd ON hd.HopDongID = hdtd.HopDongFK AND hd.TrangThaiHopDong <> 3
                            INNER JOIN
							(
								SELECT hdcttd.* FROM dbo.HopDongChiTietThayDoi hdcttd 
								WHERE 1=1 AND hdcttd.DmSanPhamREF IN (231,238,339,240,598,613,370,680,735,821,342,585,5268)
								AND NOT ( hdcttd.DmLoaiBannerREF IN (17,18) OR hdcttd.DmLoaiREF IN (13))
								AND  hdcttd.DmLoaiREF = 42
								AND NOT (EXISTS(SELECT top (1) iv.HopDongChiTietREF 
									FROM dbo.DmThongTinHopDongBanInventory iv
									WHERE hdcttd.HopDongChiTietref = iv.HopDongChiTietREF
									order by iv.HopDongChiTietREF)
								)
							 ) hdcttd ON hdtd.HopDongFK = hdcttd.HopDongFK
                    WHERE   1 = 1

					UNION ALL
					--CHECK HOPDONGCHITIET BI XOA TRONG NGAY
					SELECT DISTINCT hd.HopDongID, hd.SoHopDong, hdct.DmSanPhamREF, hdct.HopDongChiTietID AS HopDongChiTietREF FROM
					(
						SELECT hdct.HopDongChiTietID, hdct.HopDongFK, hdct.DmLoaiREF, hdct.DmSanPhamREF, hdct.DmLoaiBannerREF, hdct.DeletedStatus, hdct.LastModifiedAt 
						FROM dbo.HopDongChiTiet hdct
						WHERE 1=1 
						AND(hdct.DmLoaiREF = 42)
						AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF =18)
						AND hdct.DmSanPhamREF IN (231,238,339,240,598,613,370,680, 733,735,821,342,585,5268)
						AND hdct.DeletedStatus = 1

						AND NOT (EXISTS(SELECT HopDongChiTietREF 
								FROM dbo.DmThongTinHopDongBanInventory 
								WHERE hdct.HopDongChiTietID = HopDongChiTietREF)
						)--HD Ban Inventory
						AND CONVERT(DATE,hdct.LastModifiedAt) = @NgayThucHien
					) hdct INNER JOIN 
					(
						SELECT hd.HopDongID, hd.SoHopDong, hd.TrangThaiHopDong 
						FROM dbo.HopDong hd 
						WHERE hd.TrangThaiHopDong NOT IN (0,3) 
						AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan
					)hd
					ON hdct.HopDongFK = hd.HopDongID

                OPEN R_U_Cursor_TT_Admatic_HDTD

				-- Perform the first fetch.
                FETCH NEXT FROM R_U_Cursor_TT_Admatic_HDTD INTO @HopDongREF, @SoHopDong,
                    @DmSanPhamREF, @HopDongChiTietID
			
                WHILE @@FETCH_STATUS = 0
                    BEGIN
						--UPDATE GIA TRI THAY DOI CUA THUCCHAYDATINH = 0
                        PRINT @SoHopDong
                        UPDATE  dbo.ThucChayDaTinh
                        SET     GiaTriThayDoi = 0
                        WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                AND HopDongID = @HopDongREF
                                AND SoHopDong = @SoHopDong
                                AND HopDongChiTietREF = @HopDongChiTietID
                               --	AND DmSanPhamREF = @DmSanPhamREF --CHO NAY CAN XEM LAI VI NEU ADMATIC CHAY SAN PHAM NHIEU SAN PHAM
								AND DmHinhThucQuangCao = 42
								AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao IN (13))
								AND DotChayHopDong = N'ThanhTien_Admatic'
				
                        SET @SoLuongThucChayBF = ( SELECT   SUM(tcdt.SoLuongThucChay)
                                                   FROM     dbo.ThucChayDaTinh tcdt
                                                   WHERE    CONVERT(DATE, tcdt.NgayThucHien) < @NgayThucHien
                                                            AND tcdt.HopDongID = @HopDongREF
                                                            AND tcdt.HopDongChiTietREF = @HopDongChiTietID
															AND tcdt.DmHinhThucQuangCao = 42
                                                           	--AND DmSanPhamREF = @DmSanPhamREF --CHO NAY CAN XEM LAI VI NEU ADMATIC CHAY SAN PHAM NHIEU SAN PHAM
															AND NOT ( tcdt.DmLoaiBannerREF IN (17, 18)OR tcdt.DmHinhThucQuangCao IN (13))
															AND tcdt.DotChayHopDong <> N'NGAY'
                                                 )	
                        SET @count_HDCT = ( SELECT  COUNT(hdct.HopDongChiTietID)
                                            FROM    dbo.HopDongChiTiet hdct
                                            WHERE   hdct.HopDongChiTietID = @HopDongChiTietID
                                                    AND hdct.DeletedStatus = 0
													AND hdct.DmLoaiREF = 42
													AND NOT ( hdct.DmLoaiREF IN ( 13) OR hdct.DmLoaiBannerREF = 18 )--Khong update gia tri thay doi cho HTQC Mua Ngoai 
                                          )	
                        IF ( @SoLuongThucChayBF > 0 )
                            BEGIN
                                IF ( @count_HDCT > 0 )
								begin
									--CHECK VA UPDATE NEU HD CT CO THAY DOI THONG TIN VE GIA, SL, CK
                                    EXEC  [dbo].[sp_TC_CheckHopDongCoThayDoi_ThanhTien_Admatic] 
										@HopDongREF = @HopDongREF,
										@SoHopDong = @SoHopDong,
										@DmSanPhamREF = @DmSanPhamREF,
										@HopDongChiTietID = @HopDongChiTietID,
										@NgayThucHien = @NgayThucHien
								end
									
                                ELSE
								begin
									--CHECK HOPDONGCHITIET BI XOA
                                    EXEC [dbo].[sp_TC_CheckHopDongXoaPhanBo_ThanhTien_Admatic]
									   @pSoHopDong = @SoHopDong
									  , @pHopDongChiTietID = @HopDongChiTietID
									  , @NgayTinh = @NgayThucHien
								end
									
                            END
					
                        FETCH NEXT FROM R_U_Cursor_TT_Admatic_HDTD INTO @HopDongREF,
                            @SoHopDong, @DmSanPhamREF, @HopDongChiTietID
                    END
                CLOSE R_U_Cursor_TT_Admatic_HDTD
                DEALLOCATE R_U_Cursor_TT_Admatic_HDTD
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
            END
        SELECT  2
    END

```
