# Stored Procedure: `sp_TC_ThucChayDaTinh_CheckThucTreo_GTTD_Native_Ads`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-08 15:57:25.573000
- **Ngày sửa cuối**: 2021-06-14 15:45:32.303000

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
-- Description:	<Description,,> CHECK KHI TH THUC TREO BI XOA, VA THUC TREO BI TREO CHAM VA CO PHAT SINH THUC CHAY TRUOC DO CHUA DC TINH
-- =============================================
CREATE  PROCEDURE [dbo].[sp_TC_ThucChayDaTinh_CheckThucTreo_GTTD_Native_Ads] 
	-- Add the parameters for the stored procedure here
    @StartDate DATETIME ,
    @EndDate DATETIME
AS
    BEGIN
        DECLARE @HopDongREF INT , @SoHopDong NVARCHAR(50) , @HopDongChiTietREF INT
        DECLARE @DmSanPhamREF INT, @DmBannerREF INT, @DeletedStatus SMALLINT
        DECLARE @NgayThucHien DATETIME , @count_HDCT INT , @SoLuongThucChayBF INT, @GhiChuTD NVARCHAR(1000) = ''  
		DECLARE @Table_thuctreo TABLE(HopDongREF INT, HopDongChiTietREF INT
									, DmSanPhamREF INT
									, DmBannerREF INT, DeletedStatus SMALLINT
									, TYPE_PROCESS int --1 chi rieng banner ung voi hdct, 2 toan bo san pham ung voi hopdong
									)

		SET @NgayThucHien = CONVERT(DATE,@StartDate)

        WHILE ( CONVERT(DATE, @NgayThucHien) <= CONVERT(DATE, @EndDate) )
            BEGIN
                --PRINT CONVERT(NVARCHAR(20), @NgayThucHien)
                SET @count_HDCT = 0
                SET @SoLuongThucChayBF = 0
				INSERT INTO @Table_thuctreo
				SELECT DISTINCT tt.HopDongREF, tt.HopDongChiTietREF
					, tt.DmSanPhamREF, tt.DmBannerREF, tt.DeletedStatus, 0 AS TypeProcess FROM 
					(
						SELECT * FROM dbo.ThucChayHopDongChiTiet tt
						WHERE tt.DmSanPhamREF in (821, 5133)
						AND tt.DmHinhThucQuangCaoREF <> 42
						AND CONVERT(DATE,tt.LastModifiedAt) = @NgayThucHien 
					)tt
					INNER JOIN  
					(	SELECT * FROM dbo.HopDong hd WHERE 1=1 
						AND hd.TrangThaiHopDong <> 3
						AND hd.DeletedStatus = 0
					)hd ON hd.HopDongID = tt.HopDongREF 
					INNER JOIN
					(
						SELECT hdct.* FROM dbo.HopDongChiTiet hdct
						WHERE 1=1 AND hdct.DmSanPhamREF IN (821, 5133)
						AND NOT ( hdct.DmLoaiBannerREF IN (17,18) OR hdct.DmLoaiREF IN (13,42))
					) hdct ON tt.HopDongChiTietREF = hdct.HopDongChiTietID
					WHERE   1 = 1
					AND NOT EXISTS(SELECT top (1) iv.HopDongChiTietREF FROM DmThongTinHopDongBanInventory iv 
							WHERE iv.HopDongChiTietREF = tt.HopDongChiTietREF 
							ORDER BY iv.HopDongChiTietREF
					)
					AND NOT EXISTS (SELECT top (1) tl.HopDongChiTietID FROM GhiNhanThanhLy tl 
							WHERE tl.HopDongChiTietID = tt.HopDongChiTietREF 
							ORDER BY tl.HopDongChiTietID
					)--tuyetnta bổ sung loại những hợp đồng thanh lý ghi nhận tay khi tính theo giá làm tròn xuống
					--ORDER BY hd.SoHopDong	

                DECLARE R_U_Cursor_NativeAds_TTTD CURSOR
                FOR
                    SELECT tt.HopDongREF, tt.HopDongChiTietREF, tt.DmSanPhamREF
					, tt.DmBannerREF, tt.DeletedStatus  
					FROM @Table_thuctreo tt
                OPEN R_U_Cursor_NativeAds_TTTD

				-- Perform the first fetch.
                FETCH NEXT FROM R_U_Cursor_NativeAds_TTTD INTO @HopDongREF, @HopDongChiTietREF,
                    @DmSanPhamREF, @DmBannerREF, @DeletedStatus
			
                WHILE @@FETCH_STATUS = 0
                    BEGIN
						DECLARE @MinNgayThucHien DATETIME, @MaxNgayThucHien DATETIME

						SET @SoHopDong = ISNULL((SELECT TOP (1) SoHopDong FROM dbo.HopDong WHERE HopDongID = @HopDongREF ORDER BY HopDongID),'')
						SET @GhiChuTD = N''
						--THUC HIEN INSERT VA CAP NHAP TI LE BANNER
						--CAP NHAT THONG TIN BANNER NATIVE ADS
						EXEC [ThucChay_Insert_And_Update_HopDongChiTietAndBanner_Native_Ads] @NgayThucHien = @NgayThucHien
						EXEC [dbo].ThucChay_UpdateHopDongChiTietAndBanner_Native_Ads_NgayThucHien @NgayThucHien = @NgayThucHien

						--PRINT @SoHopDong
						--NEU THUC TREO BI XOA VI LIEN QUAN DEN NGHIEP VU CHUYEN BANNER TU HDCT NAY -> HDCT KHAC
						IF(@DeletedStatus = 1)
						BEGIN
							--PRINT 'THUC TREO BI XOA'
							SET @GhiChuTD = N'Thuc treo huy BannerID:' + Convert(nvarchar(100),@DmBannerREF) 
							--NEU THUC TREO CO PHAT SINH GIA TRI THUC CHAY
							IF(EXISTS(SELECT TOP (1) tcdt.HopDongChiTietREF, tcdt.DmBannerREF FROM dbo.ThucChayDaTinh tcdt
								WHERE tcdt.HopDongID = @HopDongREF
								AND tcdt.HopDongChiTietREF = @HopDongChiTietREF
								AND tcdt.DmSanPhamREF = @DmSanPhamREF
								AND tcdt.DmBannerREF = @DmBannerREF
								AND tcdt.NgayThucHien <= @NgayThucHien
								GROUP BY tcdt.HopDongChiTietREF, tcdt.DmBannerREF HAVING SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) <> 0
								OR SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) <> 0)
							)
							BEGIN
								--CHECK TYPE PROCESS 
								IF(NOT EXISTS(SELECT top (1) tr.HopDongREF 
										FROM @Table_thuctreo tr 
										WHERE tr.HopDongREF = @HopDongREF
										AND tr.DmSanPhamREF = @DmSanPhamREF
										AND tr.TYPE_PROCESS = 2 ORDER BY tr.HopDongREF)
									)
									BEGIN
										EXEC [dbo].[ThucChay_DoiTruVaTinhLai_CPM_Native_Ads_GhiChu] 
										@pSoHopDong = @SoHopDong,
										@pDmSanPhamREF = @DmSanPhamREF,
										@pStartDate = @MinNgayThucHien,
										@pEndDate = @MaxNgayThucHien,
										@pNgayGhiNhanThucChay = @NgayThucHien,
										@GhiChu	= @GhiChuTD
										--UPDATE TYPE_PROCESS
										UPDATE tt
										SET tt.TYPE_PROCESS = 2
										FROM @Table_thuctreo tt
										WHERE tt.HopDongREF = @HopDongREF
										AND tt.DmSanPhamREF = @DmSanPhamREF
									END
							END
						END
						--TH CHECK NEU THUC TREO DA PHAT SINH THUC CHAY NHUNG TREO CHAM CHUA DC TINH
						ELSE
						BEGIN
							--NEU KO CO PHAT SINH THUC CHAY VOI BANNER
							IF(NOT EXISTS(SELECT TOP (1) tcdt.HopDongChiTietREF, tcdt.DmBannerREF FROM dbo.ThucChayDaTinh tcdt
								WHERE tcdt.HopDongID = @HopDongREF
								AND tcdt.HopDongChiTietREF = @HopDongChiTietREF
								AND tcdt.DmSanPhamREF = @DmSanPhamREF
								AND tcdt.DmBannerREF = @DmBannerREF
								AND tcdt.NgayThucHien <= @NgayThucHien
								GROUP BY tcdt.HopDongChiTietREF, tcdt.DmBannerREF HAVING SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) <> 0
								OR SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) <> 0)
							)
							BEGIN
								--NEU DA TON TAI THUC CHAY VOI BANNER NAY TRUOC NGAYTHUCHIEN
								IF(EXISTS(SELECT TOP 1 [SoHopDong]
										FROM dbo.ThucChay_Native_Ads
										WHERE CONVERT(DATE,NgayThucHien) < CONVERT(DATE,@NgayThucHien)
										AND [DmWebsiteID] = @DmBannerREF
										AND SoHopDong = @SoHopDong
										AND DmSanPhamREF = @DmSanPhamREF
										AND (ThanhTienThucChaySauCK <> 0 OR ThanhTienThucChayKM <> 0)
								))
								BEGIN
										SET @GhiChuTD = N'Thuc treo bi treo cham BannerID:' + Convert(nvarchar(100),@DmBannerREF)
										SELECT @MinNgayThucHien = MIN(NgayThucHien)
										, @MaxNgayThucHien = MAX(NgayThucHien)
										FROM dbo.ThucChay_Native_Ads
										WHERE CONVERT(DATE,NgayThucHien) <= CONVERT(DATE,@NgayThucHien)
										AND SoHopDong = @SoHopDong
										AND DmSanPhamREF = @DmSanPhamREF

										--CHECK TYPE_PROCESS
										IF(NOT EXISTS(SELECT top (1) tr.HopDongREF 
										FROM @Table_thuctreo tr 
										WHERE tr.HopDongREF = @HopDongREF
										AND tr.DmSanPhamREF = @DmSanPhamREF
										AND tr.TYPE_PROCESS = 2 ORDER BY tr.HopDongREF)
										)
										BEGIN
											--THUC HIEN TINH TIEP VOI BANNER TREO
											EXEC [dbo].[ThucChay_ExcInsertThucChayDaTinh_Native_Ads_ByBannerAndHopDongID] 
											@StartDate = @MinNgayThucHien,
											@EndDate = @NgayThucHien,
											@NgayGhiNhanThucChay = @NgayThucHien,
											@HopDongID = @HopDongREF,
											@DmBannerID = @DmBannerREF,
											@GhiChu = @GhiChuTD

											--UPDATE TRANG THAI TYPE_PROCESS
											UPDATE tt
											SET tt.TYPE_PROCESS = 1
											FROM @Table_thuctreo tt
											WHERE tt.HopDongREF = @HopDongREF
											AND tt.HopDongChiTietREF = @HopDongChiTietREF
											AND tt.DmBannerREF = @DmBannerREF
											AND tt.DmSanPhamREF = @DmSanPhamREF
											AND tt.DeletedStatus = @DeletedStatus
										END
								END
							END

						END
					
                        FETCH NEXT FROM R_U_Cursor_NativeAds_TTTD INTO @HopDongREF, @HopDongChiTietREF,
							@DmSanPhamREF, @DmBannerREF, @DeletedStatus
                    END
                CLOSE R_U_Cursor_NativeAds_TTTD
                DEALLOCATE R_U_Cursor_NativeAds_TTTD
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
            END
        SELECT  2
    END



```
