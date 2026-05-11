# Stored Procedure: `ThucChay_InsertThucChayDaTinh_CPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-09-14 14:36:24.503000
- **Ngày sửa cuối**: 2021-05-12 14:52:55.643000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
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

--EXEC [dbo].[ThucChay_InsertThucChayDaTinh_CPR]


CREATE  PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_CPR] 
	@NgayThucHien DATETIME,
	@SoHopDong NVARCHAR(50),
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
	(CASE when (((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100))AND (TD.DonViTinh = 'VIEW')) then ISNULL(TD.SoLuongThucChay,0)
		when (((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100))AND (TD.DonViTinh = 'CLICK')) then ISNULL(TD.SoLuongThucChay,0)
		else 0
	  END
	) as SoLuongThucChayKM,
	(CASE when (TD.DonViTinh = 'VIEW') then 0
		when  (TD.DonViTinh = 'CLICK') then 0
		else 0
	  END
	)AS SoLuongLechTreoHa,
	(CASE when (TD.DonViTinh = 'VIEW') then 0
		when  (TD.DonViTinh = 'CLICK') then 0
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
	[dbo].[f_ReturnListConcatNhanHangREF_v2](C.HopDongChiTietID, @NgayThucHien) NhanHang, 
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
	CPR.UV AS SoLuongDotChayHD,
	N'CPR_GOI' DotChayBooking,
	A.uv AS SoLuongDotChayBooking, 
	C.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong,
	'VIEW' DonViTinh, 
	dbo.ThucChay_GetDonGiaByNgayThucHien(A.NgayThucHien,A.HopDongChiTietREF,C.DonGia) as DonGia,
	ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong, A.NgayThucHien, A.HopDongChiTietREF),0) AS DonGiaTheoDonViTinh,
	C.ChietKhau, C.GiamGia, C.ThanhTien,
	C.TiLeTuVan,  C.ChiPhiTuVan,
	C.IsKhuyenMai,  
	C.KhuyenMai,
	--Thuc chay
	C.DmBannerREF DmBannerREF,--A.DmBannerREF,
	0 DmChienDichREF,--A.DmChienDichREF,
	A.DmWebsiteREF,
	A.TenWebsite,
	A.TongViewThucChay,
	A.TongClickThucChay,
	A.TongSoBaiViet,
	A.TongViewThucChay as SoLuongThucChay,
	A.NgayThucHien,
	0 as GiaTriThayDoi,
	ISNULL([dbo].[ThucChay_GetThanhTienChuanThucChay_CPR]
	(
		C.DonViTinhREF, 
		C.DonGia,
		C.ChietKhau,
		CPR.UV,
		CPR.View_user,
		A.uv ,
		A.uvngay,
		A.TongViewThucChay ,
		C.HopDongChiTietID ,
		D.SoHopDong ,
		A.TypeProduct,
		@NgayThucHien 	
	),0) as ThanhTienThucChayTruocTrietKhau
	from (	
		select 
		A.NgayThucHien,
		round(SUM((A.TongViewThucChay*B.TiLeThucChayHDCTSoVoiBanner)/100),0) TongViewThucChay,
		round(SUM((A.TongClickThucChay*B.TiLeThucChayHDCTSoVoiBanner)/100),0) TongClickThucChay,
		SUM(ISNULL(A.TongSoBaiViet,0)) TongSoBaiViet,
		tcc.uv,
		tcc.uvngay,
		B.HopDongChiTietREF,
		A.TypeProduct,
		A.DmWebsiteREF,
		A.TenWebsite
		from ThucChayTemp A
		INNER JOIN  
		(
			SELECT distinct b.DmBannerID, b.HopDongChiTietREF, b.HopDongREF, b.TiLeThucChayHDCTSoVoiBanner,
			b.DeletedStatus, b.DaThucHienUpdateTiLe
		   from dbo.ThucChayHopDongChiTietAndBanner b
		) B on B.DmBannerID = Convert(nvarchar(50),A.DmBannerREF)
		INNER JOIN ThucChayCPRTemp tcc ON tcc.bannerid = A.DmBannerREF --AND tcc.typeproduct = A.TypeProduct
		WHERE a.SoHopDong = @SoHopDong AND a.TypeProduct = @TypeProduct AND A.DmWebsiteREF = @DmWebsiteREF
		AND B.DeletedStatus = 0
		group by A.NgayThucHien, B.HopDongChiTietREF, A.TypeProduct, A.TenWebsite, A.DmWebsiteREF,tcc.uv, tcc.uvngay
	 )A
	 INNER JOIN  HopDongChiTiet C on C.HopDongChiTietID = A.HopDongChiTietREF
	 INNER JOIN  HopDong D on D.HopDongID = C.HopDongFK
	 INNER JOIN DmWebsite E on E.DmWebsiteID = C.DmWebsiteREF 
	 INNER JOIN DonGiaCPR CPR ON CPR.DmLoaiBannerREF = C.DmLoaiBannerREF
	 WHERE D.TrangThaiHopDong != 3
	 AND C.DeletedStatus = 0
	 AND C.DmSanPhamREF IN (680)
	 AND c.DonViTinhREF = 10
	) TD
	
	
END

```
