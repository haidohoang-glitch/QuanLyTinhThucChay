# Stored Procedure: `sp_ThucChay_CheckTTTD_HopDongOrHopDongChiTietHuy_PR_HDCT`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2019-12-10 15:50:09.353000
- **Ngày sửa cuối**: 2024-10-21 16:23:08.467000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ThoiGianBDTinh` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
-- EXEC [dbo].[sp_TC_TinhGiaTriThayDoi_PR_HDCT]   '2017-10-09','2017-10-09'
--[sp_TC_CheckHopDongOrHopDongChiTietHuy_PR_HDCT]
--[sp_ThucChay_CheckTTTD_HopDongOrHopDongChiTietHuy_PR_HDCT]

CREATE PROCEDURE [dbo].[sp_ThucChay_CheckTTTD_HopDongOrHopDongChiTietHuy_PR_HDCT] 
    @NgayThucHien DATETIME ,
    @ThoiGianBDTinh DATETIME
AS
    BEGIN

		SET @ThoiGianBDTinh = '2019-01-01'
        DECLARE @HopDongREF INT ,@HopDongChiTietREF INT ,@ThucChayHopDongChiTietPRID INT ,@DmHinhThucQuangCaoREF INT ,@DmSanPhamREF INT 
		,@DmNhanHangREF INT ,@DmViTriREF INT ,@SoLuong INT ,@ChietKhau FLOAT ,@KhuyenMai INT ,@DmWebsiteREF INT ,@GiaTien FLOAT 
		,@ThoiGianBatDau DATETIME , @DeletedStatus INT;
        DECLARE @TrangThaiHopDong INT
        DECLARE @DeletedStatusHDCT INT
		DECLARE @NgayDanhSoGioiHan DATETIME = DATEADD(yyyy,-3, GETDATE())
	

        DECLARE Record_Cursor CURSOR
        FOR
            --LAY THONG TIN HOPDONGCHITIET CUA TAT CAC CAC THUC TREO DC NHAP HOAC SUA NGAYTHUCHIEN> THOIGIANBATDAU
	    SELECT DISTINCT
                A.HopDongREF ,
                A.HopDongChiTietREF ,
                A.TrangThaiHopDong ,
                A.DeletedStatusHDCT
        FROM    ( SELECT    tchdctp.HopDongREF ,
                            hdct.HopDongChiTietID HopDongChiTietREF ,
                            hd.TrangThaiHopDong ,
                            hdct.DeletedStatus DeletedStatusHDCT
                  FROM      dbo.ThucChayHopDongChiTietPR tchdctp
                            INNER JOIN (SELECT * FROM dbo.HopDong hd WHERE hd.DeletedStatus = 0) hd ON hd.HopDongID = tchdctp.HopDongREF
                            INNER JOIN 
							(SELECT * FROM dbo.HopDongChiTiet hdct 
								WHERE hdct.DmSanPhamREF in (141,245,250,637,305) --PR
								AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18)
							)hdct ON tchdctp.HopDongChiTietREF = hdct.HopDongChiTietID
                            LEFT JOIN dbo.HopDongThayDoi hdtd ON hd.HopDongID = hdtd.HopDongFK
                  WHERE     tchdctp.ThoiGianBatDau IS NOT NULL 
                            AND ( ( CONVERT(DATE, hd.LastModifiedAt) = @NgayThucHien )
									OR ( CONVERT(DATE, hdct.LastModifiedAt) = @NgayThucHien )
                                )
                            AND CONVERT(DATE, tchdctp.ThoiGianBatDau) >= @ThoiGianBDTinh
                            AND tchdctp.RecordStatus = 1
							AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan ---pp mapping hdct chi ap dung voi hd 2020
                ) A
				
        ORDER BY A.HopDongREF ,
                A.HopDongChiTietREF;
	
        OPEN Record_Cursor;
		-- Perform the first fetch.
        FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @HopDongChiTietREF, @TrangThaiHopDong, @DeletedStatusHDCT
        WHILE @@FETCH_STATUS = 0
            BEGIN
				--HOP DONG HUY
				DECLARE @LoaiHuy NVARCHAR(200), @SoHopDong NVARCHAR(200)
				SET @SoHopDong = (SELECT TOP (1) hd.SoHopDong FROM dbo.HopDong hd WHERE hd.HopDongID = @HopDongREF ORDER BY hd.HopDongID)
				IF (@TrangThaiHopDong = 3)	
				BEGIN
					SET @LoaiHuy = N'SoHopDong: ' + @SoHopDong + N' Hủy'
				    EXEC [dbo].[ThucChay_Insert_GTTD_HopDongHuy_PR_HDCT]
							@HopDongID = @HopDongREF ,
							@HopDongChiTietID = @HopDongChiTietREF,
							@NgaythucHien = @NgayThucHien,
							@LoaiHuy = @LoaiHuy
				END	
				ELSE
				BEGIN
					--HOP DONG CHI TIET HUY
				    IF (@DeletedStatusHDCT = 1)
					BEGIN
						SET @LoaiHuy = N'HopDongChiTiet: ' + CONVERT(NVARCHAR(100),@HopDongChiTietREF) + N' Hủy'
					     EXEC [dbo].[ThucChay_Insert_GTTD_HopDongHuy_PR_HDCT]
							@HopDongID = @HopDongREF ,
							@HopDongChiTietID = @HopDongChiTietREF,
							@NgaythucHien = @NgayThucHien,
							@LoaiHuy = @LoaiHuy
					END
				END		
               FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @HopDongChiTietREF, @TrangThaiHopDong, @DeletedStatusHDCT
            END;
        CLOSE Record_Cursor
        DEALLOCATE Record_Cursor
    END;



```
