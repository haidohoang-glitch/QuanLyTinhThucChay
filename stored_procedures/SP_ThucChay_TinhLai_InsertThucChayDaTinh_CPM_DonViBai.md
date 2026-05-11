# Stored Procedure: `ThucChay_TinhLai_InsertThucChayDaTinh_CPM_DonViBai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-03-05 15:24:09.233000
- **Ngày sửa cuối**: 2021-04-15 10:03:27.610000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@GhiChuTinhLai` | `nvarchar(2000)` | No |

## Definition (Source Code)

```sql
--EXEC [ThucChay_TinhLai_InsertThucChayDaTinh_CPM_DonViBai]
-------------------------------------------------------------
CREATE PROCEDURE [dbo].[ThucChay_TinhLai_InsertThucChayDaTinh_CPM_DonViBai] 
	@NgayThucHien DATETIME,
	@HopDongID INT,
	@HopDongChiTietREF INT,
	@DmSanPhamREF INT,
	@GhiChuTinhLai NVARCHAR(1000)
AS
BEGIN

	DECLARE @NgayGioiHanTinh DATETIME, @SoHopDong NVARCHAR(50)
	SET @NgayGioiHanTinh = '2021-01-01'
	SET @SoHopDong = ISNULL((SELECT TOP (1) hd.SoHopDong FROM dbo.HopDong hd WHERE hd.HopDongID = @HopDongID ORDER BY hd.HopDongID),'')
	--KIEM TRA TINH TON TAI CỦA THUC TREO VA THUC CHAY CUA HOP DONG DON VI BAI

	INSERT INTO [dbo].[ThucChayDaTinh]
           ([ThucChayDaTinhID]
           ,[HopDongID]
           ,[SoHopDong]
           ,[DmMaHopDongREF]
           ,[TenMaHopDong]
           ,[NgayDanhSoHopDong]
           ,[NgayKyHopDong]
           ,[NhanHopDong]
           ,[NgayNhanBanFax]
           ,[NgayNhanHopDongBanCung]
           ,[NgayChuyenHopDongChoKeToan]
           ,[So]
           ,[Thang]
           ,[Nam]
           ,[GiaTriHopDong]
           ,[CongNo]
           ,[HopDongChiTietREF]
           ,[DangSuDung]
           ,[IsGiayPhep]
           ,[TrangThaiHopDong]
           ,[IsBanCung]
           ,[DmPhongBanREF]
           ,[TenPhongBan]
           ,[DmBoPhanREF]
           ,[TenBoPhan]
           ,[DmNhomLamViecREF]
           ,[TenNhomLamViec]
           ,[DmDiaDiemLamViecREF]
           ,[TenDiaDiemLamViec]
           ,[SysNhanVienREF]
           ,[TenDangNhap]
           ,[TenNhanVien]
           ,[TenKhachHang]
           ,[NhanHang]
           ,[DmNhomNganhREF]
           ,[TenNhomNganh]
           ,[DmHinhThucQuangCao]
           ,[TenHinhThucQuangCao]
           ,[DmSanPhamREF]
           ,[TenSanPham]
           ,[DmNhomWebsiteREF]
           ,[TenNhomWebsite]
           ,[DmChuyenMucREF]
           ,[TenChuyenMuc]
           ,[DmLoaiBannerREF]
           ,[TenLoaiBanner]
           ,[DmViTriREF]
           ,[TenViTri]
           ,[DotChayHopDong]
           ,[SoLuongDotChayHD]
           ,[DotChayBooking]
           ,[SoLuongDotChayBooking]
           ,[SoLuong]
           ,[DonViTinh]
           ,[DonGia]
           ,[DonGiaTheoDonVi]
           ,[ChietKhau]
           ,[GiamGia]
           ,[ThanhTien]
           ,[TiLeTuVan]
           ,[ChiPhiTuVan]
           ,[IsKhuyenMai]
           ,[KhuyenMai]
           ,[DmBannerREF]
           ,[DmChienDichREF]
           ,[DmWebsiteREF]
           ,[TenWebsite]
           ,[TongViewThucChay]
           ,[TongClickThucChay]
           ,[TongSoBaiViet]
           ,[SoLuongThucChay]
           ,[NgayThucHien]
           ,[GiaTriThayDoi]
           ,[ThanhTienThucChayTruocTrietKhau]
           ,[GiaTriTrietKhauThucChay]
           ,[ThanhTienSauTrietKhauThucChay]
           ,[GiaTriHoaHongThucChay]
           ,[ThanhTienThucThu]
           ,[ThanhTienKM]
           ,[SoLuongThucChayKM]
           ,[SoLuongThucChayLechTreoHa]
           ,[ThanhTienLechTreoHa]
           ,[CreatedAt]
           ,[LastModifiedAt]
           ,[IsPheDuyet]
           ,[PheDuyetBy]
           ,[PheDuyetAt]
           ,[SoLuongThayDoi]
           ,[SoLuongKMThayDoi]
           ,[GiaTriKMThayDoi]
           ,[GhiChu])
   
	SELECT  NEWID(), TD.*, 
	0 AS SoLuongThucChay,
	@NgayThucHien AS NgayThucHien,
	TD.ThanhTien as GiaTriThayDoi,
	0 AS ThanhTienThucChayTruocTrietKhau,
	0 AS GiaTriTrietKhauThucChay,
	0 AS ThanhTienSauTrietKhauThucChay,	
	0 AS GiaTriHoaHongThucChay,
	0 AS ThanhTienThucThu,
	0 as ThanhTienKM,
	0 as SoLuongThucChayKM,
	0 SoLuongLechTreoHa,
	0 ThanhTienLechTreoHa,
	GETDATE(),
	GETDATE(),
	0 IsPheDuyet,
	'' PheDuyetBy,
	'' PheDuyetAt,
	TD.SoLuong SoLuongThayDoi,
	(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then TD.SoLuong
		else 0
	  END
	) SoLuongKMThayDoi,
	(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then TD.DonGia*TD.SoLuong
		else 0
	  END
	) AS GiaTriKMThayDoi,
	@GhiChuTinhLai AS GhiChu	
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
		ISNULL(D.NhanHopDong,'') AS NhanHopDong, D.NgayNhanBanFax, D.NgayNhanHopDongBanCung, D.NgayChuyenHopDongChoKeToan, 
		D.So, D.Thang, D.Nam, 
		--Thong tin ve gia tri
		D.GiaTriHopDong, D.CongNo,
		--Thong tin chi tiet phan bo
		C.HopDongChiTietID,
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
		D.TenKhachHang, 
		ISNULL(
			tchdct.DmNhanHangREF,''
		) NhanHang,
		C.DmNhomNganhREF, 
		C.TenNhomNganh, 
		--Thong tin hinh thuc quang cao
		C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
		--Thong tin San pham
		C.DmSanPhamREF as DmSanPhamREF,
		C.TenSanPham,  
		C.DmNhomWebsiteREF, 
		C.TenNhomWebsite, 
		C.DmChuyenMucREF, 
		C.TenChuyenMuc,
		C.DmLoaiBannerREF, 
		C.TenLoaiBanner, 
		C.DmViTriREF, 
		C.TenViTri, 
		N'CPM_DonViBai' DotChayHopDong,
		0 AS SoLuongDotChayHD,		
		tchdct.ThucChayHopDongChiTietID AS DotChayBooking,
		tchdct.ThucChayHopDongChiTietID AS SoLuongDotChayBooking, 
		--Thong tin ve Tien
		C.SoLuong AS SoLuong,	
		UPPER(isnull(C.DonViTinh, N'đ/v')) AS DonViTinh, 
		C.DonGia as DonGia, 
		ISNULL(C.DonGia, 0) AS DonGiaTheoDonViTinh,
		C.ChietKhau, C.GiamGia, C.ThanhTien,
		C.TiLeTuVan,  C.ChiPhiTuVan,
		C.IsKhuyenMai,  
		C.KhuyenMai,
		tchdct.DmBannerREF DmBannerREF,
		0 DmChienDichREF,
		dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF) DmWebsiteREF,
		dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,C.TenWebsite) TenWebsite,
		0 TongViewThucChay,
		0 TongClickThucChay,
		0 TongSoBaiViet
		--,
		--C.SoLuong AS SoLuongThucChay,
		--@NgayThucHien AS NgayThucHien,
		--0 as GiaTriThayDoi,
		--C.DonGia*C.SoLuong AS ThanhTienThucChayTruocTrietKhau
		FROM 
		(
			SELECT * FROM dbo.HopDongChiTiet hdct 
				WHERE hdct.HopDongChiTietID = @HopDongChiTietREF
				AND hdct.DmSanPhamREF = @DmSanPhamREF
				AND DeletedStatus = 0 
		) C  
		INNER JOIN 
		(
			SELECT TOP (1) tchdct.ThucChayHopDongChiTietID, tchdct.HopDongREF, tchdct.HopDongChiTietREF, tchdct.DmSanPhamREF, tchdct.DmBannerREF, tchdct.DmNhanHangREF FROM dbo.ThucChayHopDongChiTiet tchdct
					WHERE tchdct.HopDongREF = @HopDongID
					AND tchdct.HopDongChiTietREF = @HopDongChiTietREF
					AND tchdct.DeletedStatus = 0
					AND tchdct.DmSanPhamREF = @DmSanPhamREF
					AND EXISTS(SELECT TOP (1) tc.SoHopDong FROM dbo.ThucChay tc 
						WHERE tc.SoHopDong = @SoHopDong
						AND tc.DmSanPhamREF = @DmSanPhamREF
						AND tc.DmBannerREF = tchdct.DmBannerREF
						ORDER BY NgayThucHien )
					ORDER BY tchdct.LastModifiedAt DESC

		)tchdct ON C.HopDongFK = tchdct.HopDongREF AND C.HopDongChiTietID = tchdct.HopDongChiTietREF
		AND	C.DmSanPhamREF = tchdct.DmSanPhamREF
		INNER JOIN  
		 ( 
	 		SELECT * FROM HopDong hd 
			WHERE hd.TrangThaiHopDong <> 3
			AND hd.DeletedStatus = 0
			AND hd.HopDongID = @HopDongID
			AND hd.NgayDanhSoHopDong >= @NgayGioiHanTinh
		 ) D on D.HopDongID = C.HopDongFK
		AND C.SoLuong >0	 
		AND C.DmWebsiteREF NOT IN (307,285) -- loai tru website Google, Facebook
	) TD	

END


```
