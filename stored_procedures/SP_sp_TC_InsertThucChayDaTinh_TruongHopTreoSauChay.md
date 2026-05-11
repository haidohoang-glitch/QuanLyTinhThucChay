# Stored Procedure: `sp_TC_InsertThucChayDaTinh_TruongHopTreoSauChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-24 10:55:07.770000
- **Ngày sửa cuối**: 2017-12-09 10:56:28.023000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(100)` | No |
| `@DmBannerREF` | `int(4)` | No |
| `@pNgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucChayDaTinh]


CREATE  PROCEDURE [dbo].[sp_TC_InsertThucChayDaTinh_TruongHopTreoSauChay]
    @NgayThucHien DATETIME ,
    @SoHopDong NVARCHAR(50) ,
    @TypeProduct INT ,
    @DmWebsiteREF INT ,
    @TenWebsite NVARCHAR(50) ,
    @DmBannerREF INT,
	@pNgayThucHien DATETIME
AS
    BEGIN
	

        INSERT  INTO dbo.ThucChayDaTinh
                ( ThucChayDaTinhID
                , HopDongID
                , SoHopDong
                , DmMaHopDongREF
                , TenMaHopDong
                , NgayDanhSoHopDong
                , NgayKyHopDong
                , NhanHopDong
                , NgayNhanBanFax
                , NgayNhanHopDongBanCung
                , NgayChuyenHopDongChoKeToan
                , So
                , Thang
                , Nam
                , GiaTriHopDong
                , CongNo
                , HopDongChiTietREF
                , DangSuDung
                , IsGiayPhep
                , TrangThaiHopDong
                , IsBanCung
                , DmPhongBanREF
                , TenPhongBan
                , DmBoPhanREF
                , TenBoPhan
                , DmNhomLamViecREF
                , TenNhomLamViec
                , DmDiaDiemLamViecREF
                , TenDiaDiemLamViec
                , SysNhanVienREF
                , TenDangNhap
                , TenNhanVien
                , TenKhachHang
                , NhanHang
                , DmNhomNganhREF
                , TenNhomNganh
                , DmHinhThucQuangCao
                , TenHinhThucQuangCao
                , DmSanPhamREF
                , TenSanPham
                , DmNhomWebsiteREF
                , TenNhomWebsite
                , DmChuyenMucREF
                , TenChuyenMuc
                , DmLoaiBannerREF
                , TenLoaiBanner
                , DmViTriREF
                , TenViTri
                , DotChayHopDong
                , SoLuongDotChayHD
                , DotChayBooking
                , SoLuongDotChayBooking
                , SoLuong
                , DonViTinh
                , DonGia
                , DonGiaTheoDonVi
                , ChietKhau
                , GiamGia
                , ThanhTien
                , TiLeTuVan
                , ChiPhiTuVan
                , IsKhuyenMai
                , KhuyenMai
                , DmBannerREF
                , DmChienDichREF
                , DmWebsiteREF
                , TenWebsite
                , TongViewThucChay
                , TongClickThucChay
                , TongSoBaiViet
                , SoLuongThucChay
                , NgayThucHien
                , GiaTriThayDoi
                , ThanhTienThucChayTruocTrietKhau
                , GiaTriTrietKhauThucChay
                , ThanhTienSauTrietKhauThucChay
                , GiaTriHoaHongThucChay
                , ThanhTienThucThu
                , ThanhTienKM
                , SoLuongThucChayKM
                , SoLuongThucChayLechTreoHa
                , ThanhTienLechTreoHa
                , CreatedAt
                , LastModifiedAt
                , IsPheDuyet
                , PheDuyetBy
                , PheDuyetAt
                , SoLuongThayDoi
                , SoLuongKMThayDoi
                , GiaTriKMThayDoi
                , GhiChu
                )
                SELECT  NEWID() ,
                        TD.HopDongID ,
                        TD.SoHopDong ,
                        TD.DmMaHopDongREF ,
                        TD.TenMaHopDong ,
                        TD.NgayDanhSoHopDong ,
                        TD.NgayKyHopDong ,
                        TD.NhanHopDong ,
                        TD.NgayNhanBanFax ,
                        TD.NgayNhanHopDongBanCung ,
                        TD.NgayChuyenHopDongChoKeToan ,
                        TD.So ,
                        TD.Thang ,
                        TD.Nam ,
                        TD.GiaTriHopDong ,
                        TD.CongNo ,
                        TD.HopDongChiTietREF ,
                        TD.DangSuDung ,
                        TD.IsGiayPhep ,
                        TD.TrangThaiHopDong ,
                        TD.IsBanCung ,
                        TD.DmPhongBanREF ,
                        TD.TenPhongBan ,
                        TD.DmBoPhanREF ,
                        TD.TenBoPhan ,
                        TD.DmNhomLamViecREF ,
                        TD.TenNhom ,
                        TD.DmDiaDiemLamViecREF ,
                        TD.TenDiaDiemLamViec ,
                        TD.SysNhanVienREF ,
                        TD.TenDangNhap ,
                        TD.TenNhanVien ,
                        TD.TenKhachHang ,
                        TD.NhanHang ,
                        TD.DmNhomNganhREF ,
                        TD.TenNhomNganh ,
                        TD.DmHinhThucQuangCao ,
                        TD.TenHinhThucQuangCao ,
                        TD.DmSanPhamREF ,
                        TD.TenSanPham ,
                        TD.DmNhomWebsiteREF ,
                        TD.TenNhomWebsite ,
                        TD.DmChuyenMucREF ,
                        TD.TenChuyenMuc ,
                        TD.DmLoaiBannerREF ,
                        TD.TenLoaiBanner ,
                        TD.DmViTriREF ,
                        TD.TenViTri ,
                        TD.DotChayHopDong ,
                        TD.SoLuongDotChayHD ,
                        TD.DotChayBooking ,
                        TD.SoLuongDotChayBooking ,
                        TD.SoLuong ,
                        TD.DonViTinh ,
                        TD.DonGia ,
                        TD.DonGiaTheoDonViTinh ,
                        TD.ChietKhau ,
                        TD.GiamGia ,
                        TD.ThanhTien ,
                        TD.TiLeTuVan ,
                        TD.ChiPhiTuVan ,
                        TD.IsKhuyenMai ,
                        TD.KhuyenMai ,
                        TD.DmBannerREF ,
                        TD.DmChienDichREF ,
                        TD.DmWebsiteREF ,
                        TD.TenWebsite ,
                        TD.TongViewThucChay ,
                        TD.TongClickThucChay ,
                        TD.TongSoBaiViet ,
                        TD.SoLuongThucChay ,
                        TD.NgayThucHien ,
                        ISNULL(( TD.ThanhTienThucChayTruocTrietKhau
                                 - ( TD.ThanhTienThucChayTruocTrietKhau
                                     * TD.ChietKhau ) / 100 ), 0) GiaTriThayDoi ,
                        0 ThanhTienThucChayTruocTrietKhau ,
                        ISNULL(( ( TD.ThanhTienThucChayTruocTrietKhau
                                   * TD.ChietKhau ) / 100 ), 0) AS GiaTriTrietKhauThucChay ,
                        0 AS ThanhTienSauTrietKhauThucChay ,
                        ISNULL(( ( ( TD.ThanhTienThucChayTruocTrietKhau
                                     - ( TD.ThanhTienThucChayTruocTrietKhau
                                         * TD.ChietKhau ) / 100 )
                                   * TD.TiLeTuVan ) / 100 ), 0) AS GiaTriHoaHongThucChay ,
                        ISNULL(( TD.ThanhTienThucChayTruocTrietKhau
                                 - ( TD.ThanhTienThucChayTruocTrietKhau
                                     * TD.ChietKhau ) / 100
                                 - ( ( TD.ThanhTienThucChayTruocTrietKhau
                                       - ( TD.ThanhTienThucChayTruocTrietKhau
                                           * TD.ChietKhau ) / 100 )
                                     * TD.TiLeTuVan ) / 100 ), 0) AS ThanhTienThucThu ,
                        ( CASE WHEN TD.IsKhuyenMai = 1
                               THEN TD.ThanhTienThucChayTruocTrietKhau
                               ELSE 0
                          END ) AS ThanhTienKM ,
                        ( CASE WHEN ( ( ( TD.IsKhuyenMai = 1 )
                                        OR ( TD.ChietKhau = 100 )
                                      )
                                      AND ( TD.DonViTinh = 'VIEW' )
                                    )
                               THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(TD.TongViewThucChay,
                                                              TD.SoLuong,
                                                              TD.DonViTinh,
                                                              TD.NgayThucHien,
                                                              TD.HopDongChiTietREF),
                                           0)
                               WHEN ( ( ( TD.IsKhuyenMai = 1 )
                                        OR ( TD.ChietKhau = 100 )
                                      )
                                      AND ( TD.DonViTinh = 'CLICK' )
                                    )
                               THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(TD.TongClickThucChay,
                                                              TD.SoLuong,
                                                              TD.DonViTinh,
                                                              TD.NgayThucHien,
                                                              TD.HopDongChiTietREF),
                                           0)
                               ELSE 0
                          END ) AS SoLuongThucChayKM ,
                        ( CASE WHEN ( TD.DonViTinh = 'VIEW' )
                               THEN dbo.[ThucChay_GetSoLuongLechTreoHa_V1](@NgayThucHien,
                                                              TD.SoHopDong,
                                                              TD.HopDongChiTietREF,
                                                              TD.SoLuong,
                                                              TD.DmSanPhamREF,
                                                              TD.TongViewThucChay)
                               WHEN ( TD.DonViTinh = 'CLICK' )
                               THEN dbo.[ThucChay_GetSoLuongLechTreoHa_V1](@NgayThucHien,
                                                              TD.SoHopDong,
                                                              TD.HopDongChiTietREF,
                                                              TD.SoLuong,
                                                              TD.DmSanPhamREF,
                                                              TD.TongClickThucChay)
                               ELSE 0
                          END ) AS SoLuongLechTreoHa ,
                        ( CASE WHEN ( TD.DonViTinh = 'VIEW' )
                               THEN dbo.[ThucChay_GetSoLuongLechTreoHa_V1](@NgayThucHien,
                                                              TD.SoHopDong,
                                                              TD.HopDongChiTietREF,
                                                              TD.SoLuong,
                                                              TD.DmSanPhamREF,
                                                              TD.TongViewThucChay)
                                    * TD.DonGiaTheoDonViTinh
                               WHEN ( TD.DonViTinh = 'CLICK' )
                               THEN dbo.[ThucChay_GetSoLuongLechTreoHa_V1](@NgayThucHien,
                                                              TD.SoHopDong,
                                                              TD.HopDongChiTietREF,
                                                              TD.SoLuong,
                                                              TD.DmSanPhamREF,
                                                              TD.TongClickThucChay)
                                    * TD.DonGiaTheoDonViTinh
                               ELSE 0
                          END ) AS ThanhTienLechTreoHa ,
                        GETDATE() ,
                        GETDATE() ,
                        0 IsPheDuyet ,
                        '' PheDuyetBy ,
                        '' PheDuyetAt ,
                        SL SoLuongThayDoi ,
                        0 SoLuongKMThayDoi ,
                        0 GiaTriKMThayDoi ,
                        N'CPM: sp_TC_InsertThucChayDaTinh_TruongHopTreoSauChay' GhiChu
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
                                    D.NhanHopDong ,
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
                                    A.HopDongChiTietREF ,
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
                                    A.DsNhanHangREF NhanHang ,
                                    C.DmNhomNganhREF ,
                                    C.TenNhomNganh , 
	--Thong tin hinh thuc quang cao
                                    C.DmLoaiREF AS DmHinhThucQuangCao ,
                                    C.TenLoai AS TenHinhThucQuangCao , 
	--Thong tin San pham
                                    dbo.GetProductIDByTypeProduct(A.TypeProduct) AS DmSanPhamREF ,
                                    dbo.GetProductNameByTypeProduct(A.TypeProduct) AS TenSanPham ,
                                    C.DmNhomWebsiteREF ,
                                    C.TenNhomWebsite , 
	--C.DmWebsiteREF, 
	--C.TenWebsite, 
                                    C.DmChuyenMucREF ,
                                    C.TenChuyenMuc ,
                                    C.DmLoaiBannerREF ,
                                    C.TenLoaiBanner ,
                                    C.DmBannerREF DmViTriREF ,
                                    C.TenViTri ,
                                    ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,
                                                              'Y'), '') DotChayHopDong ,
                                    C.SoLuong AS SoLuongDotChayHD ,
                                    ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,
                                                              'N'), 0) DotChayBooking ,
                                    dbo.GetSoLuongDotChayBookingByHopDongChiTiet(C.HopDongChiTietID) SoLuongDotChayBooking , 
	--Thong tin ve Tien
	--****haidh chinh sua
                                    C.SoLuong
                                    * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong ,
	--****haidh chinh sua
                                    dbo.ThucChay_GetDonViTinhNotCPD(C.DonViTinh) AS DonViTinh , 
	--'VIEW' DonViTinh, 
                                    dbo.ThucChay_GetDonGiaByNgayThucHien(A.NgayThucHien,
                                                              A.HopDongChiTietREF,
                                                              C.DonGia) AS DonGia ,
	--****haidh chinh sua 
                                    ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,
                                                              C.DonViTinh,
                                                              C.DonGia,
                                                              D.NgayKyHopDong,
                                                              A.NgayThucHien,
                                                              A.HopDongChiTietREF),
                                           0) AS DonGiaTheoDonViTinh ,
                                    C.ChietKhau ,
                                    C.GiamGia ,
                                    C.ThanhTien ,
                                    C.TiLeTuVan ,
                                    C.ChiPhiTuVan ,
                                    C.IsKhuyenMai ,
                                    C.KhuyenMai ,
	--Thuc chay
                                    A.DmBannerREF DmBannerREF ,--A.DmBannerREF,
                                    0 DmChienDichREF ,--A.DmChienDichREF,
                                    A.DmWebsiteREF ,
                                    A.TenWebsite ,
	--C.DmWebsiteREF,--A.DmWebsiteREF,
	--E.TenWebsite,
	--A.SoHopDong,
                                    A.TongViewThucChay ,
                                    A.TongClickThucChay ,
                                    A.TongSoBaiViet ,
	--****haidh chinh sua	
                                    0 AS SoLuongThucChay ,

									  ( CASE WHEN ( ( C.IsKhuyenMai = 0 )
                                                  AND ( ( UPPER(C.DonViTinh) = 'CPM' )
                                                        OR ( UPPER(C.DonViTinh) = 'TRUE REACH' )
                                                      )
                                                )
                                           THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(A.TongViewThucChay,
                                                              C.SoLuong,
                                                              C.DonViTinh,
                                                              A.NgayThucHien,
                                                              A.HopDongChiTietREF),
                                                       0)
                                           WHEN ( ( C.IsKhuyenMai = 0 )
                                                  AND ( UPPER(C.DonViTinh) = 'CPC' )
                                                )
                                           THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(A.TongClickThucChay,
                                                              C.SoLuong,
                                                              C.DonViTinh,
                                                              A.NgayThucHien,
                                                              A.HopDongChiTietREF),
                                                       0)
                                           ELSE 0
                                      END ) AS	SL,
	--Thanhuc Tien Thuc Chay
                                    A.NgayThucHien ,
                                    0 AS GiaTriThayDoi ,
	--****haidh chinh sua	
                                    ISNULL(dbo.ThucChay_GetThanhTienChuanThucChay(C.SoLuong,
                                                              C.DonViTinh,
                                                              C.DonGia,
                                                              D.NgayKyHopDong,
                                                              A.TongViewThucChay,
                                                              A.TongClickThucChay,
                                                              A.TongSoBaiViet,
                                                              A.NgayThucHien,
                                                              A.HopDongChiTietREF),
                                           0) AS ThanhTienThucChayTruocTrietKhau

                          FROM      ( SELECT    A.NgayThucHien ,
                                                ROUND(SUM(( A.TongViewThucChay
                                                            * B.TiLeThucChayHDCTSoVoiBanner )
                                                          / 100), 0) TongViewThucChay ,
                                                ROUND(SUM(( A.TongClickThucChay
                                                            * B.TiLeThucChayHDCTSoVoiBanner )
                                                          / 100), 0) TongClickThucChay ,
                                                SUM(ISNULL(A.TongSoBaiViet, 0)) TongSoBaiViet ,
                                                [dbo].[f_ReturnListConcatNhanHangREFByBanner](@SoHopDong,
                                                              @TypeProduct,
                                                              B.HopDongChiTietREF,
                                                              A.DmWebsiteREF) DsNhanHangREF ,
                                                B.HopDongChiTietREF ,
                                                A.TypeProduct ,
                                                A.DmWebsiteREF ,
                                                A.TenWebsite ,
                                                A.DmBannerREF
                                      FROM      ThucChayTemp A
                                                INNER JOIN ( SELECT DISTINCT
                                                              B.DmBannerID ,
                                                              B.DsNhanHangREF ,
                                                              B.HopDongChiTietREF ,
                                                              B.HopDongREF ,
                                                              B.TiLeThucChayHDCTSoVoiBanner ,
                                                              B.DeletedStatus ,
                                                              B.DaThucHienUpdateTiLe
                                                             FROM
                                                              dbo.ThucChayHopDongChiTietAndBanner B
                                                           ) B ON B.DmBannerID = CONVERT(NVARCHAR(50), A.DmBannerREF)
                                      WHERE     A.SoHopDong = @SoHopDong
                                                AND A.TypeProduct = @TypeProduct
                                                AND A.DmWebsiteREF = @DmWebsiteREF
                                                AND A.DmBannerREF = @DmBannerREF
                                                AND B.DeletedStatus = 0
                                      GROUP BY  A.NgayThucHien ,
												B.HopDongChiTietREF ,
                                                A.TypeProduct ,
                                                A.TenWebsite ,
                                                A.DmWebsiteREF ,
                                                A.DmBannerREF
                                    ) A
                                    INNER JOIN HopDongChiTiet C ON C.HopDongChiTietID = A.HopDongChiTietREF
                                    INNER JOIN HopDong D ON D.HopDongID = C.HopDongFK
                                    INNER JOIN DmWebsite E ON E.DmWebsiteID = C.DmWebsiteREF
                          WHERE     D.TrangThaiHopDong != 3
                                    AND C.DeletedStatus = 0
                                    AND C.DmSanPhamREF IN ( 231, 238, 339, 240,
                                                            370, 598, 613, 735 )
                                    AND C.DmLoaiBannerREF NOT IN ( 17, 18 )--Khong tinh cho cac loai banner ChiPhi va Mua ngoai
                                    AND C.DmLoaiREF <> 13 --Khong tinh thuc chay cho HTQC Mua Ngoai
									AND C.DmLoaiREF <> 42
                                    AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](C.DonViTinhREF,
                                                              C.DonViTinh) = 3 --Đơn vị của hình thức CPM
									--AND D.SoHopDong = @SoHopDong
                        ) TD
	
	
    END

```
