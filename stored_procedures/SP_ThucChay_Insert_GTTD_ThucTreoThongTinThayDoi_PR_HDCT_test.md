# Stored Procedure: `ThucChay_Insert_GTTD_ThucTreoThongTinThayDoi_PR_HDCT_test`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-01-04 18:08:20.360000
- **Ngày sửa cuối**: 2021-01-04 18:08:20.360000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayHopDongChiTietPRID` | `int(4)` | No |
| `@HopDongID` | `int(4)` | No |
| `@NgaythucHien` | `datetime(8)` | No |
| `@GhiChu` | `nvarchar(1000)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [sp_TC_InsertThucTreoThongTinThayDoi_PR_HDCT]
--[ThucChay_Insert_GTTD_ThucTreoThongTinThayDoi_PR_HDCT]


create PROCEDURE [dbo].[ThucChay_Insert_GTTD_ThucTreoThongTinThayDoi_PR_HDCT_test]
    @ThucChayHopDongChiTietPRID INT ,
    @HopDongID INT ,
    @NgaythucHien DATETIME ,
    @GhiChu NVARCHAR(500) ,
    @HopDongChiTietID INT
AS
    BEGIN
        DECLARE @NgayGioiHanTinh DATETIME ,
            @NoteThongTinThayDoiGiam NVARCHAR(200), @NoteThongTinThayDoiTang NVARCHAR(200) 
        SET @NgayGioiHanTinh = '2019-01-01'
        SET @NoteThongTinThayDoiGiam = 'PSGTTD_PR_HDCT_2020'
		SET @NoteThongTinThayDoiTang = 'PSTTTD_PR_HDCT_2020'
	
		

		
		INSERT INTO dbo.ThucChayDaTinh
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
		SELECT  NEWID() , T.HopDongID,
                          T.SoHopDong,
                          T.DmMaHopDongREF,
                          T.TenMaHopDong,
                          T.NgayDanhSoHopDong,
                          T.NgayKyHopDong,
                          T.NhanHopDong,
                          T.NgayNhanBanFax,
                          T.NgayNhanHopDongBanCung,
                          T.NgayChuyenHopDongChoKeToan,
                          T.So,
                          T.Thang,
                          T.Nam,
                          T.GiaTriHopDong,
                          T.CongNo,
                          T.HopDongChiTietREF,
                          T.DangSuDung,
                          T.IsGiayPhep,
                          T.TrangThaiHopDong,
                          T.IsBanCung,
                          T.DmPhongBanREF,
                          T.TenPhongBan,
                          T.DmBoPhanREF,
                          T.TenBoPhan,
                          T.DmNhomLamViecREF,
                          T.TenNhom,
                          T.DmDiaDiemLamViecREF,
                          T.TenDiaDiemLamViec,
                          T.SysNhanVienREF,
                          T.TenDangNhap,
                          T.TenNhanVien,
                          T.TenKhachHang,
                          T.NhanHang,
                          T.DmNhomNganhREF,
                          T.TenNhomNganh,
                          T.DmHinhThucQuangCao,
                          T.TenHinhThucQuangCao,
                          T.DmSanPhamREF,
                          T.TenSanPham,
                          T.DmNhomWebsiteREF,
                          T.TenNhomWebsite,
                          T.DmChuyenMucREF,
                          T.TenChuyenMuc,
                          T.DmLoaiBannerREF,
                          T.TenLoaiBanner,
                          T.DmViTriREF,
                          T.TenViTri,
                          T.DotChayHopDong,
                          T.SoLuongDotChayHD,
                          T.DotChayBooking,
                          T.SoLuongDotChayBooking,
                          T.SoLuong,
                          T.DonViTinh,
                          T.DonGia,
                          T.DonGiaTheoDonViTinh,
                          T.ChietKhau,
                          T.GiamGia,
                          T.ThanhTien,
                          T.TiLeTuVan,
                          T.ChiPhiTuVan,
                          T.IsKhuyenMai,
                          T.KhuyenMai,
                          T.DmBannerREF,
                          T.DmChienDichREF,
                          T.DmWebsiteREF,
                          T.TenWebsite,
                          T.TongViewThucChay,
                          T.TongClickThucChay,
                          T.TongSoBaiViet,
                          0 AS SoLuongThucChay,
                          T.NgayThucHien,
                          T.ThanhTienThucChaySauChietKhau AS GiaTriThayDoi,
                          0 AS ThanhTienThucChayTruocChietKhau,
                          0 AS GiaTriTrietKhauThucChay,
                          0 AS ThanhTienThucChaySauChietKhau,
                          0 AS GiaTriHoaHongThucChay,
                          0 AS ThanhTienThucThu,
                          0 AS ThanhTienKM,
                          0 AS SoLuongThucChayKM,
                          0 AS SoLuongLechTreoHa,
                          0 AS ThanhTienLechTreoHa,
                          T.CreatedAt,
                          T.LastModifiedAt,
                          T.IsPheDuyet,
                          T.PheDuyetBy,
                          T.PheDuyetAt,
                          T.SoLuongThucChay AS SoLuongThayDoi,
                          T.SoLuongThucChayKM AS SoLuongKMThayDoi,
                          T.ThanhTienKM AS GiaTriKMThayDoi,
                          T.GhiChu
		FROM    ( SELECT  DISTINCT
							hd.HopDongID ,
							hd.SoHopDong ,
							hd.DmMaHopDongREF ,
							hd.TenMaHopDong ,
							hd.NgayDanhSoHopDong ,
							hd.NgayKyHopDong ,
							ISNULL(hd.NhanHopDong,
									'') AS NhanHopDong ,
							hd.NgayNhanBanFax ,
							hd.NgayNhanHopDongBanCung ,
							hd.NgayChuyenHopDongChoKeToan ,
							hd.So ,
							hd.Thang ,
							hd.Nam , 
							hd.GiaTriHopDong ,
							hd.CongNo ,
							tchpctpr.HopDongChiTietREF ,
							hd.DangSuDung ,
							hd.IsGiayPhep ,
							hd.TrangThaiHopDong ,
							hd.IsBanCung , 
							hd.DmPhongBanREF ,
							ISNULL(hd.TenPhongBan, '') AS TenPhongBan ,
							hd.DmBoPhanREF ,
							ISNULL(hd.TenBoPhan, '') AS TenBoPhan ,
							hd.DmNhomLamViecREF ,
							ISNULL(hd.TenNhom, '') AS TenNhom ,
							hd.DmDiaDiemLamViecREF ,
							ISNULL(hd.TenDiaDiemLamViec, '') AS TenDiaDiemLamViec ,
							hd.SysNhanVienREF ,
							ISNULL(hd.TenDangNhap, '') AS TenDangNhap ,
							hd.TenNhanVien ,
							hd.TenKhachHang ,
							tchpctpr.DmNhanHangREF AS NhanHang ,
							0 DmNhomNganhREF ,
							'' TenNhomNganh , 
							hdct.DmLoaiREF AS DmHinhThucQuangCao ,
							hdct.TenLoai AS TenHinhThucQuangCao , 
							hdct.DmSanPhamREF AS DmSanPhamREF ,
							hdct.TenSanPham ,
							0 DmNhomWebsiteREF ,
							'' TenNhomWebsite ,
							tchpctpr.DmChuyenMucREF ,
							tchpctpr.TenChuyenMuc ,
							hdct.DmLoaiBannerREF ,
							hdct.TenLoaiBanner ,
							tchpctpr.DmViTriREF ,
							tchpctpr.TenViTri ,
							@NoteThongTinThayDoiTang DotChayHopDong ,
							0 AS SoLuongDotChayHD ,
							tchpctpr.ThucChayHopDongChiTietPRID DotChayBooking ,
							0 AS SoLuongDotChayBooking , 
							hdct.SoLuong AS SoLuong ,
							dbo.FormatDonViTinh(hdct.DonViTinh) DonViTinh ,
							hdct.DonGia AS DonGia ,
							tchpctpr.GiaTien AS DonGiaTheoDonViTinh ,
							tchpctpr.ChietKhau ,
							hdct.GiamGia ,
							hdct.ThanhTien ,
							hdct.TiLeTuVan ,
							hdct.ChiPhiTuVan ,
							tchpctpr.KhuyenMai IsKhuyenMai ,
							'' KhuyenMai ,
							0 DmBannerREF ,--A.DmBannerREF,
							0 DmChienDichREF ,--A.DmChienDichREF,
							dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(tchpctpr.DmWebsiteREF) DmWebsiteREF ,
							dbo.GetWebsiteLinkByDmWebsiteID(tchpctpr.DmWebsiteREF,
									tchpctpr.TenWebsite) TenWebsite ,
							0 TongViewThucChay ,
							0 TongClickThucChay ,
							0 TongSoBaiViet ,
							( CASE WHEN  tchpctpr.ChietKhau <> 100 THEN ISNULL(tchpctpr.SoLuong, 0)
									ELSE 0
							END ) AS SoLuongThucChay ,
							@NgayThucHien AS NgayThucHien ,
							0 AS GiaTriThayDoi ,
							ISNULL([dbo].[ThucChay_GetThanhTienThucChayTruocChietKhau_PR]
							(
								-- Add the parameters for the function here
								hdct.HopDongFK,
								hdct.HopDongChiTietID,
								hdct.ChietKhau,
								hdct.ThanhTien,
								tchpctpr.SoLuong,
								tchpctpr.GiaTien,
								tchpctpr.ChietKhau
							),0) AS ThanhTienThucChayTruocChietKhau ,
							
							ISNULL(( CONVERT(FLOAT, ISNULL(tchpctpr.GiaTien, 0)) * CONVERT(FLOAT, ISNULL(tchpctpr.SoLuong, 0)) * CONVERT(FLOAT, tchpctpr.ChietKhau) )
									/ 100, 0) AS GiaTriTrietKhauThucChay ,

							ISNULL(tchpctpr.GiaTien, 0) * ISNULL(tchpctpr.SoLuong, 0) * ( CONVERT(FLOAT, ( 100 - tchpctpr.ChietKhau )) / 100 ) AS ThanhTienThucChaySauChietKhau ,

							( CONVERT(FLOAT, ( 100 - tchpctpr.ChietKhau )) * CONVERT(FLOAT, ( ISNULL(tchpctpr.GiaTien, 0) * ISNULL(tchpctpr.SoLuong, 0) )) / 100 )
								* ISNULL(hdct.TiLeTuVan, 0) / 100 AS GiaTriHoaHongThucChay ,

							( CASE WHEN ( tchpctpr.KhuyenMai = 1 OR tchpctpr.ChietKhau = 100 OR tchpctpr.GiaTien = 0 OR tchpctpr.SoLuong = 0 ) THEN 0
									ELSE ( 100 - hdct.TiLeTuVan ) / ( ISNULL(tchpctpr.GiaTien, 0) * ISNULL(tchpctpr.SoLuong, 0) * ( CONVERT(FLOAT, ( 100 - tchpctpr.ChietKhau )) / 100 ) )
								END ) AS ThanhTienThucThu ,

							( CASE WHEN tchpctpr.KhuyenMai = 1 OR tchpctpr.ChietKhau = 100 THEN ISNULL(tchpctpr.GiaTien, 0) * ISNULL(tchpctpr.SoLuong, 0)
									ELSE 0
								END ) AS ThanhTienKM ,

							( CASE WHEN tchpctpr.KhuyenMai = 1 OR tchpctpr.ChietKhau = 100 THEN ISNULL(tchpctpr.SoLuong, 0)
									ELSE 0
								END ) AS SoLuongThucChayKM ,

							0 SoLuongLechTreoHa ,
							0 ThanhTienLechTreoHa ,
							GETDATE() CreatedAt ,
							GETDATE() LastModifiedAt ,
							0 IsPheDuyet ,
							'' PheDuyetBy ,
							'' PheDuyetAt ,
							0 SoLuongThayDoi ,
							0 SoLuongKMThayDoi ,
							0 GiaTriKMThayDoi ,
							'' GhiChu
					FROM     (
										SELECT tchdctp.* FROM dbo.ThucChayHopDongChiTietPR tchdctp 
										WHERE tchdctp.DeletedStatus <> 1
										AND tchdctp.RecordStatus = 0
										AND tchdctp.HopDongREF = @HopDongID
										AND tchdctp.HopDongChiTietREF = @HopDongChiTietID
										AND tchdctp.ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID
										AND tchdctp.ThoiGianBatDau >= @NgayGioiHanTinh
										
							) tchpctpr
							INNER JOIN 
							(
								SELECT * FROM dbo.HopDongChiTiet hdct 
								WHERE hdct.HopDongFK = @HopDongID
								AND hdct.HopDongChiTietID = @HopDongChiTietID
								AND hdct.DmSanPhamREF in (141,245,250,637,305) --PR
								AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18)
							) hdct ON hdct.HopDongFK = tchpctpr.HopDongREF AND  hdct.HopDongChiTietID = tchpctpr.HopDongChiTietREF
							AND hdct.DmSanPhamREF = tchpctpr.DmSanPhamREF AND hdct.DmLoaiREF = tchpctpr.DmHinhThucQuangCaoREF	
							INNER JOIN ( SELECT --ID Hop Dong
									D.HopDongID ,
									D.SoHopDong ,
									D.DmMaHopDongREF ,
									D.TenMaHopDong , 
									D.NgayDanhSoHopDong ,
									D.NgayKyHopDong ,
									ISNULL(D.NhanHopDong, '') AS NhanHopDong ,
									D.NgayNhanBanFax ,
									D.NgayNhanHopDongBanCung ,
									D.NgayChuyenHopDongChoKeToan ,
									D.So ,
									D.Thang ,
									D.Nam , 
									D.GiaTriHopDong ,
									D.CongNo ,
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
									D.TenKhachHang
									FROM dbo.HopDong D
									WHERE D.TrangThaiHopDong NOT IN (0, 3)
									AND D.HopDongID = @HopDongID
							) hd ON hdct.HopDongFK = hd.HopDongID
				) T
				WHERE T.ThanhTienThucChayTruocChietKhau >0  
	
			UPDATE  dbo.ThucChayHopDongChiTietPR
			SET     RecordStatus = 1
			WHERE ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID
			AND HopDongREF= @HopDongID
			AND HopDongChiTietREF = @HopDongChiTietID
			AND EXISTS (
					
					SELECT DISTINCT DotChayBooking
					FROM    dbo.ThucChayDaTinh
					WHERE  HopDongID = @HopDongID
					AND HopDongChiTietREF = @HopDongChiTietID
					AND DmSanPhamREF IN ( 141, 245, 250, 637, 305 )
					AND NOT ( DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18 ) 
					AND NgayThucHien = @NgayThucHien
					AND DotChayBooking = CONVERT(NVARCHAR(100),ThucChayHopDongChiTietPRID)
					AND DotChayHopDong = @NoteThongTinThayDoiTang
					)

    END




--EXEC [ThucChay_InsertThucChayDaTinh_PR] '2013-07-01','2013-07-11'

```
