# Stored Procedure: `sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhiKhac`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-12 09:22:51.410000
- **Ngày sửa cuối**: 2024-10-21 10:16:42.060000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@pSoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuThuViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================
--[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhiKhac] '2016-09-19','2016-09-19'
CREATE PROCEDURE [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhiKhac]
	-- Add the parameters for the stored procedure here
    @StartDate DATETIME ,
    @EndDate DATETIME,
	@pSoHopDong NVARCHAR(50)
AS
    BEGIN
        DECLARE @HopDongREF INT ,
            @SoHopDong NVARCHAR(50) ,
            @HopDongChiTietID INT,
			@NgayDanhSoHieuLuc DATETIME = DATEADD(yyyy,-2,GETDATE()),
			@NgayDanhSoGioiHan DATETIME = '2021-10-01',
			@NgayDanhSoGioiHan_Tiktok DATETIME = '2022-01-01'
        DECLARE @SoLuongDotChayHD INT ,
            @ThanhTienHDCT FLOAT
        DECLARE @NgayThucHien DATETIME
        SET @NgayThucHien = @StartDate

        WHILE ( CONVERT(DATE, @NgayThucHien) <= CONVERT(DATE, @EndDate) )
            BEGIN
                PRINT CONVERT(NVARCHAR(20), @NgayThucHien)
                DECLARE Record_Cursor CURSOR
                FOR
					--CHECK NHUNG HOPDONGCHITIET DA TINH THUC CHAY NHUNG BI XOA TREN HOPDONGCHITIET
                    SELECT DISTINCT  A.HopDongID ,
                            A.SoHopDong ,
                            A.HopDongChiTietREF ,
                            A.SoLuong ,
                            A.ThanhTien
                    FROM    ( 
						SELECT    tcdt.HopDongID ,
                                        tcdt.SoHopDong ,
                                        tcdt.HopDongChiTietREF ,
                                        tcdt.SoLuong ,
                                        tcdt.ThanhTien
                              FROM      dbo.ThucChayDaTinh tcdt
                              WHERE     CONVERT(DATE, tcdt.NgayThucHien) = @NgayThucHien
    									AND tcdt.NgayDanhSoHopDong >= @NgayDanhSoHieuLuc
										AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = tcdt.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
										))	
										AND tcdt.DmWebsiteREF NOT IN ( 285, 307 ) --loai tru phan bo co website GG,FB
                                        AND NOT ( tcdt.DmHinhThucQuangCao = 13
                                                  OR tcdt.DmLoaiBannerREF IN ( 18 )
                                                )
										AND NOT (tcdt.DmSanPhamREF = 5184 AND tcdt.NgayDanhSoHopDong >= @NgayDanhSoGioiHan) --NGAYDANHSO CreatorContent 2021-10-01
										AND NOT ((tcdt.DmSanPhamREF = 5188  OR tcdt.DmViTriREF = 100774) AND  (tcdt.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_Tiktok)) --Haidh comment Tiktok 20211026 tinh pp GGFB
										AND NOT (tcdt.DmViTriREF in (100093,100478))	--banner của GGFB
										AND tcdt.DotChayBooking <> N'HDBAN_INVENTORY'
                                        AND tcdt.HopDongID NOT IN 
										(
											SELECT  hdct.HopDongFK
											FROM    dbo.HopDongChiTiet hdct
											WHERE   hdct.DmSanPhamREF IN ( 306, 423 )
													AND hdct.DeletedStatus <> 1 
													AND NOT EXISTS(select top (1) hdv.HopDongChiTietREF from dbo.DmThongTinHopDongBanInventory hdv 
																	WHERE hdv.HopDongChiTietREF = hdct.HopDongChiTietID 
																	order by hdv.HopDongChiTietREF)
										)

                              UNION ALL
		                      SELECT  DISTINCT
                                        hd.HopDongID ,
                                        hd.SoHopDong ,
                                        hdct.HopDongChiTietID ,
                                        hdct.SoLuong ,
                                        hdct.ThanhTien
                              FROM      dbo.HopDongChiTietLog hdctl
                                        INNER JOIN dbo.HopDong hd ON hdctl.HopDongFK = hd.HopDongID
                                        INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = hdctl.HopDongChiTietREF
                              WHERE     CONVERT(DATE, hdctl.ThoiGianLog) = @NgayThucHien
 										AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
										)) 	
										AND hd.NgayDanhSoHopDong >= @NgayDanhSoHieuLuc	
                                        AND hd.TrangThaiHopDong <> 3
										AND NOT (hdct.DmSanPhamREF = 5184 AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan) --NGAYDANHSO CreatorContent 2021-10-01
										AND NOT ((hdct.DmSanPhamREF = 5188  OR hdct.DmViTriREF = 100774) AND  (hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_Tiktok)) --Haidh comment Tiktok 20211026 tinh pp GGFB
										AND NOT (hdct.DmViTriREF in (100093,100478))	--banner của GGFB
										--AND NOT (hdct.DmLoaiREF = 42 AND hdct.DmLoaiNenTangREF = 9) --INVENTORY ADMANTIC, thay doi ngay 06/07/2022
                                        AND hdct.DmWebsiteREF NOT IN ( 285, 307 ) --loai tru phan bo co website GG,FB
                                        AND NOT ( hdct.DmLoaiREF = 13
                                                  OR hdct.DmLoaiBannerREF IN ( 18 )
                                                )
										AND NOT EXISTS(select top (1) hdv.HopDongChiTietREF from dbo.DmThongTinHopDongBanInventory hdv 
																							WHERE hdv.HopDongChiTietREF = hdct.HopDongChiTietID 
																							order by hdv.HopDongChiTietREF)
							  UNION ALL
							  --CHECK HOPDONG CO THAY DOI
                              SELECT DISTINCT
                                        hd.HopDongID ,
                                        hd.SoHopDong ,
                                        hdct.HopDongChiTietID ,
                                        hdct.SoLuong ,
                                        hdct.ThanhTien
                              FROM      dbo.HopDong hd 
                                        INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongFK = hd.HopDongID
                              WHERE     CONVERT(DATE, hd.LastModifiedAt) = @NgayThucHien
										AND hd.NgayDanhSoHopDong >= @NgayDanhSoHieuLuc	
										AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
										)) 			
                                        AND hd.TrangThaiHopDong = 3
										AND NOT (hdct.DmSanPhamREF = 5184 AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan) --NGAYDANHSO CreatorContent 2021-10-01
										AND NOT ((hdct.DmSanPhamREF = 5188  OR hdct.DmViTriREF = 100774) AND  (hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_Tiktok)) --Haidh comment Tiktok 20211026 tinh pp GGFB
										AND NOT (DmViTriREF in (100093,100478))	--banner của GGFB
										--AND NOT (hdct.DmLoaiREF = 42 AND hdct.DmLoaiNenTangREF = 9) --INVENTORY ADMANTIC, thay doi ngay 06/07/2022
                                        AND hdct.DmWebsiteREF NOT IN ( 285, 307 ) --loai tru phan bo co website GG,FB
                                        AND NOT ( hdct.DmLoaiREF = 13
                                                  OR hdct.DmLoaiBannerREF IN ( 18 )
                                                )
										AND NOT EXISTS(select top (1) hdv.HopDongChiTietREF from dbo.DmThongTinHopDongBanInventory hdv 
																							WHERE hdv.HopDongChiTietREF = hdct.HopDongChiTietID 
																							order by hdv.HopDongChiTietREF)
                            ) A
					WHERE (@pSoHopDong IS NULL OR A.SoHopDong = @pSoHopDong)

                    ORDER BY A.SoHopDong ,
                            A.HopDongChiTietREF
	
		
                OPEN Record_Cursor

				-- Perform the first fetch.
                FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong,
                    @HopDongChiTietID, @SoLuongDotChayHD, @ThanhTienHDCT
			
                WHILE @@FETCH_STATUS = 0
                    BEGIN
						--CHECK VA UPDATE NEU HD CT CO THAY DOI THONG TIN VE GIA, SL, CK
                        EXEC dbo.sp_TC_CheckHopDongCoThayDoi_ChiPhiKhac @HopDongREF,
                            @SoHopDong, @HopDongChiTietID, @NgayThucHien

                        FETCH NEXT FROM Record_Cursor INTO @HopDongREF,
                            @SoHopDong, @HopDongChiTietID, @SoLuongDotChayHD,
                            @ThanhTienHDCT
                    END
                CLOSE Record_Cursor
                DEALLOCATE Record_Cursor

				--tinh gia tri thay doi khi thuc treo bi huy
				EXEC [dbo].[sp_TC_UpdateGTTDThucChayDaTinh_ChiPhiKhac_ThucTreoHuy]  @NgayThucHien, NULL

                EXEC sp_TC_CheckThucTreoThayDoi_ChiPhiKhac @NgayThucHien, '2010-01-01' 

                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
            END
        SELECT  2
    END

	



```
