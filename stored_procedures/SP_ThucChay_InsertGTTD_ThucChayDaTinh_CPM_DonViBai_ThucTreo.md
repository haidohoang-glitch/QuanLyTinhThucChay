# Stored Procedure: `ThucChay_InsertGTTD_ThucChayDaTinh_CPM_DonViBai_ThucTreo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-07 12:44:01.647000
- **Ngày sửa cuối**: 2021-06-07 12:57:53.203000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmBannerREF` | `int(4)` | No |
| `@ThucChayHopDongChiTietREF` | `int(4)` | No |
| `@ThucChayDaTinhID_output` | `nvarchar(400)` | Yes |

## Definition (Source Code)

```sql
--EXEC [ThucChay_InsertThucChayDaTinh_CPM_DonViBai]
-------------------------------------------------------------
CREATE PROCEDURE [dbo].[ThucChay_InsertGTTD_ThucChayDaTinh_CPM_DonViBai_ThucTreo] 
	@NgayThucHien DATETIME,
	@HopDongID INT,
	@HopDongChiTietREF INT,
	@DmSanPhamREF INT,
	@DmBannerREF INT,
	@ThucChayHopDongChiTietREF INT,
	@ThucChayDaTinhID_output NVARCHAR(200) OUTPUT
AS
BEGIN

DECLARE @NgayGioiHanTinh DATETIME
	SET @NgayGioiHanTinh = '2021-01-01'
	DECLARE @Table_ouput TABLE(ThucChayDaTinhID NVARCHAR(200), HopdongID INT, HopDongChiTietID INT, ThucChayHopDongChiTietID INT, DmBannerID int)

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
   OUTPUT inserted.ThucChayDaTinhID, inserted.HopDongID, inserted.HopDongChiTietREF, inserted.DotChayBooking, inserted.DmBannerREF INTO @Table_ouput
	SELECT  NEWID(), TD.*, 
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
	(CASE when ((TD.IsKhuyenMai=0) OR (TD.ChietKhau <> 100)) then 1
		else 0
	  END
	) SoLuongThayDoi,
	(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then 1
		else 0
	  END
	) SoLuongKMThayDoi,
	(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then TD.DonGia
		else 0
	  END
	) GiaTriKMThayDoi,
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
		(SELECT TOP (1) isnull(tchdct.DmNhanHangREF,0) FROM ThucChayHopDongChiTiet tchdct
		WHERE tchdct.HopDongREF = @HopDongID
		AND tchdct.HopDongChiTietREF = @HopDongChiTietREF
		AND tchdct.DmSanPhamREF = @DmSanPhamREF
		AND tchdct.DmBannerREF = @DmBannerREF
		AND tchdct.DeletedStatus = 0),0
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
	@ThucChayHopDongChiTietREF AS DotChayBooking,
	@ThucChayHopDongChiTietREF AS SoLuongDotChayBooking, 
	--Thong tin ve Tien
	C.SoLuong AS SoLuong,	
	UPPER(isnull(C.DonViTinh, N'đ/v')) AS DonViTinh, 
	C.DonGia as DonGia, 
	C.DonGia AS DonGiaTheoDonViTinh,
	C.ChietKhau, C.GiamGia, C.ThanhTien,
	C.TiLeTuVan,  C.ChiPhiTuVan,
	C.IsKhuyenMai,  
	C.KhuyenMai,
	@DmBannerREF DmBannerREF,
	0 DmChienDichREF,
	dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF) DmWebsiteREF,
	dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,C.TenWebsite) TenWebsite,
	0 TongViewThucChay,
	0 TongClickThucChay,
	0 TongSoBaiViet,
	0 AS SoLuongThucChay, --MOI BANNER TINH LA 1 DV SO LUONG
	@NgayThucHien AS NgayThucHien,
	(CASE when ((c.IsKhuyenMai=0) OR (c.ChietKhau <> 100)) then ISNULL(C.DonGia*(100-C.ChietKhau)/100,0)
		else 0
	  END
	) as GiaTriThayDoi,
	0 AS ThanhTienThucChayTruocTrietKhau
	FROM 
	(
		SELECT * FROM dbo.HopDongChiTiet hdct 
			WHERE hdct.HopDongChiTietID = @HopDongChiTietREF
			AND DeletedStatus = 0 
	) C  
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

	SET @ThucChayDaTinhID_output = ISNULL((SELECT TOP (1) ThucChayDaTinhID FROM @Table_ouput),'')
END
```
