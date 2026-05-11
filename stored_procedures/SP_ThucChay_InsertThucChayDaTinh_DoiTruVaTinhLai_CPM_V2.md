# Stored Procedure: `ThucChay_InsertThucChayDaTinh_DoiTruVaTinhLai_CPM_V2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2023-08-15 16:21:44.840000
- **Ngày sửa cuối**: 2024-10-14 17:04:56.360000

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


CREATE  PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_DoiTruVaTinhLai_CPM_V2]
    @NgayThucHien DATETIME ,
    @SoHopDong NVARCHAR(50) ,
    @TypeProduct INT ,
    @DmWebsiteREF INT ,
    @TenWebsite NVARCHAR(50) ,
    @DmBannerREF INT ,
	@pHopDongChiTietID INT,
	@NgayTinh DATETIME
AS
    BEGIN

       INSERT  INTO dbo.[ThucChayDaTinh_DoiTruVaTinhLai_CPM]
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

	  OUTPUT INSERTED.[HopDongChiTietREF]
			,INSERTED.HopDongID 
           ,INSERTED.[DmSanPhamREF]
           ,INSERTED.CreatedAt
           ,0 [LoaiLog]
           ,N'[ThucChay_InsertThucChayDaTinh_DoiTruVaTinhLai_CPM_V2]' [ContentLog]
           ,'' [CreatedBy]
           ,INSERTED.[CreatedAt]
           ,'' [LastModifiedBy]
           ,INSERTED.[LastModifiedAt]
		INTO [dbo].[ThongTinThucChayLog]
           ([HopDongChiTietREF]
           ,[HopDongFK]
           ,[DmSanPhamREF]
           ,[ThoiGianLog]
           ,[LoaiLog]
           ,[ContentLog]
           ,[CreatedBy]
           ,[CreatedAt]
           ,[LastModifiedBy]
           ,[LastModifiedAt])
		   
      SELECT TCDT.ThucChayDaTinhID ,
                        TCDT.HopDongID , TCDT.SoHopDong, TCDT.DmMaHopDongREF, TCDT.TenMaHopDong
                      , TCDT.NgayDanhSoHopDong, TCDT.NgayKyHopDong
                      , TCDT.NhanHopDong, TCDT.NgayNhanBanFax
                      , TCDT.NgayNhanHopDongBanCung, TCDT.NgayChuyenHopDongChoKeToan
                      , TCDT.So, TCDT.Thang, TCDT.Nam, TCDT.GiaTriHopDong
                      , TCDT.CongNo, TCDT.HopDongChiTietREF
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
                      , TCDT.GiaTriHoaHongThucChay
                      , TCDT.ThanhTienThucThu
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
					, TCDT.SoLuongThucChayKM AS SoLuongKMThayDoi
					, TCDT.ThanhTienKM AS GiaTriKMThayDoi
					, TCDT.GhiChu FROM
	  (
                SELECT  NEWID() AS ThucChayDaTinhID,
                        TD.HopDongID , TD.SoHopDong, TD.DmMaHopDongREF, TD.TenMaHopDong
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
                                    )
                               THEN ISNULL(dbo.[ThucChay_GetSoLuongThucChayChuanByDonViTinh_ByDoiTruCPM](TD.TongViewThucChay,
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
                               THEN ISNULL(dbo.[ThucChay_GetSoLuongThucChayChuanByDonViTinh_ByDoiTruCPM](TD.TongClickThucChay,
                                                              TD.SoLuong,
                                                              TD.DonViTinh,
                                                              TD.NgayThucHien,
                                                              TD.HopDongChiTietREF),
                                           0)
                               ELSE 0
                          END ) AS SoLuongThucChayKM ,
                        ( CASE WHEN ( TD.DonViTinh = 'VIEW' )
                               THEN dbo.[ThucChay_GetSoLuongLechTreoHa_ByDoiTruCPM](@NgayThucHien,
                                                              TD.SoHopDong,
                                                              TD.HopDongChiTietREF,
                                                              TD.SoLuong,
                                                              TD.DmSanPhamREF,
                                                              TD.TongViewThucChay)
                               WHEN ( TD.DonViTinh = 'CLICK' )
                               THEN dbo.[ThucChay_GetSoLuongLechTreoHa_ByDoiTruCPM](@NgayThucHien,
                                                              TD.SoHopDong,
                                                              TD.HopDongChiTietREF,
                                                              TD.SoLuong,
                                                              TD.DmSanPhamREF,
                                                              TD.TongClickThucChay)
                               ELSE 0
                          END ) AS SoLuongLechTreoHa ,
                        ( CASE WHEN ( TD.DonViTinh = 'VIEW' )
                               THEN dbo.[ThucChay_GetSoLuongLechTreoHa_ByDoiTruCPM](@NgayThucHien,
                                                              TD.SoHopDong,
                                                              TD.HopDongChiTietREF,
                                                              TD.SoLuong,
                                                              TD.DmSanPhamREF,
                                                              TD.TongViewThucChay)
                                    * TD.DonGiaTheoDonViTinh
                               WHEN ( TD.DonViTinh = 'CLICK' )
                               THEN dbo.[ThucChay_GetSoLuongLechTreoHa_ByDoiTruCPM](@NgayThucHien,
                                                              TD.SoHopDong,
                                                              TD.HopDongChiTietREF,
                                                              TD.SoLuong,
                                                              TD.DmSanPhamREF,
                                                              TD.TongClickThucChay)
                                    * TD.DonGiaTheoDonViTinh
                               ELSE 0
                          END ) AS ThanhTienLechTreoHa ,
                        GETDATE() AS CreatedAt,
                        GETDATE() AS LastModifiedAt,
                        0 IsPheDuyet ,
                        '' PheDuyetBy ,
                        '' PheDuyetAt ,
                        0 SoLuongThayDoi ,
                        0 SoLuongKMThayDoi ,
                        0 GiaTriKMThayDoi ,
                        N'ThucChay_InsertThucChayDaTinh_DoiTruVaTinhLai_CPM' GhiChu
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
                                    C.DmBannerREF DmViTriREF ,
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
                                    A.TongSoBaiViet ,
                                    ( CASE WHEN ( ( C.IsKhuyenMai = 0 )
                                                  AND ( ( UPPER(C.DonViTinh) = 'CPM' )
                                                        OR ( UPPER(C.DonViTinh) = 'TRUE REACH' )
                                                      )
                                                )
                                           THEN ISNULL(dbo.[ThucChay_GetSoLuongThucChayChuanByDonViTinh_ByDoiTruCPM](A.TongViewThucChay,
                                                              C.SoLuong,
                                                              C.DonViTinh,
                                                              A.NgayThucHien,
                                                              A.HopDongChiTietREF),
                                                       0)
                                           WHEN ( ( C.IsKhuyenMai = 0 )
                                                  AND (( UPPER(C.DonViTinh) = 'CPC' ) )
                                                )
                                           THEN ISNULL(dbo.[ThucChay_GetSoLuongThucChayChuanByDonViTinh_ByDoiTruCPM](A.TongClickThucChay,
                                                              C.SoLuong,
                                                              C.DonViTinh,
                                                              A.NgayThucHien,
                                                              A.HopDongChiTietREF),
                                                       0)
                                           ELSE 0
                                      END ) AS SoLuongThucChay ,
                                    A.NgayThucHien ,
                                    0 AS GiaTriThayDoi ,
                                    ISNULL(dbo.[ThucChay_GetThanhTienChuanThucChay_ByDoiTruCPM](C.SoLuong,
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
                                                [dbo].[f_ReturnListConcatNhanHangREFByBanner_gttd](@SoHopDong,
                                                              @TypeProduct,
                                                              B.HopDongChiTietREF,
                                                              A.DmWebsiteREF) DsNhanHangREF ,
                                                B.HopDongChiTietREF ,
                                                A.TypeProduct ,
                                                A.DmWebsiteREF ,
                                                A.TenWebsite ,
                                                A.DmBannerREF
                                      FROM      (SELECT A.* FROM dbo.ThucChayTemp_TinhLai A WHERE 1=1 
															AND A.SoHopDong = @SoHopDong
															AND A.TypeProduct = @TypeProduct
															AND A.DmWebsiteREF = @DmWebsiteREF
															AND A.DmBannerREF = @DmBannerREF 
												) A
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
															  WHERE B.HopDongChiTietREF = @pHopDongChiTietID
															  AND B.DeletedStatus = 0
                                                           ) B ON B.DmBannerID = CONVERT(NVARCHAR(50), A.DmBannerREF)
                                      WHERE     1=1
                                      GROUP BY  A.NgayThucHien ,
                                                B.HopDongChiTietREF ,
                                                A.TypeProduct ,
                                                A.TenWebsite ,
                                                A.DmWebsiteREF ,
                                                A.DmBannerREF
                                    ) A
                                    INNER JOIN (SELECT C.* FROM dbo.HopDongChiTiet C WHERE C.HopDongChiTietID = @pHopDongChiTietID
												AND C.DeletedStatus = 0
												AND C.DmSanPhamREF IN ( 231, 238, 339, 240,370, 598, 613, 735, 5056 )
												AND C.DmLoaiBannerREF NOT IN ( 17, 18 )--Khong tinh cho cac loai banner ChiPhi va Mua ngoai
												AND C.DmLoaiREF <> 13 --Khong tinh thuc chay cho HTQC Mua Ngoai
												AND C.DonViTinhREF <> 31 --Don vi tinh la TRUE REACH
												AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](C.DonViTinhREF,C.DonViTinh) = 3 --Đơn vị của hình thức CPM
									) C ON C.HopDongChiTietID = A.HopDongChiTietREF
                                    INNER JOIN (SELECT D.* FROM dbo.HopDong D WHERE D.SoHopDong = @SoHopDong AND  D.TrangThaiHopDong <> 3) D ON D.HopDongID = C.HopDongFK
                                    INNER JOIN dbo.DmWebsite E ON E.DmWebsiteID = C.DmWebsiteREF
                          WHERE  1=1  
                           
                        ) TD
					)TCDT

    END

```
