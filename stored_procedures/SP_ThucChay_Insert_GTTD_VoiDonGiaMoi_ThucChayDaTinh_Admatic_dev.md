# Stored Procedure: `ThucChay_Insert_GTTD_VoiDonGiaMoi_ThucChayDaTinh_Admatic_dev`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-08-07 11:02:13.447000
- **Ngày sửa cuối**: 2017-09-07 17:07:13.343000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@DmBannerID` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE  PROCEDURE [dbo].[ThucChay_Insert_GTTD_VoiDonGiaMoi_ThucChayDaTinh_Admatic_dev] 
	@NgayThucHien DATETIME,
	@HopDongID INT, 
	@HopDongChiTietID INT,
	@DmBannerID INT,
	@DmWebsiteREF INT
AS
BEGIN
	DECLARE @Note NVARCHAR(500) = N'ADMATIC_DonGia_TD_GTTD Tăng với đơn giá mới '
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
	SELECT  NEWID() ThucChayDaTinhID ,
	          tcdt.HopDongID ,
	          tcdt.SoHopDong ,
	          tcdt.DmMaHopDongREF ,
	          tcdt.TenMaHopDong ,
	          tcdt.NgayDanhSoHopDong ,
	          tcdt.NgayKyHopDong ,
	          tcdt.NhanHopDong ,
	          tcdt.NgayNhanBanFax ,
	          tcdt.NgayNhanHopDongBanCung ,
	          tcdt.NgayChuyenHopDongChoKeToan ,
	          tcdt.So ,
	          tcdt.Thang ,
	          tcdt.Nam ,
	          tcdt.GiaTriHopDong ,
	          tcdt.CongNo ,
	          tcdt.HopDongChiTietREF ,
	          tcdt.DangSuDung ,
	          tcdt.IsGiayPhep ,
	          tcdt.TrangThaiHopDong ,
	          tcdt.IsBanCung ,
	          tcdt.DmPhongBanREF ,
	          tcdt.TenPhongBan ,
	          tcdt.DmBoPhanREF ,
	          tcdt.TenBoPhan ,
	          tcdt.DmNhomLamViecREF ,
	          tcdt.TenNhomLamViec ,
	          tcdt.DmDiaDiemLamViecREF ,
	          tcdt.TenDiaDiemLamViec ,
	          tcdt.SysNhanVienREF ,
	          tcdt.TenDangNhap ,
	          tcdt.TenNhanVien ,
	          tcdt.TenKhachHang ,
	          hdct.DanhSachNhanHangREF AS NhanHang ,
	          tcdt.DmNhomNganhREF ,
	          tcdt.TenNhomNganh ,
	          tcdt.DmHinhThucQuangCao ,
	          tcdt.TenHinhThucQuangCao ,
	          tcdt.DmSanPhamREF ,
	          tcdt.TenSanPham ,
	          tcdt.DmNhomWebsiteREF ,
	          tcdt.TenNhomWebsite ,
	          tcdt.DmChuyenMucREF ,
	          tcdt.TenChuyenMuc ,
	          tcdt.DmLoaiBannerREF ,
	          tcdt.TenLoaiBanner ,
	          tcdt.DmViTriREF ,
	          tcdt.TenViTri ,
	          tcdt.DotChayHopDong ,
	          tcdt.SoLuongDotChayHD ,
	          tcdt.DotChayBooking ,
	          tcdt.SoLuongDotChayBooking ,
	          tcdt.SoLuong ,
	          tcdt.DonViTinh ,
	          tcdt.DonGia ,
	          (CASE when (tcdt.DonViTinh = 'VIEW') then CONVERT(FLOAT,tt.DonGia_Banner)/1000
					  else  tt.DonGia_Banner
				  END
			  ) AS DonGiaTheoDonVi ,
	          tcdt.ChietKhau ,
	          tcdt.GiamGia ,
	          tcdt.ThanhTien ,
	          tcdt.TiLeTuVan ,
	          tcdt.ChiPhiTuVan ,
	          tcdt.IsKhuyenMai ,
	          tcdt.KhuyenMai ,
	          tcdt.DmBannerREF ,
	          tcdt.DmChienDichREF ,
	          tcdt.DmWebsiteREF ,
	          tcdt.TenWebsite ,
	          0 TongViewThucChay ,
	          0 TongClickThucChay ,
	          0 TongSoBaiViet ,
	          0 SoLuongThucChay ,
	          @NgayThucHien NgayThucHien ,
	          (CASE when (tcdt.DonViTinh = 'VIEW') 
					THEN (CONVERT(FLOAT,tt.DonGia_Banner)/1000)*
					(
						(CASE WHEN ((tcdt.IsKhuyenMai=0) AND (tcdt.DonViTinh = 'VIEW')) 
								OR ((tcdt.IsKhuyenMai=0) AND (tcdt.DonViTinh = 'CLICK')) 
								OR ((tcdt.IsKhuyenMai=0) AND (tcdt.DonViTinh = 'TRUE VIEW')) 
							THEN ISNULL([dbo].[ThucChay_GetSoLuongThucChay_Admatic_v1] (SUM(tcdt.TongViewThucChay),SUM(tcdt.TongClickThucChay),SUM(tcdt.TongSoBaiViet),tt.DonGia_Banner ,tcdt.DonViTinh,@NgayThucHien, tcdt.HopDongChiTietREF,tcdt.SoLuong, tcdt.DonGia, tcdt.ThanhTien, tcdt.ChietKhau),0)
							ELSE 0
						END
						)
					)*(100-tcdt.ChietKhau)/100
					  else  tt.DonGia_Banner*ISNULL([dbo].[ThucChay_GetSoLuongThucChay_Admatic_v1] (SUM(tcdt.TongViewThucChay),SUM(tcdt.TongClickThucChay),SUM(tcdt.TongSoBaiViet),tt.DonGia_Banner ,tcdt.DonViTinh,@NgayThucHien, tcdt.HopDongChiTietREF,tcdt.SoLuong, tcdt.DonGia, tcdt.ThanhTien, tcdt.ChietKhau),0)*(100-tcdt.ChietKhau)/100
				  END
			  ) GiaTriThayDoi ,--GIA TRI THAY DOI
	          0 ThanhTienThucChayTruocTrietKhau ,
	          0 GiaTriTrietKhauThucChay ,
	          0 ThanhTienSauTrietKhauThucChay ,
	          0 GiaTriHoaHongThucChay ,
	          0 ThanhTienThucThu ,
	          0 ThanhTienKM ,
	          0 SoLuongThucChayKM ,
	          0 SoLuongThucChayLechTreoHa ,
	          0 ThanhTienLechTreoHa ,
	          GETDATE() CreatedAt ,
	          GETDATE() LastModifiedAt ,
	          0 IsPheDuyet ,
	          '' PheDuyetBy ,
	          NULL PheDuyetAt ,
	          ISNULL([dbo].[ThucChay_GetSoLuongThucChay_Admatic_v1] (SUM(tcdt.TongViewThucChay),SUM(tcdt.TongClickThucChay),SUM(tcdt.TongSoBaiViet),tt.DonGia_Banner ,tcdt.DonViTinh,@NgayThucHien, tcdt.HopDongChiTietREF,tcdt.SoLuong, tcdt.DonGia, tcdt.ThanhTien, tcdt.ChietKhau),0) SoLuongThayDoi , --SOLUONG THAY DOI
	          0 SoLuongKMThayDoi ,
	          0 GiaTriKMThayDoi ,
	          @Note GhiChu
	        FROM dbo.ThucChayDaTinh tcdt
			INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
			LEFT JOIN 
			(
				SELECT DISTINCT HopDongREF, DmBannerID, DonGia_Banner FROM  dbo.ThucChayHopDongChiTietAndBanner_Admatic
			) tt ON tcdt.HopDongID = tt.HopDongREF
			AND CONVERT(INT,tt.DmBannerID) = tcdt.DmBannerREF
			WHERE 1=1
			AND tcdt.HopDongID = @HopDongID
			AND tcdt.HopDongChiTietREF = @HopDongChiTietID
			AND tcdt.NgayThucHien < @NgayThucHien
			AND tcdt.DmBannerREF = @DmBannerID
			AND tcdt.DmWebsiteREF = @DmWebsiteREF
			GROUP BY
			  tcdt.HopDongID ,
	          tcdt.SoHopDong ,
	          tcdt.DmMaHopDongREF ,
	          tcdt.TenMaHopDong ,
	          tcdt.NgayDanhSoHopDong ,
	          tcdt.NgayKyHopDong ,
	          tcdt.NhanHopDong ,
	          tcdt.NgayNhanBanFax ,
	          tcdt.NgayNhanHopDongBanCung ,
	          tcdt.NgayChuyenHopDongChoKeToan ,
	          tcdt.So ,
	          tcdt.Thang ,
	          tcdt.Nam ,
	          tcdt.GiaTriHopDong ,
	          tcdt.CongNo ,
	          tcdt.HopDongChiTietREF ,
	          tcdt.DangSuDung ,
	          tcdt.IsGiayPhep ,
	          tcdt.TrangThaiHopDong ,
	          tcdt.IsBanCung ,
	          tcdt.DmPhongBanREF ,
	          tcdt.TenPhongBan ,
	          tcdt.DmBoPhanREF ,
	          tcdt.TenBoPhan ,
	          tcdt.DmNhomLamViecREF ,
	          tcdt.TenNhomLamViec ,
	          tcdt.DmDiaDiemLamViecREF ,
	          tcdt.TenDiaDiemLamViec ,
	          tcdt.SysNhanVienREF ,
	          tcdt.TenDangNhap ,
	          tcdt.TenNhanVien ,
	          tcdt.TenKhachHang ,
	          hdct.DanhSachNhanHangREF   ,--NhanHang
	          tcdt.DmNhomNganhREF ,
	          tcdt.TenNhomNganh ,
	          tcdt.DmHinhThucQuangCao ,
	          tcdt.TenHinhThucQuangCao ,
	          tcdt.DmSanPhamREF ,
	          tcdt.TenSanPham ,
	          tcdt.DmNhomWebsiteREF ,
	          tcdt.TenNhomWebsite ,
	          tcdt.DmChuyenMucREF ,
	          tcdt.TenChuyenMuc ,
	          tcdt.DmLoaiBannerREF ,
	          tcdt.TenLoaiBanner ,
	          tcdt.DmViTriREF ,
	          tcdt.TenViTri ,
	          tcdt.DotChayHopDong ,
	          tcdt.SoLuongDotChayHD ,
	          tcdt.DotChayBooking ,
	          tcdt.SoLuongDotChayBooking ,
	          tcdt.SoLuong ,
	          tcdt.DonViTinh ,
	          tcdt.DonGia ,
	          tt.DonGia_Banner ,
	          tcdt.ChietKhau ,
	          tcdt.GiamGia ,
	          tcdt.ThanhTien ,
	          tcdt.TiLeTuVan ,
	          tcdt.ChiPhiTuVan ,
	          tcdt.IsKhuyenMai ,
	          tcdt.KhuyenMai ,
	          tcdt.DmBannerREF ,
	          tcdt.DmChienDichREF ,
	          tcdt.DmWebsiteREF ,
	          tcdt.TenWebsite 
        
END



```
