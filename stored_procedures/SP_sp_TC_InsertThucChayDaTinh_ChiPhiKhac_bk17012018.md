# Stored Procedure: `sp_TC_InsertThucChayDaTinh_ChiPhiKhac_bk17012018`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-01-17 16:59:07.403000
- **Ngày sửa cuối**: 2018-01-17 16:59:07.403000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@pSoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
--EXEC [ThucChay_InsertThucChayDaTinh_ChiPhiKhac] '2014-06-11 00:00:00.000','2014-06-11 15:42:55.690'
-------------------------------------------------------------
CREATE PROCEDURE [dbo].[sp_TC_InsertThucChayDaTinh_ChiPhiKhac_bk17012018]
    @StartDate DATETIME ,
    @EndDate DATETIME ,
    @pSoHopDong NVARCHAR(50)
AS
    BEGIN

        DECLARE @NgayThucHien DATETIME ,
            @NgayGioiHanTinh DATETIME
        SET @NgayThucHien = CONVERT(DATE, @StartDate)
        SET @NgayGioiHanTinh = '2010-01-01'



        WHILE ( @NgayThucHien <= @EndDate )
            BEGIN	 
				
                UPDATE  ThucChayHopDongChiTiet
                SET     RecordStatus = 0
                WHERE   CONVERT(NVARCHAR(500), ThucChayHopDongChiTietID) IN (
                        SELECT  DotChayBooking
                        FROM    dbo.ThucChayDaTinh
                        WHERE   NgayThucHien = @NgayThucHien
                                AND NOT ( DmHinhThucQuangCao = 13
                                          OR DmLoaiBannerREF IN ( 18 )
                                        )
                                AND DmSanPhamREF IN (--- NHOM SP TMDT --------------
                                242-- Luot up												
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
							--bo sung
							, 635-- Quản trị fanpage
							, 563-- Forum Seeding
							, 631-- Facebook Seeding
							, 651-- Đăng tin fanpage
							, 630-- Chi phí tư vấn
							, 726--Tư vấn viết đề án truyền thông
							, 731--KOL
							, 730--Livestream
							, 629--Chi phí tổ chức
							, 729--Visual Content
							, 633--Mở fanpage
							, 734
							, 736 )
                                AND ( @pSoHopDong IS NULL
                                      OR SoHopDong = @pSoHopDong
                                    ) )
				
                DELETE  FROM dbo.ThucChayDaTinh
                WHERE   NgayThucHien = @NgayThucHien
                        AND NOT ( DmHinhThucQuangCao = 13
                                  OR DmLoaiBannerREF IN ( 18 )
                                )
                        AND DmSanPhamREF IN (--- NHOM SP TMDT --------------
                        242-- Luot up												
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
							--bo sung
							, 635-- Quản trị fanpage
							, 563-- Forum Seeding
							, 631-- Facebook Seeding
							, 651-- Đăng tin fanpage
							, 630-- Chi phí tư vấn
							, 726--Tư vấn viết đề án truyền thông
							, 731--KOL
							, 730--Livestream
							, 629--Chi phí tổ chức
							, 729--Visual Content
							, 633--Mở fanpage
							, 734
							, 736)
                        AND ( @pSoHopDong IS NULL
                              OR SoHopDong = @pSoHopDong
                            )


                INSERT  INTO dbo.ThucChayDaTinh
                        SELECT  NEWID() ,
                                TD.* ,
                                ISNULL(( TD.ThanhTienThucChayTruocTrietKhau
                                         * TD.ChietKhau ) / 100, 0) AS GiaTriTrietKhauThucChay ,
                                ISNULL(( TD.ThanhTienThucChayTruocTrietKhau
                                         - ( TD.ThanhTienThucChayTruocTrietKhau
                                             * TD.ChietKhau ) / 100 ), 0) AS ThanhTienSauTrietKhauThucChay ,
                                ISNULL(( ( TD.ThanhTienThucChayTruocTrietKhau
                                           - ( TD.ThanhTienThucChayTruocTrietKhau
                                               * TD.ChietKhau ) / 100 )
                                         * TD.TiLeTuVan ) / 100, 0) AS GiaTriHoaHongThucChay ,
                                ISNULL(( TD.ThanhTienThucChayTruocTrietKhau
                                         - ( TD.ThanhTienThucChayTruocTrietKhau
                                             * TD.ChietKhau ) / 100
                                         - ( ( TD.ThanhTienThucChayTruocTrietKhau
                                               - ( TD.ThanhTienThucChayTruocTrietKhau
                                                   * TD.ChietKhau ) / 100 )
                                             * TD.TiLeTuVan ) / 100 ), 0) AS ThanhTienThucThu ,
                                ( CASE WHEN ( ( TD.IsKhuyenMai = 1 )
                                              OR ( TD.ChietKhau = 100 )
                                            )
                                       THEN TD.ThanhTienThucChayTruocTrietKhau
                                       ELSE 0
                                  END ) AS ThanhTienKM ,
                                ( CASE WHEN ( ( TD.IsKhuyenMai = 1 )
                                              OR ( TD.ChietKhau = 100 )
                                            ) THEN TD.SoLuongThucChay
                                       ELSE 0
                                  END ) AS SoLuongThucChayKM ,
                                0 SoLuongLechTreoHa ,
                                0 ThanhTienLechTreoHa ,
                                GETDATE() ,
                                GETDATE() ,
                                0 IsPheDuyet ,
                                '' PheDuyetBy ,
                                '' PheDuyetAt ,
                                0 SoLuongThayDoi ,
                                0 SoLuongKMThayDoi ,
                                0 GiaTriKMThayDoi ,
                                '' GhiChu
                        FROM    ( SELECT 
	--ID Hop Dong
                                            D.HopDongID ,
	--Thong tin ve ma so 
                                            D.SoHopDong ,
                                            D.DmMaHopDongREF ,
                                            D.TenMaHopDong , 
	--Thong tin ve thoi gian
                                            D.NgayDanhSoHopDong ,
                                            D.NgayKyHopDong ,
                                            ISNULL(D.NhanHopDong, '') AS NhanHopDong ,
                                            D.NgayNhanBanFax ,
                                            D.NgayNhanHopDongBanCung ,
                                            D.NgayChuyenHopDongChoKeToan ,
                                            D.So ,
                                            D.Thang ,
                                            D.Nam , 
	--Thong tin ve gia tri
                                            D.GiaTriHopDong ,
                                            D.CongNo ,
	--Thong tin chi tiet phan bo
                                            C.HopDongChiTietID ,
	--Thong tin ve trang thai
                                            D.DangSuDung ,
                                            D.IsGiayPhep ,
                                            D.TrangThaiHopDong ,
                                            D.IsBanCung , 
	--Thong tin ve Nhan vien kinh doanh
                                            D.DmPhongBanREF ,
                                            ISNULL(D.TenPhongBan, '') AS TenPhongBan ,
                                            D.DmBoPhanREF ,
                                            ISNULL(D.TenBoPhan, '') AS TenBoPhan ,
                                            D.DmNhomLamViecREF ,
                                            ISNULL(D.TenNhom, '') AS TenNhom ,
                                            D.DmDiaDiemLamViecREF ,
                                            D.TenDiaDiemLamViec ,
                                            D.SysNhanVienREF ,
                                            ISNULL(D.TenDangNhap, '') AS TenDangNhap ,
                                            D.TenNhanVien , 
	--Thong tin ve khach hang
	--D.DmKhachHangREF, 
                                            D.TenKhachHang , 
	--C.NhanHang, 
                                            [dbo].[f_ReturnListConcatNhanHangREF_v2](C.HopDongChiTietID,
                                                              @NgayThucHien) NhanHang ,
                                            C.DmNhomNganhREF ,
                                            C.TenNhomNganh , 
	--Thong tin hinh thuc quang cao
                                            C.DmLoaiREF AS DmHinhThucQuangCao ,
                                            C.TenLoai AS TenHinhThucQuangCao , 
	--Thong tin San pham
                                            C.DmSanPhamREF AS DmSanPhamREF ,
                                            E.TenSanPham ,
                                            C.DmNhomWebsiteREF ,
                                            C.TenNhomWebsite , 
	--C.DmWebsiteREF, 
	--C.TenWebsite, 
                                            C.DmChuyenMucREF ,
                                            C.TenChuyenMuc ,
                                            C.DmLoaiBannerREF ,
                                            C.TenLoaiBanner ,
                                            C.DmViTriREF ,
                                            C.TenViTri ,
                                            '' DotChayHopDong ,
                                            0 AS SoLuongDotChayHD ,
                                            C.ThucChayHopDongChiTietID DotChayBooking ,
                                            0 AS SoLuongDotChayBooking , 
	--Thong tin ve Tien
                                            C.SoLuongThucTreo AS SoLuong ,
                                            ISNULL(C.DonViTinh, N'đ/v') AS DonViTinh ,
                                            dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,
                                                              C.HopDongChiTietID,
                                                              C.DonGia) AS DonGia , 
	--ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong, @NgayThucHien, c.HopDongChiTietID),0) AS DonGiaTheoDonViTinh,
                                            dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,
                                                              C.HopDongChiTietID,
                                                              C.DonGia) AS DonGiaTheoDonViTinh ,
                                            C.ChietKhauThucTreo ChietKhau ,
                                            C.GiamGia ,
                                            C.ThanhTien ,
                                            C.TiLeTuVan ,
                                            C.ChiPhiTuVan ,
                                            C.IsKhuyenMai ,
                                            C.KhuyenMai ,
	--Thuc chay
                                            0 DmBannerREF ,--A.DmBannerREF,
                                            0 DmChienDichREF ,--A.DmChienDichREF,
                                            dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF) DmWebsiteREF ,
	--A.DmWebsiteREF,
                                            dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,
                                                              C.TenWebsite) TenWebsite ,
	--C.TenWebsite,
	--A.SoHopDong,
                                            0 TongViewThucChay ,
                                            0 TongClickThucChay ,
                                            0 TongSoBaiViet ,
                                            ( CASE WHEN C.IsKhuyenMai = 0
                                                   THEN C.SoLuongThucTreo
                                                   ELSE 0
                                              END ) AS SoLuongThucChay ,
	--Thanhuc Tien Thuc Chay
                                            @NgayThucHien AS NgayThucHien ,
                                            0 AS GiaTriThayDoi ,
                                            ISNULL(C.SoLuongThucTreo, 0)
                                            * ISNULL(C.DonGiaThucTreo, 0) AS ThanhTienThucChayTruocTrietKhau
                                  FROM      ( SELECT    *
                                              FROM      ( SELECT
                                                              ct.* ,
                                                              tchdctp.SoLuongThucTreo ,
                                                              tchdctp.DonGia DonGiaThucTreo ,
                                                              tchdctp.ChietKhau ChietKhauThucTreo ,
                                                              tchdctp.ThucChayHopDongChiTietID
                                                          FROM
                                                              HopDongChiTiet ct
                                                              INNER JOIN ThucChayHopDongChiTiet tchdctp ON ct.HopDongChiTietID = tchdctp.HopDongChiTietREF
                                                          WHERE
                                                              ct.DmSanPhamREF IN (--- NHOM SP TMDT --------------
                                                              242-- Luot up												
																			 --- NHOM SP Chi phí--
																			,
                                                              251--Thiết kế, quản lý
																			,
                                                              252--Hosting
																			,
                                                              253--Chi phi khac									
																			,
                                                              535--Chi phí quản lý campaign
																			,
                                                              537--Chi phí viết bài
																			,
                                                              538--Chi phí thiết kế
																			,
                                                              539--Chi phí dựng clip
																			,
                                                              540--Chi phí sáng tạo
																			,
                                                              541--Chi phí giải thưởng cuộc thi/ Contest
																			,
                                                              542--Chi phí xây dưng microsite/ tab
																			,
                                                              555--Chi phí trài trợ
																			,
                                                              556--Hiệu đính
																			,
                                                              557--Chèn Clip
																			,
                                                              558--Chi phí viết bài
																			,
                                                              559--Chi phí quay clip
																			,
                                                              560--Chi phí sản xuất										
																			,
                                                              561-- Chi phí khảo sát thị trường online
																			--bo sung
																			,
                                                              635-- Quản trị fanpage
																			,
                                                              563-- Forum Seeding
																			,
                                                              631-- Facebook Seeding
																			,
                                                              651-- Đăng tin fanpage
																			,
                                                              630-- chi phí tư vấn
																			,
                                                              726--Tư vấn viết đề án truyền thông
																			,
                                                              731--KOL
																			,
                                                              730--livestream
																			,
                                                              629--Chi phí tổ chức
																			,
                                                              729--Visual Content
																			,
                                                              633--Mở fanpage
																			,
															  734,
                                                              736 )
                                                              AND ct.DeletedStatus = 0
                                                              AND NOT ( DmLoaiREF = 13
                                                              OR DmLoaiBannerREF = 18
                                                              )	 --Khong tinh thuc chay cho HTQC Mua Ngoai

																------
                                                              AND ( CASE
                                                              WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt
                                                              THEN CONVERT(DATE, tchdctp.CreatedAt)
                                                              ELSE CONVERT(DATE, tchdctp.LastModifiedAt)
                                                              END ) = CONVERT(DATE, @NgayThucHien)
                                                              AND tchdctp.DeletedStatus = 0
                                                              AND tchdctp.RecordStatus = 0
                                                              AND CONVERT(DATE, ISNULL(tchdctp.ThoiGianBatDau,
                                                              '2013-01-01')) >= @NgayGioiHanTinh
                                                        ) T
                                              WHERE     ( ISNULL(T.SoLuong, 0)
                                                          * ISNULL(T.DonGia, 0) ) >= ( ISNULL(T.SoLuongThucTreo,
                                                              0)
                                                              * ISNULL(T.DonGiaThucTreo,
                                                              0) ) - 1000
                                            ) C
                                            INNER JOIN ( SELECT
                                                              *
                                                         FROM HopDong hd
                                                         WHERE
                                                              hd.TrangThaiHopDong <> 3
                                                              AND hd.DeletedStatus = 0
	      -- AND hd.SOHOPDONG IN ('QC2941013')
                                                              AND ( @pSoHopDong IS NULL
                                                              OR SoHopDong = @pSoHopDong
                                                              )
                                                       ) D ON D.HopDongID = C.HopDongFK
                                            INNER JOIN DmSanPham E ON E.DmSanPhamID = C.DmSanPhamREF
                                                              AND C.SoLuongThucTreo > 0
                                                              AND C.SoLuong > 0
                                                              AND C.DmWebsiteREF NOT IN (
                                                              307, 285 ) -- loai tru website Google, Facebook
                                ) TD	
	--EXEC [ThucChay_UpdateThucChayHopDongChiTiet_ChiPhiKhac] @NgayThucHien
	
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
            END 
        SELECT  '1'
    END


```
