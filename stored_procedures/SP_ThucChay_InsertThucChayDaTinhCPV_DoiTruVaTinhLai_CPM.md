# Stored Procedure: `ThucChay_InsertThucChayDaTinhCPV_DoiTruVaTinhLai_CPM`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-22 17:20:30.053000
- **Ngày sửa cuối**: 2019-07-23 11:15:38.183000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(100)` | No |
| `@DmBannerREF` | `int(4)` | No |
| `@pHopDongChiTietID` | `int(4)` | No |
| `@NgayTinh` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucChayDaTinh]


CREATE  PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinhCPV_DoiTruVaTinhLai_CPM]
    @NgayThucHien DATETIME ,
    @SoHopDong NVARCHAR(50) ,
    @TypeProduct INT ,
    @DmWebsiteREF INT ,
    @TenWebsite NVARCHAR(50) ,
    @DmBannerREF INT ,
    @pHopDongChiTietID INT ,
	@NgayTinh DATETIME
AS
    BEGIN
	  DECLARE @TongViewCPV BIGINT = 0
		SET @TongViewCPV = ISNULL((
								SELECT SUM(ISNULL(tc.TongViewThucChay,0))
								FROM   dbo.ThucChayTemp tc
								WHERE 1=1
								AND tc.NgayThucHien = @NgayThucHien
								AND tc.DmBannerREF = @DmBannerREF --tinh theo chi tiet banner
								AND tc.SoHopDong = @SoHopDong
			),0)
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
                                      AND ( TD.DonViTinh = 'CPV' )
                                    )
                               THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(TD.TongSoBaiViet,
                                                              TD.SoLuong,
                                                              TD.DonViTinh,
                                                              TD.NgayThucHien,
                                                              TD.HopDongChiTietREF),
                                           0)
                               WHEN ( ( ( TD.IsKhuyenMai = 1 )
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
                        ( CASE WHEN ( TD.DonViTinh = 'CPV' )
                               THEN dbo.[ThucChay_GetSoLuongLechTreoHa_V1](@NgayThucHien,
                                                              TD.SoHopDong,
                                                              TD.HopDongChiTietREF,
                                                              TD.SoLuong,
                                                              TD.DmSanPhamREF,
                                                              TD.TongSoBaiViet)
                               WHEN ( TD.DonViTinh = 'VIEW' )
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
                        ( CASE WHEN ( TD.DonViTinh = 'CPV' )
                               THEN dbo.[ThucChay_GetSoLuongLechTreoHa_V1](@NgayThucHien,
                                                              TD.SoHopDong,
                                                              TD.HopDongChiTietREF,
                                                              TD.SoLuong,
                                                              TD.DmSanPhamREF,
                                                              TD.TongSoBaiViet)
                                    * TD.DonGiaTheoDonViTinh
                               WHEN ( TD.DonViTinh = 'VIEW' )
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
                        0 SoLuongThayDoi ,
                        0 SoLuongKMThayDoi ,
                        0 GiaTriKMThayDoi ,
                        'ThucChay_InsertThucChayDaTinhCPV_DoiTruVaTinhLai_CPM' GhiChu
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
                                    A.DsNhanHangREF NhanHang ,
                                    C.DmNhomNganhREF ,
                                    C.TenNhomNganh , 
                                    C.DmLoaiREF AS DmHinhThucQuangCao ,
                                    C.TenLoai AS TenHinhThucQuangCao , 
                                    dbo.GetProductIDByTypeProduct(A.TypeProduct) AS DmSanPhamREF ,
                                    dbo.GetProductNameByTypeProduct(A.TypeProduct) AS TenSanPham ,
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
                                    C.SoLuong AS SoLuongDotChayHD ,
                                    ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,
                                                              'N'), 0) DotChayBooking ,
                                    dbo.GetSoLuongDotChayBookingByHopDongChiTiet(C.HopDongChiTietID) SoLuongDotChayBooking , 
                                    C.SoLuong
                                    * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong ,
                                    dbo.ThucChay_GetDonViTinhNotCPD(C.DonViTinh) AS DonViTinh , 
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
                                    A.DmBannerREF DmBannerREF ,--A.DmBannerREF,
                                    0 DmChienDichREF ,--A.DmChienDichREF,
                                    A.DmWebsiteREF ,
                                    A.TenWebsite ,
                                    A.TongViewThucChay ,
                                    A.TongClickThucChay ,
                                    A.TongCPVThucChay TongSoBaiViet , --Tam thoi lay co du lieu nay lam sl cho CPV
                                    ( CASE WHEN ( ( C.IsKhuyenMai = 0 )
                                                  AND ( UPPER(C.DonViTinh) = 'CPM' )
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
                                           WHEN ( ( C.IsKhuyenMai = 0 )
                                                  AND ( UPPER(C.DonViTinh) = 'CPV' )
                                                )
                                           THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(A.TongCPVThucChay,
                                                              C.SoLuong,
                                                              C.DonViTinh,
                                                              A.NgayThucHien,
                                                              A.HopDongChiTietREF),
                                                       0)
                                           ELSE 0
                                      END ) AS SoLuongThucChay ,
                                    A.NgayThucHien ,
                                    0 AS GiaTriThayDoi ,
                                    ISNULL(dbo.ThucChay_GetThanhTienChuanThucChay(C.SoLuong,
                                                              C.DonViTinh,
                                                              C.DonGia,
                                                              D.NgayKyHopDong,
                                                              A.TongViewThucChay,
                                                              A.TongClickThucChay,
                                                              A.TongCPVThucChay,
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
                                                ROUND(SUM(( A.SoLuongCPV
                                                            * B.TiLeThucChayHDCTSoVoiBanner )
                                                          / 100), 0) TongCPVThucChay ,
                                                SUM(ISNULL(A.TongSoBaiViet, 0)) TongSoBaiViet ,
                                                [dbo].[f_ReturnListConcatNhanHangREFByBanner_CPV](@SoHopDong,
                                                              @TypeProduct,
                                                              B.HopDongChiTietREF,
                                                              @DmWebsiteREF) DsNhanHangREF ,
                                                B.HopDongChiTietREF ,
                                                A.TypeProduct ,
                                                A.DmWebsiteREF ,
                                                A.TenWebsite ,
                                                A.DmBannerREF
                                      FROM      ( SELECT    tc.NgayThucHien ,
                                                            tc.TongViewThucChay ,
                                                            tc.TongClickThucChay ,
                                                            tc.TongSoBaiViet ,
                                                            tc.SoHopDong ,
                                                            ( CASE WHEN ISNULL(@TongViewCPV, 0) = 0 THEN 0
                                                              ELSE ( tc.TongViewThucChay /@TongViewCPV ) * tcc.CPV
                                                              END ) SoLuongCPV ,
                                                            tc.TypeProduct ,
                                                            tc.DmWebsiteREF ,
                                                            tc.TenWebsite ,
                                                            tc.DmBannerREF
                                                  FROM      dbo.ThucChayTemp tc
                                                            INNER JOIN dbo.ThucChayCPVTemp tcc ON tc.DmBannerREF = tcc.bannerid
                                                              AND tcc.NgayThucHien = tc.NgayThucHien
                                                              AND tcc.bannerid = @DmBannerREF --tinh theo chi tiet banner
                                                ) A
                                                INNER JOIN ( SELECT DISTINCT
                                                              B.DmBannerID ,
                                                              B.HopDongChiTietREF ,
                                                              B.HopDongREF ,
                                                              B.TiLeThucChayHDCTSoVoiBanner ,
                                                              B.DeletedStatus ,
                                                              B.DaThucHienUpdateTiLe
                                                             FROM
                                                              dbo.ThucChayHopDongChiTietAndBanner B
                                                              INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = B.HopDongChiTietREF
                                                             WHERE
                                                              hdct.DeletedStatus = 0
                                                              AND hdct.DonViTinhREF = 22 --CPV
                                                           ) B ON B.DmBannerID = CONVERT(NVARCHAR(50), A.DmBannerREF)
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
                                                A.DmBannerREF
                                    ) A
                                    INNER JOIN (SELECT C.* FROM dbo.HopDongChiTiet C WHERE C.HopDongChiTietID = @pHopDongChiTietID
									AND  C.DeletedStatus = 0
                                    AND C.DmLoaiREF <> 13 --Khong tinh thuc chay cho HTQC Mua Ngoai
                                    AND C.DmSanPhamREF IN ( 240,598 )
                                    AND C.DonViTinh = N'CPV') C ON C.HopDongChiTietID = A.HopDongChiTietREF
                                    INNER JOIN (SELECT * FROM dbo.HopDong D WHERE D.TrangThaiHopDong <> 3 AND D.SoHopDong = @SoHopDong) D ON D.HopDongID = C.HopDongFK
                        ) TD
	
	
    END

```
