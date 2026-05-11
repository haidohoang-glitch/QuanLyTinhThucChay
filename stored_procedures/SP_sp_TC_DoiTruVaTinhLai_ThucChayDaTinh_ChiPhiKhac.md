# Stored Procedure: `sp_TC_DoiTruVaTinhLai_ThucChayDaTinh_ChiPhiKhac`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2019-05-30 10:13:39.013000
- **Ngày sửa cuối**: 2024-12-03 09:50:27.210000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuThuViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================
/*
exec [dbo].[sp_TC_DoiTruVaTinhLai_ThucChayDaTinh_ChiPhiKhac] '1023639','585886','2020-09-29'
*/
CREATE PROCEDURE [dbo].[sp_TC_DoiTruVaTinhLai_ThucChayDaTinh_ChiPhiKhac]
	-- Add the parameters for the stored procedure here
    @HopDongID INT,
	@HopDongChiTietID INT,
	@NgayThucHien DATETIME 
AS
    BEGIN
	DECLARE @GhiChu_DoiTru NVARCHAR(2000) = '', @ThucChayHopDongChiTietID INT = 0,
	@NgayDanhSoGioiHan DATETIME = '2021-10-01',
	@NgayDanhSoGioiHan_Tiktok DATETIME = '2021-11-01'
	SET @GhiChu_DoiTru = 'Thuc hien doi tru thuc treo chi phi cua hopdongchitietid: ' + CONVERT(NVARCHAR(50),@HopDongChiTietID)

	--PRINT 'tinh doi tru'
	--THUC HIEN DOI TRU TOAN BO
	EXEC [dbo].[sp_TC_DoiTruThucChayDaTinh_ChiPhiKhac]
    @HopDongID = @HopDongID,
	@HopDongChiTietID = @HopDongChiTietID ,
    @NgaythucHien = @NgayThucHien ,
	@GhiChu = @GhiChu_DoiTru

	--PRINT 'End tinh doi tru'

	--THUC HIEN UPDATE Record_Status = 0 CUA THUC TREO
	UPDATE tchdct
	SET tchdct.RecordStatus = 0 
	FROM dbo.ThucChayHopDongChiTiet tchdct
	WHERE tchdct.HopDongChiTietREF = @HopDongChiTietID
	AND tchdct.HopDongREF = @HopDongID
	
	--THUC HIEN TINH LAI TOAN BO THUC TREO CUA HOPDONGCHITIET

    DECLARE Record_Cursor_DTR_TL CURSOR
    FOR
				
		    SELECT  DISTINCT
                    tchdct.ThucChayHopDongChiTietID
            FROM    dbo.ThucChayHopDongChiTiet tchdct
			INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
			INNER JOIN dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
            WHERE hdct.HopDongChiTietID = @HopDongChiTietID
			AND hdct.HopDongFK = @HopDongID
			AND tchdct.RecordStatus = 0
			AND tchdct.TrangThaiTreo = 2 ---=2 da duyet thi moi tinh, =1 trinh duyet, = 3 tu choi
             AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
							))
            AND hdct.DmWebsiteREF NOT IN ( 285, 307 ) --loai tru phan bo co website GG,FB
            AND NOT ( hdct.DmLoaiREF = 13
                        OR hdct.DmLoaiBannerREF IN ( 18 )
                    )
			AND NOT (hdct.DmViTriREF in (100093,100478))
			AND NOT (hdct.DmSanPhamREF = 5184 AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan) --NGAYDANHSO CreatorContent 2021-10-01
			AND NOT ((hdct.DmSanPhamREF = 5188  OR hdct.DmViTriREF = 100774) AND  (hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_Tiktok)) --haidh comment 20211026 TikTok tinh theo pp GGFB
			ORDER BY tchdct.ThucChayHopDongChiTietID


    OPEN Record_Cursor_DTR_TL

	-- Perform the first fetch.
    FETCH NEXT FROM Record_Cursor_DTR_TL INTO @ThucChayHopDongChiTietID
			
    WHILE @@FETCH_STATUS = 0
        BEGIN
						
			DECLARE @KQ INT = 0
			PRINT @ThucChayHopDongChiTietID
			--- TINH LAI GIA TRI
			EXEC [dbo].[sp_TC_Insert_GTTD_ThucChayDaTinh_ChiPhiKhac_TinhLaiThayDoi] @ThucChayHopDongChiTietID, @HopDongChiTietID, @NgayThucHien,  @KQ OUTPUT

			IF @KQ <> 0
			BEGIN
				UPDATE dbo.ThucChayHopDongChiTiet SET RecordStatus = 1
				WHERE ThucChayHopDongChiTietID = @ThucChayHopDongChiTietID
					AND HopDongChiTietREF = @HopDongChiTietID
			END
				FETCH NEXT FROM Record_Cursor_DTR_TL INTO @ThucChayHopDongChiTietID	
        END
    CLOSE Record_Cursor_DTR_TL
    DEALLOCATE Record_Cursor_DTR_TL
              
    SELECT  2
END

	



```
