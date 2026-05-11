# Stored Procedure: `sp_Check_DuLieuDauVaoSanPhamCPD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-03-07 16:17:06.150000
- **Ngày sửa cuối**: 2017-06-27 10:20:58.803000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayDanhSo` | `datetime(8)` | No |
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--sp_Check_DuLieuDauVaoSanPhamCPD '2017-01-01','2017-05-31','2017-05-31'
CREATE PROCEDURE [dbo].[sp_Check_DuLieuDauVaoSanPhamCPD]
    @NgayDanhSo DATETIME ,
    @FromDate DATETIME ,
    @ToDate DATETIME
AS
    BEGIN
--- Check đơn vị tính của các sản phẩm CPD. Đưa ra những trường hợp có đơn vị tính là đơn vị không phải thời gian
        DELETE  FROM Check_DuLieuDauVaoSanPham
        WHERE   CONVERT(DATE, NgayThucHien) = CONVERT(DATE, GETDATE())
                AND IDLoai = 1;

        SELECT DISTINCT
                hd.HopDongID
        INTO    #HopDongThayDoi
        FROM    dbo.HopDong hd
                INNER JOIN dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
        WHERE   hd.DeletedStatus = 0
                AND hdct.DeletedStatus = 0
                AND hd.TrangThaiHopDong <> 3
                AND hdct.DmSanPhamREF IN ( 140, 228, 564, 549 )
                AND hd.NgayDanhSoHopDong >= @NgayDanhSo
                AND ( CONVERT(DATE, hd.LastModifiedAt) BETWEEN @FromDate
                                                       AND    @ToDate
                      OR CONVERT(DATE, hdct.LastModifiedAt) BETWEEN @FromDate
                                                            AND
                                                              @ToDate
                    );
        INSERT  Check_DuLieuDauVaoSanPham
                ( NgayThucHien ,
                  HopDongREF ,
                  HopDongChiTietREF ,
                  DmSanPhamREF ,
                  DmHinhThucQuangCaoREF_HD ,
                  DmDonViTinhREF ,
                  DonViTinh ,
                  IDLoai ,
                  TenLoai ,
                  IDLyDo ,
                  LyDo ,
                  SoHopDong
                )
                SELECT  A.NgayThucHien ,
                        A.HopDongFK ,
                        A.HopDongChiTietID ,
                        A.DmSanPhamREF ,
                        A.DmHinhThucQuangCaoREF ,
                        A.DonViTinhREF ,
                        A.DonViTinh ,
                        A.IDLoai ,
                        A.TenLoai ,
                        IDLyDo ,
                        B.TenLoiChiTiet ,
                        hd.SoHopDong
                FROM    ( SELECT    GETDATE() NgayThucHien ,
                                    HopDongFK ,
                                    HopDongChiTietID ,
                                    DmSanPhamREF ,
                                    hdct.DmLoaiREF DmHinhThucQuangCaoREF ,
                                    DonViTinhREF ,
                                    DonViTinh ,
                                    1 IDLoai ,
                                    'CPD' TenLoai ,
                                    1 IDLyDo
                          FROM      dbo.HopDongChiTiet hdct
                                    INNER JOIN dbo.HopDong hd ON HopDongID = HopDongFK
                          WHERE     1 = 1
                                    AND DonViTinhREF NOT IN ( 3, 4, 5, 6 )
                                    AND DmSanPhamREF IN ( 140, 228, 564, 549 )
                                    AND hd.DeletedStatus = 0
                                    AND ROUND(ThanhTien, -1)
                                    - ROUND(hdct.ThanhtienThucChay, -1) <> 0
                                    AND TrangThaiHopDong <> 3
                                    AND hdct.DeletedStatus = 0
                                    AND hd.NgayDanhSoHopDong >= @NgayDanhSo
                                    AND NOT ( hdct.DmLoaiREF IN ( 13, 42 )
                                              OR hdct.DmLoaiBannerREF = 18
                                            )
                        ) A
                        INNER JOIN HopDong hd ON A.HopDongFK = hd.HopDongID
                        LEFT JOIN DmLoiKhiCheckDuLieu B ON A.IDLyDo = B.ID
                        INNER JOIN #HopDongThayDoi hdtd ON hdtd.HopDongID = hd.HopDongID;
              
--- Check thời gian chạy giữa hợp đồng và đợt chạy

        INSERT  INTO dbo.Check_DuLieuDauVaoSanPham
                ( NgayThucHien ,
                  HopDongREF ,
                  HopDongChiTietREF ,
                  DmSanPhamREF ,
                  DmDonViTinhREF ,
                  DonViTinh ,
                  SoLuongTrenHD ,
                  SoLuongTrenDotChay ,
                  IDLyDo ,
                  LyDo ,
                  TrangThaiXuLy ,
                  IDLoai ,
                  TenLoai ,
                  GhiChu ,
                  SoHopDong
                )
                SELECT  GETDATE() NgayThucHien ,
                        A.HopDongFK ,
                        A.HopDongChiTietREF ,
                        A.DmSanPhamREF ,
                        A.DonViTinhREF ,
                        A.DonViTinh ,
                        A.SLHopDongTheoNgay ,
                        A.SLNgayChay ,
                        IDLyDo ,
                        TenLoiChiTiet LyDo ,
                        A.TrangThaiXuLy ,
                        A.IDLoai ,
                        B.TenLoai ,
                        A.GhiChu ,
                        hd.SoHopDong
                FROM    ( SELECT    hdct.HopDongFK ,
                                    dchdct.HopDongChiTietREF ,
                                    hdct.DmSanPhamREF ,
                                    hdct.DonViTinhREF ,
                                    hdct.DonViTinh ,
                                    CASE WHEN hdct.DonViTinhREF = 3
                                         THEN hdct.SoLuong
                                         WHEN hdct.DonViTinhREF = 4
                                         THEN SoLuong * 7
                                         WHEN hdct.DonViTinhREF = 5
                                         THEN SoLuong * 30
                                         WHEN hdct.DonViTinhREF = 6
                                         THEN SoLuong * 365
                                    END SLHopDongTheoNgay ,
                                    hdct.GhiChu
                                    + CASE WHEN hdct.GhiChu LIKE '%slot'
                                           THEN N' (Lấy số ngày x số slot mua = SL ngày đợt chạy là OK)'
                                           ELSE ' - ' + hdct.GhiChu
                                      END GhiChu ,
                                    SUM(DATEDIFF(DD, dchdct.ThoiGianBatDau,
                                                 dchdct.ThoiGianKetThuc) + 1) SLNgayChay ,
                                    8 IDLyDo ,
                                    0 TrangThaiXuLy ,
                                    1 IDLoai
                          FROM      dbo.DotChayHopDongChiTiet dchdct
                                    INNER JOIN dbo.HopDongChiTiet hdct ON dchdct.HopDongChiTietREF = hdct.HopDongChiTietID
                                    INNER JOIN #HopDongThayDoi hd ON dchdct.HopDongREF = hd.HopDongID
                          WHERE     hdct.DmSanPhamREF IN ( 140, 228, 564, 549 )
                                    AND hdct.DonViTinhREF IN ( 3, 4, 5, 6 )
                                    AND dchdct.DeletedStatus = 0
                                    AND hdct.DeletedStatus = 0
                                    AND NOT ( hdct.DmLoaiREF IN ( 13, 42 )
                                              OR hdct.DmLoaiBannerREF = 18
                                            )
                          GROUP BY  dchdct.HopDongChiTietREF ,
                                    hdct.DmSanPhamREF ,
                                    hdct.DonViTinhREF ,
                                    hdct.DonViTinh ,
                                    hdct.GhiChu ,
                                    hdct.HopDongFK ,
                                    CASE WHEN hdct.DonViTinhREF = 3
                                         THEN hdct.SoLuong
                                         WHEN hdct.DonViTinhREF = 4
                                         THEN SoLuong * 7
                                         WHEN hdct.DonViTinhREF = 5
                                         THEN SoLuong * 30
                                         WHEN hdct.DonViTinhREF = 6
                                         THEN SoLuong * 365
                                    END
                        ) A
                        INNER JOIN dbo.HopDong hd ON A.HopDongFK = hd.HopDongID
                        LEFT JOIN DmLoiKhiCheckDuLieu B ON A.IDLyDo = B.ID
                WHERE   CASE WHEN A.DonViTinhREF IN ( 3, 4 ) THEN A.SLNgayChay
                        END <> A.SLHopDongTheoNgay
                        OR CASE WHEN A.DonViTinhREF IN ( 5, 5 )
                                THEN ABS(A.SLNgayChay - A.SLHopDongTheoNgay)
                           END > 2
                        AND hd.NgayDanhSoHopDong >= @NgayDanhSo
                        AND hd.DeletedStatus = 0;
------------- Check thời gian giữa đợt chạy và thực chạy

        INSERT  INTO dbo.Check_DuLieuDauVaoSanPham
                ( NgayThucHien ,
                  HopDongREF ,
                  HopDongChiTietREF ,
                  DmSanPhamREF ,
                  BookingREF ,
                  SoLuongTrenDotChay ,
                  SoLuongTrenThucTreo ,
                  IDLyDo ,
                  LyDo ,
                  TrangThaiXuLy ,
                  IDLoai ,
                  TenLoai ,
                  SoHopDong
                )
                SELECT  GETDATE() NgayThucHien ,
                        HopDongREF ,
                        HopDongChiTietREF ,
                        DmSanPhamREF ,
                        BookingREF ,
                        SLNgayDotChay ,
                        SLNgayThucTreo ,
                        IDLyDo ,
                        B.TenLoiChiTiet ,
                        TrangThaiXuLy ,
                        B.ID_Loai ,
                        B.TenLoai ,
                        hd.SoHopDong
                FROM    ( SELECT    ISNULL(A.HopDongREF, B.HopDongREF) HopDongREF ,
                                    ISNULL(A.HopDongChiTietREF,
                                           B.HopDongChiTietREF) HopDongChiTietREF ,
                                    ISNULL(A.DmSanPhamREF, B.DmSanPhamREF) DmSanPhamREF ,
                                    ISNULL(A.BookingREF, B.BookingREF) BookingREF ,
                                    ISNULL(SLNgayDotChay, 0) SLNgayDotChay ,
                                    ISNULL(SLNgayThucTreo, 0) SLNgayThucTreo ,
                                    CASE WHEN SLNgayDotChay IS NULL THEN 9
                                         WHEN A.SLNgayThucTreo IS NULL THEN 10
                                         ELSE 11
                                    END IDLyDo ,
                                    0 TrangThaiXuLy ,
                                    1 IDLoai
                          FROM      ( SELECT    A.HopDongREF ,
                                                A.HopDongChiTietREF ,
                                                A.DmSanPhamREF ,
                                                A.BookingREF ,
                                                SUM(DATEDIFF(DD,
                                                             A.ThoiGianBatDau,
                                                             A.ThoiGianKetThuc)
                                                    + 1) SLNgayThucTreo
                                      FROM      ( SELECT DISTINCT
                                                            HopDongREF ,
                                                            HopDongChiTietREF ,
                                                            hdct.DmSanPhamREF ,
                                                            BookingREF ,
                                                            tchdct.ThoiGianBatDau ThoiGianBatDau ,
                                                            tchdct.ThoiGianKetThuc ThoiGianKetThuc
                                                  FROM      dbo.ThucChayHopDongChiTiet tchdct
                                                            INNER JOIN dbo.HopDongChiTiet hdct ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
                                                            INNER JOIN #HopDongThayDoi hd ON tchdct.HopDongREF = hd.HopDongID
                                                  WHERE     hdct.DmSanPhamREF IN (
                                                            140, 228, 564, 549 )
                                                            AND hdct.DeletedStatus = 0
                                                            AND tchdct.DeletedStatus = 0
                                                            AND NOT ( hdct.DmLoaiREF IN (
                                                              13, 42 )
                                                              OR hdct.DmLoaiBannerREF = 18
                                                              )
                                                ) A
                                      WHERE     A.ThoiGianBatDau IS NOT NULL
                                                OR A.ThoiGianKetThuc IS NOT NULL
                                      GROUP BY  A.HopDongChiTietREF ,
                                                A.BookingREF ,
                                                A.HopDongREF ,
                                                A.DmSanPhamREF
                                    ) A
                                    FULL JOIN ( SELECT  A.HopDongREF ,
                                                        A.HopDongChiTietREF ,
                                                        A.DmSanPhamREF ,
                                                        A.BookingREF ,
                                                        SUM(DATEDIFF(DD,
                                                              A.ThoiGianBatDau,
                                                              A.ThoiGianKetThuc)
                                                            + 1) SLNgayDotChay
                                                FROM    ( SELECT DISTINCT
                                                              HopDongREF ,
                                                              HopDongChiTietREF ,
                                                              hdct.DmSanPhamREF ,
                                                              BookingREF ,
                                                              dchdct.ThoiGianBatDau ThoiGianBatDau ,
                                                              dchdct.ThoiGianKetThuc ThoiGianKetThuc
                                                          FROM
                                                              dbo.DotChayHopDongChiTiet dchdct
                                                              INNER JOIN dbo.HopDongChiTiet hdct ON dchdct.HopDongChiTietREF = hdct.HopDongChiTietID
                                                              INNER JOIN #HopDongThayDoi hd ON dchdct.HopDongREF = hd.HopDongID
                                                          WHERE
                                                              hdct.DmSanPhamREF IN (
                                                              140, 228, 564,
                                                              549 )
                                                              AND dchdct.DeletedStatus = 0
                                                              AND hdct.DeletedStatus = 0
                                                              AND NOT ( hdct.DmLoaiREF IN (
                                                              13, 42 )
                                                              OR hdct.DmLoaiBannerREF = 18
                                                              )
                                                        ) A
                                                WHERE   A.ThoiGianBatDau IS NOT NULL
                                                        OR A.ThoiGianKetThuc IS NOT NULL
                                                GROUP BY A.HopDongChiTietREF ,
                                                        A.BookingREF ,
                                                        A.HopDongREF ,
                                                        A.DmSanPhamREF
                                              ) B ON B.BookingREF = A.BookingREF
                                                     AND B.HopDongChiTietREF = A.HopDongChiTietREF
                                                     AND B.HopDongREF = A.HopDongREF
                                                     AND B.DmSanPhamREF = A.DmSanPhamREF
                          WHERE     ISNULL(A.SLNgayThucTreo, 0)
                                    - ISNULL(B.SLNgayDotChay, 0) <> 0
                                    AND ISNULL(A.SLNgayThucTreo, 0) > 0
                        ) A
                        INNER JOIN dbo.HopDong hd ON A.HopDongREF = hd.HopDongID
                        LEFT JOIN DmLoiKhiCheckDuLieu B ON A.IDLyDo = B.ID
                WHERE   hd.NgayDanhSoHopDong >= @NgayDanhSo
                        AND hd.DeletedStatus = 0;

        DECLARE @Table TABLE
            (
              NgayThucHien DATETIME ,
              HopDongID INT ,
              SoHopDong NVARCHAR(50) ,
              HopDongChiTietID INT ,
              BookingREF INT ,
              DmSanPhamREF INT ,
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
              CheckedStatus INT ,
              NguyenNhan NVARCHAR(MAX)
            );
        EXEC [ThucChay_HopDongChiTietAndBannerCPD] @FromDate;
        DECLARE @NgayThucHien DATETIME;
        SET @NgayThucHien = @FromDate;
     
        WHILE ( @NgayThucHien <= @ToDate )
            BEGIN
	--//-----------CPD CO DOT CHAY----------------------------------
	-------------DOI CHIEU DATA GIUA HD- SP - THUCTREO ---------------------
                INSERT  INTO @Table
                        SELECT  @NgayThucHien ,
                                ISNULL(ISNULL(HD.HopDongID, SP.HopDongID),
                                       ThucTreo.HopDongREF) HopDongID ,
                                ISNULL(ISNULL(HD.SoHopDong, SP.SoHopDong),
                                       ThucTreo.SoHopDong) SoHopDong ,
                                ISNULL(HD.HopDongChiTietID,
                                       ThucTreo.HopDongChiTietREF) ThucTreo ,
                                ISNULL(ISNULL(HD.BookingREF,
                                              ThucTreo.BookingREF),
                                       SP.DanhsachDmBookingREF) BookingREF ,
                                ISNULL(ISNULL(HD.DmSanPhamREF,
                                              ThucTreo.DmSanPhamREF),
                                       SP.DmSanPhamREF) DmSanPhamREF ,
                                HD.ThoiGianBatDau ,
                                HD.ThoiGianKetThuc ,
                                ThucTreo.HopDongREF ,
                                ThucTreo.HopDongChiTietREF ,
                                ISNULL(ThucTreo.DmBannerID, SP.DmBannerREF) DmBannerID ,
                                ThucTreo.BookingREF ,
                                SP.SoHopDong ,
                                SP.DanhsachDmBookingREF ,
                                SP.DmBannerREF ,
                                SP.TongViewThucChay AS ttv ,
                                CASE WHEN HD.HopDongID IS NOT NULL
                                          AND ThucTreo.HopDongREF IS NULL
                                          AND SP.SoHopDong IS NULL THEN 2
                                     WHEN HD.HopDongID IS NOT NULL
                                          AND ThucTreo.HopDongREF IS NULL
                                          AND SP.SoHopDong IS NOT NULL THEN 3
                                     WHEN HD.HopDongID IS NOT NULL
                                          AND ThucTreo.HopDongREF IS NOT NULL
                                          AND SP.SoHopDong IS NULL THEN 4
                                     WHEN HD.HopDongID IS NULL
                                          AND ThucTreo.HopDongREF IS NULL
                                          AND SP.SoHopDong IS NOT NULL THEN 5
                                     WHEN HD.HopDongID IS NULL
                                          AND ThucTreo.HopDongREF IS NOT NULL
                                          AND SP.SoHopDong IS NULL THEN 6
                                     WHEN HD.HopDongID IS NULL
                                          AND ThucTreo.HopDongREF IS NOT NULL
                                          AND SP.SoHopDong IS NOT NULL THEN 7
                                     ELSE 0
                                END ID_LyDo ,
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
                                END NguyenNhan
                        FROM    ( SELECT DISTINCT
                                            tchdctab.ThucChayHopDongChiTietID ,
                                            tchdctab.HopDongREF ,
                                            HD.SoHopDong ,
                                            tchdctab.HopDongChiTietREF ,
                                            hdct.DmSanPhamREF ,
                                            tchdctab.DmBannerID ,
                                            tchdctab.BookingREF
                                  FROM      ThucChayHopDongChiTietAndBannerCPD tchdctab
                                            INNER JOIN HopDongChiTiet hdct ON tchdctab.HopDongChiTietREF = hdct.HopDongChiTietID
                                                              AND hdct.DeletedStatus = 0
                                                              AND tchdctab.DeletedStatus = 0
                                            INNER JOIN dbo.HopDong HD ON HD.HopDongID = HopDongREF
                                  WHERE     hdct.DmSanPhamREF IN ( 140, 228,
                                                              564, 549 )
                                            AND @NgayThucHien BETWEEN tchdctab.ThoiGianBatDau
                                                              AND
                                                              tchdctab.ThoiGianKetThuc
                                            AND NOT ( hdct.DmLoaiREF IN ( 13,
                                                              42 )
                                                      OR hdct.DmLoaiBannerREF = 18
                                                    )
                                ) ThucTreo
                                FULL OUTER JOIN ( SELECT    hd2.HopDongID ,
                                                            ptcts.SoHopDong ,
                                                            ptcts.DmSanPhamREF ,
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
                                                            hdct.DmSanPhamREF ,
                                                            hdct.TenSanPham ,
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
                                                              AND NOT ( hdct.DmLoaiREF IN (
                                                              13, 42 )
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
                                                        AND ThucTreo.HopDongChiTietREF = HD.HopDongChiTietID; 	
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien);
            END;
        INSERT  INTO dbo.Check_DuLieuDauVaoSanPham
                ( NgayThucHien ,
                  HopDongREF ,
                  SoHopDong ,
                  HopDongChiTietREF ,
                  DmBannerREF ,
                  BookingREF ,
                  DmSanPhamREF ,
                  ThoiGianBatDauHD ,
                  ThoiGianKetThucHD ,
                  IDLyDo ,
                  LyDo ,
                  TrangThaiXuLy ,
                  IDLoai ,
                  TenLoai ,
                  CreatedAt
			    )
                SELECT  NgayThucHien ,
                        HopDongID ,
                        SoHopDong ,
                        HopDongChiTietID ,
                        DmBannerID_Thuctreo ,
                        BookingREF ,
                        t.DmSanPhamREF ,
                        ThoiGianBD ,
                        ThoiGianKT ,
                        t.CheckedStatus ,
                        b.TenLoiChiTiet ,
                        0 ,
                        b.ID_Loai ,
                        b.TenLoai ,
                        GETDATE()
                FROM    @Table t
                        LEFT JOIN dbo.DmLoiKhiCheckDuLieu b ON t.CheckedStatus = b.ID
                WHERE   CheckedStatus <> 0;
    END;

```
