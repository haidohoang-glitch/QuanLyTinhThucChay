# Stored Procedure: `sp_TC_UpdateGiaTriThayDoi_ThucChay_GiaiPhapCongNghe_SanPhamChinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-12 09:26:06.620000
- **Ngày sửa cuối**: 2018-05-04 16:43:07.713000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [dbo].[ThucChay_UpdateGiaTriThayDoi_ThucChay_GiaiPhapCongNghe_SanPhamChinh] '2017-01-09'
CREATE PROCEDURE [dbo].[sp_TC_UpdateGiaTriThayDoi_ThucChay_GiaiPhapCongNghe_SanPhamChinh]
	-- Add the parameters for the stored procedure here
    @NgayThucHien DATETIME
AS
    BEGIN
        DECLARE @HopDongChiTietID INT ,
            @HopDongID INT ,
            @Note NVARCHAR(MAX) ,
            @IsThayDoi INT ,
            @ThanhTien BIGINT ,
            @SoLuong INT

        DECLARE Cursor_GPCN CURSOR
        FOR
            SELECT  HopDongFK ,
                    HopDongChiTietID ,
                    ThanhTien ,
                    SoLuong
            FROM    HopDongChiTiet
            WHERE   DmSanPhamREF IN ( 370, 339, 342, 598, 775,240 )
                    AND DeletedStatus = 0
                    AND ( DmLoaiNenTangREF = 8 --Retargeting & Content base
							OR DmSanPhamREF = 775
						) 
                    AND NOT ( ( HopDongChiTiet.DmLoaiBannerREF IN ( 18 ) )
                              OR ( HopDongChiTiet.DmLoaiREF = 13 )
                            )-- --Khong tinh thuc chay cho HTQC Mua Ngoai
                    AND ( CASE WHEN CreatedAt >= LastModifiedAt
                               THEN CONVERT(DATE, CreatedAt)
                               ELSE CONVERT(DATE, LastModifiedAt)
                          END ) = CONVERT(DATE, @NgayThucHien)
        OPEN Cursor_GPCN
        FETCH NEXT FROM Cursor_GPCN   INTO @HopDongID, @HopDongChiTietID,
            @ThanhTien, @SoLuong
        WHILE @@FETCH_STATUS = 0
            BEGIN
		 
                SET @IsThayDoi = ( SELECT   COUNT(a.HopDongChiTietREF)
                                   FROM     ( SELECT    HopDongChiTietREF ,
                                                        SUM(ThanhTienSauTrietKhauThucChay
                                                            + GiaTriThayDoi) THANHTIENTHUCCHAY
                                              FROM      dbo.ThucChayDaTinh
                                              WHERE     HopDongChiTietREF = @HopDongChiTietID
                                                        AND NgayThucHien < @NgayThucHien
                                              GROUP BY  HopDongChiTietREF
                                            ) a
                                   WHERE    a.THANHTIENTHUCCHAY <> @ThanhTien
                                 )

                IF ( @IsThayDoi <> 0 )
                    BEGIN
                        SET @Note = N'Thay đổi giá trị thanh tiền '
                            + CONVERT(NVARCHAR(200), @ThanhTien) + ' Ngày:'
                            + CONVERT(NVARCHAR(200), @NgayThucHien, 120)
                        INSERT  INTO dbo.ThucChayDaTinh
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
                                SELECT  TCDT.*
                                FROM    ( SELECT    NEWID() AS ID ,
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
                                                    [NhanHang] ,
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
                                                    [DotChayBooking] ,
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
                                                    -SUM([ThanhTienSauTrietKhauThucChay]
                                                         + [GiaTriThayDoi]) [GiaTriThayDoi] ,
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
                                                    -SUM([SoLuongThucChay]
                                                         + [SoLuongThayDoi]) [SoLuongThayDoi] ,
                                                    -SUM([SoLuongThucChayKM]
                                                         + [SoLuongKMThayDoi]) [SoLuongKMThayDoi] ,
                                                    -SUM([ThanhTienKM]
                                                         + [GiaTriKMThayDoi]) [GiaTriKMThayDoi] ,
                                                    @Note + N' giam' Note
                                          FROM      [ThucChayDaTinh]
                                          WHERE     HopDongID = @HopDongID
                                                    AND HopDongChiTietREF = @HopDongChiTietID
                                                    AND NgayThucHien < @NgayThucHien
                                          GROUP BY  [HopDongID] ,
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
                                                    [NhanHang] ,
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
                                                    [DotChayBooking] ,
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
                                                    [TenWebsite]
                                        ) TCDT
                                WHERE   TCDT.GiaTriThayDoi <> 0
		
		------------
                        IF @IsThayDoi IN ( 1 )
                            INSERT  INTO dbo.ThucChayDaTinh
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
                                    SELECT  TCDT.*
                                    FROM    ( SELECT    NEWID() AS ID ,
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
                                                        [NhanHang] ,
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
                                                        [DotChayBooking] ,
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
                                                        @ThanhTien [GiaTriThayDoi] ,
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
                                                        @SoLuong [SoLuongThayDoi] ,
                                                        0 [SoLuongKMThayDoi] ,
                                                        0 [GiaTriKMThayDoi] ,
                                                        @Note + N' tang' Note
                                              FROM      [ThucChayDaTinh]
                                              WHERE     HopDongID = @HopDongID
                                                        AND HopDongChiTietREF = @HopDongChiTietID
                                                        AND NgayThucHien < @NgayThucHien
                                              GROUP BY  [HopDongID] ,
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
                                                        [NhanHang] ,
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
                                                        [DotChayBooking] ,
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
                                                        [TenWebsite]
                                            ) TCDT
                                    WHERE   TCDT.GiaTriThayDoi <> 0
                    END
                FETCH NEXT FROM Cursor_GPCN   INTO @HopDongID,
                    @HopDongChiTietID, @ThanhTien, @SoLuong
            END
        CLOSE Cursor_GPCN;  
        DEALLOCATE Cursor_GPCN;  
	
    END



```
