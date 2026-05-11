# Stored Procedure: `sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_CPM`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-19 16:32:17.263000
- **Ngày sửa cuối**: 2024-10-14 16:31:29.013000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@pSoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--[dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_CPM] '2024-10-13','2024-10-13', NULL
CREATE  PROCEDURE [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_CPM] 
	-- Add the parameters for the stored procedure here
    @StartDate DATETIME ,
    @EndDate DATETIME,
	@pSoHopDong NVARCHAR(50)
AS
    BEGIN
        DECLARE @HopDongREF INT ,
            @SoHopDong NVARCHAR(50) ,
            @HopDongChiTietID INT
        DECLARE @DmSanPhamREF INT
        DECLARE @NgayThucHien DATETIME ,
            @count_HDCT INT ,
            @SoLuongThucChayBF INT 
        SET @NgayThucHien = @StartDate

		--INSERT INTO [dbo].[Log_SP_Call]
  --         ([SP_NAME]
  --         ,[SP_TIME_CALL]
  --         ,[SP_END_TIME_CALL]
  --         ,[NOTE]
		--   , VALUE_INPUT)
  --   VALUES
  --         ('[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_CPM]'
  --         ,GETDATE()
  --         ,NULL
  --         ,''
		--   , '@StartDate = ' + CONVERT(NVARCHAR(50),@StartDate,103) +
		--     ', @EndDate = ' + CONVERT(NVARCHAR(50),@EndDate,103) +
		--	 ', @pSoHopDong = '+  ISNULL(@pSoHopDong,'')
		--	)

        WHILE ( CONVERT(DATE, @NgayThucHien) <= CONVERT(DATE, @EndDate) )
            BEGIN
               -- PRINT CONVERT(NVARCHAR(20), @NgayThucHien)
                SET @count_HDCT = 0
                SET @SoLuongThucChayBF = 0
                DECLARE Record_Cursor_Root CURSOR
                FOR
                    SELECT DISTINCT
                            hd.HopDongID ,
                            hd.SoHopDong ,
                            hdcttd.DmSanPhamREF ,
                            hdcttd.HopDongChiTietREF 
                    FROM    (SELECT d.HopDongID, d.SoHopDong FROM dbo.HopDong d 
								WHERE d.TrangThaiHopDong <> 3
								AND (@pSoHopDong IS NULL OR d.SoHopDong = @pSoHopDong) 
							) hd
                            INNER JOIN 
							(SELECT td.HopDongThayDoiID, td.HopDongFK, td.NgayThayDoi 
								FROM dbo.HopDongThayDoi td 
								WHERE CONVERT(DATE, td.NgayThayDoi) = @NgayThucHien
							) hdtd ON hd.HopDongID = hdtd.HopDongFK
                            INNER JOIN 
							(SELECT * FROM dbo.HopDongChiTietThayDoi td 
								WHERE 1=1 
								-- AND td.DmSanPhamREF IN ( 231, 238, 339, 240, 370, 598, 613, 735, 5056,5299 ) 
								AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = td.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 2 --Nhom Tinh Branding
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
									))
								 AND NOT ( td.DmLoaiREF IN ( 13, 42 ) OR td.DmLoaiBannerREF = 18 )--Khong update gia tri thay doi cho HTQC Mua Ngoai 
								 AND ( ( [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, td.DonViTinh) = 3 ) OR ( td.DonViTinh = 'CPV' )
								 AND [dbo].[ThucChay_CheckSanPhamBoxAppSelfServing](td.DmSanPhamREF, ISNULL(td.TenViTri, '')) = 0 ) --Đơn vị của hình thức CPM
								 --AND HopDongChiTietREF = 552584
							) hdcttd ON hdtd.HopDongFK = hdcttd.HopDongFK
                    WHERE   1 = 1
                ORDER BY hd.SoHopDong	
		
                OPEN Record_Cursor_Root
                FETCH NEXT FROM Record_Cursor_Root INTO @HopDongREF, @SoHopDong,
                    @DmSanPhamREF, @HopDongChiTietID
			
                WHILE @@FETCH_STATUS = 0
                    BEGIN
						--UPDATE GIA TRI THAY DOI CUA THUCCHAYDATINH = 0
                        --PRINT @SoHopDong
        --                UPDATE  dbo.ThucChayDaTinh
        --                SET     GiaTriThayDoi = 0
        --                WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien
        --                        AND HopDongID = @HopDongREF
        --                        AND SoHopDong = @SoHopDong
        --                        AND HopDongChiTietREF = @HopDongChiTietID
        --                        --AND DmSanPhamREF IN ( 231, 238, 339, 240, 370, 598, 613, 735 , 5056, 5299)
								--AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
								--									WHERE ch.DmSanPhamREF = dbo.ThucChayDaTinh.DmSanPhamREF
								--									AND ch.NhomTinhDoanhSoThucChay = 2 --Nhom Tinh Branding
								--									AND ch.DeletedStatus = 0 ORDER BY ch.ID
								--))
                        SET @SoLuongThucChayBF = ( SELECT   SUM(ThucChayDaTinh.SoLuongThucChay)
                                                   FROM     dbo.ThucChayDaTinh
                                                   WHERE    CONVERT(DATE, NgayThucHien) < @NgayThucHien
                                                            AND HopDongID = @HopDongREF
                                                            AND HopDongChiTietREF = @HopDongChiTietID
                                                            --AND DmSanPhamREF IN (231, 238, 339, 240,370, 598, 613, 735 )
															AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = dbo.ThucChayDaTinh.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 2 --Nhom Tinh Branding
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
															))
															AND NOT ( DmHinhThucQuangCao IN ( 13, 42 )
															OR DmLoaiBannerREF = 18
														)--Khong update gia tri thay doi cho HTQC Mua Ngoai 
                                                 )	
                        SET @count_HDCT = ( SELECT  COUNT(hdct.HopDongChiTietID)
                                            FROM    dbo.HopDongChiTiet hdct
                                            WHERE   hdct.HopDongChiTietID = @HopDongChiTietID
                                                    AND hdct.DeletedStatus = 0
													AND NOT ( hdct.DmLoaiREF IN ( 13, 42 )
															OR hdct.DmLoaiBannerREF = 18
														)--Khong update gia tri thay doi cho HTQC Mua Ngoai 
                                          )	
                        IF ( @SoLuongThucChayBF > 0 )
                            BEGIN
                                IF ( @count_HDCT > 0 )
								BEGIN
								PRINT N'[sp_TC_CheckHopDongCoThayDoi_CPM]'
									--CHECK VA UPDATE NEU HD CT CO THAY DOI THONG TIN VE GIA, SL, CK
                                    EXEC [dbo].[sp_TC_CheckHopDongCoThayDoi_CPM] 
										@HopDongREF = @HopDongREF,
										@SoHopDong = @SoHopDong,
										@DmSanPhamREF = @DmSanPhamREF,
										@HopDongChiTietID = @HopDongChiTietID,
										@NgayThucHien = @NgayThucHien 
								END
                                ELSE
									BEGIN
									PRINT N'[[sp_TC_CheckHopDongXoaPhanBo_CPM]]'
                                    EXEC [dbo].[sp_TC_CheckHopDongXoaPhanBo_CPM] 
										@HopDongREF = @HopDongREF,
										@SoHopDong = @SoHopDong,
										@DmSanPhamREF = @DmSanPhamREF,
										@HopDongChiTietID = @HopDongChiTietID,
										@NgayThucHien = @NgayThucHien 	
									END
                            END
					
                        FETCH NEXT FROM Record_Cursor_Root INTO @HopDongREF,
                            @SoHopDong, @DmSanPhamREF, @HopDongChiTietID
                    END
                CLOSE Record_Cursor_Root
                DEALLOCATE Record_Cursor_Root
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
            END
        --SELECT  2
    END

--EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPM] '2014-04-29', '2014-04-29'

```
