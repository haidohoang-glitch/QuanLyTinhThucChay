# Stored Procedure: `sp_TC_UpdateGiaTriThayDoi_ThucTreoThayDoi_ThanhTien_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-04 14:17:12.620000
- **Ngày sửa cuối**: 2024-10-07 15:47:02.050000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE  PROCEDURE [dbo].[sp_TC_UpdateGiaTriThayDoi_ThucTreoThayDoi_ThanhTien_Admatic] 
	-- Add the parameters for the stored procedure here
    @NgayThucHien DATETIME 
AS
    BEGIN
        DECLARE @HopDongREF INT , @SoHopDong NVARCHAR(50) , @HopDongChiTietID INT
        DECLARE @DmSanPhamREF INT, @ThucChayHopDongChiTietID INT, @DmBannerREF INT, @DeletedStatus SMALLINT = 0
		DECLARE @NgayDanhSoGioiHan DATETIME 
		DECLARE @ThucTreoThayDoi_ThanhTien_Admatic TABLE(HopDongID INT, SoHopDong NVARCHAR(100), HopDongChiTietID INT,
		ThucChayHopDongChiTietID INT, DmSanPhamID INT, DmBannerID INT)

		SET @NgayDanhSoGioiHan = DATEADD(yyyy,-3,GETDATE()) 

		INSERT INTO @ThucTreoThayDoi_ThanhTien_Admatic
		SELECT DISTINCT hd.HopDongID, hd.SoHopDong, hdct.HopDongChiTietID AS HopDongChiTietREF
		, tc.ThucChayHopDongChiTietID, tc.DmSanPhamREF, tc.DmBannerREF
		FROM
		(SELECT tc.HopDongREF, tc.HopDongChiTietREF, tc.ThucChayHopDongChiTietID, tc.DmSanPhamREF, tc.DmBannerREF FROM dbo.ThucChayHopDongChiTiet tc
			WHERE tc.DmHinhThucQuangCaoREF = 42
			AND NOT (tc.DmHinhThucQuangCaoREF = 13)
			AND tc.DmSanPhamREF IN (231,238,339,240,598,613,370,680, 733,735,821,342,585,5133,5056,5268)
			AND tc.DeletedStatus = 1
			AND CONVERT(DATE,tc.LastModifiedAt) = @NgayThucHien
		)
		tc INNER JOIN
		(
			SELECT hdct.HopDongChiTietID, hdct.HopDongFK, hdct.DmLoaiREF, hdct.DmSanPhamREF, hdct.DmLoaiBannerREF, hdct.DeletedStatus, hdct.LastModifiedAt 
			FROM dbo.HopDongChiTiet hdct
			WHERE 1=1 
			AND(hdct.DmLoaiREF = 42)
			AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF =18)
			AND hdct.DmSanPhamREF IN (231,238,339,240,598,613,370,680, 733,735,821,342,585,5133,5056,5268)
			AND hdct.DeletedStatus = 0
			AND hdct.DonViTinhREF <> 7 --DON VI BAI
			AND NOT (EXISTS(SELECT HopDongChiTietREF 
					FROM dbo.DmThongTinHopDongBanInventory 
					WHERE hdct.HopDongChiTietID = HopDongChiTietREF)
			)--HD Ban Inventory
		) hdct ON tc.HopDongChiTietREF = hdct.HopDongChiTietID
		INNER JOIN 
		(
			SELECT hd.HopDongID, hd.SoHopDong, hd.TrangThaiHopDong 
			FROM dbo.HopDong hd 
			WHERE hd.TrangThaiHopDong NOT IN (0,3) 
			AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan
		)hd
		ON hdct.HopDongFK = hd.HopDongID
        DECLARE R_U_Cursor_TT_Admatic_TTTD CURSOR
        FOR
				
			SELECT t.HopDongID , t.HopDongChiTietID ,
			t.ThucChayHopDongChiTietID , t.DmSanPhamID , t.DmBannerID 
			, 1 AS DeletedStatus
			FROM @ThucTreoThayDoi_ThanhTien_Admatic t	
						
			UNION ALL
			SELECT DISTINCT t.HopDongREF AS HopDongID, t.HopDongChiTietREF AS HopDongChiTietID,
			t.ThucChayHopDongChiTietREF AS ThucChayHopDongChiTietID, t.DmSanPhamREF AS DmSanPhamID
			, t.DmBannerREF AS DmBannerID 
			, t.DeletedStatus
			FROM dbo.ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic t
			INNER JOIN @ThucTreoThayDoi_ThanhTien_Admatic tt on t.DmBannerREF = tt.DmBannerID
			AND t.HopDongREF = tt.HopDongID AND t.DmSanPhamREF = tt.DmSanPhamID
			WHERE 1=1
			AND t.DeletedStatus = 0
			AND NOT EXISTS(
				SELECT tt.HopDongChiTietID, t.HopDongChiTietREF FROM @ThucTreoThayDoi_ThanhTien_Admatic tt
				WHERE tt.DmBannerID = 	t.DmBannerREF
				AND tt.HopDongChiTietID = t.HopDongChiTietREF
				AND tt.HopDongID = t.HopDongREF
				AND tt.DmSanPhamID = t.DmSanPhamREF
			)
			AND t.DmbannerREF NOT LIKE '%,%'
        OPEN R_U_Cursor_TT_Admatic_TTTD

		-- Perform the first fetch.
        FETCH NEXT FROM R_U_Cursor_TT_Admatic_TTTD INTO @HopDongREF, 
            @HopDongChiTietID, @ThucChayHopDongChiTietID, @DmSanPhamREF, @DmBannerREF, @DeletedStatus
			
        WHILE @@FETCH_STATUS = 0
            BEGIN
				--XAC DINH BANNER HUY CO PHAT SINH THUC CHAY KO
				SET @SoHopDong = ISNULL((SELECT TOP (1) hd.SoHopDong FROM dbo.HopDong hd WHERE hd.HopDongID = @HopDongREF ORDER BY hd.HopDongID),'')
                PRINT @SoHopDong
				IF(EXISTS(SELECT tcdt.DmBannerREF FROM dbo.ThucChayDaTinh tcdt
					WHERE tcdt.NgayThucHien <= @NgayThucHien
					AND tcdt.HopDongID = @HopDongREF
					AND tcdt.HopDongChiTietREF = @HopDongChiTietID
					AND tcdt.DmSanPhamREF = @DmSanPhamREF --san pham cua treo
					AND DmHinhThucQuangCao = 42
					AND DmBannerREF = @DmBannerREF
					AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao IN (13))
					AND DotChayHopDong = N'ThanhTien_Admatic'
					GROUP BY tcdt.DmBannerREF HAVING (SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) <> 0 OR SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) <> 0)
				))
				BEGIN
					--THUC HIEN DOI TRU VA TINH LAI
					--XAC DINH THOI GIAN TRA THUC CHAY
					DECLARE @MinNgayThucHien DATETIME
					, @MaxNgayThucHien DATETIME
					, @GhiChu NVARCHAR(500) = N''

					SELECT @MinNgayThucHien = MIN(t.NgayThucHien)
					, @MaxNgayThucHien = MAX(t.NgayThucHien) 
					FROM dbo.[ThucChay_ThanhTien_Admatic] t
					WHERE t.SoHopDong = @SoHopDong
					AND t.DmSanPhamREF = @DmSanPhamREF
					AND t.DmBannerID = @DmBannerREF

					SET @MinNgayThucHien = ISNULL(@MinNgayThucHien,'1900-01-01')
					SET @MaxNgayThucHien = ISNULL(@MaxNgayThucHien,'1900-01-01')
					
					SET @GhiChu = ', Do co banner Huy: ' + convert(nvarchar(100),@DmBannerREF)

					EXEC [dbo].[ThucChay_DoiTruVaTinhLai_ThanhTien_Admatic_TTTD] 
					@pSoHopDong = @SoHopDong,
					@pHopDongChiTietID = @HopDongChiTietID,
					@pDmSanPhamREF = @DmSanPhamREF,
					@pStartDate = @MinNgayThucHien,
					@pEndDate = @NgayThucHien,
					@pNgayGhiNhanThucChay = @NgayThucHien,
					@GhiChu = @GhiChu
					--CAP NHAP GHI CHU THEO TRANG THAI CUA BANNER

				END
			FETCH NEXT FROM R_U_Cursor_TT_Admatic_TTTD INTO @HopDongREF, 
            @HopDongChiTietID, @ThucChayHopDongChiTietID, @DmSanPhamREF, @DmBannerREF, @DeletedStatus
            END
        CLOSE R_U_Cursor_TT_Admatic_TTTD
        DEALLOCATE R_U_Cursor_TT_Admatic_TTTD
        --SELECT  2
    END

```
