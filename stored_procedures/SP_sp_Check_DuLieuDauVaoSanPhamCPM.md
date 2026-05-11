# Stored Procedure: `sp_Check_DuLieuDauVaoSanPhamCPM`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-03-11 10:23:49.530000
- **Ngày sửa cuối**: 2017-07-21 10:22:55.543000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayDanhSo` | `datetime(8)` | No |
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--sp_Check_DuLieuDauVaoSanPhamCPM '2014-01-01','2017-03-01','2014-01-01'
CREATE PROCEDURE [dbo].[sp_Check_DuLieuDauVaoSanPhamCPM]
    @NgayDanhSo DATETIME,
    @FromDate DATETIME ,
    @ToDate DATETIME 

AS
    BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
        SET NOCOUNT ON;
        DELETE  FROM dbo.Check_DuLieuDauVaoSanPham
        WHERE   CONVERT(DATE, NgayThucHien) = CONVERT(DATE, GETDATE())
                AND IDLoai = 2
                AND IDLyDo IN ( 17, 18 )
    -- Insert statements for procedure here
        INSERT  INTO dbo.Check_DuLieuDauVaoSanPham
                ( NgayThucHien ,
                  HopDongREF ,
                  SoHopDong ,
                  HopDongChiTietREF ,
                  DmSanPhamREF ,
                  DmDonViTinhREF ,
                  DonViTinh ,
                  IDLyDo ,
                  LyDo ,
                  TrangThaiXuLy ,
                  IDLoai ,
                  TenLoai ,
                  GhiChu
	            )
                SELECT  A.NgayThucHien ,
                        A.HopDongFK ,
                        A.SoHopDong ,
                        A.HopDongChiTietID ,
                        A.DmSanPhamREF ,
                        A.DonViTinhREF ,
                        A.DonViTinh ,
                        A.IDLyDo ,
                        B.TenLoiChiTiet LyDo ,
                        A.TrangThaiXuLy ,
                        B.ID_Loai ,
                        B.TenLoai ,
                        A.GhiChu
                FROM    ( SELECT    GETDATE() NgayThucHien ,
                                    HopDongFK ,
                                    hd.SoHopDong ,
                                    hdct.HopDongChiTietID ,
                                    hdct.DmSanPhamREF ,
                                    hdct.DonViTinhREF ,
                                    hdct.DonViTinh ,
                                    17 IDLyDo ,
                                    '' LyDo ,
                                    0 TrangThaiXuLy ,
                                    2 IDLoai ,
                                    'CPM' TenLoai ,
                                    hdct.GhiChu
                          FROM      dbo.HopDong hd
                                    INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
                          WHERE     DonViTinh NOT IN ( 'CPC', 'CPM' )
                                    AND hdct.DmSanPhamREF IN ( 339, 240, 370,
                                                              598, 613, 342,
                                                              680,732,735 )
                                    AND hdct.DeletedStatus = 0
                                    AND hd.Nam >= 2014
                                    AND ROUND(hdct.ThanhTien, 0) <> ROUND(hdct.ThanhtienThucChay,
                                                              0)
                                    AND hd.TrangThaiHopDong <> 3
                                    AND NOT ( (hdct.ThanhTien = 0) )
                                    AND ( hdct.DmLoaiBannerREF <> 17
                                          OR hdct.DmLoaiNenTangREF <> 8
                                        )
									AND DmLoaiREF NOT IN ( 13, 42 )
                                    AND hdct.LastModifiedAt BETWEEN @FromDate AND @ToDate
                                    AND hd.NgayDanhSoHopDong >= @NgayDanhSo
                        ) A
                        LEFT JOIN dbo.DmLoiKhiCheckDuLieu B ON A.IDLyDo = B.ID
                ORDER BY A.DonViTinh ,
                        A.DmSanPhamREF ,
                        A.HopDongFK
		
        SELECT  hd.HopDongID ,
                tc.SoHopDong SoHopDongTC ,
                CONVERT(NVARCHAR(50), DmBannerREF) BannerTC ,
                ( CASE WHEN TypeProduct = 5 THEN 339
                       WHEN TypeProduct = 8 THEN 240
                       WHEN TypeProduct = 9 THEN 370
                       WHEN TypeProduct = 10 THEN 342
                       WHEN TypeProduct = 14 THEN 598
                       WHEN TypeProduct = 15 THEN 613
                       WHEN TypeProduct = 16 THEN 680
					   WHEN TypeProduct = 17 THEN 732
                       WHEN TypeProduct = 18 THEN 735
                  END ) DmSanPhamREFTC
        INTO    #BannerThucChay
        FROM    dbo.ThucChay tc
                INNER JOIN dbo.HopDong hd ON hd.SoHopDong = tc.SoHopDong
        WHERE   DmBannerREF IS NOT NULL
                AND TypeProduct IN ( 5, 8, 9, 10, 14, 15, 16,17,18 )
                AND NgayThucHien BETWEEN @FromDate AND @ToDate
                AND hd.NgayDanhSoHopDong >= @FromDate
                AND hd.TrangThaiHopDong <> 3
				AND DmBannerREF NOT IN (SELECT DISTINCT DmBannerID FROM dbo.ThucChayHopDongChiTietAndBanner_Admatic)
        GROUP BY tc.SoHopDong ,
                DmBannerREF ,
                CASE WHEN TypeProduct = 5 THEN 339
                     WHEN TypeProduct = 8 THEN 240
                     WHEN TypeProduct = 9 THEN 370
                     WHEN TypeProduct = 10 THEN 342
                     WHEN TypeProduct = 14 THEN 598
                     WHEN TypeProduct = 15 THEN 613
                     WHEN TypeProduct = 16 THEN 680
					 WHEN TypeProduct = 17 THEN 732
                     WHEN TypeProduct = 18 THEN 735
                END ,
                hd.HopDongID
        HAVING  ISNULL(SUM(TongViewThucChay), 0) > 1000
                AND ISNULL(SUM(TongClickThucChay), 0) > 10


        SELECT DISTINCT
                hd.HopDongID ,
                hd.SoHopDong ,
                tt.DmBannerID ,
                hdct.DmSanPhamREF
        INTO    #BannerHopDong
        FROM    dbo.ThucChayHopDongChiTietAndBanner tt
                INNER JOIN HopDongChiTiet hdct ON hdct.HopDongChiTietID = tt.HopDongChiTietREF
                INNER JOIN dbo.HopDong hd ON hdct.HopDongFK = hd.HopDongID
        WHERE   tt.DeletedStatus = 0
                AND hdct.DeletedStatus = 0
                AND hd.NgayDanhSoHopDong >= @FromDate
                AND hdct.DmSanPhamREF IN ( 339, 370, 598, 240, 613, 598, 342,
                                           680 ,732,735)
                AND hd.TrangThaiHopDong <> 3
				AND DmLoaiREF NOT IN ( 13, 42 )


        INSERT  INTO dbo.Check_DuLieuDauVaoSanPham
                ( NgayThucHien ,
                  HopDongREF ,
                  SoHopDong ,
                  DmBannerREF ,
                  DmSanPhamREF ,
                  IDLyDo ,
                  LyDo ,
                  TrangThaiXuLy ,
                  IDLoai ,
                  TenLoai ,
                  GhiChu
                )
                SELECT  A.NgayThucHien ,
                        A.HopDongID ,
                        A.SoHopDongTC ,
                        A.BannerTC ,
                        A.DmSanPhamREFTC ,
                        A.IDLyDo ,
                        B.TenLoiChiTiet ,
                        A.TrangThaiXuLy ,
                        B.ID_Loai ,
                        B.TenLoai ,
                        ''
                FROM    ( SELECT    GETDATE() NgayThucHien ,
                                    A.HopDongID ,
                                    A.SoHopDongTC ,
                                    A.BannerTC ,
                                    A.DmSanPhamREFTC ,
                                    18 IDLyDo ,
                                    0 TrangThaiXuLy
                          FROM      #BannerThucChay A
                                    LEFT JOIN #BannerHopDong B ON 1 = 1
                                                              AND B.HopDongID = A.HopDongID
                                                              AND A.DmSanPhamREFTC = B.DmSanPhamREF
                                                              AND A.BannerTC = B.DmBannerID
                          WHERE     1 = 1
                                    AND ( B.HopDongID IS NULL
                                          OR A.BannerTC <> ISNULL(B.DmBannerID,
                                                              0)
                                        )
                        ) A
                        LEFT JOIN dbo.DmLoiKhiCheckDuLieu B ON A.IDLyDo = B.ID






    END

```
