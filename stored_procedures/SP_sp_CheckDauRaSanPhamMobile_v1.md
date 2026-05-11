# Stored Procedure: `sp_CheckDauRaSanPhamMobile_v1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-28 15:46:18.313000
- **Ngày sửa cuối**: 2017-09-28 15:49:08.813000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayDanhSo` | `datetime(8)` | No |
| `@NgayBatDau` | `datetime(8)` | No |
| `@NgayKetThuc` | `datetime(8)` | No |

## Definition (Source Code)

```sql
 --sp_CheckDauRaSanPhamMobile_v1 '2016-01-01','2017-09-25','2017-09-25'
CREATE PROCEDURE [dbo].[sp_CheckDauRaSanPhamMobile_v1]
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
        WHERE   hd.DmSanPhamREF IN ( 339, 240, 370, 598, 613, 680, 732, 735 )
                AND ABS(hd.ThanhtienThucChay - hd.ThanhTien) < 10;
-- Xác định phân bổ chạy sản phẩm admatic 
        SELECT DISTINCT
                HopDongChiTietREF
        INTO    #HopDongAdmatic
        FROM    dbo.ThucChayHopDongChiTietAndBanner_Admatic;

 

        SELECT DISTINCT
                hd.HopDongID ,
                hd.SoHopDong
        INTO    #HopDongPhatSinh
        FROM    dbo.ThucChay tc
                INNER JOIN dbo.HopDong hd ON hd.SoHopDong = tc.SoHopDong
        WHERE   NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
                AND TypeProduct = 10
                AND hd.DeletedStatus = 0
                AND tc.DeletedStatus = 0;
 --Check những hợp đồng chạy xong
 --SELECT A.HopDongID ,
 --       hd.GiaTriHopDong / 1.1 GiaTriHopDong ,
 --       SUM(A.ThanhTienSauTrietKhauThucChay + A.GiaTriThayDoi) DsThucChay
 --FROM   dbo.ThucChayDaTinh A
 --       INNER JOIN #HopDongPhatSinh B ON B.HopDongID = A.HopDongID
 --       LEFT JOIN dbo.HopDong hd ON A.HopDongID = hd.HopDongID
 --WHERE  A.NgayThucHien < @NgayBatDau
 --GROUP BY A.HopDongID ,
 --       hd.GiaTriHopDong
 --HAVING ABS(hd.GiaTriHopDong / 1.1 - SUM(A.ThanhTienSauTrietKhauThucChay
 --                                        + A.GiaTriThayDoi)) < 10;
--

        SELECT DISTINCT
                ct.HopDongID ,
                HopDongChiTietREF ,
                tt.DmBannerREF DmBannerREF ,
                tt.ThoiGianBatDau ,
                tt.ThoiGianKetThuc ,
                ct.DonViTinh ,
                ct.SoLuong ,
                ct.DonGia ,
                ct.ChietKhau ,
                ct.ThanhTien ,
                ct.CreatedAt
        INTO    #PhanBo_Banner
        FROM    ThucChayHopDongChiTiet tt
                INNER JOIN #HopDongPhatSinh hdps ON tt.HopDongREF = hdps.HopDongID
                INNER JOIN ( SELECT HopDongID ,
                                    HopDongChiTietID ,
                                    DonViTinh ,
                                    SoLuong ,
                                    DonGia ,
                                    ChietKhau ,
                                    ThanhTien ,
                                    hdct.CreatedAt
                             FROM   HopDong hd
                                    INNER JOIN HopDongChiTiet hdct ON HopDongID = HopDongFK
                             WHERE  TrangThaiHopDong <> 3
                                    AND hdct.DeletedStatus = 0
                                    AND DmSanPhamREF = 342
                                    AND hdct.DonViTinhREF NOT IN ( 12, 10, 19,
                                                              22, 18 )
                           ) ct ON ct.HopDongChiTietID = tt.HopDongChiTietREF
        WHERE   tt.DeletedStatus = 0 --AND tt.CreatedAt>='2017-01-01'
        ORDER BY HopDongChiTietREF DESC ,
                ct.CreatedAt;
-- 1. Xác định 1 banner chạy trên nhiều hợp đồng chi tiết

        SELECT  COUNT(A.HopDongChiTietREF) SL ,
                A.DmBannerREF
        INTO    #BannerNhieuPhanBo
        FROM    #PhanBo_Banner A
        GROUP BY A.DmBannerREF
        HAVING  COUNT(A.HopDongChiTietREF) > 1; 

-- 2. Xác định thực chạy trả về đối với các hợp đồng phát sinh (Có 1 banner chạy trên 1 phân bổ)
        SELECT  hd.HopDongID ,
                B.HopDongChiTietREF ,
                tc.NgayThucHien ,
                B.DonViTinh ,
                B.SoLuong ,
                B.DonGia ,
                B.ChietKhau ,
                B.ThanhTien ,
                SUM(CASE WHEN B.DonViTinh = 'CPM' THEN tc.TongViewThucChay
                         ELSE tc.TongClickThucChay
                    END) SLThucChay ,
                SUM(CASE WHEN B.DonViTinh = 'CPM'
                         THEN tc.TongViewThucChay / 1000
                         ELSE tc.TongClickThucChay
                    END) * ( 100 - B.ChietKhau ) / 100 * B.DonGia ThanhTienThucChay
        INTO    #ThucChayTuTinh
        FROM    dbo.ThucChay tc
                INNER JOIN dbo.HopDong hd ON hd.SoHopDong = tc.SoHopDong -- Lấy thông tin hợp đồng ID
                INNER JOIN #PhanBo_Banner B ON tc.DmBannerREF = B.DmBannerREF -- Lấy thông tin phân bổ
        WHERE   NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
                AND TypeProduct = 10
                AND hd.DeletedStatus = 0
                AND tc.DeletedStatus = 0
        --AND B.HopDongChiTietREF = 513413
                AND tc.DmBannerREF NOT IN ( SELECT  DmBannerREF
                                            FROM    #BannerNhieuPhanBo )  -- Loại bỏ những banner chạy trên nhiều phân bổ để tính sau
        GROUP BY hd.HopDongID ,
                B.HopDongChiTietREF ,
                tc.NgayThucHien ,
                B.DonViTinh ,
                B.SoLuong ,
                B.DonGia ,
                B.ChietKhau ,
                B.ThanhTien;
-- Trường hợp 1 banner trên 1 phân bổ (1:1)

--tt.NgayThucHien ,
--                tt.HopDongID ,
--                tt.HopDongChiTietREF ,
--                tt.DmSanPhamREF ,
--                tt.ThanhTienHopDong ,
--                tt.DonViTinhREF ,
--                tt.DonViTinh ,
--                tt.SoLuongThucChayTT ,
--                tt.ThanhTienThucChayTT ,
--                TTDT.SoLuongThucChay ,
--                TTDT.ThanhTienThucChay


        SELECT  A.NgayThucHien ,
                A.HopDongID ,
                A.HopDongChiTietREF ,
                342 DmSanPhamREF ,
                A.ThanhTien ThanhTienHopDong ,
                CASE WHEN A.DonViTinh = 'CPM' THEN 1
                     ELSE 2
                END DonViTinhREF ,
                A.DonViTinh ,
                A.SLThucChay SoLuongThucChayTT ,
                A.ThanhTienThucChay ThanhTienThucChayTT ,
                B.SoluongThucChay ,
                B.DsThucChay ThanhTienThucChay
				INTO #KetQua
        FROM    #ThucChayTuTinh A
                LEFT JOIN ( SELECT  HopDongID ,
                                    HopDongChiTietREF ,
                                    NgayThucHien ,
                                    SUM(ThanhTienSauTrietKhauThucChay
                                        + GiaTriThayDoi + ThanhTienLechTreoHa) DsThucChay ,
                                    SUM(SoLuongThucChay + SoLuongThayDoi
                                        + SoLuongThucChayLechTreoHa) SoluongThucChay
                            FROM    dbo.ThucChayDaTinh A
                            WHERE   1 = 1
                                    AND NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
                                    AND DmSanPhamREF = 342
                                    AND A.NgayDanhSoHopDong >= @NgayDanhSo
                            GROUP BY HopDongChiTietREF ,
                                    NgayThucHien ,
                                    HopDongID
                          ) B ON A.HopDongID = B.HopDongID
                                 AND B.HopDongChiTietREF = A.HopDongChiTietREF
                                 AND B.NgayThucHien = A.NgayThucHien
        WHERE   ABS(A.SLThucChay - ISNULL(B.SoluongThucChay, 0)) > 2
                OR ABS(A.ThanhTienThucChay - ISNULL(B.DsThucChay, 0)) > 20
        ORDER BY A.HopDongID ,
                A.HopDongChiTietREF ,
                A.NgayThucHien;
       


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
                        B.SPXuly ,
                        0 TrangThaiXuLy ,
                        GETDATE()-- Ngày tạo
                FROM    ( SELECT    *
                          FROM      ( SELECT    A.NgayThucHien ,-- Ngày thực hiện, 
                                                '' DotChayBooking ,
                                                A.HopDongID ,
                                                hd.SoHopDong ,
                                                A.HopDongChiTietREF ,
                                                A.DmSanPhamREF ,
                                                hdct.TenSanPham ,
                                                hdct.DmLoaiREF HinhThucQuangCao ,
                                                dbo.FormatNumber(A.SoLuongThucChayTT) SoLuongThucChayTT ,
                                                dbo.FormatNumber(A.SoluongThucChay) SoLuongThucChay ,
                                                19 IDLoi
                                      FROM      #KetQua A
                                                INNER JOIN dbo.HopDong hd ON A.HopDongID = hd.HopDongID
                                                INNER JOIN dbo.HopDongChiTiet hdct ON A.HopDongChiTietREF = hdct.HopDongChiTietID
                                      WHERE     ABS(A.SoluongThucChay
                                                    - A.SoLuongThucChayTT) > 10
                                      UNION ALL
                                      SELECT    A.NgayThucHien ,-- Ngày thực hiện, 
                                                '' DotChayBooking ,
                                                A.HopDongID ,
                                                hd.SoHopDong ,
                                                A.HopDongChiTietREF ,
                                                A.DmSanPhamREF ,
                                                hdct.TenSanPham ,
                                                hdct.DmLoaiREF HinhThucQuangCao ,
                                                dbo.FormatNumber(A.ThanhTienThucChayTT) ThanhTienThucChayTT ,
                                                dbo.FormatNumber(A.ThanhTienThucChay) ThanhTienThucChay ,
                                                20 IDLoi
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
