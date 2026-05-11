# Stored Procedure: `ThucChay_InsertThucChayDaTinh_ByHDLoaiSP_BySanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-18 15:38:37.007000
- **Ngày sửa cuối**: 2017-09-18 15:38:37.007000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucChayDaTinh_ByHDLoaiSP]


CREATE  PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_ByHDLoaiSP_BySanPham]
    @NgayThucHien DATETIME ,
    @SoHopDong NVARCHAR(50) ,
    @TypeProduct INT ,
    @DmWebsiteREF INT ,
    @TenWebsite NVARCHAR(50),
	@DmSanPhamREF INT
AS
    BEGIN

        INSERT  INTO dbo.ThucChayDaTinh
                SELECT  NEWID() ,
                        TD.* ,
                        ( TD.DonGia ) * TD.SoLuongThucChay AS ThanhTienThucChayTruocTrietKhau ,
                        ( ( ( TD.DonGia ) * TD.SoLuongThucChay )
                          - ( TD.DonGiaTheoDonViTinh * TD.SoLuongThucChay ) ) GiaTriTrietKhauThucChay ,
                        ( TD.DonGiaTheoDonViTinh * TD.SoLuongThucChay ) AS ThanhTienThucChaySauTrietKhau ,
                        0 AS GiaTriHoaHongThucChay ,
                        0 AS ThanhTienThucThu ,
                        ( CASE WHEN ( TD.DonViTinh = 'VIEW' )
                               THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayKMByHDLoaiSP(@NgayThucHien,
                                                              TD.TongViewThucChay,
                                                              TD.SoHopDong,
                                                              TD.DmSanPhamREF),
                                           0) * ( TD.DonGia )
                               WHEN ( TD.DonViTinh = 'CLICK' )
                               THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayKMByHDLoaiSP(@NgayThucHien,
                                                              TD.TongClickThucChay,
                                                              TD.SoHopDong,
                                                              TD.DmSanPhamREF),
                                           0) * ( TD.DonGia )
                               ELSE 0
                          END ) AS ThanhTienKM ,
                        ( CASE WHEN ( TD.DonViTinh = 'VIEW' )
                               THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayKMByHDLoaiSP(@NgayThucHien,
                                                              TD.TongViewThucChay,
                                                              TD.SoHopDong,
                                                              TD.DmSanPhamREF),
                                           0)
                               WHEN ( TD.DonViTinh = 'CLICK' )
                               THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayKMByHDLoaiSP(@NgayThucHien,
                                                              TD.TongClickThucChay,
                                                              TD.SoHopDong,
                                                              TD.DmSanPhamREF),
                                           0)
                               ELSE 0
                          END ) AS SoLuongThucChayKM ,
                        ( CASE WHEN ( TD.DonViTinh = 'VIEW' )
                               THEN dbo.ThucChay_GetSoLuongLechTreoHa(@NgayThucHien,
                                                              TD.SoHopDong,
                                                              TD.HopDongChiTietREF,
                                                              TD.soluong,
                                                              TD.DmSanPhamREF,
                                                              TD.TongViewThucChay)
                               WHEN ( TD.DonViTinh = 'CLICK' )
                               THEN dbo.ThucChay_GetSoLuongLechTreoHa(@NgayThucHien,
                                                              TD.SoHopDong,
                                                              TD.HopDongChiTietREF,
                                                              TD.soluong,
                                                              TD.DmSanPhamREF,
                                                              TD.TongClickThucChay)
                               ELSE 0
                          END ) AS SoLuongLechTreoHa ,
                        ( CASE WHEN ( TD.DonViTinh = 'VIEW' )
                               THEN dbo.ThucChay_GetSoLuongLechTreoHa(@NgayThucHien,
                                                              TD.SoHopDong,
                                                              TD.HopDongChiTietREF,
                                                              TD.soluong,
                                                              TD.DmSanPhamREF,
                                                              TD.TongViewThucChay)
                                    * TD.DonGiaTheoDonViTinh
                               WHEN ( TD.DonViTinh = 'CLICK' )
                               THEN dbo.ThucChay_GetSoLuongLechTreoHa(@NgayThucHien,
                                                              TD.SoHopDong,
                                                              TD.HopDongChiTietREF,
                                                              TD.soluong,
                                                              TD.DmSanPhamREF,
                                                              TD.TongClickThucChay)
                                    * TD.DonGiaTheoDonViTinh
                               ELSE 0
                          END ) AS ThanhTienLechTreoHa ,
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
                                    ISNULL(B.HopDongID, 0) HopDongID ,
		--Thong tin ve ma so 
                                    B.SoHopDong ,
                                    B.DmMaHopDongREF ,
                                    B.TenMaHopDong , 
		--Thong tin ve thoi gian
                                    B.NgayDanhSoHopDong ,
                                    B.NgayKyHopDong ,
                                    B.NhanHopDong ,
                                    B.NgayNhanBanFax ,
                                    B.NgayNhanHopDongBanCung ,
                                    B.NgayChuyenHopDongChoKeToan ,
                                    B.So ,
                                    B.Thang ,
                                    B.Nam , 
		--Thong tin ve gia tri
                                    B.GiaTriHopDong ,
                                    B.CongNo ,
		--Thong tin chi tiet phan bo
                                    0 HopDongChiTietREF ,
		--Thong tin ve trang thai
                                    B.DangSuDung ,
                                    B.IsGiayPhep ,
                                    B.TrangThaiHopDong ,
                                    B.IsBanCung , 
		--Thong tin ve Nhan vien kinh doanh
                                    B.DmPhongBanREF ,
                                    ISNULL(B.TenPhongBan, '') AS TenPhongBan ,
                                    B.DmBoPhanREF ,
                                    ISNULL(B.TenBoPhan, '') AS TenBoPhan ,
                                    B.DmNhomLamViecREF ,
                                    ISNULL(B.TenNhom, '') AS TenNhom ,
                                    B.DmDiaDiemLamViecREF ,
                                    B.TenDiaDiemLamViec ,
                                    B.SysNhanVienREF ,
                                    ISNULL(B.TenDangNhap, '') AS TenDangNhap ,
                                    B.TenNhanVien , 
		--Thong tin ve khach hang
		--D.DmKhachHangREF, 
                                    B.TenKhachHang ,
                                    '' NhanHang ,
                                    0 DmNhomNganhREF ,
                                    '' TenNhomNganh , 
		--Thong tin hinh thuc quang cao
                                    0 AS DmHinhThucQuangCao ,
                                    '' AS TenHinhThucQuangCao , 
		--Thong tin San pham
                                    dbo.GetProductIDByTypeProduct(A.TypeProduct) AS DmSanPhamREF ,
                                    dbo.GetProductNameByTypeProduct(A.TypeProduct) AS TenSanPham ,
                                    0 DmNhomWebsiteREF ,
                                    '' TenNhomWebsite ,
                                    0 DmChuyenMucREF ,
                                    '' TenChuyenMuc ,
                                    0 DmLoaiBannerREF ,
                                    '' TenLoaiBanner ,
                                    0 DmViTriREF ,
                                    '' TenViTri ,
                                    '' DotChayHopDong ,
                                    B.soluongdotchayHD AS SoLuongDotChayHD ,
                                    '' DotChayBooking ,
                                    0 AS SoLuongDotChayBooking , 
		--Thong tin ve Tien
                                    B.soluong ,
                                    B.DonViTinh ,
                                    B.DonGia AS DonGia ,
                                    B.DonGiaSauCK AS DonGiaTheoDonViTinh ,
                                    0 ChietKhau ,
                                    0 GiamGia ,
                                    ISNULL(B.ThanhTien, 0) ThanhTien ,
                                    0 TiLeTuVan ,
                                    0 ChiPhiTuVan ,
                                    0 IsKhuyenMai ,
                                    '' KhuyenMai ,
		--Thuc chay
                                    0 DmBannerREF ,--A.DmBannerREF,
                                    0 DmChienDichREF ,--A.DmChienDichREF,
                                    A.DmWebsiteREF ,
                                    A.TenWebsite ,
                                    A.PageView TongViewThucChay ,
                                    A.Click TongClickThucChay ,
                                    A.TongSoBaiViet ,
                                    ( CASE WHEN ( B.DonViTinh = 'VIEW' )
                                           THEN ISNULL([dbo].[ThucChay_GetSoLuongThucChayByHDLoaiSP](@NgayThucHien,
                                                              A.PageView,
                                                              A.SoHopDong,
                                                              [dbo].[GetProductIDByTypeProduct](A.TypeProduct)),
                                                       0)
                                           WHEN ( B.DonViTinh = 'CLICK' )
                                           THEN ISNULL([dbo].[ThucChay_GetSoLuongThucChayByHDLoaiSP](@NgayThucHien,
                                                              A.Click,
                                                              A.SoHopDong,
                                                              [dbo].[GetProductIDByTypeProduct](A.TypeProduct)),
                                                       0)
                                           ELSE 0
                                      END ) AS SoLuongThucChay ,
		--Thanhuc Tien Thuc Chay
                                    A.NgayThucHien ,
                                    0 AS GiaTriThayDoi
                          FROM      ( SELECT    dbo.GetProductNameByTypeProduct(tc.TypeProduct) AS TenSanPham ,
                                                tc.TypeProduct ,
                                                tc.SoHopDong ,
                                                tc.DmWebsiteREF ,
                                                tc.TenWebsite ,
                                                SUM(ISNULL(tc.TongViewThucChay,
                                                           0)) AS PageView ,
                                                SUM(ISNULL(tc.TongClickThucChay,
                                                           0)) AS Click ,
                                                SUM(ISNULL(tc.TongSoBaiViet, 0)) AS TongSoBaiViet ,
                                                tc.NgayThucHien
                                      FROM      ThucChayTemp tc
                                      WHERE     tc.SoHopDong = @SoHopDong
                                                AND tc.TypeProduct = @TypeProduct
                                                AND tc.DmWebsiteREF = @DmWebsiteREF
												AND tc.DmSanPhamREF = @DmSanPhamREF
                                      GROUP BY  tc.TypeProduct ,
                                                tc.SoHopDong ,
                                                tc.DmWebsiteREF ,
                                                tc.TenWebsite ,
                                                tc.NgayThucHien
                                    ) A
                                    LEFT JOIN ( SELECT  ( CASE
                                                              WHEN hdct.DmSanPhamREF = 231
                                                              THEN 3
                                                              WHEN hdct.DmSanPhamREF = 238
                                                              THEN 4
                                                              WHEN hdct.DmSanPhamREF = 339
                                                              THEN 5
                                                              WHEN hdct.DmSanPhamREF = 342
                                                              THEN 6
                                                              WHEN hdct.DmSanPhamREF = 337
                                                              THEN 7
                                                              WHEN hdct.DmSanPhamREF = 240
                                                              THEN 8
                                                              WHEN hdct.DmSanPhamREF = 732
                                                              THEN 17
                                                              WHEN hdct.DmSanPhamREF = 735
                                                              THEN 18
                                                              ELSE 9
                                                          END ) AS type_product ,
                                                        hd.SoHopDong ,
                                                        hd.HopDongID ,
		--Thong tin ve ma so 
                                                        hd.DmMaHopDongREF ,
                                                        hd.TenMaHopDong , 
		--Thong tin ve thoi gian
                                                        hd.NgayDanhSoHopDong ,
                                                        hd.NgayKyHopDong ,
                                                        hd.NhanHopDong ,
                                                        hd.NgayNhanBanFax ,
                                                        hd.NgayNhanHopDongBanCung ,
                                                        hd.NgayChuyenHopDongChoKeToan ,
                                                        hd.So ,
                                                        hd.Thang ,
                                                        hd.Nam , 
		--Thong tin ve gia tri
                                                        hd.GiaTriHopDong ,
                                                        hd.CongNo ,
		--Thong tin chi tiet phan bo
		--Thong tin ve trang thai
                                                        hd.DangSuDung ,
                                                        hd.IsGiayPhep ,
                                                        hd.TrangThaiHopDong ,
                                                        hd.IsBanCung , 
		--Thong tin ve Nhan vien kinh doanh
                                                        hd.DmPhongBanREF ,
                                                        ISNULL(hd.TenPhongBan,
                                                              '') AS TenPhongBan ,
                                                        hd.DmBoPhanREF ,
                                                        ISNULL(hd.TenBoPhan,
                                                              '') AS TenBoPhan ,
                                                        hd.DmNhomLamViecREF ,
                                                        ISNULL(hd.TenNhom, '') AS TenNhom ,
                                                        hd.DmDiaDiemLamViecREF ,
                                                        hd.TenDiaDiemLamViec ,
                                                        hd.SysNhanVienREF ,
                                                        ISNULL(hd.TenDangNhap,
                                                              '') AS TenDangNhap ,
                                                        hd.TenNhanVien , 
		--Thong tin ve khach hang
		--D.DmKhachHangREF, 
                                                        hd.TenKhachHang ,
                                                        SUM(hdct.SoLuong) soluongdotchayHD ,
                                                        SUM(hdct.SoLuong
                                                            * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)) soluong ,
                                                        SUM(hdct.ThanhTien) ThanhTien ,
                                                        MAX(dbo.ThucChay_GetDonViTinhNotCPD(hdct.DonViTinh)) AS DonViTinh ,
		--max(hdct.ThanhTien/hdct.SoLuong) DonGiaSauCKMax,
                                                        MAX(hdct.ThanhTien
                                                            / ( hdct.SoLuong
                                                              * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh) )) DonGiaSauCK ,
                                                        MAX(hdct.DonGia
                                                            / dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)) DonGia
                                                FROM    HopDong hd
                                                        INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
                                                              AND hdct.DmSanPhamREF = @DmSanPhamREF
                                                              AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF,
                                                              hdct.DonViTinh) = 3 --Đơn vị của hình thức CPM
                                                              AND hdct.DeletedStatus = 0
                                                              AND hdct.SoLuong > 0
                                                GROUP BY hdct.DmSanPhamREF ,
                                                        hd.SoHopDong ,
                                                        hd.HopDongID ,
		--Thong tin ve ma so 
                                                        hd.DmMaHopDongREF ,
                                                        hd.TenMaHopDong , 
		--Thong tin ve thoi gian
                                                        hd.NgayDanhSoHopDong ,
                                                        hd.NgayKyHopDong ,
                                                        hd.NhanHopDong ,
                                                        hd.NgayNhanBanFax ,
                                                        hd.NgayNhanHopDongBanCung ,
                                                        hd.NgayChuyenHopDongChoKeToan ,
                                                        hd.So ,
                                                        hd.Thang ,
                                                        hd.Nam , 
		--Thong tin ve gia tri
                                                        hd.GiaTriHopDong ,
                                                        hd.CongNo ,
		--Thong tin chi tiet phan bo
		--Thong tin ve trang thai
                                                        hd.DangSuDung ,
                                                        hd.IsGiayPhep ,
                                                        hd.TrangThaiHopDong ,
                                                        hd.IsBanCung , 
		--Thong tin ve Nhan vien kinh doanh
                                                        hd.DmPhongBanREF ,
                                                        hd.TenPhongBan ,
                                                        hd.DmBoPhanREF ,
                                                        hd.TenBoPhan ,
                                                        hd.DmNhomLamViecREF ,
                                                        hd.TenNhom ,
                                                        hd.DmDiaDiemLamViecREF ,
                                                        hd.TenDiaDiemLamViec ,
                                                        hd.SysNhanVienREF ,
                                                        hd.TenDangNhap ,
                                                        hd.TenNhanVien ,
                                                        hd.TenKhachHang
                                              ) B ON UPPER(LTRIM(RTRIM(A.SoHopDong))) = B.SoHopDong
                                                     AND A.TypeProduct = B.type_product 
		--AND B.DonGiaSauCK > 0
	--ORDER BY A.TenSanPham ,a.SoHopDong,a.TenWebsite 
                        ) TD
                WHERE   TD.SoHopDong IS NOT NULL
		

    END

```
