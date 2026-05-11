# Stored Procedure: `sp_CheckDauRaSanPhamGGFB_v1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-08-09 11:09:12.537000
- **Ngày sửa cuối**: 2017-08-17 15:18:26.277000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayDanhSo` | `datetime(8)` | No |
| `@NgayBatDau` | `datetime(8)` | No |
| `@NgayKetThuc` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--sp_CheckDauRaSanPhamGGFB_v1 '','',''
CREATE PROCEDURE [dbo].[sp_CheckDauRaSanPhamGGFB_v1]
    @NgayDanhSo DATETIME ,
    @NgayBatDau DATETIME ,
    @NgayKetThuc DATETIME
AS
    BEGIN

        IF ISNULL(@NgayBatDau, '1900-01-01 00:00:00.000') = '1900-01-01 00:00:00.000'
            SET @NgayBatDau = DATEADD(DD, -1, CONVERT(DATE, GETDATE()));
        IF ISNULL(@NgayKetThuc, '1900-01-01 00:00:00.000') = '1900-01-01 00:00:00.000'
            SET @NgayKetThuc = DATEADD(DD, -1, CONVERT(DATE, GETDATE()));
        IF ISNULL(@NgayDanhSo, '1900-01-01 00:00:00.000') = '1900-01-01 00:00:00.000'
            SET @NgayDanhSo = '2016-01-01';

    
        SELECT  A.* ,
                B.ThanhTienThucChay
        INTO    #KetQua
        FROM    ( SELECT    tcg.NgayThucHien ,
                            hd.HopDongID ,
                            tcg.SoHopDong ,
                            sp.DmSanPhamID ,
                            SUM(tcg.ThanhTienThucChay) ThanhTienThucChayTT
                  FROM      ThucChayGGFBInput tcg
                            INNER JOIN dbo.HopDong hd ON hd.SoHopDong = tcg.SoHopDong
                            LEFT JOIN dbo.DmSanPham sp ON tcg.DmSanPhamREF = sp.TenSanPham
                  WHERE     tcg.NgayThucHien IN (
                            SELECT  MAX(NgayThucHien)
                            FROM    ThucChayGGFBInput gg
                            WHERE   tcg.NgayThucHien BETWEEN @NgayBatDau
                                                     AND     @NgayKetThuc
                                    AND gg.SoHopDong = tcg.SoHopDong
                                    AND gg.DmSanPhamREF = tcg.DmSanPhamREF )
                            AND tcg.DmLoaiBannerREF <> 17
                  GROUP BY  hd.HopDongID ,
                            tcg.SoHopDong ,
                            sp.DmSanPhamID ,
                            tcg.NgayThucHien
                ) A
                LEFT JOIN ( SELECT  A.HopDongID ,
                                    DmSanPhamREF ,
                                    SUM(ThanhTienSauTrietKhauThucChay
                                        + ThanhTienKM + A.ThanhTienLechTreoHa
                                        * ( 1 - A.ChietKhau / 100 )
                                        + A.GiaTriThayDoi) ThanhTienThucChay
                            FROM    dbo.ThucChayDaTinh A
                            WHERE   DmSanPhamREF IN ( 306, 423 )
                                    AND NOT ( DmHinhThucQuangCao = 13
                                              OR DmLoaiBannerREF = 18
                                            )
                                    AND NOT ( DmHinhThucQuangCao = 42 )
                                    AND A.NgayDanhSoHopDong >= @NgayDanhSo
                                    AND A.DmLoaiBannerREF <> 17
                            GROUP BY A.HopDongID ,
                                    DmSanPhamREF
                            HAVING  NOT ( SUM(SoLuongThucChay
                                              + SoLuongThucChayKM
                                              + A.SoLuongThucChayLechTreoHa) = 0
                                          AND SUM(ThanhTienSauTrietKhauThucChay
                                                  + ThanhTienKM
                                                  + A.ThanhTienLechTreoHa
                                                  * ( 1 - A.ChietKhau / 100 )
                                                  + A.GiaTriThayDoi) = 0
                                        )
                          ) B ON B.DmSanPhamREF = A.DmSanPhamID
                                 AND B.HopDongID = A.HopDongID
        WHERE   ABS(ISNULL(A.ThanhTienThucChayTT, 0)
                    - ISNULL(B.ThanhTienThucChay, 0)) > 10;
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
                        dbo.FormatNumber(A.ThanhTienThucChayTT) ThanhTienThucChayTT ,
                        dbo.FormatNumber(A.ThanhTienThucChay) ThanhTienThucChay ,
                        A.IDLoi ,
                        B.TenLoiChiTiet ,
                        B.SPXuLy ,
                        0 TrangThaiXuLy ,
                        GETDATE()
                FROM    ( SELECT    A.NgayThucHien ,
                                    0 DotChayBooking ,
                                    A.HopDongID ,
                                    A.SoHopDong ,
                                    0 HopDongChiTietREF ,
                                    A.DmSanPhamID DmSanPhamREF ,
                                    hd.TenSanPham ,
                                    0 HinhThucQuangCao ,
                                    A.ThanhTienThucChayTT ,
                                    A.ThanhTienThucChay ,
                                    5 IDLoi
                          FROM      #KetQua A
                                    INNER JOIN ( SELECT hdct.HopDongFK ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.TenSanPham ,
                                                        SUM(hdct.ThanhTien) ThanhTien
                                                 FROM   dbo.HopDongChiTiet hdct
                                                        INNER JOIN dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
                                                 WHERE  hd.NgayDanhSoHopDong >= @NgayDanhSo
                                                 GROUP BY hdct.HopDongFK ,
                                                        hdct.DmSanPhamREF ,
                                                        hdct.TenSanPham
                                               ) hd ON A.HopDongID = hd.HopDongFK
                                                       AND hd.DmSanPhamREF = A.DmSanPhamID
                        ) A
                        INNER JOIN KiemSoatThucChay_DanhSachLoi B ON A.IDLoi = B.ID;
    END;

```
