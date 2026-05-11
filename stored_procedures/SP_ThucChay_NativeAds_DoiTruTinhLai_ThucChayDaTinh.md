# Stored Procedure: `ThucChay_NativeAds_DoiTruTinhLai_ThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-03-07 17:17:24.347000
- **Ngày sửa cuối**: 2025-03-08 08:49:43.877000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Thucchay_NativeAds_DmTinhlai` | `DataType_Thucchay_NativeAds_DmTinhlai` | No |

## Definition (Source Code)

```sql

--CREATE TYPE DataType_Thucchay_NativeAds_DmTinhlai AS TABLE 
--	(		
--			DmSanPhamREF INT, 
--			TenSanPham NVARCHAR(100),
--			DmWebsiteREF INT, 
--			TenWebsite NVARCHAR(200),
--			DmBannerREF INT, 
--			DonViTinh NVARCHAR(100),
--			NgayThucHien DATE,
--			HopDongChiTietREF INT,
--			DmNhanHangREF NVARCHAR(200),
--			DonGiaSauCK FLOAT,
--			DonGiaKM FLOAT,

--			SLTC_GhiNhan FLOAT,
--			SLTC_KM_GhiNhan FLOAT,
--			TTTC_GhiNhan FLOAT,
--			TTTC_KM_GhiNhan FLOAT,
--			SoLuongLechTreoHa FLOAT,
--			ThanhTienLechTreoHa FLOAT,

--			LyDo NVARCHAR(200)
--			)


CREATE PROCEDURE [dbo].[ThucChay_NativeAds_DoiTruTinhLai_ThucChayDaTinh] 
    @Thucchay_NativeAds_DmTinhlai DataType_Thucchay_NativeAds_DmTinhlai READONLY
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
					NhanHang = tc.DmnhanHangREF,
					DmNhomNganhREF = hdct.DmNhomNganhREF, 
					TenNhomNganh = hdct.TenNhomNganh, 
					DmHinhThucQuangCao = hdct.DmLoaiREF , 
					TenHinhThucQuangCao = hdct.TenLoai , 
					DmSanPhamREF = tc.dmsanphamREF,
					TenSanPham = tc.TenSanPham ,  
					DmNhomWebsiteREF = hdct.DmNhomWebsiteREF, 
					TenNhomWebsite = hdct.TenNhomWebsite, 
					DmChuyenMucREF = hdct.DmChuyenMucREF, 
					TenChuyenMuc = hdct.TenChuyenMuc, 
					DmLoaiBannerREF = hdct.DmLoaiBannerREF, 
					TenLoaiBanner = hdct.TenLoaiBanner, 
					DmViTriREF = hdct.DmViTriREF, 
					TenViTri = hdct.TenViTri, 
					DotChayHopDong =  N'Tính lại NativeAds',--ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(tc.HopDongChiTietREF,'Y'),''),
					SoLuongDotChayHD = hdct.SoLuong ,
					DotChayBooking = '',--ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(tc.HopDongChiTietREF,'N'),0),
					SoLuongDotChayBooking = 0,--dbo.GetSoLuongDotChayBookingByHopDongChiTiet(tc.HopDongChiTietREF) ,
					SoLuong = hdct.SoLuong ,
					DonViTinh = tc.DonViTinh , 
					DonGia = hdct.DonGia ,
					DonGiaTheoDonViTinh = IIF(hdct.ChietKhau = 100, tc.DonGiaKM,tc.DonGiaSauCK),
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
					TongViewThucChay = 0 ,
					TongClickThucChay = 0 ,
					TongSoBaiViet = 0,
					SoLuongThucChay =  0  ,
					NgayThucHien = tc.NgayThucHien,
					GiaTriThayDoi = tc.TTTC_GhiNhan,
					ThanhTienThucChayTruocTrietKhau = 0 ,
					GiaTriTrietKhauThucChay = 0 ,
					ThanhTienSauTrietKhauThucChay = 0 ,
					GiaTriHoaHongThucChay = 0 ,
					ThanhTienThucThu = 0 ,
					ThanhTienKM =0 ,
					SoLuongThucChayKM =  0  ,
					SoLuongLechTreoHa = tc.SoLuongLechTreoHa ,
					ThanhTienLechTreoHa = tc.ThanhTienLechTreoHa  ,
					CreatedAt = GETDATE(),
					LastModifiedAt = GETDATE(),
					IsPheDuyet = 0 ,
					PheDuyetBy = '' ,
					PheDuyetAt = '',
					SoLuongThayDoi = tc.SLTC_GhiNhan  ,
					SoLuongKMThayDoi = tc.SLTC_KM_GhiNhan ,
					GiaTriKMThayDoi = tc.TTTC_KM_GhiNhan  ,
					GhiChu =  N'Tính lại: SP tối ưu [dbo].[ThucChay_NativeAds_DoiTruTinhLai_ThucChayDaTinh] do ' + tc.LyDo
			FROM @Thucchay_NativeAds_DmTinhlai tc
			INNER JOIN  ABM_Data_ThucChay.dbo.HopDongChiTiet hdct on hdct.HopDongChiTietID = tc.HopDongChiTietREF
			INNER JOIN  ABM_Data_ThucChay.dbo.HopDong hd on hd.HopDongID = hdct.HopDongFK 
    
END

```
