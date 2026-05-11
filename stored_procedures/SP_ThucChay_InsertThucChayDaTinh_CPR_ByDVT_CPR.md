# Stored Procedure: `ThucChay_InsertThucChayDaTinh_CPR_ByDVT_CPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-11-25 15:40:29.030000
- **Ngày sửa cuối**: 2018-02-01 16:06:52.337000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [dbo].[ThucChay_InsertThucChayDaTinh_CPR_ByDVT_CPR]


CREATE  PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_CPR_ByDVT_CPR] 
	@NgayThucHien DATETIME,
	@HopDongID int,
	@TypeProduct INT,
	@DmWebsiteREF INT, 
	@TenWebsite NVARCHAR(50)
AS
BEGIN

INSERT INTO dbo.ThucChayDaTinh 
	SELECT  NEWID(), TD.*, 
	ISNULL(((TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) AS GiaTriTrietKhauThucChay,
	ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) AS ThanhTienSauTrietKhauThucChay,
	ISNULL((((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS GiaTriHoaHongThucChay,
	ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100 - ((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS ThanhTienThucThu,
	(CASE when TD.IsKhuyenMai=1 then TD.ThanhTienThucChayTruocTrietKhau
		else 0
	  END
	) as ThanhTienKM,
	(CASE when (((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100))AND (TD.DonViTinh = 'CPR')) then ISNULL([dbo].[ThucChay_GetSoLuongThucChayChuanByDonViTinh_CPR](TD.SoLuongDotChayBooking,TD.TongViewThucChay,TD.SoLuong,TD.DonViTinh, TD.NgayThucHien, TD.HopDongChiTietREF),0)
		else 0
	  END
	) as SoLuongThucChayKM,
	(CASE when (TD.DonViTinh = 'CPR') then [dbo].[ThucChay_GetSoLuongLechTreoHa_CPR](@NgayThucHien, TD.HopDongChiTietREF, TD.SoLuong, TD.DonViTinh, TD.DmSanPhamREF, TD.TongViewThucChay)
		else 0
	  END
	)AS SoLuongLechTreoHa,
	(CASE when (TD.DonViTinh = 'CPR') then [dbo].[ThucChay_GetSoLuongLechTreoHa_CPR](@NgayThucHien, TD.HopDongChiTietREF, TD.SoLuong, TD.DonViTinh, TD.DmSanPhamREF, TD.TongViewThucChay)*TD.DonGiaTheoDonViTinh
		else 0
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
	'' GhiChu	
	FROM 
	(
	SELECT 

	--ID Hop Dong
	D.HopDongID,
	--Thong tin ve ma so 
	D.SoHopDong, 
	D.DmMaHopDongREF, 
	D.TenMaHopDong, 
	--Thong tin ve thoi gian
	D.NgayDanhSoHopDong, D.NgayKyHopDong, 
	D.NhanHopDong, D.NgayNhanBanFax, D.NgayNhanHopDongBanCung, D.NgayChuyenHopDongChoKeToan, 
	D.So, D.Thang, D.Nam, 
	--Thong tin ve gia tri
	D.GiaTriHopDong, D.CongNo,
	--Thong tin chi tiet phan bo
	A.HopDongChiTietREF,
	--Thong tin ve trang thai
	D.DangSuDung, D.IsGiayPhep, D.TrangThaiHopDong,D.IsBanCung, 
	--Thong tin ve Nhan vien kinh doanh
	D.DmPhongBanREF, 
	ISNULL(D.TenPhongBan, '') AS TenPhongBan, 
	D.DmBoPhanREF, 
	ISNULL(D.TenBoPhan,'') AS TenBoPhan, 
	D.DmNhomLamViecREF, 
	ISNULL(D.TenNhom, '') AS TenNhom, 
	D.DmDiaDiemLamViecREF, 
	D.TenDiaDiemLamViec, 
	D.SysNhanVienREF, 
	ISNULL(D.TenDangNhap, '') AS TenDangNhap,  
	D.TenNhanVien, 
	--Thong tin ve khach hang
	--D.DmKhachHangREF, 
	D.TenKhachHang, 
	[dbo].[f_ReturnListConcatNhanHangREF_v2](C.HopDongChiTietID, @NgayThucHien)NhanHang, 
	C.DmNhomNganhREF, 
	C.TenNhomNganh, 
	--Thong tin hinh thuc quang cao
	C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
	--Thong tin San pham
	dbo.GetProductIDByTypeProduct(A.TypeProduct) as DmSanPhamREF,
	dbo.GetProductNameByTypeProduct(A.TypeProduct) as TenSanPham,  
	C.DmNhomWebsiteREF, 
	C.TenNhomWebsite, 
	--C.DmWebsiteREF, 
	--C.TenWebsite, 
	C.DmChuyenMucREF, 
	C.TenChuyenMuc, 
	C.DmLoaiBannerREF, 
	C.TenLoaiBanner, 
	C.DmViTriREF, 
	C.TenViTri, 
	ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'Y'),'') DotChayHopDong,
	0 AS SoLuongDotChayHD,
	ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'N'),0) DotChayBooking,
	A.uv AS SoLuongDotChayBooking, 
	C.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong,
	C.DonViTinh DonViTinh, 
	dbo.ThucChay_GetDonGiaByNgayThucHien(A.NgayThucHien,A.HopDongChiTietREF,C.DonGia) as DonGia,
	ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong, A.NgayThucHien, A.HopDongChiTietREF),0) AS DonGiaTheoDonViTinh,
	C.ChietKhau, C.GiamGia, C.ThanhTien,
	C.TiLeTuVan,  C.ChiPhiTuVan,
	C.IsKhuyenMai,  
	C.KhuyenMai,
	--Thuc chay
	A.bannerid DmBannerREF,--A.DmBannerREF,
	0 DmChienDichREF,--A.DmChienDichREF,
	@DmWebsiteREF AS DmWebsiteREF,
	@TenWebsite AS TenWebsite,
	a.uvngay AS TongViewThucChay,
	0 AS TongClickThucChay,
	0 AS TongSoBaiViet,
	(CASE when ((C.IsKhuyenMai=0) AND (UPPER(C.DonViTinh) = 'CPR')) then ISNULL([dbo].[ThucChay_GetSoLuongThucChayChuanByDonViTinh_CPR] (A.uv,A.uvngay,C.SoLuong,C.DonViTinh, A.NgayThucHien, A.HopDongChiTietREF),0)
		  else 0
	  END
	) as SoLuongThucChay,
	A.NgayThucHien,
	0 as GiaTriThayDoi,
	ISNULL([dbo].[ThucChay_GetThanhTienChuanThucChay_CPR_ByDVT_CPR]
	(
		C.DonViTinh, 
		C.DonGia,
		C.SoLuong,
		A.uv,
		A.uvngay,
		C.HopDongChiTietID ,
		@NgayThucHien 	
	),0) as ThanhTienThucChayTruocTrietKhau
	from (	
		select 
		tcc.NgayThucHien,
		ROUND((tcc.uv*B.TiLeThucChayHDCTSoVoiBanner)/100,0) uv,
		ROUND((tcc.uvngay*B.TiLeThucChayHDCTSoVoiBanner)/100,0) uvngay,
		B.HopDongChiTietREF,
		tcc.TypeProduct,
		tcc.bannerid
		FROM  
		(
			SELECT distinct b.DmBannerID, b.HopDongChiTietREF, b.HopDongREF, isnull(b.TiLeThucChayHDCTSoVoiBanner,0)TiLeThucChayHDCTSoVoiBanner,
			b.DeletedStatus, b.DaThucHienUpdateTiLe
		   from dbo.ThucChayHopDongChiTietAndBanner b
		) B INNER JOIN dbo.ThucChayCPRTemp tcc ON Convert(nvarchar(50),tcc.bannerid) = B.DmBannerID
		WHERE b.HopDongREF = @HopDongID AND tcc.TypeProduct = @TypeProduct AND tcc.NgayThucHien = @NgayThucHien
		AND B.DeletedStatus = 0
		group by tcc.NgayThucHien, B.HopDongChiTietREF, tcc.TypeProduct,tcc.uv, tcc.uvngay, B.TiLeThucChayHDCTSoVoiBanner,tcc.bannerid
	 )A
	 INNER JOIN  dbo.HopDongChiTiet C on C.HopDongChiTietID = A.HopDongChiTietREF
	 INNER JOIN  dbo.HopDong D on D.HopDongID = C.HopDongFK
	 WHERE D.TrangThaiHopDong <> 3
	 AND C.DeletedStatus = 0
	 AND C.DmSanPhamREF IN (680,598,735)
	 AND C.DonViTinhREF = 30 --DON VI TINH LA CPR
	) TD
	
	
END

```
