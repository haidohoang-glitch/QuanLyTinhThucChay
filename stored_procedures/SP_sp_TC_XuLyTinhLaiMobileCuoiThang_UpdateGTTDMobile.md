# Stored Procedure: `sp_TC_XuLyTinhLaiMobileCuoiThang_UpdateGTTDMobile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-14 15:05:41.723000
- **Ngày sửa cuối**: 2017-10-02 15:20:03.770000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@pSoHopDong` | `nvarchar(100)` | No |
| `@pDmBannerID` | `int(4)` | No |
| `@pNgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
-- sp_TC_XuLyTinhLaiMobileCuoiThang_UpdateGTTDMobile 'QC0480917' , 530451 , '2017-09-29'
CREATE PROCEDURE [dbo].[sp_TC_XuLyTinhLaiMobileCuoiThang_UpdateGTTDMobile] 
	-- Add the parameters for the stored procedure here
    @pSoHopDong NVARCHAR(50) ,
    @pDmBannerID INT ,
    @pNgayThucHien DATETIME
AS
    BEGIN
	
        DECLARE @SoHopDong NVARCHAR(50) ,
            @NgayThucHien DATETIME ,
            @HopDongChiTietREF INT ,
            @DonViTinh NVARCHAR(10) ,
            @DmSanPhamREF INT ,
            @DmBanner INT ,
            @GiaTriHopDong FLOAT ,
            @GiamGia FLOAT ,
            @ThanhTien FLOAT ,
            @SoLuongDCHD INT ,
            @SoLuong INT ,
            @DmNhomNganhREF INT ,
            @TenNhomNganh NVARCHAR(200) ,
            @DonGia FLOAT ,
            @DonGiaTheoDonVi FLOAT ,
            @ChietKhau FLOAT ,
            @GhiChu NVARCHAR(4000) ,
            @NgayNhanHopDongBanCung DATETIME ,
            @NgayChuyenHDChoKT DATETIME ,
            @NhanHopDong NVARCHAR(200) ,
            @SysNhanVienREF INT ,
            @NgayNhanBanFax DATETIME



        SET @SoHopDong = @pSoHopDong
        SET @NgayThucHien = @pNgayThucHien


        --SET @DonViTinh = 'VIEW'
        SET @DmSanPhamREF = 342
        SET @GhiChu = N'Tinh lai mobile cuoi thang'
        SET @DmBanner = @pDmBannerID



        DECLARE icursor CURSOR
        FOR
            SELECT DISTINCT
                    HopDongChiTietID
            FROM    dbo.HopDongChiTiet CT
                    INNER JOIN dbo.HopDong HD ON HD.HopDongID = CT.HopDongFK
            WHERE   HD.SoHopDong = @SoHopDong
                    AND DmSanPhamREF = 342
                    AND CT.DeletedStatus = 0

        OPEN icursor  

        FETCH NEXT FROM icursor   
INTO @HopDongChiTietREF

        WHILE @@FETCH_STATUS = 0
            BEGIN  
    
                SET @GiaTriHopDong = ISNULL(( SELECT    GiaTriHopDong
                                              FROM      HopDong
                                              WHERE     SoHopDong = @SoHopDong
                                            ), 0)
                SET @GiamGia = ISNULL(( SELECT  GiamGia
                                        FROM    dbo.HopDongChiTiet
                                        WHERE   HopDongChiTietID = @HopDongChiTietREF
                                      ), 0)
                SET @ThanhTien = ISNULL(( SELECT    ThanhTien
                                          FROM      dbo.HopDongChiTiet
                                          WHERE     HopDongChiTietID = @HopDongChiTietREF
                                        ), 0)
                SET @SoLuongDCHD = ISNULL(( SELECT  SoLuong
                                            FROM    dbo.HopDongChiTiet
                                            WHERE   HopDongChiTietID = @HopDongChiTietREF
                                          ), 0)
                SET @SoLuong = ISNULL(( SELECT  CASE WHEN DonViTinh = 'CPM'
                                                     THEN SoLuong * 1000
                                                     ELSE SoLuong
                                                END
                                        FROM    dbo.HopDongChiTiet
                                        WHERE   HopDongChiTietID = @HopDongChiTietREF
                                      ), 0)
                SET @DmNhomNganhREF = ISNULL(( SELECT   DmNhomNganhREF
                                               FROM     dbo.HopDongChiTiet
                                               WHERE    HopDongChiTietID = @HopDongChiTietREF
                                             ), 0)
                SET @TenNhomNganh = ISNULL(( SELECT TenNhomNganh
                                             FROM   dbo.HopDongChiTiet
                                             WHERE  HopDongChiTietID = @HopDongChiTietREF
                                           ), '')
                SET @DonGia = ISNULL(( SELECT   DonGia
                                       FROM     dbo.HopDongChiTiet
                                       WHERE    HopDongChiTietID = @HopDongChiTietREF
                                     ), 0)
                SET @DonGiaTheoDonVi = ISNULL(( SELECT  CASE WHEN DonViTinh = 'CPM'
                                                             THEN DonGia
                                                              / 1000
                                                             ELSE DonGia
                                                        END
                                                FROM    dbo.HopDongChiTiet
                                                WHERE   HopDongChiTietID = @HopDongChiTietREF
                                              ), 0)
                SET @ChietKhau = ISNULL(( SELECT    ChietKhau
                                          FROM      dbo.HopDongChiTiet
                                          WHERE     HopDongChiTietID = @HopDongChiTietREF
                                        ), 0)
                SET @NgayNhanHopDongBanCung = ( SELECT TOP 1
                                                        NgayNhanHopDongBanCung
                                                FROM    dbo.HopDong
                                                WHERE   SoHopDong = @SoHopDong
                                              )
                SET @NgayChuyenHDChoKT = ( SELECT TOP 1
                                                    NgayChuyenHopDongChoKeToan
                                           FROM     dbo.HopDong
                                           WHERE    SoHopDong = @SoHopDong
                                         )
                SET @NgayNhanBanFax = ( SELECT TOP 1
                                                NgayNhanBanFax
                                        FROM    dbo.HopDong
                                        WHERE   SoHopDong = @SoHopDong
                                      )
                SET @NhanHopDong = ISNULL(( SELECT  NhanHopDong
                                            FROM    HopDong
                                            WHERE   SoHopDong = @SoHopDong
                                          ), 0)
                SET @SysNhanVienREF = ( SELECT TOP 1
                                                SysNhanVienREF
                                        FROM    dbo.HopDong
                                        WHERE   SoHopDong = @SoHopDong
                                      )

                INSERT  INTO dbo.ThucChayDaTinh
                SELECT  NEWID() ,
                        T.HopDongID1 ,
                        T.SoHopDong ,
                        T.DmMaHopDongREF ,
                        T.TenMaHopDong ,
                        T.NgayDanhSoHopDong ,
                        T.NgayKyHopDong ,
                        T.NhanHopDong ,
                        T.NgayNhanBanFax ,
                        T.NgayNhanHopDongBanCung ,
                        T.NgayChuyenHopDongChoKeToan ,
                        T.So ,
                        T.Thang ,
                        T.Nam ,
                        T.GiaTriHopDong ,
                        T.CongNo ,
                        T.HopDongChiTietREF ,
                        T.DangSuDung ,
                        T.IsGiayPhep ,
                        T.TrangThaiHopDong ,
                        T.IsBanCung ,
                        T.DmPhongBanREF ,
                        T.TenPhongBan ,
                        T.DmBoPhanREF ,
                        T.TenBoPhan ,
                        T.DmNhomLamViecREF ,
                        T.TenNhomLamViec ,
                        T.DmDiaDiemLamViecREF ,
                        T.TenDiaDiemLamViec ,
                        T.SysNhanVienREF ,
                        ISNULL(T.TenDangNhap, '') TenDangNhap ,
                        ISNULL(T.TenNhanVien, '') TenNhanVien ,
                        T.TenKhachHang ,
                        T.NhanHang ,
                        T.DmNhomNganhREF ,
                        T.TenNhomNganh ,
                        T.DmHinhThucQuangCao ,
                        T.TenHinhThucQuangCao ,
                        DmSanPhamREF ,
                        TenSanPham ,
                        T.DmNhomWebsiteREF ,
                        T.TenNhomWebsite ,
                        T.DmChuyenMucREF ,
                        T.TenChuyenMuc ,
                        T.DmLoaiBannerREF ,
                        T.TenLoaiBanner ,
                        T.DmViTriREF ,
                        T.TenViTri ,
                        T.DotChayHopDong ,
                        T.SoLuongDotChayHD ,
                        T.DotChayBooking ,
                        T.SoLuongDotChayBooking ,
                        T.SoLuong ,
                        T.DonViTinh ,
                        T.DonGia ,
                        T.DonGiaTheoDonVi ,
                        T.ChietKhau ,
                        T.GiamGia ,
                        T.ThanhTien ,
                        T.TiLeTuVan ,
                        T.ChiPhiTuVan ,
                        T.IsKhuyenMai ,
                        T.KhuyenMai ,
                        T.DmBannerREF ,	--A.DmBannerREF,
                        T.DmChienDichREF ,
                        T.DmWebsiteREF ,
                        T.TenWebsite ,
                        0 TongView ,
                        0 TongClick ,
                        0 TongSoBaiViet ,
                        0 SoLuongThucChay ,
                        @NgayThucHien NgayThucHien ,
                        T.mobiletcdt GiaTriThayDoi ,
                        0 ThanhTienThucChayTruocChietKhau ,
                        0 GiaTriChietKhau ,
                        0 ThanhTienSauTrietKhauThucChay ,
                        0 AS GiaTriHoaHongThucChay ,
                        0 ThanhTienThucThu ,
                        0 AS ThanhTienKM ,
                        0 AS SoLuongThucChayKM ,
                        T.sllthm SoLuongLechTreoHa ,
                        T.ttlthm ThanhTienLechTreoHa ,
                        GETDATE() ,
                        GETDATE() ,
                        0 IsPheDuyet ,
                        '' PheDuyetBy ,
                        '' PheDuyetAt ,
                        T.sltdm ,	-- SoLuongThayDoi
                        0 ,
                        0 ,
                        @GhiChu
                FROM    ( SELECT    ISNULL(b.HopDongID1, a.HopDongID) HopDongID1,
                                    ISNULL(b.SoHopDong, a.SoHopDong) SoHopDong,
                                    ISNULL(b.DmMaHopDongREF, a.DmMaHopDongREF) DmMaHopDongREF,
                                    ISNULL(b.TenMaHopDong, a.TenMaHopDong) TenMaHopDong,
                                    ISNULL(b.NgayDanhSoHopDong,
                                           a.NgayDanhSoHopDong) NgayDanhSoHopDong,
                                    ISNULL(b.NgayKyHopDong, a.NgayKyHopDong) NgayKyHopDong,
                                    ISNULL(b.NhanHopDong, a.NhanHopDong) NhanHopDong,
                                    ISNULL(b.NgayNhanBanFax, a.NgayNhanBanFax) NgayNhanBanFax,
                                    ISNULL(b.NgayNhanHopDongBanCung,
                                           a.NgayNhanHopDongBanCung) NgayNhanHopDongBanCung,
                                    ISNULL(b.NgayChuyenHopDongChoKeToan,
                                           a.NgayChuyenHopDongChoKeToan) NgayChuyenHopDongChoKeToan,
                                    ISNULL(b.So, a.So) So,
                                    ISNULL(b.Thang, a.Thang) Thang,
                                    ISNULL(b.Nam, a.Nam) Nam,
                                    ISNULL(b.GiaTriHopDong, a.GiaTriHopDong) GiaTriHopDong,
                                    ISNULL(b.CongNo, a.CongNo) CongNo,
                                    ISNULL(b.HopDongChiTietREF,
                                           a.HopDongChiTietREF) HopDongChiTietREF,
                                    ISNULL(b.DangSuDung, a.DangSuDung) DangSuDung,
                                    ISNULL(b.IsGiayPhep, a.IsGiayPhep) IsGiayPhep,
                                    ISNULL(b.TrangThaiHopDong,
                                           a.TrangThaiHopDong) TrangThaiHopDong,
                                    ISNULL(b.IsBanCung, a.IsBanCung) IsBanCung,
                                    ISNULL(b.DmPhongBanREF, a.DmPhongBanREF) DmPhongBanREF,
                                    ISNULL(b.TenPhongBan, a.TenPhongBan) TenPhongBan,
                                    ISNULL(b.DmBoPhanREF, a.DmBoPhanREF) DmBoPhanREF,
                                    ISNULL(b.TenBoPhan, a.TenBoPhan) TenBoPhan,
                                    ISNULL(b.DmNhomLamViecREF,
                                           a.DmNhomLamViecREF) DmNhomLamViecREF,
                                    ISNULL(b.TenNhomLamViec, a.TenNhomLamViec) TenNhomLamViec,
                                    ISNULL(b.DmDiaDiemLamViecREF,
                                           a.DmDiaDiemLamViecREF) DmDiaDiemLamViecREF,
                                    ISNULL(b.TenDiaDiemLamViec,
                                           a.TenDiaDiemLamViec) TenDiaDiemLamViec,
                                    ISNULL(b.SysNhanVienREF, a.SysNhanVienREF) SysNhanVienREF,
                                    ISNULL(b.TenDangNhap, a.TenDangNhap) TenDangNhap,
                                    ISNULL(b.TenNhanVien, a.TenNhanVien) TenNhanVien,
                                    ISNULL(b.TenKhachHang, a.TenKhachHang) TenKhachHang,
                                    ISNULL(b.NhanHang, a.NhanHang) NhanHang,
                                    ISNULL(b.DmNhomNganhREF, a.DmNhomNganhREF) DmNhomNganhREF,
                                    ISNULL(b.TenNhomNganh, a.TenNhomNganh) TenNhomNganh,
                                    ISNULL(b.DmHinhThucQuangCao,
                                           a.DmHinhThucQuangCao) DmHinhThucQuangCao,
                                    ISNULL(b.TenHinhThucQuangCao,
                                           a.TenHinhThucQuangCao) TenHinhThucQuangCao,
                                    ISNULL(b.DmSanPhamREF, a.DmSanPhamREF) DmSanPhamREF,
                                    ISNULL(b.TenSanPham, a.TenSanPham) TenSanPham,
                                    ISNULL(b.DmNhomWebsiteREF,
                                           a.DmNhomWebsiteREF) DmNhomWebsiteREF,
                                    ISNULL(b.TenNhomWebsite, a.TenNhomWebsite) TenNhomWebsite,
                                    ISNULL(b.DmChuyenMucREF, a.DmChuyenMucREF) DmChuyenMucREF,
                                    ISNULL(b.TenChuyenMuc, a.TenChuyenMuc) TenChuyenMuc,
                                    ISNULL(b.DmLoaiBannerREF,
                                           a.DmLoaiBannerREF) DmLoaiBannerREF,
                                    ISNULL(b.TenLoaiBanner, a.TenLoaiBanner) TenLoaiBanner,
                                    ISNULL(b.DmViTriREF, a.DmViTriREF) DmViTriREF,
                                    ISNULL(b.TenViTri, a.TenViTri) TenViTri,
                                    ISNULL(b.DotChayHopDong, a.DotChayHopDong) DotChayHopDong,
                                    ISNULL(b.SoLuongDotChayHD,
                                           a.SoLuongDotChayHD) SoLuongDotChayHD,
                                    ISNULL(b.DotChayBooking, a.DotChayBooking) DotChayBooking,
                                    ISNULL(b.SoLuongDotChayBooking,
                                           a.SoLuongDotChayBooking) SoLuongDotChayBooking,
                                    ISNULL(b.SoLuong, a.SoLuong) SoLuong,
                                    ISNULL(b.DonViTinh, a.DonViTinh) DonViTinh,
                                    ISNULL(b.DonGia, a.DonGia) DonGia,
                                    ISNULL(b.DonGiaTheoDonVi,
                                           a.DonGiaTheoDonVi) DonGiaTheoDonVi,
                                    ISNULL(b.ChietKhau, a.ChietKhau) ChietKhau,
                                    ISNULL(b.GiamGia, a.GiamGia) GiamGia,
                                    ISNULL(b.ThanhTien, a.ThanhTien) ThanhTien,
                                    ISNULL(b.TiLeTuVan, a.TiLeTuVan) TiLeTuVan,
                                    ISNULL(b.ChiPhiTuVan, a.ChiPhiTuVan) ChiPhiTuVan ,
                                    ISNULL(b.IsKhuyenMai, a.IsKhuyenMai) IsKhuyenMai,
                                    ISNULL(b.KhuyenMai, a.KhuyenMai) KhuyenMai,
                                    ISNULL(b.DmBannerREF, a.DmBannerREF) DmBannerREF,
                                    ISNULL(b.DmChienDichREF, a.DmChienDichREF) DmChienDichREF,
                                    ISNULL(b.DmWebsiteREF, a.DmWebsiteREF) DmWebsiteREF,
                                    ISNULL(b.TenWebsite, a.TenWebsite) TenWebsite,
                                    b.tt1 ,
                                    b.sl1 ,
                                    b.sllth1 ,
                                    b.ttlth1 ,
                                    ISNULL(b.tt1, 0) - ISNULL(a.tt, 0) mobiletcdt ,
                                    ISNULL(b.sl1, 0) - ISNULL(a.sl, 0) sltdm ,
                                    ( ISNULL(b.sllth1, 0) - ISNULL(a.sllth, 0) ) sllthm ,
                                    ( ISNULL(b.ttlth1, 0) - ISNULL(a.ttlth, 0) ) ttlthm
                          FROM      ( SELECT    [HopDongID] ,
                                                [SoHopDong] ,
                                                [DmMaHopDongREF] ,
                                                [TenMaHopDong] ,
                                                [NgayDanhSoHopDong] ,
                                                [NgayKyHopDong] ,
                                                @NhanHopDong [NhanHopDong] ,
                                                @NgayNhanBanFax [NgayNhanBanFax] ,
                                                @NgayNhanHopDongBanCung [NgayNhanHopDongBanCung] ,
                                                @NgayChuyenHDChoKT [NgayChuyenHopDongChoKeToan] ,
                                                [So] ,
                                                [Thang] ,
                                                [Nam] ,
                                                @GiaTriHopDong [GiaTriHopDong] ,
                                                [CongNo] ,
                                                [HopDongChiTietREF] ,
                                                1 [DangSuDung] ,
                                                [IsGiayPhep] ,
                                                1 [TrangThaiHopDong] ,
                                                1 [IsBanCung] ,
                                                [DmPhongBanREF] ,
                                                [TenPhongBan] ,
                                                [DmBoPhanREF] ,
                                                [TenBoPhan] ,
                                                [DmNhomLamViecREF] ,
                                                [TenNhomLamViec] ,
                                                [DmDiaDiemLamViecREF] ,
                                                [TenDiaDiemLamViec] ,
                                                @SysNhanVienREF [SysNhanVienREF] ,
                                                [TenDangNhap] ,
                                                [TenNhanVien] ,
                                                [TenKhachHang] ,
                                                [NhanHang] ,
                                                @DmNhomNganhREF [DmNhomNganhREF] ,
                                                @TenNhomNganh [TenNhomNganh] ,
                                                [DmHinhThucQuangCao] ,
                                                [TenHinhThucQuangCao] ,
                                                [DmSanPhamREF] ,
                                                [TenSanPham] ,
                                                5000 [DmNhomWebsiteREF] ,
                                                'Default' [TenNhomWebsite] ,
                                                -1 [DmChuyenMucREF] ,
                                                '' [TenChuyenMuc] ,
                                                1 [DmLoaiBannerREF] ,
                                                '' [TenLoaiBanner] ,
                                                [DmViTriREF] ,
                                                [TenViTri] ,
                                                '' [DotChayHopDong] ,
                                                @SoLuongDCHD [SoLuongDotChayHD] ,
                                                0 [DotChayBooking] ,
                                                0 [SoLuongDotChayBooking] ,
                                                @SoLuong [SoLuong] ,
                                                [DonViTinh] ,
                                                @DonGia [DonGia] ,
                                                @DonGiaTheoDonVi [DonGiaTheoDonVi] ,
                                                @ChietKhau [ChietKhau] ,
                                                @GiamGia [GiamGia] ,
                                                @ThanhTien [ThanhTien] ,
                                                [TiLeTuVan] ,
                                                [ChiPhiTuVan] ,
                                                [IsKhuyenMai] ,
                                                0 [KhuyenMai] ,
                                                [DmBannerREF] ,
                                                [DmChienDichREF] ,
                                                [DmWebsiteREF] ,
                                                [TenWebsite] ,
                                                SUM(ISNULL([ThanhTienSauTrietKhauThucChay],
                                                           0)
                                                    + ISNULL([GiaTriThayDoi],
                                                             0)) tt ,
                                                SUM(ISNULL(tcdt.SoLuongThucChay,
                                                           0)) sl ,
                                                SUM(ISNULL(tcdt.SoLuongThucChayLechTreoHa,
                                                           0)) sllth ,
                                                SUM(ISNULL(tcdt.ThanhTienLechTreoHa,
                                                           0)) ttlth
                                      FROM      dbo.ThucChayDaTinh tcdt
                                      WHERE     tcdt.DmSanPhamREF = @DmSanPhamREF
                                                AND tcdt.SoHopDong = @SoHopDong
                                                AND HopDongChiTietREF = @HopDongChiTietREF
                                                        --AND tcdt.DonViTinh = @DonViTinh
                                                AND NgayThucHien <= @NgayThucHien
                                                AND tcdt.DmBannerREF = @DmBanner
                                      GROUP BY  [HopDongID] ,
                                                [SoHopDong] ,
                                                [DmMaHopDongREF] ,
                                                [TenMaHopDong] ,
                                                [NgayDanhSoHopDong] ,
                                                [NgayKyHopDong] ,
                            -- [NhanHopDong],
                            -- [NgayNhanBanFax],
                             --[NgayNhanHopDongBanCung],
                             --[NgayChuyenHopDongChoKeToan],
                                                [So] ,
                                                [Thang] ,
                                                [Nam] ,
                             --[GiaTriHopDong],
                                                [CongNo] ,
                                                [HopDongChiTietREF] ,
                                                [IsGiayPhep] ,
                                                [DmPhongBanREF] ,
                                                [TenPhongBan] ,
                                                [DmBoPhanREF] ,
                                                [TenBoPhan] ,
                                                [DmNhomLamViecREF] ,
                                                [TenNhomLamViec] ,
                                                [DmDiaDiemLamViecREF] ,
                                                [TenDiaDiemLamViec] ,
                            -- [SysNhanVienREF],
                                                [TenDangNhap] ,
                                                [TenNhanVien] ,
                                                [TenKhachHang] ,
                                                [NhanHang] ,
                             --[DmNhomNganhREF],
                             --[TenNhomNganh],
                                                [DmHinhThucQuangCao] ,
                                                [TenHinhThucQuangCao] ,
                                                [DmSanPhamREF] ,
                                                [TenSanPham] ,
                                                [DmViTriREF] ,
                                                [TenViTri] ,
                             --[SoLuongDotChayHD],
                             --[SoLuong],
                                                [DonViTinh] ,
                             --[DonGia],
                             --[DonGiaTheoDonVi],
                             --[ChietKhau],
                             --[GiamGia],
                             --[ThanhTien],
                                                [TiLeTuVan] ,
                                                [ChiPhiTuVan] ,
                                                [IsKhuyenMai] ,
                                                [DmBannerREF] ,
                                                [DmChienDichREF] ,
                                                [DmWebsiteREF] ,
                                                [TenWebsite]
                                    ) a
                                    FULL OUTER JOIN ( SELECT  [HopDongID] [HopDongID1] ,
                                                              [SoHopDong] ,
                                                              [DmMaHopDongREF] ,
                                                              [TenMaHopDong] ,
                                                              [NgayDanhSoHopDong] ,
                                                              [NgayKyHopDong] ,
                                                              @NhanHopDong [NhanHopDong] ,
                                                              @NgayNhanBanFax [NgayNhanBanFax] ,
                                                              @NgayNhanHopDongBanCung [NgayNhanHopDongBanCung] ,
                                                              @NgayChuyenHDChoKT [NgayChuyenHopDongChoKeToan] ,
                                                              [So] ,
                                                              [Thang] ,
                                                              [Nam] ,
                                                              @GiaTriHopDong [GiaTriHopDong] ,
                                                              [CongNo] ,
                                                              [HopDongChiTietREF] ,
                                                              1 [DangSuDung] ,
                                                              [IsGiayPhep] ,
                                                              1 [TrangThaiHopDong] ,
                                                              1 [IsBanCung] ,
                                                              [DmPhongBanREF] ,
                                                              [TenPhongBan] ,
                                                              [DmBoPhanREF] ,
                                                              [TenBoPhan] ,
                                                              [DmNhomLamViecREF] ,
                                                              [TenNhomLamViec] ,
                                                              [DmDiaDiemLamViecREF] ,
                                                              [TenDiaDiemLamViec] ,
                                                              @SysNhanVienREF [SysNhanVienREF] ,
                                                              [TenDangNhap] ,
                                                              [TenNhanVien] ,
                                                              [TenKhachHang] ,
                                                              [NhanHang] ,
                                                              @DmNhomNganhREF [DmNhomNganhREF] ,
                                                              @TenNhomNganh [TenNhomNganh] ,
                                                              [DmHinhThucQuangCao] ,
                                                              [TenHinhThucQuangCao] ,
                                                              [DmSanPhamREF] ,
                                                              [TenSanPham] ,
                                                              5000 [DmNhomWebsiteREF] ,
                                                              'Default' [TenNhomWebsite] ,
                                                              -1 [DmChuyenMucREF] ,
                                                              '' [TenChuyenMuc] ,
                                                              1 [DmLoaiBannerREF] ,
                                                              '' [TenLoaiBanner] ,
                                                              [DmViTriREF] ,
                                                              [TenViTri] ,
                                                              '' [DotChayHopDong] ,
                                                              @SoLuongDCHD [SoLuongDotChayHD] ,
                                                              0 [DotChayBooking] ,
                                                              0 [SoLuongDotChayBooking] ,
                                                              @SoLuong [SoLuong] ,
                                                              [DonViTinh] ,
                                                              @DonGia [DonGia] ,
                                                              @DonGiaTheoDonVi [DonGiaTheoDonVi] ,
                                                              @ChietKhau [ChietKhau] ,
                                                              @GiamGia [GiamGia] ,
                                                              @ThanhTien [ThanhTien] ,
                                                              [TiLeTuVan] ,
                                                              [ChiPhiTuVan] ,
                                                              [IsKhuyenMai] ,
                                                              0 [KhuyenMai] ,
                                                              [DmBannerREF] ,
                                                              [DmChienDichREF] ,
                                                              [DmWebsiteREF] ,
                                                              [TenWebsite] ,
                                                              SUM(ISNULL([ThanhTienSauTrietKhauThucChay],
                                                              0)
                                                              + ISNULL([GiaTriThayDoi],
                                                              0)) tt1 ,
                                                              SUM(ISNULL(tcdt.SoLuongThucChay,
                                                              0)) sl1 ,
                                                              SUM(ISNULL(tcdt.SoLuongThucChayLechTreoHa,
                                                              0)) sllth1 ,
                                                              SUM(ISNULL(tcdt.ThanhTienLechTreoHa,
                                                              0)) ttlth1
                                                      FROM    dbo.ThucChayDaTinh_TinhLaiCuoiThang tcdt
                                                      WHERE   tcdt.DmSanPhamREF = @DmSanPhamREF
                                                              AND tcdt.SoHopDong = @SoHopDong
                                                              AND HopDongChiTietREF = @HopDongChiTietREF
                                                              --AND tcdt.DonViTinh = @DonViTinh
                                                              AND tcdt.NgayThucHien <= @NgayThucHien
                                                              AND tcdt.DmBannerREF = @DmBanner
                                                      GROUP BY [HopDongID] ,
                                                              [SoHopDong] ,
                                                              [DmMaHopDongREF] ,
                                                              [TenMaHopDong] ,
                                                              [NgayDanhSoHopDong] ,
                                                              [NgayKyHopDong] ,
                                 --[NhanHopDong],
                                 -- [NgayNhanBanFax],
                                 -- [NgayNhanHopDongBanCung],
                                 -- [NgayChuyenHopDongChoKeToan],
                                                              [So] ,
                                                              [Thang] ,
                                                              [Nam] ,
                                 --[GiaTriHopDong],
                                                              [CongNo] ,
                                                              [HopDongChiTietREF] ,
                                                              [IsGiayPhep] ,
                                                              [DmPhongBanREF] ,
                                                              [TenPhongBan] ,
                                                              [DmBoPhanREF] ,
                                                              [TenBoPhan] ,
                                                              [DmNhomLamViecREF] ,
                                                              [TenNhomLamViec] ,
                                                              [DmDiaDiemLamViecREF] ,
                                                              [TenDiaDiemLamViec] ,
                                 -- [SysNhanVienREF],
                                                              [TenDangNhap] ,
                                                              [TenNhanVien] ,
                                                              [TenKhachHang] ,
                                                              [NhanHang] ,
                                  --[DmNhomNganhREF],
                                  --[TenNhomNganh],
                                                              [DmHinhThucQuangCao] ,
                                                              [TenHinhThucQuangCao] ,
                                                              [DmSanPhamREF] ,
                                                              [TenSanPham] ,
                                                              [DmLoaiBannerREF] ,
                                                              [TenLoaiBanner] ,
                                                              [DmViTriREF] ,
                                                              [TenViTri] ,
                                  --[SoLuongDotChayHD],
                                  --[SoLuong],
                                                              [DonViTinh] ,
                                  --[DonGia],
                                  --[DonGiaTheoDonVi],
                                  --[ChietKhau],
                                  --[GiamGia],
                                  --[ThanhTien],
                                                              [TiLeTuVan] ,
                                                              [ChiPhiTuVan] ,
                                                              [IsKhuyenMai] ,
                                                              [DmBannerREF] ,
                                                              [DmChienDichREF] ,
                                                              [DmWebsiteREF] ,
                                                              [TenWebsite]
                                                    ) b ON ( a.[HopDongID] = b.[HopDongID1]
                                                             AND a.[SoHopDong] = b.[SoHopDong]
                                                             AND a.[HopDongChiTietREF] = b.[HopDongChiTietREF]
                                                             AND a.[DmPhongBanREF] = b.[DmPhongBanREF]
                                                             AND a.[TenPhongBan] = b.[TenPhongBan]
                                                             AND a.[DmBoPhanREF] = b.[DmBoPhanREF]
                                                             AND a.[TenBoPhan] = b.[TenBoPhan]
                                                             AND a.[DmNhomLamViecREF] = b.[DmNhomLamViecREF]
                                                             AND a.[TenNhomLamViec] = b.[TenNhomLamViec]
                                                             AND a.[DmDiaDiemLamViecREF] = b.[DmDiaDiemLamViecREF]
                                                             AND a.[TenDiaDiemLamViec] = b.[TenDiaDiemLamViec]
                                                             AND a.[SysNhanVienREF] = b.[SysNhanVienREF]
                                                             AND a.[TenDangNhap] = b.[TenDangNhap]
                                                             AND a.[TenNhanVien] = b.[TenNhanVien]
                                                             AND a.[TenKhachHang] = b.[TenKhachHang]
                                                             AND a.[NhanHang] = b.[NhanHang]
                                                             AND a.[DmNhomNganhREF] = b.[DmNhomNganhREF]
                                                             AND a.[TenNhomNganh] = b.[TenNhomNganh]
                                                             AND a.[DmHinhThucQuangCao] = b.[DmHinhThucQuangCao]
                                                             AND a.[TenHinhThucQuangCao] = b.[TenHinhThucQuangCao]
                                                             AND a.[DmSanPhamREF] = b.[DmSanPhamREF]
                                                             AND a.[TenSanPham] = b.[TenSanPham]
                                                             AND a.[DmViTriREF] = b.[DmViTriREF]
                                                             AND a.[TenViTri] = b.[TenViTri]
                                                             AND a.[DonViTinh] = b.[DonViTinh]
                                                             AND a.[IsKhuyenMai] = b.[IsKhuyenMai]
                                                             AND a.[DmWebsiteREF] = b.[DmWebsiteREF]
                                                             AND a.[TenWebsite] = b.[TenWebsite]
                                                           )
                          WHERE     ( ( ISNULL(a.tt, 0) - ISNULL(b.tt1, 0) <> 0 )
                                      OR ( ISNULL(a.sl, 0) - ISNULL(b.sl1, 0) <> 0 )
                                      OR ( ISNULL(a.sllth, 0)
                                           - ISNULL(b.sllth1, 0) <> 0 )
                                      OR ( ISNULL(a.ttlth, 0)
                                           - ISNULL(b.ttlth1, 0) <> 0 )
                                    )
                                            --AND a.HopDongID IS NULL
                        ) T
       
	 
                FETCH NEXT FROM icursor   
    INTO @HopDongChiTietREF 
            END   
        CLOSE icursor;  
        DEALLOCATE icursor;  




    END

```
