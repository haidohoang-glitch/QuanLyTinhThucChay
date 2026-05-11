# Stored Procedure: `ThucChay_InsertThucChayDaTinh_CPR_DoiTruVaTinhLai_CPM`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-23 09:11:11.957000
- **Ngày sửa cuối**: 2017-11-30 09:25:10.820000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(100)` | No |
| `@pHopDongChiTietID` | `int(4)` | No |
| `@NgayTinh` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [dbo].[ThucChay_InsertThucChayDaTinh_CPR]


CREATE  PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_CPR_DoiTruVaTinhLai_CPM]
    @NgayThucHien DATETIME ,
    @SoHopDong NVARCHAR(50) ,
    @TypeProduct INT ,
    @DmWebsiteREF INT ,
    @TenWebsite NVARCHAR(50) ,
    @pHopDongChiTietID INT,
	@NgayTinh DATETIME
AS
    BEGIN

        INSERT  INTO dbo.ThucChayDaTinh
                SELECT  NEWID() ,
                        TD.HopDongID
                      , TD.SoHopDong
                      , TD.DmMaHopDongREF
                      , TD.TenMaHopDong
                      , TD.NgayDanhSoHopDong
                      , TD.NgayKyHopDong
                      , TD.NhanHopDong
                      , TD.NgayNhanBanFax
                      , TD.NgayNhanHopDongBanCung
                      , TD.NgayChuyenHopDongChoKeToan
                      , TD.So
                      , TD.Thang
                      , TD.Nam
                      , TD.GiaTriHopDong
                      , TD.CongNo
                      , TD.HopDongChiTietREF
                      , TD.DangSuDung
                      , TD.IsGiayPhep
                      , TD.TrangThaiHopDong
                      , TD.IsBanCung
                      , TD.DmPhongBanREF
                      , TD.TenPhongBan
                      , TD.DmBoPhanREF
                      , TD.TenBoPhan
                      , TD.DmNhomLamViecREF
                      , TD.TenNhom
                      , TD.DmDiaDiemLamViecREF
                      , TD.TenDiaDiemLamViec
                      , TD.SysNhanVienREF
                      , TD.TenDangNhap
                      , TD.TenNhanVien
                      , TD.TenKhachHang
                      , TD.NhanHang
                      , TD.DmNhomNganhREF
                      , TD.TenNhomNganh
                      , TD.DmHinhThucQuangCao
                      , TD.TenHinhThucQuangCao
                      , TD.DmSanPhamREF
                      , TD.TenSanPham
                      , TD.DmNhomWebsiteREF
                      , TD.TenNhomWebsite
                      , TD.DmChuyenMucREF
                      , TD.TenChuyenMuc
                      , TD.DmLoaiBannerREF
                      , TD.TenLoaiBanner
                      , TD.DmViTriREF
                      , TD.TenViTri
                      , TD.DotChayHopDong
                      , TD.SoLuongDotChayHD
                      , TD.DotChayBooking
                      , TD.SoLuongDotChayBooking
                      , TD.SoLuong
                      , TD.DonViTinh
                      , TD.DonGia
                      , TD.DonGiaTheoDonViTinh
                      , TD.ChietKhau
                      , TD.GiamGia
                      , TD.ThanhTien
                      , TD.TiLeTuVan
                      , TD.ChiPhiTuVan
                      , TD.IsKhuyenMai
                      , TD.KhuyenMai
                      , TD.DmBannerREF
                      , TD.DmChienDichREF
                      , TD.DmWebsiteREF
                      , TD.TenWebsite
                      , TD.TongViewThucChay
                      , TD.TongClickThucChay
                      , TD.TongSoBaiViet
                      , TD.SoLuongThucChay
                      , TD.NgayThucHien
                      , TD.GiaTriThayDoi
                      , TD.ThanhTienThucChayTruocTrietKhau ,
                        ISNULL(( ( TD.ThanhTienThucChayTruocTrietKhau
                                   * TD.ChietKhau ) / 100 ), 0) AS GiaTriTrietKhauThucChay ,
                        ISNULL(( TD.ThanhTienThucChayTruocTrietKhau
                                 - ( TD.ThanhTienThucChayTruocTrietKhau
                                     * TD.ChietKhau ) / 100 ), 0) AS ThanhTienSauTrietKhauThucChay ,
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
                                    ) THEN ISNULL(TD.SoLuongThucChay, 0)
                               WHEN ( ( ( TD.IsKhuyenMai = 1 )
                                        OR ( TD.ChietKhau = 100 )
                                      )
                                      AND ( TD.DonViTinh = 'CLICK' )
                                    ) THEN ISNULL(TD.SoLuongThucChay, 0)
                               ELSE 0
                          END ) AS SoLuongThucChayKM ,
                        ( CASE WHEN ( TD.DonViTinh = 'VIEW' ) THEN 0
                               WHEN ( TD.DonViTinh = 'CLICK' ) THEN 0
                               ELSE 0
                          END ) AS SoLuongLechTreoHa ,
                        ( CASE WHEN ( TD.DonViTinh = 'VIEW' ) THEN 0
                               WHEN ( TD.DonViTinh = 'CLICK' ) THEN 0
                               ELSE 0
                          END ) AS ThanhTienLechTreoHa ,
                        GETDATE() ,
                        GETDATE() ,
                        0 IsPheDuyet ,
                        '' PheDuyetBy ,
                        '' PheDuyetAt ,
                        0 SoLuongThayDoi ,
                        0 SoLuongKMThayDoi ,
                        0 GiaTriKMThayDoi ,
                        'ThucChay_InsertThucChayDaTinh_CPR_DoiTruVaTinhLai_CPM' GhiChu
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
                                    [dbo].[f_ReturnListConcatNhanHangREF_v2](C.HopDongChiTietID,
                                                              @NgayThucHien) NhanHang ,
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
                                    C.DmViTriREF ,
                                    C.TenViTri ,
                                    ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,
                                                              'Y'), '') DotChayHopDong ,
                                    CPR.UV AS SoLuongDotChayHD ,
                                    ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,
                                                              'N'), 0) DotChayBooking ,
                                    A.uv AS SoLuongDotChayBooking ,
                                    C.SoLuong
                                    * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong ,
                                    'VIEW' DonViTinh ,
                                    dbo.ThucChay_GetDonGiaByNgayThucHien(A.NgayThucHien,
                                                              A.HopDongChiTietREF,
                                                              C.DonGia) AS DonGia ,
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
                                    C.DmBannerREF DmBannerREF ,--A.DmBannerREF,
                                    0 DmChienDichREF ,--A.DmChienDichREF,
                                    A.DmWebsiteREF ,
                                    A.TenWebsite ,
                                    A.TongViewThucChay ,
                                    A.TongClickThucChay ,
                                    A.TongSoBaiViet ,
                                    A.TongViewThucChay AS SoLuongThucChay ,
                                    A.NgayThucHien ,
                                    0 AS GiaTriThayDoi ,
                                    ISNULL([dbo].[ThucChay_GetThanhTienChuanThucChay_CPR](C.DonViTinhREF,
                                                              C.DonGia,
                                                              C.ChietKhau,
                                                              CPR.UV,
                                                              CPR.view_user,
                                                              A.uv, A.uvngay,
                                                              A.TongViewThucChay,
                                                              C.HopDongChiTietID,
                                                              D.SoHopDong,
                                                              A.TypeProduct,
                                                              @NgayThucHien),
                                           0) AS ThanhTienThucChayTruocTrietKhau
                          FROM      ( SELECT    A.NgayThucHien ,
                                                ROUND(SUM(( A.TongViewThucChay
                                                            * B.TiLeThucChayHDCTSoVoiBanner )
                                                          / 100), 0) TongViewThucChay ,
                                                ROUND(SUM(( A.TongClickThucChay
                                                            * B.TiLeThucChayHDCTSoVoiBanner )
                                                          / 100), 0) TongClickThucChay ,
                                                SUM(ISNULL(A.TongSoBaiViet, 0)) TongSoBaiViet ,
                                                tcc.uv ,
                                                tcc.uvngay ,
                                                B.HopDongChiTietREF ,
                                                A.TypeProduct ,
                                                A.DmWebsiteREF ,
                                                A.TenWebsite
                                      FROM      ThucChayTemp A
                                                INNER JOIN ( SELECT DISTINCT
                                                              B.DmBannerID ,
                                                              B.HopDongChiTietREF ,
                                                              B.HopDongREF ,
                                                              B.TiLeThucChayHDCTSoVoiBanner ,
                                                              B.DeletedStatus ,
                                                              B.DaThucHienUpdateTiLe
                                                             FROM
                                                              dbo.ThucChayHopDongChiTietAndBanner B
                                                           ) B ON B.DmBannerID = CONVERT(NVARCHAR(50), A.DmBannerREF)
                                                INNER JOIN ThucChayCPRTemp tcc ON tcc.bannerid = A.DmBannerREF
                                      WHERE     A.SoHopDong = @SoHopDong
                                                AND A.TypeProduct = @TypeProduct
                                                AND A.DmWebsiteREF = @DmWebsiteREF
                                                AND B.DeletedStatus = 0
												AND B.HopDongChiTietREF = @pHopDongChiTietID
                                      GROUP BY  A.NgayThucHien ,
                                                B.HopDongChiTietREF ,
                                                A.TypeProduct ,
                                                A.TenWebsite ,
                                                A.DmWebsiteREF ,
                                                tcc.uv ,
                                                tcc.uvngay
                                    ) A
                                    INNER JOIN HopDongChiTiet C ON C.HopDongChiTietID = A.HopDongChiTietREF
                                    INNER JOIN HopDong D ON D.HopDongID = C.HopDongFK
                                    INNER JOIN DmWebsite E ON E.DmWebsiteID = C.DmWebsiteREF
                                    INNER JOIN DonGiaCPR CPR ON CPR.DmLoaiBannerREF = C.DmLoaiBannerREF
                          WHERE     D.TrangThaiHopDong != 3
                                    AND C.DeletedStatus = 0
                                    AND C.DmSanPhamREF IN ( 680 )
                                    AND C.DonViTinhREF = 10
                        ) TD
	
	
    END

```
