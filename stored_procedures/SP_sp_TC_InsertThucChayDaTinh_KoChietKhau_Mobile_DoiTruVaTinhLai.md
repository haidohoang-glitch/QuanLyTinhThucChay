# Stored Procedure: `sp_TC_InsertThucChayDaTinh_KoChietKhau_Mobile_DoiTruVaTinhLai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-11-17 11:33:23.873000
- **Ngày sửa cuối**: 2018-04-04 11:14:03.167000

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
CREATE PROCEDURE [dbo].[sp_TC_InsertThucChayDaTinh_KoChietKhau_Mobile_DoiTruVaTinhLai]
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
                SELECT  TC.ThucChayDaTinhID ,
                                    TC.HopDongID ,TC.SoHopDong ,TC.DmMaHopDongREF ,TC.TenMaHopDong ,
									TC.NgayDanhSoHopDong ,TC.NgayKyHopDong ,TC.NhanHopDong ,TC.NgayNhanBanFax ,TC.NgayNhanHopDongBanCung ,TC.NgayChuyenHopDongChoKeToan ,
                                    TC.So ,TC.Thang ,TC.Nam ,TC.GiaTriHopDong ,TC.CongNo ,TC.HopDongChiTietREF ,
                                    TC.DangSuDung ,TC.IsGiayPhep ,TC.TrangThaiHopDong ,TC.IsBanCung , 
                                    TC.DmPhongBanREF ,TC.TenPhongBan ,TC.DmBoPhanREF ,TC.TenBoPhan ,TC.DmNhomLamViecREF ,TC.TenNhom ,TC.DmDiaDiemLamViecREF ,TC.TenDiaDiemLamViec ,
                                    TC.SysNhanVienREF ,TC.TenDangNhap ,TC.TenNhanVien ,TC.TenKhachHang ,
									---thong tin hopdongchitiet
									TC.NhanHang ,TC.DmNhomNganhREF ,TC.TenNhomNganh ,TC.DmHinhThucQuangCao ,TC.TenHinhThucQuangCao , 
                                    TC.DmSanPhamREF ,TC.TenSanPham ,TC.DmNhomWebsiteREF ,TC.TenNhomWebsite ,TC.DmChuyenMucREF ,TC.TenChuyenMuc ,
                                    TC.DmLoaiBannerREF ,TC.TenLoaiBanner ,TC.DmViTriREF ,TC.TenViTri ,
									TC.DotChayHopDong ,TC.SoLuongDotChayHD ,TC.DotChayBooking ,TC.SoLuongDotChayBooking ,
									---thong tin soluong, dongia, donvitinh, chietkhau,... cua hopdongchitiet
                                    TC.SoLuong, TC.DonViTinh ,TC.DonGia ,TC.DonGiaTheoDonViTinh ,
									TC.ChietKhau ,TC.GiamGia ,TC.ThanhTien ,TC.TiLeTuVan ,TC.ChiPhiTuVan ,TC.IsKhuyenMai ,TC.KhuyenMai ,
                                    TC.DmBannerREF ,TC.DmChienDichREF ,TC.DmWebsiteREF ,TC.TenWebsite ,
                                    TC.TongViewThucChay ,TC.TongClickThucChay ,TC.TongSoBaiViet ,

                                    0 AS SoLuongThucChay ,
                                    TC.NgayThucHien ,
                                    TC.ThanhTienSauTrietKhauThucChay AS GiaTriThayDoi ,
                                    0 AS ThanhTienThucChayTruocTrietKhau ,
									0 AS GiaTriTrietKhauThucChay ,
									0 AS ThanhTienSauTrietKhauThucChay ,
									0 AS GiaTriHoaHongThucChay ,
									TC.ThanhTienSauTrietKhauThucChay AS ThanhTienThucThu ,
									0 AS ThanhTienKM ,
									0 AS SoLuongThucChayKM ,
									TC.SoLuongLechTreoHa ,
									TC.ThanhTienLechTreoHa ,
									TC.CreatedAt ,TC.LastModifiedAt ,TC.IsPheDuyet ,TC.PheDuyetBy ,TC.PheDuyetAt ,
									TC.SoLuongThucChay AS SoLuongThayDoi ,
									TC.SoLuongThucChayKM AS SoLuongKMThayDoi ,
									TC.ThanhTienKM AS GiaTriKMThayDoi ,
									TC.GhiChu
                FROM    ( SELECT    NEWID() ThucChayDaTinhID ,
                                    TD.* ,
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
                                           THEN dbo.fn_TC_GetSoLuongLechTreoHaThucChayMobile_KoChietKhau_DoiTruVaTinhLai(TD.HopDongChiTietREF,
                                                              TD.DonGiaTheoDonViTinh,
                                                              TD.NgayThucHien,
                                                              TD.TongViewThucChay,
                                                              TD.DmBannerREF,
															  @v_DmWebsiteREF)
                                           WHEN ( TD.DonViTinh = 'CLICK' )
                                           THEN dbo.fn_TC_GetSoLuongLechTreoHaThucChayMobile_KoChietKhau_DoiTruVaTinhLai(TD.HopDongChiTietREF,
                                                              TD.DonGiaTheoDonViTinh,
                                                              TD.NgayThucHien,
                                                              TD.TongClickThucChay,
                                                              TD.DmBannerREF,
															  @v_DmWebsiteREF)
                                           ELSE 0
                                      END ) AS SoLuongLechTreoHa ,
                                    ( CASE WHEN ( TD.DonViTinh = 'VIEW' )
                                           THEN dbo.fn_TC_GetSoLuongLechTreoHaThucChayMobile_KoChietKhau_DoiTruVaTinhLai(TD.HopDongChiTietREF,
                                                              TD.DonGiaTheoDonViTinh,
                                                              TD.NgayThucHien,
                                                              TD.TongViewThucChay,
                                                              TD.DmBannerREF,
															  @v_DmWebsiteREF)
                                                * TD.DonGiaTheoDonViTinh
                                                * ( 100 - TD.ChietKhau ) / 100
                                           WHEN ( TD.DonViTinh = 'CLICK' )
                                           THEN dbo.fn_TC_GetSoLuongLechTreoHaThucChayMobile_KoChietKhau_DoiTruVaTinhLai(TD.HopDongChiTietREF,
                                                              TD.DonGiaTheoDonViTinh,
                                                              TD.NgayThucHien,
                                                              TD.TongClickThucChay,
                                                              TD.DmBannerREF,
															  @v_DmWebsiteREF)
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
                                    N'sp_TC_InsertThucChayDaTinh_KoChietKhau_Mobile_DoiTruVaTinhLai' GhiChu
                          FROM      ( SELECT 
	--ID Hop Dong
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
                                                ( CASE WHEN C.DonViTinh = 'CPC' THEN 'CLICK'
                                                       WHEN C.DonViTinh = 'CPM' THEN 'VIEW'
                                                       WHEN C.DonViTinh = 'CPV' THEN 'CPV'
                                                       ELSE ( CASE WHEN C.DonViTinh = N'Gói' AND C.TenLoai = 'CPC' THEN 'CLICK'
                                                              WHEN C.DonViTinh = N'Gói' AND C.TenLoai = 'CPM' THEN 'VIEW'
															  ELSE ''
                                                              END )
                                                  END ) AS DonViTinh , -- tuyetnta sửa
                                                dbo.ThucChay_GetDonGiaTheoDonViTruocChietKhau(C.HopDongChiTietID,-- @ProductUnitName
                                                              ( CASE WHEN C.DonViTinh IN ('CPC', 'CPM' ) THEN C.DonViTinh
																  WHEN C.DonViTinh = N'Gói' AND C.TenLoai = 'CPC' THEN 'CPC'
																  WHEN C.DonViTinh = N'Gói' AND C.TenLoai = 'CPM' THEN 'CPM'
																  ELSE ''
                                                              END ),
                                                              @BannerType,
                                                              @NgayThucHien) AS DonGia ,
                                                dbo.ThucChay_GetDonGiaTheoDonViTruocChietKhau(C.HopDongChiTietID,--@ProductUnitName,
                                                              ( CASE WHEN C.DonViTinh IN ('CPC', 'CPM' ) THEN C.DonViTinh
																  WHEN C.DonViTinh = N'Gói' AND C.TenLoai = 'CPC' THEN 'CPC'
																  WHEN C.DonViTinh = N'Gói' AND C.TenLoai = 'CPM' THEN 'CPM'
																  ELSE ''
                                                              END ),
                                                              @BannerType,
                                                              @NgayThucHien) AS DonGiaTheoDonViTinh ,
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
                                                ISNULL(dbo.[fn_TC_GetSoLuongThucChayMobile_KoChietKhau_DoiTruVaTinhLai](@HopDongChiTietID,
                                                              dbo.ThucChay_GetDonGiaTheoDonViTruocChietKhau(@HopDongChiTietID,
                                                              ( CASE WHEN C.DonViTinh = N'Gói' AND C.TenLoai = 'CPC' THEN 'CPC'
																  WHEN C.DonViTinh = N'Gói' AND C.TenLoai = 'CPM' THEN 'CPM'
																  ELSE ''
                                                              END ),
                                                              @BannerType,
                                                              @NgayThucHien),
                                                              @NgayThucHien,
                                                              @TongViewThucChay,
                                                              @TongClickThucChay,
                                                              CASE WHEN C.DonViTinh IN ('CPC', 'CPM','CPV' ) THEN C.DonViTinh
                                                              ELSE ( CASE WHEN C.DonViTinh = N'Gói' AND C.TenLoai = 'CPC' THEN 'CPC'
																  WHEN C.DonViTinh = N'Gói' AND C.TenLoai = 'CPM' THEN 'CPM'
																  ELSE ''
                                                              END )
                                                              END, @DmBannerID, @v_DmWebsiteREF), 0) AS SoLuongThucChay ,
                                                @NgayThucHien NgayThucHien ,
                                                0 AS GiaTriThayDoi ,
                                                ISNULL(dbo.fn_TC_GetThanhTienChuanThucChay_Mobile_KoChietKhau_DoiTruVaTinhLai(0,--@SoLuong 
                                                              @ProductUnitName,-- 
                                                              0,--@DonGia,
                                                              '',--@NgayKyHopDong,
                                                              @TongViewThucChay,
                                                              @TongClickThucChay,
                                                              @BannerType,
                                                              @NgayThucHien,
                                                              @HopDongChiTietID,
                                                              @DmBannerID, @v_DmWebsiteREF), 0) AS ThanhTienThucChayTruocTrietKhau
                                      FROM      (SELECT * FROM dbo.HopDongChiTiet C 
												WHERE C.HopDongChiTietID = @HopDongChiTietID
												AND C.DeletedStatus = 0
                                                AND C.DmSanPhamREF = 342
                                                AND C.DmLoaiBannerREF NOT IN (17, 18 )
												AND C.DmLoaiNenTangREF <> 8)C
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

				DECLARE @TongSoLuongLechTreoHa FLOAT
				DECLARE @SoLuongLechTreoHa FLOAT

				SELECT @TongSoLuongLechTreoHa = SUM(tcdt.SoLuongThucChayLechTreoHa) 
						FROM dbo.ThucChayDaTinh_DoiTruVaTinhLai_Mobile tcdt 
						WHERE tcdt.NgayThucHien = @NgayThucHien
								AND tcdt.DmBannerREF = @DmBannerID
								AND tcdt.DmSanPhamREF = 342

				IF ISNULL(@TongSoLuongLechTreoHa, 0) > 0
					BEGIN

						-- Xac dinh so luong lech treo ha
						SELECT @SoLuongLechTreoHa = SUM(tcdt.SoLuongThucChayLechTreoHa) 
						FROM dbo.ThucChayDaTinh_DoiTruVaTinhLai_Mobile tcdt 
						WHERE tcdt.NgayThucHien = @NgayThucHien
								AND tcdt.DmBannerREF = @DmBannerID
								AND tcdt.DmWebsiteREF = @v_DmWebsiteREF
								AND tcdt.DmSanPhamREF = 342

					    IF ISNULL(@SoLuongLechTreoHa, 0) > 0
							BEGIN
							    UPDATE dbo.ThucChayDaTinh_DoiTruVaTinhLai_Mobile SET SoLuongThucChayLechTreoHa = 0
											, ThanhTienLechTreoHa = 0
								WHERE DmBannerREF = @DmBannerID
									AND DmWebsiteREF = @v_DmWebsiteREF
									AND DmSanPhamREF = 342
									AND NgayThucHien = @NgayThucHien
									AND HopDongChiTietREF <> @HopDongChiTietID
							END

					END

    END

```
