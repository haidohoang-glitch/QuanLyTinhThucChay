# Stored Procedure: `ThucChay_InsertThucChayDaTinh_CPR_ByDVT_CPR_DoiTruVaTinhLai_CPM`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-23 09:18:50.850000
- **Ngày sửa cuối**: 2018-03-16 14:15:36.167000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
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

--EXEC [dbo].[ThucChay_InsertThucChayDaTinh_CPR_ByDVT_CPR]


CREATE  PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_CPR_ByDVT_CPR_DoiTruVaTinhLai_CPM]
    @NgayThucHien DATETIME ,
    @HopDongID INT ,
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
                                      AND ( TD.DonViTinh = 'CPR' )
                                    )
                               THEN ISNULL([dbo].[ThucChay_GetSoLuongThucChayChuanByDonViTinh_CPR](TD.SoLuongDotChayBooking,
                                                              TD.TongViewThucChay,
                                                              TD.SoLuong,
                                                              TD.DonViTinh,
                                                              TD.NgayThucHien,
                                                              TD.HopDongChiTietREF),
                                           0)
                               ELSE 0
                          END ) AS SoLuongThucChayKM ,
                        ( CASE WHEN ( TD.DonViTinh = 'CPR' )
                               THEN [dbo].[ThucChay_GetSoLuongLechTreoHa_CPR](@NgayThucHien,
                                                              TD.HopDongChiTietREF,
                                                              TD.SoLuong,
                                                              TD.DonViTinh,
                                                              TD.DmSanPhamREF,
                                                              TD.TongViewThucChay)
                               ELSE 0
                          END ) AS SoLuongLechTreoHa ,
                        ( CASE WHEN ( TD.DonViTinh = 'CPR' )
                               THEN [dbo].[ThucChay_GetSoLuongLechTreoHa_CPR](@NgayThucHien,
                                                              TD.HopDongChiTietREF,
                                                              TD.SoLuong,
                                                              TD.DonViTinh,
                                                              TD.DmSanPhamREF,
                                                              TD.TongViewThucChay)
                                    * TD.DonGiaTheoDonViTinh
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
                        'ThucChay_InsertThucChayDaTinh_CPR_ByDVT_CPR_DoiTruVaTinhLai_CPM' GhiChu
                FROM    ( SELECT 

                                    D.HopDongID ,
                                    D.SoHopDong ,
                                    D.DmMaHopDongREF ,
                                    D.TenMaHopDong , 
                                    D.NgayDanhSoHopDong ,
                                    D.NgayKyHopDong ,
                                    D.NhanHopDong ,
                                    D.NgayNhanBanFax ,
                                    D.NgayNhanHopDongBanCung ,
                                    D.NgayChuyenHopDongChoKeToan ,
                                    D.So ,
                                    D.Thang ,
                                    D.Nam , 
                                    D.GiaTriHopDong ,
                                    D.CongNo ,
                                    A.HopDongChiTietREF ,
                                    D.DangSuDung ,
                                    D.IsGiayPhep ,
                                    D.TrangThaiHopDong ,
                                    D.IsBanCung , 
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
                                    D.TenKhachHang ,
                                    [dbo].[f_ReturnListConcatNhanHangREF_v2](C.HopDongChiTietID,
                                                              @NgayThucHien) NhanHang ,
                                    C.DmNhomNganhREF ,
                                    C.TenNhomNganh , 
                                    C.DmLoaiREF AS DmHinhThucQuangCao ,
                                    C.TenLoai AS TenHinhThucQuangCao , 
                                    dbo.GetProductIDByTypeProduct(A.typeproduct) AS DmSanPhamREF ,
                                    dbo.GetProductNameByTypeProduct(A.typeproduct) AS TenSanPham ,
                                    C.DmNhomWebsiteREF ,
                                    C.TenNhomWebsite , 
                                    C.DmChuyenMucREF ,
                                    C.TenChuyenMuc ,
                                    C.DmLoaiBannerREF ,
                                    C.TenLoaiBanner ,
                                    C.DmViTriREF ,
                                    C.TenViTri ,
                                    ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,
                                                              'Y'), '') DotChayHopDong ,
                                    0 AS SoLuongDotChayHD ,
                                    ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,
                                                              'N'), 0) DotChayBooking ,
                                    A.uv AS SoLuongDotChayBooking ,
                                    C.SoLuong
                                    * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong ,
                                    C.DonViTinh DonViTinh ,
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
                                    A.bannerid DmBannerREF ,--A.DmBannerREF,
                                    0 DmChienDichREF ,--A.DmChienDichREF,
                                    @DmWebsiteREF AS DmWebsiteREF ,
                                    @TenWebsite AS TenWebsite ,
                                    A.uvngay AS TongViewThucChay ,
                                    0 AS TongClickThucChay ,
                                    0 AS TongSoBaiViet ,
                                    ( CASE WHEN ( ( C.IsKhuyenMai = 0 )
                                                  AND ( UPPER(C.DonViTinh) = 'CPR' )
                                                )
                                           THEN ISNULL([dbo].[ThucChay_GetSoLuongThucChayChuanByDonViTinh_CPR](A.uv,
                                                              A.uvngay,
                                                              C.SoLuong,
                                                              C.DonViTinh,
                                                              A.NgayThucHien,
                                                              A.HopDongChiTietREF),
                                                       0)
                                           ELSE 0
                                      END ) AS SoLuongThucChay ,
                                    A.NgayThucHien ,
                                    0 AS GiaTriThayDoi ,
                                    ISNULL([dbo].[ThucChay_GetThanhTienChuanThucChay_CPR_ByDVT_CPR](C.DonViTinh,
                                                              C.DonGia,
                                                              C.SoLuong, A.uv,
                                                              A.uvngay,
                                                              C.HopDongChiTietID,
                                                              @NgayThucHien),
                                           0) AS ThanhTienThucChayTruocTrietKhau
                          FROM      ( SELECT    tcc.NgayThucHien ,
                                                ROUND(( tcc.uv
                                                        * B.TiLeThucChayHDCTSoVoiBanner )
                                                      / 100, 0) uv ,
                                                ROUND(( tcc.uvngay
                                                        * B.TiLeThucChayHDCTSoVoiBanner )
                                                      / 100, 0) uvngay ,
                                                B.HopDongChiTietREF ,
                                                tcc.typeproduct ,
                                                tcc.bannerid
                                      FROM      ( SELECT DISTINCT
                                                            B.DmBannerID ,
                                                            B.HopDongChiTietREF ,
                                                            B.HopDongREF ,
                                                            ISNULL(B.TiLeThucChayHDCTSoVoiBanner,
                                                              0) TiLeThucChayHDCTSoVoiBanner ,
                                                            B.DeletedStatus ,
                                                            B.DaThucHienUpdateTiLe
                                                  FROM      dbo.ThucChayHopDongChiTietAndBanner B
                                                ) B
                                                INNER JOIN dbo.ThucChayCPRTemp tcc ON CONVERT(NVARCHAR(50), tcc.bannerid) = B.DmBannerID
                                      WHERE     B.HopDongREF = @HopDongID
                                                AND tcc.typeproduct = @TypeProduct
                                                AND tcc.NgayThucHien = @NgayThucHien
                                                AND B.DeletedStatus = 0
												AND B.HopDongChiTietREF = @pHopDongChiTietID
                                      GROUP BY  tcc.NgayThucHien ,
                                                B.HopDongChiTietREF ,
                                                tcc.typeproduct ,
                                                tcc.uv ,
                                                tcc.uvngay ,
                                                B.TiLeThucChayHDCTSoVoiBanner ,
                                                tcc.bannerid
                                    ) A
                                    INNER JOIN dbo.HopDongChiTiet C ON C.HopDongChiTietID = A.HopDongChiTietREF
                                    INNER JOIN dbo.HopDong D ON D.HopDongID = C.HopDongFK
                          WHERE     D.TrangThaiHopDong <> 3
                                    AND C.DeletedStatus = 0
                                    AND C.DmSanPhamREF IN ( 680, 598, 735 )
                                    AND C.DonViTinhREF = 30 --DON VI TINH LA CPR
                        ) TD
	
	
    END

```
