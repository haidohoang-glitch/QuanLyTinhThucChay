# Stored Procedure: `ThucChay_MKT_FEE_GhiNhanThayDoi_bk20251016`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-10-16 11:15:54.673000
- **Ngày sửa cuối**: 2025-10-16 11:15:54.673000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@NgayDanhSoGioiHan` | `datetime(8)` | No |

## Definition (Source Code)

```sql

/*
EXEC [dbo].[ThucChay_MKT_FEE_GhiNhanThayDoi]
	@NgayThucHien = '2025-06-22 00:00:00.000',
	@NgayDanhSoGioiHan = '2020-05-01 00:00:00.000'
*/

create PROCEDURE [dbo].[ThucChay_MKT_FEE_GhiNhanThayDoi_bk20251016] 
	@NgayThucHien DATETIME,
	@NgayDanhSoGioiHan DATETIME
AS
BEGIN
	DECLARE @GhiChu NVARCHAR(1000) = N'PP_M doi tru thuc chay thay doi PB-Marketing fee'

	SET NOCOUNT ON;
	--Tao danh muc du lieu can check thay doi gia tri thanhtien HopDongChiTiet
	CREATE TABLE #DsHDCT_MKT_FEE_TD
	(		 HopDongID INT				
			,HopDongChiTietID INT	
			,ThanhTien_HDCT FLOAT
			,ChietKhau FLOAT
			,NgayThucHien DATETIME
	)

	CREATE TABLE #DsTCDT_MKT_FEE
	(		 HopDongID INT				
			,HopDongChiTietID INT	
			,ThanhTien_HDCT FLOAT
			,ChietKhau FLOAT
			,ThanhTien_DaTinh_HDCT FLOAT
			,TrangThaiGhiNhan SMALLINT
			,NgayThucHien DATETIME
			,RowNumberTCDT int
			,NgayThucHienTCDT DATETIME
			,ThucChayDaTinhID NVARCHAR(100)
			,ThanhTienGhiNhanTCDT FLOAT
	)

	--XOA CAC BAN GHI PHAT SINH GIA TRI THAY DOI NGAYTHUCHIEN
	DELETE dbo.ThucChayDaTinh 
	WHERE NgayThucHien = @NgayThucHien
	AND DmHinhThucQuangCao = 5038
	AND DmSanPhamREF = 817
	AND DotChayHopDong = N'PerformanceBase_MKT' --Nhung ban ghi doi tru khi ghi nhan giam gia tri thanh tien
	AND DotChayBooking = N'TinhTD_PerformanceBase_MKT'
	AND NgayDanhSoHopDong >= @NgayDanhSoGioiHan

	;WITH LastHopdongchitietLog AS (
    SELECT 
        HopDongChiTietREF,
        Thoigianlog,
        ThanhTien AS ThanhTien_Log,
		SoLuong*DonGia AS ThanhTienTruocCK_log,
        ROW_NUMBER() OVER (
            PARTITION BY HopDongChiTietREF
            ORDER BY Thoigianlog DESC
        ) AS RN
    FROM HopDongChiTietLog
	WHERE DmLoaiREF = 5038 -- N'%Performance base%'
	AND DmSanPhamREF = 817 --Marketing fee – Chi phí marketing 
	AND CAST(ThoiGianLog AS DATE) < @NgayThucHien
	
	)

	--XAC DINH HOPDONGCHITIET CO THAY DOI THANHTIEN/THANHTIENTRUOCCK
	INSERT INTO #DsHDCT_MKT_FEE_TD
	(		 HopDongID 				
			,HopDongChiTietID 	
			,ThanhTien_HDCT 
			,ChietKhau 
			,NgayThucHien 
	)
	SELECT hd.HopDongID,
		h.HopDongChiTietID,
		(CASE WHEN h.ChietKhau = 100 THEN h.DonGia*h.SoLuong
			ELSE  h.ThanhTien 
		END) AS ThanhTien_HienTai,
		h.ChietKhau,
		@NgayThucHien
	FROM 
	(SELECT * FROM HopDongChiTiet h
		WHERE 1=1 
		AND h.DmLoaiREF = 5038 -- N'%Performance base%'
		AND h.DmSanPhamREF = 817 --Marketing fee – Chi phí marketing
		AND h.DeletedStatus = 0
		AND CAST(h.LastModifiedAt AS DATE) = @NgayThucHien
	)h
	INNER JOIN (
		SELECT HopDongChiTietREF, ThanhTien_Log, ThanhTienTruocCK_log
		FROM LastHopdongchitietLog
		WHERE RN = 1
	) l	ON h.HopDongChiTietID = l.HopDongChiTietREF
	INNER JOIN HopDong hd ON hd.HopDongID = h.HopDongFK
	WHERE 1=1 
		AND h.DmLoaiREF = 5038 -- N'%Performance base%'
		AND h.DmSanPhamREF = 817 --Marketing fee – Chi phí marketing
		AND ((h.ThanhTien <> l.ThanhTien_Log) OR (h.DonGia*h.SoLuong <> l.ThanhTienTruocCK_log)) --Check co su thay doi ve tien ko
		AND h.DeletedStatus = 0
		AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan
		AND CAST(h.LastModifiedAt AS DATE) = @NgayThucHien


	--select * from #DsHDCT_MKT_FEE_TD
	--INSERT DU LIEU THUC CHAY DA DUOC TINH CAC NGAY TRUOC DAY
	INSERT INTO #DsTCDT_MKT_FEE
	(		 HopDongID 				
			,HopDongChiTietID 	
			,ThanhTien_HDCT 
			,ChietKhau 
			,ThanhTien_DaTinh_HDCT 
			,TrangThaiGhiNhan 
			,NgayThucHien 
			,RowNumberTCDT 
			,NgayThucHienTCDT 
			,ThucChayDaTinhID 
			,ThanhTienGhiNhanTCDT
	)
	SELECT mkt.HopDongID
	, mkt.HopDongChiTietID
	, mkt.ThanhTien_HDCT
	, mkt.ChietKhau
	, ISNULL(tcdt.ThanhTienThucChay,0)
	, 0 AS TrangThiGhiNhan
	, mkt.NgayThucHien --Ngay ghi nhan thay doi
	, tcdt.RN
	, tcdt.NgayThucHien --
	, tcdt.ThucChayDaTinhID
	, 0 AS ThanhTienGhiNhanTCDT
	FROM #DsHDCT_MKT_FEE_TD mkt 
	OUTER APPLY (SELECT (tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi + tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) AS ThanhTienThucChay
				,  ROW_NUMBER() OVER (
						PARTITION BY HopDongChiTietREF
						ORDER BY tcdt.NgayThucHien, tcdt.ThucChayDaTinhID, tcdt.SoLuongDotChayBooking  DESC
					) AS RN
					, tcdt.ThucChayDaTinhID
					, tcdt.NgayThucHien
					FROM dbo.ThucChayDaTinh tcdt 
					WHERE tcdt.HopDongID = mkt.HopDongID AND tcdt.HopDongChiTietREF = mkt.HopDongChiTietID
					AND tcdt.NgayThucHien <= @NgayThucHien) tcdt


	--SELECT * FROM #DsTCDT_MKT_FEE

	/*	RULE:
		NEU CO SU THAY DOI THANHTIEN MA ThanhTien_DaTinh_HDCT < THANHTIEN 
		=> THUC HIEN DOI TRU PHAN VUOT THEO tcdt.NgayThucHien, tcdt.ThucChayDaTinhID, tcdt.SoLuongDotChayBooking
	*/
	;WITH BaseDataCRT AS (
		SELECT t.HopDongID ,
		 t.HopDongChiTietID ,
		 t.ThanhTien_HDCT ,
		 t.ThanhTien_DaTinh_HDCT ,
		 t.RowNumberTCDT ,
		 t.ThucChayDaTinhID ,
		 SUM(t.ThanhTien_DaTinh_HDCT) OVER( PARTITION BY t.HopDongChiTietID
			ORDER BY t.RowNumberTCDT, t.ThucChayDaTinhID
			ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)ThucChayDaTinhTichLuy
		FROM #DsTCDT_MKT_FEE t
	),
	MarkFlag AS(
		SELECT * 
		, (CASE WHEN m.ThucChayDaTinhTichLuy > m.ThanhTien_HDCT THEN 0
			ELSE 1
			END
		)TrangThaiGhiNhan
		FROM BaseDataCRT m
	)
	
	--SELECT * FROM MarkFlag

	UPDATE tc
	SET tc.ThanhTienGhiNhanTCDT = m.ThucChayDaTinhTichLuy
	, tc.TrangThaiGhiNhan = m.TrangThaiGhiNhan
	FROM #DsTCDT_MKT_FEE tc
	INNER JOIN MarkFlag m ON TC.HopDongID = m.HopDongID AND tc.HopDongChiTietID = m.HopDongChiTietID
	AND tc.RowNumberTCDT = m.RowNumberTCDT



	--SELECT * FROM #DsTCDT_MKT_FEE 

	--THUC HIEN DOI TRU NHUNG BAN GHI CO RowNumberTCDT = 0 => VUOT GIA TRI THANH TIEN HDCT

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
				HopDongID = tcdt.HopDongID,
				SoHopDong = tcdt.SoHopDong,
				DmMaHopDongREF = tcdt.DmMaHopDongREF,
				TenMaHopDong = tcdt.TenMaHopDong,
				NgayDanhSoHopDong = tcdt.NgayDanhSoHopDong,
				NgayKyHopDong = tcdt.NgayKyHopDong,
				NhanHopDong = tcdt.NhanHopDong,
				NgayNhanBanFax = tcdt.NgayNhanBanFax,
				NgayNhanHopDongBanCung = tcdt.NgayNhanHopDongBanCung,
				NgayChuyenHopDongChoKeToan = tcdt.NgayChuyenHopDongChoKeToan,
				So = tcdt.So,
				Thang = tcdt.Thang,
				Nam = tcdt.Nam,
				GiaTriHopDong = tcdt.GiaTriHopDong,
				CongNo = tcdt.CongNo,
				HopDongChiTietREF = tcdt.HopDongChiTietREF,
				DangSuDung = tcdt.DangSuDung,
				IsGiayPhep = tcdt.IsGiayPhep,
				TrangThaiHopDong = 2,
				IsBanCung = tcdt.IsBanCung,
				DmPhongBanREF = ISNULL(tcdt.DmPhongBanREF,0),		
				TenPhongBan = ISNULL(tcdt.TenPhongBan,''),					
				DmBoPhanREF = ISNULL(tcdt.DmBoPhanREF,0),				
				TenBoPhan = ISNULL(tcdt.TenBoPhan,'')	,			
				DmNhomLamViecREF = ISNULL(tcdt.DmNhomLamViecREF,0),				
				TenNhomLamViec = ISNULL(tcdt.TenNhomLamViec,''),				
				DmDiaDiemLamViecREF = tcdt.DmDiaDiemLamViecREF, 				
				TenDiaDiemLamViec = ISNULL(tcdt.TenDiaDiemLamViec,''),				
				SysNhanVienREF = tcdt.SysNhanVienREF,				
				TenDangNhap = tcdt.TenDangNhap,				
				TenNhanVien = tcdt.TenNhanVien,				
				TenKhachHang = tcdt.TenKhachHang,		
				NhanHang = tcdt.NhanHang,
				DmNhomNganhREF = tcdt.DmNhomNganhREF,				
				TenNhomNganh = ISNULL(tcdt.TenNhomNganh,''),				
				DmHinhThucQuangCao = tcdt.DmHinhThucQuangCao,				
				TenHinhThucQuangCao = tcdt.TenHinhThucQuangCao,				
				DmSanPhamREF = tcdt.DmSanPhamREF,				
				TenSanPham = tcdt.TenSanPham,				
				DmNhomWebsiteREF = tcdt.DmNhomWebsiteREF,				
				TenNhomWebsite = tcdt.TenNhomWebsite,				
				DmChuyenMucREF= tcdt.DmChuyenMucREF,			
				TenChuyenMuc = tcdt.TenChuyenMuc,			
				DmLoaiBannerREF= tcdt.DmLoaiBannerREF,				
				TenLoaiBanner = tcdt.TenLoaiBanner,					
				DmViTriREF = tcdt.DmViTriREF,						
				TenViTri  = tcdt.TenViTri,	
				DotChayHopDong = DotChayHopDong,
				SoLuongDotChayHD = 0,
				DotChayBooking = N'TinhTD_PerformanceBase_MKT',
				SoLuongDotChayBooking = tcdt.SoLuongDotChayBooking,
				SoLuong = tcdt.SoLuong,
				DonViTinh = tcdt.DonViTinh,
				DonGia = tcdt.DonGia,
				DonGiaTheoDonVi = tcdt.DonGiaTheoDonVi,
				ChietKhau = tcdt.ChietKhau,
				GiamGia  = tcdt.GiamGia,					
				ThanhTien  = tcdt.ThanhTien,						
				TiLeTuVan   = tcdt.TiLeTuVan,                
				ChiPhiTuVan = tcdt.ChiPhiTuVan,                       
				IsKhuyenMai = tcdt.IsKhuyenMai,                 
				KhuyenMai   = tcdt.KhuyenMai,                     
				DmBannerREF = tcdt.DmBannerREF ,
				DmChienDichREF = 0,
				DmWebsiteREF = tcdt.DmWebsiteREF,   
				TenWebsite = tcdt.TenWebsite,  
				TongViewThucChay = 0,
				TongClickThucChay = 0,
				TongSoBaiViet = 0,
				SoLuongThucChay = 0,
				NgayThucHien = @NgayThucHien,
				GiaTriThayDoi = -IIF(tcdt.ChietKhau = 100, 0, tcdt.ThanhTienSauTrietKhauThucChay),
				ThanhTienThucChayTruocTrietKhau = 0,
				GiaTriTrietKhauThucChay = -IIF(tcdt.ChietKhau = 100, 0, tcdt.GiaTriTrietKhauThucChay),
				ThanhTienSauTrietKhauThucChay = 0,
				GiaTriHoaHongThucChay = 0,
				ThanhTienThucThu = -IIF(tcdt.ChietKhau = 100, 0, tcdt.ThanhTienThucThu),
				ThanhTienKM = 0,
				SoLuongThucChayKM = 0,
				SoLuongThucChayLechTreoHa = 0,
				ThanhTienLechTreoHa = 0,
				CreatedAt = GETDATE(),
				LastModifiedAt = GETDATE(),
				IsPheDuyet = '',
				PheDuyetBy = '',
				PheDuyetAt = '',
				SoLuongThayDoi = -tcdt.SoLuongThucChay,
				SoLuongKMThayDoi = -tcdt.SoLuongThucChayKM,
				GiaTriKMThayDoi = -tcdt.ThanhTienKM,
				GhiChu = @GhiChu + '; ThucChayDaTinhID = ' + tcdt.ThucChayDaTinhID
	FROM dbo.ThucChayDaTinh tcdt
	WHERE tcdt.ThucChayDaTinhID IN (SELECT mkt.ThucChayDaTinhID FROM #DsTCDT_MKT_FEE mkt WHERE mkt.TrangThaiGhiNhan = 0) --DOI TRU NHUNG BAN GHI VUOT GIA TRI THANH TIEN
	
	DROP TABLE #DsHDCT_MKT_FEE_TD
	DROP TABLE #DsTCDT_MKT_FEE
END

```
