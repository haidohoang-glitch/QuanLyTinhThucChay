# Stored Procedure: `sp_ThucChayDaTinh_Mobile_UpdateGiaTriThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-23 17:59:02.180000
- **Ngày sửa cuối**: 2024-10-24 10:47:00.620000

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
--EXEC [ThucChayDaTinh_Mobile_UpdateGiaTriThayDoi_v2]  '2016-01-29', '2016-01-29'
CREATE PROCEDURE [dbo].[sp_ThucChayDaTinh_Mobile_UpdateGiaTriThayDoi]
	-- Add the parameters for the stored procedure here
    @StartDate DATETIME ,
    @EndDate DATETIME,
	@pSoHopDong NVARCHAR(50)
AS
    BEGIN
        DECLARE @NgayThucHien DATETIME ,
            @HopDongID INT ,
            @HopDongChiTietID INT ,
            @SoHopDong NVARCHAR(50) ,
            @count_HDCT INT ,
            @BannerType INT ,
            @ProductUnitName NVARCHAR(50) ,
            @DeletedStatus INT ,
            @DmHinhThucQuangCaoREF INT ,
            @DmSanPhamREF INT ,
            @DmNhanHangREF INT 
        DECLARE @NgayDanhSoHopDong DATETIME ,
            @SysNhanVienREF INT ,
            @DmMaHopDongREF INT ,
            @TenDangNhap NVARCHAR(25) ,
            @DmBannerREF INT
        DECLARE @TenKhachHang NVARCHAR(255);
        DECLARE @TrangThaiHopDong INT
        DECLARE @DeletedStatusHDCT INT
        DECLARE @LoaiThayDoi INT 
        DECLARE @CONTENT_LOG NVARCHAR(MAX) = '' ,
            @NGUON_LOG NVARCHAR(MAX) 
        DECLARE @DonGia FLOAT ,
            @ChietKhau FLOAT ,
            @ThanhTien FLOAT,
			@NgayDanhSoGioiHan DATETIME = DATEADD(yyyy,-3,GETDATE()) --HAIDH COMMENT Gioi han check cua cac hop dong danh so tu ngay nay moi check su thay doi
			
				
        SET @NgayThucHien = @StartDate
        WHILE ( CONVERT(DATE, @NgayThucHien) <= CONVERT(DATE, @EndDate) )
            BEGIN
                DECLARE Record_Cursor CURSOR
                FOR
                    SELECT DISTINCT
                            T.SoHopDong ,
                            T.HopDongID ,
                            T.HopDongChiTietID ,
                            --tc.DeletedStatus ,
							0 DeletedStatus,
                            T.NgayDanhSoHopDong ,
                            T.SysNhanVienREF ,
                            T.DmMaHopDongREF ,
                            T.TenDangNhap ,
                            T.TenKhachHang ,
                            T.TrangThaiHopDong ,
                            T.DeletedStatusHDCT ,
                            T.DmHinhThucQuangCaoREF ,
                            T.DmSanPhamREF ,
                            '0' DmNhanHangREF ,
                            0 DmBannerREF ,
                            T.DonGia ,
                            T.ChietKhau ,
                            T.ThanhTien,
							0 BannerType
							--tc.BannerType
                    FROM    --ThucChay_MobileTemp tc
                            --INNER JOIN 
							( SELECT hdct.HopDongChiTietID ,
                                                tchdct.DmBannerREF ,
                                                hd.SoHopDong ,
                                                hd.HopDongID ,
                                                hd.NgayDanhSoHopDong ,
                                                hd.SysNhanVienREF ,
                                                hd.DmMaHopDongREF ,
                                                hd.TenDangNhap ,
                                                hd.TenKhachHang ,
                                                hd.TrangThaiHopDong ,
                                                hdct.DeletedStatus DeletedStatusHDCT ,
                                                hdct.DmLoaiREF DmHinhThucQuangCaoREF ,
                                                hdct.DmSanPhamREF ,
                                                tchdct.DmNhanHangREF ,
                                                hdct.DonGia ,
                                                hdct.ChietKhau ,
                                                hdct.ThanhTien
                                         FROM   dbo.ThucChayHopDongChiTiet tchdct
                                                INNER JOIN dbo.HopDongChiTiet hdct ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
                                                INNER JOIN dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
                                         WHERE  hdct.DmSanPhamREF = 342
                                                AND NOT ( hdct.DmLoaiREF IN ( 13, 42 ) OR hdct.DmLoaiBannerREF = 18 )
												AND hdct.DonViTinhREF NOT IN (3,4,5,6)
                                                AND EXISTS (SELECT  HopDongChiTietREF
															FROM dbo.HopDongChiTietLog
															WHERE HopDongChiTietREF = hdct.HopDongChiTietID 
															AND CONVERT(DATE, ThoiGianLog) = @NgayThucHien )
												AND (@pSoHopDong IS NULL OR hd.SoHopDong = @pSoHopDong)
												AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan
                                       ) T 

                    ORDER BY HopDongChiTietID


                OPEN Record_Cursor

		-- Perform the first fetch.
                FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @HopDongID,
                    @HopDongChiTietID, @DeletedStatus, @NgayDanhSoHopDong,
                    @SysNhanVienREF, @DmMaHopDongREF, @TenDangNhap,
                    @TenKhachHang, @TrangThaiHopDong, @DeletedStatusHDCT,
                    @DmHinhThucQuangCaoREF, @DmSanPhamREF, @DmNhanHangREF,
                    @DmBannerREF, @DonGia, @ChietKhau, @ThanhTien, @BannerType
                WHILE @@FETCH_STATUS = 0
                    BEGIN			
						
					
                        SET @count_HDCT = ( SELECT  COUNT(hdct.HopDongChiTietID)
                                            FROM    dbo.HopDongChiTiet hdct
                                            WHERE   hdct.HopDongChiTietID = @HopDongChiTietID
                                                    AND hdct.DeletedStatus = 0
                                          )		
			
                        IF @count_HDCT > 0
                            BEGIN		
								--XAC DINH THONG TIN HOPDONGCHITIET THAY DOI VA LOG NGUYEN NHAN THAY DOI
                                EXEC dbo.sp_TC_CheckHopDongCoThayDoi_Mobile @HopDongID,
                                    @SoHopDong, 342, @HopDongChiTietID,
                                    @NgayThucHien, @BannerType, @DmBannerREF
                            END
                        ELSE
                            BEGIN
                                EXEC dbo.sp_TC_CheckHopDongXoaPhanBo_Mobile @HopDongID,
                                    @SoHopDong, 342, @HopDongChiTietID,
                                    @NgayThucHien, @BannerType	, @DmBannerREF
				
                            END

					
                        FETCH NEXT FROM Record_Cursor INTO @SoHopDong,
                            @HopDongID, @HopDongChiTietID, @DeletedStatus,
                            @NgayDanhSoHopDong, @SysNhanVienREF,
                            @DmMaHopDongREF, @TenDangNhap, @TenKhachHang,
                            @TrangThaiHopDong, @DeletedStatusHDCT,
                            @DmHinhThucQuangCaoREF, @DmSanPhamREF,
                            @DmNhanHangREF, @DmBannerREF, @DonGia, @ChietKhau,
                            @ThanhTien, @BannerType
                    END
                CLOSE Record_Cursor
                DEALLOCATE Record_Cursor
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
		
		    
            END
	
	
    END

```
