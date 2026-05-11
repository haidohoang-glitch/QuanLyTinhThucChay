# Stored Procedure: `ThucChay_CheckThucChayCPDByDate_V1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-03 16:02:09.700000
- **Ngày sửa cuối**: 2019-07-19 11:17:30.717000

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
--EXEC ThucChay_CheckThucChayCPDByDate_V1	@StartDate = '2017-05-31',	@EndDate = '2017-05-31'
CREATE PROCEDURE [dbo].[ThucChay_CheckThucChayCPDByDate_V1]
    @StartDate DATETIME ,
    @EndDate DATETIME
AS
    BEGIN
        DECLARE @Table TABLE
            (
              NgayThucHien DATETIME ,
              HopDongID INT ,
              SoHopDong NVARCHAR(50) ,
              HopDongChiTietID INT ,
              BookingREF INT ,
              ThoiGianBD DATETIME ,
              ThoiGianKT DATETIME ,
              HopDongREF_Thuctreo INT ,
              HopDongChiTietREF_Thuctreo INT ,
              DmBannerID_Thuctreo INT ,
              BookingREF_Thuctreo INT ,
              SoHopDong_sp NVARCHAR(50) ,
              BookingREF_sp NVARCHAR(MAX) ,
              DmBannerREF_sp INT ,
              TTV FLOAT ,
		--SLNgayHD int,
		--SLNgayDotChay int,
		--SLThucChayTest int,		
		--SLThucChay_tcdt int,
		--DonGiaNgay float,
		--ThanhTien float,
		--TienThucChay_Test float,
		--TienThucChay_tcdt float,
		--TienLech float, 
              CheckedStatus INT , 
		--[Status] int,
              NguyenNhan NVARCHAR(MAX) ,
              GhiChuPhanBo NVARCHAR(MAX)
            )
        EXEC [ThucChay_HopDongChiTietAndBannerCPD] @StartDate

        DECLARE @NgayThucHien DATETIME
        SET @NgayThucHien = @StartDate
        DELETE  FROM ThucChay_CheckThucChayCPDDaily
        WHERE   NgayThucHien BETWEEN @StartDate AND @EndDate
        WHILE ( @NgayThucHien <= @EndDate )
            BEGIN
	--//-----------CPD CO DOT CHAY----------------------------------
	-------------DOI CHIEU DATA GIUA HD- SP - THUCTREO ---------------------
                INSERT  INTO @Table
                        SELECT  @NgayThucHien
		-------Thong tin hop dong
                                ,
                                HD.HopDongID ,
                                HD.SoHopDong ,
                                HD.HopDongChiTietID ,
                                HD.BookingREF ,
                                HD.ThoiGianBatDau ,
                                HD.ThoiGianKetThuc ,
                                ThucTreo.HopDongREF ,
                                ThucTreo.HopDongChiTietREF ,
                                ThucTreo.DmBannerID ,
                                ThucTreo.BookingREF ,
                                SP.SoHopDong ,
                                SP.DanhsachDmBookingREF ,
                                SP.DmBannerREF ,
                                SP.TongViewThucChay AS ttv		
		--, 0, 0, 0, 0, 0, 0, 0, 0, 0		 	
		----- Thong tin kiem tra
		--, 1			
                                ,
                                CASE WHEN HD.HopDongID IS NOT NULL
                                          AND ThucTreo.HopDongREF IS NULL
                                          AND SP.SoHopDong IS NULL THEN 2
                                     WHEN HD.HopDongID IS NOT NULL
                                          AND ThucTreo.HopDongREF IS NULL
                                          AND SP.SoHopDong IS NOT NULL THEN 1
                                     WHEN HD.HopDongID IS NOT NULL
                                          AND ThucTreo.HopDongREF IS NOT NULL
                                          AND SP.SoHopDong IS NULL THEN 1
                                     WHEN HD.HopDongID IS NULL
                                          AND ThucTreo.HopDongREF IS NULL
                                          AND SP.SoHopDong IS NOT NULL THEN 1
                                     WHEN HD.HopDongID IS NULL
                                          AND ThucTreo.HopDongREF IS NOT NULL
                                          AND SP.SoHopDong IS NULL THEN 1
                                     WHEN HD.HopDongID IS NULL
                                          AND ThucTreo.HopDongREF IS NOT NULL
                                          AND SP.SoHopDong IS NOT NULL THEN 1
                                     ELSE 0
                                END CheckedStatus ,
                                CASE WHEN HD.HopDongID IS NOT NULL
                                          AND ThucTreo.HopDongREF IS NULL
                                          AND SP.SoHopDong IS NULL
                                     THEN N'Chưa treo - chưa chạy'
                                     WHEN HD.HopDongID IS NOT NULL
                                          AND ThucTreo.HopDongREF IS NULL
                                          AND SP.SoHopDong IS NOT NULL
                                     THEN N'Đang chạy - HĐ có ngày chạy - Không có thực treo'
                                     WHEN HD.HopDongID IS NOT NULL
                                          AND ThucTreo.HopDongREF IS NOT NULL
                                          AND SP.SoHopDong IS NULL
                                     THEN N'Ngừng chạy - HĐ, Thực Treo chưa update'
                                     WHEN HD.HopDongID IS NULL
                                          AND ThucTreo.HopDongREF IS NULL
                                          AND SP.SoHopDong IS NOT NULL
                                     THEN N'Đang chạy - Không có hđ, thực treo'
                                     WHEN HD.HopDongID IS NULL
                                          AND ThucTreo.HopDongREF IS NOT NULL
                                          AND SP.SoHopDong IS NULL
                                     THEN N'Có thực treo - Không có hđ, thực chạy'
                                     WHEN HD.HopDongID IS NULL
                                          AND ThucTreo.HopDongREF IS NOT NULL
                                          AND SP.SoHopDong IS NOT NULL
                                     THEN N'Đang chạy - Đã treo - HĐ không có ngày chạy/ BookingREF giữa treo và đợt chạy sai'
                                     ELSE ''
                                END NguyenNhan ,
                                '' AS GhiChu
                        FROM    ( SELECT DISTINCT
                                            tchdctab.ThucChayHopDongChiTietID ,
                                            tchdctab.HopDongREF ,
                                            tchdctab.HopDongChiTietREF ,
                                            tchdctab.DmBannerID ,
                                            tchdctab.BookingREF
                                  FROM      ThucChayHopDongChiTietAndBannerCPD tchdctab
                                            INNER JOIN HopDongChiTiet hdct ON tchdctab.HopDongChiTietREF = hdct.HopDongChiTietID
                                                              AND hdct.DeletedStatus = 0
                                                              AND tchdctab.DeletedStatus = 0
                                                              AND hdct.DmSanPhamREF IN (
                                                              140, 228, 564,
                                                              549 )
                                                              AND @NgayThucHien BETWEEN tchdctab.ThoiGianBatDau
                                                              AND
                                                              tchdctab.ThoiGianKetThuc
                                ) ThucTreo
                                FULL OUTER JOIN ( SELECT    ptcts.SoHopDong ,
                                                            ptcts.DanhsachDmBookingREF ,
                                                            ptcts.DmBannerREF ,
                                                            ptcts.TongViewThucChay
                                                  FROM      ThucChay ptcts
                                                            INNER JOIN HopDong hd2 ON hd2.SoHopDong = ptcts.SoHopDong
                                                              AND ptcts.TypeProduct IN (
                                                              -2, -3 )
                                                  WHERE     hd2.TrangThaiHopDong <> 3
                                                            AND ptcts.NgayThucHien = @NgayThucHien
                                                ) SP ON ThucTreo.DmBannerID = SP.DmBannerREF
                                FULL OUTER JOIN ( SELECT    HD.HopDongID ,
                                                            HD.SoHopDong ,
                                                            hdct.HopDongChiTietID ,
                                                            hdct.TenSanPham ,
                                                            hdct.DmSanPhamREF ,
                                                            hdct.TenWebsite ,
                                                            hdct.ThanhTien ,
                                                            dchdct.BookingREF ,
                                                            dchdct.ThoiGianBatDau ,
                                                            dchdct.ThoiGianKetThuc ,
                                                            hdct.SoLuong ,
                                                            hdct.DonViTinh
                                                  FROM      HopDong HD
                                                            INNER JOIN HopDongChiTiet hdct ON HD.HopDongID = hdct.HopDongFK
                                                              AND HD.TrangThaiHopDong <> 3
                                                              AND hdct.DeletedStatus = 0
                                                              AND NOT ( hdct.DmLoaiREF = 13
                                                              OR hdct.DmLoaiBannerREF = 18
                                                              )
                                                            LEFT JOIN DotChayHopDongChiTiet dchdct ON hdct.HopDongChiTietID = dchdct.HopDongChiTietREF
                                                              AND hdct.HopDongFK = dchdct.HopDongREF
                                                              AND dchdct.DeletedStatus = 0
                                                  WHERE     @NgayThucHien BETWEEN dchdct.ThoiGianBatDau
                                                              AND
                                                              dchdct.ThoiGianKetThuc
                                                            AND hdct.DmSanPhamREF IN (
                                                            140, 228, 564, 549 )
                                                ) HD ON HD.BookingREF = ThucTreo.BookingREF
                                                        AND ThucTreo.HopDongChiTietREF = HD.HopDongChiTietID 	
	
	--//-----------CPD KHONG DOT CHAY - TMDT ----------------------------------
	-------------DOI CHIEU DATA GIUA HD - THUCTREO ---------------------
                SELECT  * ,
                        ( CASE WHEN HD.HopDongID IS NULL
                                    OR ThucTreo.HopDongREF IS NULL THEN 1
                               ELSE 0
                          END ) AS CheckedStatus ,
                        ( CASE WHEN HD.HopDongID IS NULL
                                    OR ThucTreo.HopDongREF IS NULL THEN 1
                               ELSE 0
                          END ) AS [Status] ,
                        CASE WHEN HD.HopDongID IS NOT NULL
                                  AND ThucTreo.HopDongREF IS NULL
                             THEN N'HĐ có ngày chạy - Chưa treo'
                             WHEN HD.HopDongID IS NULL
                                  AND ThucTreo.HopDongREF IS NOT NULL
                             THEN N'HĐ không có ngày chạy - Có thực treo'
                             ELSE ''
                        END NguyenNhan
                FROM    ( SELECT    HD.HopDongID ,
                                    HD.SoHopDong ,
                                    hdct.HopDongChiTietID ,
                                    hdct.TenSanPham ,
                                    hdct.DmSanPhamREF ,
                                    hdct.ThanhTien
                          FROM      HopDong HD
                                    INNER JOIN HopDongChiTiet hdct ON HD.HopDongID = hdct.HopDongFK
                                                              AND HD.TrangThaiHopDong <> 3
                                                              AND hdct.DeletedStatus = 0
                                                              AND NOT ( hdct.DmLoaiREF = 13
                                                              OR hdct.DmLoaiBannerREF = 18
                                                              )
                                    LEFT JOIN DotChayHopDongChiTiet dchdct ON hdct.HopDongChiTietID = dchdct.HopDongChiTietREF
                                                              AND hdct.HopDongFK = dchdct.HopDongREF
                          WHERE     @NgayThucHien BETWEEN dchdct.ThoiGianBatDau
                                                  AND     dchdct.ThoiGianKetThuc
                                    AND hdct.DmSanPhamREF IN ( 241, 242, 264,
                                                              300, 268, 248,
                                                              270, 243, 244,
                                                              249, 385, 5005, 5006, 5007, 5082 )
                        ) HD
                        FULL OUTER JOIN ( SELECT    tchdct.ThucChayHopDongChiTietID ,
                                                    tchdct.HopDongREF ,
                                                    tchdct.HopDongChiTietREF
                                          FROM      ThucChayHopDongChiTiet tchdct
                                                    INNER JOIN HopDongChiTiet hdct ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
                                                              AND hdct.DeletedStatus = 0
                                                              AND tchdct.DeletedStatus = 0
                                          WHERE     1 = 1
                                                    AND @NgayThucHien BETWEEN tchdct.ThoiGianBatDau
                                                              AND
                                                              tchdct.ThoiGianKetThuc
                                                    AND hdct.DmSanPhamREF IN (
                                                    241, 242, 264, 300, 268,
                                                    248, 270, 243, 244, 249,
                                                    385, 5005, 5006, 5007, 5082 )
                                        ) ThucTreo ON HD.HopDongID = ThucTreo.HopDongREF
                                                      AND HD.HopDongChiTietID = ThucTreo.HopDongChiTietREF	

                SELECT  *
                FROM    @Table
                WHERE   CheckedStatus <> 0
	
		
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
            END
    END

```
