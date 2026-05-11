# Stored Procedure: `ThucChay_InsertThucChayDaTinh_BySanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-18 15:28:32.813000
- **Ngày sửa cuối**: 2018-08-28 11:44:41.557000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(100)` | No |
| `@DmBannerREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucChayDaTinh]


CREATE  PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_BySanPham]
    @NgayThucHien DATETIME ,
    @SoHopDong NVARCHAR(50) ,
    @TypeProduct INT ,
    @DmWebsiteREF INT ,
    @TenWebsite NVARCHAR(50) ,
    @DmBannerREF INT ,
    @DmSanPhamREF INT
AS
    BEGIN
	

        INSERT  INTO dbo.ThucChayDaTinh
                SELECT  NEWID() ,
                        TD.* ,
                        ISNULL(( ( TD.ThanhTienThucChayTruocTrietKhau
                                   * TD.ChietKhau ) / 100 ), 0) AS GiaTriTrietKhauThucChay ,
                        ISNULL(( TD.ThanhTienThucChayTruocTrietKhau
                                 - ( TD.ThanhTienThucChayTruocTrietKhau
                                     * TD.ChietKhau ) / 100 ), 0) AS ThanhTienSauTrietKhauThucChay ,
                        ISNULL(( ( ( TD.ThanhTienThucChayTruocTrietKhau
                                     - ( TD.ThanhTienThucChayTruocTrietKhau
                                         * TD.ChietKhau ) / 100 )
                                   * TD.TiLeTuVan ) / 100 ), 0) AS GiaTriHoaHongThucChay ,
                        ISNULL(( TD.ThanhTienThucChayTruocTrietKhau
                                 - ( TD.ThanhTienThucChayTruocTrietKhau
                                     * TD.ChietKhau ) / 100
                                 - ( ( TD.ThanhTienThucChayTruocTrietKhau
                                       - ( TD.ThanhTienThucChayTruocTrietKhau
                                           * TD.ChietKhau ) / 100 )
                                     * TD.TiLeTuVan ) / 100 ), 0) AS ThanhTienThucThu ,
                        ( CASE WHEN TD.IsKhuyenMai = 1
                               THEN TD.ThanhTienThucChayTruocTrietKhau
                               ELSE 0
                          END ) AS ThanhTienKM ,
                        ( CASE WHEN ( ( ( TD.IsKhuyenMai = 1 )
                                        OR ( TD.ChietKhau = 100 )
                                      )
                                      AND ( TD.DonViTinh = 'VIEW' )
                                    )
                               THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(TD.TongViewThucChay,
                                                              TD.SoLuong,
                                                              TD.DonViTinh,
                                                              TD.NgayThucHien,
                                                              TD.HopDongChiTietREF),
                                           0)
                               WHEN ( ( ( TD.IsKhuyenMai = 1 )
                                        OR ( TD.ChietKhau = 100 )
                                      )
                                      AND ( TD.DonViTinh = 'CLICK' )
                                    )
                               THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(TD.TongClickThucChay,
                                                              TD.SoLuong,
                                                              TD.DonViTinh,
                                                              TD.NgayThucHien,
                                                              TD.HopDongChiTietREF),
                                           0)
                               ELSE 0
                          END ) AS SoLuongThucChayKM ,
                        ( CASE WHEN ( TD.DonViTinh = 'VIEW' )
                               THEN dbo.[ThucChay_GetSoLuongLechTreoHa_V1](@NgayThucHien,
                                                              TD.SoHopDong,
                                                              TD.HopDongChiTietREF,
                                                              TD.SoLuong,
                                                              TD.DmSanPhamREF,
                                                              TD.TongViewThucChay)
                               WHEN ( TD.DonViTinh = 'CLICK' )
                               THEN dbo.[ThucChay_GetSoLuongLechTreoHa_V1](@NgayThucHien,
                                                              TD.SoHopDong,
                                                              TD.HopDongChiTietREF,
                                                              TD.SoLuong,
                                                              TD.DmSanPhamREF,
                                                              TD.TongClickThucChay)
                               ELSE 0
                          END ) AS SoLuongLechTreoHa ,
                        ( CASE WHEN ( TD.DonViTinh = 'VIEW' )
                               THEN dbo.[ThucChay_GetSoLuongLechTreoHa_V1](@NgayThucHien,
                                                              TD.SoHopDong,
                                                              TD.HopDongChiTietREF,
                                                              TD.SoLuong,
                                                              TD.DmSanPhamREF,
                                                              TD.TongViewThucChay)
                                    * TD.DonGiaTheoDonViTinh
                               WHEN ( TD.DonViTinh = 'CLICK' )
                               THEN dbo.[ThucChay_GetSoLuongLechTreoHa_V1](@NgayThucHien,
                                                              TD.SoHopDong,
                                                              TD.HopDongChiTietREF,
                                                              TD.SoLuong,
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
                                    D.HopDongID ,
	--Thong tin ve ma so 
                                    D.SoHopDong ,
                                    D.DmMaHopDongREF ,
                                    D.TenMaHopDong , 
	--Thong tin ve thoi gian
                                    D.NgayDanhSoHopDong ,
                                    D.NgayKyHopDong ,
                                    D.NhanHopDong ,
                                    D.NgayNhanBanFax ,
                                    D.NgayNhanHopDongBanCung ,
                                    D.NgayChuyenHopDongChoKeToan ,
                                    D.So ,
                                    D.Thang ,
                                    D.Nam , 
	--Thong tin ve gia tri
                                    D.GiaTriHopDong ,
                                    D.CongNo ,
	--Thong tin chi tiet phan bo
                                    A.HopDongChiTietREF ,
	--Thong tin ve trang thai
                                    D.DangSuDung ,
                                    D.IsGiayPhep ,
                                    D.TrangThaiHopDong ,
                                    D.IsBanCung , 
	--Thong tin ve Nhan vien kinh doanh
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
	--Thong tin ve khach hang
	--D.DmKhachHangREF, 
                                    D.TenKhachHang , 
	--C.NhanHang, 
                                    A.DsNhanHangREF NhanHang ,
                                    C.DmNhomNganhREF ,
                                    C.TenNhomNganh , 
	--Thong tin hinh thuc quang cao
                                    C.DmLoaiREF AS DmHinhThucQuangCao ,
                                    C.TenLoai AS TenHinhThucQuangCao , 
	--Thong tin San pham
                                    dbo.GetProductIDByTypeProduct(A.TypeProduct) AS DmSanPhamREF ,
                                    dbo.GetProductNameByTypeProduct(A.TypeProduct) AS TenSanPham ,
                                    C.DmNhomWebsiteREF ,
                                    C.TenNhomWebsite , 
	--C.DmWebsiteREF, 
	--C.TenWebsite, 
                                    C.DmChuyenMucREF ,
                                    C.TenChuyenMuc ,
                                    C.DmLoaiBannerREF ,
                                    C.TenLoaiBanner ,
                                    C.DmBannerREF DmViTriREF ,
                                    C.TenViTri ,
                                    ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,
                                                              'Y'), '') DotChayHopDong ,
                                    C.SoLuong AS SoLuongDotChayHD ,
                                    ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,
                                                              'N'), 0) DotChayBooking ,
                                    dbo.GetSoLuongDotChayBookingByHopDongChiTiet(C.HopDongChiTietID) SoLuongDotChayBooking , 
	--Thong tin ve Tien
	--****haidh chinh sua
                                    C.SoLuong
                                    * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong ,
	--****haidh chinh sua
                                    dbo.ThucChay_GetDonViTinhNotCPD(C.DonViTinh) AS DonViTinh , 
	--'VIEW' DonViTinh, 
                                    dbo.ThucChay_GetDonGiaByNgayThucHien(A.NgayThucHien,
                                                              A.HopDongChiTietREF,
                                                              C.DonGia) AS DonGia ,
	--****haidh chinh sua 
                                    ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,
                                                              C.DonViTinh,
                                                              C.DonGia,
                                                              D.NgayKyHopDong,
                                                              A.NgayThucHien,
                                                              A.HopDongChiTietREF),
                                           0) AS DonGiaTheoDonViTinh ,
                                    C.ChietKhau ,
                                    C.GiamGia ,
                                    C.ThanhTien ,
                                    C.TiLeTuVan ,
                                    C.ChiPhiTuVan ,
                                    C.IsKhuyenMai ,
                                    C.KhuyenMai ,
	--Thuc chay
                                    A.DmBannerREF DmBannerREF ,--A.DmBannerREF,
                                    0 DmChienDichREF ,--A.DmChienDichREF,
                                    A.DmWebsiteREF ,
                                    A.TenWebsite ,
	--C.DmWebsiteREF,--A.DmWebsiteREF,
	--E.TenWebsite,
	--A.SoHopDong,
                                    A.TongViewThucChay ,
                                    A.TongClickThucChay ,
                                    A.TongSoBaiViet ,
	--****haidh chinh sua	
                                    ( CASE WHEN ( ( C.IsKhuyenMai = 0 )
                                                  AND ( ( UPPER(C.DonViTinh) = 'CPM' )
                                                        OR ( UPPER(C.DonViTinh) = 'TRUE REACH' )
                                                      )
                                                )
                                           THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(A.TongViewThucChay,
                                                              C.SoLuong,
                                                              C.DonViTinh,
                                                              A.NgayThucHien,
                                                              A.HopDongChiTietREF),
                                                       0)
                                           WHEN ( ( C.IsKhuyenMai = 0 )
                                                  AND ( UPPER(C.DonViTinh) = 'CPC' )
                                                )
                                           THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1(A.TongClickThucChay,
                                                              C.SoLuong,
                                                              C.DonViTinh,
                                                              A.NgayThucHien,
                                                              A.HopDongChiTietREF),
                                                       0)
                                           ELSE 0
                                      END ) AS SoLuongThucChay ,
	--Thanhuc Tien Thuc Chay
                                    A.NgayThucHien ,
                                    0 AS GiaTriThayDoi ,
	--****haidh chinh sua	
                                    ISNULL(dbo.ThucChay_GetThanhTienChuanThucChay(C.SoLuong,
                                                              C.DonViTinh,
                                                              C.DonGia,
                                                              D.NgayKyHopDong,
                                                              A.TongViewThucChay,
                                                              A.TongClickThucChay,
                                                              A.TongSoBaiViet,
                                                              A.NgayThucHien,
                                                              A.HopDongChiTietREF),
                                           0) AS ThanhTienThucChayTruocTrietKhau
                          FROM      ( SELECT    A.NgayThucHien ,
                                                ROUND(SUM(( A.TongViewThucChay
                                                            * B.TiLeThucChayHDCTSoVoiBanner )
                                                          / 100), 0) TongViewThucChay ,
                                                ROUND(SUM(( A.TongClickThucChay
                                                            * B.TiLeThucChayHDCTSoVoiBanner )
                                                          / 100), 0) TongClickThucChay ,
                                                SUM(ISNULL(A.TongSoBaiViet, 0)) TongSoBaiViet ,
                                                [dbo].[f_ReturnListConcatNhanHangREFByBanner](@SoHopDong,
                                                              @TypeProduct,
                                                              B.HopDongChiTietREF,
                                                              A.DmWebsiteREF) DsNhanHangREF ,
                                                B.HopDongChiTietREF ,
                                                A.TypeProduct ,
                                                A.DmWebsiteREF ,
                                                A.TenWebsite ,
                                                A.DmBannerREF
                                      FROM      ThucChayTemp A
                                                INNER JOIN ( SELECT DISTINCT
                                                              B.DmBannerID ,
                                                              B.DsNhanHangREF ,
                                                              B.HopDongChiTietREF ,
                                                              B.HopDongREF ,
                                                              B.TiLeThucChayHDCTSoVoiBanner ,
                                                              B.DeletedStatus ,
                                                              B.DaThucHienUpdateTiLe
                                                             FROM
                                                              dbo.ThucChayHopDongChiTietAndBanner B
                                                           ) B ON B.DmBannerID = CONVERT(NVARCHAR(50), A.DmBannerREF)
                                      WHERE     A.SoHopDong = @SoHopDong
                                                AND A.TypeProduct = @TypeProduct
                                                AND A.DmWebsiteREF = @DmWebsiteREF
                                                AND A.DmBannerREF = @DmBannerREF
                                                AND B.DeletedStatus = 0
												AND A.DmSanPhamREF = @DmSanPhamREF
                                      GROUP BY  A.NgayThucHien ,
                                                B.HopDongChiTietREF ,
                                                A.TypeProduct ,
                                                A.TenWebsite ,
                                                A.DmWebsiteREF ,
                                                A.DmBannerREF
                                    ) A
                                    INNER JOIN 
									(SELECT * FROM dbo.HopDongChiTiet C 
										WHERE 1=1 
										AND C.DeletedStatus = 0
										AND C.DmSanPhamREF = @DmSanPhamREF
										AND C.DmLoaiBannerREF NOT IN ( 17, 18 )--Khong tinh cho cac loai banner ChiPhi va Mua ngoai
										AND C.DmLoaiREF <> 13 --Khong tinh thuc chay cho HTQC Mua Ngoai
										AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](C.DonViTinhREF,C.DonViTinh) = 3 --Đơn vị của hình thức CPM
										AND C.DonViTinhREF <> 31 --Don vi trinh TRUE REACH
									)C ON C.HopDongChiTietID = A.HopDongChiTietREF
                                    INNER JOIN (SELECT * FROM dbo.HopDong D WHERE D.TrangThaiHopDong <> 3 AND D.DeletedStatus = 0)D ON D.HopDongID = C.HopDongFK
                                    INNER JOIN DBO.DmWebsite E ON E.DmWebsiteID = C.DmWebsiteREF
                         
                                   
                        ) TD
	
	
    END

```
