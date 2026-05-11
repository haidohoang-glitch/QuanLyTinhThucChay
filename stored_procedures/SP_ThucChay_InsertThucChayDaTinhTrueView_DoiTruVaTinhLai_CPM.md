# Stored Procedure: `ThucChay_InsertThucChayDaTinhTrueView_DoiTruVaTinhLai_CPM`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-12-19 17:07:12.887000
- **Ngày sửa cuối**: 2023-08-21 17:52:03.020000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(100)` | No |
| `@DmBannerREF` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucChayDaTinh]


CREATE  PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinhTrueView_DoiTruVaTinhLai_CPM]
    @NgayThucHien DATETIME
  , @SoHopDong NVARCHAR(50)
  , @TypeProduct INT
  , @DmWebsiteREF INT
  , @TenWebsite NVARCHAR(50)
  , @DmBannerREF INT
  , @HopDongChiTietID int
AS
    BEGIN

        INSERT  INTO dbo.ThucChayDaTinh
        (
            ThucChayDaTinhID,
            HopDongID,
            SoHopDong,
            DmMaHopDongREF,
            TenMaHopDong,
            NgayDanhSoHopDong,
            NgayKyHopDong,
            NhanHopDong,
            NgayNhanBanFax,
            NgayNhanHopDongBanCung,
            NgayChuyenHopDongChoKeToan,
            So,
            Thang,
            Nam,
            GiaTriHopDong,
            CongNo,
            HopDongChiTietREF,
            DangSuDung,
            IsGiayPhep,
            TrangThaiHopDong,
            IsBanCung,
            DmPhongBanREF,
            TenPhongBan,
            DmBoPhanREF,
            TenBoPhan,
            DmNhomLamViecREF,
            TenNhomLamViec,
            DmDiaDiemLamViecREF,
            TenDiaDiemLamViec,
            SysNhanVienREF,
            TenDangNhap,
            TenNhanVien,
            TenKhachHang,
            NhanHang,
            DmNhomNganhREF,
            TenNhomNganh,
            DmHinhThucQuangCao,
            TenHinhThucQuangCao,
            DmSanPhamREF,
            TenSanPham,
            DmNhomWebsiteREF,
            TenNhomWebsite,
            DmChuyenMucREF,
            TenChuyenMuc,
            DmLoaiBannerREF,
            TenLoaiBanner,
            DmViTriREF,
            TenViTri,
            DotChayHopDong,
            SoLuongDotChayHD,
            DotChayBooking,
            SoLuongDotChayBooking,
            SoLuong,
            DonViTinh,
            DonGia,
            DonGiaTheoDonVi,
            ChietKhau,
            GiamGia,
            ThanhTien,
            TiLeTuVan,
            ChiPhiTuVan,
            IsKhuyenMai,
            KhuyenMai,
            DmBannerREF,
            DmChienDichREF,
            DmWebsiteREF,
            TenWebsite,
            TongViewThucChay,
            TongClickThucChay,
            TongSoBaiViet,
            SoLuongThucChay,
            NgayThucHien,
            GiaTriThayDoi,
            ThanhTienThucChayTruocTrietKhau,
            GiaTriTrietKhauThucChay,
            ThanhTienSauTrietKhauThucChay,
            GiaTriHoaHongThucChay,
            ThanhTienThucThu,
            ThanhTienKM,
            SoLuongThucChayKM,
            SoLuongThucChayLechTreoHa,
            ThanhTienLechTreoHa,
            CreatedAt,
            LastModifiedAt,
            IsPheDuyet,
            PheDuyetBy,
            PheDuyetAt,
            SoLuongThayDoi,
            SoLuongKMThayDoi,
            GiaTriKMThayDoi,
            GhiChu
        )
       SELECT TCDT.ThucChayDaTinhID, TCDT.HopDongID
            , TCDT.SoHopDong
            , TCDT.DmMaHopDongREF
            , TCDT.TenMaHopDong
            , TCDT.NgayDanhSoHopDong
            , TCDT.NgayKyHopDong
            , TCDT.NhanHopDong
            , TCDT.NgayNhanBanFax
            , TCDT.NgayNhanHopDongBanCung
            , TCDT.NgayChuyenHopDongChoKeToan
            , TCDT.So
            , TCDT.Thang
            , TCDT.Nam
            , TCDT.GiaTriHopDong
            , TCDT.CongNo
            , TCDT.HopDongChiTietREF
            , TCDT.DangSuDung
            , TCDT.IsGiayPhep
            , TCDT.TrangThaiHopDong
            , TCDT.IsBanCung
            , TCDT.DmPhongBanREF
            , TCDT.TenPhongBan
            , TCDT.DmBoPhanREF
            , TCDT.TenBoPhan
            , TCDT.DmNhomLamViecREF
            , TCDT.TenNhom
            , TCDT.DmDiaDiemLamViecREF
            , TCDT.TenDiaDiemLamViec
            , TCDT.SysNhanVienREF
            , TCDT.TenDangNhap
            , TCDT.TenNhanVien
            , TCDT.TenKhachHang
            , TCDT.NhanHang
            , TCDT.DmNhomNganhREF
            , TCDT.TenNhomNganh
            , TCDT.DmHinhThucQuangCao
            , TCDT.TenHinhThucQuangCao
            , TCDT.DmSanPhamREF
            , TCDT.TenSanPham
            , TCDT.DmNhomWebsiteREF
            , TCDT.TenNhomWebsite
            , TCDT.DmChuyenMucREF
            , TCDT.TenChuyenMuc
            , TCDT.DmLoaiBannerREF
            , TCDT.TenLoaiBanner
            , TCDT.DmViTriREF
            , TCDT.TenViTri
            , TCDT.DotChayHopDong
            , TCDT.SoLuongDotChayHD
            , TCDT.DotChayBooking
            , TCDT.SoLuongDotChayBooking
            , TCDT.SoLuong
            , TCDT.DonViTinh
            , TCDT.DonGia
            , TCDT.DonGiaTheoDonViTinh
            , TCDT.ChietKhau
            , TCDT.GiamGia
            , TCDT.ThanhTien
            , TCDT.TiLeTuVan
            , TCDT.ChiPhiTuVan
            , TCDT.IsKhuyenMai
            , TCDT.KhuyenMai
            , TCDT.DmBannerREF
            , TCDT.DmChienDichREF
            , TCDT.DmWebsiteREF
            , TCDT.TenWebsite
            , TCDT.TongViewThucChay
            , TCDT.TongClickThucChay
            , TCDT.TongSoBaiViet
            , 0 AS SoLuongThucChay
            , TCDT.NgayThucHien
            , TCDT.ThanhTienSauTrietKhauThucChay AS GiaTriThayDoi
            , 0 AS ThanhTienThucChayTruocTrietKhau 
			, 0 AS GiaTriTrietKhauThucChay
            , 0 AS ThanhTienSauTrietKhauThucChay
            , 0 AS GiaTriHoaHongThucChay
            , TCDT.ThanhTienSauTrietKhauThucChay AS ThanhTienThucThu
            , 0 AS ThanhTienKM
            , 0 AS SoLuongThucChayKM
            , TCDT.SoLuongLechTreoHa AS SoLuongLechTreoHa
            , TCDT.ThanhTienLechTreoHa AS ThanhTienLechTreoHa
            , TCDT.CreatedAt
            , TCDT.LastModifiedAt
            , TCDT.IsPheDuyet
            , TCDT.PheDuyetBy
            , TCDT.PheDuyetAt
            , TCDT.SoLuongThucChay AS SoLuongThayDoi
            , TCDT.SoLuongThucChayKM  AS SoLuongKMThayDoi
            , TCDT.ThanhTienKM AS GiaTriKMThayDoi
            , TCDT.GhiChu
		FROM
	   (
                SELECT  NEWID() AS ThucChayDaTinhID
                      , TD.*
                      , ISNULL(( ( TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau ) / 100 ), 0) AS GiaTriTrietKhauThucChay
                      , ISNULL(( TD.ThanhTienThucChayTruocTrietKhau - ( TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau ) / 100 ), 0) AS ThanhTienSauTrietKhauThucChay
                      , ISNULL(( ( ( TD.ThanhTienThucChayTruocTrietKhau - ( TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau ) / 100 ) * TD.TiLeTuVan ) / 100 ),
                               0) AS GiaTriHoaHongThucChay
                      , ISNULL(( TD.ThanhTienThucChayTruocTrietKhau - ( TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau ) / 100
                                 - ( ( TD.ThanhTienThucChayTruocTrietKhau - ( TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau ) / 100 ) * TD.TiLeTuVan ) / 100 ),
                               0) AS ThanhTienThucThu
                      , ( CASE WHEN TD.IsKhuyenMai = 1 THEN TD.ThanhTienThucChayTruocTrietKhau
                               ELSE 0
                          END ) AS ThanhTienKM
                      , ( CASE WHEN ( ( ( TD.IsKhuyenMai = 1 )
                                        OR ( TD.ChietKhau = 100 )
                                      )
                                      AND ( TD.DonViTinh = N'TRUE VIEW' OR TD.DonViTinh = N'TRUE REACH' )
                                    )
                               THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(TD.TongSoBaiViet, TD.SoLuong, TD.DonViTinh, TD.NgayThucHien,
                                                                                              TD.HopDongChiTietREF), 0)
                               ELSE 0
                          END ) AS SoLuongThucChayKM
                      , ( CASE WHEN ( TD.DonViTinh = N'TRUE VIEW' OR TD.DonViTinh = N'TRUE REACH' )
                               THEN dbo.[ThucChay_GetSoLuongLechTreoHa_V1](@NgayThucHien, TD.SoHopDong, TD.HopDongChiTietREF, TD.SoLuong, TD.DmSanPhamREF,
                                                                           TD.TongSoBaiViet)
                               ELSE 0
                          END ) AS SoLuongLechTreoHa
                      , ( CASE WHEN ( TD.DonViTinh = N'TRUE VIEW' OR TD.DonViTinh = N'TRUE REACH' )
                               THEN dbo.[ThucChay_GetSoLuongLechTreoHa_V1](@NgayThucHien, TD.SoHopDong, TD.HopDongChiTietREF, TD.SoLuong, TD.DmSanPhamREF,
                                                                           TD.TongSoBaiViet) * TD.DonGiaTheoDonViTinh
                               ELSE 0
                          END ) AS ThanhTienLechTreoHa
                      , GETDATE() AS CreatedAt
                      , GETDATE() AS LastModifiedAt
                      , 0 IsPheDuyet
                      , '' PheDuyetBy
                      , '' PheDuyetAt
                      , 0 SoLuongThayDoi
                      , 0 SoLuongKMThayDoi
                      , 0 GiaTriKMThayDoi
                      , 'ThucChay_InsertThucChayDaTinhTrueView_DoiTruVaTinhLai_CPM' GhiChu
                FROM    ( SELECT   D.HopDongID
                                  , D.SoHopDong
                                  , D.DmMaHopDongREF
                                  , D.TenMaHopDong
                                  , D.NgayDanhSoHopDong
                                  , D.NgayKyHopDong
                                  , D.NhanHopDong
                                  , D.NgayNhanBanFax
                                  , D.NgayNhanHopDongBanCung
                                  , D.NgayChuyenHopDongChoKeToan
                                  , D.So
                                  , D.Thang
                                  , D.Nam
                                  , D.GiaTriHopDong
                                  , D.CongNo
                                  , A.HopDongChiTietREF
                                  , D.DangSuDung
                                  , D.IsGiayPhep
                                  , D.TrangThaiHopDong
                                  , D.IsBanCung
                                  , D.DmPhongBanREF
                                  , ISNULL(D.TenPhongBan, '') AS TenPhongBan
                                  , D.DmBoPhanREF
                                  , ISNULL(D.TenBoPhan, '') AS TenBoPhan
                                  , D.DmNhomLamViecREF
                                  , ISNULL(D.TenNhom, '') AS TenNhom
                                  , D.DmDiaDiemLamViecREF
                                  , D.TenDiaDiemLamViec
                                  , D.SysNhanVienREF
                                  , ISNULL(D.TenDangNhap, '') AS TenDangNhap
                                  , D.TenNhanVien
                                  , D.TenKhachHang
                                  , A.DsNhanHangREF NhanHang
                                  , C.DmNhomNganhREF
                                  , C.TenNhomNganh
                                  , C.DmLoaiREF AS DmHinhThucQuangCao
                                  , C.TenLoai AS TenHinhThucQuangCao
                                  , dbo.GetProductIDByTypeProduct(A.TypeProduct) AS DmSanPhamREF
                                  , dbo.GetProductNameByTypeProduct(A.TypeProduct) AS TenSanPham
                                  , C.DmNhomWebsiteREF
                                  , C.TenNhomWebsite
                                  , C.DmChuyenMucREF
                                  , C.TenChuyenMuc
                                  , C.DmLoaiBannerREF
                                  , C.TenLoaiBanner
                                  , C.DmViTriREF
                                  , C.TenViTri
                                  , ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID, 'Y'), '') DotChayHopDong
                                  , C.SoLuong AS SoLuongDotChayHD
                                  , ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID, 'N'), 0) DotChayBooking
                                  , dbo.GetSoLuongDotChayBookingByHopDongChiTiet(C.HopDongChiTietID) SoLuongDotChayBooking
                                  , C.SoLuong * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong
                                  , dbo.ThucChay_GetDonViTinhNotCPD(C.DonViTinh) AS DonViTinh
                                  , dbo.ThucChay_GetDonGiaByNgayThucHien(A.NgayThucHien, A.HopDongChiTietREF, C.DonGia) AS DonGia
                                  , ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong, C.DonViTinh, C.DonGia, D.NgayKyHopDong, A.NgayThucHien,
                                                                                    A.HopDongChiTietREF), 0) AS DonGiaTheoDonViTinh
                                  , C.ChietKhau
                                  , C.GiamGia
                                  , C.ThanhTien
                                  , C.TiLeTuVan
                                  , C.ChiPhiTuVan
                                  , C.IsKhuyenMai
                                  , C.KhuyenMai
                                  , A.DmBannerREF DmBannerREF
                                  , 0 AS DmChienDichREF
                                  , A.DmWebsiteREF
                                  , A.TenWebsite
                                  , A.TongViewThucChay
                                  , A.TongClickThucChay
                                  , A.TongTrueViewThucChay TongSoBaiViet
                                  , ( CASE WHEN ( ( C.IsKhuyenMai = 0 )
                                                  AND ( UPPER(C.DonViTinh) = N'TRUE VIEW' OR UPPER(C.DonViTinh) = N'TRUE REACH' )
                                                )
                                           THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(A.TongTrueViewThucChay, C.SoLuong, C.DonViTinh,
                                                                                                          A.NgayThucHien, A.HopDongChiTietREF), 0)
                                           ELSE 0
                                      END ) AS SoLuongThucChay
                                  , A.NgayThucHien
                                  , 0 AS GiaTriThayDoi
                                  , ISNULL(dbo.ThucChay_GetThanhTienChuanThucChay(C.SoLuong, C.DonViTinh, C.DonGia, D.NgayKyHopDong, A.TongViewThucChay,
                                                                                  A.TongClickThucChay, A.TongTrueViewThucChay, A.NgayThucHien, A.HopDongChiTietREF),
                                           0) AS ThanhTienThucChayTruocTrietKhau
                          FROM      ( SELECT    A.NgayThucHien
                                              , ROUND(SUM(( A.TongViewThucChay * B.TiLeThucChayHDCTSoVoiBanner ) / 100), 0) TongViewThucChay
                                              , ROUND(SUM(( A.TongClickThucChay * B.TiLeThucChayHDCTSoVoiBanner ) / 100), 0) TongClickThucChay
                                              , ROUND(SUM(( A.SoLuongTrueView * B.TiLeThucChayHDCTSoVoiBanner ) / 100), 0) TongTrueViewThucChay
                                              , SUM(ISNULL(A.TongSoBaiViet, 0)) TongSoBaiViet
                                              , [dbo].[f_ReturnListConcatNhanHangREFByBanner_TrueView](B.HopDongChiTietREF, @DmBannerREF) DsNhanHangREF
                                              , B.HopDongChiTietREF
                                              , A.TypeProduct
                                              , A.DmWebsiteREF
                                              , A.TenWebsite
                                              , A.DmBannerREF
                                      FROM      ( SELECT    tcc.NgayThucHien
                                                          , tcc.Views TongViewThucChay
                                                          , tcc.Clicks TongClickThucChay
                                                          , 0 TongSoBaiViet
                                                          , tcc.SoHopDong
                                                          , tcc.True_View SoLuongTrueView
                                                          , tcc.TypeProduct
														  , tcc.DmSanPhamREF
                                                          , tcc.SiteID DmWebsiteREF
                                                          , tcc.SiteName TenWebsite
                                                          , tcc.bannerid DmBannerREF
                                                  FROM    dbo.ThucChayTrueViewTemp tcc WHERE 1=1
                                                        AND tcc.NgayThucHien = @NgayThucHien
                                                        AND tcc.bannerid = @DmBannerREF --tinh theo chi tiet banner
														AND tcc.SiteID = @DmWebsiteREF
														AND tcc.SoHopDong = @SoHopDong
														AND tcc.TypeProduct = @TypeProduct
                                                ) A
                                                INNER JOIN ( SELECT DISTINCT
                                                                    B.DmBannerID
                                                                  , B.HopDongChiTietREF
                                                                  , B.HopDongREF
                                                                  , B.TiLeThucChayHDCTSoVoiBanner
                                                                  , B.DeletedStatus
                                                                  , B.DaThucHienUpdateTiLe
																  , hdct.DmSanPhamREF
                                                             FROM   dbo.ThucChayHopDongChiTietAndBanner B
                                                                    INNER JOIN (select * from dbo.HopDongChiTiet hdct where 1=1 and hdct.HopDongChiTietID = @HopDongChiTietID)hdct ON hdct.HopDongChiTietID = B.HopDongChiTietREF
                                                             WHERE  hdct.DeletedStatus = 0
                                                                    AND (hdct.DonViTinhREF = 32 OR hdct.DonViTinhREF = 31)
																	AND B.HopDongChiTietREF = @HopDongChiTietID
																	
                                                           ) B ON B.DmBannerID = CONVERT(NVARCHAR(50), A.DmBannerREF)
														   AND ((A.DmSanPhamREF = B.DmSanPhamREF) OR (B.DmSanPhamREF = 733))
                                      WHERE     A.SoHopDong = @SoHopDong
                                                AND A.TypeProduct = @TypeProduct
                                                AND A.DmWebsiteREF = @DmWebsiteREF
                                                AND B.DeletedStatus = 0
                                      GROUP BY  A.NgayThucHien
                                              , B.HopDongChiTietREF
                                              , A.TypeProduct
                                              , A.TenWebsite
                                              , A.DmWebsiteREF
                                              , A.DmBannerREF
                                    ) A
                                    INNER JOIN (select C.* from dbo.HopDongChiTiet C where C.HopDongChiTietID = @HopDongChiTietID
									AND C.DeletedStatus = 0
                                    AND C.DmLoaiREF <> 13 --Khong tinh thuc chay cho HTQC Mua Ngoai
									AND C.DmLoaiREF <> 42
                                    AND C.DmSanPhamREF IN ( 240, 733 )
                                    AND (C.DonViTinhREF = 32 OR C.DonViTinhREF = 31) -- true reach or true view
									)C ON C.HopDongChiTietID = A.HopDongChiTietREF
                                    INNER JOIN (SELECT D.* FROM dbo.HopDong D WHERE D.TrangThaiHopDong <> 3 )D ON D.HopDongID = C.HopDongFK

                        ) TD
	
	  )TCDT
    END

```
