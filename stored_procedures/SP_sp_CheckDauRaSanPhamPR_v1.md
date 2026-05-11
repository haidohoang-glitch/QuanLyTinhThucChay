# Stored Procedure: `sp_CheckDauRaSanPhamPR_v1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-08-16 11:46:30.673000
- **Ngày sửa cuối**: 2017-08-17 16:11:11.853000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayDanhSo` | `datetime(8)` | No |
| `@NgayBatDau` | `datetime(8)` | No |
| `@NgayKetThuc` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--sp_CheckDauRaSanPhamPR_v1 '2016-01-01','2017-07-01','2017-08-10'
CREATE PROCEDURE [dbo].[sp_CheckDauRaSanPhamPR_v1]
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
        SELECT DISTINCT
                hd.HopDongID
        INTO    #HopDongPhatSinhTC
        FROM    dbo.ThucChayHopDongChiTietPR pr
                INNER JOIN dbo.HopDong hd ON hd.HopDongID = pr.HopDongREF
        WHERE   CONVERT(DATE, pr.LastModifiedAt) BETWEEN @NgayBatDau
                                                 AND     @NgayKetThuc
                AND DmSanPhamREF IN ( 141, 637, 305 )
                AND hd.DeletedStatus = 0
                AND pr.DeletedStatus = 0
                AND hd.TrangThaiHopDong <> 3; 
        SELECT  A.* ,
                ISNULL(B.SoLuongThucChay, 0) SoLuongThucChay ,
                ISNULL(B.ThanhTienThucChay, 0) ThanhTienThucChay
        INTO    #KetQua
        FROM    ( SELECT    hd.HopDongID ,
                            pr.DmSanPhamREF ,
                            pr.DmHinhThucQuangCaoREF ,
                            pr.ThucChayHopDongChiTietPRID DotChayBooking ,
                            ISNULL(map.DmWebsiteReportingdbID, pr.DmWebsiteREF) DmWebsiteREF ,
                            SUM(pr.SoLuong) SoLuongTT ,
                            SUM(CASE WHEN pr.ChietKhau = 100 THEN pr.GiaTien
                                     ELSE CONVERT(FLOAT, GiaTien * SoLuong)
                                          * ( 100 - ChietKhau ) / 100
                                END) ThanhTienThucChayTT ,
                            pr.RecordStatus
                  FROM      dbo.ThucChayHopDongChiTietPR pr
                            INNER JOIN dbo.HopDong hd ON hd.HopDongID = pr.HopDongREF
                            INNER JOIN #HopDongPhatSinhTC pstc ON pstc.HopDongID = hd.HopDongID
                            LEFT JOIN WebsiteMapping_HDCN_Reporting map ON pr.DmWebsiteREF = map.DmWebsiteID
                  WHERE     CONVERT(DATE, pr.LastModifiedAt) BETWEEN @NgayBatDau
                                                             AND
                                                              @NgayKetThuc
                            AND DmSanPhamREF IN ( 141, 637, 305 )
                            AND hd.DeletedStatus = 0
                            AND pr.DeletedStatus = 0
                            AND hd.TrangThaiHopDong <> 3
                            AND hd.NgayDanhSoHopDong >= @NgayDanhSo
                  GROUP BY  hd.HopDongID ,
                            pr.DmSanPhamREF ,
                            pr.DmHinhThucQuangCaoREF ,
                            pr.ThucChayHopDongChiTietPRID ,
                            ISNULL(map.DmWebsiteReportingdbID, pr.DmWebsiteREF) ,
                            pr.RecordStatus ,
                            pr.ChietKhau
                ) A
                LEFT JOIN ( SELECT  tcdt.HopDongID ,
                                    tcdt.DmSanPhamREF ,
                                    tcdt.DmHinhThucQuangCao DmHinhThucQuangCaoREF ,
                                    tcdt.DotChayBooking ,
                                    tcdt.DmWebsiteREF ,
                                    SUM(SoLuongThucChay + SoLuongThucChayKM
                                        + tcdt.SoLuongThayDoi) SoLuongThucChay ,
                                    SUM(ThanhTienSauTrietKhauThucChay
                                        + ThanhTienKM + tcdt.GiaTriThayDoi) ThanhTienThucChay
                            FROM    dbo.ThucChayDaTinh tcdt
                                    INNER JOIN #HopDongPhatSinhTC pstc ON pstc.HopDongID = tcdt.HopDongID
                            WHERE   DmSanPhamREF IN ( 141, 637, 305 )
                                    AND ( tcdt.DmHinhThucQuangCao NOT IN ( 13,
                                                              42 )
                                          OR tcdt.DmLoaiBannerREF <> 18
                                        )
                                    AND tcdt.TrangThaiHopDong <> 3
                                    AND tcdt.NgayThucHien <= @NgayKetThuc
                                    AND tcdt.NgayDanhSoHopDong >= @NgayDanhSo
									--AND tcdt.GiaTriThayDoi 
                            GROUP BY tcdt.HopDongID ,
                                    tcdt.SoHopDong ,
                                    tcdt.DmSanPhamREF ,
                                    tcdt.DmHinhThucQuangCao ,
                                    tcdt.DotChayBooking ,
                                    tcdt.DmWebsiteREF
                          ) B ON B.DmHinhThucQuangCaoREF = A.DmHinhThucQuangCaoREF
                                 AND B.DmSanPhamREF = A.DmSanPhamREF
                                 AND B.DmWebsiteREF = A.DmWebsiteREF
                                 AND B.DotChayBooking = A.DotChayBooking
                                 AND B.HopDongID = A.HopDongID
        WHERE   ABS(A.ThanhTienThucChayTT - ISNULL(B.ThanhTienThucChay, 0)) > 10
                OR ABS(A.SoLuongTT - ISNULL(B.SoLuongThucChay, 0)) > 0;

        --SELECT  A.HopDongID ,
        --        hd.SoHopDong ,
        --        0 HopDongChiTietREF ,
        --        A.DmSanPhamREF ,
        --        sp.TenSanPham ,
        --        A.DmHinhThucQuangCaoREF DmHinhThucQuangCaoREF ,
        --        A.DotChayBooking ,
        --        0 ThanhTienHD ,
        --        0 ThucChayTong ,
        --        A.SoLuongThucChay ,
        --        A.SoLuongTT SoLuongThucChayTT ,
        --        A.SoLuongThucChay - A.SoLuongTT SoLuongLech ,
        --        A.ThanhTienThucChay ,
        --        A.ThanhTienThucChayTT ,
        --        A.ThanhTienThucChay - A.ThanhTienThucChayTT GiaTriLech ,
        --        A.RecordStatus
        --FROM    #KetQua A
        --        INNER JOIN dbo.HopDong hd ON A.HopDongID = hd.HopDongID
        --        LEFT JOIN dbo.DmSanPham sp ON A.DmSanPhamREF = sp.DmSanPhamID;
       

        --SELECT  @NgayBatDau NgayThucHien ,-- Ngày thực hiện, 
        --        A.DotChayBooking DotChayBooking ,
        --        A.HopDongID ,
        --        hd.SoHopDong ,
        --        0 HopDongChiTietREF ,
        --        A.DmSanPhamREF ,
        --        sp.TenSanPham ,
        --        DmHinhThucQuangCaoREF HinhThucQuangCao ,
        --        dbo.FormatNumber(A.SoLuongTT) SoLuongThucChayTT ,
        --        dbo.FormatNumber(A.SoLuongThucChay) SoLuongThucChay ,
        --        10 IDLoi
        --FROM    #KetQua A
        --        INNER JOIN dbo.HopDong hd ON A.HopDongID = hd.HopDongID
        --        LEFT JOIN dbo.DmSanPham sp ON A.DmSanPhamREF = sp.DmSanPhamID
        --WHERE   A.SoLuongThucChay - A.SoLuongTT <> 0;



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
                                                A.DotChayBooking DotChayBooking ,
                                                A.HopDongID ,
                                                hd.SoHopDong ,
                                                0 HopDongChiTietREF ,
                                                A.DmSanPhamREF ,
                                                sp.TenSanPham ,
                                                DmHinhThucQuangCaoREF HinhThucQuangCao ,
                                                dbo.FormatNumber(A.SoLuongTT) SoLuongThucChayTT ,
                                                dbo.FormatNumber(A.SoLuongThucChay) SoLuongThucChay ,
                                                11 IDLoi
                                      FROM      #KetQua A
                                                INNER JOIN dbo.HopDong hd ON A.HopDongID = hd.HopDongID
                                                LEFT JOIN dbo.DmSanPham sp ON A.DmSanPhamREF = sp.DmSanPhamID
                                      WHERE     A.SoLuongThucChay
                                                - A.SoLuongTT <> 0
                                      UNION ALL
                                      SELECT    @NgayBatDau NgayThucHien ,-- Ngày thực hiện, 
                                                A.DotChayBooking DotChayBooking ,
                                                A.HopDongID ,
                                                hd.SoHopDong ,
                                                0 HopDongChiTietREF ,
                                                A.DmSanPhamREF ,
                                                sp.TenSanPham ,
                                                DmHinhThucQuangCaoREF HinhThucQuangCao ,
                                                dbo.FormatNumber(A.ThanhTienThucChayTT) ThanhTienThucChayTT ,
                                                dbo.FormatNumber(A.ThanhTienThucChay) ThanhTienThucChay ,
                                                12 IDLoi
                                      FROM      #KetQua A
                                                INNER JOIN dbo.HopDong hd ON A.HopDongID = hd.HopDongID
                                                LEFT JOIN dbo.DmSanPham sp ON A.DmSanPhamREF = sp.DmSanPhamID
                                      WHERE     A.ThanhTienThucChay
                                                - A.ThanhTienThucChayTT <> 0
                                    ) A
                        ) A
                        INNER JOIN KiemSoatThucChay_DanhSachLoi B ON A.IDLoi = B.ID;


    END;
	--sp_CheckDauRaSanPhamCPD_v1 '2015-01-01','2017-07-02','2017-08-02'
```
