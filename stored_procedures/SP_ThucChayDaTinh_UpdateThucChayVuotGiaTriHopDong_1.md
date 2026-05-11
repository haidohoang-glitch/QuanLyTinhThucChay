# Stored Procedure: `ThucChayDaTinh_UpdateThucChayVuotGiaTriHopDong_1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-02-26 17:00:18.960000
- **Ngày sửa cuối**: 2015-02-26 17:04:41.270000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@DmHinhThucQuangCao` | `int(4)` | No |
| `@TenHinhThucQuangCao` | `nvarchar(100)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
-- EXEC dbo.ThucChayDaTinh_UpdateThucChayVuotGiaTriHopDong_1 '2014-12-31', 'QC1400814', 381, N'Sponsored Post', 7, N'CPC', N'CLICK',63179
CREATE PROCEDURE [dbo].[ThucChayDaTinh_UpdateThucChayVuotGiaTriHopDong_1]
	-- Add the parameters for the stored procedure here
	@NgayThucHien	DATETIME,
	@SoHopDong		NVARCHAR(50),
	@DmSanPhamREF	INT,
	@TenSanPham		NVARCHAR(50),
	@DmHinhThucQuangCao	INT,
	@TenHinhThucQuangCao	NVARCHAR(50),
	@DonViTinh		NVARCHAR(50),
	@HopDongChiTietID INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @TongTienThucChay	FLOAT = 0,
			@GiaTriHopDong		FLOAT = 0,
			@GiaTriThucChayVuot	FLOAT = 0,
			@Count				INT	  = 0,
			@ThucChayTheoSite	FLOAT = 0,
			@TyLe				FLOAT = 0,
			
			@TyLePhanBo			FLOAT = 0
			
	DECLARE @DmWebsiteREF	INT,
			@TenWebsite		NVARCHAR(50),
			@DonViTinhPB	NVARCHAR(50)
			
	SET @TongTienThucChay = (SELECT SUM(ISNULL(ThanhTienSauTrietKhauThucChay,0) + ISNULL(GiaTriThayDoi,0))
	FROM	ThucChayDaTinh AS tcdt
	WHERE tcdt.SoHopDong = @SoHopDong
		AND tcdt.DmSanPhamREF = @DmSanPhamREF
		AND tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCao
		AND tcdt.DonViTinh = @DonViTinh
		AND tcdt.HopDongChiTietREF = @HopDongChiTietID
		
	)

	SET @TongTienThucChay = ISNULL(@TongTienThucChay,0);
		
	PRINT 'TongTienThucChay: ' + CONVERT(NVARCHAR(50),@TongTienThucChay);
	
	IF @DonViTinh = 'VIEW'
		SET @DonViTinhPB = 'CPM'
	ELSE IF @DonViTinh = 'CLICK'
		SET @DonViTinhPB = 'CPC'
	ELSE 
		SET @DonViTinhPB = @DonViTinh
	
	SELECT @GiaTriHopDong = ISNULL(SUM(ThanhTien),0)
	FROM HopDong AS hd 
		INNER JOIN HopDongChiTiet AS hdct ON hdct.HopDongFK = hd.HopDongID
	WHERE hdct.DmSanPhamREF = @DmSanPhamREF
		AND hd.SoHopDong = @SoHopDong	
		AND hdct.IsKhuyenMai = 0
		AND hdct.DeletedStatus = 0
		AND hdct.DmLoaiREF = @DmHinhThucQuangCao
		AND hdct.DonViTinh = @DonViTinhPB
		AND hdct.HopDongChiTietID = @HopDongChiTietID
		
		
	PRINT 'GiaTriHopDong: ' + CONVERT(NVARCHAR(50),@GiaTriHopDong);	
	
	SET @GiaTriThucChayVuot = @TongTienThucChay - @GiaTriHopDong

	PRINT 'GiaTriThucChayVuot: ' + CONVERT(NVARCHAR(50),@GiaTriThucChayVuot);	
	
	SELECT @Count = COUNT(DISTINCT DmWebsiteREF) 
	FROM ThucChayDaTinh AS tcdt
	WHERE tcdt.SoHopDong = @SoHopDong AND tcdt.DmSanPhamREF = @DmSanPhamREF
		AND tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCao
		AND tcdt.DonViTinh = @DonViTinh
		AND tcdt.HopDongChiTietREF = @HopDongChiTietID
		
	PRINT 'SoLuongWebsite: ' + CONVERT(NVARCHAR(50),@Count);	
	
	DECLARE td_cursor CURSOR FOR
	SELECT DISTINCT DmWebsiteREF, TenWebsite
	FROM ThucChayDaTinh AS tcdt
	WHERE tcdt.SoHopDong = @SoHopDong AND tcdt.DmSanPhamREF = @DmSanPhamREF
		AND tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCao
		AND tcdt.DonViTinh = @DonViTinh
		AND tcdt.HopDongChiTietREF = @HopDongChiTietID
		
	OPEN td_cursor
	
	FETCH NEXT FROM td_cursor INTO @DmWebsiteREF, @TenWebsite
	WHILE @@FETCH_STATUS = 0
	BEGIN
		SELECT @ThucChayTheoSite = SUM(ISNULL(ThanhTienSauTrietKhauThucChay,0) + ISNULL(GiaTriThayDoi,0))
		FROM ThucChayDaTinh AS tcdt
		WHERE tcdt.SoHopDong = @SoHopDong
			AND tcdt.DmSanPhamREF = @DmSanPhamREF
			AND tcdt.DmWebsiteREF = @DmWebsiteREF
			AND tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCao
			AND tcdt.DonViTinh = @DonViTinh
			AND tcdt.HopDongChiTietREF = @HopDongChiTietID
			
		SET @TyLe = @ThucChayTheoSite/@TongTienThucChay*100
		
		PRINT 'Website: ' + @TenWebsite;
		PRINT 'TyLe: ' + CONVERT(NVARCHAR(50),@TyLe);
		
		
		IF (@TyLe > 0 
			--AND @DmWebsiteREF > 0
		)
		BEGIN
			PRINT 'OK'
			
			INSERT INTO ThucChayDaTinh
			SELECT  NEWID(), TD.*, 
				 0 GiaTriTrietKhauThucChay,
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
				 0 SoLuongThayDoi,
				 0 GiaTriKhuyenMaiThayDoi,
				 0 SoLuongKhuyenMaiThayDoi,
				 '' GhiChu
			FROM 
			(
				 SELECT DISTINCT
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
					 @HopDongChiTietID HopDongChiTietID,
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
					 0 NhanHang, 
					 0 DmNhomNganhREF, 
					 0 TenNhomNganh, 
					 --Thong tin hinh thuc quang cao
					 @DmHinhThucQuangCao AS DmHinhThucQuangCao, 
					 @TenHinhThucQuangCao AS TenHinhThucQuangCao, 
					 --Thong tin San pham
					 @DmSanPhamREF as DmSanPhamREF,
					 @TenSanPham TenSanPham,  
					 0 DmNhomWebsiteREF, 
					 0 TenNhomWebsite, 
					 --C.DmWebsiteREF, 
					 --C.TenWebsite, 
					 0 DmChuyenMucREF, 
					 0 TenChuyenMuc,
					 0 DmLoaiBannerREF, 
					 0 TenLoaiBanner, 
					 0 DmViTriREF, 
					 0 TenViTri, 
					 'Update_VuotGiaTriHopDong' DotChayHopDong,
					 0 AS SoLuongDotChayHD,
					 'PS Update thuc chay vuot gia tri hop dong' DotChayBooking,
					 0 AS SoLuongDotChayBooking, 
					 --Thong tin ve Tien
					 0 AS SoLuong, 
					 @DonViTinh DonViTinh, 
					 0 as DonGia, 
					 --ISNULL(dbo.ThucChay_GetDonGiaThucTreo_PR(D.NgayKyHopDong, '2014-05-14', C.HopDongChiTietID),0) AS DonGiaTheoDonViTinh,
					 0 AS DonGiaTheoDonViTinh,
					 0 ChietKhau, 0 GiamGia, 0 ThanhTien,
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
					 0 SoLuongThucChay,
					 --Thanhuc Tien Thuc Chay
					 @NgayThucHien AS NgayThucHien,
					 0 - (@GiaTriThucChayVuot*@TyLe/100) as GiaTriThayDoi,
					 --(@GiaTriThucChayVuot*@TyLe/100) as GiaTriThayDoi,
					 0 as ThanhTienThucChayTruocTrietKhau
				 FROM 
					Hopdong D 
					--INNER JOIN HopDongChiTiet C ON C.HopDongFK = D.HopDongID
				 WHERE D.SoHopDong = @SoHopDong
			) TD
		END
		
		FETCH NEXT FROM td_cursor INTO @DmWebsiteREF, @TenWebsite
	END
	
	CLOSE td_cursor
	DEALLOCATE td_cursor
	
	
	SELECT 
			A.SoHopDong, A.ThanhTienThucChay, B.GiaTriHopDong,
			(B.GiaTriHopDong - A.ThanhTienThucChay) Lech
		FROM
		(
			SELECT 
				SoHopDong,
				SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0)) ThanhTienThucChay
			FROM ThucChayDaTinh tcdt
			WHERE 1=1
				--AND tcdt.NgayThucHien >= '2014-01-01'
				AND tcdt.DmSanPhamREF = @DmSanPhamREF
				AND tcdt.SoHopDong = @SoHopDong
				AND tcdt.HopDongChiTietREF = @HopDongChiTietID
			GROUP BY 
				tcdt.SoHopDong
		) A INNER JOIN
		(
			SELECT 
				hd.SoHopDong,
				SUM(hdct.ThanhTien) GiaTriHopDong
			FROM HopDong AS hd
				INNER JOIN HopDongChiTiet AS hdct ON hdct.HopDongFK = hd.HopDongID
			WHERE 1 = 1
				AND hdct.DmSanPhamREF = @DmSanPhamREF
				AND hd.TrangThaiHopDong <> 3
				AND hdct.IsKhuyenMai = 0
				AND hdct.DeletedStatus = 0
				AND hd.SoHopDong = @SoHopDong
				AND hdct.HopDongChiTietID = @HopDongChiTietID
			GROUP BY hd.SoHopDong
		)B ON B.SoHopDong = A.SoHopDong
END

```
