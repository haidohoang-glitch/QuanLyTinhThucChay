# Stored Procedure: `ThucChayDaTinhAdmarket_UpdateThucChayByCongNo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-13 10:31:40.250000
- **Ngày sửa cuối**: 2014-10-14 10:39:49.453000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--
-- EXEC dbo.ThucChayDaTinhAdmarket_UpdateThucChayByCongNo 144

CREATE PROCEDURE [dbo].[ThucChayDaTinhAdmarket_UpdateThucChayByCongNo]
	-- Add the parameters for the stored procedure here
	--@DmSanPhamREF INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @HopDongID			INT,
			@SoHopDong			NVARCHAR(50),
			@GiaTriHopDong		FLOAT,
			@HopDongChiTietID	INT,
			@SoLuongPhanBo		INT,
			@ThanhTienPhanBo	FLOAT,
			@DonViTinhPhanBo	NVARCHAR(50),
			@IsKhuyenMai		INT,
			@DmSanPhamREF		INT,
			@TenSanPham			NVARCHAR(50),
			@TenWebsite			NVARCHAR(50),
			@DonGiaPhanBo		FLOAT		
	
	DECLARE @NgayThanhToan		DATETIME,
			@GiaTriThanhToan	FLOAT
			
	DECLARE @TongGiaTriHopDong	FLOAT,
			@TyLeTheoPhanBo		FLOAT,
			@TongTyLe			FLOAT,
			@TongGiaTriTheoPB	FLOAT,
			@ThanhTienTheoTyLe	FLOAT
			
	SET @TongTyLe = 0;
	SET @TongGiaTriTheoPB = 0;
			
	DECLARE record_cursor CURSOR FOR
	SELECT DISTINCT
		A.HopDongID, A.SoHopDong, A.GiaTriHopDong,
		B.HopDongChiTietID, B.DmSanPhamREF, B.TenSanPham, B.SoLuong, B.DonGia, B.ThanhTien,
		A.GiaTriThanhToan, A.NgayThanhToan
	FROM
	(
		SELECT 
			hd.HopDongID, hd.SoHopDong, hd.GiaTriHopDong, 
			(SELECT SUM(GiaTriThanhToan) FROM CongNo AS cn WHERE cn.HopDongREF = hd.HopDongID) AS GiaTriThanhToan,
			(SELECT MAX(NgayThanhToan) FROM CongNo AS cn WHERE cn.HopDongREF = hd.HopdongID) AS NgayThanhToan
		FROM HopDong AS hd
			INNER JOIN HopDongChiTiet AS hdct ON hdct.HopDongFK = hd.HopDongID
		WHERE hdct.DmSanPhamREF IN (144,299,337)
			AND hd.NgayDanhSoHopDong >= '2013-01-01'	
			AND hdct.IsKhuyenMai <> 1
			AND (hdct.TK_AdMarket = '' OR hdct.TK_AdMarket IS NULL)
			--AND hd.HopDongID = 25645
	)A INNER JOIN HopDongChiTiet B ON B.HopDongFK = A.HopDongID
	WHERE A.GiaTriHopDong > A.GiaTriThanhToan
		AND B.IsKhuyenMai <> 1
		AND A.NgayThanhToan IS NOT NULL
		AND A.NgayThanhToan >= '2014-01-01'
	ORDER BY A.NgayThanhToan
		
	OPEN record_cursor
	
	FETCH NEXT FROM record_cursor INTO @HopDongID, @SoHopDong, @GiaTriHopDong, @HopDongChiTietID, @DmSanPhamREF, @TenSanPham, 
										@SoLuongPhanBo, @DonGiaPhanBo, @ThanhTienPhanBo,
										@GiaTriThanhToan, @NgayThanhToan
	WHILE @@FETCH_STATUS = 0
	BEGIN		
		SELECT @TongGiaTriHopDong = SUM(ThanhTien)
		FROM HopDongChiTiet AS hdct
		WHERE hdct.HopDongFK = @HopDongID
			AND hdct.IsKhuyenMai <> 1
			AND hdct.DeletedStatus = 0
			
		--PRINT '@TongGiaTriHopDong: ' + CONVERT(NVARCHAR(50), @TongGiaTriHopDong)	
		--PRINT '@Tyle Phan bo ' + CONVERT(NVARCHAR(50), @HopDongChiTietID) + ': ' + CONVERT(NVARCHAR(50), @TyLeTheoPhanBo)
		
		SELECT @TongTyLe += @TyLeTheoPhanBo
		SET @TongGiaTriTheoPB += @ThanhTienPhanBo;
		
		--PRINT '@TongTyLe: ' + CONVERT(NVARCHAR(50), @TongTyLe);
		--PRINT '@TongTien: ' + CONVERT(NVARCHAR(50), @TongGiaTriTheoPB)
		
		IF (@DmSanPhamREF = 144 OR @DmSanPhamREF = 299 OR @DmSanPhamREF = 337)
		BEGIN
			SET @TyLeTheoPhanBo = ((@ThanhTienPhanBo * 100)/@TongGiaTriHopDong);
			SET @ThanhTienTheoTyLe = ((@TyLeTheoPhanBo*(@GiaTriThanhToan/1.1))/100);
			
			PRINT '@TyLeTheoPhanBo: ' + CONVERT(NVARCHAR(50), @TyLeTheoPhanBo);
			PRINT '@GiaTriThanhToan: ' + CONVERT(NVARCHAR(50), @GiaTriThanhToan);
			PRINT '@ThanhTienTheoTyLe: ' + CONVERT(NVARCHAR(50), @ThanhTienTheoTyLe);
			
			INSERT INTO ThucChayDaTinhAdmarket                      
			SELECT DISTINCT
				NEWID() ThucChayDaTinhID,
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
				C.HopDongChiTietID AS HopDongChiTietREF,
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
				'' NhanHang, 
				'' DmNhomNganhREF, 
				'' TenNhomNganh, 
				--Thong tin hinh thuc quang cao
				C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
				--Thong tin San pham
				@DmSanPhamREF as DmSanPhamREF,
				@TenSanPham as TenSanPham,  
				C.DmNhomWebsiteREF DmNhomWebsiteREF, 
				C.TenNhomWebsite TenNhomWebsite, 
				--C.DmWebsiteREF, 
				--C.TenWebsite, 
				C.DmChuyenMucREF DmChuyenMucREF, 
				C.TenChuyenMuc TenChuyenMuc, 
				C.DmLoaiBannerREF DmLoaiBannerREF, 
				C.TenLoaiBanner TenLoaiBanner, 
				C.DmViTriREF DmViTriREF, 
				C.TenViTri TenViTri, 
				N'ThucChay_By_CongNo' AS DotChayHopDong,
				C.SoLuong AS SoLuongDotChayHD,
				N'Update thuc chay theo cong no hop dong' AS DotChayBooking,
				dbo.GetSoLuongDotChayBookingByHopDongChiTiet(C.HopDongChiTietID) SoLuongDotChayBooking, 
				--Thong tin ve Tien
				--****haidh chinh sua
				C.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong,
				--****haidh chinh sua
				CASE @DmSanPhamREF 
					WHEN 337 THEN N'VIEW'
					ELSE N'CLICK'
				END DonViTinh, 
				--dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,C.HopDongChiTietID,C.DonGia) as DonGia,
				dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThanhToan,@HopDongChiTietID,C.DonGia) AS DonGia,
				--****haidh chinh sua 
				ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong, @NgayThanhToan, C.HopDongChiTietID),0),
				C.ChietKhau, C.GiamGia, C.ThanhTien,
				C.TiLeTuVan,  C.ChiPhiTuVan,
				C.IsKhuyenMai,  
				C.KhuyenMai,
				--Thuc chay
				0 DmBannerREF,--A.DmBannerREF,
				0 DmChienDichREF,--A.DmChienDichREF,
				0 DmWebsiteREF,
				'' AS TenWebsite,
				0 TongViewThucChay,
				0 TongClickThucChay,
				0 TongSoBaiViet,
				@SoLuongPhanBo as SoLuongThucChay,
				--Thanhuc Tien Thuc Chay
				@NgayThanhToan NgayThucHien,
				0 as GiaTriThayDoi,
				0 as ThanhTienThucChayTruocTrietKhau,
				0 GiaTriTrietKhauThucChay,
				@ThanhTienTheoTyLe ThanhTienSauTrietKhauThucChay,
				0 AS GiaTriHoaHongThucChay,
				@ThanhTienTheoTyLe AS ThanhTienThucThu,
				0 as ThanhTienKM,
				0 as SoLuongThucChayKM,
				0 AS SoLuongLechTreoHa,
				0 AS ThanhTienLechTreoHa,
				GETDATE(),
				GETDATE(),
				0 IsPheDuyet,
				'' PheDuyetBy,
				'' PheDuyetAt 
			FROM
				HopDong AS D 
					INNER JOIN HopDongChiTiet C ON C.HopDongFK = D.HopDongID
			WHERE D.TrangThaiHopDong <> 3
				AND C.HopDongChiTietID = @HopDongCHiTietID
				AND D.SoHopDong = @SoHopDong
		END
		
		
		
		
		
		--INSERT INTO ThucChayDaTinhAdmarket	
		--SELECT  NEWID(), TD.*, 
		--	0 AS GiaTriTrietKhauThucChay,
		--	CASE WHEN @IsKhuyenMai = 0 THEN @ThanhTienPhanBo
		--		ELSE 0
		--	END AS ThanhTienSauTrietKhauThucChay,
		--	0 AS GiaTriHoaHongThucChay,
		--	@ThanhTienPhanBo AS ThanhTienThucThu,
		--	CASE WHEN @IsKhuyenMai = 1 THEN (@SoLuongPhanBo*@DonGiaPhanBo)
		--		ELSE 0
		--	END as ThanhTienKM,
		--	CASE WHEN @IsKhuyenMai = 1 THEN @SoLuongPhanBo
		--		ELSE 0
		--	END as SoLuongThucChayKM,
		--	0 AS SoLuongLechTreoHa,
		--	0 AS ThanhTienLechTreoHa,
		--	GETDATE(),
		--	GETDATE(),
		--	0 IsPheDuyet,
		--	'' PheDuyetBy,
		--	'' PheDuyetAt	
		--FROM
		--(			                       
		--	SELECT distinct
		--		--ID Hop Dong
		--		D.HopDongID,
		--		--Thong tin ve ma so 
		--		D.SoHopDong, 
		--		D.DmMaHopDongREF, 
		--		D.TenMaHopDong, 
		--		--Thong tin ve thoi gian
		--		D.NgayDanhSoHopDong, D.NgayKyHopDong, 
		--		D.NhanHopDong, D.NgayNhanBanFax, D.NgayNhanHopDongBanCung, D.NgayChuyenHopDongChoKeToan, 
		--		D.So, D.Thang, D.Nam, 
		--		--Thong tin ve gia tri
		--		D.GiaTriHopDong, D.CongNo,
		--		--Thong tin chi tiet phan bo
		--		C.HopDongChiTietID AS HopDongChiTietREF,
		--		--Thong tin ve trang thai
		--		D.DangSuDung, D.IsGiayPhep, D.TrangThaiHopDong,D.IsBanCung, 
		--		--Thong tin ve Nhan vien kinh doanh
		--		D.DmPhongBanREF, 
		--		ISNULL(D.TenPhongBan, '') AS TenPhongBan, 
		--		D.DmBoPhanREF, 
		--		ISNULL(D.TenBoPhan,'') AS TenBoPhan, 
		--		D.DmNhomLamViecREF, 
		--		ISNULL(D.TenNhom, '') AS TenNhom, 
		--		D.DmDiaDiemLamViecREF, 
		--		D.TenDiaDiemLamViec, 
		--		D.SysNhanVienREF, 
		--		ISNULL(D.TenDangNhap, '') AS TenDangNhap,  
		--		D.TenNhanVien, 
		--		--Thong tin ve khach hang
		--		--D.DmKhachHangREF, 
		--		D.TenKhachHang, 
		--		C.NhanHang, 
		--		C.DmNhomNganhREF, 
		--		C.TenNhomNganh, 
		--		--Thong tin hinh thuc quang cao
		--		C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
		--		--Thong tin San pham
		--		@DmSanPhamREF as DmSanPhamREF,
		--		@TenSanPham as TenSanPham,  
		--		C.DmNhomWebsiteREF, 
		--		C.TenNhomWebsite, 
		--		--C.DmWebsiteREF, 
		--		--C.TenWebsite, 
		--		C.DmChuyenMucREF, 
		--		C.TenChuyenMuc, 
		--		C.DmLoaiBannerREF, 
		--		C.TenLoaiBanner, 
		--		C.DmViTriREF, 
		--		C.TenViTri, 
		--		--ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'Y'),'') DotChayHopDong,
		--		N'ThucChay_By_CongNo' DotChayHopDong,
		--		C.SoLuong AS SoLuongDotChayHD,
		--		--ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'N'),0) DotChayBooking,
		--		N'Update thuc chay theo cong no hop dong' DotChayBooking,
		--		dbo.GetSoLuongDotChayBookingByHopDongChiTiet(C.HopDongChiTietID) SoLuongDotChayBooking, 
		--		--Thong tin ve Tien
		--		--****haidh chinh sua
		--		C.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong,
		--		--****haidh chinh sua
		--		--dbo.ThucChay_GetDonViTinhNotCPD(C.DonViTinh) as DonViTinh, 
		--		CASE C.DmSanPhamREF
		--			WHEN 337 THEN 'VIEW'
		--			ELSE 'CLICK'
		--		END DonViTinh,
		--		--'VIEW' DonViTinh, 
		--		--dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,C.HopDongChiTietID,C.DonGia) as DonGia,
		--		dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThanhToan,@HopDongChiTietID,C.DonGia) AS DonGia,
		--		--****haidh chinh sua 
		--		ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong, @NgayTHanhToan, C.HopDongChiTietID),0)  AS DonGiaTheoDonViTinh,
		--		C.ChietKhau, C.GiamGia, C.ThanhTien,
		--		C.TiLeTuVan,  C.ChiPhiTuVan,
		--		C.IsKhuyenMai,  
		--		C.KhuyenMai,
		--		--Thuc chay
		--		0 DmBannerREF,--A.DmBannerREF,
		--		0 DmChienDichREF,--A.DmChienDichREF,
		--		(SELECT TOP 1 DmWebsiteReportingdbID FROM DmWebsiteReportingdb WHERE DmWebsiteReportingdb.TenWebsite = @TenWebsite) DmWebsiteREF,
		--		@TenWebsite AS TenWebsite,
		--		0 TongViewThucChay,
		--		0 TongClickThucChay,
		--		0 TongSoBaiViet,
		--		CASE WHEN @IsKhuyenMai = 0 THEN @SoLuongPhanBo
		--			ELSE 0
		--		END as SoLuongThucChay,
		--		--Thanhuc Tien Thuc Chay
		--		@NgayThanhToan NgayThucHien,
		--		0 as GiaTriThayDoi,
		--		0 as ThanhTienThucChayTruocTrietKhau 
		--	FROM
		--		HopDong AS D 
		--		INNER JOIN HopDongChiTiet C ON C.HopDongFK = D.HopDongID
		--	WHERE D.TrangThaiHopDong <> 3
		--		AND C.HopDongChiTietID = @HopDongChiTietID
		--		AND C.DmSanPhamREF = @DmSanPhamREF
		--		AND C.DeletedStatus = 0
		--)TD
	
		FETCH NEXT FROM record_cursor INTO @HopDongID, @SoHopDong, @GiaTriHopDong, @HopDongChiTietID, @DmSanPhamREF, @TenSanPham, 
										@SoLuongPhanBo, @DonGiaPhanBo, @ThanhTienPhanBo,
										@GiaTriThanhToan, @NgayThanhToan
	END
	
	CLOSE record_cursor;
	DEALLOCATE record_cursor;
END

```
