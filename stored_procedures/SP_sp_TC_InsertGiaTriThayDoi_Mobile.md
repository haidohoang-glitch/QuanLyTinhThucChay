# Stored Procedure: `sp_TC_InsertGiaTriThayDoi_Mobile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-16 10:50:48.150000
- **Ngày sửa cuối**: 2017-06-23 17:57:38.680000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTiet` | `int(4)` | No |
| `@NgaythucHien` | `datetime(8)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(200)` | No |
| `@BannerType` | `int(4)` | No |
| `@DmBannerID` | `int(4)` | No |
| `@SoLuongThayDoi` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--ThucChay_InsertGiaTriThayDoi_Mobile 91102,'2016-02-15',2,56,'dantri.com.vn',

CREATE PROCEDURE [dbo].[sp_TC_InsertGiaTriThayDoi_Mobile]
    @HopDongChiTiet INT ,
    @NgaythucHien DATETIME ,
    @GiaTriThayDoi FLOAT ,
    @DmWebsiteREF INT ,
    @TenWebsite NVARCHAR(100) ,
    @BannerType INT ,
    @DmBannerID INT ,
    @SoLuongThayDoi INT
	--,
	--@ProductUnitName NVARCHAR(50)
AS
    BEGIN	
        INSERT  INTO dbo.ThucChayDaTinh
                SELECT  NEWID() ,
                        TD.*
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
	--Thong tin ve gia tri
                                    D.GiaTriHopDong ,
                                    D.CongNo ,
	--Thong tin chi tiet phan bo
                                    C.HopDongChiTietID ,
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
                                    [dbo].[f_ReturnListConcatNhanHangREF_v2](C.HopDongChiTietID,
                                                              @NgaythucHien) NhanHang ,
                                    C.DmNhomNganhREF ,
                                    C.TenNhomNganh , 
	--Thong tin hinh thuc quang cao
                                    C.DmLoaiREF AS DmHinhThucQuangCao ,
                                    C.TenLoai AS TenHinhThucQuangCao , 
	--Thong tin San pham
                                    C.DmSanPhamREF AS DmSanPhamREF ,
                                    E.TenSanPham ,
                                    C.DmNhomWebsiteREF ,
                                    C.TenNhomWebsite , 
	--C.DmWebsiteREF, 
	--C.TenWebsite, 
                                    C.DmChuyenMucREF ,
                                    C.TenChuyenMuc ,
                                    C.DmLoaiBannerREF ,
                                    C.TenLoaiBanner ,
                                    C.DmViTriREF ,
                                    C.TenViTri ,
                                    'Update Gia tri thay doi Mobile' DotChayHopDong ,
                                    C.SoLuong AS SoLuongDotChayHD ,
                                    'PS Gia tri thay doi Mobile' DotChayBooking ,
                                    0 AS SoLuongDotChayBooking , 
	--Thong tin ve Tien
                                    C.SoLuong
                                    * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong ,
                                    ( CASE WHEN C.DonViTinh IN ( 'CPC', 'CPM' )
                                           THEN C.DonViTinh
                                           ELSE C.TenLoai
                                      END ) AS DonViTinh , -- tuyetnta sửa
                                    dbo.ThucChay_GetDonGiaTheoDonViTruocChietKhau(C.HopDongChiTietID,
                                                              dbo.ThucChay_GetDonViTinhMobileByHopDongChiTietID(C.HopDongChiTietID,
                                                              @NgaythucHien),
                                                              @BannerType,
                                                              @NgaythucHien) AS DonGia ,
                                    dbo.ThucChay_GetDonGiaTheoDonViTruocChietKhau(C.HopDongChiTietID,
                                                              dbo.ThucChay_GetDonViTinhMobileByHopDongChiTietID(C.HopDongChiTietID,
                                                              @NgaythucHien),
                                                              @BannerType,
                                                              @NgaythucHien) AS DonGiaTheoDonViTinh ,
                                    C.ChietKhau ,
                                    C.GiamGia ,
                                    C.ThanhTien ,
                                    C.TiLeTuVan ,
                                    C.ChiPhiTuVan ,
                                    C.IsKhuyenMai ,
                                    C.KhuyenMai ,
	--Thuc chay
                                    @DmBannerID DmBannerREF ,--A.DmBannerREF,
                                    0 DmChienDichREF ,--A.DmChienDichREF,
                                    @DmWebsiteREF DmWebsiteREF ,
                                    @TenWebsite TenWebsite ,
                                    0 TongViewThucChay ,
                                    0 TongClickThucChay ,
                                    0 TongSoBaiViet ,
                                    0 SoLuongThucChay ,
	--Thanhuc Tien Thuc Chay
                                    @NgaythucHien AS NgayThucHien ,
                                    ( CASE WHEN C.IsKhuyenMai = 0
                                           THEN @GiaTriThayDoi
                                           ELSE 0
                                      END ) AS GiaTriThayDoi ,
                                    0 AS ThanhTienThucChayTruocTrietKhau ,
                                    0 GiaTriTrietKhauThucChay ,
                                    0 AS ThanhTienSauTrietKhauThucChay ,
                                    0 AS GiaTriHoaHongThucChay ,
                                    0 AS ThanhTienThucThu ,
                                    0 AS ThanhTienKM ,
                                    0 AS SoLuongThucChayKM ,
                                    0 SoLuongLechTreoHa ,
                                    0 ThanhTienLechTreoHa ,
                                    GETDATE() CreatedAt ,
                                    GETDATE() LastModified ,
                                    0 IsPheDuyet ,
                                    '' PheDuyetBy ,
                                    '' PheDuyetAt ,
                                    @SoLuongThayDoi SoLuongThayDoi ,
                                    0 SoLuongKMThayDoi ,
                                    ( CASE WHEN C.IsKhuyenMai = 1
                                           THEN @GiaTriThayDoi
                                           ELSE 0
                                      END ) AS GiaTriKMThayDoi ,
                                    '' GhiChu
                          FROM      ( SELECT    *
                                      FROM      HopDongChiTiet
                                      WHERE     DmSanPhamREF IN ( 342 )
                                                AND HopDongChiTietID = @HopDongChiTiet
                                                AND DeletedStatus = 0
                                    ) C
                                    INNER JOIN ( SELECT *
                                                 FROM   HopDong hd
                                                 WHERE  hd.TrangThaiHopDong != 3
                                               ) D ON D.HopDongID = C.HopDongFK
                                    INNER JOIN DmSanPham E ON E.DmSanPhamID = C.DmSanPhamREF
                        ) TD

    END

```
