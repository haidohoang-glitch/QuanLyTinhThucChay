# Stored Procedure: `sp_Insert_ThucChayDaTinh_ReInsertByHopDong_NhanHang_Manual`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-12-16 17:47:52.260000
- **Ngày sửa cuối**: 2018-09-21 11:31:39.803000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@PhanBoID` | `int(4)` | No |
| `@NhanHangOld` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong_NhanHang] '2016-09-29', 40969,	91354
CREATE PROCEDURE [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong_NhanHang_Manual]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@HopDongID INT,
	@PhanBoID INT,
	@NhanHangOld NVARCHAR(50)

AS
BEGIN
		-- SET NOCOUNT ON added to prevent extra result sets from
		-- interfering with SELECT statements.
		 DECLARE @GhiChu NVARCHAR(200) ='NH_TREO_TD: ', @CONTENT_LOG NVARCHAR(300), @DmNhanThucChayDaTinh NVARCHAR(200) = ''
		 DECLARE @DmNhanHangNew NVARCHAR(200)

		 --Xoa du lieu truoc khi chay tinh
		 DELETE FROM dbo.ThucChayDaTinh
		 WHERE HopDongID = @HopDongID
		 AND HopDongChiTietREF = @PhanBoID
		 AND NgayThucHien = @NgayThucHien
		 AND GhiChu LIKE '%NH_TREO_TD%'

		 --CHECK THONG TIN DMNHANHANG BI TRUNG NHAU GIUA THUCCHAYDATINH VA LOG THUC TREO
		 SET @DmNhanThucChayDaTinh = 
		 ISNULL((
			SELECT TOP 1 NhanHang FROM dbo.ThucChayDaTinh
			WHERE HopDongChiTietREF = @PhanBoID
			AND NgayThucHien <= @NgayThucHien
			AND NhanHang = @NhanHangOld
			ORDER BY NgayThucHien DESC, LastModifiedAt DESC
		 ),'')
		 
		 
		 SELECT @DmNhanHangNew = COALESCE(@DmNhanHangNew + ',', '') + ISNULL(CAST(T.DmNhanHangREF AS VARCHAR(1000)),'')
		 FROM   (
					SELECT DISTINCT DmNhanHangREF FROM dbo.ThucChayHopDongChiTiet
					WHERE  1=1
					AND HopDongChiTietREF = @PhanBoID AND DeletedStatus = 0
				) T         
 
		SET @DmNhanHangNew = ISNULL(@DmNhanHangNew,'');
		SET @CONTENT_LOG = N'Ngày :' + CONVERT(NVARCHAR(20), @NgayThucHien,103) + N' Nhãn được chuẩn hóa về dmnhanhang: ' + @DmNhanHangNew

		SELECT @DmNhanHangNew
		SET NOCOUNT ON;
		IF(@DmNhanThucChayDaTinh <> @DmNhanHangNew)
		BEGIN
		--DOI TRU GIAM
		   INSERT INTO ThucChayDaTinh
			  SELECT newid() AS ID
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
			  ,0[TongViewThucChay]
			  ,0[TongClickThucChay]
			  ,0[TongSoBaiViet]
			  ,0[SoLuongThucChay]
			  ,@NgayThucHien
			  ,-sum([ThanhTienSauTrietKhauThucChay]+[GiaTriThayDoi]) [GiaTriThayDoi]
			  ,0[ThanhTienThucChayTruocTrietKhau]
			  ,0[GiaTriTrietKhauThucChay]
			  ,0[ThanhTienSauTrietKhauThucChay]
			  ,0[GiaTriHoaHongThucChay]
			  ,0[ThanhTienThucThu]
			  ,0[ThanhTienKM]
			  ,0[SoLuongThucChayKM]
			  ,0[SoLuongThucChayLechTreoHa]
			  ,0[ThanhTienLechTreoHa]
			  ,getdate()[CreatedAt]
			  ,getdate()[LastModifiedAt]
			  ,0 [IsPheDuyet]
			  ,''[PheDuyetBy]
			  ,''[PheDuyetAt]
			  ,-sum([SoLuongThucChay]+[SoLuongThayDoi])[SoLuongThayDoi]
			  ,-sum(ISNULL([SoLuongThucChayKM],0)+ ISNULL([SoLuongKMThayDoi],0))[SoLuongKMThayDoi]
			  ,-sum([ThanhTienKM]+[GiaTriKMThayDoi])[GiaTriKMThayDoi]
			  ,@GhiChu + 'UPdate nhan hang theo thuc treo'
			  FROM [ThucChayDaTinh]
			  where HopDongID = @HopDongID AND HopDongChiTietREF = @PhanBoID
			  AND NgayThucHien >=	ISNULL((SELECT MAX(tc.NgayThucHien) FROM ThucChayDaTinh tc WHERE tc.HopDongID = @HopDongID AND tc.HopDongChiTietREF = @PhanBoID AND tc.NgayThucHien < @NgayThucHien and tc.GhiChu = 'UPdate nhan hang theo thuc treo' ),'2009-01-01')
			  AND NgayThucHien < @NgayThucHien
			  GROUP BY [HopDongID]
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
		

		---------DOI TRU TANG GIA TRI THAY DOI
	    INSERT INTO ThucChayDaTinh
			  SELECT newid() AS ID
			  ,[HopDongID]
			  ,[SoHopDong]
			  ,DmMaHopDongREF
			  ,ISNULL((SELECT dmhdc.TenMaHopDong
			               FROM DmMaHopDongChuan dmhdc WHERE dmhdc.DmMaHopDongID = DmMaHopDongREF),'')TenMaHopDong
			  ,NgayDanhSoHopDong
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
			  ,SysNhanVienREF
			  ,(SELECT hd.TenDangNhap
			      FROM HopDong hd WHERE hd.HopDongID = @HopDongID )
			  ,(SELECT nssyll.HoVaTen
							FROM NhanSuSoYeuLyLich nssyll WHERE nssyll.NhanSuSoYeuLyLichID = SysNhanVienREF)
			  ,TenKhachHang
			  ,@DmNhanHangNew --nhanhang
			  ,[DmNhomNganhREF]
			  ,[TenNhomNganh]
			  ,DmHinhThucQuangCao
			  ,(SELECT dhtqc.TenHinhThucQuangCao 
							FROM DmHinhThucQuangCao dhtqc WHERE dhtqc.DmHinhThucQuangCaoID = DmHinhThucQuangCao)
			  ,DmSanPhamREF
			  ,(SELECT dsp.TenSanPham
			                FROM DmSanPham dsp WHERE dsp.DmSanPhamID = DmSanPhamREF)
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
			  ,0[TongViewThucChay]
			  ,0[TongClickThucChay]
			  ,0[TongSoBaiViet]
			  ,0 [SoLuongThucChay]
			  ,@NgayThucHien
			  ,SUM([ThanhTienSauTrietKhauThucChay]+[GiaTriThayDoi]) GiaTriThayDoi
			  ,0[ThanhTienThucChayTruocTrietKhau]
			  ,0[GiaTriTrietKhauThucChay]
			  ,0 [ThanhTienSauTrietKhauThucChay]
			  ,0[GiaTriHoaHongThucChay]
			  ,0[ThanhTienThucThu]
			  ,SUM([ThanhTienKM]+[GiaTriKMThayDoi]) [ThanhTienKM]
			  ,SUM([SoLuongThucChayKM]+[SoLuongKMThayDoi]) [SoLuongThucChayKM]
			  ,0[SoLuongThucChayLechTreoHa]
			  ,0[ThanhTienLechTreoHa]
			  ,getdate()[CreatedAt]
			  ,getdate()[LastModifiedAt]
			  ,0 [IsPheDuyet]
			  ,''[PheDuyetBy]
			  ,''[PheDuyetAt]
			  ,SUM([SoLuongThucChay]+[SoLuongThayDoi])[SoLuongThayDoi]
			  ,0[SoLuongKMThayDoi]
			  ,0[GiaTriKMThayDoi]
			  ,@GhiChu +'Chay lai thuc chay'
			  FROM [ThucChayDaTinh]
			  where HopDongID = @HopDongID AND HopDongChiTietREF = @PhanBoID
			   AND NgayThucHien >=	ISNULL((SELECT MAX(tc.NgayThucHien) FROM ThucChayDaTinh tc WHERE tc.HopDongID = @HopDongID AND tc.HopDongChiTietREF = @PhanBoID AND tc.NgayThucHien < @NgayThucHien and tc.GhiChu = 'UPdate nhan hang theo thuc treo' ),'2009-01-01')
			   AND isnull(GhiChu,'') <> 'UPdate nhan hang theo thuc treo'
			   --AND isnull(GhiChu,'') <> 'PHAN BO BI XOA'
			   --AND isnull(GhiChu,'') <> 'THAY DOI DANH SACH NHAN HANG'
			   AND NgayThucHien < @NgayThucHien
			   GROUP BY [HopDongID]
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

		--Insert log
	    INSERT INTO [dbo].[ThucChay_LogNNTinhGiaTriThayDoi]
			SELECT  NEWID(), D.HopDongID,
	                    --Thong tin ve ma so 
	                    D.SoHopDong,
	                    C.HopDongChiTietID,
	                    C.DmSanPhamREF AS DmSanPhamREF,
						0 DmWebsiteREF,
						@NgayThucHien NgayThucHien,
						0 GiaTriThayDoi,
	                    0 AS GiaSauCK1,
	                    0 Soluong1,
	                    0 AS GiaSauCK2,
	                    0 Soluong2,
	                    @CONTENT_LOG,
	                    N'Chuẩn hóa nhãn hàng ',
	                    'CPM',	'ThucChay',	GETDATE(),
						'ThucChay',GETDATE(),0,
	                    0,0
			FROM    HopDongChiTiet C
	                    INNER JOIN HopDong D
	                        ON  D.HopDongID = C.HopDongFK
	            WHERE  D.TrangThaiHopDong != 3
					AND C.HopDongChiTietID = @PhanBoID
	                    AND C.DeletedStatus = 0
	                    AND C.DmSanPhamREF IN (140,228,240,241,242,243,251,252,253,300,339,342,370,385,531,535,540,541,549,560,563,
									586,598,613,629,630,631,632,633,634,635,636,732)
	END
END



```
