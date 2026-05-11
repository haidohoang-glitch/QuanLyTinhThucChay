# Stored Procedure: `prc_asd_InsertThucChay_Admarket_With_HopDong_MKT_FEE`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-07-02 10:33:00.150000
- **Ngày sửa cuối**: 2025-07-11 14:21:04.570000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(200)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChitietID` | `int(4)` | No |
| `@ThucChay_PerformanceBase_ThayDoi_ID` | `int(4)` | No |
| `@DmSanPhamID` | `int(4)` | No |
| `@TK_Admarket` | `nvarchar(1000)` | No |
| `@DmViTriID` | `int(4)` | No |
| `@TienThucChay_GhiNhan` | `float(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		HAIDH
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- exec [dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong] '2017-09-05'
-- =============================================
/*
	[dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong] '2021-03-24'
*/

CREATE PROCEDURE [dbo].[prc_asd_InsertThucChay_Admarket_With_HopDong_MKT_FEE]
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime
	,@SoHopDong NVARCHAR(100)
	,@HopDongID INT
	,@HopDongChitietID INT
	,@ThucChay_PerformanceBase_ThayDoi_ID INT
	,@DmSanPhamID INT
	,@TK_Admarket NVARCHAR(500)
	,@DmViTriID INT
	,@TienThucChay_GhiNhan FLOAT

AS
BEGIN
	DECLARE @NgayGhiNhanThayDoi   DATETIME
			  ,@LyDoLoi NVARCHAR(500) = N''
			  ,@RecordStatus int = 0
			  ,@GiaTriPhuTroi int = 1
			  ,@NgayDanhSoGioiHan DATETIME = '2025-07-05' --HAIDH COMMENT NGAYDANHSOGIOI HAN CHO VIEC BAT DAU AP DUNG VIEC TINH CHO SAN PHAM MKT-FEE
	DECLARE @ThanhTienThucChayDaTinh FLOAT = 0, 
		@ThanhTienThucChayDaTinhHopDong_All_Tk FLOAT = 0,
		@TongTienThucChayTK FLOAT = 0,
		@RecordStatus_UPDATE INT = 0,
		@ThucChayDaTinhID_output nvarchar(100) = N'',
		@SoLuongThucChay INT = 1, --So luong thuc chay cho don vi goi mac dinh = 1
		@DmChienDichREF INT = 4, --Tien thuc chay ghi nhan cho MKT-FEE
		@ThanhTien_HDCT FLOAT = 0

	DECLARE @Table_thucchaydatinh_id table(
		ThucChayDaTinhID NVARCHAR(50),
		HopDongREF INT
		)

	
		SET @RecordStatus_UPDATE = ISNULL((
							SELECT tctd.RecordStatus FROM [dbo].[ThucChay_PerformanceBase_ThayDoi_HopDong] tctd
							WHERE tctd.ThucChay_PerformanceBase_ThayDoi_ID = @ThucChay_PerformanceBase_ThayDoi_ID
						),0)

		SET @LyDoLoi = N''
		SET @RecordStatus = 0
		-----------ThucChayDaTinh----------------THONG TIN THUC CHAY DA TINH THEO HOP DONG

		SET @ThanhTienThucChayDaTinh = ISNULL(
			 (SELECT SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi + tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi)
			   FROM ThucChayDaTinh tcdt 
			   WHERE tcdt.HopDongID =  @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChitietID
			   AND tcdt.DmSanPhamREF = @DmSanPhamID AND tcdt.NgayThucHien <= @NgayThucHien
			   ),0)

		--THANH TIEN HOPDONGCHITIET
		SET @ThanhTien_HDCT = ISNULL((
			SELECT TOP (1) (CASE WHEN hdct.ChietKhau = 100 THEN hdct.DonGia*hdct.SoLuong
				ELSE hdct.ThanhTien
			END)
			FROM dbo.HopDongChiTiet hdct 
				WHERE hdct.HopDongChiTietID = @HopDongChiTietID 
				AND hdct.DmSanPhamREF = @DmSanPhamID 
				AND hdct.DeletedStatus = 0
				--AND hdct.ThanhTien >= (@ThanhTienThucChayDaTinh + @TienThucChay_GhiNhan) - @GiaTriPhuTroi
		),0)
		--**********************RULE************
		--Check gia tri muon them dam bao rule
		--1. gia tri them vao hop dong ko vuot qua gia tri phan bo
		IF((@ThanhTien_HDCT >= (@ThanhTienThucChayDaTinh + @TienThucChay_GhiNhan) - @GiaTriPhuTroi)
			AND ((@ThanhTienThucChayDaTinh + @TienThucChay_GhiNhan)>0)
		)
		BEGIN
			--THUC HIEN GHI NHAN THUC CHAY
			--PRINT 'Ghi nhan thuc chay thang du giai phap'
			--3. Sp insert dữ liệu
			DECLARE @DmWebsiteREF INT, @TenWebsite NVARCHAR(50), @TenViTri nvarchar(50) = '', @GhiChu NVARCHAR(max) ='',
			@v_ThucChayDaTinhID_output NVARCHAR(200)
			SET @DmWebsiteREF = 826
			SET @TenWebsite = '(Blanks)'
			SET @GhiChu = N'Tinh TC MKT-Fee theo Request'
			SET @TenViTri  = (CASE WHEN @DmViTriID = 1 THEN N'AdX'
									WHEN @DmViTriID = 2 THEN N'AdX Mobile'
									WHEN @DmViTriID = 3 THEN N'AdX Ecommerce'
									WHEN @DmViTriID = 4 THEN N'AdX Leadform'
								ELSE N''
							END)

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

		OUTPUT INSERTED.ThucChayDaTinhID, INSERTED.HopDongID INTO @Table_thucchaydatinh_id

		SELECT 
			NEWID() thucchaydatinhid,
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
			C.HopDongChiTietID,
			--Thong tin ve trang thai
			D.DangSuDung, D.IsGiayPhep, 2 TrangThaiHopDong,D.IsBanCung, 
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
			C.DanhSachNhanHangREF NhanHang, 
			C.DmNhomNganhREF, 
			C.TenNhomNganh, 
			C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
			c.DmSanPhamREF as DmSanPhamREF,
			C.TenSanPham,  
			C.DmNhomWebsiteREF, 
			C.TenNhomWebsite, 
			C.DmChuyenMucREF, 
			C.TenChuyenMuc,
			C.DmLoaiBannerREF, 
			C.TenLoaiBanner, 
			C.DmViTriREF DmViTriREF, 
			C.TenViTri TenViTri, 
			N'PerformanceBase_MKT' DotChayHopDong,
			0 AS SoLuongDotChayHD,
			N'Request_TD_PerformanceBase_MKT' DotChayBooking,
			@ThucChay_PerformanceBase_ThayDoi_ID AS SoLuongDotChayBooking, 
			C.SoLuong AS SoLuong, 
			C.DonViTinh as DonViTinh, 
			C.DonGia as DonGia, 
			C.DonGia AS DonGiaTheoDonViTinh,
			C.ChietKhau, C.GiamGia, C.ThanhTien,
			C.TiLeTuVan,  C.ChiPhiTuVan,
			C.IsKhuyenMai,  
			C.KhuyenMai,
			C.DmBannerREF DmBannerREF,
			@DmChienDichREF DmChienDichREF,
			@DmWebsiteREF DmWebsiteREF,
			@TenWebsite TenWebsite,
			0 TongViewThucChay,
			0 TongClickThucChay,
			0 TongSoBaiViet,
			IIF(C.ChietKhau = 100,0,@SoLuongThucChay)  SoLuongThucChay,
			@NgayThucHien AS NgayThucHien,
			0 as GiaTriThayDoi,	 
			0 as ThanhTienThucChayTruocTrietKhau,
			0 AS GiaTriTrietKhauThucChay,
			IIF(C.ChietKhau = 100,0,@TienThucChay_GhiNhan) AS ThanhTienSauTrietKhauThucChay,	
			0 AS GiaTriHoaHongThucChay,
			IIF(C.ChietKhau = 100,0,@TienThucChay_GhiNhan) AS ThanhTienThucThu,
			IIF(C.ChietKhau = 100,@TienThucChay_GhiNhan,0) ThanhTienKM,
			IIF(C.ChietKhau = 100,@SoLuongThucChay,0) as SoLuongThucChayKM,
			0 SoLuongLechTreoHa,
			0 ThanhTienLechTreoHa,
			GETDATE() createdat,
			GETDATE() lastmodifiedat,
			0 IsPheDuyet,
			'' PheDuyetBy,
			'' PheDuyetAt,
			0 SoLuongThayDoi,
			0 SoLuongKMThayDoi,
			0 GiaTriKMThayDoi,
			@GhiChu GhiChu	
	
			FROM 
			(
				SELECT * FROM dbo.HopDongChiTiet 
					WHERE HopDongChiTietID = @HopDongChiTietID
						AND DmSanPhamREF = @DmSanPhamID
						AND DmLoaiREF = 5038
						AND DmSanPhamREF = 817
						AND RecordStatus = 0
			) C  
			INNER JOIN  
			 ( 
	 			SELECT * FROM dbo.HopDong hd 
	 			WHERE 1=1-- hd.TrangThaiHopDong <> 3	    
				   AND hd.HopDongID = @HopDongID
				   AND hd.DeletedStatus = 0
				   AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan
			 ) D on D.HopDongID = C.HopDongFK

		SET @ThucChayDaTinhID_output  = (SELECT top (1)  ISNULL(ThucChayDaTinhID,'') FROM @Table_thucchaydatinh_id )

		--select   isnull(@ThucChayDaTinhID_output,'')

		IF(EXISTS(SELECT TOP (1) tc.HopDongID FROM ThucChayDaTinh tc
			WHERE tc.ThucChayDaTinhID = @ThucChayDaTinhID_output
			AND tc.HopDongID = @HopDongID
			AND tc.HopDongChiTietREF = @HopDongChitietID
			AND tc.DmSanPhamREF = @DmSanPhamID
			AND tc.NgayThucHien = @NgayThucHien
			AND tc.DmChienDichREF = @DmChienDichREF --GHI NHAN THEO SAN PHAM CHI PHI MKT-FEE
			ORDER BY tc.HopDongID ))
			BEGIN
				--PRINT 'Update trang thai da tinh'
				--print convert(varchar(50), @ThucChay_PerformanceBase_ThayDoi_ID)

				UPDATE tc
				SET tc.RecordStatus = 1
				FROM [ThucChay_PerformanceBase_ThayDoi_HopDong] tc
				WHERE tc.ThucChay_PerformanceBase_ThayDoi_ID = @ThucChay_PerformanceBase_ThayDoi_ID
				AND tc.HopDongID = @HopDongID
				AND tc.HopDongChitietID = @HopDongChitietID
		
				--GHI NHAN THUC CHAY VA TRANG THAI RECORDSTATUS = 1 CỦA [ThucChay_PerformanceBase_ThayDoi_HopDong]		
				SET @RecordStatus = 1
			END
		END
		ELSE 
		BEGIN
			--LOI GIA TRI THANH TIEN VUOT PHAN BO
			SET @LyDoLoi = N'Giá trị thêm vào hợp đồng vượt giá trị phân bổ, '
			
			IF((@ThanhTienThucChayDaTinh + @TienThucChay_GhiNhan) < 0)
				SET @LyDoLoi = N'Giá trị thực chạy thêm + Thành tiền thực chạy đã tính <0, '
			
			--LOI GHI NHAN THUC CHAY VA TRANG THAI RECORDSTATUS = 2 CỦA [ThucChay_PerformanceBase_ThayDoi_HopDong]		
			SET @RecordStatus = 2
		END

		--CAP NHAP LY DO TU CHOI
		UPDATE tctd
		SET tctd.LyDoLoi = tctd.LyDoLoi + @LyDoLoi
		, tctd.RecordStatus = @RecordStatus
		FROM [dbo].[ThucChay_PerformanceBase_ThayDoi_HopDong] tctd
		WHERE tctd.ThucChay_PerformanceBase_ThayDoi_ID = @ThucChay_PerformanceBase_ThayDoi_ID

		DELETE @Table_thucchaydatinh_id
END

```
