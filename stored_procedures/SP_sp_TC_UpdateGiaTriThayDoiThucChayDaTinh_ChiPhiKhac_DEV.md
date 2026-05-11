# Stored Procedure: `sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhiKhac_DEV`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-03 10:48:51.303000
- **Ngày sửa cuối**: 2021-06-03 10:49:40.643000

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
CREATE PROCEDURE [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhiKhac_DEV]
	-- Add the parameters for the stored procedure here
    @StartDate DATETIME ,
    @EndDate DATETIME,
	@pSoHopDong NVARCHAR(50)
AS
    BEGIN
        DECLARE @HopDongREF INT ,
            @SoHopDong NVARCHAR(50) ,
            @HopDongChiTietID INT
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
        	
										AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = tcdt.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
										))	
										AND tcdt.DmWebsiteREF NOT IN ( 285, 307 ) --loai tru phan bo co website GG,FB
                                        AND NOT ( tcdt.DmHinhThucQuangCao = 13
                                                  OR tcdt.DmLoaiBannerREF IN ( 18 )
                                                )
										AND NOT (DmViTriREF in (100093,100478))	--banner của GGFB
                                        AND tcdt.HopDongID NOT IN (
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
                 --                       AND hdct.DmSanPhamREF IN (242, 251, 252, 253, 535, 537, 538, 539, 540--Chi phí sáng tạo
																	--	, 541, 542, 555, 556, 557, 558, 559, 560, 561,586, 629, 635, 563, 631
																	--	, 651, 630, 731, 726, 730, 629, 729, 633, 736, 734, 771, 772,775,792, 805
																	--	, 806,817, 5012, 5075 ,5074 ,5073
																	--	,5072 ,5071 ,5070, 5061
																	--	,5094	--Youtube
																	--	,5095	--Instagram
																	--	,5096	--Chi phí tư vấn - Sáng tạo
																	--	,5097
																	--	,5109
																	--	,5119,5120,5121,5122,5123,5128,5129,5130,5136,550,5141,5142,5143,5149 --bizfly
																	--	,5156,5157,5158,5159,5160,5161,5162,5163,5164,5165
																	--	,5140,5182,5183,5193, 5184 ,5195,5191, 5200, 5201 ,5204 ,774 , 5199, 5214 ,5151 ,5057,5198 
																	--	,550, 5141, 5142, 5143, 5143
																	--	,5160, 5188,5112,5151 ,5212, 5223, 5217,5207
																	--)
										AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
										)) 		
                                        AND hd.TrangThaiHopDong <> 3
										AND NOT (hdct.DmViTriREF in (100093,100478))	--banner của GGFB
										AND NOT (hdct.DmLoaiREF = 42 AND hdct.DmLoaiNenTangREF = 9) --INVENTORY ADMANTIC
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
    									AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
										)) 			
                                        AND hd.TrangThaiHopDong = 3
										AND NOT (DmViTriREF in (100093,100478))	--banner của GGFB
										AND NOT (hdct.DmLoaiREF = 42 AND hdct.DmLoaiNenTangREF = 9) --INVENTORY ADMANTIC
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
