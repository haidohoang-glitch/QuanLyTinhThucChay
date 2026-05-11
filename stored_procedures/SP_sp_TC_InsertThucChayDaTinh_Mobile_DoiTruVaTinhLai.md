# Stored Procedure: `sp_TC_InsertThucChayDaTinh_Mobile_DoiTruVaTinhLai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-11-17 11:25:36.580000
- **Ngày sửa cuối**: 2018-04-04 10:23:04.353000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@TenWebsite` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@ProductUnitName` | `nvarchar(100)` | No |
| `@BannerType` | `int(4)` | No |
| `@DmBannerID` | `int(4)` | No |
| `@TongViewThucChay` | `int(4)` | No |
| `@TongClickThucChay` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucChayDaTinh]

--[ThucChay_InsertThucChayDaTinh_Mobile] '2014-06-09','QC2170314',3140,'cafef.vn',56937,10,'CPM',4,19956,	59
CREATE PROCEDURE [dbo].[sp_TC_InsertThucChayDaTinh_Mobile_DoiTruVaTinhLai]
    @NgayThucHien DATETIME ,
    @SoHopDong NVARCHAR(50) ,
    @TenWebsite NVARCHAR(50) ,
    @HopDongChiTietID INT ,
    @TypeProduct INT ,
    @ProductUnitName NVARCHAR(50) ,
    @BannerType INT ,
    @DmBannerID INT ,
    @TongViewThucChay INT ,
    @TongClickThucChay INT
AS
    BEGIN
		
        DECLARE @v_DmWebsiteREF INT ,
            @v_DsNhanHangREF NVARCHAR(200)
        SET @v_DmWebsiteREF = 0
        SET @v_DsNhanHangREF = ''
	
        SET @v_DmWebsiteREF = ( SELECT TOP (1)
                                        DmWebsiteReportingdbID
                                FROM    dbo.DmWebsiteReportingdb
                                WHERE   DmWebsiteReportingdb.TenWebsite = @TenWebsite
								ORDER BY DmWebsiteReportingdbID
                              )
        SET @v_DsNhanHangREF = [dbo].[f_ReturnListConcatNhanHangREF_MobileSingleBanner_BannerID](@SoHopDong,
                                                              @TypeProduct,
                                                              @HopDongChiTietID,
                                                              @v_DmWebsiteREF,
                                                              @NgayThucHien,
                                                              @ProductUnitName,
                                                              @DmBannerID)
	
        SET @v_DsNhanHangREF = ISNULL(@v_DsNhanHangREF, 0)

        INSERT  INTO dbo.ThucChayDaTinh_DoiTruVaTinhLai_Mobile
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
                SELECT  TC.ThucChayDaTinhID ,TC.HopDongID, TC.SoHopDong, TC.DmMaHopDongREF, TC.TenMaHopDong, TC.NgayDanhSoHopDong, TC.NgayKyHopDong
                                  , TC.NhanHopDong, TC.NgayNhanBanFax, TC.NgayNhanHopDongBanCung, TC.NgayChuyenHopDongChoKeToan
                                  , TC.So, TC.Thang, TC.Nam, TC.GiaTriHopDong, TC.CongNo, TC.HopDongChiTietREF, TC.DangSuDung
                                  , TC.IsGiayPhep, TC.TrangThaiHopDong, TC.IsBanCung, TC.DmPhongBanREF, TC.TenPhongBan, TC.DmBoPhanREF, TC.TenBoPhan, TC.DmNhomLamViecREF
								  --hopdongchi tiet
                                  , TC.TenNhom, TC.DmDiaDiemLamViecREF, TC.TenDiaDiemLamViec, TC.SysNhanVienREF, TC.TenDangNhap, TC.TenNhanVien, TC.TenKhachHang
                                  , TC.NhanHang, TC.DmNhomNganhREF, TC.TenNhomNganh, TC.DmHinhThucQuangCao, TC.TenHinhThucQuangCao, TC.DmSanPhamREF, TC.TenSanPham
                                  , TC.DmNhomWebsiteREF, TC.TenNhomWebsite, TC.DmChuyenMucREF, TC.TenChuyenMuc, TC.DmLoaiBannerREF, TC.TenLoaiBanner
								  , TC.DmViTriREF, TC.TenViTri
								  --thong tin soluong, thanhtien, dongia, donvitinh,... cua hopdongchitiet
                                  , TC.DotChayHopDong, TC.SoLuongDotChayHD, TC.DotChayBooking, TC.SoLuongDotChayBooking
                                  , TC.SoLuong, TC.DonViTinh, TC.DonGia, TC.DonGiaTheoDonViTinh, TC.ChietKhau, TC.GiamGia, TC.ThanhTien
								  , TC.TiLeTuVan, TC.ChiPhiTuVan, TC.IsKhuyenMai, TC.KhuyenMai
                                  , TC.DmBannerREF, TC.DmChienDichREF, TC.DmWebsiteREF, TC.TenWebsite, TC.TongViewThucChay, TC.TongClickThucChay, TC.TongSoBaiViet
                                  , 0 SoLuongThucChay
                                  , TC.NgayThucHien
                                  , TC.ThanhTienSauTrietKhauThucChay GiaTriThayDoi
                                  , 0 ThanhTienThucChayTruocTrietKhau 
								  , 0 GiaTriTrietKhauThucChay 
								  , 0 ThanhTienSauTrietKhauThucChay 
								  , 0 GiaTriHoaHongThucChay 
								  , TC.ThanhTienSauTrietKhauThucChay AS ThanhTienThucThu 
								  , 0 ThanhTienKM 
								  , 0 SoLuongThucChayKM 
								  , TC.SoLuongLechTreoHa 
								  , TC.ThanhTienLechTreoHa 
								  , TC.CreatedAt, TC.LastModifiedAt, TC.IsPheDuyet, TC.PheDuyetBy, TC.PheDuyetAt 
								  , TC.SoLuongThucChay AS SoLuongThayDoi 
								  , TC.SoLuongThucChayKM SoLuongKMThayDoi 
								  , TC.ThanhTienKM AS GiaTriKMThayDoi 
								  , TC.GhiChu
                FROM    ( SELECT    NEWID() ThucChayDaTinhID ,
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
                                                )
                                           THEN ISNULL(dbo.fn_TC_GetSoLuongThucChayKMMobile_DoiTruVaTinhLai(TD.HopDongChiTietREF,
                                                              1,
                                                              TD.DonGiaTheoDonViTinh,
                                                              TD.NgayThucHien,
                                                              TD.TongViewThucChay,
                                                              TD.DmBannerREF),
                                                       0)
                                           WHEN ( ( ( TD.IsKhuyenMai = 1 )
                                                    OR ( TD.ChietKhau = 100 )
                                                  )
                                                  AND ( TD.DonViTinh = 'CLICK' )
                                                )
                                           THEN ISNULL(dbo.fn_TC_GetSoLuongThucChayKMMobile_DoiTruVaTinhLai(TD.HopDongChiTietREF,
                                                              1,
                                                              TD.DonGiaTheoDonViTinh,
                                                              TD.NgayThucHien,
                                                              TD.TongClickThucChay,
                                                              TD.DmBannerREF),
                                                       0)
                                           ELSE 0
                                      END ) AS SoLuongThucChayKM ,
                                    ( CASE WHEN ( TD.DonViTinh = 'VIEW' )
                                           THEN dbo.fn_TC_GetSoLuongLechTreoHaThucChayMobile_DoiTruVaTinhLai(TD.HopDongChiTietREF,
                                                              TD.DonGiaTheoDonViTinh,
                                                              TD.NgayThucHien,
                                                              TD.TongViewThucChay,
                                                              TD.DmBannerREF)
                                           WHEN ( TD.DonViTinh = 'CLICK' )
                                           THEN dbo.fn_TC_GetSoLuongLechTreoHaThucChayMobile_DoiTruVaTinhLai(TD.HopDongChiTietREF,
                                                              TD.DonGiaTheoDonViTinh,
                                                              TD.NgayThucHien,
                                                              TD.TongClickThucChay,
                                                              TD.DmBannerREF)
                                           ELSE 0
                                      END ) AS SoLuongLechTreoHa ,
                                    ( CASE WHEN ( TD.DonViTinh = 'VIEW' )
                                           THEN dbo.fn_TC_GetSoLuongLechTreoHaThucChayMobile_DoiTruVaTinhLai(TD.HopDongChiTietREF,
                                                              TD.DonGiaTheoDonViTinh,
                                                              TD.NgayThucHien,
                                                              TD.TongViewThucChay,
                                                              TD.DmBannerREF)
                                                * TD.DonGiaTheoDonViTinh
                                                * ( 100 - TD.ChietKhau ) / 100
                                           WHEN ( TD.DonViTinh = 'CLICK' )
                                           THEN dbo.fn_TC_GetSoLuongLechTreoHaThucChayMobile_DoiTruVaTinhLai(TD.HopDongChiTietREF,
                                                              TD.DonGiaTheoDonViTinh,
                                                              TD.NgayThucHien,
                                                              TD.TongClickThucChay,
                                                              TD.DmBannerREF)
                                                * TD.DonGiaTheoDonViTinh
                                                * ( 100 - TD.ChietKhau ) / 100
                                           ELSE 0
                                      END ) AS ThanhTienLechTreoHa ,
                                    GETDATE() CreatedAt ,
                                    GETDATE() LastModifiedAt ,
                                    0 IsPheDuyet ,
                                    '' PheDuyetBy ,
                                    '' PheDuyetAt ,
                                    0 SoLuongThayDoi ,
                                    0 SoLuongKMThayDoi ,
                                    0 GiaTriKMThayDoi ,
                                    N'sp_TC_InsertThucChayDaTinh_Mobile_DoiTruVaTinhLai' GhiChu
                          FROM      ( SELECT 
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
                                                C.HopDongChiTietID HopDongChiTietREF ,
                                                D.DangSuDung ,
												D.IsBanCung,
                                                D.IsGiayPhep ,
                                                D.TrangThaiHopDong ,
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
                                                @v_DsNhanHangREF NhanHang ,
                                                C.DmNhomNganhREF ,
                                                C.TenNhomNganh , 
                                                C.DmLoaiREF AS DmHinhThucQuangCao ,
                                                C.TenLoai AS TenHinhThucQuangCao , 
                                                dbo.GetProductIDByTypeProduct(@TypeProduct) AS DmSanPhamREF ,
                                                dbo.GetProductNameByTypeProduct(@TypeProduct) AS TenSanPham ,
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
                                                0 SoLuongDotChayBooking ,
                                                C.SoLuong
                                                * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong ,
                                                ( CASE WHEN C.DonViTinh = 'CPC'
                                                       THEN 'CLICK'
                                                       WHEN C.DonViTinh = 'CPM'
                                                       THEN 'VIEW'
                                                       WHEN C.DonViTinh = 'CPV'
                                                       THEN 'CPV'
                                                       ELSE ( CASE
                                                              WHEN C.DonViTinh = N'Gói'
                                                              AND C.TenLoai = 'CPC'
                                                              THEN 'CLICK'
                                                              WHEN C.DonViTinh = N'Gói'
                                                              AND C.TenLoai = 'CPM'
                                                              THEN 'VIEW'
                                                              END )
                                                  END ) AS DonViTinh , -- tuyetnta sửa
                                                ISNULL(dbo.ThucChay_GetDonGiaTheoDonViTruocChietKhau(C.HopDongChiTietID,-- @ProductUnitName
                                                              ( CASE
                                                              WHEN C.DonViTinh IN (
                                                              'CPC', 'CPM' )
                                                              THEN C.DonViTinh
                                                              WHEN C.DonViTinh = N'Gói'
                                                              AND C.TenLoai = 'CPC'
                                                              THEN 'CPC'
                                                              WHEN C.DonViTinh = N'Gói'
                                                              AND C.TenLoai = 'CPM'
                                                              THEN 'CPM'
                                                              END ),
                                                              @BannerType,
                                                              @NgayThucHien), 0) AS DonGia ,
                                                ISNULL(dbo.ThucChay_GetDonGiaTheoDonViTruocChietKhau(C.HopDongChiTietID,--@ProductUnitName,
                                                              ( CASE
                                                              WHEN C.DonViTinh IN (
                                                              'CPC', 'CPM' )
                                                              THEN C.DonViTinh
                                                              WHEN C.DonViTinh = N'Gói'
                                                              AND C.TenLoai = 'CPC'
                                                              THEN 'CPC'
                                                              WHEN C.DonViTinh = N'Gói'
                                                              AND C.TenLoai = 'CPM'
                                                              THEN 'CPM'
                                                              END ),
                                                              @BannerType,
                                                              @NgayThucHien), 0) AS DonGiaTheoDonViTinh ,
                                                C.ChietKhau ,
                                                C.GiamGia ,
                                                C.ThanhTien ,
                                                C.TiLeTuVan ,
                                                C.ChiPhiTuVan ,
                                                C.IsKhuyenMai ,
                                                C.KhuyenMai ,
                                                @DmBannerID DmBannerREF ,--A.DmBannerREF,
                                                0 DmChienDichREF ,--A.DmChienDichREF,
                                                @v_DmWebsiteREF DmWebsiteREF ,
                                                @TenWebsite TenWebsite ,
                                                @TongViewThucChay TongViewThucChay ,
                                                @TongClickThucChay TongClickThucChay ,
                                                0 TongSoBaiViet ,
                                                ISNULL(dbo.[fn_TC_GetSoLuongThucChayMobile_DoiTruVaTinhLai](@HopDongChiTietID,
                                                              dbo.ThucChay_GetDonGiaTheoDonViTruocChietKhau(@HopDongChiTietID,
                                                              ( CASE
                                                              WHEN C.DonViTinh = N'Gói' AND C.TenLoai = 'CPC' THEN 'CPC'
                                                              WHEN C.DonViTinh = N'Gói' AND C.TenLoai = 'CPM' THEN 'CPM'
															  ELSE ''
                                                              END ),
                                                              @BannerType,
                                                              @NgayThucHien),
                                                              @NgayThucHien,
                                                              @TongViewThucChay,
                                                              @TongClickThucChay,
                                                              CASE
                                                              WHEN C.DonViTinh IN ('CPC', 'CPM','CPV' ) THEN C.DonViTinh
                                                              ELSE ( CASE WHEN C.DonViTinh = N'Gói' AND C.TenLoai = 'CPC' THEN 'CPC'
																		WHEN C.DonViTinh = N'Gói' AND C.TenLoai = 'CPM' THEN 'CPM'
																		ELSE ''
																	END )
                                                              END, @DmBannerID), 0) AS SoLuongThucChay ,
                                                @NgayThucHien NgayThucHien ,
                                                0 AS GiaTriThayDoi ,
                                                ISNULL(dbo.fn_TC_GetThanhTienChuanThucChay_Mobile_DoiTruVaTinhLai(0,
                                                              @ProductUnitName,-- 
                                                              0,--@DonGia,
                                                              '',--@NgayKyHopDong,
                                                              @TongViewThucChay,
                                                              @TongClickThucChay,
                                                              @BannerType,
                                                              @NgayThucHien,
                                                              @HopDongChiTietID,
                                                              @DmBannerID), 0) AS ThanhTienThucChayTruocTrietKhau
                                      FROM      (SELECT * FROM dbo.HopDongChiTiet  C
												WHERE C.HopDongChiTietID = @HopDongChiTietID
												AND C.DeletedStatus = 0
                                                AND C.DeletedStatus = 0
                                                AND C.DmSanPhamREF = 342
                                                AND C.DmLoaiBannerREF NOT IN (17, 18 )
												AND C.DmLoaiNenTangREF <> 8
												AND C.DmLoaiREF <> 42 ) C
                                                INNER JOIN dbo.HopDong D ON D.HopDongID = C.HopDongFK
                                      WHERE    1=1
                                                AND D.TrangThaiHopDong <> 3
                                    ) TD
                        ) TC
                WHERE   ( TC.SoLuongThucChay > 0
                          OR TC.SoLuongThucChayKM > 0
                          OR TC.SoLuongLechTreoHa > 0
                        )
                        AND ( TC.SoLuongThucChay IS NOT NULL
                              OR TC.SoLuongThucChayKM IS NOT NULL
                              OR TC.SoLuongLechTreoHa IS NOT NULL
                            )
    END

```
