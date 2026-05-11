# Stored Procedure: `ThucChayDaTinh_MuaNgoai_InsertThucChayLaiMuaNgoai_ThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-05-20 15:11:44.183000
- **Ngày sửa cuối**: 2020-06-05 10:06:48.880000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ThucChayMuaNgoaiChiTietID` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DonViTinhThucChay` | `nvarchar(100)` | No |
| `@ghiChu` | `nvarchar(1024)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMW
-- Create date: 2015-01-12
-- Description:	Insert Thuc chay da tinh mua ngoai by phanBoId
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinh_MuaNgoai_InsertThucChayLaiMuaNgoai_ThayDoi]
	@NgayThucHien						DATETIME,
	@ThucChayMuaNgoaiChiTietID			INT,
	@HopDongREF							INT,
	@HopDongChiTietREF					INT,
	@DonViTinhThucChay					NVARCHAR(50),
	@ghiChu								NVARCHAR(512)
AS
BEGIN
	DECLARE @NgayGioiHanTinh DATETIME = '2013-01-01'
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

   INSERT INTO [dbo].[ThucChayDaTinh_MuaNgoai]
           ([HopDongREF]
           ,[SoHopDong]
           ,[DmMaHopDongREF]
           ,[NgayDanhSoHopDong]
           ,[TrangThaiHopDong]
           ,[DmNhanVienREF]
           ,[TenDangNhap]
           ,[DmPhongBanREF]
           ,[DmBoPhanREF]
           ,[DmNhomLamViecREF]
           ,[DmDiaDiemLamViecREF]
           ,[DmKhachHangREF]
           ,[HopDongChiTietREF]
           ,[LstDmNhanHangREF]
           ,[LstDmNhomNganhREF]
           ,[DmHinhThucQuangCaoREF]
           ,[DmSanPhamREF]
           ,[DmChuyenMucREF]
           ,[DmLoaiBannerREF]
           ,[DmViTriREF]
           ,[SoLuong]
           ,[DonViTinhREF]
           ,[DonGia]
           ,[ChietKhau]
           ,[ThanhTien]
           ,[IsKhuyenMai]
           ,[KhuyenMai]
           ,[ThucChayMuaNgoaiChiTietREF]
		   ,[TongTienDuToanMuaSauCK] 
		   ,[TongTienDuToanLaiMuaSauCK]
           ,[ChietKhauMua]
           ,[DmBannerREF]
           ,[DmChienDichREF]
           ,[DmWebsiteREF]
           ,[TenWebsite]
           ,[NgayThucHien]
           ,[NgayBatDau]
           ,[NgayKetThuc]
           ,[DonViTinhThucChay]
           ,[DonGiaTheoDonViTinhTC]
           ,[TongViewClickThucChay]
           ,[TongSoBaiVietChiPhiThucChay]
           ,[SoLuongThucChay]
           ,[TongThanhTienThucChayBanSauCK]
           ,[TongThanhTienThucChayMuaSauCK]
           ,[ThanhTienLaiThucChaySauCK]
           ,[ThanhTienLaiThucChayKM]
           ,[SoLuongThucChayKM]
           ,[SoLuongThucChayLechTreoHa]
           ,[ThanhTienLechTreoHa]
           ,[GiaTriThayDoiLaiSauCK]
           ,[SoLuongThayDoi]
           ,[SoLuongKMThayDoi]
           ,[GiaTriKMLaiThayDoi]
           ,[GhiChu]
           ,[CreatedAt]
           ,[LastModifiedAt])

     SELECT tcmn.HopDongID, tcmn.SoHopDong, tcmn.DmMaHopDongREF, tcmn.NgayDanhSoHopDong
		, tcmn.TrangThaiHopDong, tcmn.SysNhanVienREF, tcmn.TenDangNhap
		, tcmn.DmPhongBanREF, tcmn.DmBoPhanREF, tcmn.DmNhomLamViecREF, tcmn.DmDiaDiemLamViecREF, tcmn.DmKhachHangREF
		, tcmn.HopDongChiTietID, tcmn.DanhSachNhanHangREF, tcmn.DmNhomNganhREF
		, tcmn.DmLoaiREF, tcmn.DmSanPhamREF, tcmn.DmChuyenMucREF, tcmn.DmLoaiBannerREF
		, tcmn.DmViTriREF, tcmn.SoLuong, tcmn.DonViTinhREF, tcmn.DonGia
		, tcmn.ChietKhau, tcmn.ThanhTien, tcmn.IsKhuyenMai, tcmn.KhuyenMai
		, tcmn.ThucChayMuaNgoaiChiTietID
		, tcmn.TongTienDuToanMuaSauCK
		, tcmn.TongTienDuToanLaiMuaSauCK, tcmn.ChietKhauMuaNgoai, tcmn.DmBannerREF
		, tcmn.DmChienDichREF
		, tcmn.DmWebsiteREF
		, tcmn.TenWebsite
		, tcmn.NgayThucHien
		, tcmn.NgayBatDau
		, tcmn.NgayKetThuc
		, tcmn.DonViTinhThucChay
		, tcmn.DonGiaMuaTheoDonViTinhTC
		, tcmn.TongViewClickThucChay
		, tcmn.TongBaiVietChiPhiThucChay
		, tcmn.SoLuongThucChay
		, tcmn.ThanhTienThucChayBanSauCK
		, tcmn.TongThanhTienThucChayMuaSauCK
		, tcmn.ThanhTienLaiThucChaySauCK
		, tcmn.ThanhTienLaiThucChayKM
		, tcmn.SoLuongThucChayKM
		, tcmn.SoLuongThucChayLechTreoHa
		, tcmn.ThanhTienLaiThucChayLechTreoHa
		, tcmn.GiaTriThayDoiLaiSauCK
		, tcmn.SoLuongThayDoi
		, tcmn.SoLuongKMThayDoi
		, tcmn.GiaTriKMThayDoi
		, tcmn.GhiChu
		, tcmn.CreatedAt
		, tcmn.LastModifiedAt	
	FROM
	(
		SELECT hd.HopDongID, hd.SoHopDong, hd.DmMaHopDongREF, hd.NgayDanhSoHopDong
		, hd.TrangThaiHopDong, hd.SysNhanVienREF, hd.TenDangNhap
		, hd.DmPhongBanREF, hd.DmBoPhanREF, hd.DmNhomLamViecREF, hd.DmDiaDiemLamViecREF, hd.DmKhachHangREF
		, hdct.HopDongChiTietID, ISNULL(hdct.DanhSachNhanHangREF,'') DanhSachNhanHangREF, hdct.DmNhomNganhREF
		, hdct.DmLoaiREF, hdct.DmSanPhamREF, hdct.DmChuyenMucREF, hdct.DmLoaiBannerREF
		, hdct.DmViTriREF, hdct.SoLuong, hdct.DonViTinhREF, hdct.DonGia
		, hdct.ChietKhau, hdct.ThanhTien, hdct.IsKhuyenMai, hdct.KhuyenMai
		, tcmn.ThucChayMuaNgoaiChiTietID
		, tcmn.TongTienDuToanMuaSauCK
		, tcmn.TongTienDuToanLaiMuaSauCK
		, tcmn.ChietKhauMuaNgoai, 0 AS DmBannerREF
		, 0 AS DmChienDichREF
		, dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(hdct.DmWebsiteREF) DmWebsiteREF
		, dbo.GetWebsiteLinkByDmWebsiteID(hdct.DmWebsiteREF,hdct.TenWebsite) TenWebsite
		, @NgayThucHien AS NgayThucHien
		, CONVERT(Date,tcmn.TuNgay) AS NgayBatDau
		, CONVERT(DATE,tcmn.DenNgay) AS NgayKetThuc
		, @DonViTinhThucChay AS DonViTinhThucChay
		, (CASE WHEN ISNULL(tcmn.SoLuongThucChay,0) <> 0 THEN (tcmn.ThanhTienMuaNgoaiTruocCK*(100-tcmn.ChietKhauMuaNgoai)/100)/ISNULL(tcmn.SoLuongThucChay,0)
			ELSE (tcmn.ThanhTienMuaNgoaiTruocCK*(100-tcmn.ChietKhauMuaNgoai)/100)
		END) AS DonGiaMuaTheoDonViTinhTC
		, 0 AS TongViewClickThucChay
		, 0 AS TongBaiVietChiPhiThucChay
		, 0 AS SoLuongThucChay
		, ISNULL(tcmn.ThanhTienThucChayBanSauCK,0) ThanhTienThucChayBanSauCK
		, (tcmn.ThanhTienMuaNgoaiTruocCK*(100-tcmn.ChietKhauMuaNgoai)/100) AS TongThanhTienThucChayMuaSauCK
		, 0 AS ThanhTienLaiThucChaySauCK
		, 0 AS ThanhTienLaiThucChayKM
		, 0 AS SoLuongThucChayKM
		, 0 AS SoLuongThucChayLechTreoHa
		, 0 AS ThanhTienLaiThucChayLechTreoHa
		, (CASE WHEN hdct.ChietKhau <> 100 THEN tcmn.ThanhTienLaiThucChaySauCK
		ELSE 0
		END) AS GiaTriThayDoiLaiSauCK
		, (CASE WHEN hdct.ChietKhau <> 100 THEN ISNULL(tcmn.SoLuongThucChay,0)
			ELSE 0 
		END) AS SoLuongThayDoi
		, (CASE WHEN hdct.ChietKhau = 100 THEN ISNULL(tcmn.SoLuongThucChay,0)
		ELSE 0
		END) AS SoLuongKMThayDoi
		, (CASE WHEN hdct.ChietKhau = 100 THEN tcmn.ThanhTienLaiThucChaySauCK
		ELSE 0
		END) AS GiaTriKMThayDoi
		, @ghiChu AS GhiChu
		, Getdate() AS CreatedAt
		, GetDate() AS LastModifiedAt
		FROM
		(
			SELECT tcmn.*, ISNULL(mn.ThanhTienSauCKMua,0) AS [TongTienDuToanMuaSauCK], ISNULL(mn.ThanhTienLaiSauCK,0) AS [TongTienDuToanLaiMuaSauCK]
			FROM 
			(SELECT tcmn.* FROM dbo.ThucChayMuaNgoaiChiTiet tcmn 
				WHERE 1=1 
				AND Status in (1,2, 4) --trang thai duyet thanh toan, duyet thuc chay
				--AND CONVERT(DATE,tcmn.LastModifiedAt) = @NgayThucHien
				AND tcmn.TuNgay >= @NgayGioiHanTinh
				AND tcmn.DeletedStatus = 0
				AND tcmn.ThucChayMuaNgoaiChiTietID = @ThucChayMuaNgoaiChiTietID
			)tcmn
			INNER JOIN (select mn.* from dbo.HopDongChiTiet_MuaNgoai mn where mn.HopDongChiTietID = @HopDongChiTietREF) mn 
			on mn.HopDongChiTietID = tcmn.HopDongChiTietREF
			
		)tcmn
		INNER JOIN 
		(SELECT ct.* FROM dbo.HopDongChiTiet ct 
			WHERE ct.DeletedStatus = 0
			AND (ct.DmLoaiREF = 13 OR ct.DmLoaiBannerREF = 18)
			AND ct.HopDongChiTietID = @HopDongChiTietREF
		)hdct ON hdct.HopDongFK = tcmn.HopDongREF AND hdct.HopDongChiTietID = tcmn.HopDongChiTietREF
		INNER JOIN (select * from HopDong hd where hd.HopDongID = @HopDongREF)hd on hd.HopDongID = hdct.HopDongFK
	
	)tcmn WHERE 1=1
	AND tcmn.HopDongChiTietID NOT IN (SELECT  DISTINCT hopdongchiTietID FROM MuaNgoaiChot_TinhBoSung_2016)
	
END

```
