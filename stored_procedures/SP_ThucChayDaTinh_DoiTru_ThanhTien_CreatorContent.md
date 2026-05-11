# Stored Procedure: `ThucChayDaTinh_DoiTru_ThanhTien_CreatorContent`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-25 16:30:12.210000
- **Ngày sửa cuối**: 2021-06-25 16:30:12.210000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayGhiNhanThucChay` | `datetime(8)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@ghiChuDoiTru` | `nvarchar(1024)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChayDaTinh_DoiTru_ThanhTien_CreatorContent]
	@NgayGhiNhanThucChay				DATETIME,
	@HopDongREF							INT,
	@HopDongChiTietREF					INT,
	@ghiChuDoiTru						NVARCHAR(512)

AS
BEGIN
	DECLARE @NgayGioiHanTinh DATETIME  = '2020-01-01'
	, @NgayGioiHanTinh_HDCT DATETIME = '2020-01-01'
	, @Ghichu_DotChayHopDong NVARCHAR(200) = N'ThanhTien_CreatorContent'


	print @NgayGhiNhanThucChay
	print @HopDongREF
	print @HopDongChiTietREF

	INSERT INTO dbo.ThucChayDaTinh
	(
			ThucChayDaTinhID,										-- id bản ghi
			HopDongID,												-- HĐ
			SoHopDong,		   										-- HĐ
			DmMaHopDongREF,											-- HĐ
			TenMaHopDong,											-- HĐ		
			NgayDanhSoHopDong,										-- HĐ	
			NgayKyHopDong,											-- HĐ	
			NhanHopDong,											-- HĐ	
			NgayNhanBanFax,											-- HĐ	
			NgayNhanHopDongBanCung,									-- HĐ	
			NgayChuyenHopDongChoKeToan,								-- HĐ	
			So,														-- HĐ	
			Thang,													-- HĐ	
			Nam,													-- HĐ	
			GiaTriHopDong,											-- HĐ	
			CongNo,													-- HĐ	
			HopDongChiTietREF,										-- HĐ	
			DangSuDung,												-- HĐ	
			IsGiayPhep,												-- HĐ	
			TrangThaiHopDong,										-- Thay đổi	: 2
			IsBanCung,												-- HĐ	
			DmPhongBanREF,											-- HĐ	
			TenPhongBan,											-- HĐ	
			DmBoPhanREF,											-- HĐ
			TenBoPhan,												-- HĐ
			DmNhomLamViecREF,										-- HĐ
			TenNhomLamViec,											-- HĐ
			DmDiaDiemLamViecREF,									-- HĐ
			TenDiaDiemLamViec,										-- HĐ
			SysNhanVienREF,											-- HĐ
			TenDangNhap,											-- HĐ
			TenNhanVien,											-- HĐ
			TenKhachHang,											-- HĐ
			NhanHang,												-- HĐCT
			DmNhomNganhREF,											-- HĐCT
			TenNhomNganh,											-- HĐCT
			DmHinhThucQuangCao,										-- HĐCT
			TenHinhThucQuangCao,									-- HĐCT
			DmSanPhamREF,											-- HĐCT
			TenSanPham,												-- HĐCT
			DmNhomWebsiteREF,										-- HĐCT
			TenNhomWebsite,											-- HĐCT
			DmChuyenMucREF,											-- HĐCT
			TenChuyenMuc,											-- HĐCT
			DmLoaiBannerREF,										-- HĐCT
			TenLoaiBanner,											-- HĐCT
			DmViTriREF,												-- HĐCT
			TenViTri,												-- HĐCT
			DotChayHopDong,											-- ghi chú
			SoLuongDotChayHD,										-- 0      ??????????????????????
			DotChayBooking,											-- id thực chạy bán
			SoLuongDotChayBooking,									-- id thực chạy bán
			SoLuong,												-- HĐCT
			DonViTinh,												-- TC
			DonGia,													-- HĐCT
			DonGiaTheoDonVi,										-- HĐCT
			ChietKhau,												-- HĐCT
			GiamGia,												-- HĐCT
			ThanhTien,												-- HĐCT
			TiLeTuVan,												-- HĐCT
			ChiPhiTuVan,											-- HĐCT
			IsKhuyenMai,											-- HĐCT <=> chiết khấu = 100
			KhuyenMai,												-- HĐCT
			DmBannerREF,											-- HĐCT
			DmChienDichREF,											-- 0
			DmWebsiteREF,											-- HĐCT
			TenWebsite,											    -- HĐCT
			TongViewThucChay,									    -- 0
			TongClickThucChay,									    -- 0
			TongSoBaiViet,										    -- 0
			SoLuongThucChay,										-- TC:  nếu phân bổ khuyến mại  thì không ghi nhận => 0
			NgayThucHien,											-- @NgayThucHien
			GiaTriThayDoi,											-- 0
			ThanhTienThucChayTruocTrietKhau,						-- nếu phân bổ khuyến mai thì = ?????
			GiaTriTrietKhauThucChay,								-- nếu phân bổ khuyến mại thì = ????
			ThanhTienSauTrietKhauThucChay,							
			GiaTriHoaHongThucChay,									-- 0
			ThanhTienThucThu,										-- TCB Sau CK
			ThanhTienKM,											-- thành tiền TC của HĐKM , nếu phân bổ KM thì tính => TCBSCK              
			SoLuongThucChayKM,										-- SL TC của HĐKM , nếu phân bổ KM thì tính => SLTC 
			SoLuongThucChayLechTreoHa,								-- số lượng TC vượt hợp đồng
			ThanhTienLechTreoHa,									-- thành tiền thực chạy vượt hợp đồng
			CreatedAt,												-- GETDATE()
			LastModifiedAt,											-- GETDATE()
			IsPheDuyet,												-- ''
			PheDuyetBy,												-- ''
			PheDuyetAt,												-- ''
			SoLuongThayDoi,											-- 0
			SoLuongKMThayDoi,										-- 0
			GiaTriKMThayDoi,										-- 0
			GhiChu													-- @ghichu
		)

	

	SELECT NEWID() AS ThucChayDaTinhID, 
			tcdt.HopDongID,														
			tcdt.SoHopDong,		   												
			tcdt.DmMaHopDongREF,														
			tcdt.TenMaHopDong,														
			tcdt.NgayDanhSoHopDong,														
			tcdt.NgayKyHopDong,														
			tcdt.NhanHopDong,														
			tcdt.NgayNhanBanFax,														
			tcdt.NgayNhanHopDongBanCung,														
			tcdt.NgayChuyenHopDongChoKeToan,														
			tcdt.So,														
			tcdt.Thang,														
			tcdt.Nam,														
			tcdt.GiaTriHopDong,														
			tcdt.CongNo,														
			tcdt.HopDongChiTietREF,														
			tcdt.DangSuDung,														
			tcdt.IsGiayPhep,														
			tcdt.TrangThaiHopDong,											
			tcdt.IsBanCung,														
			tcdt.DmPhongBanREF,														
			tcdt.TenPhongBan,														
			tcdt.DmBoPhanREF,														
			tcdt.TenBoPhan,														
			tcdt.DmNhomLamViecREF,														
			tcdt.TenNhomLamViec,														
			tcdt.DmDiaDiemLamViecREF,														
			tcdt.TenDiaDiemLamViec,														
			tcdt.SysNhanVienREF,														
			tcdt.TenDangNhap,														
			tcdt.TenNhanVien,														
			tcdt.TenKhachHang,														
			tcdt.NhanHang,														
			tcdt.DmNhomNganhREF,														
			tcdt.TenNhomNganh,														
			tcdt.DmHinhThucQuangCao,														
			tcdt.TenHinhThucQuangCao,														
			tcdt.DmSanPhamREF,														
			tcdt.TenSanPham,														
			tcdt.DmNhomWebsiteREF,														
			tcdt.TenNhomWebsite,														
			tcdt.DmChuyenMucREF,														
			tcdt.TenChuyenMuc,														
			tcdt.DmLoaiBannerREF,														
			tcdt.TenLoaiBanner,														
			tcdt.DmViTriREF,														
			tcdt.TenViTri,														
			tcdt.DotChayHopDong,														
			tcdt.SoLuongDotChayHD,										-- 0      ??????????????????????				
			tcdt.DotChayBooking,														
			tcdt.SoLuongDotChayBooking,														
			tcdt.SoLuong,														
			tcdt.DonViTinh,														
			tcdt.DonGia,														
			tcdt.DonGiaTheoDonVi,														
			tcdt.ChietKhau,														
			tcdt.GiamGia,														
			tcdt.ThanhTien,														
			tcdt.TiLeTuVan,														
			tcdt.ChiPhiTuVan,														
			tcdt.IsKhuyenMai,											-- HĐCT <=> chiết khấu = 100			
			tcdt.KhuyenMai,														
			tcdt.DmBannerREF,														
			tcdt.DmChienDichREF,											
			tcdt.DmWebsiteREF,														
			tcdt.TenWebsite,											    -- HĐCT			
			0 AS TongViewThucChay,									    -- 0					
			0 AS TongClickThucChay,									    -- 0					
			0 AS TongSoBaiViet,										    -- 0				
			0 AS SoLuongThucChay,										-- TC:  nếu phân bổ khuyến mại  thì không ghi nhận => 0				
			@NgayGhiNhanThucChay NgayThucHien,											-- @NgayThucHien			
			-SUM(tcdt.GiaTriThayDoi	 + tcdt.ThanhTienSauTrietKhauThucChay)	AS GiaTriThayDoi,										
			0 AS ThanhTienThucChayTruocTrietKhau,						-- nếu phân bổ khuyến mai thì = ?????								
			0 AS GiaTriTrietKhauThucChay,								-- nếu phân bổ khuyến mại thì = ????						
			0 AS ThanhTienSauTrietKhauThucChay,														
			0 AS GiaTriHoaHongThucChay,												
			0 AS ThanhTienThucThu,														
			0 AS ThanhTienKM,											-- thành tiền TC của HĐKM , nếu phân bổ KM thì tính => TCBSCK              			
			0 AS SoLuongThucChayKM,										-- SL TC của HĐKM , nếu phân bổ KM thì tính => SLTC 				
			-SUM(SoLuongThucChayLechTreoHa) AS SoLuongThucChayLechTreoHa,														
			-SUM(ThanhTienLechTreoHa) AS ThanhTienLechTreoHa,														
			GETDATE() AS CreatedAt,														
			GETDATE() AS LastModifiedAt,														
			0 IsPheDuyet,												-- ''		
			'' PheDuyetBy,												-- ''		
			GETDATE() AS PheDuyetAt,												-- ''		
			-SUM(tcdt.SoLuongThucChay  + tcdt.SoLuongThayDoi) AS SoLuongThayDoi,														
			-SUM(tcdt.SoLuongKMThayDoi + tcdt.SoLuongThucChayKM) AS SoLuongKMThayDoi,													
			-SUM(tcdt.GiaTriKMThayDoi + tcdt.ThanhTienKM) AS GiaTriKMThayDoi,													
			@ghiChuDoiTru AS GhiChu												-- @ghichu	
			FROM dbo.ThucChayDaTinh tcdt
			WHERE tcdt.HopDongID = @HopDongREF
			AND tcdt.HopDongChiTietREF = @HopDongChiTietREF
			AND tcdt.NgayThucHien <= @NgayGhiNhanThucChay
			AND tcdt.NgayThucHien >= @NgayGioiHanTinh_HDCT
			AND tcdt.DotChayHopDong = @Ghichu_DotChayHopDong
			GROUP BY
			tcdt.HopDongID,														
			tcdt.SoHopDong,		   												
			tcdt.DmMaHopDongREF,														
			tcdt.TenMaHopDong,														
			tcdt.NgayDanhSoHopDong,														
			tcdt.NgayKyHopDong,														
			tcdt.NhanHopDong,														
			tcdt.NgayNhanBanFax,														
			tcdt.NgayNhanHopDongBanCung,														
			tcdt.NgayChuyenHopDongChoKeToan,														
			tcdt.So,														
			tcdt.Thang,														
			tcdt.Nam,														
			tcdt.GiaTriHopDong,														
			tcdt.CongNo,														
			tcdt.HopDongChiTietREF,														
			tcdt.DangSuDung,														
			tcdt.IsGiayPhep,														
			tcdt.TrangThaiHopDong,											
			tcdt.IsBanCung,														
			tcdt.DmPhongBanREF,														
			tcdt.TenPhongBan,														
			tcdt.DmBoPhanREF,														
			tcdt.TenBoPhan,														
			tcdt.DmNhomLamViecREF,														
			tcdt.TenNhomLamViec,														
			tcdt.DmDiaDiemLamViecREF,														
			tcdt.TenDiaDiemLamViec,														
			tcdt.SysNhanVienREF,														
			tcdt.TenDangNhap,														
			tcdt.TenNhanVien,														
			tcdt.TenKhachHang,														
			tcdt.NhanHang,														
			tcdt.DmNhomNganhREF,														
			tcdt.TenNhomNganh,														
			tcdt.DmHinhThucQuangCao,														
			tcdt.TenHinhThucQuangCao,														
			tcdt.DmSanPhamREF,														
			tcdt.TenSanPham,														
			tcdt.DmNhomWebsiteREF,														
			tcdt.TenNhomWebsite,														
			tcdt.DmChuyenMucREF,														
			tcdt.TenChuyenMuc,														
			tcdt.DmLoaiBannerREF,														
			tcdt.TenLoaiBanner,														
			tcdt.DmViTriREF,														
			tcdt.TenViTri,														
			tcdt.DotChayHopDong,														
			tcdt.SoLuongDotChayHD,										-- 0      ??????????????????????				
			tcdt.DotChayBooking,														
			tcdt.SoLuongDotChayBooking,														
			tcdt.SoLuong,														
			tcdt.DonViTinh,														
			tcdt.DonGia,														
			tcdt.DonGiaTheoDonVi,														
			tcdt.ChietKhau,														
			tcdt.GiamGia,														
			tcdt.ThanhTien,														
			tcdt.TiLeTuVan,														
			tcdt.ChiPhiTuVan,														
			tcdt.IsKhuyenMai,											-- HĐCT <=> chiết khấu = 100			
			tcdt.KhuyenMai,														
			tcdt.DmBannerREF,														
			tcdt.DmChienDichREF,											
			tcdt.DmWebsiteREF,														
			tcdt.TenWebsite
			HAVING (SUM(ThanhTienLechTreoHa) <> 0
			OR SUM(tcdt.GiaTriThayDoi	 + tcdt.ThanhTienSauTrietKhauThucChay) <> 0
			OR SUM(tcdt.GiaTriKMThayDoi + tcdt.ThanhTienKM) <> 0)
END


 
```
