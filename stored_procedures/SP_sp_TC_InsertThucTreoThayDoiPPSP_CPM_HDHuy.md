# Stored Procedure: `sp_TC_InsertThucTreoThayDoiPPSP_CPM_HDHuy`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-23 17:58:33.213000
- **Ngày sửa cuối**: 2017-06-23 17:58:33.213000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@NgaythucHien` | `datetime(8)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(200)` | No |
| `@SoLuongThucChayWebsite` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucChayDaTinh_PR]


CREATE  PROCEDURE [dbo].[sp_TC_InsertThucTreoThayDoiPPSP_CPM_HDHuy]
	@HopDongID INT,
	@DmSanPhamREF INT,
	@TenSanPham NVARCHAR(50),
	@NgaythucHien DATETIME,
	@GiaTriThayDoi FLOAT,
	@DmWebsiteREF INT,
	@TenWebsite NVARCHAR(100),
	@SoLuongThucChayWebsite INT
AS
BEGIN
	PRINT @HopDongID
	
	INSERT INTO dbo.ThucChayDaTinh 
	SELECT  NEWID(), TD.*,
	(TD.DonGia)* TD.SoLuongThucChay as ThanhTienThucChayTruocTrietKhau,
	(((TD.DonGia)* TD.SoLuongThucChay) - (TD.DonGiaTheoDonViTinh* TD.SoLuongThucChay))GiaTriTrietKhauThucChay,
	(TD.DonGiaTheoDonViTinh* TD.SoLuongThucChay) AS ThanhTienThucChaySauTrietKhau,
	0 AS GiaTriHoaHongThucChay,
	0 AS ThanhTienThucThu,
	(CASE when (TD.DonViTinh = 'VIEW') THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayKMByHDLoaiSP(@NgayThucHien, TD.TongViewThucChay, TD.SoHopDong, TD.DmSanPhamREF),0)*(TD.DonGia) 
			when (TD.DonViTinh = 'CLICK') THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayKMByHDLoaiSP(@NgayThucHien, TD.TongClickThucChay, TD.SoHopDong, TD.DmSanPhamREF),0)*(TD.DonGia) 
			else 0
		END
		)AS ThanhTienKM,
	(CASE when (TD.DonViTinh = 'VIEW') THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayKMByHDLoaiSP(@NgayThucHien, TD.TongViewThucChay, TD.SoHopDong, TD.DmSanPhamREF),0) 
			when (TD.DonViTinh = 'CLICK') THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayKMByHDLoaiSP(@NgayThucHien, TD.TongClickThucChay, TD.SoHopDong, TD.DmSanPhamREF),0) 
			else 0
		END
		)AS SoLuongThucChayKM,		
	(CASE when (TD.DonViTinh = 'VIEW') THEN dbo.ThucChay_GetSoLuongLechTreoHa(@NgayThucHien, TD.SoHopDong, TD.HopDongChiTietREF, TD.SoLuong, TD.DmSanPhamREF, TD.TongViewThucChay)
	 
			when (TD.DonViTinh = 'CLICK') THEN dbo.ThucChay_GetSoLuongLechTreoHa(@NgayThucHien, TD.SoHopDong, TD.HopDongChiTietREF, TD.SoLuong, TD.DmSanPhamREF, TD.TongClickThucChay) 
			else 0
		END
	) AS SoLuongLechTreoHa,
	(CASE when (TD.DonViTinh = 'VIEW') THEN dbo.ThucChay_GetSoLuongLechTreoHa(@NgayThucHien, TD.SoHopDong, TD.HopDongChiTietREF, TD.SoLuong, TD.DmSanPhamREF, TD.TongViewThucChay)*TD.DonGiaTheoDonViTinh 
			when (TD.DonViTinh = 'CLICK') THEN dbo.ThucChay_GetSoLuongLechTreoHa(@NgayThucHien, TD.SoHopDong, TD.HopDongChiTietREF, TD.SoLuong, TD.DmSanPhamREF, TD.TongClickThucChay)*TD.DonGiaTheoDonViTinh 
			else 0
		END
	) AS ThanhTienLechTreoHa,
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
		isnull(b.HopDongID,0) HopDongID,
		--Thong tin ve ma so 
		b.SoHopDong, 
		b.DmMaHopDongREF, 
		b.TenMaHopDong, 
		--Thong tin ve thoi gian
		b.NgayDanhSoHopDong, b.NgayKyHopDong, 
		b.NhanHopDong, b.NgayNhanBanFax, b.NgayNhanHopDongBanCung, b.NgayChuyenHopDongChoKeToan, 
		b.So, b.Thang, b.Nam, 
		--Thong tin ve gia tri
		b.GiaTriHopDong, b.CongNo,
		--Thong tin chi tiet phan bo
		0 HopDongChiTietREF,
		--Thong tin ve trang thai
		b.DangSuDung, b.IsGiayPhep, 2 TrangThaiHopDong,b.IsBanCung, 
		--Thong tin ve Nhan vien kinh doanh
		b.DmPhongBanREF, 
		ISNULL(b.TenPhongBan, '') AS TenPhongBan, 
		b.DmBoPhanREF, 
		ISNULL(b.TenBoPhan,'') AS TenBoPhan, 
		b.DmNhomLamViecREF, 
		ISNULL(b.TenNhom, '') AS TenNhom, 
		b.DmDiaDiemLamViecREF, 
		b.TenDiaDiemLamViec, 
		b.SysNhanVienREF, 
		ISNULL(b.TenDangNhap, '') AS TenDangNhap,  
		b.TenNhanVien, 
		--Thong tin ve khach hang
		--D.DmKhachHangREF, 
		b.TenKhachHang, 
		'' NhanHang, 
		0 DmNhomNganhREF, 
		'' TenNhomNganh, 
		--Thong tin hinh thuc quang cao
		b.DmHinhThucQC AS DmHinhThucQuangCao,
		b.TenHinhThucQC AS TenHinhThucQuangCao, 
		--Thong tin San pham
		@DmSanPhamREF as DmSanPhamREF,
		@TenSanPham as TenSanPham,  
		0 DmNhomWebsiteREF, 
		'' TenNhomWebsite, 
		0 DmChuyenMucREF, 
		'' TenChuyenMuc, 
		0 DmLoaiBannerREF, 
		'' TenLoaiBanner, 
		0 DmViTriREF, 
		'' TenViTri, 
		'HDHUY' DotChayHopDong,
		b.soluongdotchayHD AS SoLuongDotChayHD,
		'' DotChayBooking,
		0 AS SoLuongDotChayBooking, 
		--Thong tin ve Tien
		b.soluong, 
		b.DonViTinh, 
		b.DonGia as DonGia, 
		b.DonGiaSauCK AS DonGiaTheoDonViTinh,
		0 ChietKhau, 0 GiamGia, ISNULL(b.ThanhTien,0) ThanhTien,
		0 TiLeTuVan,  0 ChiPhiTuVan,
		0 IsKhuyenMai,  
		'' KhuyenMai,
		--Thuc chay
		0 DmBannerREF,--A.DmBannerREF,
		0 DmChienDichREF,--A.DmChienDichREF,
		@DmWebsiteREF DmWebsiteREF,
		@TenWebsite TenWebsite,
		0 TongViewThucChay,
		0 TongClickThucChay,
		0 TongSoBaiViet,
		0 AS SoLuongThucChay,
		--Thanhuc Tien Thuc Chay
		@NgaythucHien NgayThucHien,
		@GiaTriThayDoi as GiaTriThayDoi
	FROM 
	(
		SELECT (case when HDCT.DmSanPhamREF=231 then 3
					 when HDCT.DmSanPhamREF=238 then 4
					 when HDCT.DmSanPhamREF=339 then 5
					 when HDCT.DmSanPhamREF=342 then 6
					 when HDCT.DmSanPhamREF=337 then 7
					 when HDCT.DmSanPhamREF=240 then 8
					else 9
				end) as type_product, hd.SoHopDong, 
				hd.HopDongID,
		--Thong tin ve ma so 
		hd.DmMaHopDongREF, 
		hd.TenMaHopDong, 
		--Thong tin ve thoi gian
		hd.NgayDanhSoHopDong, hd.NgayKyHopDong, 
		hd.NhanHopDong, hd.NgayNhanBanFax, hd.NgayNhanHopDongBanCung, hd.NgayChuyenHopDongChoKeToan, 
		hd.So, hd.Thang, hd.Nam, 
		--Thong tin ve gia tri
		hd.GiaTriHopDong, hd.CongNo,
		--Thong tin chi tiet phan bo
		--Thong tin ve trang thai
		hd.DangSuDung, hd.IsGiayPhep, 2 TrangThaiHopDong,hd.IsBanCung, 
		--Thong tin ve Nhan vien kinh doanh
		hd.DmPhongBanREF, 
		ISNULL(hd.TenPhongBan, '') AS TenPhongBan, 
		hd.DmBoPhanREF, 
		ISNULL(hd.TenBoPhan,'') AS TenBoPhan, 
		hd.DmNhomLamViecREF, 
		ISNULL(hd.TenNhom, '') AS TenNhom, 
		hd.DmDiaDiemLamViecREF, 
		hd.TenDiaDiemLamViec, 
		hd.SysNhanVienREF, 
		ISNULL(hd.TenDangNhap, '') AS TenDangNhap,  
		hd.TenNhanVien, 
		--Thong tin ve khach hang
		--D.DmKhachHangREF, 
		hd.TenKhachHang,
		MAX(hdct.DmLoaiREF) DmHinhThucQC,
		MAX(hdct.TenLoai) TenHinhThucQC,
		SUM(hdct.SoLuong) soluongdotchayHD,
		SUM(hdct.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)) soluong,
		SUM(hdct.ThanhTien) ThanhTien, 
		MAX(dbo.ThucChay_GetDonViTinhNotCPD(hdct.DonViTinh)) as DonViTinh,
		--max(hdct.ThanhTien/hdct.SoLuong) DonGiaSauCKMax,
		MAX(hdct.ThanhTien/(hdct.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh))) DonGiaSauCK,
		MAX(hdct.DonGia/dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)) DonGia						
		FROM HopDong hd
		INNER JOIN HopDongChiTiet hdct ON HD.HopDongID = HDCT.HopDongFK
		--AND HDCT.DmSanPhamREF IN (231,238,339,240,370)
		--AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) = 3 --Đơn vị của hình thức CPM
		AND hdct.DeletedStatus = 0
		--AND hdct.SoLuong >0
		WHERE hd.HopDongID = @HopDongID
		AND hdct.DmSanPhamREF =@DmSanPhamREF
		GROUP BY HDCT.DmSanPhamREF,  HD.SoHopDong,
		hd.HopDongID,
		--Thong tin ve ma so 
		hd.DmMaHopDongREF, 
		hd.TenMaHopDong, 
		--Thong tin ve thoi gian
		hd.NgayDanhSoHopDong, hd.NgayKyHopDong, 
		hd.NhanHopDong, hd.NgayNhanBanFax, hd.NgayNhanHopDongBanCung, hd.NgayChuyenHopDongChoKeToan, 
		hd.So, hd.Thang, hd.Nam, 
		--Thong tin ve gia tri
		hd.GiaTriHopDong, hd.CongNo,
		--Thong tin chi tiet phan bo
		--Thong tin ve trang thai
		hd.DangSuDung, hd.IsGiayPhep, hd.TrangThaiHopDong,hd.IsBanCung, 
		--Thong tin ve Nhan vien kinh doanh
		hd.DmPhongBanREF, 
		hd.TenPhongBan, 
		hd.DmBoPhanREF, 
		hd.TenBoPhan, 
		hd.DmNhomLamViecREF, 
		hd.TenNhom, 
		hd.DmDiaDiemLamViecREF, 
		hd.TenDiaDiemLamViec, 
		hd.SysNhanVienREF, 
		hd.TenDangNhap,  
		hd.TenNhanVien, 
		hd.TenKhachHang
	)B 
	
	) TD
	WHERE TD.SoHopDong IS NOT NULL
		

END

```
