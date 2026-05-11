# Stored Procedure: `sp_CheckDauRaSanPhamCPD_v1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-08-04 10:56:42.600000
- **Ngày sửa cuối**: 2017-08-17 16:11:36.080000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayDanhSo` | `datetime(8)` | No |
| `@NgayBatDau` | `datetime(8)` | No |
| `@NgayKetThuc` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--sp_CheckDauRaSanPhamCPD_v1 '','',''
CREATE PROCEDURE [dbo].[sp_CheckDauRaSanPhamCPD_v1]
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
-- Xác định HĐ phát sinh thực chạy
        SELECT  A.HopDongREF ,
                A.HopDongChiTietREF ,
                A.DmSanPhamREF ,
                SUM(DATEDIFF(DD, A.ThoiGianBatDau, A.ThoiGianKetThuc) + 1) SoNgayChay
        INTO    #HDPhatSinhThucChay
        FROM    ( SELECT DISTINCT
							--ThucChayHopDongChiTietID,
                            HopDongREF ,
                            HopDongChiTietREF ,
                            DmSanPhamREF ,
                            BookingREF ,
                            CASE WHEN ThoiGianBatDau <= @NgayBatDau
                                 THEN @NgayBatDau
                                 WHEN ThoiGianBatDau > @NgayBatDau
                                      AND ThoiGianBatDau <= @NgayKetThuc
                                 THEN ThoiGianBatDau
                            END ThoiGianBatDau ,
                            CASE WHEN ThoiGianKetThuc >= @NgayKetThuc
                                 THEN @NgayKetThuc
                                 WHEN ThoiGianKetThuc <= @NgayKetThuc
                                      AND ThoiGianKetThuc >= @NgayBatDau
                                 THEN ThoiGianKetThuc
                            END ThoiGianKetThuc
                  FROM      dbo.ThucChayHopDongChiTiet
                  WHERE     ( ThoiGianBatDau BETWEEN @NgayBatDau
                                             AND     @NgayKetThuc
                              OR ThoiGianKetThuc BETWEEN @NgayBatDau
                                                 AND     @NgayKetThuc
                              OR ( ThoiGianBatDau <= @NgayBatDau
                                   AND ThoiGianKetThuc >= @NgayKetThuc
                                 )
                            )
                            AND DmSanPhamREF IN ( 140, 228, 564, 549 )
                            AND DeletedStatus = 0
                ) A
                INNER JOIN dbo.HopDong hd ON A.HopDongREF = hd.HopDongID
        WHERE   hd.NgayDanhSoHopDong >= @NgayDanhSo
                AND hd.DeletedStatus = 0
        GROUP BY A.HopDongREF ,
                A.HopDongChiTietREF ,
                A.DmSanPhamREF; 

-- Xác định đơn giá theo ngày
-- B1. Xác định đợt chạy của các hợp đồng
        SELECT  A.HopDongREF ,
                A.HopDongChiTietREF ,
                hdct.DmSanPhamREF ,
                CASE WHEN hdct.ChietKhau = 100 THEN hdct.DonGia
                     ELSE hdct.ThanhTien
                END ThanhTien ,
                SUM(DATEDIFF(DD, A.ThoiGianBatDau, A.ThoiGianKetThuc) + 1) TongSoNgayDuKien ,
                CASE WHEN hdct.ChietKhau = 100 THEN hdct.DonGia
                     ELSE hdct.ThanhTien
                END / SUM(DATEDIFF(DD, A.ThoiGianBatDau, A.ThoiGianKetThuc)
                          + 1) DonGiaTheoNgay
        INTO    #DonGiaTheoNgay
        FROM    dbo.DotChayHopDongChiTiet A
                INNER JOIN ( SELECT DISTINCT
                                    hd.HopDongREF ,
                                    hd.HopDongChiTietREF
                             FROM   #HDPhatSinhThucChay hd
                           ) B ON B.HopDongREF = A.HopDongREF
                                  AND B.HopDongChiTietREF = A.HopDongChiTietREF
                INNER JOIN dbo.HopDongChiTiet hdct ON A.HopDongREF = hdct.HopDongFK
                                                      AND A.HopDongChiTietREF = hdct.HopDongChiTietID
        WHERE   A.DeletedStatus = 0
                AND hdct.DeletedStatus = 0
        GROUP BY A.HopDongREF ,
                A.HopDongChiTietREF ,
                hdct.DmSanPhamREF ,
                CASE WHEN hdct.ChietKhau = 100 THEN hdct.DonGia
                     ELSE hdct.ThanhTien
                END
        ORDER BY HopDongChiTietREF;


        SELECT  ISNULL(A.HopDongREF, B.HopDongID) HopDongREF ,
                ISNULL(A.HopDongChiTietREF, B.HopDongChiTietREF) HopDongChiTietREF ,
                ISNULL(A.DmSanPhamREF, B.DmSanPhamREF) DmSanPhamREF ,
                ISNULL(A.SoNgayChay, 0) SoNgayChay ,
                ISNULL(A.DonGiaTheoNgay, 0) DonGiaTheoNgay ,
                ISNULL(A.ThanhTienThucChayTT, 0) ThanhTienThucChayTT ,
                ISNULL(B.SoLuongThucChay, 0) SoLuongThucChay ,
                ISNULL(B.ThanhTienThucChay, 0) ThanhTienThucChay
        INTO    #KetQua
        FROM    ( SELECT    A.* ,
                            B.DonGiaTheoNgay ,
                            A.SoNgayChay * B.DonGiaTheoNgay ThanhTienThucChayTT
                  FROM      #HDPhatSinhThucChay A
                            LEFT JOIN #DonGiaTheoNgay B ON B.HopDongREF = A.HopDongREF
                                                           AND B.HopDongChiTietREF = A.HopDongChiTietREF
                                                           AND B.DmSanPhamREF = A.DmSanPhamREF
--WHERE   A.HopDongChiTietREF = 509571;
                ) A
                LEFT JOIN ( SELECT  A.HopDongID ,
                                    HopDongChiTietREF ,
                                    DmSanPhamREF ,
                                    SUM(SoLuongThucChay + SoLuongThucChayKM) SoLuongThucChay ,
                                    SUM(ThanhTienSauTrietKhauThucChay
                                        + ThanhTienKM) ThanhTienThucChay
                            FROM    dbo.ThucChayDaTinh A
                                   -- INNER JOIN dbo.HopDong hd ON A.HopDongID = hd.HopDongID
                            WHERE   DmSanPhamREF IN ( 140, 228, 564, 549 )
                                    AND NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
                                    AND NOT ( DmHinhThucQuangCao = 13
                                              OR DmLoaiBannerREF = 18
                                            )
                                    AND NOT ( DmHinhThucQuangCao = 42 )
                                    AND A.NgayDanhSoHopDong >= @NgayDanhSo
                            GROUP BY A.HopDongID ,
                                    HopDongChiTietREF ,
                                    DmSanPhamREF
                            HAVING  NOT ( SUM(SoLuongThucChay
                                              + SoLuongThucChayKM) = 0
                                          AND SUM(ThanhTienSauTrietKhauThucChay
                                                  + ThanhTienKM) = 0
                                        )
                          ) B ON B.DmSanPhamREF = A.DmSanPhamREF
                                 AND B.HopDongChiTietREF = A.HopDongChiTietREF
                                 AND B.HopDongID = A.HopDongREF
        WHERE   ABS(A.ThanhTienThucChayTT - ISNULL(B.ThanhTienThucChay, 0)) > 10
                OR ABS(A.SoNgayChay - ISNULL(B.SoLuongThucChay, 0)) > 0;
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
                        A.HopDongREF ,
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
                                                A.HopDongREF ,
                                                hd.SoHopDong ,
                                                A.HopDongChiTietREF ,
                                                A.DmSanPhamREF ,
                                                hdct.TenSanPham ,
                                                hdct.DmLoaiREF HinhThucQuangCao ,
                                                dbo.FormatNumber(A.SoNgayChay) SoLuongThucChayTT ,
                                                dbo.FormatNumber(A.SoLuongThucChay) SoLuongThucChay ,
                                                1 IDLoi
                                      FROM      #KetQua A
                                                INNER JOIN dbo.HopDong hd ON A.HopDongREF = hd.HopDongID
                                                INNER JOIN dbo.HopDongChiTiet hdct ON A.HopDongChiTietREF = hdct.HopDongChiTietID
                                      WHERE     A.SoLuongThucChay
                                                - A.SoNgayChay <> 0
                                      UNION ALL
                                      SELECT    @NgayBatDau NgayThucHien ,-- Ngày thực hiện, 
                                                '' DotChayBooking ,
                                                A.HopDongREF ,
                                                hd.SoHopDong ,
                                                A.HopDongChiTietREF ,
                                                A.DmSanPhamREF ,
                                                hdct.TenSanPham ,
                                                hdct.DmLoaiREF HinhThucQuangCao ,
                                                dbo.FormatNumber(A.ThanhTienThucChayTT) ThanhTienThucChayTT ,
                                                dbo.FormatNumber(A.ThanhTienThucChay) ThanhTienThucChay ,
                                                2 IDLoi
                                      FROM      #KetQua A
                                                INNER JOIN dbo.HopDong hd ON A.HopDongREF = hd.HopDongID
                                                INNER JOIN dbo.HopDongChiTiet hdct ON A.HopDongChiTietREF = hdct.HopDongChiTietID
                                      WHERE     A.ThanhTienThucChayTT
                                                - A.ThanhTienThucChay <> 0
                                    ) A
                        ) A
                        INNER JOIN KiemSoatThucChay_DanhSachLoi B ON A.IDLoi = B.ID;

    END;
	--sp_CheckDauRaSanPhamCPD_v1 '2015-01-01','2017-07-02','2017-08-02'
```
