# Stored Procedure: `sp_TC_InsertThucChayDaTinh_PR_HopDongSanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-10-23 13:58:06.073000
- **Ngày sửa cuối**: 2019-12-11 15:12:52.033000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

/*
--EXEC [ThucChay_InsertThucChayDaTinh_PR_GoiHD_vt] '2017-04-08','2017-04-08'
-- [dbo].[sp_TC_InsertThucChayDaTinh_PR_HopDongSanPham] '2018-10-22',111,141
*/
CREATE PROCEDURE [dbo].[sp_TC_InsertThucChayDaTinh_PR_HopDongSanPham]
    @NgayThucHien DATETIME ,
    @HopDongREF INT,
	@DmSanPhamREF INT
AS
    BEGIN
		DECLARE @v_count INT = 0, @NgayDSGioiHanTinh DATETIME ,
		@v_row_thucchaytreopr INT = 0,
		@ThucChayHopDongChiTietPRID INT = 0
							SET @NgayDSGioiHanTinh = '2019-12-31'
							SET @v_count = 0
							SET @v_row_thucchaytreopr = ISNULL((SELECT COUNT(ThucChayHopDongChiTietPRID) FROM dbo.ThucChayHopDongChiTietPR
							WHERE DeletedStatus = 0
							AND HopDongREF = @HopDongREF
							AND DmSanPhamREF = @DmSanPhamREF
							AND ThoiGianBatDau >= '2014-01-01'
                            AND ( CASE WHEN CreatedAt >= LastModifiedAt THEN CONVERT(DATE, CreatedAt)
                                       ELSE CONVERT(DATE, LastModifiedAt)
                                  END ) = @NgayThucHien
							),0)

							--PRINT @HopDongREF
							--PRINT @DmSanPhamREF
							--PRINT @v_row_thucchaytreopr
							-----****TINH THUC CHAY TREN TUNG HOP DONG, SAN PHAM
							WHILE (@v_count < @v_row_thucchaytreopr)
							BEGIN
								--XAC DINH TRONG SO CUA CAC THUC TREO PR CAN TINH THUC CHAY
								EXEC [dbo].[sp_TC_CapNhatThuTuTrongSoThucChayHopDongChiTietPR_ByHopDongSanPhamNgayThucHien]
									@EndDate = @NgayThucHien ,
									@DmSanPhamREF = @DmSanPhamREF,
									@pHopDongID = @HopDongREF


									INSERT  INTO dbo.ThucChayDaTinh
										SELECT  NEWID() , T.*
										FROM    ( SELECT  DISTINCT
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
															'' GhiChu
												 FROM      ( SELECT tchpctpr.* ,T.HopDongChiTietREF HopDongChiTietID 
																FROM
																	(SELECT * FROM  dbo.ThucChayHopDongChiTietPR WHERE HopDongREF = @HopDongREF) tchpctpr
																	INNER JOIN (
																			SELECT TOP (1) HopDongREF, HopDongChiTietREF, ThucChayHopDongChiTietPRID,ThuTuTrongSo 
																			FROM dbo.[ThucChayHopDongChiTietPR_ThuTuTrongSo_Temp]
																			WHERE HopDongREF = @HopDongREF
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
																  AND D.NgayDanhSoHopDong <= @NgayDSGioiHanTinh
															) hd ON tchpctpr.HopDongREF = hd.HopDongID
															INNER JOIN (SELECT * FROM dbo.HopDongChiTiet hdct WHERE hdct.HopDongFK = @HopDongREF)hdct 
															ON tchpctpr.HopDongChiTietID = hdct.HopDongChiTietID
															AND hdct.DmLoaiREF = tchpctpr.DmHinhThucQuangCaoREF
															AND hdct.DmSanPhamREF = tchpctpr.DmSanPhamREF
												) T;            
	

								IF NOT EXISTS ( SELECT  *
												FROM    dbo.ThucChay_ThongTinHopDongChiTietID_PR tc
												WHERE    EXISTS (
														SELECT TOP (1) t.ThucChayHopDongChiTietPRID
														FROM    dbo.ThucChayHopDongChiTietPR_ThuTuTrongSo_Temp t 
														WHERE t.HopDongREF = @HopDongREF 
														AND t.ThucChayHopDongChiTietPRID = tc.ThucChayHopDongChiTietPRID 
														ORDER BY t.ThuTuTrongSo, t.ThucChayHopDongChiTietPRID ) )
									BEGIN
											 INSERT  INTO dbo.ThucChay_ThongTinHopDongChiTietID_PR
											SELECT  t.HopDongChiTietREF ,
													t.ThucChayHopDongChiTietPRID
											FROM    (
														SELECT TOP (1) HopDongREF, HopDongChiTietREF, ThucChayHopDongChiTietPRID,ThuTuTrongSo 
														FROM dbo.[ThucChayHopDongChiTietPR_ThuTuTrongSo_Temp]
														WHERE HopDongREF = @HopDongREF
														ORDER BY ThuTuTrongSo, ThucChayHopDongChiTietPRID
											) t
									END

								SET @ThucChayHopDongChiTietPRID = (SELECT TOP (1) ThucChayHopDongChiTietPRID 
																			FROM dbo.[ThucChayHopDongChiTietPR_ThuTuTrongSo_Temp]
																			WHERE HopDongREF = @HopDongREF
																			ORDER BY ThuTuTrongSo, ThucChayHopDongChiTietPRID)

								EXEC [dbo].[sp_TC_UpdateRecordStatus_ThucChayHopDongChiTietPR_ByID]
								@NgayThucHien = @NgayThucHien,
								@HopDong = @HopDongREF,
								@ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID,
								@DmSanPhamREF = @DmSanPhamREF 

								DELETE FROM dbo.[ThucChayHopDongChiTietPR_ThuTuTrongSo_Temp]
								SET @v_count = @v_count + 1
							END
						
    END;

```
