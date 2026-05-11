# Stored Procedure: `sp_CheckDauRaChiPhiKhac_v1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-08-14 10:29:10.140000
- **Ngày sửa cuối**: 2017-08-17 16:10:57.910000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayDanhSo` | `datetime(8)` | No |
| `@NgayBatDau` | `datetime(8)` | No |
| `@NgayKetThuc` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--sp_CheckDauRaChiPhiKhac_v1 '2015-01-01','2017-08-12','2017-08-16'
CREATE PROCEDURE [dbo].[sp_CheckDauRaChiPhiKhac_v1]
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
                SoLuongThucTreo SoNgayChay
        INTO    #HDPhatSinhThucChay
        FROM    ( SELECT DISTINCT
                            HopDongREF ,
                            HopDongChiTietREF ,
                            DmSanPhamREF ,
                            BookingREF ,
                            SoLuongThucTreo
                  FROM      dbo.ThucChayHopDongChiTiet
                  WHERE     CONVERT(DATE, LastModifiedAt) BETWEEN @NgayBatDau
                                                          AND @NgayKetThuc
                            AND DmSanPhamREF IN ( 242-- Luot up							
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
							, 629 )
                            AND DeletedStatus = 0
                ) A
                INNER JOIN dbo.HopDong hd ON A.HopDongREF = hd.HopDongID
        WHERE   hd.NgayDanhSoHopDong >= @NgayDanhSo
                AND hd.DeletedStatus = 0;
       
	   
-- Xác định đơn giá theo ngày
-- B1. Xác định đợt chạy của các hợp đồng
        SELECT  B.HopDongREF ,
                B.HopDongChiTietREF ,
                hdct.DmSanPhamREF ,
                CASE WHEN hdct.ChietKhau = 100 THEN hdct.DonGia
                     ELSE hdct.ThanhTien
                END ThanhTien ,
                hdct.SoLuong TongSoNgayDuKien ,
                CASE WHEN hdct.ChietKhau = 100 THEN hdct.DonGia
                     ELSE hdct.ThanhTien
                END / hdct.SoLuong DonGiaTheoNgay
        INTO    #DonGiaTheoNgay
        FROM    ( SELECT DISTINCT
                            hd.HopDongREF ,
                            hd.HopDongChiTietREF
                  FROM      #HDPhatSinhThucChay hd
                ) B
                INNER JOIN dbo.HopDongChiTiet hdct ON B.HopDongREF = hdct.HopDongFK
                                                      AND B.HopDongChiTietREF = hdct.HopDongChiTietID
        WHERE   hdct.DeletedStatus = 0
                AND NOT ( hdct.DmLoaiREF = 13
                          OR DmLoaiBannerREF = 18
                        )
                AND NOT ( hdct.DmLoaiREF = 42 )
                AND hdct.DmLoaiREF <> 17
        ORDER BY HopDongChiTietREF;
		--SELECT * FROM #HDPhatSinhThucChay
		--SELECT * FROM #DonGiaTheoNgay
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
                            WHERE   DmSanPhamREF IN ( 242-- Luot up							
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
							, 629 )
                                    AND NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
                                    AND NOT ( DmHinhThucQuangCao = 13
                                              OR DmLoaiBannerREF = 18
                                            )
                                    AND NOT ( DmHinhThucQuangCao = 42 )
                                    AND A.DmHinhThucQuangCao <> 17
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
                                                9 IDLoi
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
                                                10 IDLoi
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
