# Stored Procedure: `ThucChay_InsertThucChayDaTinhCPV`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:22.500000
- **Ngày sửa cuối**: 2019-02-15 11:13:14.380000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(100)` | No |
| `@DmBannerREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucChayDaTinh]


CREATE  PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinhCPV] 
	@NgayThucHien DATETIME,
	@SoHopDong NVARCHAR(50),
	@TypeProduct INT,
	@DmWebsiteREF INT, 
	@TenWebsite NVARCHAR(50),
	@DmBannerREF INT
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
	(CASE when (((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100))AND (TD.DonViTinh = 'CPV')) then ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(TD.TongSoBaiViet,TD.SoLuong,TD.DonViTinh, TD.NgayThucHien, TD.HopDongChiTietREF),0)
		when (((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100))AND (TD.DonViTinh = 'VIEW')) then ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(TD.TongViewThucChay,TD.SoLuong,TD.DonViTinh, TD.NgayThucHien, TD.HopDongChiTietREF),0)
		when (((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100))AND (TD.DonViTinh = 'CLICK')) then ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(TD.TongClickThucChay,TD.SoLuong,TD.DonViTinh, TD.NgayThucHien, TD.HopDongChiTietREF),0)
		
		else 0
	  END
	) as SoLuongThucChayKM,
	(CASE when (TD.DonViTinh = 'CPV') then dbo.[ThucChay_GetSoLuongLechTreoHa_V1](@NgayThucHien, TD.SoHopDong, TD.HopDongChiTietREF, TD.SoLuong, TD.DmSanPhamREF, TD.TongSoBaiViet)
		when (TD.DonViTinh = 'VIEW') then dbo.[ThucChay_GetSoLuongLechTreoHa_V1](@NgayThucHien, TD.SoHopDong, TD.HopDongChiTietREF, TD.SoLuong, TD.DmSanPhamREF, TD.TongViewThucChay)
		when  (TD.DonViTinh = 'CLICK') then dbo.[ThucChay_GetSoLuongLechTreoHa_V1](@NgayThucHien, TD.SoHopDong, TD.HopDongChiTietREF, TD.SoLuong, TD.DmSanPhamREF, TD.TongClickThucChay)
		else 0
	  END
	)AS SoLuongLechTreoHa,
	(CASE when (TD.DonViTinh = 'CPV') then dbo.[ThucChay_GetSoLuongLechTreoHa_V1](@NgayThucHien, TD.SoHopDong, TD.HopDongChiTietREF, TD.SoLuong, TD.DmSanPhamREF, TD.TongSoBaiViet)*TD.DonGiaTheoDonViTinh
		when (TD.DonViTinh = 'VIEW') then dbo.[ThucChay_GetSoLuongLechTreoHa_V1](@NgayThucHien, TD.SoHopDong, TD.HopDongChiTietREF, TD.SoLuong, TD.DmSanPhamREF, TD.TongViewThucChay)*TD.DonGiaTheoDonViTinh
		when  (TD.DonViTinh = 'CLICK') then dbo.[ThucChay_GetSoLuongLechTreoHa_V1](@NgayThucHien, TD.SoHopDong, TD.HopDongChiTietREF, TD.SoLuong, TD.DmSanPhamREF, TD.TongClickThucChay)*TD.DonGiaTheoDonViTinh
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
	--C.NhanHang, 
	A.DsNhanHangREF NhanHang,
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
	C.SoLuong AS SoLuongDotChayHD,
	ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'N'),0) DotChayBooking,
	dbo.GetSoLuongDotChayBookingByHopDongChiTiet(C.HopDongChiTietID) SoLuongDotChayBooking, 
	--Thong tin ve Tien
	--****haidh chinh sua
	C.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong,
	--****haidh chinh sua
	dbo.ThucChay_GetDonViTinhNotCPD(C.DonViTinh) as DonViTinh, 
	--'VIEW' DonViTinh, 
	dbo.ThucChay_GetDonGiaByNgayThucHien(A.NgayThucHien,A.HopDongChiTietREF,C.DonGia) as DonGia,
	--****haidh chinh sua 
	ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong, A.NgayThucHien, A.HopDongChiTietREF),0) AS DonGiaTheoDonViTinh,
	C.ChietKhau, C.GiamGia, C.ThanhTien,
	C.TiLeTuVan,  C.ChiPhiTuVan,
	C.IsKhuyenMai,  
	C.KhuyenMai,
	--Thuc chay
	A.DmBannerREF DmBannerREF,--A.DmBannerREF,
	0 DmChienDichREF,--A.DmChienDichREF,
	A.DmWebsiteREF,
	A.TenWebsite,
	--C.DmWebsiteREF,--A.DmWebsiteREF,
	--E.TenWebsite,
	--A.SoHopDong,
	A.TongViewThucChay,
	A.TongClickThucChay,
	--A.TongSoBaiViet,
	A.TongCPVThucChay TongSoBaiViet, --Tam thoi lay co du lieu nay lam sl cho CPV
	--****haidh chinh sua	
	(CASE when ((C.IsKhuyenMai=0) AND (UPPER(C.DonViTinh) = 'CPM')) then ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(A.TongViewThucChay,C.SoLuong,C.DonViTinh, A.NgayThucHien, A.HopDongChiTietREF),0)
		  when ((C.IsKhuyenMai=0) AND (UPPER(C.DonViTinh) = 'CPC')) then ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(A.TongClickThucChay,C.SoLuong,C.DonViTinh, A.NgayThucHien, A.HopDongChiTietREF),0)
		  when ((C.IsKhuyenMai=0) AND (UPPER(C.DonViTinh) = 'CPV')) then ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(A.TongCPVThucChay,C.SoLuong,C.DonViTinh, A.NgayThucHien, A.HopDongChiTietREF),0)
		  else 0
	  END
	) as SoLuongThucChay,
	--Thanhuc Tien Thuc Chay
	A.NgayThucHien,
	0 as GiaTriThayDoi,
	--****haidh chinh sua	
	ISNULL(dbo.ThucChay_GetThanhTienChuanThucChay(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong,A.TongViewThucChay,A.TongClickThucChay,A.TongCPVThucChay,A.NgayThucHien,	A.HopDongChiTietREF),0) as ThanhTienThucChayTruocTrietKhau
	from (	
			select 
			A.NgayThucHien,
			round(SUM((A.TongViewThucChay*B.TiLeThucChayHDCTSoVoiBanner)/100),0) TongViewThucChay,
			round(SUM((A.TongClickThucChay*B.TiLeThucChayHDCTSoVoiBanner)/100),0) TongClickThucChay,
			round(SUM((A.SoLuongCPV*B.TiLeThucChayHDCTSoVoiBanner)/100),0) TongCPVThucChay,
			SUM(ISNULL(A.TongSoBaiViet,0)) TongSoBaiViet,
			[dbo].[f_ReturnListConcatNhanHangREFByBanner_CPV]
			(	@SoHopDong,
				@TypeProduct,
				B.HopDongChiTietREF,
				@DmWebsiteREF
			) DsNhanHangREF,
			B.HopDongChiTietREF,
			A.TypeProduct,
			A.DmWebsiteREF,
			A.TenWebsite,
			A.DmBannerREF
			from (
				select tc.NgayThucHien, tc.TongViewThucChay, tc.TongClickThucChay
				, tc.TongSoBaiViet,tc.SoHopDong,
				(
					CASE WHEN ISNULL(tcc.totalview,0) = 0 THEN 0
					ELSE (tc.TongViewThucChay/tcc.totalview)*tcc.CPV
					END
				)SoLuongCPV
				, tc.TypeProduct, tc.DmWebsiteREF, tc.TenWebsite, tc.DmBannerREF
				  from dbo.ThucChayTemp tc INNER JOIN dbo.ThucChayCPVTemp tcc ON tc.DmBannerREF = tcc.bannerid
				  AND tcc.NgayThucHien = tc.NgayThucHien
				  AND tcc.bannerid = @DmBannerREF --tinh theo chi tiet banner
			) A
			INNER JOIN  
			(
				SELECT DISTINCT b.DmBannerID,
				       b.HopDongChiTietREF,
				       b.HopDongREF,
				       b.TiLeThucChayHDCTSoVoiBanner,
				       b.DeletedStatus,
				       b.DaThucHienUpdateTiLe
				FROM   dbo.ThucChayHopDongChiTietAndBanner b
				       INNER JOIN dbo.HopDongChiTiet hdct
				            ON  hdct.HopDongChiTietID = b.HopDongChiTietREF
				WHERE  hdct.DeletedStatus = 0
				       AND hdct.DonViTinhREF = 22 --CPV
			) B on B.DmBannerID = Convert(nvarchar(50),A.DmBannerREF)
			WHERE A.SoHopDong = @SoHopDong AND a.TypeProduct = @TypeProduct        
			AND A.DmWebsiteREF = @DmWebsiteREF
			AND B.DeletedStatus = 0
			group by A.NgayThucHien, B.HopDongChiTietREF, A.TypeProduct, A.TenWebsite, A.DmWebsiteREF,A.DmBannerREF
	 )A
	 INNER JOIN  dbo.HopDongChiTiet C on C.HopDongChiTietID = A.HopDongChiTietREF
	 INNER JOIN  dbo.HopDong D on D.HopDongID = C.HopDongFK
	 INNER JOIN dbo.DmWebsite E on E.DmWebsiteID = C.DmWebsiteREF 
	 WHERE D.TrangThaiHopDong <> 3
	 AND C.DeletedStatus = 0
	 AND C.DmLoaiREF <> 13 --Khong tinh thuc chay cho HTQC Mua Ngoai
	 AND C.DmSanPhamREF IN (240,598)
	 AND C.DonViTinh = N'CPV' 
	) TD
	
	
END

```
