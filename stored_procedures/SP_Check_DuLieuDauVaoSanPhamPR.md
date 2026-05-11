# Stored Procedure: `Check_DuLieuDauVaoSanPhamPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-04-11 15:22:02.303000
- **Ngày sửa cuối**: 2017-06-27 10:18:15.490000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayDanhSo` | `datetime(8)` | No |
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--[Check_DuLieuDauVaoSanPhamPR] '2017-01-01','2017-01-01','2017-04-19'
CREATE PROCEDURE [dbo].[Check_DuLieuDauVaoSanPhamPR]
    @NgayDanhSo DATETIME ,
    @FromDate DATETIME ,
    @ToDate DATETIME
AS
    BEGIN 
--- Check thêm trường hợp đối với hđ vừa ký gói vừa ký theo site



----------------

---- Xác định những hđ ký với website blanks
        DELETE  FROM dbo.Check_DuLieuDauVaoSanPham
        WHERE   CONVERT(DATE, NgayThucHien) = CONVERT(DATE, GETDATE())
                AND IDLoai = 3
                AND IDLyDo = 21
        DELETE  FROM dbo.Check_DuLieuDauVaoSanPham
        WHERE   CONVERT(DATE, NgayThucHien) = CONVERT(DATE, GETDATE())
                AND IDLoai = 3
                AND IDLyDo = 22
        DELETE  FROM dbo.Check_DuLieuDauVaoSanPham
        WHERE   CONVERT(DATE, NgayThucHien) = CONVERT(DATE, GETDATE())
                AND IDLoai = 3
                AND IDLyDo = 23


        SELECT  hd.HopDongID
        INTO    #HopDongBlanks
        FROM    dbo.HopDong hd
                INNER JOIN dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
        WHERE   ( hd.NgayDanhSoHopDong >= @NgayDanhSo
                  OR hd.LastModifiedAt BETWEEN @FromDate AND @ToDate
                )
                AND hdct.DmSanPhamREF IN ( 141, 305, 637 )
                AND hd.DeletedStatus = 0
                AND hdct.DeletedStatus = 0
                AND hd.TrangThaiHopDong <> 3
                AND hdct.DmWebsiteREF IN ( 265 )
		-- Chiết khấu------------
        SELECT DISTINCT
                HopDongFK ,
                hd.SoHopDong ,
                DmLoaiREF ,
                DmSanPhamREF ,
                ChietKhau
        INTO    #HopDongPhatSinh
        FROM    dbo.HopDong hd
                INNER JOIN dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
        WHERE   ( hd.NgayDanhSoHopDong >= @NgayDanhSo
                  OR hd.LastModifiedAt BETWEEN @FromDate AND @ToDate
                )
                AND hdct.DmSanPhamREF IN ( 141, 305, 637 )
                AND hd.DeletedStatus = 0
                AND hdct.DeletedStatus = 0
                AND hd.TrangThaiHopDong <> 3
        --AND hd.HopDongID NOT IN ( SELECT    *
        --                          FROM      #HopDongBlanks )
                AND NOT ( hdct.DmLoaiREF IN( 13,42)
                          OR hdct.DmLoaiBannerREF = 18
                        )


        SELECT DISTINCT
                HopDongREF ,
                DmHinhThucQuangCaoREF ,
                A.DmSanPhamREF ,
                A.ChietKhau
        INTO    #ThucTreoPR
        FROM    dbo.ThucChayHopDongChiTietPR A
                INNER JOIN #HopDongPhatSinh B ON A.HopDongREF = B.HopDongFK
        WHERE   A.DeletedStatus = 0
		---------- 
		---------Website--------------
        SELECT DISTINCT
                HopDongFK ,
				hd.SoHopDong,
                DmLoaiREF ,
                DmSanPhamREF ,
                hdct.DmWebsiteREF
        INTO    #HopDongPhatSinh_W
        FROM    dbo.HopDong hd
                INNER JOIN dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
        WHERE   ( hd.NgayDanhSoHopDong >= @NgayDanhSo
                  OR hd.LastModifiedAt BETWEEN @FromDate AND @ToDate
                )
                AND hdct.DmSanPhamREF IN ( 141, 305, 637 )
                AND hd.DeletedStatus = 0
                AND hdct.DeletedStatus = 0
                AND hd.TrangThaiHopDong <> 3
                AND hd.HopDongID NOT IN ( SELECT    *
                                          FROM      #HopDongBlanks )
                AND NOT ( hdct.DmLoaiREF IN( 13,42)
                          OR hdct.DmLoaiBannerREF = 18
                        )


        SELECT DISTINCT
                HopDongREF ,
                DmHinhThucQuangCaoREF ,
                A.DmSanPhamREF ,
                A.DmWebsiteREF
        INTO    #ThucTreoPR_W
        FROM    dbo.ThucChayHopDongChiTietPR A
                INNER JOIN #HopDongPhatSinh B ON A.HopDongREF = B.HopDongFK
        WHERE   A.DeletedStatus = 0
		--------------
-------------- Check dữ liệu về Website
        INSERT  INTO dbo.Check_DuLieuDauVaoSanPham
                ( NgayThucHien ,
                  HopDongREF ,
                  SoHopDong ,
                  DmSanPhamREF ,
                  DmHinhThucQuangCaoREF_HD ,
                  DmHinhThucQuangCaoREF_TT ,
                  DmWebSiteHD ,
                  DmWebSite_TT ,
                  IDLyDo ,
                  LyDo ,
                  TrangThaiXuLy ,
                  IDLoai ,
                  TenLoai ,
                  GhiChu
                )
                SELECT  GETDATE() NgayThucHien ,
                        HopDongID ,
                        SoHopDong ,
                        A.DmSanPhamREF ,
                        DmHinhThucQuangCaoREF_HD ,
                        DmHinhThucQuangCaoREF DmHinhThucQuangCaoREF_TC ,
                        DmWebsiteREF_HD DmWebsiteREF_HD ,
                        DmWebsiteREF DmWebsiteREF_TC ,
                        IDLyDo ,
                        TenLoiChiTiet ,
                        TrangThaiXuLy ,
                        ID_Loai ,
                        TenLoai ,
                        '' GhiChu
                FROM    ( SELECT    A.HopDongID ,
                                    A.DmHinhThucQuangCaoREF_HD ,
                                    A.DmSanPhamREF ,
                                    A.SoHopDong ,
                                    A.DmWebsiteREF_HD ,
                                    B.DmHinhThucQuangCaoREF ,
                                    B.DmWebsiteREF ,
                                    21 IDLyDo ,
                                    0 TrangThaiXuLy
                          FROM      ( SELECT DISTINCT
                                                t.HopDongFK HopDongID ,
                                                t.DmLoaiREF DmHinhThucQuangCaoREF_HD ,
                                                t.DmSanPhamREF ,
                                                t.SoHopDong ,
                                                STUFF( (SELECT  DISTINCT
                                                              ','
                                                              + CONVERT(NVARCHAR(10), ISNULL(p2.DmWebsiteREF,
                                                              0))
                                                        FROM  #HopDongPhatSinh_W p2
                                                        WHERE t.HopDongFK = p2.HopDongFK
                                                              AND t.DmSanPhamREF = p2.DmSanPhamREF
                                                              AND t.DmLoaiREF = p2.DmLoaiREF
                                                FOR   XML PATH('') ,
                                                          TYPE).value('.',
                                                              'nvarchar(max)'),
                                                      1, 1, '') DmWebsiteREF_HD
                                      FROM      #HopDongPhatSinh_W t
                                    ) A
                                    INNER JOIN #ThucTreoPR_W B ON B.DmSanPhamREF = A.DmSanPhamREF
                                                              AND A.HopDongID = B.HopDongREF
                                                              AND A.DmHinhThucQuangCaoREF_HD = B.DmHinhThucQuangCaoREF
                          WHERE     CHARINDEX(CONVERT(NVARCHAR(10), B.DmWebsiteREF),
                                              A.DmWebsiteREF_HD) = 0
                        ) A
                        LEFT JOIN dbo.DmLoiKhiCheckDuLieu B ON A.IDLyDo = B.ID
                ORDER BY HopDongID ,
                        SoHopDong ,
                        DmSanPhamREF 

------------ Check dữ liệu về chiết khấu

        INSERT  INTO dbo.Check_DuLieuDauVaoSanPham
                ( NgayThucHien ,
                  HopDongREF ,
                  SoHopDong ,
                  DmSanPhamREF ,
                  DmHinhThucQuangCaoREF_HD ,
                  DmHinhThucQuangCaoREF_TT ,
                  ChietKhauHD ,
                  ChietKhau_TT ,
                  IDLyDo ,
                  LyDo ,
                  TrangThaiXuLy ,
                  IDLoai ,
                  TenLoai ,
                  GhiChu
                )
                SELECT  GETDATE() NgayThucHien ,
                        A.HopDongID ,
                        A.SoHopDong ,
                        A.DmSanPhamREF ,
                        A.DmHinhThucQuangCaoREF_HD ,
                        A.DmHinhThucQuangCaoREF_TC ,
                        A.ChietKhauHD ,
                        A.ChietKhauTC ,
                        IDLyDo ,
                        TenLoiChiTiet ,
                        TrangThaiXuLy ,
                        ID_Loai ,
                        TenLoai ,
                        '' GhiChu
                FROM    ( SELECT    A.HopDongFK HopDongID ,
                                    A.SoHopDong ,
                                    A.DmLoaiREF DmHinhThucQuangCaoREF_HD ,
                                    B.DmHinhThucQuangCaoREF DmHinhThucQuangCaoREF_TC ,
                                    A.DmSanPhamREF ,
                                    A.DanhMucCKHD ChietKhauHD ,
                                    B.DanhMucCKPR ChietKhauTC ,
                                    22 IDLyDo ,
                                    0 TrangThaiXuLy
                          FROM      ( SELECT DISTINCT
                                                t.HopDongFK ,
                                                t.DmLoaiREF ,
                                                t.SoHopDong ,
                                                t.DmSanPhamREF ,
                                                STUFF( (SELECT  DISTINCT
                                                              ','
                                                              + CONVERT(NVARCHAR(10), ISNULL(p2.ChietKhau,
                                                              0))
                                                        FROM  #HopDongPhatSinh p2
                                                        WHERE t.HopDongFK = p2.HopDongFK
                                                              AND t.DmSanPhamREF = p2.DmSanPhamREF
                                                              AND t.DmLoaiREF = p2.DmLoaiREF
                                                FOR   XML PATH('') ,
                                                          TYPE).value('.',
                                                              'nvarchar(max)'),
                                                      1, 1, '') DanhMucCKHD
                                      FROM      #HopDongPhatSinh t
                                    ) A
                                    INNER JOIN ( SELECT DISTINCT
                                                        t.HopDongREF ,
                                                        t.DmHinhThucQuangCaoREF ,
                                                        t.DmSanPhamREF ,
                                                        STUFF( (SELECT  DISTINCT
                                                              ','
                                                              + CONVERT(NVARCHAR(10), ISNULL(p2.ChietKhau,
                                                              0))
                                                              FROM
                                                              #ThucTreoPR p2
                                                              WHERE
                                                              t.HopDongREF = p2.HopDongREF
                                                              AND t.DmSanPhamREF = p2.DmSanPhamREF
                                                              AND t.DmHinhThucQuangCaoREF = p2.DmHinhThucQuangCaoREF
                                                        FOR   XML
                                                              PATH('') ,
                                                              TYPE).value('.',
                                                              'nvarchar(max)'),
                                                              1, 1, '') DanhMucCKPR
                                                 FROM   #ThucTreoPR t
                                               ) B ON B.DmSanPhamREF = A.DmSanPhamREF
                                                      AND A.HopDongFK = B.HopDongREF
                                                      AND A.DmLoaiREF = B.DmHinhThucQuangCaoREF
                          WHERE     CHARINDEX(B.DanhMucCKPR, A.DanhMucCKHD) = 0
                        ) A
                        LEFT JOIN dbo.DmLoiKhiCheckDuLieu B ON A.IDLyDo = B.ID
                ORDER BY HopDongID ,
                        A.DmSanPhamREF 

    END


```
