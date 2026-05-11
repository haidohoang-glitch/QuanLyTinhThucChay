# Stored Procedure: `sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_DonViBai_Admatic_ThucTreo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-23 11:33:18.513000
- **Ngày sửa cuối**: 2023-08-30 14:47:31.993000

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
CREATE  PROCEDURE [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_DonViBai_Admatic_ThucTreo] 
	-- Add the parameters for the stored procedure here
    @StartDate DATETIME ,
    @EndDate DATETIME
AS
    BEGIN
        DECLARE @HopDongREF INT , @SoHopDong NVARCHAR(50) , @HopDongChiTietID INT
        DECLARE @DmSanPhamREF INT
        DECLARE @NgayThucHien DATETIME , @count_HDCT INT , @SoLuongThucChayBF INT         
		, @NgayDanhSoGioiHan DATETIME = '2021-06-10'

		SET @NgayThucHien = @StartDate

        WHILE ( CONVERT(DATE, @NgayThucHien) <= CONVERT(DATE, @EndDate) )
            BEGIN
                --PRINT CONVERT(NVARCHAR(20), @NgayThucHien)
                SET @count_HDCT = 0
                SET @SoLuongThucChayBF = 0

                DECLARE R_U_Cursor_DonViBai_HDTD CURSOR
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
								INNER JOIN 
								(SELECT hdct.* FROM dbo.HopDongChiTiet hdct 
									WHERE hdct.DeletedStatus = 0
									--HAIDH 29052023 THEM SAN PHAM ADPAGE ADMATIC
									AND((hdct.DmSanPhamREF in (305,5312)) OR( hdct.DmSanPhamREF = 598 AND hdct.DmViTriREF = 9198 )) 
									AND UPPER(hdct.DonViTinhREF) IN (7,84)--King size, Sponsor Page, Bai, URL 
									AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18) --loai mua ngoai
									AND hdct.DmLoaiREF = 42 --Admatic
								) hdct on hdcttd.HopDongChiTietREF = hdct.HopDongChiTietID
								WHERE hdcttd.DeletedStatus = 0
								AND hdcttd.DmSanPhamREF IN (305,598,5312)  --King size, Sponsor Page, Bai 
								AND NOT (hdcttd.DmLoaiREF = 13 OR hdcttd.DmLoaiBannerREF = 18) --loai mua ngoai
								AND hdcttd.DmLoaiREF = 42 --Admatic

							 ) hdcttd ON hdtd.HopDongFK = hdcttd.HopDongFK
                    WHERE   1 = 1
					AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan --HAIDH COMMENT THEM VAO VI THEO CACH TINH MOI THEO TUNG THUC TREO VA CHAY 2021-06-07
					AND NOT EXISTS(SELECT top (1) iv.HopDongChiTietREF FROM DmThongTinHopDongBanInventory iv 
							WHERE iv.HopDongChiTietREF = hdcttd.HopDongChiTietREF 
							ORDER BY iv.HopDongChiTietREF
					)
					AND NOT EXISTS (SELECT top (1) tl.HopDongChiTietID FROM GhiNhanThanhLy tl 
							WHERE tl.HopDongChiTietID = hdcttd.HopDongChiTietREF 
							ORDER BY tl.HopDongChiTietID
					)
					
					ORDER BY hd.SoHopDong	
                OPEN R_U_Cursor_DonViBai_HDTD

				-- Perform the first fetch.
                FETCH NEXT FROM R_U_Cursor_DonViBai_HDTD INTO @HopDongREF, @SoHopDong,
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
								AND DmSanPhamREF = @DmSanPhamREF
								AND DmHinhThucQuangCao = 42 --Admatic
								AND DmLoaiBannerREF NOT IN (17,18)
								AND (DonViTinh = N'BÀI' OR DonViTinh = N'URL')
								AND DotChayHopDong = N'CPM_DonViBai'
				
                        SET @SoLuongThucChayBF = ISNULL(( SELECT   SUM(ThucChayDaTinh.SoLuongThucChay + ThucChayDaTinh.SoLuongThayDoi)
                                                   FROM     dbo.ThucChayDaTinh
                                                   WHERE    CONVERT(DATE, NgayThucHien) < @NgayThucHien
                                                            AND HopDongID = @HopDongREF
                                                            AND HopDongChiTietREF = @HopDongChiTietID
                                                            AND DmSanPhamREF = @DmSanPhamREF
															AND DmHinhThucQuangCao = 42 --Admatic
															AND DmLoaiBannerREF NOT IN (17,18)
															--AND DmVitriREF = 9198
															AND (DonViTinh = N'BÀI' OR DonViTinh = N'URL')
															AND DotChayHopDong = N'CPM_DonViBai'
                                                 ),0)
                        SET @count_HDCT = ISNULL(( SELECT  COUNT(hdct.HopDongChiTietID)
                                            FROM    dbo.HopDongChiTiet hdct
                                            WHERE hdct.DeletedStatus = 0
											AND hdct.HopDongChiTietID = @HopDongChiTietID
											AND hdct.DmSanPhamREF = @DmSanPhamREF AND hdct.DonViTinhREF IN (7,84) --King size, Sponsor Page, Bai 
											AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18) --loai mua ngoai
											AND hdct.DmLoaiREF = 42 --Admatic
                                          )	,0)

                        IF ( @SoLuongThucChayBF > 0)
                            BEGIN
                                IF ( @count_HDCT > 0 )
								BEGIN
									--CHECK VA UPDATE NEU HD CT CO THAY DOI THONG TIN VE GIA, SL, CK
          --                          EXEC  [dbo].[sp_TC_CheckHopDongCoThayDoi_DonViBai_ThucTreo] 
										--@HopDongREF = @HopDongREF,
										--@SoHopDong = @SoHopDong,
										--@DmSanPhamREF = @DmSanPhamREF,
										--@HopDongChiTietID = @HopDongChiTietID,
										--@NgayThucHien = @NgayThucHien

										EXEC [dbo].[sp_TC_CheckHopDongCoThayDoi_DonViBai_Admatic_ThucTreo] 
										@HopDongREF = @HopDongREF,
										@SoHopDong = @SoHopDong,
										@DmSanPhamREF = @DmSanPhamREF,
										@HopDongChiTietID = @HopDongChiTietID,
										@NgayThucHien = @NgayThucHien
								END
                                ELSE
								BEGIN
									--CHECK HOPDONGCHITIET BI XOA
									--PRINT 'CHECK XOA PHAN BO'
                                    EXEC [dbo].[sp_TC_CheckHopDongXoaPhanBo_DonViBai_Admatic_ThucTreo]
									   @pHopDongID = @HopDongREF
									  , @pHopDongChiTietID = @HopDongChiTietID
									  , @pDmSanPhamREF = @DmSanPhamREF
									  , @pNgayThucHien = @NgayThucHien
								END	
                            END
					
                        FETCH NEXT FROM R_U_Cursor_DonViBai_HDTD INTO @HopDongREF,
                            @SoHopDong, @DmSanPhamREF, @HopDongChiTietID
                    END
                CLOSE R_U_Cursor_DonViBai_HDTD
                DEALLOCATE R_U_Cursor_DonViBai_HDTD
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
            END
        --SELECT  2
    END



```
