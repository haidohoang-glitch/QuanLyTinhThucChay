# Stored Procedure: `ThucChay_CheckThongTinThucChayCPD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-03-10 16:00:03.977000
- **Ngày sửa cuối**: 2017-03-10 16:12:29.090000

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
--EXEC [ThucChay_CheckThongTinThucChayCPD]	@StartDate = '2017-03-05',	@EndDate = '2017-03-06'
CREATE PROCEDURE [dbo].[ThucChay_CheckThongTinThucChayCPD]
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
              DmBannerID_Thuctreo INT ,
              BookingREF_Thuctreo INT ,
              BookingREF_sp NVARCHAR(MAX) ,
              DmBannerREF_sp INT ,
              IDLoai INT ,
              GhiChuPhanBo NVARCHAR(MAX) ,
              LyDo NVARCHAR(2500)
            )
        DECLARE @NgayThucHien DATETIME
        SET @NgayThucHien = @StartDate
	--DELETE FROM ThucChay_CheckThucChayCPDDaily WHERE NgayThucHien BETWEEN @StartDate AND @EndDate
        WHILE ( @NgayThucHien <= @EndDate )
            BEGIN
	--//-----------CPD CO DOT CHAY----------------------------------
	-------------DOI CHIEU DATA GIUA HD- SP - THUCTREO ---------------------
                INSERT  INTO @Table
                        SELECT  A.* ,
                                B.TenLoiChiTiet
                        FROM    ( SELECT    @NgayThucHien NgayThucHien ,
                                            ISNULL(HD.HopDongID,
                                                   ThucTreo.HopDongREF) HopDongID ,
                                            ISNULL(HD.SoHopDong, SP.SoHopDong) SoHopDong ,
                                            ISNULL(HD.HopDongChiTietID,
                                                   ThucTreo.HopDongChiTietREF) HopDongChiTietREF ,
                                            HD.BookingREF ,
                                            HD.ThoiGianBatDau ,
                                            HD.ThoiGianKetThuc ,
                                            ThucTreo.DmBannerID ,
                                            ThucTreo.BookingREF BookingTT ,
                                            SP.DanhsachDmBookingREF ,
                                            SP.DmBannerREF ,
                                            CASE WHEN HD.HopDongID IS NOT NULL
                                                      AND ThucTreo.HopDongREF IS NULL
                                                      AND SP.SoHopDong IS NULL
                                                 THEN 2
                                                 WHEN HD.HopDongID IS NOT NULL
                                                      AND ThucTreo.HopDongREF IS NULL
                                                      AND SP.SoHopDong IS NOT NULL
                                                 THEN 3
                                                 WHEN HD.HopDongID IS NOT NULL
                                                      AND ThucTreo.HopDongREF IS NOT NULL
                                                      AND SP.SoHopDong IS NULL
                                                 THEN 4
                                                 WHEN HD.HopDongID IS NULL
                                                      AND ThucTreo.HopDongREF IS NULL
                                                      AND SP.SoHopDong IS NOT NULL
                                                 THEN 5
                                                 WHEN HD.HopDongID IS NULL
                                                      AND ThucTreo.HopDongREF IS NOT NULL
                                                      AND SP.SoHopDong IS NULL
                                                 THEN 6
                                                 WHEN HD.HopDongID IS NULL
                                                      AND ThucTreo.HopDongREF IS NOT NULL
                                                      AND SP.SoHopDong IS NOT NULL
                                                 THEN 7
                                                 ELSE 0
                                            END IDLoai ,
                                            '' AS GhiChu
                                  FROM      ( SELECT DISTINCT
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
                                            FULL OUTER JOIN ( SELECT
                                                              ptcts.SoHopDong ,
                                                              ptcts.DanhsachDmBookingREF ,
                                                              ptcts.DmBannerREF ,
                                                              ptcts.TongViewThucChay
                                                              FROM
                                                              ThucChay ptcts
                                                              INNER JOIN HopDong hd2 ON hd2.SoHopDong = ptcts.SoHopDong
                                                              AND ptcts.TypeProduct IN (
                                                              -2, -3 )
                                                              WHERE
                                                              hd2.TrangThaiHopDong <> 3
                                                              AND ptcts.NgayThucHien = @NgayThucHien
                                                            ) SP ON ThucTreo.DmBannerID = SP.DmBannerREF
                                            FULL OUTER JOIN ( SELECT
                                                              HD.HopDongID ,
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
                                                              FROM
                                                              HopDong HD
                                                              INNER JOIN HopDongChiTiet hdct ON HD.HopDongID = hdct.HopDongFK
                                                              AND HD.TrangThaiHopDong <> 3
                                                              AND hdct.DeletedStatus = 0
                                                              AND NOT ( hdct.DmLoaiREF = 13
                                                              OR hdct.DmLoaiBannerREF = 18
                                                              )
                                                              LEFT JOIN DotChayHopDongChiTiet dchdct ON hdct.HopDongChiTietID = dchdct.HopDongChiTietREF
                                                              AND hdct.HopDongFK = dchdct.HopDongREF
                                                              AND dchdct.DeletedStatus = 0
                                                              WHERE
                                                              @NgayThucHien BETWEEN dchdct.ThoiGianBatDau
                                                              AND
                                                              dchdct.ThoiGianKetThuc
                                                              AND hdct.DmSanPhamREF IN (
                                                              140, 228, 564,
                                                              549 )
                                                            ) HD ON HD.BookingREF = ThucTreo.BookingREF
                                                              AND ThucTreo.HopDongChiTietREF = HD.HopDongChiTietID
                                ) A
                                LEFT JOIN dbo.DmLoiKhiCheckDuLieu B ON A.IDLoai = B.ID

                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
            END
        SELECT  *
        FROM    @Table
        WHERE   IDLoai <> 0
    END

```
