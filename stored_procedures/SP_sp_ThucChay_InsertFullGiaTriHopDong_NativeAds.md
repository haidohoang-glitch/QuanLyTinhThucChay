# Stored Procedure: `sp_ThucChay_InsertFullGiaTriHopDong_NativeAds`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-03-12 15:42:14.773000
- **Ngày sửa cuối**: 2021-05-18 14:49:24.363000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChitietID` | `int(4)` | No |
| `@ThanhTienThucChay` | `float(8)` | No |
| `@GhiChu` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql

--exec sp_ThucChay_InsertFullGiaTriHopDong_NativeAds '2021-03-11',1007331,537188,738643.63636364,N'Ghi nhận mail sản phẩm v/v Danh sách hợp đồng sản phẩm Native/OnImage đủ số lượng chưa đủ thực chạy đã tính'


CREATE proc [dbo].[sp_ThucChay_InsertFullGiaTriHopDong_NativeAds]

@NgayThucHien datetime,
@HopDongID int,
@HopDongChitietID int,
@ThanhTienThucChay float,
@GhiChu nvarchar(200)
as
begin 
			declare @shd nvarchar(50), @sanphamid int
			set @shd = (select SoHopDong from HopDong where HopDongID = @HopDongID)
			set @sanphamid =(select DmSanPhamREF from HopDongChiTiet where HopDongChiTietID = @HopDongChiTietID)

			insert into ghinhanthanhly select @shd,@HopDongID,@HopDongChiTietID,@sanphamid,getdate()
			--THUCCHAYDATINH

			INSERT INTO dbo.ThucChayDaTinh 
			SELECT  NEWID(), TD.*, 
			ISNULL((TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100,0) AS GiaTriTrietKhauThucChay,
			@ThanhTienThucChay AS ThanhTienSauTrietKhauThucChay,	
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
			@GhiChu GhiChu	
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
			0 SoLuongThucChay,
			--Thanhuc Tien Thuc Chay
			@NgayThucHien AS NgayThucHien,
			0GiaTriThayDoi,
			0 as ThanhTienThucChayTruocTrietKhau
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
			AND C.HopDongFK = @HopDongID
			AND C.SoLuong >0	 
			) TD
		
			
End
		


		
```
