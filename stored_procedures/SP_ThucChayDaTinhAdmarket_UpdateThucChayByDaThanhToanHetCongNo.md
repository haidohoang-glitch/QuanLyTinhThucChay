# Stored Procedure: `ThucChayDaTinhAdmarket_UpdateThucChayByDaThanhToanHetCongNo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-14 12:00:12.593000
- **Ngày sửa cuối**: 2014-10-14 10:39:49.433000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--
-- EXEC dbo.ThucChayDaTinhAdmarket_UpdateThucChayByDaThanhToanHetCongNo 144

CREATE PROCEDURE [dbo].[ThucChayDaTinhAdmarket_UpdateThucChayByDaThanhToanHetCongNo]
	-- Add the parameters for the stored procedure here
	@DmSanPhamREF INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @HopDongID			INT,
			@SoHopDong			NVARCHAR(50),
			@GiaTriHopDong		FLOAT,
			@NgayThanhToan		DATETIME,
			@HopDongChiTietID	INT,
			@SoLuongPhanBo		INT,
			@ThanhTienPhanBo	FLOAT,
			@DonViTinhPhanBo	NVARCHAR(50),
			@IsKhuyenMai		INT,
			@TenSanPham			NVARCHAR(50),
			@TenWebsite			NVARCHAR(50),
			@DonGiaPhanBo		FLOAT
			
	DECLARE record_cursor CURSOR FOR
	SELECT 
		A.HopDongID, A.SoHopDong, A.GiaTriHopDong
		--, A.GiaTriThanhToan
		, NgayThanhToan, B.HopDongChiTietID, B.SoLuong, B.DonViTinh, B.ThanhTien, B.IsKhuyenMai,
		B.TenSanPham, B.TenWebsite, B.DonGia
	FROM
	(
		SELECT HopDongID, hd.SoHopDong,
			hd.GiaTriHopDong, SUM(cn.GiaTriThanhToan) GiaTriThanhToan, MAX(cn.NgayThanhToan) NgayThanhToan
		FROM HopDong AS hd 
			INNER JOIN HopDongChiTiet AS hdct ON hd.HopDongID = hdct.HopDongFK
			INNER JOIN CongNo AS cn ON cn.HopDongREF = hd.HopDongID
		WHERE
			hd.TrangThaiHopDong <> 3
			AND hdct.DeletedStatus = 0
			AND hdct.DmSanPhamREF = @DmSanPhamREF
			AND hd.NgayDanhSoHopDong >= '2013-01-01'
		GROUP BY
			HopDongID, hd.SoHopDong, hd.GiaTriHopDong
	)A
	INNER JOIN HopDongChiTiet AS B ON B.HopDongFK = A.HopDongID
	WHERE
		B.DmSanPhamREF = @DmSanPhamREF
		AND A.GiaTriThanhToan >= A.GiaTriHopDong
		AND (B.TK_AdMarket = '' OR B.TK_AdMarket IS NULL)
		AND A.NgayThanhToan >= '2014-01-01'
		--AND A.SoHopDong = 'CPC020113'
	ORDER BY 
		A.HopDongID
		
	OPEN record_cursor
	
	FETCH NEXT FROM record_cursor INTO @HopDongID, @SoHopDong, @GiaTriHopDong, @NgayThanhToan, @HopDongChiTietID, @SoLuongPhanBo, @DonViTinhPhanBo, @ThanhTienPhanBo 
					,@IsKhuyenMai, @TenSanPham, @TenWebsite, @DonGiaPhanBo
	
	WHILE @@FETCH_STATUS = 0
	BEGIN		
		INSERT INTO ThucChayDaTinhAdmarket	
		SELECT  NEWID(), TD.*, 
			0 AS GiaTriTrietKhauThucChay,
			CASE WHEN @IsKhuyenMai = 0 THEN @ThanhTienPhanBo
				ELSE 0
			END AS ThanhTienSauTrietKhauThucChay,
			0 AS GiaTriHoaHongThucChay,
			@ThanhTienPhanBo AS ThanhTienThucThu,
			CASE WHEN @IsKhuyenMai = 1 THEN (@SoLuongPhanBo*@DonGiaPhanBo)
				ELSE 0
			END as ThanhTienKM,
			CASE WHEN @IsKhuyenMai = 1 THEN @SoLuongPhanBo
				ELSE 0
			END as SoLuongThucChayKM,
			0 AS SoLuongLechTreoHa,
			0 AS ThanhTienLechTreoHa,
			GETDATE(),
			GETDATE(),
			0 IsPheDuyet,
			'' PheDuyetBy,
			'' PheDuyetAt	
		FROM
		(			                       
			SELECT distinct
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
				C.NhanHang, 
				C.DmNhomNganhREF, 
				C.TenNhomNganh, 
				--Thong tin hinh thuc quang cao
				C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
				--Thong tin San pham
				@DmSanPhamREF as DmSanPhamREF,
				@TenSanPham as TenSanPham,  
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
				--ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'Y'),'') DotChayHopDong,
				N'ThucChay_By_CongNo' DotChayHopDong,
				C.SoLuong AS SoLuongDotChayHD,
				--ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'N'),0) DotChayBooking,
				N'Update thuc chay da thanh toan het cong no hop dong' DotChayBooking,
				dbo.GetSoLuongDotChayBookingByHopDongChiTiet(C.HopDongChiTietID) SoLuongDotChayBooking, 
				--Thong tin ve Tien
				--****haidh chinh sua
				C.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong,
				--****haidh chinh sua
				--dbo.ThucChay_GetDonViTinhNotCPD(C.DonViTinh) as DonViTinh, 
				CASE C.DmSanPhamREF
					WHEN 337 THEN 'VIEW'
					ELSE 'CLICK'
				END DonViTinh,
				--'VIEW' DonViTinh, 
				--dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,C.HopDongChiTietID,C.DonGia) as DonGia,
				dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThanhToan,@HopDongChiTietID,C.DonGia) AS DonGia,
				--****haidh chinh sua 
				ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong, @NgayTHanhToan, C.HopDongChiTietID),0)  AS DonGiaTheoDonViTinh,
				C.ChietKhau, C.GiamGia, C.ThanhTien,
				C.TiLeTuVan,  C.ChiPhiTuVan,
				C.IsKhuyenMai,  
				C.KhuyenMai,
				--Thuc chay
				0 DmBannerREF,--A.DmBannerREF,
				0 DmChienDichREF,--A.DmChienDichREF,
				(SELECT TOP 1 DmWebsiteReportingdbID FROM DmWebsiteReportingdb WHERE DmWebsiteReportingdb.TenWebsite = @TenWebsite) DmWebsiteREF,
				@TenWebsite AS TenWebsite,
				0 TongViewThucChay,
				0 TongClickThucChay,
				0 TongSoBaiViet,
				CASE WHEN @IsKhuyenMai = 0 THEN @SoLuongPhanBo
					ELSE 0
				END as SoLuongThucChay,
				--Thanhuc Tien Thuc Chay
				@NgayThanhToan NgayThucHien,
				0 as GiaTriThayDoi,
				0 as ThanhTienThucChayTruocTrietKhau 
			FROM
				HopDong AS D 
				INNER JOIN HopDongChiTiet C ON C.HopDongFK = D.HopDongID
			WHERE D.TrangThaiHopDong <> 3
				AND C.HopDongChiTietID = @HopDongChiTietID
				AND C.DmSanPhamREF = @DmSanPhamREF
				AND C.DeletedStatus = 0
		)TD
		
		-- Update trang thai cho phan bo hop dong
		--UPDATE HopDongChiTietAdmarket
		--SET TrangthaiThucChay = 1 -- da chay xong
		--WHERE HopDongChiTietID = @HopDongChiTietID
	
		FETCH NEXT FROM record_cursor INTO @HopDongID, @SoHopDong, @GiaTriHopDong, @NgayThanhToan, @HopDongChiTietID, @SoLuongPhanBo, @DonViTinhPhanBo, @ThanhTienPhanBo 
					,@IsKhuyenMai, @TenSanPham, @TenWebsite, @DonGiaPhanBo
	END
	
	CLOSE record_cursor;
	DEALLOCATE record_cursor;
END

```
