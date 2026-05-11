# Stored Procedure: `sp_TC_InsertThucTreoThayDoi_ChiPhiKhac`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-12 09:22:17.407000
- **Ngày sửa cuối**: 2022-09-26 14:47:12.697000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTiet` | `int(4)` | No |
| `@NgaythucHien` | `datetime(8)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |
| `@ThucChayHopDongChiTietID` | `nvarchar(2000)` | No |
| `@SoLuongThayDoi` | `int(4)` | No |
| `@GhiChu` | `nvarchar(1000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucTreoThayDoi_ChiPhiKhac]
/*
EXEC [dbo].[sp_TC_InsertThucTreoThayDoi_ChiPhiKhac] 502854, '2017-05-31', -455555, 91016, -3
*/

CREATE PROCEDURE [dbo].[sp_TC_InsertThucTreoThayDoi_ChiPhiKhac]
    @HopDongChiTiet INT ,
    @NgaythucHien DATETIME ,
    @GiaTriThayDoi FLOAT,
	@ThucChayHopDongChiTietID NVARCHAR(1000),
	@SoLuongThayDoi INT,
	@GhiChu NVARCHAR(500)
AS
    BEGIN
		DECLARE @ChietKhau FLOAT = 0
		SET @ChietKhau =
		(
			SELECT TOP (1) ChietKhau FROM dbo.HopDongChiTiet
			WHERE HopDongChiTietID = @HopDongChiTiet
			ORDER BY HopDongChiTietID
		)

		DECLARE @TABLE_OP TABLE(ThucChayDaTinhID NVARCHAR(100), ThucChayHopDongChiTietID int)

		--DOI TRU THONG TIN KHONG PHAI LA KHUYEN MAI
		IF(@ChietKhau <> 100)
		BEGIN
		     INSERT  INTO dbo.ThucChayDaTinh
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
			 OUTPUT INSERTED.ThucChayDaTinhID, INSERTED.DotChayBooking INTO @TABLE_OP
                SELECT NEWID() ,
                        TD.* ,
                        0 GiaTriTrietKhauThucChay ,
                        0 AS ThanhTienSauTrietKhauThucChay ,
                        0 AS GiaTriHoaHongThucChay ,
                        0 AS ThanhTienThucThu ,
                        0 AS ThanhTienKM ,
                        0 AS SoLuongThucChayKM ,
                        0 SoLuongLechTreoHa ,
                        0 ThanhTienLechTreoHa ,
                        GETDATE() ,
                        GETDATE() ,
                        0 IsPheDuyet ,
                        '' PheDuyetBy ,
                        '' PheDuyetAt ,
                        @SoLuongThayDoi SoLuongThayDoi ,
                        0 SoLuongKMThayDoi ,
                        0 GiaTriKMThayDoi ,
                        @GhiChu GhiChu
                FROM    ( SELECT TOP (1)
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
                                    tcdt.HopDongChiTietREF ,
                                    DangSuDung ,
                                    IsGiayPhep ,
                                    TrangThaiHopDong ,
                                    IsBanCung , 
                                    DmPhongBanREF ,
                                    TenPhongBan ,
                                    DmBoPhanREF ,
                                    TenBoPhan ,
                                    DmNhomLamViecREF ,
                                    tcdt.TenNhomLamViec ,
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
                                    @ThucChayHopDongChiTietID DotChayBooking ,
                                    SoLuongDotChayBooking , 
                                    SoLuong ,
                                    DonViTinh ,
                                    DonGia , 
                                    tcdt.DonGiaTheoDonVi ,
                                    ChietKhau ,
                                    GiamGia ,
                                    ThanhTien ,
                                    TiLeTuVan ,
                                    ChiPhiTuVan ,
                                    IsKhuyenMai ,
                                    KhuyenMai ,
                                    0 DmBannerREF ,
                                    DmChienDichREF ,
                                    DmWebsiteREF ,
                                    TenWebsite ,
                                    0 TongViewThucChay ,
                                    0 TongClickThucChay ,
                                    0 TongSoBaiViet ,
                                    0 SoLuongThucChay ,
                                    @NgaythucHien AS NgayThucHien ,
                                    @GiaTriThayDoi AS GiaTriThayDoi ,
                                    0 AS ThanhTienThucChayTruocTrietKhau
                          FROM      dbo.ThucChayDaTinh tcdt
						  WHERE tcdt.DotChayBooking = @ThucChayHopDongChiTietID
								AND HopDongChiTietREF = @HopDongChiTiet
						  ORDER BY CreatedAt DESC
                        ) TD
						

		END
		--DOI TRU THONG TIN CHI PHI LA KHUYEN MAI
		ELSE
		BEGIN
			   INSERT  INTO dbo.ThucChayDaTinh
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
			   	 OUTPUT INSERTED.ThucChayDaTinhID, INSERTED.DotChayBooking INTO @TABLE_OP
				SELECT NEWID() ,
						TD.* ,
						0 GiaTriTrietKhauThucChay ,
						0 AS ThanhTienSauTrietKhauThucChay ,
						0 AS GiaTriHoaHongThucChay ,
						0 AS ThanhTienThucThu ,
						0 AS ThanhTienKM ,
						0 AS SoLuongThucChayKM ,
						0 SoLuongLechTreoHa ,
						0 ThanhTienLechTreoHa ,
						GETDATE() ,
						GETDATE() ,
						0 IsPheDuyet ,
						'' PheDuyetBy ,
						'' PheDuyetAt ,
						0 SoLuongThayDoi ,
						@SoLuongThayDoi SoLuongKMThayDoi ,
						@GiaTriThayDoi GiaTriKMThayDoi ,
						@GhiChu GhiChu
				FROM    ( SELECT TOP (1)
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
									tcdt.HopDongChiTietREF ,
									DangSuDung ,
									IsGiayPhep ,
									TrangThaiHopDong ,
									IsBanCung , 
									DmPhongBanREF ,
									TenPhongBan ,
									DmBoPhanREF ,
									TenBoPhan ,
									DmNhomLamViecREF ,
									tcdt.TenNhomLamViec ,
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
									@ThucChayHopDongChiTietID DotChayBooking ,
									SoLuongDotChayBooking , 
									SoLuong ,
									DonViTinh ,
									DonGia , 
									tcdt.DonGiaTheoDonVi ,
									ChietKhau ,
									GiamGia ,
									ThanhTien ,
									TiLeTuVan ,
									ChiPhiTuVan ,
									IsKhuyenMai ,
									KhuyenMai ,
									0 DmBannerREF ,
									DmChienDichREF ,
									DmWebsiteREF ,
									TenWebsite ,
									0 TongViewThucChay ,
									0 TongClickThucChay ,
									0 TongSoBaiViet ,
									0 SoLuongThucChay ,
									@NgaythucHien AS NgayThucHien ,
									0 AS GiaTriThayDoi ,
									0 AS ThanhTienThucChayTruocTrietKhau
							FROM      dbo.ThucChayDaTinh tcdt
							WHERE tcdt.DotChayBooking = @ThucChayHopDongChiTietID
								AND HopDongChiTietREF = @HopDongChiTiet
							ORDER BY CreatedAt DESC
						) TD
		--COMMENT THEM UPDATE TRANG THAI HAIDH 2021-06-03
		IF(EXISTS(SELECT top (1) ThucChayDaTinhID FROM @TABLE_OP
		WHERE ThucChayHopDongChiTietID = @ThucChayHopDongChiTietID
		ORDER BY ThucChayHopDongChiTietID))
		BEGIN
			--UPDATE LAI TRANG THAI
			UPDATE tc
			SET tc.RecordStatus = 0
			FROM dbo.ThucChayHopDongChiTiet tc
			WHERE tc.ThucChayHopDongChiTietID = @ThucChayHopDongChiTietID
		END
		END
END
       



```
