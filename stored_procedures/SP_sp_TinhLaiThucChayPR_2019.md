# Stored Procedure: `sp_TinhLaiThucChayPR_2019`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-09-11 10:53:55.733000
- **Ngày sửa cuối**: 2020-09-11 10:54:02.203000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongREF` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@ThucChayHopDongChiTietREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
	CREATE PROCEDURE sp_TinhLaiThucChayPR_2019 

	 @HopDongREF int,
	 @HopDongChiTietID INT,	
	 @ThucChayHopDongChiTietREF INT, 
	  @NgayThucHien DATETIME
	as
	begin
	Declare @GhiChu NVARCHAR(200)
	
	SET @GhiChu =N'Tính lại thực chạy cho id '+ convert(nvarchar(50),@ThucChayHopDongChiTietREF)

   UPDATE dbo.ThucChayHopDongChiTietPR SET RecordStatus = 1 where ThucChayHopDongChiTietPRID =@ThucChayHopDongChiTietREF

	INSERT INTO thucchaydatinh 


	SELECT  NEWID() , T.*
										FROM    ( 
	SELECT  DISTINCT
															hd.HopDongID ,
															hd.SoHopDong ,
															hd.DmMaHopDongREF ,
															hd.TenMaHopDong ,
															hd.NgayDanhSoHopDong ,
															hd.NgayKyHopDong ,
															ISNULL(hd.NhanHopDong,
																  '') AS NhanHopDong ,
															hd.NgayNhanBanFax ,
															hd.NgayNhanHopDongBanCung ,
															hd.NgayChuyenHopDongChoKeToan ,
															hd.So ,
															hd.Thang ,
															hd.Nam , 
															hd.GiaTriHopDong ,
															hd.CongNo ,
															tchpctpr.HopDongChiTietID ,
															hd.DangSuDung ,
															hd.IsGiayPhep ,
															hd.TrangThaiHopDong ,
															hd.IsBanCung , 
															hd.DmPhongBanREF ,
															ISNULL(hd.TenPhongBan, '') AS TenPhongBan ,
															hd.DmBoPhanREF ,
															ISNULL(hd.TenBoPhan, '') AS TenBoPhan ,
															hd.DmNhomLamViecREF ,
															ISNULL(hd.TenNhom, '') AS TenNhom ,
															hd.DmDiaDiemLamViecREF ,
															ISNULL(hd.TenDiaDiemLamViec, '') AS TenDiaDiemLamViec ,
															hd.SysNhanVienREF ,
															ISNULL(hd.TenDangNhap, '') AS TenDangNhap ,
															hd.TenNhanVien ,
															hd.TenKhachHang ,
															tchpctpr.DmNhanHangREF AS NhanHang ,
															0 DmNhomNganhREF ,
															'' TenNhomNganh , 
															hdct.DmLoaiREF AS DmHinhThucQuangCao ,
															hdct.TenLoai AS TenHinhThucQuangCao , 
															hdct.DmSanPhamREF AS DmSanPhamREF ,
															hdct.TenSanPham ,
															0 DmNhomWebsiteREF ,
															'' TenNhomWebsite ,
															tchpctpr.DmChuyenMucREF ,
															tchpctpr.TenChuyenMuc ,
															hdct.DmLoaiBannerREF ,
															hdct.TenLoaiBanner ,
															tchpctpr.DmViTriREF ,
															tchpctpr.TenViTri ,
															'' DotChayHopDong ,
															0 AS SoLuongDotChayHD ,
															tchpctpr.ThucChayHopDongChiTietPRID DotChayBooking ,
															0 AS SoLuongDotChayBooking , 
															hdct.SoLuong AS SoLuong ,
															dbo.FormatDonViTinh(hdct.DonViTinh) DonViTinh ,
															hdct.DonGia AS DonGia ,
															tchpctpr.GiaTien AS DonGiaTheoDonViTinh ,
															tchpctpr.ChietKhau ,
															hdct.GiamGia ,
															hdct.ThanhTien ,
															hdct.TiLeTuVan ,
															hdct.ChiPhiTuVan ,
															tchpctpr.KhuyenMai IsKhuyenMai ,
															'' KhuyenMai ,
															0 DmBannerREF ,--A.DmBannerREF,
															0 DmChienDichREF ,--A.DmChienDichREF,
															dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(tchpctpr.DmWebsiteREF) DmWebsiteREF ,
															dbo.GetWebsiteLinkByDmWebsiteID(tchpctpr.DmWebsiteREF,
																  tchpctpr.TenWebsite) TenWebsite ,
															0 TongViewThucChay ,
															0 TongClickThucChay ,
															0 TongSoBaiViet ,
															( CASE WHEN tchpctpr.KhuyenMai = 0 AND tchpctpr.ChietKhau <> 100 THEN ISNULL(tchpctpr.SoLuong, 0)
																  ELSE 0
															END ) AS SoLuongThucChay ,
															@NgayThucHien AS NgayThucHien ,
															0 AS GiaTriThayDoi ,
															ISNULL(tchpctpr.GiaTien, 0) * ISNULL(tchpctpr.SoLuong, 0) AS ThanhTienThucChayTruocChietKhau ,
															ISNULL(( CONVERT(FLOAT, ISNULL(tchpctpr.GiaTien, 0)) * CONVERT(FLOAT, ISNULL(tchpctpr.SoLuong, 0)) * CONVERT(FLOAT, tchpctpr.ChietKhau) )
																  / 100, 0) AS GiaTriTrietKhauThucChay ,

															ISNULL(tchpctpr.GiaTien, 0) * ISNULL(tchpctpr.SoLuong, 0) * ( CONVERT(FLOAT, ( 100 - tchpctpr.ChietKhau )) / 100 ) AS ThanhTienThucChaySauChietKhau ,

															( CONVERT(FLOAT, ( 100 - tchpctpr.ChietKhau )) * CONVERT(FLOAT, ( ISNULL(tchpctpr.GiaTien, 0) * ISNULL(tchpctpr.SoLuong, 0) )) / 100 )
															 * ISNULL(hdct.TiLeTuVan, 0) / 100 AS GiaTriHoaHongThucChay ,

															( CASE WHEN ( tchpctpr.KhuyenMai = 1 OR tchpctpr.ChietKhau = 100 OR tchpctpr.GiaTien = 0 OR tchpctpr.SoLuong = 0 ) THEN 0
																  ELSE ( 100 - hdct.TiLeTuVan ) / ( ISNULL(tchpctpr.GiaTien, 0) * ISNULL(tchpctpr.SoLuong, 0) * ( CONVERT(FLOAT, ( 100 - tchpctpr.ChietKhau )) / 100 ) )
															  END ) AS ThanhTienThucThu ,

															( CASE WHEN tchpctpr.KhuyenMai = 1 OR tchpctpr.ChietKhau = 100 THEN ISNULL(tchpctpr.GiaTien, 0) * ISNULL(tchpctpr.SoLuong, 0)
																  ELSE 0
															  END ) AS ThanhTienKM ,

															( CASE WHEN tchpctpr.KhuyenMai = 1 OR tchpctpr.ChietKhau = 100 THEN ISNULL(tchpctpr.SoLuong, 0)
																  ELSE 0
															  END ) AS SoLuongThucChayKM ,

															0 SoLuongLechTreoHa ,
															0 ThanhTienLechTreoHa ,
															GETDATE() CreatedAt ,
															GETDATE() LastModifiedAt ,
															0 IsPheDuyet ,
															'' PheDuyetBy ,
															'' PheDuyetAt ,
															0 SoLuongThayDoi ,
															0 SoLuongKMThayDoi ,
															0 GiaTriKMThayDoi ,
															@GhiChu GhiChu
												 FROM      ( SELECT tchpctpr.* ,T.HopDongChiTietREF HopDongChiTietID 
																FROM
																	(SELECT * FROM  dbo.ThucChayHopDongChiTietPR WHERE HopDongREF =@HopDongREF
																	AND ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietREF
																	) tchpctpr
																	INNER JOIN (
																			SELECT TOP 1 HopDongREF, @HopDongChiTietID HopDongChiTietREF, ThucChayHopDongChiTietPRID,0 ThuTuTrongSo 
																			FROM dbo.[ThucChayHopDongChiTietPR]
																			WHERE HopDongREF = @HopDongREF 
																			AND ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietREF
																			ORDER BY ThuTuTrongSo, ThucChayHopDongChiTietPRID
																) T ON tchpctpr.ThucChayHopDongChiTietPRID = T.ThucChayHopDongChiTietPRID
															) tchpctpr 
												INNER JOIN ( SELECT --ID Hop Dong
																  D.HopDongID ,
																  D.SoHopDong ,
																  D.DmMaHopDongREF ,
																  D.TenMaHopDong , 
																  D.NgayDanhSoHopDong ,
																  D.NgayKyHopDong ,
																  ISNULL(D.NhanHopDong, '') AS NhanHopDong ,
																  D.NgayNhanBanFax ,
																  D.NgayNhanHopDongBanCung ,
																  D.NgayChuyenHopDongChoKeToan ,
																  D.So ,
																  D.Thang ,
																  D.Nam , 
																  D.GiaTriHopDong ,
																  D.CongNo ,
																  D.DangSuDung ,
																  D.IsGiayPhep ,
																  D.TrangThaiHopDong ,
																  D.IsBanCung , 
																  D.DmPhongBanREF ,
																  ISNULL(D.TenPhongBan, '') AS TenPhongBan ,
																  D.DmBoPhanREF ,
																  ISNULL(D.TenBoPhan, '') AS TenBoPhan ,
																  D.DmNhomLamViecREF ,
																  ISNULL(D.TenNhom, '') AS TenNhom ,
																  D.DmDiaDiemLamViecREF ,
																  D.TenDiaDiemLamViec ,
																  D.SysNhanVienREF ,
																  ISNULL(D.TenDangNhap, '') AS TenDangNhap ,
																  D.TenNhanVien ,
																  D.TenKhachHang
																  FROM dbo.HopDong D
																  WHERE D.TrangThaiHopDong NOT IN (0, 3)
																  AND D.Nam >= 2013
																  AND D.NgayDanhSoHopDong <= '2019-12-31'
															) hd ON tchpctpr.HopDongREF = hd.HopDongID
															INNER JOIN (SELECT * FROM dbo.HopDongChiTiet hdct WHERE hdct.HopDongFK = @HopDongREF 
															AND hdct.HopDongChiTietID =@HopDongChiTietID
																		)hdct 
															ON tchpctpr.HopDongChiTietID = hdct.HopDongChiTietID
															AND hdct.DmLoaiREF = tchpctpr.DmHinhThucQuangCaoREF
															AND hdct.DmSanPhamREF = tchpctpr.DmSanPhamREF
										    
											) T;     
END
```
