# Stored Procedure: `ThucChay_InsertThucChayDaTinh_ByHDLoaiSP_ThieuBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-12 11:16:05.243000
- **Ngày sửa cuối**: 2014-11-19 12:16:58.337000

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
-- Author:		PhuongTM
-- Create date: 2014-06-12
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucChayDaTinh_ByHDLoaiSP_ThieuBanner]

CREATE PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_ByHDLoaiSP_ThieuBanner] 
	@NgayThucHien DATETIME,
	@SoHopDong NVARCHAR(50),
	@TypeProduct INT,
	@DmWebsiteREF INT, 
	@TenWebsite NVARCHAR(50)
AS
BEGIN

INSERT INTO dbo.ThucChayDaTinh_ThieuBanner 
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
	'' PheDuyetAt
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
		b.DangSuDung, b.IsGiayPhep, b.TrangThaiHopDong,b.IsBanCung, 
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
		0 AS DmHinhThucQuangCao, '' AS TenHinhThucQuangCao, 
		--Thong tin San pham
		dbo.GetProductIDByTypeProduct(a.TypeProduct) as DmSanPhamREF,
		dbo.GetProductNameByTypeProduct(a.TypeProduct) as TenSanPham,  
		0 DmNhomWebsiteREF, 
		'' TenNhomWebsite, 
		0 DmChuyenMucREF, 
		'' TenChuyenMuc, 
		0 DmLoaiBannerREF, 
		'' TenLoaiBanner, 
		0 DmViTriREF, 
		'' TenViTri, 
		'' DotChayHopDong,
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
		A.DmWebsiteREF,
		A.TenWebsite,
		A.PageView TongViewThucChay,
		A.Click TongClickThucChay,
		A.TongSoBaiViet,
		(CASE when (b.DonViTinh = 'VIEW') THEN ISNULL([dbo].[ThucChay_GetSoLuongThucChayByHDLoaiSP](@NgayThucHien, A.PageView, A.SoHopDong, [dbo].[GetProductIDByTypeProduct](A.TypeProduct)),0) 
			when (b.DonViTinh = 'CLICK') THEN ISNULL([dbo].[ThucChay_GetSoLuongThucChayByHDLoaiSP](@NgayThucHien, A.Click, A.SoHopDong, [dbo].[GetProductIDByTypeProduct](A.TypeProduct)),0) 
			else 0
		END
		) AS SoLuongThucChay,
		--Thanhuc Tien Thuc Chay
		A.NgayThucHien,
		0 as GiaTriThayDoi
	FROM (
		SELECT dbo.GetProductNameByTypeProduct(tc.TypeProduct) AS TenSanPham
		, tc.TypeProduct, tc.SoHopDong,tc.DmWebsiteREF, tc.TenWebsite ,
		SUM(ISNULL(tc.TongViewThucChay,0)) AS PageView,
		SUM(ISNULL(tc.TongClickThucChay,0)) AS Click,
		SUM(ISNULL(tc.TongSoBaiViet,0)) AS TongSoBaiViet,
		tc.NgayThucHien	 
		FROM ThucChayTemp tc
		WHERE tc.SoHopDong = @SoHopDong
		AND tc.TypeProduct = @TypeProduct
		AND tc.DmWebsiteREF = @DmWebsiteREF
		GROUP BY tc.TypeProduct, tc.SoHopDong,tc.DmWebsiteREF, tc.TenWebsite,tc.NgayThucHien
	)A LEFT JOIN
	(
		SELECT (case when HDCT.DmSanPhamREF=231 then 3
					 when HDCT.DmSanPhamREF=238 then 4
					 when HDCT.DmSanPhamREF=339 then 5
					 when HDCT.DmSanPhamREF=342 then 6
					 when HDCT.DmSanPhamREF=337 then 7
					 when HDCT.DmSanPhamREF=240 then 8
					 when HDCT.DmSanPhamREF=370 then 9
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
		hd.DangSuDung, hd.IsGiayPhep, hd.TrangThaiHopDong,hd.IsBanCung, 
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
		SUM(hdct.SoLuong) soluongdotchayHD,
		SUM(hdct.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)) soluong,
		SUM(hdct.ThanhTien) ThanhTien, 
		MAX(dbo.ThucChay_GetDonViTinhNotCPD(hdct.DonViTinh)) as DonViTinh,
		--max(hdct.ThanhTien/hdct.SoLuong) DonGiaSauCKMax,
		MAX(hdct.ThanhTien/(hdct.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh))) DonGiaSauCK,
		MAX(hdct.DonGia/dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)) DonGia						
		FROM HopDong hd
		INNER JOIN HopDongChiTiet hdct ON HD.HopDongID = HDCT.HopDongFK
		AND HDCT.DmSanPhamREF IN (231,238,339,240,370)
		AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) = 3 --Đơn vị của hình thức CPM
		AND hdct.DeletedStatus = 0
		AND hdct.SoLuong >0
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
	ON UPPER(LTRIM(RTRIM(A.SoHopDong))) = B.SoHopDong AND
		A.TypeProduct = B.type_product 
		--AND B.DonGiaSauCK > 0
	--ORDER BY A.TenSanPham ,a.SoHopDong,a.TenWebsite 
	) TD
	WHERE TD.SoHopDong IS NOT NULL
		

END

```
