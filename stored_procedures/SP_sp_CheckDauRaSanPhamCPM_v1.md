# Stored Procedure: `sp_CheckDauRaSanPhamCPM_v1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-08-08 16:22:31.323000
- **Ngày sửa cuối**: 2017-09-22 10:19:10.280000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayDanhSo` | `datetime(8)` | No |
| `@NgayBatDau` | `datetime(8)` | No |
| `@NgayKetThuc` | `datetime(8)` | No |

## Definition (Source Code)

```sql
 --sp_CheckDauRaSanPhamCPM_v1 '2016-01-01','2017-09-06','2017-09-06'
CREATE PROCEDURE [dbo].[sp_CheckDauRaSanPhamCPM_v1]
    @NgayDanhSo DATETIME = '2014-01-01' ,
    @NgayBatDau DATETIME = '2017-08-06' ,
    @NgayKetThuc DATETIME = '2017-08-06'
AS
    BEGIN
        IF ISNULL(@NgayBatDau, '1900-01-01 00:00:00.000') = '1900-01-01 00:00:00.000'
            SET @NgayBatDau = DATEADD(DD, -1, CONVERT(DATE, GETDATE()));
      
        IF ISNULL(@NgayKetThuc, '1900-01-01 00:00:00.000') = '1900-01-01 00:00:00.000'
            SET @NgayKetThuc = DATEADD(DD, -1, CONVERT(DATE, GETDATE()));
        IF ISNULL(@NgayDanhSo, '1900-01-01 00:00:00.000') = '1900-01-01 00:00:00.000'
            SET @NgayDanhSo = '2016-01-01';

	-- Xác định hợp đồng đã chạy xong
        SELECT  hd.HopDongChiTietID
        INTO    #HopDongChayXong
        FROM    [192.168.23.217].ABM_Data_Release.dbo.HopDongChiTiet hd
        WHERE   hd.DmSanPhamREF IN ( 339, 240, 370, 598, 613, 680, 732,
                                     735 )
                AND ABS(hd.ThanhtienThucChay - hd.ThanhTien) < 10;
-- Xác định phân bổ chạy sản phẩm admatic 
        SELECT DISTINCT
                HopDongChiTietREF
        INTO    #HopDongAdmatic
        FROM    dbo.ThucChayHopDongChiTietAndBanner_Admatic;

 

        SELECT  tc.NgayThucHien ,
                hd.HopDongID ,
                ( CASE WHEN TypeProduct = 5 THEN 339
                       WHEN TypeProduct = 8 THEN 240
                       WHEN TypeProduct = 9 THEN 370
                       --WHEN TypeProduct = 10 THEN 342
                       WHEN TypeProduct = 14 THEN 598
                       WHEN TypeProduct = 15 THEN 613
                       WHEN TypeProduct = 16 THEN 680
                       WHEN TypeProduct = 17 THEN 732
                       WHEN TypeProduct = 18 THEN 735
                  END ) DmSanPhamREF ,
                tc.DmBannerREF ,
                SUM(tc.TongClickThucChay) TongClickThucChay ,
                SUM(tc.TongViewThucChay) TongViewThucChay
        INTO    #ThucChayTraVe
        FROM    dbo.ThucChay tc
                INNER JOIN dbo.HopDong hd ON hd.SoHopDong = tc.SoHopDong
        WHERE   tc.NgayThucHien BETWEEN @NgayBatDau
                                AND     @NgayKetThuc
                AND TypeProduct IN ( 5, 8, 9, 14, 15, 16, 17, 18 )
        GROUP BY hd.HopDongID ,
                ( CASE WHEN TypeProduct = 5 THEN 339
                       WHEN TypeProduct = 8 THEN 240
                       WHEN TypeProduct = 9 THEN 370
                       --WHEN TypeProduct = 10 THEN 342
                       WHEN TypeProduct = 14 THEN 598
                       WHEN TypeProduct = 15 THEN 613
                       WHEN TypeProduct = 16 THEN 680
                       WHEN TypeProduct = 17 THEN 732
                       WHEN TypeProduct = 18 THEN 735
                  END ) ,
                tc.DmBannerREF ,
                tc.NgayThucHien;   
        SELECT  tt.* ,
                TTDT.SoLuongThucChay ,
                TTDT.ThanhTienThucChay
        INTO    #KetQua
        FROM    ( SELECT    A.NgayThucHien ,
                            A.HopDongID ,
                            A.HopDongChiTietREF ,
                            A.DmSanPhamREF ,
                            A.ThanhTienHopDong ,
                            A.DonViTinhREF ,
                            A.DonViTinh ,
                            CASE WHEN A.DonViTinhREF = 1 THEN A.TongView
                                 ELSE A.TongClick
                            END SoLuongThucChayTT ,
                            CASE WHEN A.DonViTinhREF = 1
                                 THEN A.ThanhTienTheoDVT * A.TongView
                                 ELSE A.ThanhTienTheoDVT * A.TongClick
                            END ThanhTienThucChayTT
                  FROM      ( SELECT    A.NgayThucHien ,
                                        A.HopDongID ,
                                        ISNULL(hdctabn.HopDongChiTietREF, 0) HopDongChiTietREF ,
                                        A.DmSanPhamREF ,
                                        CASE WHEN hdctabn.ChietKhau = 100
                                             THEN hdctabn.DonGia
                                             ELSE hdctabn.ThanhTien
                                        END ThanhTienHopDong ,
                                        hdctabn.DonViTinhREF ,
                                        hdctabn.DonViTinh ,
                                        hdctabn.SoLuong ,
                                        CASE WHEN hdctabn.ChietKhau = 100
                                             THEN hdctabn.DonGia
                                             ELSE hdctabn.ThanhTien
                                        END
                                        / CASE WHEN hdctabn.DonViTinhREF = 1
                                               THEN hdctabn.SoLuong * 1000
                                               ELSE hdctabn.SoLuong
                                          END ThanhTienTheoDVT ,
                                        SUM(A.TongViewThucChay
                                            * ISNULL(hdctabn.TiLeThucChayHDCTSoVoiBanner,
                                                     0)) / 100 TongView ,
                                        SUM(A.TongClickThucChay
                                            * ISNULL(hdctabn.TiLeThucChayHDCTSoVoiBanner,
                                                     0)) / 100 TongClick
                              FROM      #ThucChayTraVe A
                                        LEFT JOIN ( SELECT  hdctabn.* ,
                                                            hdct.DmSanPhamREF ,
                                                            hdct.SoLuong ,
                                                            hdct.DonGia ,
                                                            hdct.ChietKhau ,
                                                            hdct.ThanhTien ,
                                                            hdct.DonViTinhREF ,
                                                            hdct.DonViTinh
                                                    FROM    dbo.ThucChayHopDongChiTietAndBanner hdctabn
                                                            INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = hdctabn.HopDongChiTietREF
                                                  ) hdctabn ON A.HopDongID = hdctabn.HopDongREF
                                                              AND A.DmBannerREF = hdctabn.DmBannerID
                                                              AND hdctabn.DmSanPhamREF = A.DmSanPhamREF
                              WHERE     DeletedStatus = 0
                                        AND hdctabn.DonViTinhREF IN ( 1, 2 )
                                    --AND hdctabn.HopDongChiTietREF = 509313
                                        AND ISNULL(hdctabn.HopDongChiTietREF,
                                                   0) NOT IN ( SELECT
                                                              *
                                                              FROM
                                                              #HopDongChayXong )
                                        AND ISNULL(hdctabn.HopDongChiTietREF,
                                                   0) NOT IN ( SELECT
                                                              *
                                                              FROM
                                                              #HopDongAdmatic )
                              GROUP BY  A.NgayThucHien ,
                                        A.HopDongID ,
                                        hdctabn.HopDongChiTietREF ,
                                        CASE WHEN hdctabn.ChietKhau = 100
                                             THEN hdctabn.DonGia
                                             ELSE hdctabn.ThanhTien
                                        END ,
                                        hdctabn.DonViTinhREF ,
                                        hdctabn.DonViTinh ,
                                        A.DmSanPhamREF ,
                                        hdctabn.SoLuong
                            ) A
                ) tt
                LEFT JOIN ( SELECT  A.NgayThucHien ,
                                    A.HopDongID ,
                                    HopDongChiTietREF ,
                                    DmSanPhamREF ,
                                    SUM(SoLuongThucChay + SoLuongThucChayKM
                                        + A.SoLuongThucChayLechTreoHa) SoLuongThucChay ,
                                    SUM(ThanhTienSauTrietKhauThucChay
                                        + ThanhTienKM + A.ThanhTienLechTreoHa
                                        * ( 1 - A.ChietKhau / 100 )) ThanhTienThucChay
                            FROM    dbo.ThucChayDaTinh A
                                   -- INNER JOIN dbo.HopDong hd ON A.HopDongID = hd.HopDongID
                            WHERE   DmSanPhamREF IN ( 339, 240, 370, 598,
                                                      613, 680, 732, 735 )
                                    AND NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
                                    AND NOT ( DmHinhThucQuangCao = 13
                                              OR DmLoaiBannerREF = 18
                                            )
                                    AND NOT ( DmHinhThucQuangCao = 42 )
                                    AND A.NgayDanhSoHopDong >= @NgayDanhSo
                                    AND A.HopDongChiTietREF NOT IN ( SELECT
                                                              *
                                                              FROM
                                                              #HopDongChayXong )
                                --AND A.HopDongChiTietREF = 509313
                            GROUP BY A.HopDongID ,
                                    HopDongChiTietREF ,
                                    DmSanPhamREF ,
                                    A.NgayThucHien
                            HAVING  NOT ( SUM(SoLuongThucChay
                                              + SoLuongThucChayKM
                                              + A.SoLuongThucChayLechTreoHa) = 0
                                          AND SUM(ThanhTienSauTrietKhauThucChay
                                                  + ThanhTienKM
                                                  + A.ThanhTienLechTreoHa
                                                  * ( 1 - A.ChietKhau / 100 )) = 0
                                        )
                          ) TTDT ON TTDT.DmSanPhamREF = tt.DmSanPhamREF
                                    AND TTDT.HopDongChiTietREF = tt.HopDongChiTietREF
                                    AND TTDT.HopDongID = tt.HopDongID
                                    AND TTDT.NgayThucHien = tt.NgayThucHien
        WHERE   ABS(ISNULL(tt.ThanhTienThucChayTT, 0)
                    - ISNULL(TTDT.ThanhTienThucChay, 0)) > 10
        ORDER BY tt.HopDongChiTietREF;
       


        INSERT  INTO dbo.KiemSoatDauRaThucChay_ChiTiet
                ( NgayThucHien ,
                  DotChayBooking ,
                  HopDongID ,
                  SoHopDong ,
                  HopDongChiTietREF ,
                  DmSanPhamREF ,
                  TenSanPham ,
                  DmHinhThucQuangCaoREF ,
                  ThongTinThucTreo ,
                  ThongTinThucChay ,
                  IDLoi ,
                  TenLoiChiTiet ,
                  SPXuLyLoi ,
                  TrangThaiXuLy ,
                  CreatedAt
                )
                SELECT  A.NgayThucHien ,
                        A.DotChayBooking ,
                        A.HopDongID ,
                        A.SoHopDong ,
                        A.HopDongChiTietREF ,
                        A.DmSanPhamREF ,
                        A.TenSanPham ,
                        A.HinhThucQuangCao ,
                        A.SoLuongThucChayTT ,
                        A.SoLuongThucChay ,
                        A.IDLoi ,
                        B.TenLoiChiTiet ,
                        B.SPXuLy ,
                        0 TrangThaiXuLy ,
                        GETDATE()-- Ngày tạo
                FROM    ( SELECT    *
                          FROM      ( SELECT    @NgayBatDau NgayThucHien ,-- Ngày thực hiện, 
                                                '' DotChayBooking ,
                                                A.HopDongID ,
                                                hd.SoHopDong ,
                                                A.HopDongChiTietREF ,
                                                A.DmSanPhamREF ,
                                                hdct.TenSanPham ,
                                                hdct.DmLoaiREF HinhThucQuangCao ,
                                                dbo.FormatNumber(A.SoLuongThucChayTT) SoLuongThucChayTT ,
                                                dbo.FormatNumber(A.SoLuongThucChay) SoLuongThucChay ,
                                                3 IDLoi
                                      FROM      #KetQua A
                                                INNER JOIN dbo.HopDong hd ON A.HopDongID = hd.HopDongID
                                                INNER JOIN dbo.HopDongChiTiet hdct ON A.HopDongChiTietREF = hdct.HopDongChiTietID
                                      WHERE     ABS(A.SoLuongThucChay
                                                    - A.SoLuongThucChayTT) > 10
                                      UNION ALL
                                      SELECT    @NgayBatDau NgayThucHien ,-- Ngày thực hiện, 
                                                '' DotChayBooking ,
                                                A.HopDongID ,
                                                hd.SoHopDong ,
                                                A.HopDongChiTietREF ,
                                                A.DmSanPhamREF ,
                                                hdct.TenSanPham ,
                                                hdct.DmLoaiREF HinhThucQuangCao ,
                                                dbo.FormatNumber(A.ThanhTienThucChayTT) ThanhTienThucChayTT ,
                                                dbo.FormatNumber(A.ThanhTienThucChay) ThanhTienThucChay ,
                                                4 IDLoi
                                      FROM      #KetQua A
                                                INNER JOIN dbo.HopDong hd ON A.HopDongID = hd.HopDongID
                                                INNER JOIN dbo.HopDongChiTiet hdct ON A.HopDongChiTietREF = hdct.HopDongChiTietID
                                      WHERE     ABS(A.ThanhTienThucChayTT
                                                    - A.ThanhTienThucChay) > 10
                                    ) A
                        ) A
                        INNER JOIN KiemSoatThucChay_DanhSachLoi B ON A.IDLoi = B.ID;



    END;
  
```
