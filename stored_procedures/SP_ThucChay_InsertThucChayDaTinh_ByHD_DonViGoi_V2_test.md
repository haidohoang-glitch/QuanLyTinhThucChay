# Stored Procedure: `ThucChay_InsertThucChayDaTinh_ByHD_DonViGoi_V2_test`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2023-05-04 15:37:53.277000
- **Ngày sửa cuối**: 2023-05-04 15:38:02.560000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@ThucChayHopDongChiTietREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(400)` | No |
| `@DmBannerID` | `int(4)` | No |
| `@GhiChu` | `nvarchar(2000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucChayDaTinh_ByHD_Native_Ads]


CREATE  PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_ByHD_DonViGoi_V2_test] 
	@NgayThucHien DATETIME,
	@SoHopDong NVARCHAR(50),
	@HopDongID INT,
	@HopDongChiTietREF INT,
	@ThucChayHopDongChiTietREF INT,
	@DmSanPhamREF INT,
	@DmWebsiteREF INT,
	@TenWebsite NVARCHAR(200), 
	@DmBannerID INT,
	@GhiChu NVARCHAR(1000)
AS
BEGIN
	--PRINT 'Insert thuc chay ThanhTien_Admatic'
	DECLARE @DotChayHopDong NVARCHAR(100) = N'CPM_DonViGoi'

		--INSERT INTO dbo.ThucChayDaTinh
		--(
		--    ThucChayDaTinhID,
		--    HopDongID,
		--    SoHopDong,
		--    DmMaHopDongREF,
		--    TenMaHopDong,
		--    NgayDanhSoHopDong,
		--    NgayKyHopDong,
		--    NhanHopDong,
		--    NgayNhanBanFax,
		--    NgayNhanHopDongBanCung,
		--    NgayChuyenHopDongChoKeToan,
		--    So,
		--    Thang,
		--    Nam,
		--    GiaTriHopDong,
		--    CongNo,
		--    HopDongChiTietREF,
		--    DangSuDung,
		--    IsGiayPhep,
		--    TrangThaiHopDong,
		--    IsBanCung,
		--    DmPhongBanREF,
		--    TenPhongBan,
		--    DmBoPhanREF,
		--    TenBoPhan,
		--    DmNhomLamViecREF,
		--    TenNhomLamViec,
		--    DmDiaDiemLamViecREF,
		--    TenDiaDiemLamViec,
		--    SysNhanVienREF,
		--    TenDangNhap,
		--    TenNhanVien,
		--    TenKhachHang,
		--    NhanHang,
		--    DmNhomNganhREF,
		--    TenNhomNganh,
		--    DmHinhThucQuangCao,
		--    TenHinhThucQuangCao,
		--    DmSanPhamREF,
		--    TenSanPham,
		--    DmNhomWebsiteREF,
		--    TenNhomWebsite,
		--    DmChuyenMucREF,
		--    TenChuyenMuc,
		--    DmLoaiBannerREF,
		--    TenLoaiBanner,
		--    DmViTriREF,
		--    TenViTri,
		--    DotChayHopDong,
		--    SoLuongDotChayHD,
		--    DotChayBooking,
		--    SoLuongDotChayBooking,
		--    SoLuong,
		--    DonViTinh,
		--    DonGia,
		--    DonGiaTheoDonVi,
		--    ChietKhau,
		--    GiamGia,
		--    ThanhTien,
		--    TiLeTuVan,
		--    ChiPhiTuVan,
		--    IsKhuyenMai,
		--    KhuyenMai,
		--    DmBannerREF,
		--    DmChienDichREF,
		--    DmWebsiteREF,
		--    TenWebsite,
		--    TongViewThucChay,
		--    TongClickThucChay,
		--    TongSoBaiViet,
		--    SoLuongThucChay,
		--    NgayThucHien,
		--    GiaTriThayDoi,
		--    ThanhTienThucChayTruocTrietKhau,
		--    GiaTriTrietKhauThucChay,
		--    ThanhTienSauTrietKhauThucChay,
		--    GiaTriHoaHongThucChay,
		--    ThanhTienThucThu,
		--    ThanhTienKM,
		--    SoLuongThucChayKM,
		--    SoLuongThucChayLechTreoHa,
		--    ThanhTienLechTreoHa,
		--    CreatedAt,
		--    LastModifiedAt,
		--    IsPheDuyet,
		--    PheDuyetBy,
		--    PheDuyetAt,
		--    SoLuongThayDoi,
		--    SoLuongKMThayDoi,
		--    GiaTriKMThayDoi,
		--    GhiChu
		--)
		
	SELECT  NEWID() AS ThucChayDaTinhID,
		TD.HopDongID, TD.SoHopDong, TD.DmMaHopDongREF, TD.TenMaHopDong, TD.NgayDanhSoHopDong, TD.NgayKyHopDong, 
		TD.NhanHopDong, TD.NgayNhanBanFax, TD.NgayNhanHopDongBanCung, TD.NgayChuyenHopDongChoKeToan, TD.So, TD.Thang, TD.Nam, 
		TD.GiaTriHopDong, TD.CongNo, TD.HopDongChiTietREF, TD.DangSuDung, TD.IsGiayPhep, TD.TrangThaiHopDong,TD.IsBanCung, 
		TD.DmPhongBanREF, TD.TenPhongBan, TD.DmBoPhanREF, TD.TenBoPhan, TD.DmNhomLamViecREF, TD.TenNhom, TD.DmDiaDiemLamViecREF, TD.TenDiaDiemLamViec, 
		TD.SysNhanVienREF, TD.TenDangNhap, TD.TenNhanVien, TD.TenKhachHang, TD.NhanHang,
		TD.DmNhomNganhREF, TD.TenNhomNganh, TD.DmHinhThucQuangCao, TD.TenHinhThucQuangCao, 
		TD.DmSanPhamREF, TD.TenSanPham, TD.DmNhomWebsiteREF, 
		TD.TenNhomWebsite, TD.DmChuyenMucREF, TD.TenChuyenMuc, 
		TD.DmLoaiBannerREF, TD.TenLoaiBanner, TD.DmViTriREF, TD.TenViTri, 
		TD.DotChayHopDong, TD.SoLuongDotChayHD,
		TD.DotChayBooking, TD.SoLuongDotChayBooking, 
		TD.SoLuong, TD.DonViTinh, TD.DonGia, 
		TD.DonGiaTheoDonViTinh,--cho nay xem lai viec xac dinh don gia Native ads
		TD.ChietKhau, TD.GiamGia, TD.ThanhTien,
		TD.TiLeTuVan,  TD.ChiPhiTuVan,
		TD.IsKhuyenMai,  
		TD.KhuyenMai,
		TD.DmBannerREF,
		TD.DmChienDichREF,
		TD.DmWebsiteREF,
		TD.TenWebsite,
		TD.TongViewThucChay,
		TD.TongClickThucChay,
		TD.TongSoBaiViet,
		TD.SoLuongThucChay,
		TD.NgayThucHien,
		TD.GiaTriThayDoi,
		(CASE WHEN TD.ChietKhau = 100 THEN TD.ThanhTienKM
		ELSE (TD.ThanhTienSauTrietKhauThucChay*(100-TD.ChietKhau))/100
		END) AS ThanhTienThucChayTruocTrietKhau ,
		ISNULL(((TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) AS GiaTriTrietKhauThucChay,
		TD.ThanhTienSauTrietKhauThucChay,
		ISNULL(((TD.ThanhTienSauTrietKhauThucChay * TD.TiLeTuVan)/100),0) AS GiaTriHoaHongThucChay,
		ISNULL(((TD.ThanhTienSauTrietKhauThucChay - TD.ThanhTienSauTrietKhauThucChay * TD.TiLeTuVan)/100),0) AS ThanhTienThucThu,
		TD.ThanhTienKM,
		TD.SoLuongThucChayKM,
		(CASE WHEN TD.ChietKhau = 100 THEN (TD.SoLuongThucChayKM_tc - TD.SoLuongThucChayKM)
				ELSE (TD.SoLuongThucChay_tc - TD.SoLuongThucChay)
			END
		)AS SoLuongLechTreoHa,
		(CASE WHEN TD.ChietKhau = 100 THEN (TD.ThanhTienThucChayKM_tc- TD.ThanhTienKM)
				ELSE ((TD.ThanhTienThucChaySauCK_tc - TD.ThanhTienSauTrietKhauThucChay)/(100-TD.ChietKhau))*100
			END
		)AS ThanhTienLechTreoHa,
		GETDATE(),
		GETDATE(),
		0 IsPheDuyet,
		'' PheDuyetBy,
		'' PheDuyetAt,
		0 SoLuongThayDoi,
		0 SoLuongKMThayDoi,
		0 GiaTriKMThayDoi,
		@GhiChu AS GhiChu	
		FROM 
		(
			SELECT 
			hd.HopDongID,
			hd.SoHopDong, 
			hd.DmMaHopDongREF, 
			hd.TenMaHopDong, 
			hd.NgayDanhSoHopDong, hd.NgayKyHopDong, 
			hd.NhanHopDong, hd.NgayNhanBanFax, hd.NgayNhanHopDongBanCung, hd.NgayChuyenHopDongChoKeToan, 
			hd.So, hd.Thang, hd.Nam, 
			hd.GiaTriHopDong, hd.CongNo,
			hd.HopDongChiTietID HopDongChiTietREF,
			hd.DangSuDung, hd.IsGiayPhep, hd.TrangThaiHopDong,hd.IsBanCung, 
			hd.DmPhongBanREF, 
			ISNULL(hd.TenPhongBan, '') AS TenPhongBan, 
			hd.DmBoPhanREF, 
			ISNULL(hd.TenBoPhan,'') AS TenBoPhan, 
			hd.DmNhomLamViecREF, 
			ISNULL(hd.TenNhom, '') AS TenNhom, 
			hd.DmDiaDiemLamViecREF, 
			hd.TenDiaDiemLamViec, 
			hd.SysNhanVienREF, 
			ISNULL(hd.TenDangNhap, '') AS TenDangNhap,  
			hd.TenNhanVien, 
			hd.TenKhachHang, 
			hd.DanhSachNhanHangREF AS NhanHang,
			hd.DmNhomNganhREF AS DmNhomNganhREF, 
			hd.TenNhomNganh AS TenNhomNganh, 
			--Thong tin hinh thuc quang cao
			hd.DmLoaiREF AS DmHinhThucQuangCao, hd.TenLoai AS TenHinhThucQuangCao, 
			--Thong tin San pham
			tc.DmSanPhamREF as DmSanPhamREF,
			(SELECT TOP (1) sp.TenSanPham FROM DmSanPham sp WHERE sp.DmSanPhamID = tc.DmSanPhamREF ORDER BY sp.DmSanPhamID) AS TenSanPham,  
			hd.DmNhomWebsiteREF, 
			hd.TenNhomWebsite, 
			hd.DmChuyenMucREF, 
			hd.TenChuyenMuc, 
			hd.DmLoaiBannerREF, 
			hd.TenLoaiBanner, 
			hd.DmBannerREF AS DmViTriREF, 
			hd.TenViTri, 
			@DotChayHopDong DotChayHopDong,
			hd.SoLuong AS SoLuongDotChayHD,
			ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(hd.HopDongChiTietID,'N'),0) DotChayBooking,
			dbo.GetSoLuongDotChayBookingByHopDongChiTiet(hd.HopDongChiTietID) SoLuongDotChayBooking, 
			hd.SoLuong AS SoLuong,
			tc.DonViTinh as DonViTinh, 
			hd.DonGia as DonGia, 
			--****haidh chinh sua 
			tc.DonGia AS DonGiaTheoDonViTinh,--cho nay xem lai viec xac dinh don gia Native ads
			hd.ChietKhau, hd.GiamGia, hd.ThanhTien,
			hd.TiLeTuVan,  hd.ChiPhiTuVan,
			hd.IsKhuyenMai,  
			hd.KhuyenMai,
			tc.DmBannerID DmBannerREF,
			0 DmChienDichREF,
			tc.DmWebsiteID AS DmWebsiteREF,
			tc.TenWebsite AS TenWebsite,
			(CASE WHEN tc.DonViTinh = N'VIEW' THEN tc.SoLuongThucChay
			ELSE 0
			END) AS   TongViewThucChay,
			(CASE WHEN tc.DonViTinh = N'CLICK' THEN tc.SoLuongThucChay
			ELSE 0
			END) AS   TongClickThucChay,
			(CASE WHEN tc.DonViTinh <> N'CLICK' AND TC.DonViTinh <> N'VIEW' THEN tc.SoLuongThucChay
			ELSE 0
			END) AS  TongSoBaiViet,
			--VIET FUNCTION CHECK VUOT GIA TRI VA SO LUONG
			(CASE WHEN HD.ChietKhau <> 100 THEN ([dbo].[ThucChay_GetSoLuongThucChay_ThanhTien_Admatic] (tc.SoLuongThucChay, tc.ThanhTienThucChaySauCK_ChuaVAT, tc.SoLuongThucChayKM, tc.ThanhTienThucChayKM,
														@NgayThucHien, hd.HopDongChiTietID, hd.SoLuong, hd.DonGia, hd.ThanhTien, hd.ChietKhau))
			ELSE 0
			END) AS SoLuongThucChay,
			tc.NgayThucHien,
			0 as GiaTriThayDoi,
			--VIET FUNCTION CHECK VUOT GIA TRI VA SO LUONG
			0 AS ThanhTienThucChayTruocTrietKhau,
			0 AS GiaTriTrietKhauThucChay,
			(CASE WHEN HD.ChietKhau <> 100 THEN ([dbo].[ThucChay_ThanhTienThucChay_DonViGoi] (tc.ThanhTienThucChaySauCK_ChuaVAT, tc.ThanhTienThucChayKM, @NgayThucHien,
													tc.HopDongChiTietREF, hd.SoLuong, hd.DonGia, hd.ThanhTien, hd.ChietKhau))
			ELSE 0
			END)  AS ThanhTienSauTrietKhauThucChay ,
			0 GiaTriHoaHongThucChay,
			(CASE WHEN HD.ChietKhau = 100 THEN ([dbo].[ThucChay_ThanhTienThucChay_DonViGoi] (tc.ThanhTienThucChaySauCK_ChuaVAT, tc.ThanhTienThucChayKM, @NgayThucHien,
													tc.HopDongChiTietREF, hd.SoLuong, hd.DonGia, hd.ThanhTien, hd.ChietKhau))
			ELSE 0
			END) AS  ThanhTienKM,
			(CASE WHEN HD.ChietKhau = 100 THEN ([dbo].[ThucChay_GetSoLuongThucChay_DonViGoi] (tc.SoLuongThucChay, tc.ThanhTienThucChaySauCK_ChuaVAT, tc.SoLuongThucChayKM, tc.ThanhTienThucChayKM,
														@NgayThucHien, hd.HopDongChiTietID, hd.SoLuong, hd.DonGia, hd.ThanhTien, hd.ChietKhau))
			ELSE 0
			END) AS SoLuongThucChayKM,
			tc.SoLuongThucChay AS SoLuongThucChay_tc,
			tc.SoLuongThucChayKM AS SoLuongThucChayKM_tc,
			tc.ThanhTienThucChaySauCK_ChuaVAT AS ThanhTienThucChaySauCK_tc,
			tc.ThanhTienThucChayKM AS ThanhTienThucChayKM_tc
		FROM
		(
			SELECT tct.*
			FROM dbo.[ThucChay_DonViGoi_temp] tct
			WHERE tct.HopDongREF = @HopDongID
			AND tct.HopDongChitietREF = @HopDongChiTietREF
			AND tct.DmSanPhamREF = @DmSanPhamREF
			AND tct.DmBannerID = @DmBannerID
			AND tct.DmWebsiteID = @DmWebsiteREF
			AND tct.NgayThucHien = @NgayThucHien
		)tc
		INNER JOIN
		(SELECT hd.HopDongID,
			hd.SoHopDong, 
			hd.DmMaHopDongREF, 
			hd.TenMaHopDong, 
			hd.NgayDanhSoHopDong, hd.NgayKyHopDong, 
			hd.NhanHopDong, hd.NgayNhanBanFax, hd.NgayNhanHopDongBanCung, hd.NgayChuyenHopDongChoKeToan, 
			hd.So, hd.Thang, hd.Nam, 
			hd.GiaTriHopDong, hd.CongNo,
			hd.DangSuDung, hd.IsGiayPhep, hd.TrangThaiHopDong,hd.IsBanCung, 
			hd.DmPhongBanREF, 
			ISNULL(hd.TenPhongBan, '') AS TenPhongBan, 
			hd.DmBoPhanREF, 
			ISNULL(hd.TenBoPhan,'') AS TenBoPhan, 
			hd.DmNhomLamViecREF, 
			ISNULL(hd.TenNhom, '') AS TenNhom, 
			hd.DmDiaDiemLamViecREF, 
			hd.TenDiaDiemLamViec, 
			hd.SysNhanVienREF, 
			ISNULL(hd.TenDangNhap, '') AS TenDangNhap,  
			hd.TenNhanVien, 
			hd.TenKhachHang, hdct.* FROM 
			(SELECT hd.* FROM dbo.HopDong hd WHERE hd.HopDongID = @HopDongID AND hd.TrangThaiHopDong NOT IN (0,3)) hd
			INNER JOIN 
			(SELECT * FROM dbo.HopDongChiTiet hdct 
				WHERE 1=1
				AND hdct.HopDongFK = @HopDongID
				AND hdct.HopDongChiTietID = @HopDongChiTietREF
				AND hdct.DonViTinhREF = 10 --Don Vi Goi
				AND hdct.DmSanPhamREF IN (339, 240, 598, 342, 5056, 733)-- haidh comment them san pham 733 nhieu san pham cho DonViGoi
				AND NOT (hdct.DmLoaiBannerREF = 18 OR hdct.DmLoaiREF IN (42,13))
				AND hdct.DeletedStatus = 0
			)hdct ON hd.HopDongID = hdct.HopDongFK
		)hd ON hd.HopDongID = tc.HopDongREF AND tc.HopDongChiTietREF = hd.HopDongChiTietID
	)TD
END


```
