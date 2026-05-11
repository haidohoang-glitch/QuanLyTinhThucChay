# Stored Procedure: `ThucChay_Mobile_Insert_ThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-03-14 16:59:49.030000
- **Ngày sửa cuối**: 2025-03-21 11:56:35.420000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@thucchay_Mobile_SoLuongGhiNhantheoID` | `DataType_Thucchay_Mobile_DmTinhMoi2` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChay_Mobile_Insert_ThucChayDaTinh] 
	@thucchay_Mobile_SoLuongGhiNhantheoID DataType_Thucchay_Mobile_DmTinhMoi2 READONLY
AS
BEGIN

    INSERT INTO ABM_data_ThucChay.dbo.ThucChayDaTinh
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
					DmSanPhamREF = dbo.GetProductIDByTypeProduct(10),
					TenSanPham = dbo.GetProductNameByTypeProduct(10) ,  
					DmNhomWebsiteREF = hdct.DmNhomWebsiteREF, 
					TenNhomWebsite = hdct.TenNhomWebsite, 
					DmChuyenMucREF = hdct.DmChuyenMucREF, 
					TenChuyenMuc = hdct.TenChuyenMuc, 
					DmLoaiBannerREF = hdct.DmLoaiBannerREF, 
					TenLoaiBanner = hdct.TenLoaiBanner, 
					DmViTriREF = hdct.DmViTriREF, 
					TenViTri = hdct.TenViTri, 
					DotChayHopDong = N'Tính mới Mobile',--ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(tc.HopDongChiTietREF,'Y'),''),
					SoLuongDotChayHD = hdct.SoLuong ,
					DotChayBooking = '',--ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(tc.HopDongChiTietREF,'N'),0),
					SoLuongDotChayBooking = 0,--dbo.GetSoLuongDotChayBookingByHopDongChiTiet(tc.HopDongChiTietREF) ,
					SoLuong = hdct.SoLuong*IIF(hdct.DonViTinh = 'CPM', 1000, 1) ,
					DonViTinh = dbo.ThucChay_Mobile_GetDonViTinh(hdct.DonViTinh, ISNULL(tc.DonViTinhTreo, '')) , 
					DonGia = hdct.DonGia ,
					DonGiaTheoDonViTinh = tc.DonGia,
					ChietKhau = hdct.ChietKhau, 
					GiamGia = hdct.GiamGia, 
					ThanhTien = hdct.ThanhTien,
					TiLeTuVan = hdct.TiLeTuVan,  
					ChiPhiTuVan = hdct.ChiPhiTuVan,
					IsKhuyenMai = hdct.IsKhuyenMai,  
					KhuyenMai = hdct.KhuyenMai,
					DmBannerREF = tc.DmBannerREF ,
					DmChienDichREF = 0 ,
					DmWebsiteREF = ISNULL(w.DmWebsiteReportingdbID, 0),
					TenWebsite = tc.TenWebsite,
					TongViewThucChay = ISNULL(tc.TongViewThucChay,0) ,
					TongClickThucChay = ISNULL(tc.TongClickThucChay,0) ,
					TongSoBaiViet = 0,
					SoLuongThucChay =  tc.SoLuongThucChay_GhiNhan, 
					NgayThucHien = tc.NgayThucHien,
					GiaTriThayDoi = 0 ,
					ThanhTienThucChayTruocTrietKhau = IIF(hdct.ChietKhau = 100, tc.ThanhTienKM_GhiNhan,  tc.ThanhTienThucChay_GhiNhan/(1-hdct.ChietKhau/100)) ,
					GiaTriTrietKhauThucChay = IIF(hdct.ChietKhau = 100,  tc.ThanhTienKM_GhiNhan,  tc.ThanhTienThucChay_GhiNhan*hdct.ChietKhau/(1-hdct.ChietKhau/100)) ,
					ThanhTienSauTrietKhauThucChay = tc.ThanhTienThucChay_GhiNhan ,
					GiaTriHoaHongThucChay = tc.ThanhTienThucChay_GhiNhan * hdct.TiLeTuVan/100 ,
					ThanhTienThucThu = tc.ThanhTienThucChay_GhiNhan * (1- hdct.TiLeTuVan/100)  ,
					ThanhTienKM =  tc.ThanhTienKM_GhiNhan,
					SoLuongThucChayKM =  tc.SoLuongKM_GhiNhan   ,
					SoLuongLechTreoHa = tc.SoLuongLechTreoHa,
					ThanhTienLechTreoHa = tc.ThanhTienLechTreoHa,
					CreatedAt = GETDATE(),
					LastModifiedAt = GETDATE(),
					IsPheDuyet = 0 ,
					PheDuyetBy = '' ,
					PheDuyetAt = '',
					SoLuongThayDoi = 0 ,
					SoLuongKMThayDoi = 0 ,
					GiaTriKMThayDoi = 0 ,
					GhiChu =  tc.GhiChu
			FROM @thucchay_Mobile_SoLuongGhiNhantheoID tc
			INNER JOIN  ABM_Data_ThucChay.dbo.HopDongChiTiet hdct on hdct.HopDongChiTietID = tc.HopDongChiTietREF
			INNER JOIN  ABM_Data_ThucChay.dbo.HopDong hd on hd.HopDongID = hdct.HopDongFK 
			OUTER APPLY (SELECT TOP 1 DmWebsiteReportingdbID
						 FROM ABM_Data_ThucChay.dbo.DmWebsiteReportingdb  w 
						 WHERE w.TenWebsite = tc.TenWebsite  ) w

			
		    
END

```
