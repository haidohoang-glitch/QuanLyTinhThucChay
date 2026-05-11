# Stored Procedure: `ThucChay_CPMDonViGoi_Insert_ThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-03-07 17:19:42.147000
- **Ngày sửa cuối**: 2025-03-08 08:51:57.220000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Thucchay_CPMDonViGoi_DmTinhMoi` | `DataType_Thucchay_CPMDonViGoi_DmTinhMoi` | No |

## Definition (Source Code)

```sql
--CREATE TYPE DataType_Thucchay_CPMDonViGoi_DmTinhMoi AS TABLE 
--	(		DmWebsiteREF INT,
--			TenWebsite NVARCHAR(100),
--			DmBannerREF INT,
--			NgayThucHien DATE,
--			HopDongChiTietREF INT,
--			DonViTinh NVARCHAR(50),
--			DonGiaSauCK FLOAT,
--			DonGiaKM FLOAT,
--			DmSanPhamREF INT,
--			DmNhanHangREF NVARCHAR(200),
--			GhiChu NVARCHAR(200),
--			SoLuongThucChay_GhiNhan INT,
--			SoLuongKM_GhiNhan INT,
--			ThanhTienTC_GhiNhan FLOAT,
--			ThanhTienKM_GhiNhan FLOAT,
--			SoLuongLechTreoHa INT,
--			ThanhTienLechTreoHa FLOAT
--			)

CREATE PROCEDURE [dbo].[ThucChay_CPMDonViGoi_Insert_ThucChayDaTinh] 
	@Thucchay_CPMDonViGoi_DmTinhMoi DataType_Thucchay_CPMDonViGoi_DmTinhMoi READONLY
AS
BEGIN

    INSERT INTO ABM_Data_ThucChay.dbo.thucchaydatinh
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
	SELECT NEWID(), HopDongID = hd.HopDongID,
					SoHopDong = hd.SoHopDong, 
					DmMaHopDongREF = hd.DmMaHopDongREF, 
					TenMaHopDong = hd.TenMaHopDong, 
					NgayDanhSoHopDong = hd.NgayDanhSoHopDong, 
					NgayKyHopDong = hd.NgayKyHopDong, 
					NhanHopDong = hd.NhanHopDong, 
					NgayNhanBanFax = hd.NgayNhanBanFax, 
					NgayNhanHopDongBanCung = hd.NgayNhanHopDongBanCung, 
					NgayChuyenHopDongChoKeToan = hd.NgayChuyenHopDongChoKeToan, 
					So = hd.So, 
					Thang = hd.Thang, Nam = hd.Nam, 
					GiaTriHopDong = hd.GiaTriHopDong, CongNo = hd.CongNo,
					HopDongChiTietREF = tc.HopDongChiTietREF,
					DangSuDung = hd.DangSuDung, IsGiayPhep = hd.IsGiayPhep, TrangThaiHopDong = hd.TrangThaiHopDong, IsBanCung = hd.IsBanCung, 
					DmPhongBanREF = hd.DmPhongBanREF, 
					TenPhongBan = ISNULL(hd.TenPhongBan, '') , 
					DmBoPhanREF = hd.DmBoPhanREF, 
					TenBoPhan = ISNULL(hd.TenBoPhan,'') , 
					DmNhomLamViecREF = hd.DmNhomLamViecREF, 
					TenNhom = ISNULL(hd.TenNhom, '') , 
					DmDiaDiemLamViecREF = hd.DmDiaDiemLamViecREF, 
					TenDiaDiemLamViec = hd.TenDiaDiemLamViec, 
					SysNhanVienREF = hd.SysNhanVienREF, 
					TenDangNhap = ISNULL(hd.TenDangNhap, '') ,  
					TenNhanVien = hd.TenNhanVien, 
					TenKhachHang = hd.TenKhachHang, 
					NhanHang = tc.DmNhanHangREF,
					DmNhomNganhREF = hdct.DmNhomNganhREF, 
					TenNhomNganh = hdct.TenNhomNganh, 
					DmHinhThucQuangCao = hdct.DmLoaiREF , 
					TenHinhThucQuangCao = hdct.TenLoai , 
					DmSanPhamREF = tc.DmSanPhamREF,
					TenSanPham = sp.TenSanPham ,  
					DmNhomWebsiteREF = hdct.DmNhomWebsiteREF, 
					TenNhomWebsite = hdct.TenNhomWebsite, 
					DmChuyenMucREF = hdct.DmChuyenMucREF, 
					TenChuyenMuc = hdct.TenChuyenMuc, 
					DmLoaiBannerREF = hdct.DmLoaiBannerREF, 
					TenLoaiBanner = hdct.TenLoaiBanner, 
					DmViTriREF = hdct.DmViTriREF, 
					TenViTri = hdct.TenViTri, 
					DotChayHopDong = N'Tính mới CPM DonViGoi',--ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(tc.HopDongChiTietREF,'Y'),''),
					SoLuongDotChayHD = hdct.SoLuong ,
					DotChayBooking = '',--ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(tc.HopDongChiTietREF,'N'),0),
					SoLuongDotChayBooking = 0,--dbo.GetSoLuongDotChayBookingByHopDongChiTiet(tc.HopDongChiTietREF) ,
					SoLuong = hdct.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh) ,
					DonViTinh = tc.DonViTinh , 
					DonGia = hdct.DonGia ,
					DonGiaTheoDonViTinh = IIF(hdct.ChietKhau = 100, tc.DonGiaKM, tc.DonGiaSauCK),
					ChietKhau = hdct.ChietKhau, 
					GiamGia = hdct.GiamGia, 
					ThanhTien = hdct.ThanhTien,
					TiLeTuVan = hdct.TiLeTuVan,  
					ChiPhiTuVan = hdct.ChiPhiTuVan,
					IsKhuyenMai = hdct.IsKhuyenMai,  
					KhuyenMai = hdct.KhuyenMai,
					DmBannerREF = tc.DmBannerREF ,
					DmChienDichREF = 0 ,
					DmWebsiteREF = tc.DmWebsiteREF,
					TenWebsite = tc.TenWebsite,
					TongViewThucChay = IIF(tc.donvitinh IN (N'VIEW', N'TRUE VIEW'), IIF(hdct.ChietKhau = 100, tc.SoLuongKM_GhiNhan, tc.SoLuongThucChay_GhiNhan),0) ,
					TongClickThucChay = IIF(tc.donvitinh = N'CLICK', IIF(hdct.ChietKhau = 100, tc.SoLuongKM_GhiNhan, tc.SoLuongThucChay_GhiNhan),0) ,
					TongSoBaiViet = 0,
					SoLuongThucChay =  tc.SoLuongThucChay_GhiNhan  ,
					NgayThucHien = tc.NgayThucHien,
					GiaTriThayDoi = 0 ,
					ThanhTienThucChayTruocTrietKhau = ISNULL(IIF(hdct.ChietKhau <> 100, tc.ThanhTienTC_GhiNhan/(1-hdct.ChietKhau/100), tc.ThanhTienKM_GhiNhan), 0) ,
					GiaTriTrietKhauThucChay = ISNULL(IIF(hdct.ChietKhau <> 100, (tc.ThanhTienTC_GhiNhan/(1-hdct.ChietKhau/100)) * hdct.ChietKhau/100, 0) , 0),
					ThanhTienSauTrietKhauThucChay = ISNULL(tc.ThanhTienTC_GhiNhan,0) ,
					GiaTriHoaHongThucChay = ISNULL(tc.ThanhTienTC_GhiNhan * hdct.TiLeTuVan/100, 0) ,
					ThanhTienThucThu = ISNULL(tc.ThanhTienTC_GhiNhan * (1-hdct.TiLeTuVan/100), 0) ,
					ThanhTienKM = ISNULL(IIF( hdct.IsKhuyenMai=1, tc.ThanhTienKM_GhiNhan, 0), 0) ,
					SoLuongThucChayKM =  ISNULL(IIF( hdct.IsKhuyenMai=1, tc.SoLuongKM_GhiNhan, 0), 0)  ,
					SoLuongLechTreoHa = ISNULL(tc.SoLuongLechTreoHa, 0),
					ThanhTienLechTreoHa = ISNULL(tc.ThanhTienLechTreoHa , 0) ,
					CreatedAt = GETDATE(),
					LastModifiedAt = GETDATE(),
					IsPheDuyet = 0 ,
					PheDuyetBy = '' ,
					PheDuyetAt = '',
					SoLuongThayDoi = 0 ,
					SoLuongKMThayDoi = 0 ,
					GiaTriKMThayDoi = 0 ,
					GhiChu =  tc.GhiChu
			FROM @Thucchay_CPMDonViGoi_DmTinhMoi tc
			INNER JOIN  ABM_Data_ThucChay.dbo.HopDongChiTiet hdct on hdct.HopDongChiTietID = tc.HopDongChiTietREF
			INNER JOIN  ABM_Data_ThucChay.dbo.HopDong hd on hd.HopDongID = hdct.HopDongFK 
			OUTER APPLY (SELECT TOP (1) sp.TenSanPham 
						 FROM ABM_Data_ThucChay.dbo.DmSanPham sp 
						 WHERE sp.DmSanPhamID = tc.DmSanPhamREF 
						 ORDER BY sp.DmSanPhamID) sp
			
		    
END

```
