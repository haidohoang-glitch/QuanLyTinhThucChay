# Stored Procedure: `ThucChay_InsertThucChayDaTinhTrueView`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-12-19 10:31:11.783000
- **Ngày sửa cuối**: 2023-08-22 16:56:37.250000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(100)` | No |
| `@DmBannerREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucChayDaTinh]


CREATE  PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinhTrueView]
    @NgayThucHien DATETIME
  , @SoHopDong NVARCHAR(50)
  , @TypeProduct INT
  , @DmWebsiteREF INT
  , @TenWebsite NVARCHAR(50)
  , @DmBannerREF INT
AS
    BEGIN
	DECLARE @HopDongID INT
	SET @HopDongID = (
			SELECT TOP 1 HopDongID FROM dbo.HopDong WHERE SoHopDong = @SoHopDong
		)
	
        INSERT  INTO dbo.ThucChayDaTinh
                SELECT  NEWID()
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
                                      AND ( TD.DonViTinh = N'TRUE VIEW' OR TD.DonViTinh = N'TRUE REACH')
                                    )
                               THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(TD.TongSoBaiViet, TD.SoLuong, TD.DonViTinh, TD.NgayThucHien,
                                                                                              TD.HopDongChiTietREF), 0)
                               ELSE 0
                          END ) AS SoLuongThucChayKM
                      , ( CASE WHEN ( TD.DonViTinh = N'TRUE VIEW' OR TD.DonViTinh = N'TRUE REACH')
                               THEN dbo.[ThucChay_GetSoLuongLechTreoHa_V1](@NgayThucHien, TD.SoHopDong, TD.HopDongChiTietREF, TD.SoLuong, TD.DmSanPhamREF,
                                                                           TD.TongSoBaiViet)
                               ELSE 0
                          END ) AS SoLuongLechTreoHa
                      , ( CASE WHEN ( TD.DonViTinh = N'TRUE VIEW' OR TD.DonViTinh = N'TRUE REACH')
                               THEN dbo.[ThucChay_GetSoLuongLechTreoHa_V1](@NgayThucHien, TD.SoHopDong, TD.HopDongChiTietREF, TD.SoLuong, TD.DmSanPhamREF,
                                                                           TD.TongSoBaiViet) * TD.DonGiaTheoDonViTinh
                               ELSE 0
                          END ) AS ThanhTienLechTreoHa
                      , GETDATE()
                      , GETDATE()
                      , 0 IsPheDuyet
                      , '' PheDuyetBy
                      , '' PheDuyetAt
                      , 0 SoLuongThayDoi
                      , 0 SoLuongKMThayDoi
                      , 0 GiaTriKMThayDoi
                      , 'ThucChay_InsertThucChayDaTinhTrueView' GhiChu
                FROM    ( SELECT D.HopDongID
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
                                  ,	dbo.ThucChay_GetDonViTinhNotCPD(C.DonViTinh) AS DonViTinh
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
                                  , 0 DmChienDichREF
                                  , A.DmWebsiteREF
                                  , A.TenWebsite
                                  , A.TongViewThucChay
                                  , A.TongClickThucChay
                                  , A.TongTrueViewThucChay TongSoBaiViet
                                  , ( CASE WHEN ( ( C.IsKhuyenMai = 0 )
                                                  AND ( UPPER(C.DonViTinh) = N'TRUE VIEW' OR   UPPER(C.DonViTinh) = N'TRUE REACH')
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
                                                             FROM   ( SELECT * FROM dbo.ThucChayHopDongChiTietAndBanner WHERE HopDongREF = @HopDongID) B
                                                                    INNER JOIN (SELECT * from dbo.HopDongChiTiet WHERE HopDongFK = @HopDongID) hdct ON hdct.HopDongChiTietID = B.HopDongChiTietREF
                                                             WHERE  hdct.DeletedStatus = 0
                                                                    AND (hdct.DonViTinhREF = 32  OR hdct.DonViTinhREF = 31)--True View, true reach
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
                                    INNER JOIN ( SELECT C.* FROM dbo.HopDongChiTiet C 
										WHERE C.HopDongFK = @HopDongID 
										AND C.DeletedStatus = 0
										AND C.DmLoaiREF <> 13 --Khong tinh thuc chay cho HTQC Mua Ngoai
										AND C.DmLoaiREF <> 42
										AND C.DmSanPhamREF IN ( 240, 733)
										AND (UPPER(C.DonViTinh) = N'TRUE VIEW'  OR UPPER(C.DonViTinh) = N'TRUE REACH')
									)C ON C.HopDongChiTietID = A.HopDongChiTietREF
                                    INNER JOIN (SELECT * FROM dbo.HopDong WHERE HopDongID = @HopDongID AND TrangThaiHopDong <> 3) D ON D.HopDongID = C.HopDongFK
                               
                                   
                        ) TD
	
	
    END

```
