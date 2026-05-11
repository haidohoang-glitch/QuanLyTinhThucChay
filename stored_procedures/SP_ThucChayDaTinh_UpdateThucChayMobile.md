# Stored Procedure: `ThucChayDaTinh_UpdateThucChayMobile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-20 16:51:25.147000
- **Ngày sửa cuối**: 2014-11-19 12:24:49.860000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmHinhThucQuangCao` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
-- EXEC dbo.ThucChayDaTinh_UpdateThucChayMobile '2014-06-13', 'QC140414', 7, 'CLICK'

CREATE PROCEDURE [dbo].[ThucChayDaTinh_UpdateThucChayMobile]
	-- Add the parameters for the stored procedure here
	@NgayThucHien	DATETIME,
	@SoHopDong		NVARCHAR(50),
	@DmHinhThucQuangCao	INT,
	@DonViTinh		NVARCHAR(50)
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
		AND tcdt.DmSanPhamREF = 342
		AND tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCao
		AND tcdt.DonViTinh = @DonViTinh
	)
	
	SET @TongTienThucChay = ISNULL(@TongTienThucChay,0);
		
	PRINT 'TongTienThucChay: ' + CONVERT(NVARCHAR(50),@TongTienThucChay);
	
	IF @DonViTinh = 'VIEW'
		SET @DonViTinhPB = 'CPM'
	ELSE
		SET @DonViTinhPB = 'CPC'
	
	SELECT @GiaTriHopDong = ISNULL(SUM(ThanhTien),0)
	FROM HopDong AS hd 
		INNER JOIN HopDongChiTiet AS hdct ON hdct.HopDongFK = hd.HopDongID
	WHERE hdct.DmSanPhamREF = 342
		AND hd.SoHopDong = @SoHopDong	
		AND hdct.IsKhuyenMai = 0
		AND hdct.DeletedStatus = 0
		AND hdct.DmLoaiREF = @DmHinhThucQuangCao
		AND hdct.DonViTinh = @DonViTinhPB
		
	PRINT 'GiaTriHopDong: ' + CONVERT(NVARCHAR(50),@GiaTriHopDong);	
	
	SET @GiaTriThucChayVuot = @TongTienThucChay - @GiaTriHopDong
	--SET @GiaTriThucChayVuot = 751653290.908
	PRINT 'GiaTriThucChayVuot: ' + CONVERT(NVARCHAR(50),@GiaTriThucChayVuot);	
	
	SELECT @Count = COUNT(DISTINCT DmWebsiteREF) 
	FROM ThucChayDaTinh AS tcdt
	WHERE tcdt.SoHopDong = @SoHopDong AND tcdt.DmSanPhamREF = 342
		AND tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCao
		AND tcdt.DonViTinh = @DonViTinh
	
	PRINT 'SoLuongWebsite: ' + CONVERT(NVARCHAR(50),@Count);	
	
	DECLARE td_cursor CURSOR FOR
	SELECT DISTINCT DmWebsiteREF, TenWebsite
	FROM ThucChayDaTinh AS tcdt
	WHERE tcdt.SoHopDong = @SoHopDong AND tcdt.DmSanPhamREF = 342
		AND tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCao
		AND tcdt.DonViTinh = @DonViTinh
	
	OPEN td_cursor
	
	FETCH NEXT FROM td_cursor INTO @DmWebsiteREF, @TenWebsite
	WHILE @@FETCH_STATUS = 0
	BEGIN
		SELECT @ThucChayTheoSite = SUM(ISNULL(ThanhTienSauTrietKhauThucChay,0) + ISNULL(GiaTriThayDoi,0))
		FROM ThucChayDaTinh AS tcdt
		WHERE tcdt.SoHopDong = @SoHopDong
			AND tcdt.DmSanPhamREF = 342
			AND tcdt.DmWebsiteREF = @DmWebsiteREF
			AND tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCao
			AND tcdt.DonViTinh = @DonViTinh
			
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
				 0 SoLuongKMThayDoi,
				 0 GiaTriKMThayDoi,
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
					 0 HopDongChiTietID,
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
					 CASE WHEN @DmHinhThucQuangCao = 6 THEN 'CPM'
						  WHEN @DmHinhThucQuangCao = 7 THEN 'CPC'
					 END AS TenHinhThucQuangCao, 
					 --Thong tin San pham
					 342 as DmSanPhamREF,
					 'Mobile' TenSanPham,  
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
					 'Mobile_Update' DotChayHopDong,
					 0 AS SoLuongDotChayHD,
					 'PS Mobile Update thuc chay vuot gia tri hop dong' DotChayBooking,
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
					--AND C.DmSanPhamREF = 342
					--AND C.IsKhuyenMai = 0
			) TD
		END
		
		FETCH NEXT FROM td_cursor INTO @DmWebsiteREF, @TenWebsite
	END
	
	CLOSE td_cursor
	DEALLOCATE td_cursor
END

```
