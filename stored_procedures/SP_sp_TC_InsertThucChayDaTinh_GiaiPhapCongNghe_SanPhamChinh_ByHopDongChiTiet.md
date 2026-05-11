# Stored Procedure: `sp_TC_InsertThucChayDaTinh_GiaiPhapCongNghe_SanPhamChinh_ByHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-05-02 09:15:07.937000
- **Ngày sửa cuối**: 2018-11-21 17:40:21.097000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- USE [ABM_Data_Release]
-- GO
-- /****** Object:  StoredProcedure [dbo].[ThucChay_InsertThucChayDaTinh_ChiPhi_SanPhamChinh]    Script Date: 05/12/2016 11:16:46 ******/
-- SET ANSI_NULLS ON
-- GO
-- SET QUOTED_IDENTIFIER ON
-- GO
------------------------------------------------------------
CREATE PROCEDURE [dbo].[sp_TC_InsertThucChayDaTinh_GiaiPhapCongNghe_SanPhamChinh_ByHopDongChiTiet]
    @NgayThucHien DATETIME,
	@HopDongChiTietREF INT
AS
    BEGIN
 
        DECLARE @NgayGioiHanTinh DATETIME
        SET @NgayGioiHanTinh = '2013-01-01'
 	---------***********DANH SACH CAC SAN PHAM CHINH CO TINH CHI PHI*******-------------
 					--BoxApp CPM	 370
 					--Balloon Ads	339
 					--Mobile	342
 
 	----- insert data 
        INSERT  INTO dbo.ThucChayDaTinh
                SELECT  NEWID() ,
                        TD.* ,
                        ISNULL(( TD.ThanhTienThucChayTruocTrietKhau
                                 * TD.ChietKhau ) / 100, 0) AS GiaTriTrietKhauThucChay ,
                        ISNULL(( TD.ThanhTienThucChayTruocTrietKhau
                                 - ( TD.ThanhTienThucChayTruocTrietKhau
                                     * TD.ChietKhau ) / 100 ), 0) AS ThanhTienSauTrietKhauThucChay ,
                        ISNULL(( ( TD.ThanhTienThucChayTruocTrietKhau
                                   - ( TD.ThanhTienThucChayTruocTrietKhau
                                       * TD.ChietKhau ) / 100 ) * TD.TiLeTuVan )
                               / 100, 0) AS GiaTriHoaHongThucChay ,
                        ISNULL(( TD.ThanhTienThucChayTruocTrietKhau
                                 - ( TD.ThanhTienThucChayTruocTrietKhau
                                     * TD.ChietKhau ) / 100
                                 - ( ( TD.ThanhTienThucChayTruocTrietKhau
                                       - ( TD.ThanhTienThucChayTruocTrietKhau
                                           * TD.ChietKhau ) / 100 )
                                     * TD.TiLeTuVan ) / 100 ), 0) AS ThanhTienThucThu ,
                        ( CASE WHEN ( ( TD.IsKhuyenMai = 1 )
                                      OR ( TD.ChietKhau = 100 )
                                    ) THEN TD.ThanhTienThucChayTruocTrietKhau
                               ELSE 0
                          END ) AS ThanhTienKM ,
                        ( CASE WHEN ( ( TD.IsKhuyenMai = 1 )
                                      OR ( TD.ChietKhau = 100 )
                                    )
                               THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_ChiPhi_SanPhamChinh(@NgayThucHien,
                                                              @NgayGioiHanTinh,
                                                              TD.HopDongChiTietID),
                                           0)
                               ELSE 0
                          END ) AS SoLuongThucChayKM ,
                        0 SoLuongLechTreoHa ,
                        0 ThanhTienLechTreoHa ,
                        GETDATE() ,
                        GETDATE() ,
                        0 IsPheDuyet ,
                        '' PheDuyetBy ,
                        '' PheDuyetAt ,
                        0 SoLuongThayDoi ,
                        0 SoLuongKMThayDoi ,
                        0 GiaTriKMThayDoi ,
                        '' GhiChu
                FROM    ( SELECT 
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
                                    C.HopDongChiTietID ,
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
                                    D.TenKhachHang ,
                                    --[dbo].[f_ReturnListConcatNhanHangREF_v2](C.HopDongChiTietID,
                                    --                          @NgayThucHien) NhanHang ,
									tchdt.DmNhanHangREF_ThucTreo AS NhanHang,
                                    C.DmNhomNganhREF ,
                                    C.TenNhomNganh , 
                                    C.DmLoaiREF AS DmHinhThucQuangCao ,
                                    C.TenLoai AS TenHinhThucQuangCao , 
                                    C.DmSanPhamREF AS DmSanPhamREF ,
                                    E.TenSanPham ,
                                    C.DmNhomWebsiteREF ,
                                    C.TenNhomWebsite ,
                                    C.DmChuyenMucREF ,
                                    C.TenChuyenMuc ,
                                    C.DmLoaiBannerREF ,
                                    C.TenLoaiBanner ,
                                    C.DmViTriREF ,
                                    C.TenViTri ,
                                    '' DotChayHopDong ,
                                    0 AS SoLuongDotChayHD ,
                                    tchdt.ThucChayHopDongChiTietID DotChayBooking ,
                                    0 AS SoLuongDotChayBooking , 
                                    ISNULL(C.SoLuong, 0) AS SoLuong ,
                                    ISNULL(C.DonViTinh, N'đ/v') AS DonViTinh ,
                                    C.DonGia AS DonGia ,
                                    C.DonGia AS DonGiaTheoDonViTinh ,
                                    C.ChietKhau ,
                                    C.GiamGia ,
                                    C.ThanhTien ,
                                    C.TiLeTuVan ,
                                    C.ChiPhiTuVan ,
                                    C.IsKhuyenMai ,
                                    C.KhuyenMai ,
                                    tchdt.DmBannerREF DmBannerREF ,--A.DmBannerREF,
                                    0 DmChienDichREF ,--A.DmChienDichREF,
                                    dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF) DmWebsiteREF ,
                                    dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,
                                                              C.TenWebsite) TenWebsite ,
                                    0 TongViewThucChay ,
                                    0 TongClickThucChay ,
                                    0 TongSoBaiViet ,
                                    C.SoLuong AS SoLuongThucChay , 
                                    @NgayThucHien AS NgayThucHien ,
                                    0 AS GiaTriThayDoi ,
                                    C.SoLuong * C.DonGia AS ThanhTienThucChayTruocTrietKhau
                          FROM      ( SELECT    *
                                      FROM      dbo.HopDongChiTiet
                                      WHERE     DmSanPhamREF IN ( 370, 339, 342, 598, 775,240 )
                                                AND DeletedStatus = 0
                                                AND (DmLoaiNenTangREF = 8 --Retargeting & Content base
														OR DmSanPhamREF = 775 -- campaing audit
													)
                                                AND NOT ( ( HopDongChiTiet.DmLoaiBannerREF IN (18))OR ( HopDongChiTiet.DmLoaiREF = 13 ))-- --Khong tinh thuc chay cho HTQC Mua Ngoai
												AND HopDongChiTietID = @HopDongChiTietREF
                                    ) C
                                    INNER JOIN ( SELECT *
                                                 FROM   dbo.HopDong hd
                                                 WHERE  hd.TrangThaiHopDong <> 3
                                                        AND hd.DeletedStatus = 0
                                               ) D ON D.HopDongID = C.HopDongFK
									INNER JOIN ( SELECT TOP (1) ThucChayHopDongChiTietID,
													DmBannerREF,
													DmNhanHangREF AS DmNhanHangREF_ThucTreo,
													HopDongChiTietREF
												FROM   dbo.ThucChayHopDongChiTiet
												WHERE  DeletedStatus = 0
												AND HopDongChiTietREF = @HopDongChiTietREF
											) tchdt ON C.HopDongChiTietID = tchdt.HopDongChiTietREF
                                    INNER JOIN dbo.DmSanPham E ON E.DmSanPhamID = C.DmSanPhamREF
                --                                              AND ISNULL(([dbo].[ThucChay_GetSoLuongThucChayChuanByDonViTinh_ChiPhi_CongNghe_ByHopDongChiTiet] 
																--(
																--	@NgayThucHien,
																--	@NgayGioiHanTinh,
																--	C.HopDongChiTietID
																--)), 0) > 0
                                                              AND C.SoLuong > 0
                        ) TD	
	
        --UPDATE TRANG THAI BAN GHI
		
		UPDATE dbo.ThucChayHopDongChiTiet
		SET RecordStatus = 1
		WHERE HopDongChiTietREF IN
		(
			SELECT HopDongChiTietREF FROM dbo.ThucChayDaTinh
			WHERE HopDongChiTietREF = @HopDongChiTietREF 
			AND NgayThucHien = @NgayThucHien
		)
 		AND DeletedStatus = 0
        SELECT  '1'
    END

```
