# Stored Procedure: `sp_TC_InsertThucChayDaTinh_Mobile_TinhLai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-07-05 11:40:51.580000
- **Ngày sửa cuối**: 2017-10-30 09:08:16.870000

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
| `@NgayTinhThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucChayDaTinh]
--EXEC [dbo].[sp_TC_InsertThucChayDaTinh_Mobile_TinhLai] '2017-06-01 00:00:00.000',	'SH0050617',	'gamek.vn',	109964,	10,	'CPM',	14,	519229,	25786,	72,	'2017-07-03 00:00:00.000'
--[ThucChay_InsertThucChayDaTinh_Mobile] '2014-06-09','QC2170314',3140,'cafef.vn',56937,10,'CPM',4,19956,	59
CREATE PROCEDURE [dbo].[sp_TC_InsertThucChayDaTinh_Mobile_TinhLai]
    @NgayThucHien DATETIME ,
    @SoHopDong NVARCHAR(50) ,
    @TenWebsite NVARCHAR(50) ,
    @HopDongChiTietID INT ,
    @TypeProduct INT ,
    @ProductUnitName NVARCHAR(50) ,
    @BannerType INT ,
    @DmBannerID INT ,
    @TongViewThucChay INT ,
    @TongClickThucChay INT,
	@NgayTinhThucHien DATETIME
AS
    BEGIN



        DECLARE @v_DmWebsiteREF INT ,
            @v_DsNhanHangREF NVARCHAR(200)
        SET @v_DmWebsiteREF = 0
        SET @v_DsNhanHangREF = ''
	
        SET @v_DmWebsiteREF = ( SELECT TOP 1
                                        DmWebsiteReportingdbID
                                FROM    DmWebsiteReportingdb
                                WHERE   DmWebsiteReportingdb.TenWebsite = @TenWebsite
                              )
        SET @v_DsNhanHangREF = [dbo].[f_ReturnListConcatNhanHangREF_MobileSingleBanner_BannerID](@SoHopDong,
                                                              @TypeProduct,
                                                              @HopDongChiTietID,
                                                              @v_DmWebsiteREF,
                                                              @NgayThucHien,
                                                              @ProductUnitName,
                                                              @DmBannerID)
	
        SET @v_DsNhanHangREF = ISNULL(@v_DsNhanHangREF, 0)

		

	
        INSERT  INTO dbo.ThucChayDaTinh
                SELECT  TC.*
                FROM    ( SELECT    NEWID() ThucChayDaTinhID ,
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
                                    0 SoLuongThucChay ,
                                    @NgayTinhThucHien NgayThucHien ,
                                    ISNULL(( TD.ThanhTienThucChayTruocTrietKhau
                                             - ( TD.ThanhTienThucChayTruocTrietKhau
                                                 * TD.ChietKhau ) / 100 ), 0) GiaTriThayDoi ,
                                    TD.ThanhTienThucChayTruocTrietKhau ,
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
                                           THEN ISNULL(dbo.fn_TC_GetSoLuongThucChayKMMobile(TD.HopDongChiTietREF,
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
                                           THEN ISNULL(dbo.fn_TC_GetSoLuongThucChayKMMobile(TD.HopDongChiTietREF,
                                                              1,
                                                              TD.DonGiaTheoDonViTinh,
                                                              TD.NgayThucHien,
                                                              TD.TongClickThucChay,
                                                              TD.DmBannerREF),
                                                       0)
                                           ELSE 0
                                      END ) AS SoLuongThucChayKM ,
                                    ( CASE WHEN ( TD.DonViTinh = 'VIEW' )
                                           THEN dbo.fn_TC_GetSoLuongLechTreoHaThucChayMobile(TD.HopDongChiTietREF,
                                                              TD.DonGiaTheoDonViTinh,
                                                              TD.NgayThucHien,
                                                              TD.TongViewThucChay,
                                                              TD.DmBannerREF)
                                           WHEN ( TD.DonViTinh = 'CLICK' )
                                           THEN dbo.fn_TC_GetSoLuongLechTreoHaThucChayMobile(TD.HopDongChiTietREF,
                                                              TD.DonGiaTheoDonViTinh,
                                                              TD.NgayThucHien,
                                                              TD.TongClickThucChay,
                                                              TD.DmBannerREF)
                                           ELSE 0
                                      END ) AS SoLuongLechTreoHa ,
                                    ( CASE WHEN ( TD.DonViTinh = 'VIEW' )
                                           THEN dbo.fn_TC_GetSoLuongLechTreoHaThucChayMobile(TD.HopDongChiTietREF,
                                                              TD.DonGiaTheoDonViTinh,
                                                              TD.NgayThucHien,
                                                              TD.TongViewThucChay,
                                                              TD.DmBannerREF)
                                                * TD.DonGiaTheoDonViTinh
                                                * ( 100 - TD.ChietKhau ) / 100
                                           WHEN ( TD.DonViTinh = 'CLICK' )
                                           THEN dbo.fn_TC_GetSoLuongLechTreoHaThucChayMobile(TD.HopDongChiTietREF,
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
                                    TD.SoLuongThucChay SoLuongThayDoi ,
                                    0 SoLuongKMThayDoi ,
                                    0 GiaTriKMThayDoi ,
                                    'Tinh lai Single Mobile' GhiChu
                          FROM      ( SELECT 
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
                                                C.HopDongChiTietID HopDongChiTietREF ,
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
                                                @v_DsNhanHangREF NhanHang ,
                                                C.DmNhomNganhREF ,
                                                C.TenNhomNganh , 
	--Thong tin hinh thuc quang cao
                                                C.DmLoaiREF AS DmHinhThucQuangCao ,
                                                C.TenLoai AS TenHinhThucQuangCao , 
	--Thong tin San pham
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
	--Thong tin ve Tien
	--****haidh chinh sua
                                                C.SoLuong
                                                * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong ,
                                                ( CASE WHEN C.DonViTinh = 'CPC'
                                                       THEN 'CLICK'
                                                       WHEN C.DonViTinh = 'CPM'
                                                       THEN 'VIEW'
                                                       WHEN C.DonViTinh = 'CPV'
                                                       THEN 'CPV'
	  --ELSE (case when @ProductUnitName = 'CPC' THEN 'CLICK'
			--WHEN @ProductUnitName = 'CPM' THEN 'VIEW'
			--END)
                                                       ELSE ( CASE
                                                              WHEN C.DonViTinh = N'Gói'
                                                              AND C.TenLoai = 'CPC'
                                                              THEN 'CLICK'
                                                              WHEN C.DonViTinh = N'Gói'
                                                              AND C.TenLoai = 'CPM'
                                                              THEN 'VIEW'
                                                              END )
                                                  END ) AS DonViTinh , -- tuyetnta sửa
	--dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,C.HopDongChiTietID,C.DonGia) as DonGia,
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
	----Thuc chay
                                                @DmBannerID DmBannerREF ,--A.DmBannerREF,
                                                0 DmChienDichREF ,--A.DmChienDichREF,
	--(SELECT TOP 1 DmWebsiteReportingdbID FROM DmWebsiteReportingdb WHERE DmWebsiteReportingdb.TenWebsite = @TenWebsite) DmWebsiteREF,
                                                @v_DmWebsiteREF DmWebsiteREF ,
                                                @TenWebsite TenWebsite ,
                                                @TongViewThucChay TongViewThucChay ,
                                                @TongClickThucChay TongClickThucChay ,
                                                0 TongSoBaiViet ,
                                                ISNULL(dbo.[fn_TC_GetSoLuongThucChayMobile](@HopDongChiTietID,
                                                              dbo.ThucChay_GetDonGiaTheoDonViTruocChietKhau(@HopDongChiTietID,
                                                              ( CASE
                                                              WHEN C.DonViTinh = N'Gói'
                                                              AND C.TenLoai = 'CPC'
                                                              THEN 'CPC'
                                                              WHEN C.DonViTinh = N'Gói'
                                                              AND C.TenLoai = 'CPM'
                                                              THEN 'CPM'
                                                              END ),
                                                              @BannerType,
                                                              @NgayThucHien),
                                                              --@NgayThucHien,
															  @NgayTinhThucHien,
                                                              @TongViewThucChay,
                                                              @TongClickThucChay,
                                                              CASE
                                                              WHEN C.DonViTinh IN (
                                                              'CPC', 'CPM',
                                                              'CPV' )
                                                              THEN C.DonViTinh
											--else @ProductUnitName 
                                                              ELSE ( CASE
                                                              WHEN C.DonViTinh = N'Gói'
                                                              AND C.TenLoai = 'CPC'
                                                              THEN 'CPC'
                                                              WHEN C.DonViTinh = N'Gói'
                                                              AND C.TenLoai = 'CPM'
                                                              THEN 'CPM'
                                                              END )
                                                              END, @DmBannerID), 0) AS SoLuongThucChay ,
                                                @NgayTinhThucHien NgayThucHien ,
                                                0 AS GiaTriThayDoi ,
                                                ISNULL(dbo.fn_TC_GetThanhTienChuanThucChay_Mobile(0,--@SoLuong 
                                                              @ProductUnitName,-- 
                                                              0,--@DonGia,
                                                              '',--@NgayKyHopDong,
                                                              @TongViewThucChay,
                                                              @TongClickThucChay,
                                                              @BannerType,
                                                              @NgayTinhThucHien,
                                                              @HopDongChiTietID,
                                                              @DmBannerID), 0) AS ThanhTienThucChayTruocTrietKhau
                                      FROM      HopDongChiTiet C
                                                INNER JOIN HopDong D ON D.HopDongID = C.HopDongFK
                                      WHERE     C.HopDongChiTietID = @HopDongChiTietID
                                                AND D.TrangThaiHopDong != 3
                                                AND C.DeletedStatus = 0
                                                AND C.DmSanPhamREF = 342
                                                AND C.DmLoaiBannerREF NOT IN (
                                                17, 18 )
												AND C.DmLoaiNenTangREF <> 8
												AND C.DmLoaiREF <> 42
                                    ) TD
                        ) TC
                WHERE   ( TC.GiaTriThayDoi > 0
                          OR TC.GiaTriKMThayDoi > 0
                        )
                        AND ( TC.GiaTriThayDoi IS NOT NULL
                              OR TC.GiaTriKMThayDoi IS NOT NULL
                            )
    END

```
