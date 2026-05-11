# Stored Procedure: `sp_TC_InsertThucTreoThayDoi_ChiPhi_SanPhamChinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-12 09:24:25.397000
- **Ngày sửa cuối**: 2018-11-21 11:26:03.877000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTiet` | `int(4)` | No |
| `@NgaythucHien` | `datetime(8)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucTreoThayDoi_ChiPhi_SanPhamChinh] 1333,'2014-01-02',8888887


CREATE PROCEDURE [dbo].[sp_TC_InsertThucTreoThayDoi_ChiPhi_SanPhamChinh]
    @HopDongChiTiet INT ,
    @NgaythucHien DATETIME ,
    @GiaTriThayDoi FLOAT
AS
    BEGIN
        PRINT @HopDongChiTiet
        INSERT  INTO dbo.ThucChayDaTinh
                SELECT  NEWID() ,
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
                        0 SoLuongKMThayDoi ,
                        0 GiaTriKMThayDoi ,
                        '' GhiChu
                FROM    ( SELECT 
	--ID Hop Dong
                                    D.HopDongID ,
	--Thong tin ve ma so 
                                    D.SoHopDong ,
                                    D.DmMaHopDongREF ,
                                    D.TenMaHopDong , 
	--Thong tin ve thoi gian
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
                                    --                          @NgaythucHien) NhanHang ,
									tchdt.DmNhanHangREF_ThucTreo AS NhanHang,
                                    C.DmNhomNganhREF ,
                                    C.TenNhomNganh , 
                                    C.DmLoaiREF AS DmHinhThucQuangCao ,
                                    C.TenLoai AS TenHinhThucQuangCao , 
                                    C.DmSanPhamREF AS DmSanPhamREF ,
                                    C.TenSanPham ,
                                    C.DmNhomWebsiteREF ,
                                    C.TenNhomWebsite , 
                                    C.DmChuyenMucREF ,
                                    C.TenChuyenMuc ,
                                    C.DmLoaiBannerREF ,
                                    C.TenLoaiBanner ,
                                    C.DmViTriREF ,
                                    C.TenViTri ,
                                    'CP_SPC_TTR' DotChayHopDong ,
                                    0 AS SoLuongDotChayHD ,
                                    ThucChayHopDongChiTietID DotChayBooking ,
                                    0 AS SoLuongDotChayBooking , 
                                    C.SoLuong AS SoLuong ,
                                    dbo.FormatDonViTinh(C.DonViTinh) DonViTinh ,
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
                                    0 SoLuongThucChay ,
                                    @NgaythucHien AS NgayThucHien ,
                                    @GiaTriThayDoi AS GiaTriThayDoi ,
                                    0 AS ThanhTienThucChayTruocTrietKhau
                          FROM      ( SELECT * FROM  dbo.HopDongChiTiet
                                      WHERE     DmSanPhamREF IN ( 140, 228, 549, 564, 375, 231, 238, 337,
                                                              531, 370, 339, 342, 306, 423, 305, 381 )
                                                AND HopDongChiTietID = @HopDongChiTiet
                                                AND DmLoaiBannerREF = 17 --CHI PHI cua San Pham Chinh
                                    ) C
                                    INNER JOIN ( SELECT *
                                                 FROM   dbo.HopDong hd
                                                 WHERE  hd.TrangThaiHopDong <> 3
                                               ) D ON D.HopDongID = C.HopDongFK
									INNER JOIN ( SELECT ThucChayHopDongChiTietID,
													DmBannerREF,
													DmNhanHangREF AS DmNhanHangREF_ThucTreo,
													HopDongChiTietREF
												FROM   dbo.ThucChayHopDongChiTiet
												WHERE  DeletedStatus = 1
											) tchdt ON C.HopDongChiTietID = tchdt.HopDongChiTietREF

                        ) TD

    END




--EXEC [ThucChay_InsertThucChayDaTinh_ChiPhiKhac] '2013-07-01','2013-07-11'

```
