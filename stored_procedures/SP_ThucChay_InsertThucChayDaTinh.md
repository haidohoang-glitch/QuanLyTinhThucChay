# Stored Procedure: `ThucChay_InsertThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:23.360000
- **Ngày sửa cuối**: 2022-12-21 15:20:23.937000

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


CREATE  PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh] 
	@NgayThucHien DATETIME,
	@SoHopDong NVARCHAR(50),
	@TypeProduct INT,
	@DmWebsiteREF INT, 
	@TenWebsite NVARCHAR(50),
	@DmBannerREF INT
AS
BEGIN
	
	--INSERT INTO [dbo].[Log_SP_Call]
 --          ([SP_NAME]
 --          ,[SP_TIME_CALL]
 --          ,[SP_END_TIME_CALL]
 --          ,[NOTE]
	--	   , VALUE_INPUT)
 --    VALUES
 --          ('[ThucChay_InsertThucChayDaTinh]'
 --          ,GETDATE()
 --          ,NULL
 --          ,''
	--	   , '@NgayThucHien = ' + CONVERT(NVARCHAR(50),@NgayThucHien,103) +
	--			', @SoHopDong = ' + @SoHopDong +
	--			', @TypeProduct = ' + CONVERT(NVARCHAR(50), @TypeProduct) +
	--			', @DmWebsiteREF = ' + CONVERT(NVARCHAR(50),@DmWebsiteREF) +
	--			', @TenWebsite = ' + @TenWebsite +
	--			', @DmBannerREF = ' + CONVERT(NVARCHAR(50),@DmBannerREF)
	--		)

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
	(CASE when (((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100))AND (TD.DonViTinh = 'VIEW')) then ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(TD.TongViewThucChay,TD.SoLuong,TD.DonViTinh, TD.NgayThucHien, TD.HopDongChiTietREF),0)
		when (((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100))AND (TD.DonViTinh = 'CLICK')) then ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(TD.TongClickThucChay,TD.SoLuong,TD.DonViTinh, TD.NgayThucHien, TD.HopDongChiTietREF),0)
		else 0
	  END
	) as SoLuongThucChayKM,
	(CASE when (TD.DonViTinh = 'VIEW') then dbo.[ThucChay_GetSoLuongLechTreoHa_V1](@NgayThucHien, TD.SoHopDong, TD.HopDongChiTietREF, TD.SoLuong, TD.DmSanPhamREF, TD.TongViewThucChay)
		when  (TD.DonViTinh = 'CLICK') then dbo.[ThucChay_GetSoLuongLechTreoHa_V1](@NgayThucHien, TD.SoHopDong, TD.HopDongChiTietREF, TD.SoLuong, TD.DmSanPhamREF, TD.TongClickThucChay)
		else 0
	  END
	)AS SoLuongLechTreoHa,
	(CASE when (TD.DonViTinh = 'VIEW') then dbo.[ThucChay_GetSoLuongLechTreoHa_V1](@NgayThucHien, TD.SoHopDong, TD.HopDongChiTietREF, TD.SoLuong, TD.DmSanPhamREF, TD.TongViewThucChay)*TD.DonGiaTheoDonViTinh
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
	C.DmSanPhamREF as DmSanPhamREF,
	C.TenSanPham as TenSanPham,  
	C.DmNhomWebsiteREF, 
	C.TenNhomWebsite, 
	--C.DmWebsiteREF, 
	--C.TenWebsite, 
	C.DmChuyenMucREF, 
	C.TenChuyenMuc, 
	C.DmLoaiBannerREF, 
	C.TenLoaiBanner, 
	C.DmBannerREF DmViTriREF, 
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
	A.TongSoBaiViet,
	--****haidh chinh sua	
	(CASE when (
					(C.IsKhuyenMai=0) AND ((UPPER(C.DonViTinh) = 'CPM')OR (UPPER(C.DonViTinh) = 'TRUE REACH'))
				) then ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(A.TongViewThucChay,C.SoLuong,C.DonViTinh
																				, A.NgayThucHien, A.HopDongChiTietREF),0)
		  when (
					(C.IsKhuyenMai=0) AND ((UPPER(C.DonViTinh) = 'CPC'))
		  ) then ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(A.TongClickThucChay,C.SoLuong,C.DonViTinh, A.NgayThucHien, A.HopDongChiTietREF),0)
		  else 0
	  END
	) as SoLuongThucChay,
	--Thanhuc Tien Thuc Chay
	A.NgayThucHien,
	0 as GiaTriThayDoi,
	--****haidh chinh sua	
	ISNULL(dbo.ThucChay_GetThanhTienChuanThucChay(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong,A.TongViewThucChay,A.TongClickThucChay,A.TongSoBaiViet,A.NgayThucHien,	A.HopDongChiTietREF),0) as ThanhTienThucChayTruocTrietKhau
	from (	
		select 
		A.NgayThucHien,
		round(SUM((A.TongViewThucChay*B.TiLeThucChayHDCTSoVoiBanner)/100),0) TongViewThucChay,
		round(SUM((A.TongClickThucChay*B.TiLeThucChayHDCTSoVoiBanner)/100),0) TongClickThucChay,
		SUM(ISNULL(A.TongSoBaiViet,0)) TongSoBaiViet,
		[dbo].[f_ReturnListConcatNhanHangREFByBanner] 
		(
			@SoHopDong,
			@TypeProduct,
			B.HopDongChiTietREF,
			A.DmWebsiteREF
		)DsNhanHangREF, 
		B.HopDongChiTietREF,
		A.TypeProduct,
		dbo.GetProductIDByTypeProduct(A.TypeProduct) AS DmSanPhamREF,
		A.DmWebsiteREF,
		A.TenWebsite,
		A.DmBannerREF
		from (SELECT * FROM dbo.ThucChayTemp 
						WHERE DmBannerREF = @DmBannerREF 
						AND SoHopDong = @SoHopDong 
						AND TypeProduct = @TypeProduct 
						AND DmWebsiteREF = @DmWebsiteREF) A
		INNER JOIN  
		(
			SELECT distinct b.DmBannerID, b.dsNhanHangREF, b.HopDongChiTietREF, b.HopDongREF, b.TiLeThucChayHDCTSoVoiBanner,
			b.DeletedStatus, b.DaThucHienUpdateTiLe
		   from dbo.ThucChayHopDongChiTietAndBanner b
		   WHERE B.DmBannerID = Convert(nvarchar(50),@DmBannerREF)
		) B on B.DmBannerID = Convert(nvarchar(50),A.DmBannerREF)
		WHERE 1=1
		AND B.DeletedStatus = 0
		group by A.NgayThucHien, B.HopDongChiTietREF, A.TypeProduct, A.TenWebsite, A.DmWebsiteREF, A.DmBannerREF
	 )A
	 INNER JOIN  (SELECT * FROM dbo.HopDongChiTiet C 
						WHERE 1=1  AND C.DeletedStatus = 0
						 --AND C.DmSanPhamREF IN (231,238,339,240,370,598,613,735,5056,680,5299)
						 AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = C.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 2 --Nhom Tinh Branding
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
							))
						 AND C.DmLoaiBannerREF NOT IN (17,18)--Khong tinh cho cac loai banner ChiPhi va Mua ngoai
						 AND C.DmLoaiREF <> 13 --Khong tinh thuc chay cho HTQC Mua Ngoai
						 AND C.DmLoaiREF <> 42
						 AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](C.DonViTinhREF, C.DonViTinh) = 3 --Đơn vị của hình thức CPM
						 AND C.DonViTinhREF <> 31
	 )C ON C.HopDongChiTietID = A.HopDongChiTietREF AND C.DmSanPhamREF = A.DmSanPhamREF
	 INNER JOIN (SELECT * FROM dbo.HopDong WHERE SoHopDong = @SoHopDong AND TrangThaiHopDong <> 3)D ON D.HopDongID = C.HopDongFK
	 INNER JOIN dbo.DmWebsite E ON E.DmWebsiteID = C.DmWebsiteREF 
	 WHERE 1=1
	
	) TD
	
	
END

```
