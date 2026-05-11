# Stored Procedure: `native_goi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-01-02 18:30:53.320000
- **Ngày sửa cuối**: 2021-01-02 18:32:24.550000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChitietID` | `int(4)` | No |
| `@sltc` | `int(4)` | No |
| `@Giatrithaydoi` | `float(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE native_goi 
	-- Add the parameters for the stored procedure here
	
@NgayThucHien datetime ,
@HopDongChitietID int,
@sltc int ,
@Giatrithaydoi float
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	INSERT INTO dbo.ThucChayDaTinh 
			SELECT  NEWID(), TD.*, 
			ISNULL((TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100,0) AS GiaTriTrietKhauThucChay,
			 0 AS ThanhTienSauTrietKhauThucChay,	
			ISNULL(((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100,0) AS GiaTriHoaHongThucChay,
			0,----ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100 - ((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS ThanhTienThucThu,
			(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then TD.ThanhTienThucChayTruocTrietKhau
				else 0
			  END
			) as ThanhTienKM,
			(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then TD.Soluong
				else 0
			  END
			) as SoLuongThucChayKM,
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
			N' Ghi nhận mail sản phẩm' GhiChu	
			FROM 
			(
			SELECT 
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
			C.HopDongChiTietID,
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
			C.DanhSachNhanHangREF, 
			C.DmNhomNganhREF, 
			C.TenNhomNganh, 
			--Thong tin hinh thuc quang cao
			C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
			--Thong tin San pham
			c.DmSanPhamREF as DmSanPhamREF,
			E.TenSanPham,  
			C.DmNhomWebsiteREF, 
			C.TenNhomWebsite, 
			C.DmChuyenMucREF, 
			C.TenChuyenMuc,
			C.DmLoaiBannerREF, 
			C.TenLoaiBanner, 
			C.DmViTriREF, 
			C.TenViTri, 
			ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'N'),0) DotChayHopDong,
			0 AS SoLuongDotChayHD,		
			ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'N'),0)DotChayBooking,
			dbo.GetSoLuongDotChayBookingByHopDongChiTiet(C.HopDongChiTietID) AS SoLuongDotChayBooking, 
			--Thong tin ve Tien
			C.SoLuong AS SoLuong,	
			isnull(C.DonViTinh, N'đ/v') as DonViTinh, 
			dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,c.HopDongChiTietID,C.DonGia) as DonGia, 
			dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,c.HopDongChiTietID,C.DonGia) AS DonGiaTheoDonViTinh,
			C.ChietKhau, C.GiamGia, C.ThanhTien,
			C.TiLeTuVan,  C.ChiPhiTuVan,
			C.IsKhuyenMai,  
			C.KhuyenMai,
			--Thuc chay
			0 DmBannerREF,--A.DmBannerREF,
			0 DmChienDichREF,--A.DmChienDichREF,
			dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF) DmWebsiteREF,
			--A.DmWebsiteREF,
			dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,C.TenWebsite) TenWebsite,
			--C.TenWebsite,
			--A.SoHopDong,
			0 TongViewThucChay,
			0 TongClickThucChay,
			0 TongSoBaiViet,
			@sltc SoLuongThucChay,
			--Thanhuc Tien Thuc Chay
			@NgayThucHien AS NgayThucHien,
			@Giatrithaydoi as GiaTriThayDoi,
			@sltc*C.DonGia as ThanhTienThucChayTruocTrietKhau
			FROM 
			(
				SELECT * FROM HopDongChiTiet 
				WHERE 1=1
				AND DeletedStatus = 0 
   				AND NOT (DmLoaiREF = 13 or DmLoaiBannerREF = 18)	 --Khong tinh thuc chay cho HTQC Mua Ngoai
			) C  
			INNER JOIN  
			 ( 
	 			SELECT * FROM HopDong hd 
				WHERE hd.TrangThaiHopDong <> 3
				AND hd.DeletedStatus = 0
			 ) D on D.HopDongID = C.HopDongFK
			INNER JOIN DmSanPham E ON E.DmSanPhamID = C.DmSanPhamREF 	
			WHERE C.HopDongChiTietID = @HopDongChitietID
			--AND C.HopDongFK = @HopDongID
			AND C.SoLuong >0	 
			) TD
		
			

		
END

```
