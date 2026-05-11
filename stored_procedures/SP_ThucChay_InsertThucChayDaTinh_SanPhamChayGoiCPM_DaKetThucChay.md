# Stored Procedure: `ThucChay_InsertThucChayDaTinh_SanPhamChayGoiCPM_DaKetThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-12-17 15:26:53.567000
- **Ngày sửa cuối**: 2018-12-17 15:29:06.037000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC [dbo].[ThucChay_InsertThucChayDaTinh_SanPhamChayGoiCPM_DaKetThucChay] 
	@NgayThucHien DATETIME,
	@SoHopDong NVARCHAR(50),
	@HopDongChiTietID INT,
	@DmSanPhamREF INT
*/


CREATE  PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_SanPhamChayGoiCPM_DaKetThucChay] 
	@NgayThucHien DATETIME,
	@SoHopDong NVARCHAR(50),
	@HopDongChiTietID INT,
	@DmSanPhamREF INT

AS
BEGIN
	DECLARE  @TongViewThucChayHDCT BIGINT = 0
	, @TypeProduct INT = 0, @Note NVARCHAR(max) = ''

	SET @Note = N'Xử lý hợp đồng chạy goi san phẩm đã kết thúc chạy :' + @SoHopDong

	SET @TypeProduct = [dbo].[GetDmSanPhamIDByTypeProductID](@DmSanPhamREF)

	SET @TongViewThucChayHDCT = ISNULL((SELECT  SUM(TongViewThucChay)TongViewThucChay
	FROM dbo.ThucChay
	WHERE SoHopDong = @SoHopDong
	AND EXISTS (SELECT DmBannerID FROM dbo.ThucChayHopDongChiTietAndBanner WHERE HopDongChiTietREF = @HopDongChiTietID
	AND DmBannerID = CONVERT(NVARCHAR(100),DmBannerREF))
	AND TypeProduct = @TypeProduct),0)

INSERT INTO dbo.ThucChayDaTinh
(
    ThucChayDaTinhID,
    HopDongID,
    SoHopDong,
    DmMaHopDongREF,
    TenMaHopDong,
    NgayDanhSoHopDong,
    NgayKyHopDong,
    NhanHopDong,
    NgayNhanBanFax,
    NgayNhanHopDongBanCung,
    NgayChuyenHopDongChoKeToan,
    So,
    Thang,
    Nam,
    GiaTriHopDong,
    CongNo,
    HopDongChiTietREF,
    DangSuDung,
    IsGiayPhep,
    TrangThaiHopDong,
    IsBanCung,
    DmPhongBanREF,
    TenPhongBan,
    DmBoPhanREF,
    TenBoPhan,
    DmNhomLamViecREF,
    TenNhomLamViec,
    DmDiaDiemLamViecREF,
    TenDiaDiemLamViec,
    SysNhanVienREF,
    TenDangNhap,
    TenNhanVien,
    TenKhachHang,
    NhanHang,
    DmNhomNganhREF,
    TenNhomNganh,
    DmHinhThucQuangCao,
    TenHinhThucQuangCao,
    DmSanPhamREF,
    TenSanPham,
    DmNhomWebsiteREF,
    TenNhomWebsite,
    DmChuyenMucREF,
    TenChuyenMuc,
    DmLoaiBannerREF,
    TenLoaiBanner,
    DmViTriREF,
    TenViTri,
    DotChayHopDong,
    SoLuongDotChayHD,
    DotChayBooking,
    SoLuongDotChayBooking,
    SoLuong,
    DonViTinh,
    DonGia,
    DonGiaTheoDonVi,
    ChietKhau,
    GiamGia,
    ThanhTien,
    TiLeTuVan,
    ChiPhiTuVan,
    IsKhuyenMai,
    KhuyenMai,
    DmBannerREF,
    DmChienDichREF,
    DmWebsiteREF,
    TenWebsite,
    TongViewThucChay,
    TongClickThucChay,
    TongSoBaiViet,
    SoLuongThucChay,
    NgayThucHien,
    GiaTriThayDoi,
    ThanhTienThucChayTruocTrietKhau,
    GiaTriTrietKhauThucChay,
    ThanhTienSauTrietKhauThucChay,
    GiaTriHoaHongThucChay,
    ThanhTienThucThu,
    ThanhTienKM,
    SoLuongThucChayKM,
    SoLuongThucChayLechTreoHa,
    ThanhTienLechTreoHa,
    CreatedAt,
    LastModifiedAt,
    IsPheDuyet,
    PheDuyetBy,
    PheDuyetAt,
    SoLuongThayDoi,
    SoLuongKMThayDoi,
    GiaTriKMThayDoi,
    GhiChu
)

SELECT  NEWID(), TD.*, 
	ISNULL(((TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) AS GiaTriTrietKhauThucChay,
	ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) AS ThanhTienSauTrietKhauThucChay,
	ISNULL((((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS GiaTriHoaHongThucChay,
	ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100 - ((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS ThanhTienThucThu,
	(CASE when TD.IsKhuyenMai=1 then TD.ThanhTienThucChayTruocTrietKhau
		else 0
	  END
	) as ThanhTienKM,
	(CASE when (((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100))AND (TD.DonViTinh = 'VIEW')) then ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(TD.TongViewThucChay,TD.SoLuong,TD.DonViTinh, TD.NgayThucHien, TD.HopDongChiTietREF),0)
		when (((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100))AND (TD.DonViTinh = 'CLICK')) then ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(TD.TongClickThucChay,TD.SoLuong,TD.DonViTinh, TD.NgayThucHien, TD.HopDongChiTietREF),0)
		else 0
	  END
	) as SoLuongThucChayKM,
	0 AS SoLuongLechTreoHa,
	0 AS ThanhTienLechTreoHa,
	GETDATE(),
	GETDATE(),
	0 IsPheDuyet,
	'' PheDuyetBy,
	'' PheDuyetAt,
	0 SoLuongThayDoi,
	0 SoLuongKMThayDoi,
	0 GiaTriKMThayDoi,
	@Note GhiChu	
	FROM 
	(
		SELECT 
		D.HopDongID,
		D.SoHopDong, 
		D.DmMaHopDongREF, 
		D.TenMaHopDong, 
		D.NgayDanhSoHopDong, D.NgayKyHopDong, 
		D.NhanHopDong, D.NgayNhanBanFax, D.NgayNhanHopDongBanCung, D.NgayChuyenHopDongChoKeToan, 
		D.So, D.Thang, D.Nam, 
		D.GiaTriHopDong, D.CongNo,
		A.HopDongChiTietID HopDongChiTietREF,
		D.DangSuDung, D.IsGiayPhep, D.TrangThaiHopDong,D.IsBanCung, 
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
		C.DmSanPhamREF as DmSanPhamREF,
		C.TenSanPham as TenSanPham,  
		C.DmNhomWebsiteREF, 
		C.TenNhomWebsite, 
		C.DmChuyenMucREF, 
		C.TenChuyenMuc, 
		C.DmLoaiBannerREF, 
		C.TenLoaiBanner, 
		C.DmBannerREF DmViTriREF, 
		C.TenViTri, 
		'' DotChayHopDong,
		C.SoLuong AS SoLuongDotChayHD,
		'' DotChayBooking,
		0 SoLuongDotChayBooking, 
		C.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong,
		N'VIEW' as DonViTinh, 
		dbo.ThucChay_GetDonGiaByNgayThucHien(A.NgayThucHien,A.HopDongChiTietID,C.DonGia) as DonGia,
		(CASE WHEN A.TongViewThucChay <> 0 THEN ((C.DonGia*C.SoLuong*A.TiLeView)/A.TongViewThucChay)
		ELSE 0
		END ) AS DonGiaTheoDonViTinh,
		C.ChietKhau, C.GiamGia, C.ThanhTien,
		C.TiLeTuVan,  C.ChiPhiTuVan,
		C.IsKhuyenMai,  
		C.KhuyenMai,
		A.DmBannerREF DmBannerREF,
		0 DmChienDichREF,
		A.DmWebsiteREF,
		A.TenWebsite,
		A.TongViewThucChay,
		A.TongClickThucChay,
		0 TongSoBaiViet,
		(CASE when A.TongViewThucChay <> 0 THEN A.TongViewThucChay
			else 0
		  END
		) as SoLuongThucChay,
		--Thanhuc Tien Thuc Chay
		A.NgayThucHien,
		0 as GiaTriThayDoi,
		--****haidh chinh sua	
		C.DonGia*C.SoLuong*A.TiLeView as ThanhTienThucChayTruocTrietKhau
		from (	
				SELECT tc.SoHopDong, tt.HopDongChiTietID, tc.TypeProduct, @NgayThucHien NgayThucHien, tc.DmBannerREF, tc.DmWebsiteREF, tc.TenWebsite, tc.TongClickThucChay, tc.TongViewThucChay, (CONVERT(FLOAT,tc.TongViewThucChay)/CONVERT(FLOAT,@TongViewThucChayHDCT)) TiLeView FROM
				(
					SELECT SoHopDong, TypeProduct, DmBannerREF, DmWebsiteREF, TenWebsite, SUM(TongViewThucChay)TongViewThucChay, SUM(TongClickThucChay)TongClickThucChay 
					FROM dbo.ThucChay
					WHERE SoHopDong = @SoHopDong
					AND TypeProduct = @TypeProduct
					GROUP BY SoHopDong, TypeProduct, DmBannerREF, DmWebsiteREF, TenWebsite
				)tc
				INNER JOIN 
				(
					SELECT tt.HopDongChiTietREF HopDongChiTietID, tt.DmBannerID, tt.HopDongREF
					FROM
					(
						SELECT HopDongChiTietREF, DmBannerID, HopDongREF FROM dbo.ThucChayHopDongChiTietAndBanner
						WHERE HopDongChiTietREF = @HopDongChiTietID
						AND DeletedStatus = 0
						GROUP BY HopDongChiTietREF, DmBannerID, HopDongREF
					)tt
				)tt ON tc.DmBannerREF = CONVERT(NVARCHAR(50),tt.DmBannerID)
				--XAC DINH TI LE TREN TUNG SITE
		 )A
		 INNER JOIN  (SELECT * FROM dbo.HopDongChiTiet C 
							WHERE 1=1  AND C.DeletedStatus = 0
							 AND C.DmLoaiBannerREF NOT IN (17,18)--Khong tinh cho cac loai banner ChiPhi va Mua ngoai
							 AND C.DmLoaiREF <> 13 --Khong tinh thuc chay cho HTQC Mua Ngoai
							 AND C.DmLoaiREF <> 42
							 AND C.HopDongChiTietID = @HopDongChiTietID
							 AND C.DmSanPhamREF = @DmSanPhamREF
							 AND C.DonViTinhREF <> 31
		 )C ON C.HopDongChiTietID = A.HopDongChiTietID
		 INNER JOIN (SELECT * FROM dbo.HopDong WHERE SoHopDong = @SoHopDong AND TrangThaiHopDong <> 3)D ON D.HopDongID = C.HopDongFK
		 WHERE 1=1
	
	) TD
	
END

```
