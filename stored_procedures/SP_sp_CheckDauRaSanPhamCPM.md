# Stored Procedure: `sp_CheckDauRaSanPhamCPM`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-03-29 16:31:58.513000
- **Ngày sửa cuối**: 2017-06-27 10:39:37.423000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayDanhSoHopDong` | `datetime(8)` | No |
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--sp_CheckDauRaSanPhamCPM '2015-01-01','2017-05-20','2017-06-25'
CREATE PROCEDURE [dbo].[sp_CheckDauRaSanPhamCPM]
    @NgayDanhSoHopDong DATETIME = '2015-01-01' ,
    @FromDate DATETIME = '2017-05-20' ,
    @ToDate DATETIME = '2017-05-25'
AS
    BEGIN
        DELETE  FROM dbo.Check_ThongTinDauRaSanPham
        WHERE   CONVERT(DATE, NgayThucHien) = CONVERT(DATE, GETDATE())
                AND IDLyDo IN ( 19, 20 );
        SELECT DISTINCT
                HopDongID
        INTO    #HopDongPhatSinhThucChay
        FROM    dbo.ThucChayDaTinh
        WHERE   DmSanPhamREF IN ( 339, 370, 598, 240, 613, 598, 342, 680, 732,
                                  735 )
                AND NgayThucHien BETWEEN @FromDate AND @ToDate
                AND GiaTriThayDoi = 0
                AND NgayDanhSoHopDong >= @NgayDanhSoHopDong;
                
	  ----Hợp đồng đã chạy xong
   --     SELECT  A.HopDongID
   --     INTO    #HopDongChayXong
   --     FROM    dbo.ThucChayDaTinh A
   --             INNER JOIN #HopDongPhatSinhThucChay B ON B.HopDongID = A.HopDongID
   --     WHERE   DmSanPhamREF IN ( 339, 370, 598, 240, 613, 598, 342, 680, 732,
   --                               735 )
   --             AND ( A.DmHinhThucQuangCao NOT IN ( 13, 42 )
   --                   OR A.DmLoaiBannerREF = 18
   --                 )
   --     GROUP BY A.HopDongID ,
   --             A.ThanhTien
   --     HAVING  SUM(A.ThanhTienThucChayTruocTrietKhau + A.GiaTriThayDoi) <> A.ThanhTien;

--DROP TABLE #HopDongPhatSinhThucChay
        SELECT  A.HopDongID ,
                SoHopDong ,
                DmSanPhamREF ,
                HopDongChiTietREF ,
                DonViTinh ,
                SUM(SoLuongThucChay) 
                + SUM(A.SoLuongThayDoi) SoLuongThucChay ,
                SUM(ThanhTienSauTrietKhauThucChay) 
                + SUM(A.GiaTriThayDoi) ThanhTienThucChay
        INTO    #ThucChayDaTinh
        FROM    dbo.ThucChayDaTinh A
                INNER JOIN #HopDongPhatSinhThucChay B ON B.HopDongID = A.HopDongID
        WHERE   DmSanPhamREF IN ( 339, 370, 598, 240, 613, 598, 342, 680, 732,
                                  735 )
                AND ( A.DmHinhThucQuangCao NOT IN ( 13, 42 )
                      OR A.DmLoaiBannerREF = 18
                    ) 
        --AND GiaTriThayDoi = 0
GROUP BY        A.HopDongID ,
                SoHopDong ,
                DmSanPhamREF ,
                HopDongChiTietREF ,
                DonViTinh; 
        
        SELECT  hdct.HopDongFK ,
                hdct.HopDongChiTietID ,
                hdct.DmSanPhamREF ,
                hdct.TenSanPham ,
                hdct.DonViTinh ,
                CASE WHEN hdct.DonViTinh = 'CPM' THEN hdct.SoLuong * 1000
                     ELSE hdct.SoLuong
                END SoLuong ,
                hdct.ThanhTien ,
                hdct.KhuyenMai
        INTO    #HopDongChiTiet
        FROM    dbo.HopDong
                INNER JOIN dbo.HopDongChiTiet hdct ON HopDongID = hdct.HopDongFK
                INNER JOIN #HopDongPhatSinhThucChay pstc ON pstc.HopDongID = HopDong.HopDongID
        WHERE   hdct.DmSanPhamREF IN ( 339, 370, 598, 240, 613, 598, 342, 680,
                                       732, 735 )
                AND ( hdct.DmLoaiREF NOT IN ( 13, 42 )
                      OR hdct.DmLoaiBannerREF = 18
                    ); 

--DROP TABLE #ThucChayDaTinh

        SELECT  hd.HopDongID ,
                hd.SoHopDong ,
                hdct.DmSanPhamREF ,
                hdct.HopDongChiTietID ,
                hdct.DonViTinh ,
                hdct.SoLuong ,
                hdct.DonGia ,
                hdct.ChietKhau ,
                hdctabn.TiLeThucChayHDCTSoVoiBanner ,
                hdctabn.DmBannerID
        INTO    #ThongTinSanPham
        FROM    dbo.ThucChayHopDongChiTietAndBanner hdctabn
                INNER JOIN dbo.HopDong hd ON hd.HopDongID = hdctabn.HopDongREF
                INNER JOIN dbo.HopDongChiTiet hdct ON hdctabn.HopDongChiTietREF = hdct.HopDongChiTietID
                INNER JOIN #HopDongPhatSinhThucChay pstc ON pstc.HopDongID = hd.HopDongID
        WHERE   1 = 1
                AND DmSanPhamREF IN ( 339, 240, 370, 598, 613, 342, 680, 732,
                                      735 )
        --AND hd.NgayDanhSoHopDong >= @NgayDanhSoHopDong
                AND NOT ( hdct.DmLoaiBannerREF = 17 -- Bỏ chi phí
                          AND hdct.DonViTinhREF = 10 -- Bỏ gói
                          AND hdct.DmLoaiNenTangREF = 8 -- Bỏ nền tảng retargeting
                          AND hdct.DmLoaiREF = 42 -- Bỏ HTQC admatic
                        );
        

        SELECT  hd.HopDongID ,
                hd.SoHopDong ,
                ( CASE WHEN TypeProduct = 5 THEN 339
                       WHEN TypeProduct = 8 THEN 240
                       WHEN TypeProduct = 9 THEN 370
                       WHEN TypeProduct = 10 THEN 342
                       WHEN TypeProduct = 14 THEN 598
                       WHEN TypeProduct = 15 THEN 613
                       WHEN TypeProduct = 16 THEN 680
                       WHEN TypeProduct = 17 THEN 732
                       WHEN TypeProduct = 18 THEN 735
                  END ) DmSanPhamREFTC ,
                tc.DmBannerREF ,
                SUM(tc.TongViewThucChay) TongView ,
                SUM(tc.TongClickThucChay) TongClick
        INTO    #ThucChaySanPham
        FROM    dbo.ThucChay tc
                INNER JOIN dbo.HopDong hd ON hd.SoHopDong = tc.SoHopDong
                INNER JOIN #HopDongPhatSinhThucChay pstc ON pstc.HopDongID = hd.HopDongID
                                                            AND DmBannerREF IS NOT NULL
                                                            AND TypeProduct IN (
                                                            5, 8, 9, 10, 14,
                                                            15, 16, 17, 18 )
--WHERE   hd.NgayDanhSoHopDong >= @NgayDanhSoHopDong
        --AND hd.NgayDanhSoHopDong >= '2017-01-01'
        GROUP BY hd.HopDongID ,
                hd.SoHopDong ,
                tc.DmBannerREF ,
                CASE WHEN TypeProduct = 5 THEN 339
                     WHEN TypeProduct = 8 THEN 240
                     WHEN TypeProduct = 9 THEN 370
                     WHEN TypeProduct = 10 THEN 342
                     WHEN TypeProduct = 14 THEN 598
                     WHEN TypeProduct = 15 THEN 613
                     WHEN TypeProduct = 16 THEN 680
                     WHEN TypeProduct = 17 THEN 732
                     WHEN TypeProduct = 18 THEN 735
                END;

        --SELECT  *
        --FROM    #ThucChaySanPham
        --WHERE   SoHopDong = 'QC1710617';

        SELECT  A.HopDongID ,
                A.SoHopDong ,
                SUM(A.TongView * ISNULL(B.TiLeThucChayHDCTSoVoiBanner, 0))
                / 100 TongView ,
                SUM(A.TongClick * ISNULL(B.TiLeThucChayHDCTSoVoiBanner, 0))
                / 100 TongClick ,
                A.DmSanPhamREFTC ,
                B.HopDongChiTietID ,
                B.SoLuong ,
                B.DonGia ,
                B.ChietKhau ,
                B.DonViTinh ,
                CASE WHEN B.DonViTinh = 'CPM'
                     THEN SUM(A.TongView / 1000) * B.DonGia * ( 1
                                                              - B.ChietKhau
                                                              / 100 )
                     ELSE SUM(A.TongClick) * B.DonGia * ( 1 - B.ChietKhau
                                                          / 100 )
                END ThanhTienThucChay
        INTO    #ThucChayTuTinh
        FROM    #ThucChaySanPham A
                LEFT JOIN #ThongTinSanPham B ON B.HopDongID = A.HopDongID
                                                AND B.SoHopDong = A.SoHopDong
                                                AND A.DmSanPhamREFTC = B.DmSanPhamREF
                                                AND A.DmBannerREF = B.DmBannerID
--WHERE   A.HopDongID = 47653
GROUP BY        A.HopDongID ,
                A.SoHopDong ,
                A.DmSanPhamREFTC ,
                B.HopDongChiTietID ,
                B.DonGia ,
                B.ChietKhau ,
                B.DonViTinh ,
                B.SoLuong;
--SELECT * FROM  #ThucChayTuTinh WHERE SoHopDong='QC1710617'
        SELECT  HopDongID ,
                SoHopDong ,
                TongView ,
                TongClick ,
                DmSanPhamREFTC ,
                HopDongChiTietID ,
                SoLuong ,
                DonGia ,
                ChietKhau ,
                DonViTinh ,
                CASE WHEN DonViTinh = 'CPM'
                     THEN CASE WHEN TongView - SoLuong * 1000 > 0
                               THEN SoLuong * 1000
                               ELSE TongView
                          END
                     WHEN DonViTinh = 'CPC'
                     THEN CASE WHEN TongClick - SoLuong > 0 THEN SoLuong
                               ELSE TongClick
                          END
                     ELSE 0
                END SoLuongThucChay ,
                CASE WHEN ChietKhau < 100
                     THEN CASE WHEN DonViTinh = 'CPM'
                               THEN CASE WHEN TongView - SoLuong * 1000 > 0
                                         THEN SoLuong * DonGia * ( 1
                                                              - ChietKhau
                                                              / 100 )
                                         ELSE SUM(TongView / 1000) * DonGia
                                              * ( 1 - ChietKhau / 100 )
                                    END
                               WHEN DonViTinh = 'CPC'
                               THEN CASE WHEN TongClick - SoLuong > 0
                                         THEN SoLuong * DonGia * ( 1
                                                              - ChietKhau
                                                              / 100 )
                                         ELSE SUM(TongClick) * DonGia * ( 1
                                                              - ChietKhau
                                                              / 100 )
                                    END
                               ELSE 0
                          END
                END ThanhTienThucChay ,
                CASE WHEN ChietKhau = 100
                     THEN CASE WHEN DonViTinh = 'CPM'
                               THEN CASE WHEN TongView - SoLuong * 1000 > 0
                                         THEN SoLuong * DonGia
                                         ELSE SUM(TongView / 1000) * DonGia
                                    END
                               WHEN DonViTinh = 'CPC'
                               THEN CASE WHEN TongClick - SoLuong > 0
                                         THEN SoLuong * DonGia
                                         ELSE SUM(TongClick) * DonGia
                                    END
                               ELSE 0
                          END
                END ThanhTienThucChayKM
        FROM    #ThucChayTuTinh
        WHERE   SoHopDong = 'QC1710617'
        GROUP BY HopDongID ,
                SoHopDong ,
                TongView ,
                TongClick ,
                DmSanPhamREFTC ,
                HopDongChiTietID ,
                SoLuong ,
                DonGia ,
                ChietKhau ,
                DonViTinh;
        INSERT  INTO dbo.Check_ThongTinDauRaSanPham
                ( NgayThucHien ,
                  HopDongID ,
                  SoHopDong ,
                  HopDongChiTietID ,
                  DmSanPhamREF ,
                  DonViTinh ,
                  SLThucChay ,
                  SLChayTuTinh ,
                  ThanhTienThucChay ,
                  TienThucChayTuTinh ,
                  GiaTriLech ,
                  IDLyDo ,
                  LyDo ,
                  TrangThaiXuLy ,
                  IDLoai ,
                  TenLoai ,
                  GhiChu ,
                  TenSanPham ,
                  SoLuongHD ,
                  ThanhTienHD ,
                  CreatedAt
                )
                SELECT  NgayThucHien ,
                        A.HopDongID ,
                        A.SoHopDong ,
                        A.HopDongChiTietREF ,
                        A.DmSanPhamREF ,
                        A.DonViTinh ,
                        A.SoLuongThucChay ,
                        SoLuongThucChayTuTinh ,
                        A.ThanhTienThucChay ,
                        ThanhTienThucChayTuTinh ,
                        SLLech ,
                        19 IDLyDo ,
                        B.TenLoiChiTiet ,
                        0 ,
                        ID_Loai ,
                        TenLoai ,
                        '' ,
                        A.TenSanPham ,
                        A.SoLuong ,
                        A.ThanhTien ,
                        GETDATE()
                FROM    ( SELECT    GETDATE() NgayThucHien ,
                                    A.HopDongID ,
                                    A.SoHopDong ,
                                    A.HopDongChiTietREF ,
                                    A.DmSanPhamREF ,
                                    A.DonViTinh ,
                                    A.SoLuongThucChay ,
                                    ISNULL(B.SoLuongThucChay, 0) SoLuongThucChayTuTinh ,
                                    A.ThanhTienThucChay ,
                                    ISNULL(B.ThanhTienThucChay, 0)
                                    + ISNULL(ThanhTienThucChayKM, 0) ThanhTienThucChayTuTinh ,
                                    A.SoLuongThucChay
                                    - ISNULL(B.SoLuongThucChay, 0) SLLech ,
                                    19 IDLyDo ,
                                    hdct.TenSanPham ,
                                    hdct.SoLuong ,
                                    hdct.ThanhTien
                          FROM      #ThucChayDaTinh A
                                    INNER JOIN #HopDongChiTiet hdct ON A.HopDongID = hdct.HopDongFK
                                                              AND A.HopDongChiTietREF = hdct.HopDongChiTietID
                                                              AND hdct.DmSanPhamREF = A.DmSanPhamREF
                                    LEFT JOIN ( SELECT  HopDongID ,
                                                        SoHopDong ,
                                                        TongView ,
                                                        TongClick ,
                                                        DmSanPhamREFTC ,
                                                        HopDongChiTietID ,
                                                        SoLuong ,
                                                        DonGia ,
                                                        ChietKhau ,
                                                        DonViTinh ,
                                                        CASE WHEN DonViTinh = 'CPM'
                                                             THEN CASE
                                                              WHEN TongView
                                                              - SoLuong * 1000 > 0
                                                              THEN SoLuong
                                                              * 1000
                                                              ELSE TongView
                                                              END
                                                             WHEN DonViTinh = 'CPC'
                                                             THEN CASE
                                                              WHEN TongClick
                                                              - SoLuong > 0
                                                              THEN SoLuong
                                                              ELSE TongClick
                                                              END
                                                             ELSE 0
                                                        END SoLuongThucChay ,
                                                        CASE WHEN ChietKhau < 100
                                                             THEN CASE
                                                              WHEN DonViTinh = 'CPM'
                                                              THEN CASE
                                                              WHEN TongView
                                                              - SoLuong * 1000 > 0
                                                              THEN SoLuong
                                                              * DonGia * ( 1
                                                              - ChietKhau
                                                              / 100 )
                                                              ELSE SUM(TongView
                                                              / 1000) * DonGia
                                                              * ( 1
                                                              - ChietKhau
                                                              / 100 )
                                                              END
                                                              WHEN DonViTinh = 'CPC'
                                                              THEN CASE
                                                              WHEN TongClick
                                                              - SoLuong > 0
                                                              THEN SoLuong
                                                              * DonGia * ( 1
                                                              - ChietKhau
                                                              / 100 )
                                                              ELSE SUM(TongClick)
                                                              * DonGia * ( 1
                                                              - ChietKhau
                                                              / 100 )
                                                              END
                                                              ELSE 0
                                                              END
                                                        END ThanhTienThucChay ,
                                                        CASE WHEN ChietKhau = 100
                                                             THEN CASE
                                                              WHEN DonViTinh = 'CPM'
                                                              THEN CASE
                                                              WHEN TongView
                                                              - SoLuong * 1000 > 0
                                                              THEN SoLuong
                                                              * DonGia
                                                              ELSE SUM(TongView
                                                              / 1000) * DonGia
                                                              END
                                                              WHEN DonViTinh = 'CPC'
                                                              THEN CASE
                                                              WHEN TongClick
                                                              - SoLuong > 0
                                                              THEN SoLuong
                                                              * DonGia
                                                              ELSE SUM(TongClick)
                                                              * DonGia
                                                              END
                                                              ELSE 0
                                                              END
                                                        END ThanhTienThucChayKM
                                                FROM    #ThucChayTuTinh
                                                GROUP BY HopDongID ,
                                                        SoHopDong ,
                                                        TongView ,
                                                        TongClick ,
                                                        DmSanPhamREFTC ,
                                                        HopDongChiTietID ,
                                                        SoLuong ,
                                                        DonGia ,
                                                        ChietKhau ,
                                                        DonViTinh
                                              ) B ON B.HopDongID = A.HopDongID
                                                     AND B.SoHopDong = A.SoHopDong
                                                     AND A.DmSanPhamREF = B.DmSanPhamREFTC
                                                     AND A.HopDongChiTietREF = B.HopDongChiTietID
                          WHERE     A.DonViTinh IN ( 'VIEW', 'CLICK' )
                                    AND ABS(A.SoLuongThucChay
                                            - ISNULL(B.SoLuongThucChay, 0)) > 3
                                    AND ABS(hdct.SoLuong - A.SoLuongThucChay) > 2
                        ) A
                        LEFT JOIN dbo.DmLoiKhiCheckDuLieu B ON A.IDLyDo = B.ID
                WHERE   ABS(A.ThanhTienThucChay - A.ThanhTien) > 10;
        INSERT  INTO dbo.Check_ThongTinDauRaSanPham
                ( NgayThucHien ,
                  HopDongID ,
                  SoHopDong ,
                  HopDongChiTietID ,
                  DmSanPhamREF ,
                  DonViTinh ,
                  SLThucChay ,
                  SLChayTuTinh ,
                  ThanhTienThucChay ,
                  TienThucChayTuTinh ,
                  GiaTriLech ,
                  IDLyDo ,
                  LyDo ,
                  TrangThaiXuLy ,
                  IDLoai ,
                  TenLoai ,
                  GhiChu ,
                  TenSanPham ,
                  SoLuongHD ,
                  ThanhTienHD ,
                  CreatedAt
                )
                SELECT  NgayThucHien ,
                        A.HopDongID ,
                        A.SoHopDong ,
                        A.HopDongChiTietREF ,
                        A.DmSanPhamREF ,
                        A.DonViTinh ,
                        A.SoLuongThucChay ,
                        SoLuongThucChayTuTinh ,
                        A.ThanhTienThucChay ,
                        ThanhTienThucChayTuTinh ,
                        GiaTriLech ,
                        20 IDLyDo ,
                        B.TenLoiChiTiet ,
                        0 ,
                        ID_Loai ,
                        TenLoai ,
                        '' ,
                        A.TenSanPham ,
                        A.SoLuong ,
                        A.ThanhTien ,
                        GETDATE()
                FROM    ( SELECT    GETDATE() NgayThucHien ,
                                    A.HopDongID ,
                                    A.SoHopDong ,
                                    A.HopDongChiTietREF ,
                                    A.DmSanPhamREF ,
                                    A.DonViTinh ,
                                    A.SoLuongThucChay ,
                                    B.SoLuongThucChay SoLuongThucChayTuTinh ,
                                    A.ThanhTienThucChay ,
                                    ISNULL(B.ThanhTienThucChay, 0)
                                    + ISNULL(ThanhTienThucChayKM, 0) ThanhTienThucChayTuTinh ,
                                    A.ThanhTienThucChay
                                    - ( ISNULL(B.ThanhTienThucChay, 0)
                                        + ISNULL(ThanhTienThucChayKM, 0) ) GiaTriLech ,
                                    20 IDLyDo ,
                                    hdct.TenSanPham ,
                                    hdct.SoLuong ,
                                    hdct.ThanhTien
                          FROM      #ThucChayDaTinh A
                                    INNER JOIN #HopDongChiTiet hdct ON A.HopDongID = hdct.HopDongFK
                                                              AND A.HopDongChiTietREF = hdct.HopDongChiTietID
                                                              AND hdct.DmSanPhamREF = A.DmSanPhamREF
                                    LEFT JOIN ( SELECT  HopDongID ,
                                                        SoHopDong ,
                                                        TongView ,
                                                        TongClick ,
                                                        DmSanPhamREFTC ,
                                                        HopDongChiTietID ,
                                                        SoLuong ,
                                                        DonGia ,
                                                        ChietKhau ,
                                                        DonViTinh ,
                                                        CASE WHEN DonViTinh = 'CPM'
                                                             THEN CASE
                                                              WHEN TongView
                                                              - SoLuong * 1000 > 0
                                                              THEN SoLuong
                                                              * 1000
                                                              ELSE TongView
                                                              END
                                                             WHEN DonViTinh = 'CPC'
                                                             THEN CASE
                                                              WHEN TongClick
                                                              - SoLuong > 0
                                                              THEN SoLuong
                                                              ELSE TongClick
                                                              END
                                                             ELSE 0
                                                        END SoLuongThucChay ,
                                                        CASE WHEN ChietKhau < 100
                                                             THEN CASE
                                                              WHEN DonViTinh = 'CPM'
                                                              THEN CASE
                                                              WHEN TongView
                                                              - SoLuong * 1000 > 0
                                                              THEN SoLuong
                                                              * DonGia * ( 1
                                                              - ChietKhau
                                                              / 100 )
                                                              ELSE SUM(TongView
                                                              / 1000) * DonGia
                                                              * ( 1
                                                              - ChietKhau
                                                              / 100 )
                                                              END
                                                              WHEN DonViTinh = 'CPC'
                                                              THEN CASE
                                                              WHEN TongClick
                                                              - SoLuong > 0
                                                              THEN SoLuong
                                                              * DonGia * ( 1
                                                              - ChietKhau
                                                              / 100 )
                                                              ELSE SUM(TongClick)
                                                              * DonGia * ( 1
                                                              - ChietKhau
                                                              / 100 )
                                                              END
                                                              ELSE 0
                                                              END
                                                        END ThanhTienThucChay ,
                                                        CASE WHEN ChietKhau = 100
                                                             THEN CASE
                                                              WHEN DonViTinh = 'CPM'
                                                              THEN CASE
                                                              WHEN TongView
                                                              - SoLuong * 1000 > 0
                                                              THEN SoLuong
                                                              * DonGia
                                                              ELSE SUM(TongView
                                                              / 1000) * DonGia
                                                              END
                                                              WHEN DonViTinh = 'CPC'
                                                              THEN CASE
                                                              WHEN TongClick
                                                              - SoLuong > 0
                                                              THEN SoLuong
                                                              * DonGia
                                                              ELSE SUM(TongClick)
                                                              * DonGia
                                                              END
                                                              ELSE 0
                                                              END
                                                        END ThanhTienThucChayKM
                                                FROM    #ThucChayTuTinh
                                                GROUP BY HopDongID ,
                                                        SoHopDong ,
                                                        TongView ,
                                                        TongClick ,
                                                        DmSanPhamREFTC ,
                                                        HopDongChiTietID ,
                                                        SoLuong ,
                                                        DonGia ,
                                                        ChietKhau ,
                                                        DonViTinh
                                              ) B ON B.HopDongID = A.HopDongID
                                                     AND B.SoHopDong = A.SoHopDong
                                                     AND A.DmSanPhamREF = B.DmSanPhamREFTC
                                                     AND A.HopDongChiTietREF = B.HopDongChiTietID
                          WHERE     A.DonViTinh IN ( 'VIEW', 'CLICK' )
                                    AND ABS(A.ThanhTienThucChay
                                            - ( ISNULL(B.ThanhTienThucChay, 0)
                                                + ISNULL(ThanhTienThucChayKM,
                                                         0) )) > 10
                                    AND ABS(hdct.ThanhTien
                                            - A.ThanhTienThucChay) > 10
                        ) A
                        LEFT JOIN dbo.DmLoiKhiCheckDuLieu B ON A.IDLyDo = B.ID
                WHERE   ABS(A.ThanhTienThucChay - A.ThanhTien) > 10;     
    END;
--DROP TABLE #ThongTinSanPham
--DROP TABLE #ThucChaySanPham
--DROP TABLE #ThucChayDaTinh
--DROP TABLE #ThucChayTuTinh
--SELECT * FROM dbo.HopDongChiTiet WHERE HopDongChiTietID=108657

--SELECT  DonViTinh ,
--        SUM(SoLuongThucChay) ,
--        SUM(SoLuongThayDoi) ,
--        SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)
--FROM    dbo.ThucChayDaTinh
--WHERE   HopDongChiTietREF = 108657
--GROUP BY DonViTinh

--SELECT  NgayThucHien ,
--        *
--FROM    dbo.ThucChayDaTinh
--WHERE   HopDongChiTietREF = 108657
--GROUP BY DonViTinh
```
