# Stored Procedure: `ThucChay_InsertGiaTriThayDoiThucChayDaTinhAdmarket_xulynhan_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-10-11 10:39:24.480000
- **Ngày sửa cuối**: 2016-10-12 14:01:13.480000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(200)` | No |
| `@DmNhanHangREF` | `int(4)` | No |
| `@DmNhanHangThayDoiREF` | `int(4)` | No |
| `@ThanhTienThucChay` | `bigint(8)` | No |
| `@SoLuongThucChay` | `bigint(8)` | No |
| `@CONTENT_LOG` | `nvarchar` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_InsertGiaTriThayDoiThucChayDaTinhAdmarket_xulynhan_v2] 
-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@HopDongID INT,
	@DmSanPhamREF INT,
	@HopDongChiTietREF INT,
	@DonViTinh NVARCHAR(100),
	@DmNhanHangREF INT,
	@DmNhanHangThayDoiREF INT,
	@ThanhTienThucChay BIGINT,
	@SoLuongThucChay BIGINT,
	@CONTENT_LOG NVARCHAR(MAX)
AS
BEGIN
	DECLARE @MinDate DATETIME
	DECLARE @GhiChu NVARCHAR(200) ='NH_TREO_TD_xuly: ' + N'Update nhan hang chuan hoa giam'
	
	DECLARE @GhiChu_tang NVARCHAR(200) ='NH_TREO_TD_xuly: ' + N'Update nhan hang chuan hoa tang'
	
			        
	IF (@ThanhTienThucChay != 0)
	BEGIN
	--DOI TRU AM VOI NHAN HANG BI CHUAN HOA
	    --INSERT INTO ThucChayDaTinhAdmarket
		--@GhiChu
		--@DmNhanHangREF
		-- - @ThanhTienThucChay
		INSERT INTO ThucChayDaTinhAdmarket_xulynhan
	   	SELECT * FROM
			(
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
			  ,@DmNhanHangREF Nhanhang
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
			  ,@NgayThucHien NgayThucHien
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
			  ,-sum([SoLuongThucChayKM]+[SoLuongKMThayDoi])[SoLuongKMThayDoi]
			  ,-sum([ThanhTienKM]+[GiaTriKMThayDoi])[GiaTriKMThayDoi]
			  ,@GhiChu GhiChu
			  FROM [dbo].[ThucChayDaTinhAdmarket]
			  where HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietREF
			  --AND NgayThucHien >=	ISNULL((SELECT MAX(tc.NgayThucHien) FROM dbo.ThucChayDaTinhAdmarket tc WHERE tc.HopDongID = @HopDongID AND tc.HopDongChiTietREF = @HopDongChiTietREF AND tc.NgayThucHien < @NgayThucHien ),'2009-01-01')
			  AND NgayThucHien < @NgayThucHien
			  AND NhanHang =CONVERT(NVARCHAR(200), @DmNhanHangREF)
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
			  , NhanHang
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
		)TD
		WHERE TD.GiaTriThayDoi <> 0


		--DOI TRU DUONG VOI NHAN HANG DUOC NHAN CHUAN HOA TU NHAN KHAC
		--INSERT INTO ThucChayDaTinhAdmarket
		
		INSERT INTO ThucChayDaTinhAdmarket_xulynhan
		   SELECT * FROM
		(
			  SELECT newid() AS ID
			  ,[HopDongID]
			  ,[SoHopDong]
			  ,DmMaHopDongREF
			  ,TenMaHopDong
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
			  ,TenDangNhap
			  ,TenNhanVien
			  ,TenKhachHang
			  ,@DmNhanHangThayDoiREF nhanhang
			  ,[DmNhomNganhREF]
			  ,[TenNhomNganh]
			  ,DmHinhThucQuangCao
			  ,TenHinhThucQuangCao
			  ,DmSanPhamREF
			  ,TenSanPham
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
			  ,@NgayThucHien NgayThucHien
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
			  ,@GhiChu_tang GhiChu
			  FROM [dbo].[ThucChayDaTinhAdmarket]
			  where HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietREF
			   --AND NgayThucHien >=	ISNULL((SELECT MAX(tc.NgayThucHien) FROM dbo.ThucChayDaTinhAdmarket tc WHERE tc.HopDongID = @HopDongID AND tc.HopDongChiTietREF = @HopDongChiTietREF AND tc.NgayThucHien < @NgayThucHien),'2009-01-01')
			   AND NgayThucHien < @NgayThucHien
			   AND NhanHang = CONVERT(NVARCHAR(200),@DmNhanHangREF)
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

	)TD
	WHERE TD.GiaTriThayDoi <> 0
	            
	            
			--Insert log
	        INSERT INTO [dbo].[ThucChay_LogNNTinhGiaTriThayDoi]
				SELECT  NEWID(), D.HopDongID,
	                        --Thong tin ve ma so 
	                        D.SoHopDong,
	                        @HopDongChiTietREF HopDongChiTietREF,
	                        C.DmSanPhamREF AS DmSanPhamREF,
							0 DmWebsiteREF,
							@NgayThucHien NgayThucHien,
							@ThanhTienThucChay GiaTriThayDoi,
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
	                        AND C.DeletedStatus = 0
	                        AND C.DmSanPhamREF IN (144,299,337,585,628)
							AND C.HopDongChiTietID = @HopDongChiTietREF
	                             
	END

END



```
