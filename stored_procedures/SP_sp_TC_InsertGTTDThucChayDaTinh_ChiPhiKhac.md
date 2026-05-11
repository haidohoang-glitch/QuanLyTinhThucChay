# Stored Procedure: `sp_TC_InsertGTTDThucChayDaTinh_ChiPhiKhac`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-12 09:21:11.090000
- **Ngày sửa cuối**: 2020-04-13 17:19:52.923000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmNhanHangREF` | `nvarchar(400)` | No |
| `@GiaTriThayDoi` | `bigint(8)` | No |
| `@SoLuongThayDoi` | `int(4)` | No |
| `@ThucChayHopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
--EXEC [ThucChay_InsertThucChayDaTinh_ChiPhiKhac] '2014-06-11 00:00:00.000','2014-06-11 15:42:55.690'
-------------------------------------------------------------
CREATE PROCEDURE [dbo].[sp_TC_InsertGTTDThucChayDaTinh_ChiPhiKhac]
    @NgayThucHien DATETIME ,
    @HopDongChiTietREF INT ,
    @DmNhanHangREF NVARCHAR(200) ,
    @GiaTriThayDoi BIGINT ,
    @SoLuongThayDoi INT,
	@ThucChayHopDongChiTietID INT
AS
    BEGIN
        DECLARE @Note NVARCHAR(300)
        SET @Note = 'PS GTTD ChiPhiKhac Thuc treo bi huy'
	
        INSERT  dbo.ThucChayDaTinh
                ( ThucChayDaTinhID ,
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
                  HopDongChiTietREF ,
                  DangSuDung ,
                  IsGiayPhep ,
                  TrangThaiHopDong ,
                  IsBanCung ,
                  DmPhongBanREF ,
                  TenPhongBan ,
                  DmBoPhanREF ,
                  TenBoPhan ,
                  DmNhomLamViecREF ,
                  TenNhomLamViec ,
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
                  DotChayBooking ,
                  SoLuongDotChayBooking ,
                  SoLuong ,
                  DonViTinh ,
                  DonGia ,
                  DonGiaTheoDonVi ,
                  ChietKhau ,
                  GiamGia ,
                  ThanhTien ,
                  TiLeTuVan ,
                  ChiPhiTuVan ,
                  IsKhuyenMai ,
                  KhuyenMai ,
                  DmBannerREF ,
                  DmChienDichREF ,
                  DmWebsiteREF ,
                  TenWebsite ,
                  TongViewThucChay ,
                  TongClickThucChay ,
                  TongSoBaiViet ,
                  SoLuongThucChay ,
                  NgayThucHien ,
                  GiaTriThayDoi ,
                  ThanhTienThucChayTruocTrietKhau ,
                  GiaTriTrietKhauThucChay ,
                  ThanhTienSauTrietKhauThucChay ,
                  GiaTriHoaHongThucChay ,
                  ThanhTienThucThu ,
                  ThanhTienKM ,
                  SoLuongThucChayKM ,
                  SoLuongThucChayLechTreoHa ,
                  ThanhTienLechTreoHa ,
                  CreatedAt ,
                  LastModifiedAt ,
                  IsPheDuyet ,
                  PheDuyetBy ,
                  PheDuyetAt ,
                  SoLuongThayDoi ,
                  SoLuongKMThayDoi ,
                  GiaTriKMThayDoi ,
                  GhiChu
	            )
                SELECT TOP 1
                        NEWID() AS ID ,
                        [HopDongID] ,
                        [SoHopDong] ,
                        [DmMaHopDongREF] ,
                        [TenMaHopDong] ,
                        [NgayDanhSoHopDong] ,
                        [NgayKyHopDong] ,
                        [NhanHopDong] ,
                        [NgayNhanBanFax] ,
                        [NgayNhanHopDongBanCung] ,
                        [NgayChuyenHopDongChoKeToan] ,
                        [So] ,
                        [Thang] ,
                        [Nam] ,
                        [GiaTriHopDong] ,
                        [CongNo] ,
                        [HopDongChiTietREF] ,
                        [DangSuDung] ,
                        [IsGiayPhep] ,
                        [TrangThaiHopDong] ,
                        [IsBanCung] ,
                        [DmPhongBanREF] ,
                        [TenPhongBan] ,
                        [DmBoPhanREF] ,
                        [TenBoPhan] ,
                        [DmNhomLamViecREF] ,
                        [TenNhomLamViec] ,
                        [DmDiaDiemLamViecREF] ,
                        [TenDiaDiemLamViec] ,
                        [SysNhanVienREF] ,
                        [TenDangNhap] ,
                        [TenNhanVien] ,
                        [TenKhachHang] ,
                        @DmNhanHangREF [NhanHang] ,
                        [DmNhomNganhREF] ,
                        [TenNhomNganh] ,
                        [DmHinhThucQuangCao] ,
                        [TenHinhThucQuangCao] ,
                        [DmSanPhamREF] ,
                        [TenSanPham] ,
                        [DmNhomWebsiteREF] ,
                        [TenNhomWebsite] ,
                        [DmChuyenMucREF] ,
                        [TenChuyenMuc] ,
                        [DmLoaiBannerREF] ,
                        [TenLoaiBanner] ,
                        [DmViTriREF] ,
                        [TenViTri] ,
                        [DotChayHopDong] ,
                        [SoLuongDotChayHD] ,
                        @ThucChayHopDongChiTietID [DotChayBooking] ,
                        [SoLuongDotChayBooking] ,
                        [SoLuong] ,
                        [DonViTinh] ,
                        [DonGia] ,
                        [DonGiaTheoDonVi] ,
                        [ChietKhau] ,
                        [GiamGia] ,
                        [ThanhTien] ,
                        [TiLeTuVan] ,
                        [ChiPhiTuVan] ,
                        [IsKhuyenMai] ,
                        [KhuyenMai] ,
                        [DmBannerREF] ,
                        [DmChienDichREF] ,
                        [DmWebsiteREF] ,
                        [TenWebsite] ,
                        0 [TongViewThucChay] ,
                        0 [TongClickThucChay] ,
                        0 [TongSoBaiViet] ,
                        0 [SoLuongThucChay] ,
                        @NgayThucHien NgayThucHien ,
                        (CASE WHEN ChietKhau <> 100 THEN @GiaTriThayDoi
						ELSE 0
						END) [GiaTriThayDoi] ,
                        0 [ThanhTienThucChayTruocTrietKhau] ,
                        0 [GiaTriTrietKhauThucChay] ,
                        0 [ThanhTienSauTrietKhauThucChay] ,
                        0 [GiaTriHoaHongThucChay] ,
                        0 [ThanhTienThucThu] ,
                        0 [ThanhTienKM] ,
                        0 [SoLuongThucChayKM] ,
                        0 [SoLuongThucChayLechTreoHa] ,
                        0 [ThanhTienLechTreoHa] ,
                        GETDATE() [CreatedAt] ,
                        GETDATE() [LastModifiedAt] ,
                        0 [IsPheDuyet] ,
                        '' [PheDuyetBy] ,
                        '' [PheDuyetAt] ,
                        (CASE WHEN ChietKhau <> 100 THEN @SoLuongThayDoi
						ELSE 0
						END) [SoLuongThayDoi] ,
                        -(SoLuongKMThayDoi + SoLuongThucChayKM) [SoLuongKMThayDoi] ,
                        -(ThanhTienKM + GiaTriKMThayDoi) [GiaTriKMThayDoi] ,
                        @Note Note
                FROM    dbo.[ThucChayDaTinh]
                WHERE   HopDongChiTietREF = @HopDongChiTietREF
                        AND NgayThucHien < @NgayThucHien
						AND DotChayBooking = CONVERT(NVARCHAR(1000), @ThucChayHopDongChiTietID)
						AND ((ThanhTienKM + GiaTriKMThayDoi) <> 0 OR (@GiaTriThayDoi <> 0))
                ORDER BY NgayThucHien DESC ,
                        LastModifiedAt DESC

 		
		
	--INSERT INTO dbo.ThucChay_LogNNTinhGiaTriThayDoi		
		
        --SELECT  NEWID() ThuChay_LogNNTinhGiaTriThayDoiID ,
        --        HopDongID HopDongREF ,
        --        SoHopDong ,
        --        HopDongChiTietREF ,
        --        DmSanPhamREF ,
        --        DmWebsiteREF ,
        --        NgayThucHien ,
        --        GiaTriThayDoi ,
        --        0 GiaSauCK1 ,
        --        0 Soluong1 ,
        --        0 GiaSauCK2 ,
        --        0 Soluong2 ,
        --        N'Update Giá Trị thay đổi' NoiDungLog ,
        --        N'Update Giá Trị thay đổi' NguonLog ,
        --        'Đổi tên sản phẩm' GhiChu ,
        --        'ThucChay' CreatedBy ,
        --        GETDATE() CreatedAt ,
        --        'ThucChay' LastModifiedBy ,
        --        GETDATE() LastModifiedAt ,
        --        0 DeletedStatus ,
        --        0 PrintStatus ,
        --        0 RecordStatus
        --FROM    dbo.ThucChayDaTinh tcdt
        --WHERE   tcdt.NgayThucHien = @NgayThucHien
        --        AND GiaTriThayDoi = @GiaTriThayDoi
        --        AND HopDongChiTietREF = @HopDongChiTietREF		
    END


```
