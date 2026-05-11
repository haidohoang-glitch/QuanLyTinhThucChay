# Stored Procedure: `ThucChay_Insert_TinhLaiGTTD_ThucChayDaTinh_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-07-31 16:41:22.443000
- **Ngày sửa cuối**: 2019-11-09 10:02:14.193000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(100)` | No |
| `@DmBannerREF` | `int(4)` | No |
| `@GhiChu` | `nvarchar(2000)` | No |

## Definition (Source Code)

```sql
					  /*ThucChay_Insert_TinhLaiGTTD_ThucChayDaTinh_Admatic*/
CREATE  PROCEDURE [dbo].[ThucChay_Insert_TinhLaiGTTD_ThucChayDaTinh_Admatic] 
	@NgayThucHien DATETIME,
	@HopDongID INT, 
	@SoHopDong NVARCHAR(50), 
	@HopDongChiTietID INT,
	@TypeProduct INT, 
	@DmSanPhamREF INT, 
	@DmWebsiteREF INT, 
	@TenWebsite NVARCHAR(50), 
	@DmBannerREF INT,
	@GhiChu NVARCHAR(1000)
AS
BEGIN
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
	
	SELECT TD.ThucChayDaTinhID, 
	-----------------
	TD.HopDongID,	TD.SoHopDong, 	TD.DmMaHopDongREF, 	TD.TenMaHopDong, 	TD.NgayDanhSoHopDong, TD.NgayKyHopDong, 
	TD.NhanHopDong, TD.NgayNhanBanFax, TD.NgayNhanHopDongBanCung, TD.NgayChuyenHopDongChoKeToan, 
	TD.So, TD.Thang, TD.Nam,	TD.GiaTriHopDong, TD.CongNo,	TD.HopDongChiTietREF,	TD.DangSuDung, TD.IsGiayPhep, 
	TD.TrangThaiHopDong, TD.IsBanCung, 	TD.DmPhongBanREF, 	TD.TenPhongBan, 	TD.DmBoPhanREF, 	TD.TenBoPhan, 	TD.DmNhomLamViecREF, 	
	TD.TenNhom, 	TD.DmDiaDiemLamViecREF, 	TD.TenDiaDiemLamViec, 	TD.SysNhanVienREF, 	
	TD.TenDangNhap,  	TD.TenNhanVien, 	TD.TenKhachHang, 	TD.NhanHang,	TD.DmNhomNganhREF, 	TD.TenNhomNganh, 
	TD.DmHinhThucQuangCao, TD.TenHinhThucQuangCao,	TD.DmSanPhamREF,	TD.TenSanPham,  
	TD.DmNhomWebsiteREF, 	TD.TenNhomWebsite, 	TD.DmChuyenMucREF, 	TD.TenChuyenMuc, 
	TD.DmLoaiBannerREF, 	TD.TenLoaiBanner, 	TD.DmViTriREF, 	TD.TenViTri, 
	TD.DotChayHopDong,	TD.SoLuongDotChayHD, TD.DotChayBooking, TD.SoLuongDotChayBooking, 
	TD.SoLuong,TD.DonViTinh, 
	TD.DonGia,TD.DonGiaTheoDonViTinh,
	TD.ChietKhau, TD.GiamGia, TD.ThanhTien,
	TD.TiLeTuVan,  TD.ChiPhiTuVan,
	TD.IsKhuyenMai,  
	TD.KhuyenMai,
	TD.DmBannerREF,--A.DmBannerREF,
	TD.DmChienDichREF,--A.DmChienDichREF,
	TD.DmWebsiteREF,
	TD.TenWebsite,
	TD.TongViewThucChay,
	TD.TongClickThucChay,
	TD.TongTrueViewThucChay, --Don Vi tinh True View
	0 AS SoLuongThucChay,
	TD.NgayThucHien,
	TD.ThanhTienSauTrietKhauThucChay AS  GiaTriThayDoi,
	0 AS ThanhTienThucChayTruocTrietKhau,
	------------------

	0 AS GiaTriTrietKhauThucChay,
	0 AS ThanhTienSauTrietKhauThucChay,
	0 AS GiaTriHoaHongThucChay,
	0 AS ThanhTienThucThu,
	0 AS ThanhTienKM,
	0 AS SoLuongThucChayKM,
	(CASE	WHEN (TD.DonViTinh = 'VIEW') AND (TD.ChietKhau <> 100) then (TD.TongViewThucChay - TD.SoLuongThucChay)
			WHEN  (TD.DonViTinh = 'CLICK') AND (TD.ChietKhau <> 100) then (TD.TongClickThucChay - TD.SoLuongThucChay)
			WHEN  (TD.DonViTinh = 'TRUE VIEW') AND (TD.ChietKhau <> 100) then (TD.TongTrueViewThucChay- TD.SoLuongThucChay)
			--KM
			WHEN (TD.DonViTinh = 'VIEW') AND (TD.ChietKhau = 100) then (TD.TongViewThucChay - TD.SoLuongThucChayKM)
			WHEN  (TD.DonViTinh = 'CLICK') AND (TD.ChietKhau = 100) then (TD.TongClickThucChay - TD.SoLuongThucChayKM)
			WHEN  (TD.DonViTinh = 'TRUE VIEW') AND (TD.ChietKhau = 100) then (TD.TongTrueViewThucChay- TD.SoLuongThucChayKM)
		else 0
		END
	)AS SoLuongLechTreoHa,
	(CASE	WHEN (TD.DonViTinh = 'VIEW')  AND (TD.ChietKhau <> 100)  THEN  (TD.TongViewThucChay - TD.SoLuongThucChay)*TD.DonGiaTheoDonViTinh
			WHEN  (TD.DonViTinh = 'CLICK')  AND (TD.ChietKhau <> 100)  THEN (TD.TongClickThucChay - TD.SoLuongThucChay)*TD.DonGiaTheoDonViTinh
			WHEN  (TD.DonViTinh = 'TRUE VIEW')  AND (TD.ChietKhau <> 100)  THEN (TD.TongTrueViewThucChay - TD.SoLuongThucChay)*TD.DonGiaTheoDonViTinh
			--KM
			WHEN (TD.DonViTinh = 'VIEW')  AND (TD.ChietKhau = 100)  THEN  (TD.TongViewThucChay - TD.SoLuongThucChayKM)*TD.DonGiaTheoDonViTinh
			WHEN  (TD.DonViTinh = 'CLICK')  AND (TD.ChietKhau = 100)   THEN (TD.TongClickThucChay - TD.SoLuongThucChayKM)*TD.DonGiaTheoDonViTinh
			WHEN  (TD.DonViTinh = 'TRUE VIEW')   AND (TD.ChietKhau = 100)  THEN (TD.TongTrueViewThucChay - TD.SoLuongThucChayKM)*TD.DonGiaTheoDonViTinh
		else 0
		END
	)AS ThanhTienLechTreoHa,
	GETDATE() AS CreatedAt,
	GETDATE() AS LastModifiedAt,
	0 IsPheDuyet,
	'' PheDuyetBy,
	'' PheDuyetAt,
	TD.SoLuongThucChay AS SoLuongThayDoi,
	TD.SoLuongThucChayKM AS  SoLuongKMThayDoi,
	TD.ThanhTienKM AS GiaTriKMThayDoi,
	@GhiChu GhiChu
	FROM
	(
			SELECT  NEWID() ThucChayDaTinhID, TD.*, 
			ISNULL(((TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) AS GiaTriTrietKhauThucChay,
			ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) AS ThanhTienSauTrietKhauThucChay,
			ISNULL((((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS GiaTriHoaHongThucChay,
			ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100 - ((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS ThanhTienThucThu,
			(CASE WHEN TD.ChietKhau = 100 then TD.ThanhTienThucChayTruocTrietKhau
				else 0
			  END
			) as ThanhTienKM,
			(CASE when (((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) AND (TD.DonGiaTheoDonViTinh <> 0)) then TD.ThanhTienThucChayTruocTrietKhau/TD.DonGiaTheoDonViTinh
				else 0
			  END
			) as SoLuongThucChayKM
			
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
			C.DanhSachNhanHangREF NhanHang,
			C.DmNhomNganhREF, 
			C.TenNhomNganh, 
			--Thong tin hinh thuc quang cao
			C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
			--Thong tin San pham
			dbo.GetProductIDByTypeProduct(A.TypeProduct) as DmSanPhamREF,
			dbo.GetProductNameByTypeProduct(A.TypeProduct) as TenSanPham,  
			C.DmNhomWebsiteREF, 
			C.TenNhomWebsite, 
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
			C.SoLuong AS SoLuong,
			(CASE WHEN A.DonViTinh = 'CPM' THEN 'VIEW'
				WHEN A.DonViTinh = 'TRUE VIEW' THEN 'TRUE VIEW'
				ELSE 'CLICK'
				--HAIDH COMMENT: them thong tin don vi tinh voi True View
				END
			 ) DonViTinh, 
			dbo.ThucChay_GetDonGiaByNgayThucHien(A.NgayThucHien,A.HopDongChiTietREF,C.DonGia) as DonGia,
			(CASE when (A.DonViTinh = 'CPM') then CONVERT(FLOAT,A.DonGia_Banner)/1000
				  else  A.DonGia_Banner --DUNG CHO CA CPC VA TRUE VIEW
			  END
			) AS DonGiaTheoDonViTinh,
			C.ChietKhau, C.GiamGia, C.ThanhTien,
			C.TiLeTuVan,  C.ChiPhiTuVan,
			C.IsKhuyenMai,  
			C.KhuyenMai,
			--Thuc chay
			@DmBannerREF DmBannerREF,--A.DmBannerREF,
			0 DmChienDichREF,--A.DmChienDichREF,
			A.DmWebsiteREF,
			A.TenWebsite,
			A.TongViewThucChay,
			A.TongClickThucChay,
			A.TongTrueViewThucChay, --Don Vi tinh True View
			--****haidh chinh sua	
			(CASE WHEN ((C.ChietKhau  <> 100) AND (A.DonViTinh = 'CPM')) 
				  THEN ISNULL([dbo].[ThucChay_GetSoLuongThucChay_Admatic_v1] (A.TongViewThucChay,A.TongClickThucChay,A.TongTrueViewThucChay,A.DonGia_Banner ,A.DonViTinh,A.NgayThucHien, A.HopDongChiTietREF,C.SoLuong, C.DonGia, C.ThanhTien, C.ChietKhau ),0)
				  WHEN ((C.ChietKhau <> 100) AND (A.DonViTinh = 'CPC')) 
				  THEN ISNULL([dbo].[ThucChay_GetSoLuongThucChay_Admatic_v1] (A.TongViewThucChay,A.TongClickThucChay,A.TongTrueViewThucChay,A.DonGia_Banner ,A.DonViTinh,A.NgayThucHien, A.HopDongChiTietREF,C.SoLuong, C.DonGia, C.ThanhTien, C.ChietKhau ),0)
				  --HAIDH COMMENT: them thong tin don vi tinh voi True View
				   WHEN ((C.ChietKhau <> 100) AND (A.DonViTinh = 'TRUE VIEW')) 
				  THEN ISNULL([dbo].[ThucChay_GetSoLuongThucChay_Admatic_v1] (A.TongViewThucChay,A.TongClickThucChay,A.TongTrueViewThucChay ,A.DonGia_Banner ,A.DonViTinh,A.NgayThucHien, A.HopDongChiTietREF,C.SoLuong, C.DonGia, C.ThanhTien, C.ChietKhau ),0)
				  ELSE 0
			  END
			) as SoLuongThucChay,
			--Thanhuc Tien Thuc Chay
			A.NgayThucHien,
			0 as GiaTriThayDoi,
			--HAIDH COMMENT: them thong tin don vi tinh voi True View
			ISNULL(dbo.[ThucChay_GetThanhTienChuanThucChay_Admatic](C.SoLuong, C.DonGia, C.ThanhTien, C.ChietKhau,A.DonViTinh,A.DonGia_Banner,D.NgayKyHopDong,A.TongViewThucChay,A.TongClickThucChay,A.TongTrueViewThucChay,A.NgayThucHien,	A.HopDongChiTietREF),0) as ThanhTienThucChayTruocTrietKhau
			from (	
				select 
				A.NgayThucHien,
				round(SUM((ISNULL(A.TongViewThucChay,0)*B.TiLeThucChayHDCTSoVoiBanner)/100),0) TongViewThucChay,
				round(SUM((ISNULL(A.TongClickThucChay,0)*B.TiLeThucChayHDCTSoVoiBanner)/100),0) TongClickThucChay,
				round(SUM((ISNULL(A.TongTrueViewThucChay,0)*B.TiLeThucChayHDCTSoVoiBanner)/100),0) TongTrueViewThucChay,--Don Vi Tinh True View
				@HopDongChiTietID HopDongChiTietREF,
				A.DmBannerREF,
				B.DonGia_Banner,
				B.DonViTinh,
				A.TypeProduct,
				A.DmSanPhamref,
				A.DmWebsiteREF,
				A.TenWebsite
				from dbo.ThucChay_Admatic A
				INNER JOIN  
				(
					SELECT distinct b.DmBannerID, b.dsNhanHangREF, b.HopDongChiTietREF, b.HopDongREF, b.TiLeThucChayHDCTSoVoiBanner,
					b.DeletedStatus, b.DaThucHienUpdateTiLe, b.DmSanPhamID, B.DonGia_banner, b.DonViTinh
				   from dbo.ThucChayHopDongChiTietAndBanner_Admatic b
				) B on B.DmBannerID = Convert(nvarchar(50),A.DmBannerREF) AND B.DmSanPhamID = A.DmSanPhamREF
				WHERE a.SoHopDong = @SoHopDong AND a.TypeProduct = @TypeProduct AND A.DmWebsiteREF = @DmWebsiteREF
				AND B.DeletedStatus = 0
				AND A.DmBannerREF = @DmBannerREF
				AND A.NgayThucHien = @NgayThucHien
				group by A.NgayThucHien, A.TypeProduct, A.DmSanPhamREF, A.TenWebsite, A.DmWebsiteREF, B.DonGia_banner, A.DmBannerREF, B.DonViTinh
			 )A
			 INNER JOIN (SELECT * FROM dbo.HopDongChiTiet C WHERE C.HopDongChiTietID = @HopDongChiTietID) C on C.HopDongChiTietID = A.HopDongChiTietREF
			 INNER JOIN  (SELECT * FROM dbo.HopDong D WHERE D.HopDongID = @HopDongID)D on D.HopDongID = C.HopDongFK
			 WHERE D.TrangThaiHopDong <> 3
			 AND C.DeletedStatus = 0
			 AND C.HopDongChiTietID = @HopDongChiTietID
			 AND D.HopDongID = @HopDongID
			 AND C.DmLoaiREF = 42 --Admatic
			 AND C.DmSanPhamREF IN  (231,238,339,240,370,598,613,733,342)
			 AND C.DmLoaiBannerREF NOT IN (17,18)--Khong tinh cho cac loai banner ChiPhi va Mua ngoai
			 --HAIDH COMMENT: them thong tin don vi tinh voi True View
			 AND C.DonViTinhREF IN (1,10,2,32) --Chi tinh cho Goi, CPM, CPC, TRUE VIEW
			 ) TD
	)TD
	
END



```
