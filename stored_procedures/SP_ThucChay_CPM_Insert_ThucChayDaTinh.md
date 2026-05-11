# Stored Procedure: `ThucChay_CPM_Insert_ThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-11-22 16:20:03.183000
- **Ngày sửa cuối**: 2025-03-08 08:44:42.680000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Thucchay_CPMthuan_DmTinhMoi` | `DataType_Thucchay_CPMthuan_DmTinhMoi` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[ThucChay_CPM_Insert_ThucChayDaTinh] 
	@Thucchay_CPMthuan_DmTinhMoi DataType_Thucchay_CPMthuan_DmTinhMoi READONLY
AS
BEGIN

    INSERT INTO ABM_Data_ThucChay.dbo.ThucChayDaTinh
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
					DmSanPhamREF = dbo.GetProductIDByTypeProduct(tc.TypeProduct),
					TenSanPham = dbo.GetProductNameByTypeProduct(tc.TypeProduct) ,  
					DmNhomWebsiteREF = hdct.DmNhomWebsiteREF, 
					TenNhomWebsite = hdct.TenNhomWebsite, 
					DmChuyenMucREF = hdct.DmChuyenMucREF, 
					TenChuyenMuc = hdct.TenChuyenMuc, 
					DmLoaiBannerREF = hdct.DmLoaiBannerREF, 
					TenLoaiBanner = hdct.TenLoaiBanner, 
					DmViTriREF = hdct.DmViTriREF, 
					TenViTri = hdct.TenViTri, 
					DotChayHopDong = N'Tính mới CPM thuần',--ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(tc.HopDongChiTietREF,'Y'),''),
					SoLuongDotChayHD = hdct.SoLuong ,
					DotChayBooking = '',--ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(tc.HopDongChiTietREF,'N'),0),
					SoLuongDotChayBooking = 0,--dbo.GetSoLuongDotChayBookingByHopDongChiTiet(tc.HopDongChiTietREF) ,
					SoLuong = hdct.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh) ,
					DonViTinh = dbo.ThucChay_GetDonViTinhNotCPD_v2(hdct.DonViTinh, NULL) , 
					DonGia = hdct.DonGia ,
					DonGiaTheoDonViTinh = hdct.DonGia/dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh),
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
					TongViewThucChay = ISNULL(tc.TongViewThucChay,0) ,
					TongClickThucChay = ISNULL(tc.TongClickThucChay,0) ,
					TongSoBaiViet = ISNULL(tc.TongSoBaiViet, 0),
					SoLuongThucChay =  (CASE	WHEN ISNULL(hdct.IsKhuyenMai, 0) <> 1
												THEN ISNULL(tc.SoLuongGhiNhan, 0)
												ELSE 0
										END )  ,
					NgayThucHien = tc.NgayThucHien,
					GiaTriThayDoi = 0 ,
					ThanhTienThucChayTruocTrietKhau = ISNULL((hdct.DonGia / dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh))*tc.SoLuongGhiNhan, 0) ,
					GiaTriTrietKhauThucChay = ISNULL((hdct.DonGia / dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh))*tc.SoLuongGhiNhan * hdct.ChietKhau/100,0) ,
					ThanhTienSauTrietKhauThucChay = ISNULL((hdct.DonGia / dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh))*tc.SoLuongGhiNhan * (100 - hdct.ChietKhau)/100,0) ,
					GiaTriHoaHongThucChay = ISNULL(((hdct.DonGia / dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh))*tc.SoLuongGhiNhan * (100 - hdct.ChietKhau)/100) * hdct.TiLeTuVan/100,0) ,
					ThanhTienThucThu = ISNULL(((hdct.DonGia / dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh))*tc.SoLuongGhiNhan * (100 - hdct.ChietKhau)/100) * (100 - hdct.TiLeTuVan) / 100, 0) ,
					ThanhTienKM = IIF( hdct.IsKhuyenMai=1, ISNULL((hdct.DonGia / dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh))*tc.SoLuongGhiNhan, 0), 0) ,
					SoLuongThucChayKM =  CASE WHEN hdct.IsKhuyenMai=1 OR hdct.ChietKhau = 100 
												  THEN tc.SoLuongGhiNhan
												  ELSE 0
										 END  ,
					SoLuongLechTreoHa = ISNULL(tc.SoLuongLechTreoHa, 0),
					ThanhTienLechTreoHa = ISNULL(tc.SoLuongLechTreoHa * (hdct.DonGia / dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)), 0) ,
					CreatedAt = GETDATE(),
					LastModifiedAt = GETDATE(),
					IsPheDuyet = 0 ,
					PheDuyetBy = '' ,
					PheDuyetAt = '',
					SoLuongThayDoi = 0 ,
					SoLuongKMThayDoi = 0 ,
					GiaTriKMThayDoi = 0 ,
					GhiChu =  tc.GhiChu
			FROM @Thucchay_CPMthuan_DmTinhMoi tc
			INNER JOIN  ABM_Data_ThucChay.dbo.HopDongChiTiet hdct on hdct.HopDongChiTietID = tc.HopDongChiTietREF
			INNER JOIN  ABM_Data_ThucChay.dbo.HopDong hd on hd.HopDongID = hdct.HopDongFK 
			
		    
END

```
