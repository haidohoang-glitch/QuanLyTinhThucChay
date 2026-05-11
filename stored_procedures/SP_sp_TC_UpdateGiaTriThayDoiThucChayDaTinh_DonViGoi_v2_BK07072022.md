# Stored Procedure: `sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_DonViGoi_v2_BK07072022`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-07-07 14:55:08.363000
- **Ngày sửa cuối**: 2022-07-07 14:55:08.363000

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
exec [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_DonViGoi]  @StartDate = '2021-06-30' , @EndDate = '2021-06-30' 
*/
CREATE  PROCEDURE [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_DonViGoi_v2_BK07072022] 
	-- Add the parameters for the stored procedure here
    @StartDate datetime,
    @EndDate datetime
AS
    BEGIN
        DECLARE @HopDongREF INT , @SoHopDong NVARCHAR(50) , @HopDongChiTietID INT
        DECLARE @DmSanPhamREF INT, @DmBannerREF int, @LoaiThayDoi smallint
        DECLARE @NgayThucHien DATETIME , @count_HDCT INT , @SoLuongThucChayBF INT   , @GhiChu NVARCHAR(1000) = N''
		SET @NgayThucHien = @StartDate
		
		DECLARE @Table_thaydoi_donvigoi TABLE(HopdongID int, SoHopDong Nvarchar(100)
		, DmSanPhamREF int, HopDongChiTietREF int, DmBannerREF int, LoaiThayDoi SMALLINT, RecordStatus smallint)


        WHILE ( CONVERT(DATE, @NgayThucHien) <= CONVERT(DATE, @EndDate) )
            BEGIN
                --PRINT CONVERT(NVARCHAR(20), @NgayThucHien)
                SET @count_HDCT = 0
                SET @SoLuongThucChayBF = 0
					
					INSERT INTO @Table_thaydoi_donvigoi
					(
						HopdongID,
						SoHopDong,
						DmSanPhamREF,
						HopDongChiTietREF,
						DmBannerREF,
						LoaiThayDoi, --1: Thay doi dg,ck,sl, thanhtien hopdongchitiet, 2 HopDongChiTiet huy, 3: thuc treo huy, 4: thay doi gia banner treo
						RecordStatus --0: chua thuc hien xl, 1: da thuc hien xl
					)
					--THAY DOI NOI DUNG HOP DONG
					SELECT tc.HopDongID, tc.SoHopDong
					, tc.DmSanPhamREF
					, tc.HopDongChiTietID as HopDongChiTietREF 
					, 0 DmBannerREF
					, (CASE WHEN ((ISNULL(TC.ThanhTien,0) <> ISNULL(TCL.ThanhTien,0))) 
						OR ((ISNULL(TC.ChietKhau,0) <> ISNULL(TCL.ChietKhau,0)))
						OR ((ISNULL(TC.DonGia,0) <> ISNULL(TCL.DonGia,0))) THEN 1
						WHEN ( tc.DeletedStatus = 1) THEN 2
						ELSE 0
					END) LoaiThayDoi,
					0 RecordStatus
					FROM
					(
						SELECT hd.SoHopDong,hd.HopDongID,hdct.* FROM [dbo].HopDongChiTiet hdct
						INNER JOIN dbo.HopDong hd on hdct.HopDongFK = hd.HopDongID
						WHERE hdct.DonViTinhREF =10 --Don Vi Goi
						AND hdct.DmSanPhamREF IN (339, 240, 598, 342, 5056, 733)---haidh comment them san pham 733 - nhieu sanpham cho donvigoi 2021-10-29)
						AND NOT (hdct.DmLoaiBannerREF = 18 OR hdct.DmLoaiREF IN (42,13))
						AND convert(date,hdct.LastModifiedAt) = @NgayThucHien
					)TC
					OUTER APPLY
					(SELECT  TOP 1 tcl.HopDongChiTietREF, tcl.ThanhTien, tcl.ChietKhau, tcl.DonGia
					FROM  [dbo].HopDongChiTietLog TCL WHERE TCL.HopDongChiTietREF = tc.HopDongChiTietID
					AND convert(date,TCL.LastModifiedAt) < convert(date,tc.LastModifiedAt)
					order by tcl.LastModifiedAt desc
					)TCL
					WHERE (((ISNULL(TC.ThanhTien,0) <> ISNULL(TCL.ThanhTien,0))) 
						OR ((ISNULL(TC.ChietKhau,0) <> ISNULL(TCL.ChietKhau,0)))
						OR ((ISNULL(TC.DonGia,0) <> ISNULL(TCL.DonGia,0)))
						OR ( tc.DeletedStatus = 1)
					)
					AND TCL.HopDongChiTietREF IS NOT NULL

					UNION ALL
                    --THAY DOI THONG TIN THUC TREO
					SELECT  tc.HopDongID, tc.SoHopDong
					, tc.DmSanPhamREF, tc.HopDongChiTietREF
					, tc.DmBannerREF
					, (CASE WHEN (ISNULL(TC.DonGia,0) <> ISNULL(TCL.DonGia,0)) THEN 4
						WHEN  ( tc.DeletedStatus = 1) THEN 3
						ELSE 0
						END
					)LoaiThayDoi,
					0 RecordStatus
					FROM
					(
						SELECT hdct.SoHopDong, hdct.HopDongID, tt.DmSanPhamREF, hdct.HopDongChiTietID as HopDongChiTietREF
						,tt.DmBannerREF, tt.DonGia, tt.ThucChayHopDongChiTietID, tt.LastModifiedAt, tt.DeletedStatus FROM
						(
							SELECT * FROM [dbo].ThucChayHopDongChiTiet hdct
							WHERE 1=1
							AND hdct.DmSanPhamREF IN (339, 240, 598, 342, 5056)
							AND convert(date,hdct.LastModifiedAt) = @NgayThucHien
						)tt
						INNER JOIN 
						(
								SELECT hd.SoHopDong, hd.HopDongID, hdcttd.* FROM dbo.HopDongChiTiet hdcttd 
								INNER JOIN dbo.HopDong hd on hd.HopDongID = hdcttd.HopDongFk
								WHERE hdcttd.DonViTinhREF = 10 --Don Vi Goi
								AND hdcttd.DmSanPhamREF IN (339, 240, 598, 342, 5056, 733)---haidh comment them san pham 733 - nhieu sanpham cho donvigoi 2021-10-29)
								AND NOT (hdcttd.DmLoaiBannerREF = 18 OR hdcttd.DmLoaiREF IN (42,13))
								AND hdcttd.DeletedStatus = 0
						)hdct ON tt.HopDongChiTietREF = hdct.HopDongChiTietID

					)TC
					OUTER APPLY
					(SELECT  TOP 1 tcl.HopDongChiTietREF, tcl.DmBannerREF, tcl.DonGia
					FROM  [dbo].ThucChayHopDongChiTietLog TCL WHERE TCL.HopDongChiTietREF = tc.HopDongChiTietREF
					AND TCL.ThucChayHopDongChiTietID = tc.ThucChayHopDongChiTietID
					AND TCL.DmBannerREF= TCL.DmBannerREF
					AND convert(date,TCL.LastModifiedAt) < convert(date,tc.LastModifiedAt)
					order by tcl.LastModifiedAt desc
					)TCL
					WHERE ((ISNULL(TC.DonGia,0) <> ISNULL(TCL.DonGia,0))
						OR ( tc.DeletedStatus = 1)
					)
					AND TCL.HopDongChiTietREF IS NOT NULL

					--THAY DOI DON GIA HOAC THUC TREO HUY
					--SELECT * FROM @Table_thaydoi_donvigoi

                DECLARE R_U_Cursor_DonViGoi_HDTD CURSOR
                FOR
					SELECT HopdongID, SoHopDong, DmSanPhamREF, HopDongChiTietREF, DmBannerREF, LoaiThayDoi 
					FROM @Table_thaydoi_donvigoi
					ORDER BY LoaiThayDoi ASC, HopDongChiTietREF
						
                OPEN R_U_Cursor_DonViGoi_HDTD

				-- Perform the first fetch.
                FETCH NEXT FROM R_U_Cursor_DonViGoi_HDTD INTO @HopDongREF, @SoHopDong,
                    @DmSanPhamREF, @HopDongChiTietID,  @DmBannerREF, @LoaiThayDoi
			
                WHILE @@FETCH_STATUS = 0
                    BEGIN
						--PRINT @LoaiThayDoi
						DECLARE @RecordStatus SMALLINT = 0
						DECLARE @MinNgayThucChay DATETIME

						SET @GhiChu = N' TH:' + CONVERT(NVARCHAR(50),@LoaiThayDoi)

	                    UPDATE  dbo.ThucChayDaTinh
                        SET     GiaTriThayDoi = 0
                        WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                AND HopDongID = @HopDongREF
                                AND SoHopDong = @SoHopDong
                                AND HopDongChiTietREF = @HopDongChiTietID
								AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao IN (13,42))
								AND DmSanPhamREF IN (339, 240, 598, 342, 5056)
								AND DotChayHopDong = N'CPM_DonViGoi'

						SET @RecordStatus = (SELECT TOP (1) t.RecordStatus FROM @Table_thaydoi_donvigoi t
												WHERE t.HopdongID = @HopDongREF
												AND t.HopDongChiTietREF = @HopDongChiTietID
												AND t.DmSanPhamREF = @DmSanPhamREF
												AND t.DmBannerREF = @DmBannerREF
												AND t.LoaiThayDoi = @LoaiThayDoi
												ORDER BY t.HopDongChiTietREF)
						--TH 1: THAY DOI DON GIA/SL/CK/THANHTIEN HOPDONGCHITIET
						IF((@LoaiThayDoi = 1) AND (@RecordStatus = 0))
						BEGIN
							--PRINT 'loai thay doi 1'
							--NEU TON TAI THUC CHAY
							IF(EXISTS(SELECT tcdt.HopDongChiTietREF
								FROM dbo.ThucChayDaTinh tcdt
								WHERE convert(date,tcdt.NgayThucHien) <= @NgayThucHien
								AND tcdt.HopDongID = @HopDongREF
								--AND tcdt.DmSanPhamREF = @DmSanPhamREF
								AND tcdt.HopDongChiTietREF = @HopDongChiTietID
								AND tcdt.DotChayHopDong = N'CPM_DonViGoi'
								GROUP BY tcdt.HopDongChiTietREF HAVING sum(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) <> 0
							))
							BEGIN

								SELECT @MinNgayThucChay = MIN(tc.NgayThucHien)
								FROM dbo.ThucChay tc
								where  tc.SoHopDong = @SoHopDong
								--AND tc.DmSanPhamREF = @DmSanPhamREF

								--TH CO THAY DOI VE GIA TRI, THUC HIEN DOI TRU DI VA TINH LAI
								--EXEC [dbo].[ThucChay_DoiTruVaTinhLai_CPM_DonViGoi_ByThoiGian] 
								--@StartDate = @MinNgayThucChay,
								--@EndDate = @NgayThucHien,
								--@pSoHopDong = @SoHopDong,
								--@pHopDongChiTietREF = @HopDongChiTietID,
								--@pDmSanPhamREF = @DmSanPhamREF,
								--@pNgayGhiNhanThucChay = @NgayThucHien,
								--@GhiChu = @GhiChu

								EXEC [dbo].[ThucChay_DoiTruVaTinhLai_CPM_DonViGoi_ByThoiGian_V2] 
								@StartDate = @MinNgayThucChay,
								@EndDate = @NgayThucHien,
								@pSoHopDong = @SoHopDong,
								@pHopDongChiTietREF = @HopDongChiTietID,
								--@pDmSanPhamREF = @DmSanPhamREF,
								@pNgayGhiNhanThucChay = @NgayThucHien,
								@GhiChu = @GhiChu
								
								--CAP NHAP TRANG THAI DA TINH LAI CHO HopDongChiTiet
								UPDATE tt 
								SET tt.RecordStatus = 1
								FROM @Table_thaydoi_donvigoi tt
								WHERE tt.HopdongID = @HopDongREF
								AND tt.HopDongChiTietREF = @HopDongChiTietID
                            END                                
						END
						ELSE
						BEGIN
							--TH2: HopDongChiTiet Huy
							DECLARE @GhiChuDoiTru NVARCHAR(1000) = N'Đối trừ toàn bộ do hopdongchitiet huy: ' + CONVERT(NVARCHAR(50), @HopDongChiTietID) + @GhiChu
							IF(@LoaiThayDoi = 2) AND (@RecordStatus = 0)
							BEGIN
								--PRINT 'loai thay doi 2'
								--EXEC [dbo].[ThucChay_Insert_GTTD_DoiTruGiam_ThucChayDaTinh_CPM_DonViGoi_ThoiGian] 
								--@NgayThucHien = @NgayThucHien,
								--@HopDongID = @HopDongREF,
								--@HopDongChiTietREF = @HopDongChiTietID,
								--@DmSanPhamREF = @DmSanPhamREF,
								--@GhiChu = @GhiChuDoiTru
								EXEC [dbo].[ThucChay_Insert_GTTD_DoiTruGiam_ThucChayDaTinh_CPM_DonViGoi_ThoiGian_V2] 
								@NgayThucHien = @NgayThucHien,
								@HopDongID = @HopDongREF,
								@HopDongChiTietREF = @HopDongChiTietID,
								--@DmSanPhamREF = @DmSanPhamREF,
								@GhiChu = @GhiChuDoiTru

								--CAP NHAP TRANG THAI DA TINH LAI CHO HopDongChiTiet
								UPDATE tt 
								SET tt.RecordStatus = 1
								FROM @Table_thaydoi_donvigoi tt
								WHERE tt.HopdongID = @HopDongREF
								AND tt.HopDongChiTietREF = @HopDongChiTietID
							END
							ELSE
							BEGIN
								--TH3: thuc treo huy
								IF(@LoaiThayDoi = 3) AND (@RecordStatus = 0) 
								BEGIN
									--PRINT 'loai thay doi 3'
									-- CO PHAT SINH THUC CHAY VOI BANNER
									IF(EXISTS(SELECT tcdt.HopDongChiTietREF
										FROM dbo.ThucChayDaTinh tcdt
										WHERE convert(date,tcdt.NgayThucHien) <= @NgayThucHien
										AND tcdt.HopDongID = @HopDongREF
										AND tcdt.DmSanPhamREF = @DmSanPhamREF
										AND tcdt.HopDongChiTietREF = @HopDongChiTietID
										AND tcdt.DotChayHopDong = N'CPM_DonViGoi'
										AND tcdt.DmBannerREF = @DmBannerREF
										GROUP BY tcdt.HopDongChiTietREF HAVING sum(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) <> 0
									))
									BEGIN
										SELECT @MinNgayThucChay = MIN(tc.NgayThucHien)
										FROM dbo.ThucChay tc
										where  tc.SoHopDong = @SoHopDong
										--AND tc.DmSanPhamREF = @DmSanPhamREF

										--TH CO THAY DOI VE GIA TRI, THUC HIEN DOI TRU DI VA TINH LAI
										EXEC [dbo].[ThucChay_DoiTruVaTinhLai_CPM_DonViGoi_ByThoiGian_V2] 
										@StartDate = @MinNgayThucChay,
										@EndDate = @NgayThucHien,
										@pSoHopDong = @SoHopDong,
										@pHopDongChiTietREF = @HopDongChiTietID,
										--@pDmSanPhamREF = @DmSanPhamREF,
										@pNgayGhiNhanThucChay = @NgayThucHien,
										@GhiChu = @GhiChu
								
										--CAP NHAP TRANG THAI DA TINH LAI CHO HopDongChiTiet
										UPDATE tt 
										SET tt.RecordStatus = 1
										FROM @Table_thaydoi_donvigoi tt
										WHERE tt.HopdongID = @HopDongREF
										AND tt.HopDongChiTietREF = @HopDongChiTietID
									END
								END
								ELSE
								BEGIN
								--THAY DOI DONGIA BANNER TREO
									IF(@LoaiThayDoi = 4) AND (@RecordStatus = 0) 
									BEGIN
										--PRINT 'loai thay doi 4'
										IF(EXISTS(SELECT tcdt.HopDongChiTietREF
										FROM dbo.ThucChayDaTinh tcdt
										WHERE convert(date,tcdt.NgayThucHien) <= @NgayThucHien
										AND tcdt.HopDongID = @HopDongREF
										AND tcdt.DmSanPhamREF = @DmSanPhamREF
										AND tcdt.HopDongChiTietREF = @HopDongChiTietID
										AND tcdt.DotChayHopDong = N'CPM_DonViGoi'
										AND tcdt.DmBannerREF = @DmBannerREF
										GROUP BY tcdt.HopDongChiTietREF HAVING (SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) <> 0
										OR SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) <> 0)
										))
										BEGIN
											--PRINT 'th4'
											SELECT @MinNgayThucChay = MIN(tc.NgayThucHien)
											FROM dbo.ThucChay tc
											where  tc.SoHopDong = @SoHopDong
											--AND tc.DmSanPhamREF = @DmSanPhamREF

											--TH CO THAY DOI VE GIA TRI, THUC HIEN DOI TRU DI VA TINH LAI
											--EXEC [dbo].[ThucChay_DoiTruVaTinhLai_CPM_DonViGoi_ByThoiGian] 
											--@StartDate = @MinNgayThucChay,
											--@EndDate = @NgayThucHien,
											--@pSoHopDong = @SoHopDong,
											--@pHopDongChiTietREF = @HopDongChiTietID,
											--@pDmSanPhamREF = @DmSanPhamREF,
											--@pNgayGhiNhanThucChay = @NgayThucHien,
											--@GhiChu = @GhiChu

											EXEC [dbo].[ThucChay_DoiTruVaTinhLai_CPM_DonViGoi_ByThoiGian_V2] 
											@StartDate = @MinNgayThucChay,
											@EndDate = @NgayThucHien,
											@pSoHopDong = @SoHopDong,
											@pHopDongChiTietREF = @HopDongChiTietID,
											--@pDmSanPhamREF = @DmSanPhamREF,
											@pNgayGhiNhanThucChay = @NgayThucHien,
											@GhiChu = @GhiChu
								
											--CAP NHAP TRANG THAI DA TINH LAI CHO HopDongChiTiet
											UPDATE tt 
											SET tt.RecordStatus = 1
											FROM @Table_thaydoi_donvigoi tt
											WHERE tt.HopdongID = @HopDongREF
											AND tt.HopDongChiTietREF = @HopDongChiTietID
										END
									END
								END
							END
						END
       					
                        FETCH NEXT FROM R_U_Cursor_DonViGoi_HDTD INTO @HopDongREF, @SoHopDong,
						@DmSanPhamREF, @HopDongChiTietID,  @DmBannerREF, @LoaiThayDoi
                    END
                CLOSE R_U_Cursor_DonViGoi_HDTD
                DEALLOCATE R_U_Cursor_DonViGoi_HDTD
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
            END
        --SELECT  2
    END


```
