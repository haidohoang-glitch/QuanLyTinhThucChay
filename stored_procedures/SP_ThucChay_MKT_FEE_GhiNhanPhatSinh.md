# Stored Procedure: `ThucChay_MKT_FEE_GhiNhanPhatSinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-06-23 15:14:33.580000
- **Ngày sửa cuối**: 2025-11-01 09:30:31.617000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@NgayDanhSoGioiHan` | `datetime(8)` | No |

## Definition (Source Code)

```sql

/*
EXEC [dbo].[ThucChay_MKT_FEE_GhiNhanPhatSinh] 
	@NgayThucHien = '2025-06-17 00:00:00.000',
	@NgayDanhSoGioiHan = '2025-05-01 00:00:00.000'
*/

CREATE PROCEDURE [dbo].[ThucChay_MKT_FEE_GhiNhanPhatSinh] 
	@NgayThucHien DATETIME,
	@NgayDanhSoGioiHan DATETIME
AS
BEGIN
	DECLARE @GhiChu NVARCHAR(1000) = N'PP moi tinh thuc chay Performance Base - Marketing fee'
	SET NOCOUNT ON;

	--Tao danh muc du lieu can tinh moi
	CREATE TABLE #DmTinhMoi_MKT_FEE
	(		 HopDongID INT				
			,HopDongChiTietID INT	
			,ThanhTien_HDCT FLOAT
			,ChietKhau FLOAT
			,ThucChayID BIGINT
			,ThanhTienChay FLOAT
			,ThanhTien_DaTinh_HDCT FLOAT
			,ThanhTien_GhiNhan FLOAT
			,TrangThaiGhiNhan SMALLINT
			,NgayThucHien DATETIME
	)
	--THONG TIN HOPDONG
	INSERT INTO #DmTinhMoi_MKT_FEE
	(		 HopDongID 				
			,HopDongChiTietID 	
			,ThanhTien_HDCT 
			,ChietKhau 
			,ThucChayID 
			,ThanhTienChay 
			,ThanhTien_DaTinh_HDCT 
			,ThanhTien_GhiNhan 
			,TrangThaiGhiNhan 
			,NgayThucHien 
	)
	SELECT hd.HopDongID, hd.HopDongChiTietID
	, hd.ThanhTienHDCT, hd.ChietKhau
	, tc.ThucChayID
	, CASE WHEN hd.ChietKhau <> 100 THEN tc.ThanhTienThucChay
			 ELSE tc.ThanhTienThucChayKM
	END AS ThanhTienChay
	, 0 AS ThanhTien_DaTinh_HDCT
	, 0 AS ThanhTien_GhiNhan
	, 0 AS TrangThaiGhiNhan --0 khong ghi nhan thuc chay, 1 thuc hien ghi nhan thuc chay
	, tc.NgayThucHien 
	FROM
	(
		SELECT ISNULL(TRY_CAST(t.phanbo AS INT), 0) AS HopDongChiTietREF
		, t.ID AS ThucChayID
		, ISNULL(TRY_CAST(t.DmSanPhamREF AS INT), 0) AS DmSanPhamREF
		, ISNULL(TRY_CAST(t.balance AS float), 0) AS ThanhTienThucChay --Thanh tien thuc chay sau chiet khau va truoc VAT
		, ISNULL(TRY_CAST(t.promotion AS float), 0) AS ThanhTienThucChayKM --Thanh tien thuc chay khuyen mai va truoc VAT
		, t.NgayThucHien FROM dbo.ThucChayMarketingFee_PerformanceBaseFinal t
		WHERE t.NgayThucHien = CONVERT(DATE,@NgayThucHien)
	)tc
	INNER JOIN 
	(SELECT hd.SoHopDong, hd.HopDongID, hdct.HopDongChiTietID, 
	(CASE WHEN hdct.ChietKhau = 100 THEN hdct.DonGia*hdct.SoLuong
		ELSE  hdct.ThanhTien 
	END) AS ThanhTienHDCT , hdct.ChietKhau
	FROM dbo.HopDong hd inner join 
	dbo.HopDongChiTiet hdct on hd.HopDongID = hdct.HopDongFK
		WHERE hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan
		AND hdct.DmLoaiREF = 5038 -- N'%Performance base%'
		AND hdct.DmSanPhamREF = 817 --Marketing fee – Chi phí marketing
		AND hdct.DeletedStatus = 0
	)hd ON hd.HopDongChiTietID = tc.HopDongChiTietREF

	--XOA DU LIEU THUC CHAY NEU DA DUOC TINH NGAYTHUCHIEN
	DELETE dbo.ThucChayDaTinh
	WHERE NgayThucHien = @NgayThucHien
	AND DmHinhThucQuangCao = 5038
	AND DmSanPhamREF = 817
	AND DotChayHopDong = N'PerformanceBase_MKT'
	AND	DotChayBooking = N'TinhMoi_PerformanceBase_MKT'
	AND NgayDanhSoHopDong >= @NgayDanhSoGioiHan
	--AND EXISTS(SELECT top 1 m.HopDongChiTietID FROM #DmTinhMoi_MKT_FEE m WHERE m.HopDongChiTietID = HopDongChiTietREF)

	--CAP NHAP DU LIEU THUCCHAYDATINH
	UPDATE mkt
	SET mkt.ThanhTien_DaTinh_HDCT = ISNULL(tcdt.ThanhTien_DaTinh_HDCT, 0)
	FROM #DmTinhMoi_MKT_FEE mkt
	OUTER APPLY (SELECT ThanhTien_DaTinh_HDCT = SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi + tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi)
	             FROM dbo.ThucChayDaTinh tcdt
				 WHERE tcdt.HopDongID = mkt.HopDongID AND tcdt.HopDongChiTietREF = mkt.HopDongChiTietID 
				 AND   tcdt.NgayThucHien <= @NgayThucHien 
				) tcdt

	--THUC HIEN TINH THUC CHAY
	;WITH BaseData AS (
		SELECT 
			HopDongChiTietID,
			ThucChayID,
			ThanhTienChay,
			ThanhTien_HDCT,
			ThanhTien_DaTinh_HDCT,
			ThanhTien_GhiNhan = ThanhTien_DaTinh_HDCT + SUM(ThanhTienChay) OVER (
				PARTITION BY HopDongChiTietID
				ORDER BY ThucChayID
				ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
			)
		FROM #DmTinhMoi_MKT_FEE  -- thay bằng tên bảng thật của bạn
	),
	MarkFlag AS (
		SELECT
			*,
		 	TrangThaiGhiNhan= (CASE 
				WHEN ThanhTien_GhiNhan > ThanhTien_HDCT THEN 0
				ELSE 1
			END)
		FROM BaseData
	)
	
	--UPDATE THONG TIN SAU KHI DA DUNG WINDOW FUNTION TINH TOAN VÀ CHECK VUOT
	UPDATE mktf 
	SET mktf.TrangThaiGhiNhan = Mar.TrangThaiGhiNhan
	, mktf.ThanhTien_GhiNhan = mar.ThanhTien_GhiNhan
	, mktf.ThanhTien_DaTinh_HDCT = mar.ThanhTien_DaTinh_HDCT
	FROM #DmTinhMoi_MKT_FEE mktf INNER JOIN MarkFlag Mar ON mktf.HopDongChiTietID = Mar.HopDongChiTietID
	AND mktf.ThucChayID = Mar.ThucChayID

	--SELECT * FROM #DmTinhMoi_MKT_FEE

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
	SELECT		ThucChayDaTinhID = NEWID(),
				HopDongID = hd.HopDongID,
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
				Thang = hd.Thang,
				Nam = hd.Nam,
				GiaTriHopDong = hd.GiaTriHopDong,
				CongNo = hd.CongNo,
				HopDongChiTietREF = hdct.HopDongChiTietID,
				DangSuDung = hd.DangSuDung,
				IsGiayPhep = hd.IsGiayPhep,
				TrangThaiHopDong = 2,
				IsBanCung = hd.IsBanCung,
				DmPhongBanREF = ISNULL(hd.DmPhongBanREF,0),		
				TenPhongBan = ISNULL(HD.TenPhongBan,''),					
				DmBoPhanREF = ISNULL(HD.DmBoPhanREF,0),				
				TenBoPhan = ISNULL(HD.TenBoPhan,'')	,			
				DmNhomLamViecREF = ISNULL(HD.DmNhomLamViecREF,0),				
				TenNhomLamViec = ISNULL(HD.TenNhom,''),				
				DmDiaDiemLamViecREF = HD.DmDiaDiemLamViecREF, 				
				TenDiaDiemLamViec = ISNULL(HD.TenDiaDiemLamViec,''),				
				SysNhanVienREF = HD.SysNhanVienREF,				
				TenDangNhap = HD.TenDangNhap,				
				TenNhanVien = HD.TenNhanVien,				
				TenKhachHang = HD.TenKhachHang,		
				NhanHang = hdct.DanhSachNhanHangREF,
				DmNhomNganhREF = HDCT.DmNhomNganhREF,				
				TenNhomNganh = ISNULL(HDCT.TenNhomNganh,''),				
				DmHinhThucQuangCao = HDCT.DmLoaiREF,				
				TenHinhThucQuangCao = HDCT.TenLoai,				
				DmSanPhamREF = HDCT.DmSanPhamREF,				
				TenSanPham = HDCT.TenSanPham,				
				DmNhomWebsiteREF = HDCT.DmNhomWebsiteREF,				
				TenNhomWebsite = HDCT.TenNhomWebsite,				
				DmChuyenMucREF= HDCT.DmChuyenMucREF,			
				TenChuyenMuc = HDCT.TenChuyenMuc,			
				DmLoaiBannerREF= HDCT.DmLoaiBannerREF,				
				TenLoaiBanner = HDCT.TenLoaiBanner,					
				DmViTriREF = HDCT.DmViTriREF,						
				TenViTri  = HDCT.TenViTri,	
				DotChayHopDong = N'PerformanceBase_MKT',
				SoLuongDotChayHD = 0,
				DotChayBooking = N'TinhMoi_PerformanceBase_MKT',
				SoLuongDotChayBooking = mkt.ThucChayID,
				SoLuong = hdct.SoLuong,
				DonViTinh = hdct.DonViTinh,
				DonGia = hdct.DonGia,
				DonGiaTheoDonVi = mkt.ThanhTienChay,
				ChietKhau = hdct.ChietKhau,
				GiamGia  = HDCT.GiamGia,					
				ThanhTien  = HDCT.ThanhTien,						
				TiLeTuVan   = HDCT.TiLeTuVan,                
				ChiPhiTuVan = HDCT.ChiPhiTuVan,                       
				IsKhuyenMai = HDCT.IsKhuyenMai,                 
				KhuyenMai   = HDCT.KhuyenMai,                     
				DmBannerREF = HDCT.DmBannerREF ,
				DmChienDichREF = 0,
				DmWebsiteREF = ISNULL(w.DmWebsiteReportingdbID,826),   
				TenWebsite = ISNULL(w.WebsiteLink, N'(Blanks)'),  
				TongViewThucChay = 0,
				TongClickThucChay = 0,
				TongSoBaiViet = 0,
				SoLuongThucChay = ROUND(IIF(hdct.ChietKhau = 100, 0, 1), 0),
				NgayThucHien = @NgayThucHien,
				GiaTriThayDoi = 0,
				ThanhTienThucChayTruocTrietKhau = IIF(hdct.ChietKhau = 100, mkt.ThanhTienChay, mkt.ThanhTienChay/(1-hdct.ChietKhau/100)),
				GiaTriTrietKhauThucChay = IIF(hdct.ChietKhau = 100, 0, mkt.ThanhTienChay*hdct.ChietKhau/(100-hdct.ChietKhau)),
				ThanhTienSauTrietKhauThucChay = IIF(hdct.ChietKhau = 100, 0, mkt.ThanhTienChay),
				GiaTriHoaHongThucChay = IIF(hdct.ChietKhau = 100, 0, mkt.ThanhTienChay*hdct.TiLeTuVan/100),
				ThanhTienThucThu = IIF(hdct.ChietKhau = 100, 0, mkt.ThanhTienChay - mkt.ThanhTienChay*hdct.TiLeTuVan/100),
				ThanhTienKM = IIF(hdct.ChietKhau = 100, mkt.ThanhTienChay, 0),
				SoLuongThucChayKM = ROUND(IIF(hdct.ChietKhau = 100, 1, 0), 0),
				SoLuongThucChayLechTreoHa = 0,
				ThanhTienLechTreoHa = 0,
				CreatedAt = GETDATE(),
				LastModifiedAt = GETDATE(),
				IsPheDuyet = '',
				PheDuyetBy = '',
				PheDuyetAt = '',
				SoLuongThayDoi = 0,
				SoLuongKMThayDoi = 0,
				GiaTriKMThayDoi = 0,
				GhiChu = @GhiChu
	FROM #DmTinhMoi_MKT_FEE mkt
	INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = mkt.HopDongChiTietID
	INNER JOIN dbo.hopDong hd ON hd.HopDongID = hdct.HopDongFK
	LEFT JOIN dbo.WebsiteMapping_HDCN_Reporting w ON w.DmWebsiteID = hdct.DmWebsiteREF
	WHERE mkt.TrangThaiGhiNhan = 1 --1: TRANG THI GHI NHAN THUC CHAY, 0: VUOT GIA TRI THANHTIEN PHANBO => KHONG GHI NHAN THUC CHAY

	DROP TABLE #DmTinhMoi_MKT_FEE

END

```
