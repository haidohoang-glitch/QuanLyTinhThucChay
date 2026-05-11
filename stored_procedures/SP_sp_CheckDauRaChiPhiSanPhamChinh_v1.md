# Stored Procedure: `sp_CheckDauRaChiPhiSanPhamChinh_v1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-08-14 11:00:33.840000
- **Ngày sửa cuối**: 2017-08-17 16:12:15.367000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayDanhSo` | `datetime(8)` | No |
| `@NgayBatDau` | `datetime(8)` | No |
| `@NgayKetThuc` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--sp_CheckDauRaChiPhiSanPhamChinh_v1 '2015-01-01','2017-07-01','2017-08-10'
CREATE PROCEDURE [dbo].[sp_CheckDauRaChiPhiSanPhamChinh_v1]
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
        SELECT  A.ThucChayHopDongChiTietID ,
                A.HopDongREF ,
                A.HopDongChiTietREF ,
                A.DmSanPhamREF
        INTO    #HDPhatSinhThucChay
        FROM    ( SELECT DISTINCT
                            ThucChayHopDongChiTietID ,
                            HopDongREF ,
                            HopDongChiTietREF ,
                            DmSanPhamREF ,
                            BookingREF
                  FROM      dbo.ThucChayHopDongChiTiet
                  WHERE     CONVERT(DATE, LastModifiedAt) BETWEEN @NgayBatDau
                                                          AND @NgayKetThuc
                            AND DeletedStatus = 0
                ) A
                INNER JOIN dbo.HopDong hd ON A.HopDongREF = hd.HopDongID
                INNER JOIN dbo.HopDongChiTiet hdct ON A.HopDongChiTietREF = hdct.HopDongChiTietID
                                                      AND A.HopDongREF = hdct.HopDongFK
        WHERE   hdct.DeletedStatus = 0
                AND hdct.DmLoaiBannerREF = 17
                AND A.DmSanPhamREF NOT IN ( 242-- Luot up							
						--NHOM SP Chi phí--	
							, 251--Thiết kế, quản lý
							, 252--Hosting
							, 253--Chi phi khac
							, 535--Chi phí quản lý campaign
							, 537--Chi phí viết bài
							, 538--Chi phí thiết kế
							, 539--Chi phí dựng clip
							, 540--Chi phí sáng tạo
							, 541--Chi phí giải thưởng cuộc thi/ Contest
							, 542--Chi phí xây dưng microsite/ tab
							, 555--Chi phí trài trợ
							, 556--Hiệu đính
							, 557--Chèn Clip
							, 558--Chi phí viết bài
							, 559--Chi phí quay clip
							, 560--Chi phí sản xuất
							, 561-- Chi phí khảo sát thị trường online
							, 635-- Quản trị fanpage
							, 563-- Forum Seeding
							, 631-- facebook seeding
							, 651-- đăng tin fanpage
							, 629, 423, 306 )
                AND hdct.DmLoaiREF NOT IN ( 29, 28, 30, 33, 31, 32, 22, 34, 10,
                                            13, 14, 26 )
                AND hd.NgayDanhSoHopDong >= @NgayDanhSo
                AND hd.DeletedStatus = 0;
       
	   
-- Xác định đơn giá theo ngày
-- B1. Xác định đợt chạy của các hợp đồng
        SELECT  B.HopDongREF ,
                B.HopDongChiTietREF ,
                hdct.DmSanPhamREF ,
                CASE WHEN hdct.ChietKhau = 100 THEN hdct.DonGia
                     ELSE hdct.ThanhTien
                END ThanhTien ,
                COUNT(B.ThucChayHopDongChiTietID) SoLuongThucChay ,
                CASE WHEN hdct.ChietKhau = 100 THEN hdct.DonGia
                     ELSE hdct.ThanhTien
                END * COUNT(DISTINCT B.ThucChayHopDongChiTietID) * ( 1
                                                              - hdct.ChietKhau
                                                              / 100 ) DonGiaTheoSL
        INTO    #DonGiaTheoNgay
        FROM    ( SELECT DISTINCT
                            hd.ThucChayHopDongChiTietID ,
                            hd.HopDongREF ,
                            hd.HopDongChiTietREF
                  FROM      #HDPhatSinhThucChay hd
                ) B
                INNER JOIN dbo.HopDongChiTiet hdct ON B.HopDongREF = hdct.HopDongFK
                                                      AND B.HopDongChiTietREF = hdct.HopDongChiTietID
        WHERE   hdct.DeletedStatus = 0
                AND hdct.DmLoaiBannerREF = 17
                AND hdct.DmLoaiREF NOT IN ( 29, 28, 30, 33, 31, 32, 22, 34, 10,
                                            13, 14, 26 )
                AND hdct.DmSanPhamREF NOT IN ( 242-- Luot up							
						--NHOM SP Chi phí--	
							, 251--Thiết kế, quản lý
							, 252--Hosting
							, 253--Chi phi khac
							, 535--Chi phí quản lý campaign
							, 537--Chi phí viết bài
							, 538--Chi phí thiết kế
							, 539--Chi phí dựng clip
							, 540--Chi phí sáng tạo
							, 541--Chi phí giải thưởng cuộc thi/ Contest
							, 542--Chi phí xây dưng microsite/ tab
							, 555--Chi phí trài trợ
							, 556--Hiệu đính
							, 557--Chèn Clip
							, 558--Chi phí viết bài
							, 559--Chi phí quay clip
							, 560--Chi phí sản xuất
							, 561-- Chi phí khảo sát thị trường online
							, 635-- Quản trị fanpage
							, 563-- Forum Seeding
							, 631-- facebook seeding
							, 651-- đăng tin fanpage
							, 629, 423, 306 )
        GROUP BY B.HopDongREF ,
                B.HopDongChiTietREF ,
                hdct.DmSanPhamREF ,
                CASE WHEN hdct.ChietKhau = 100 THEN hdct.DonGia
                     ELSE hdct.ThanhTien
                END ,
                hdct.ChietKhau
        ORDER BY HopDongChiTietREF;
		--SELECT * FROM #HDPhatSinhThucChay
		--SELECT * FROM #DonGiaTheoNgay
        SELECT  ISNULL(A.HopDongREF, B.HopDongID) HopDongREF ,
                ISNULL(A.HopDongChiTietREF, B.HopDongChiTietREF) HopDongChiTietREF ,
                ISNULL(A.DmSanPhamREF, B.DmSanPhamREF) DmSanPhamREF ,
                ISNULL(B.SoLuongThucChay, 0) SoNgayChay ,
                ISNULL(A.DonGiaTheoSL, 0) DonGiaTheoNgay ,
                ISNULL(A.ThanhTienThucChayTT, 0) ThanhTienThucChayTT ,
                ISNULL(B.SoLuongThucChay, 0) SoLuongThucChay ,
                ISNULL(B.ThanhTienThucChay, 0) ThanhTienThucChay
        INTO    #KetQua
        FROM    ( SELECT    A.* ,
                            B.DonGiaTheoSL ,
                            B.SoLuongThucChay * B.DonGiaTheoSL ThanhTienThucChayTT
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
                            WHERE   1 = 1
                                    AND NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
                                    AND A.DmLoaiBannerREF = 17
                                    AND A.DmHinhThucQuangCao NOT IN ( 29, 28,
                                                              30, 33, 31, 32,
                                                              22, 34, 10, 13,
                                                              14, 26 )
                                    AND A.DmSanPhamREF NOT IN ( 242-- Luot up							
						--NHOM SP Chi phí--	
							, 251--Thiết kế, quản lý
							, 252--Hosting
							, 253--Chi phi khac
							, 535--Chi phí quản lý campaign
							, 537--Chi phí viết bài
							, 538--Chi phí thiết kế
							, 539--Chi phí dựng clip
							, 540--Chi phí sáng tạo
							, 541--Chi phí giải thưởng cuộc thi/ Contest
							, 542--Chi phí xây dưng microsite/ tab
							, 555--Chi phí trài trợ
							, 556--Hiệu đính
							, 557--Chèn Clip
							, 558--Chi phí viết bài
							, 559--Chi phí quay clip
							, 560--Chi phí sản xuất
							, 561-- Chi phí khảo sát thị trường online
							, 635-- Quản trị fanpage
							, 563-- Forum Seeding
							, 631-- facebook seeding
							, 651-- đăng tin fanpage
							, 629, 423, 306 )
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
        WHERE   ABS(ISNULL(B.ThanhTienThucChay, 0)
                    - ISNULL(A.ThanhTienThucChayTT, 0)) > 10;

        --SELECT  A.HopDongREF ,
        --        hd.SoHopDong ,
        --        A.HopDongChiTietREF ,
        --        A.DmSanPhamREF ,
        --        hdct.TenSanPham ,
        --        hdct.DmLoaiREF HinhThucQuangCao ,
        --        hdct.ThanhTien ThanhTienHD ,
        --        0 ThucChayTong ,
        --        A.SoLuongThucChay ,
        --        A.SoNgayChay SoLuongThucChayTT ,
        --        A.SoLuongThucChay - A.SoNgayChay SoLuongLech ,
        --        A.ThanhTienThucChay ,
        --        A.ThanhTienThucChayTT ,
        --        A.ThanhTienThucChay - A.ThanhTienThucChayTT GiaTriLech
        --FROM    #KetQua A
        --        INNER JOIN dbo.HopDong hd ON A.HopDongREF = hd.HopDongID
        --        INNER JOIN dbo.HopDongChiTiet hdct ON A.HopDongChiTietREF = hdct.HopDongChiTietID;
       
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
                                                7 IDLoi
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
                                                8 IDLoi
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
