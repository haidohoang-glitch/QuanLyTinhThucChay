# Stored Procedure: `sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhi_SanPhamChinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-12 09:24:41.023000
- **Ngày sửa cuối**: 2024-10-21 10:20:57.170000

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
--EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhi_SanPhamChinh] '2014-08-05','2014-08-05'
CREATE PROCEDURE [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhi_SanPhamChinh]
	-- Add the parameters for the stored procedure here
    @StartDate DATETIME ,
    @EndDate DATETIME ,
    @pSoHopDong NVARCHAR(50)
AS
    BEGIN
        DECLARE @HopDongREF INT ,
            @SoHopDong NVARCHAR(50) ,
            @HopDongChiTietID INT
        DECLARE @SoLuongDotChayHD INT ,
            @ThanhTienHDCT FLOAT
        DECLARE @NgayThucHien DATETIME,
		@NgayDanhSoHieuLuc DATETIME = DATEADD(yyyy,-2,GETDATE())
        SET @NgayThucHien = @StartDate

        WHILE ( CONVERT(DATE, @NgayThucHien) <= CONVERT(DATE, @EndDate) )
            BEGIN
                PRINT CONVERT(NVARCHAR(20), @NgayThucHien)
                DECLARE Record_Cursor_SPChiPhi_2 CURSOR
                FOR
                    SELECT DISTINCT
                            hd.HopDongID ,
                            hd.SoHopDong ,
                            hdct.HopDongChiTietID ,
                            hdct.SoLuong ,
                            hdct.ThanhTien
                    FROM    dbo.HopDongThayDoi hdtd
                            INNER JOIN dbo.HopDong hd ON hdtd.HopDongFK = hd.HopDongID
                            INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongFK = hdtd.HopDongFK
                    WHERE   CONVERT(DATE, hdtd.NgayThayDoi) = @NgayThucHien
                            AND hdct.DmSanPhamREF IN ( 140, 228, 549, 564, 375,
                                                       231, 238, 337, 531, 370,
                                                       339, 342, 381, 821,735 )
                            AND hdct.DmLoaiBannerREF = 17 --Chi phi san pham chinh
                            AND hd.TrangThaiHopDong <> 3
							AND hd.NgayDanhSoHopDong >= @NgayDanhSoHieuLuc
							AND (@pSoHopDong IS NULL OR hd.SoHopDong = @pSoHopDong)

                OPEN Record_Cursor_SPChiPhi_2

		-- Perform the first fetch.
                FETCH NEXT FROM Record_Cursor_SPChiPhi_2 INTO @HopDongREF, @SoHopDong,
                    @HopDongChiTietID, @SoLuongDotChayHD, @ThanhTienHDCT
			
                WHILE @@FETCH_STATUS = 0
                    BEGIN
				--UPDATE GIA TRI THAY DOI CUA THUCCHAYDATINH = 0
                        UPDATE  dbo.ThucChayDaTinh
                        SET     GiaTriThayDoi = 0
                        WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                AND HopDongID = @HopDongREF
                                AND SoHopDong = @SoHopDong
                                AND HopDongChiTietREF = @HopDongChiTietID
                                AND DmSanPhamREF IN ( 140, 228, 549, 564, 375,
                                                      231, 238, 337, 531, 370,
                                                      339, 342, 381, 821,735 )
                                AND DmLoaiBannerREF = 17 --Chi phi san pham chinh
				--CHECK VA UPDATE NEU HD CT CO THAY DOI THONG TIN VE GIA, SL, CK
				
                        EXEC dbo.sp_TC_CheckHopDongCoThayDoi_ChiPhi_SanPhamChinh @HopDongREF,
                            @SoHopDong, @HopDongChiTietID, @NgayThucHien
                        FETCH NEXT FROM Record_Cursor_SPChiPhi_2 INTO @HopDongREF,
                            @SoHopDong, @HopDongChiTietID, @SoLuongDotChayHD,
                            @ThanhTienHDCT
                    END
                CLOSE Record_Cursor_SPChiPhi_2
                DEALLOCATE Record_Cursor_SPChiPhi_2
                EXEC dbo.[sp_TC_CheckThucTreoThayDoi_ChiPhiKhac] @NgayThucHien,
                    '2013-01-01' 
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
            END
        SELECT  2
    END

	

--endregion

```
