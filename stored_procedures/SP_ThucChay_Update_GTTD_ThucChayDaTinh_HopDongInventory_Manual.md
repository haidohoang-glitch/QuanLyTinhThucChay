# Stored Procedure: `ThucChay_Update_GTTD_ThucChayDaTinh_HopDongInventory_Manual`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-01-07 13:55:32.010000
- **Ngày sửa cuối**: 2021-09-27 17:53:12.163000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
/*
[ThucChay_Update_GTTD_ThucChayDaTinh_HopDongInventory_Manual]
	@NgayThucHien = '2016-12-31'
	,@HopDongChiTietID =93809
*/

-------------------------------------------------------------
CREATE PROCEDURE [dbo].[ThucChay_Update_GTTD_ThucChayDaTinh_HopDongInventory_Manual] 
	@NgayThucHien DATETIME,
	@HopDongChiTietID INT
AS
BEGIN
		DECLARE @HopDongREF INT, @SoHopDong NVARCHAR(50),  @DmSanPhamREF INT
		, @ThanhTien_ThucChayDaTinh BIGINT, @ThanhTien_HopDongChiTiet BIGINT, @Note NVARCHAR(MAX) = ''

		DECLARE Record_Cursor CURSOR FOR 
	    
		SELECT distinct  hd.HopDongID, hd.SoHopDong,  hdtd.DmSanPhamREF, hdtd.HopDongChiTietID
		FROM HopDong hd
		INNER JOIN dbo.HopDongChiTiet hdtd ON hd.HopDongID = hdtd.HopDongFK AND hd.TrangThaiHopDong <> 3
		WHERE 1=1
		AND NOT (hdtd.DmLoaiREF in (13) or hdtd.DmLoaiBannerREF = 18)--Khong update gia tri thay doi cho HTQC Mua Ngoai 
		AND hd.HopDongID IN (SELECT DISTINCT HopDongREF FROM dbo.DmThongTinHopDongBanInventory)
		AND hdtd.HopDongChiTietID = @HopDongChiTietID
		ORDER BY hd.SoHopDong	
		
		OPEN Record_Cursor

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong,  @DmSanPhamREF, @HopDongChiTietID
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				--SET @Note = 'INVENTORY_TDTC_THANHTIEN '
				SET @Note = 'TD_2016_INVENTORY_TDTC_THANHTIEN '
				--XAC DINH THANH TIEN THUCCHAY VA THANH TIEN HOPDONGCHITIET
				SET @ThanhTien_HopDongChiTiet = ISNULL((
					SELECT ThanhTien FROM dbo.HopDongChiTiet
					WHERE HopDongChiTietID = @HopDongChiTietID
				) ,0)
				IF(@DmSanPhamREF NOT IN (585,144,628)) 
				BEGIN
					SET @ThanhTien_ThucChayDaTinh = ISNULL((
					SELECT TOP 1 (ThanhTiensautrietkhauthucchay + giatrithaydoi) FROM dbo.ThucChayDaTinh
					WHERE HopDongID = @HopDongREF
					AND HopDongChiTietREF = @HopDongChiTietID
					ORDER BY NgayThucHien , CreatedAt DESC
					),0)
				END
				ELSE
				BEGIN
					SET @ThanhTien_ThucChayDaTinh = ISNULL((
					SELECT TOP 1 (ThanhTiensautrietkhauthucchay + giatrithaydoi) FROM dbo.ThucChayDaTinhAdmarket
					WHERE HopDongID = @HopDongREF
					AND HopDongChiTietREF = @HopDongChiTietID
					ORDER BY NgayThucHien , CreatedAt DESC
					),0)
				END
				IF(@ThanhTien_HopDongChiTiet <> @ThanhTien_ThucChayDaTinh)
				BEGIN
					--THUC HIEN UPDATE GIA TRI THAY DOI
					PRINT 'THAY DOI GIAM'

					INSERT INTO dbo.ThucChayDaTinh
					        ( ThucChayDaTinhID ,
					          HopDongID ,
					          SoHopDong ,
					          DmMaHopDongREF ,
					          TenMaHopDong ,
					          NgayDanhSoHopDong ,
					          NgayKyHopDong ,
					          NhanHopDong ,
					          NgayNhanBanFax ,
					          NgayNhanHopDongBanCung ,
					          NgayChuyenHopDongChoKeToan ,
					          So ,
					          Thang ,
					          Nam ,
					          GiaTriHopDong ,
					          CongNo ,
					          HopDongChiTietREF ,
					          DangSuDung ,
					          IsGiayPhep ,
					          TrangThaiHopDong ,
					          IsBanCung ,
					          DmPhongBanREF ,
					          TenPhongBan ,
					          DmBoPhanREF ,
					          TenBoPhan ,
					          DmNhomLamViecREF ,
					          TenNhomLamViec ,
					          DmDiaDiemLamViecREF ,
					          TenDiaDiemLamViec ,
					          SysNhanVienREF ,
					          TenDangNhap ,
					          TenNhanVien ,
					          TenKhachHang ,
					          NhanHang ,
					          DmNhomNganhREF ,
					          TenNhomNganh ,
					          DmHinhThucQuangCao ,
					          TenHinhThucQuangCao ,
					          DmSanPhamREF ,
					          TenSanPham ,
					          DmNhomWebsiteREF ,
					          TenNhomWebsite ,
					          DmChuyenMucREF ,
					          TenChuyenMuc ,
					          DmLoaiBannerREF ,
					          TenLoaiBanner ,
					          DmViTriREF ,
					          TenViTri ,
					          DotChayHopDong ,
					          SoLuongDotChayHD ,
					          DotChayBooking ,
					          SoLuongDotChayBooking ,
					          SoLuong ,
					          DonViTinh ,
					          DonGia ,
					          DonGiaTheoDonVi ,
					          ChietKhau ,
					          GiamGia ,
					          ThanhTien ,
					          TiLeTuVan ,
					          ChiPhiTuVan ,
					          IsKhuyenMai ,
					          KhuyenMai ,
					          DmBannerREF ,
					          DmChienDichREF ,
					          DmWebsiteREF ,
					          TenWebsite ,
					          TongViewThucChay ,
					          TongClickThucChay ,
					          TongSoBaiViet ,
					          SoLuongThucChay ,
					          NgayThucHien ,
					          GiaTriThayDoi ,
					          ThanhTienThucChayTruocTrietKhau ,
					          GiaTriTrietKhauThucChay ,
					          ThanhTienSauTrietKhauThucChay ,
					          GiaTriHoaHongThucChay ,
					          ThanhTienThucThu ,
					          ThanhTienKM ,
					          SoLuongThucChayKM ,
					          SoLuongThucChayLechTreoHa ,
					          ThanhTienLechTreoHa ,
					          CreatedAt ,
					          LastModifiedAt ,
					          IsPheDuyet ,
					          PheDuyetBy ,
					          PheDuyetAt ,
					          SoLuongThayDoi ,
					          SoLuongKMThayDoi ,
					          GiaTriKMThayDoi ,
					          GhiChu
					        )
					SELECT TCDT.* FROM
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
							,'' [DotChayHopDong]
							,0 [SoLuongDotChayHD]
							,'HDBAN_INVENTORY' [DotChayBooking]
							,0 [SoLuongDotChayBooking]
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
							,-sum(ISNULL([SoLuongThucChayKM],0)+ ISNULL([SoLuongKMThayDoi],0))[SoLuongKMThayDoi]
							,-sum([ThanhTienKM]+[GiaTriKMThayDoi])[GiaTriKMThayDoi]
							,@Note + ' GIAM GIA TRI' Note
							FROM [ThucChayDaTinh]
							where HopDongID = @HopDongREF AND HopDongChiTietREF = @HopDongChiTietID
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
					)TCDT
					WHERE TCDT.GiaTriThayDoi <> 0
				
					
				--2. THAY DOI TANG
				INSERT INTO dbo.ThucChayDaTinh
				        ( ThucChayDaTinhID ,
				          HopDongID ,
				          SoHopDong ,
				          DmMaHopDongREF ,
				          TenMaHopDong ,
				          NgayDanhSoHopDong ,
				          NgayKyHopDong ,
				          NhanHopDong ,
				          NgayNhanBanFax ,
				          NgayNhanHopDongBanCung ,
				          NgayChuyenHopDongChoKeToan ,
				          So ,
				          Thang ,
				          Nam ,
				          GiaTriHopDong ,
				          CongNo ,
				          HopDongChiTietREF ,
				          DangSuDung ,
				          IsGiayPhep ,
				          TrangThaiHopDong ,
				          IsBanCung ,
				          DmPhongBanREF ,
				          TenPhongBan ,
				          DmBoPhanREF ,
				          TenBoPhan ,
				          DmNhomLamViecREF ,
				          TenNhomLamViec ,
				          DmDiaDiemLamViecREF ,
				          TenDiaDiemLamViec ,
				          SysNhanVienREF ,
				          TenDangNhap ,
				          TenNhanVien ,
				          TenKhachHang ,
				          NhanHang ,
				          DmNhomNganhREF ,
				          TenNhomNganh ,
				          DmHinhThucQuangCao ,
				          TenHinhThucQuangCao ,
				          DmSanPhamREF ,
				          TenSanPham ,
				          DmNhomWebsiteREF ,
				          TenNhomWebsite ,
				          DmChuyenMucREF ,
				          TenChuyenMuc ,
				          DmLoaiBannerREF ,
				          TenLoaiBanner ,
				          DmViTriREF ,
				          TenViTri ,
				          DotChayHopDong ,
				          SoLuongDotChayHD ,
				          DotChayBooking ,
				          SoLuongDotChayBooking ,
				          SoLuong ,
				          DonViTinh ,
				          DonGia ,
				          DonGiaTheoDonVi ,
				          ChietKhau ,
				          GiamGia ,
				          ThanhTien ,
				          TiLeTuVan ,
				          ChiPhiTuVan ,
				          IsKhuyenMai ,
				          KhuyenMai ,
				          DmBannerREF ,
				          DmChienDichREF ,
				          DmWebsiteREF ,
				          TenWebsite ,
				          TongViewThucChay ,
				          TongClickThucChay ,
				          TongSoBaiViet ,
				          SoLuongThucChay ,
				          NgayThucHien ,
				          GiaTriThayDoi ,
				          ThanhTienThucChayTruocTrietKhau ,
				          GiaTriTrietKhauThucChay ,
				          ThanhTienSauTrietKhauThucChay ,
				          GiaTriHoaHongThucChay ,
				          ThanhTienThucThu ,
				          ThanhTienKM ,
				          SoLuongThucChayKM ,
				          SoLuongThucChayLechTreoHa ,
				          ThanhTienLechTreoHa ,
				          CreatedAt ,
				          LastModifiedAt ,
				          IsPheDuyet ,
				          PheDuyetBy ,
				          PheDuyetAt ,
				          SoLuongThayDoi ,
				          SoLuongKMThayDoi ,
				          GiaTriKMThayDoi ,
				          GhiChu
				        )
			
				SELECT * FROM
				(
						SELECT TOP 1 newid() AS ID
						,[HopDongID]
						,[SoHopDong]
						, DmMaHopDongREF
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
						,[NhanHang] --nhan hang       
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
						,'' [DotChayHopDong]
						,0 [SoLuongDotChayHD]
						,'HDBAN_INVENTORY' [DotChayBooking]
						,'' [SoLuongDotChayBooking]
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
						,@ThanhTien_HopDongChiTiet GiaTriThayDoi
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
						, SoLuong [SoLuongThayDoi]
						,0[SoLuongKMThayDoi]
						,0[GiaTriKMThayDoi]
						,(@Note + 'Chay lai thuc chay ') Note
						FROM [ThucChayDaTinh]
						where HopDongID = @HopDongREF AND HopDongChiTietREF = @HopDongChiTietID
    					AND NgayThucHien < @NgayThucHien
						GROUP BY
						[HopDongID]
						,[SoHopDong]
						,DmMaHopDongREF
						,TenMaHopDong
						,NgayDanhSoHopDong
						,[NgayKyHopDong]
						,[NhanHopDong]
						,[NgayNhanBanFax]
						,SysNhanVienREF
						, TenNhanVien
						, TenKhachHang
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
						,[TenDangNhap]
						, DmHinhThucQuangCao
						, TenHinhThucQuangCao
						,[NhanHang]
						,[DmNhomNganhREF]
						,[TenNhomNganh]
						, DmSanPhamREF
						, TenSanPham
						,[DmNhomWebsiteREF]
						,[TenNhomWebsite]
						,[DmChuyenMucREF]
						,[TenChuyenMuc]
						,[DmLoaiBannerREF]
						,[TenLoaiBanner]
						,[DmViTriREF]
						,[TenViTri]
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
				)TCDT
				WHERE TCDT.GiaTriThayDoi <> 0

				IF(@DmSanPhamREF  NOT IN (585,144,628)) 
				BEGIN
					PRINT 'THAY DOI GIAM'
					INSERT INTO dbo.ThucChayDaTinhAdmarket
					        ( ThucChayDaTinhID ,
					          HopDongID ,
					          SoHopDong ,
					          DmMaHopDongREF ,
					          TenMaHopDong ,
					          NgayDanhSoHopDong ,
					          NgayKyHopDong ,
					          NhanHopDong ,
					          NgayNhanBanFax ,
					          NgayNhanHopDongBanCung ,
					          NgayChuyenHopDongChoKeToan ,
					          So ,
					          Thang ,
					          Nam ,
					          GiaTriHopDong ,
					          CongNo ,
					          HopDongChiTietREF ,
					          DangSuDung ,
					          IsGiayPhep ,
					          TrangThaiHopDong ,
					          IsBanCung ,
					          DmPhongBanREF ,
					          TenPhongBan ,
					          DmBoPhanREF ,
					          TenBoPhan ,
					          DmNhomLamViecREF ,
					          TenNhomLamViec ,
					          DmDiaDiemLamViecREF ,
					          TenDiaDiemLamViec ,
					          SysNhanVienREF ,
					          TenDangNhap ,
					          TenNhanVien ,
					          TenKhachHang ,
					          NhanHang ,
					          DmNhomNganhREF ,
					          TenNhomNganh ,
					          DmHinhThucQuangCao ,
					          TenHinhThucQuangCao ,
					          DmSanPhamREF ,
					          TenSanPham ,
					          DmNhomWebsiteREF ,
					          TenNhomWebsite ,
					          DmChuyenMucREF ,
					          TenChuyenMuc ,
					          DmLoaiBannerREF ,
					          TenLoaiBanner ,
					          DmViTriREF ,
					          TenViTri ,
					          DotChayHopDong ,
					          SoLuongDotChayHD ,
					          DotChayBooking ,
					          SoLuongDotChayBooking ,
					          SoLuong ,
					          DonViTinh ,
					          DonGia ,
					          DonGiaTheoDonVi ,
					          ChietKhau ,
					          GiamGia ,
					          ThanhTien ,
					          TiLeTuVan ,
					          ChiPhiTuVan ,
					          IsKhuyenMai ,
					          KhuyenMai ,
					          DmBannerREF ,
					          DmChienDichREF ,
					          DmWebsiteREF ,
					          TenWebsite ,
					          TongViewThucChay ,
					          TongClickThucChay ,
					          TongSoBaiViet ,
					          SoLuongThucChay ,
					          NgayThucHien ,
					          GiaTriThayDoi ,
					          ThanhTienThucChayTruocTrietKhau ,
					          GiaTriTrietKhauThucChay ,
					          ThanhTienSauTrietKhauThucChay ,
					          GiaTriHoaHongThucChay ,
					          ThanhTienThucThu ,
					          ThanhTienKM ,
					          SoLuongThucChayKM ,
					          SoLuongThucChayLechTreoHa ,
					          ThanhTienLechTreoHa ,
					          CreatedAt ,
					          LastModifiedAt ,
					          IsPheDuyet ,
					          PheDuyetBy ,
					          PheDuyetAt ,
					          SoLuongThayDoi ,
					          SoLuongKMThayDoi ,
					          GiaTriKMThayDoi ,
					          GhiChu
					        )
					SELECT TCDT.* FROM
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
							,'' [DotChayHopDong]
							,0 [SoLuongDotChayHD]
							,'HDBAN_INVENTORY' [DotChayBooking]
							,0 [SoLuongDotChayBooking]
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
							,-sum(ISNULL([SoLuongThucChayKM],0)+ ISNULL([SoLuongKMThayDoi],0))[SoLuongKMThayDoi]
							,-sum([ThanhTienKM]+[GiaTriKMThayDoi])[GiaTriKMThayDoi]
							,@Note + ' GIAM GIA TRI' Note
							FROM [dbo].[ThucChayDaTinhAdmarket]
							where HopDongID = @HopDongREF AND HopDongChiTietREF = @HopDongChiTietID
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
					)TCDT
					WHERE TCDT.GiaTriThayDoi <> 0
				
					
				--2. THAY DOI TANG
				INSERT INTO dbo.ThucChayDaTinhAdmarket
				        ( ThucChayDaTinhID ,
				          HopDongID ,
				          SoHopDong ,
				          DmMaHopDongREF ,
				          TenMaHopDong ,
				          NgayDanhSoHopDong ,
				          NgayKyHopDong ,
				          NhanHopDong ,
				          NgayNhanBanFax ,
				          NgayNhanHopDongBanCung ,
				          NgayChuyenHopDongChoKeToan ,
				          So ,
				          Thang ,
				          Nam ,
				          GiaTriHopDong ,
				          CongNo ,
				          HopDongChiTietREF ,
				          DangSuDung ,
				          IsGiayPhep ,
				          TrangThaiHopDong ,
				          IsBanCung ,
				          DmPhongBanREF ,
				          TenPhongBan ,
				          DmBoPhanREF ,
				          TenBoPhan ,
				          DmNhomLamViecREF ,
				          TenNhomLamViec ,
				          DmDiaDiemLamViecREF ,
				          TenDiaDiemLamViec ,
				          SysNhanVienREF ,
				          TenDangNhap ,
				          TenNhanVien ,
				          TenKhachHang ,
				          NhanHang ,
				          DmNhomNganhREF ,
				          TenNhomNganh ,
				          DmHinhThucQuangCao ,
				          TenHinhThucQuangCao ,
				          DmSanPhamREF ,
				          TenSanPham ,
				          DmNhomWebsiteREF ,
				          TenNhomWebsite ,
				          DmChuyenMucREF ,
				          TenChuyenMuc ,
				          DmLoaiBannerREF ,
				          TenLoaiBanner ,
				          DmViTriREF ,
				          TenViTri ,
				          DotChayHopDong ,
				          SoLuongDotChayHD ,
				          DotChayBooking ,
				          SoLuongDotChayBooking ,
				          SoLuong ,
				          DonViTinh ,
				          DonGia ,
				          DonGiaTheoDonVi ,
				          ChietKhau ,
				          GiamGia ,
				          ThanhTien ,
				          TiLeTuVan ,
				          ChiPhiTuVan ,
				          IsKhuyenMai ,
				          KhuyenMai ,
				          DmBannerREF ,
				          DmChienDichREF ,
				          DmWebsiteREF ,
				          TenWebsite ,
				          TongViewThucChay ,
				          TongClickThucChay ,
				          TongSoBaiViet ,
				          SoLuongThucChay ,
				          NgayThucHien ,
				          GiaTriThayDoi ,
				          ThanhTienThucChayTruocTrietKhau ,
				          GiaTriTrietKhauThucChay ,
				          ThanhTienSauTrietKhauThucChay ,
				          GiaTriHoaHongThucChay ,
				          ThanhTienThucThu ,
				          ThanhTienKM ,
				          SoLuongThucChayKM ,
				          SoLuongThucChayLechTreoHa ,
				          ThanhTienLechTreoHa ,
				          CreatedAt ,
				          LastModifiedAt ,
				          IsPheDuyet ,
				          PheDuyetBy ,
				          PheDuyetAt ,
				          SoLuongThayDoi ,
				          SoLuongKMThayDoi ,
				          GiaTriKMThayDoi ,
				          GhiChu
				        )
				
				SELECT * FROM
				(
						SELECT newid() AS ID
						,[HopDongID]
						,[SoHopDong]
						, DmMaHopDongREF
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
						,[NhanHang] --nhan hang       
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
						,'' [DotChayHopDong]
						,0 [SoLuongDotChayHD]
						,'HDBAN_INVENTORY' [DotChayBooking]
						,'' [SoLuongDotChayBooking]
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
						,@ThanhTien_HopDongChiTiet GiaTriThayDoi
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
						, SoLuong [SoLuongThayDoi]
						,0[SoLuongKMThayDoi]
						,0[GiaTriKMThayDoi]
						,(@Note + 'Chay lai thuc chay ') Note
						FROM [dbo].[ThucChayDaTinhAdmarket]
						where HopDongID = @HopDongREF AND HopDongChiTietREF = @HopDongChiTietID
    					AND NgayThucHien < @NgayThucHien
						GROUP BY
						[HopDongID]
						,[SoHopDong]
						,DmMaHopDongREF
						,TenMaHopDong
						,NgayDanhSoHopDong
						,[NgayKyHopDong]
						,[NhanHopDong]
						,[NgayNhanBanFax]
						,SysNhanVienREF
						, TenNhanVien
						, TenKhachHang
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
						,[TenDangNhap]
						, DmHinhThucQuangCao
						, TenHinhThucQuangCao
						,[NhanHang]
						,[DmNhomNganhREF]
						,[TenNhomNganh]
						, DmSanPhamREF
						, TenSanPham
						,[DmNhomWebsiteREF]
						,[TenNhomWebsite]
						,[DmChuyenMucREF]
						,[TenChuyenMuc]
						,[DmLoaiBannerREF]
						,[TenLoaiBanner]
						,[DmViTriREF]
						,[TenViTri]
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
				)TCDT
				WHERE TCDT.GiaTriThayDoi <> 0
				END
				END
			FETCH NEXT FROM Record_Cursor into @HopDongREF, @SoHopDong, @DmSanPhamREF, @HopDongChiTietID
			END
	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor
	SELECT '1'
END


```
