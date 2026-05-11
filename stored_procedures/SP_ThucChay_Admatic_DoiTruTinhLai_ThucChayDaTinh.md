# Stored Procedure: `ThucChay_Admatic_DoiTruTinhLai_ThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-03-10 17:06:36.250000
- **Ngày sửa cuối**: 2025-10-08 14:54:25.340000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Thucchay_Admatic_DmTinhlai` | `DataType_Thucchay_Admatic_DmTinhlai` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChay_Admatic_DoiTruTinhLai_ThucChayDaTinh] 
    @Thucchay_Admatic_DmTinhlai DataType_Thucchay_Admatic_DmTinhlai READONLY
AS
BEGIN
	DECLARE @GhiChu NVARCHAR(2000) =  N'Tính lại: SP tối ưu + MKT-FEE [dbo].[ThucChay_Admatic_DoiTruTinhLai_ThucChayDaTinh] do '

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
					NhanHang = hdct.DanhSachNhanHangREF,
					DmNhomNganhREF = hdct.DmNhomNganhREF, 
					TenNhomNganh = hdct.TenNhomNganh, 
					DmHinhThucQuangCao = hdct.DmLoaiREF , 
					TenHinhThucQuangCao = hdct.TenLoai , 
					DmSanPhamREF = tc.dmsanphamREF,
					TenSanPham = sp.TenSanPham ,  
					DmNhomWebsiteREF = hdct.DmNhomWebsiteREF, 
					TenNhomWebsite = hdct.TenNhomWebsite, 
					DmChuyenMucREF = hdct.DmChuyenMucREF, 
					TenChuyenMuc = hdct.TenChuyenMuc, 
					DmLoaiBannerREF = hdct.DmLoaiBannerREF, 
					TenLoaiBanner = hdct.TenLoaiBanner, 
					DmViTriREF = hdct.DmViTriREF, 
					TenViTri = hdct.TenViTri, 
					DotChayHopDong =  N'Tính lại Admatic',--ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(tc.HopDongChiTietREF,'Y'),''),
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
					TongViewThucChay = 0 ,
					TongClickThucChay = 0 ,
					TongSoBaiViet = 0,
					SoLuongThucChay =  0  ,
					NgayThucHien = tc.NgayThucHien,
					GiaTriThayDoi = tc.ThanhTienTC_GhiNhan ,
					ThanhTienThucChayTruocTrietKhau = 0 ,
					GiaTriTrietKhauThucChay = 0 ,
					ThanhTienSauTrietKhauThucChay = 0 ,
					GiaTriHoaHongThucChay = 0 ,
					ThanhTienThucThu = 0 ,
					ThanhTienKM =0 ,
					SoLuongThucChayKM =  0  ,
					SoLuongLechTreoHa = tc.SoLuongLechTreoHa,
					ThanhTienLechTreoHa = tc.ThanhTienLechTreoHa,
					CreatedAt = GETDATE(),
					LastModifiedAt = GETDATE(),
					IsPheDuyet = 0 ,
					PheDuyetBy = '' ,
					PheDuyetAt = '',
					SoLuongThayDoi = tc.SoLuongThucChay_GhiNhan ,
					SoLuongKMThayDoi = tc.SoLuongKM_GhiNhan ,
					GiaTriKMThayDoi = tc.ThanhTienKM_GhiNhan  ,
					GhiChu =  @GhiChu + tc.LyDo
			FROM @Thucchay_Admatic_DmTinhlai tc
			INNER JOIN  dbo.HopDongChiTiet hdct on hdct.HopDongChiTietID = tc.HopDongChiTietREF
			INNER JOIN  dbo.HopDong hd on hd.HopDongID = hdct.HopDongFK 
			OUTER APPLY (SELECT TOP (1) sp.TenSanPham 
						 FROM dbo.DmSanPham sp 
						 WHERE sp.DmSanPhamID = tc.DmSanPhamREF 
						 ORDER BY sp.DmSanPhamID) sp
    
END

```
