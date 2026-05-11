# Stored Procedure: `prc_insert_thucchaydatinh_bythucchaydatinh_admarket_dev`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-11 15:02:54.670000
- **Ngày sửa cuối**: 2018-10-09 14:53:02.847000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ngaythuchien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
-- exec [dbo].[prc_insert_thucchaydatinh_bythucchaydatinh_admarket_dev]  '2018-10-08'
CREATE PROCEDURE [dbo].[prc_insert_thucchaydatinh_bythucchaydatinh_admarket_dev] 
	-- Add the parameters for the stored procedure here
	@ngaythuchien datetime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	DECLARE @Count INT, @slsite INT, @v_TenWebsite NVARCHAR(2000)

	/*XU LY THONG TIN WEBSITE TRUOC KHI THUC HIEN INSERT*/
	--[dbo].[ThucChayAdmarket_ViewPlus_HopDong]

	SET @Count = 0
    SET @slsite = 0
    SET @v_TenWebsite =''

	SET @slsite = ( SELECT  COUNT(DISTINCT a.TenWebsite)
                    FROM    ( SELECT    [dbo].[GetWebsiteIDByDomainName](domain_name) DmWebsiteREF ,
                                        domain_name TenWebsite
                                FROM      [dbo].[ThucChayAdmarket_ViewPlus_HopDong]
                                WHERE     CONVERT(DATE, NgayThucHien) = @ngaythuchien
                            ) a
                    WHERE   a.DmWebsiteREF IS NULL
                    )
    IF ( @slsite > 0 )
        WHILE @Count < @slsite
            BEGIN
                SET @v_TenWebsite = ( SELECT TOP (1)
                                            TenWebsite
                                        FROM
                                            ( SELECT
                                            [dbo].[GetWebsiteIDByDomainName](domain_name) DmWebsiteREF ,
                                            domain_name TenWebsite
                                            FROM
                                             [dbo].[ThucChayAdmarket_ViewPlus_HopDong]
                                            WHERE
                                            CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                           
                                            ) a
                                        WHERE
                                            a.DmWebsiteREF IS NULL
											ORDER BY a.TenWebsite
                                    )
									
				IF @v_TenWebsite IS NOT NULL
					BEGIN
						INSERT  INTO dbo.DmWebsiteReportingdb
								( TenWebsite ,
									CreatedBy ,
									CreatedAt ,
									LastModifiedBy ,
									LastModifiedAt ,
									DeletedStatus ,
									PrintStatus ,
									RecordStatus ,
									ID
								)
						VALUES  ( @v_TenWebsite ,	-- TenWebsite - nvarchar(200)
									N'asd' ,	-- CreatedBy - nvarchar(50)
									GETDATE() ,	-- CreatedAt - datetime
									N'asd' ,	-- LastModifiedBy - nvarchar(50)
									GETDATE() ,	-- LastModifiedAt - datetime
									0 ,	-- DeletedStatus - int
									0 ,	-- PrintStatus - int
									0 ,	-- RecordStatus - int
									N'New' -- ID - nvarchar(50)
								)	
					END
                           
                SET @Count = @Count + 1
		END

	/*XU LY THONG TIN WEBSITE TRUOC KHI THUC HIEN INSERT*/
	--[dbo].ThucChayAdmarket_ADX_CPC_HopDong
	SET @Count = 0
    SET @slsite = 0
    SET @v_TenWebsite =''

	SET @slsite = ( SELECT  COUNT(DISTINCT a.TenWebsite)
                    FROM    ( SELECT    [dbo].[GetWebsiteIDByDomainName](domain_name) DmWebsiteREF ,
                                        domain_name TenWebsite
                                FROM      [dbo].ThucChayAdmarket_ADX_CPC_HopDong
                                WHERE     CONVERT(DATE, NgayThucHien) = @ngaythuchien
                            ) a
                    WHERE   a.DmWebsiteREF IS NULL
                    )
    IF ( @slsite > 0 )
        WHILE @Count < @slsite
            BEGIN
                SET @v_TenWebsite = ( SELECT TOP (1)
                                            TenWebsite
                                        FROM
                                            ( SELECT
                                            [dbo].[GetWebsiteIDByDomainName](domain_name) DmWebsiteREF ,
                                            domain_name TenWebsite
                                            FROM
                                             [dbo].ThucChayAdmarket_ADX_CPC_HopDong
                                            WHERE
                                            CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                           
                                            ) a
                                        WHERE
                                            a.DmWebsiteREF IS NULL
											ORDER BY a.TenWebsite
                                    )
									
				IF @v_TenWebsite IS NOT NULL
					BEGIN
						INSERT  INTO dbo.DmWebsiteReportingdb
								( TenWebsite ,
									CreatedBy ,
									CreatedAt ,
									LastModifiedBy ,
									LastModifiedAt ,
									DeletedStatus ,
									PrintStatus ,
									RecordStatus ,
									ID
								)
						VALUES  ( @v_TenWebsite ,	-- TenWebsite - nvarchar(200)
									N'asd' ,	-- CreatedBy - nvarchar(50)
									GETDATE() ,	-- CreatedAt - datetime
									N'asd' ,	-- LastModifiedBy - nvarchar(50)
									GETDATE() ,	-- LastModifiedAt - datetime
									0 ,	-- DeletedStatus - int
									0 ,	-- PrintStatus - int
									0 ,	-- RecordStatus - int
									N'New' -- ID - nvarchar(50)
								)	
					END
                                    

                SET @Count = @Count + 1
		END



	--DELETE FROM dbo.ThucChayDaTinh 
	--WHERE DmSanPhamREF IN( 628,144,585) and DmHinhThucQuangCao <> 42 and  NgayThucHien = @ngaythuchien

	---- view plus 
	--INSERT INTO dbo.ThucChayDaTinh
	--(
	--    ThucChayDaTinhID,
	--    HopDongID,
	--    SoHopDong,
	--    DmMaHopDongREF,
	--    TenMaHopDong,
	--    NgayDanhSoHopDong,
	--    NgayKyHopDong,
	--    NhanHopDong,
	--    NgayNhanBanFax,
	--    NgayNhanHopDongBanCung,
	--    NgayChuyenHopDongChoKeToan,
	--    So,
	--    Thang,
	--    Nam,
	--    GiaTriHopDong,
	--    CongNo,
	--    HopDongChiTietREF,
	--    DangSuDung,
	--    IsGiayPhep,
	--    TrangThaiHopDong,
	--    IsBanCung,
	--    DmPhongBanREF,
	--    TenPhongBan,
	--    DmBoPhanREF,
	--    TenBoPhan,
	--    DmNhomLamViecREF,
	--    TenNhomLamViec,
	--    DmDiaDiemLamViecREF,
	--    TenDiaDiemLamViec,
	--    SysNhanVienREF,
	--    TenDangNhap,
	--    TenNhanVien,
	--    TenKhachHang,
	--    NhanHang,
	--    DmNhomNganhREF,
	--    TenNhomNganh,
	--    DmHinhThucQuangCao,
	--    TenHinhThucQuangCao,
	--    DmSanPhamREF,
	--    TenSanPham,
	--    DmNhomWebsiteREF,
	--    TenNhomWebsite,
	--    DmChuyenMucREF,
	--    TenChuyenMuc,
	--    DmLoaiBannerREF,
	--    TenLoaiBanner,
	--    DmViTriREF,
	--    TenViTri,
	--    DotChayHopDong,
	--    SoLuongDotChayHD,
	--    DotChayBooking,
	--    SoLuongDotChayBooking,
	--    SoLuong,
	--    DonViTinh,
	--    DonGia,
	--    DonGiaTheoDonVi,
	--    ChietKhau,
	--    GiamGia,
	--    ThanhTien,
	--    TiLeTuVan,
	--    ChiPhiTuVan,
	--    IsKhuyenMai,
	--    KhuyenMai,
	--    DmBannerREF,
	--    DmChienDichREF,
	--    DmWebsiteREF,
	--    TenWebsite,
	--    TongViewThucChay,
	--    TongClickThucChay,
	--    TongSoBaiViet,
	--    SoLuongThucChay,
	--    NgayThucHien,
	--    GiaTriThayDoi,
	--    ThanhTienThucChayTruocTrietKhau,
	--    GiaTriTrietKhauThucChay,
	--    ThanhTienSauTrietKhauThucChay,
	--    GiaTriHoaHongThucChay,
	--    ThanhTienThucThu,
	--    ThanhTienKM,
	--    SoLuongThucChayKM,
	--    SoLuongThucChayLechTreoHa,
	--    ThanhTienLechTreoHa,
	--    CreatedAt,
	--    LastModifiedAt,
	--    IsPheDuyet,
	--    PheDuyetBy,
	--    PheDuyetAt,
	--    SoLuongThayDoi,
	--    SoLuongKMThayDoi,
	--    GiaTriKMThayDoi,
	--    GhiChu
	--)
	--	SELECT
	--		newid(),
	--		0 HopDongID,
	--		'-' SoHopDong,
	--		0 DmMaHopDongREF,
	--		'' TenMaHopDong,
	--		getdate() NgayDanhSoHopDong,
	--		getdate() NgayKyHopDong,
	--		'' NhanHopDong,
	--		getdate() NgayNhanBanFax,
	--		getdate() NgayNhanHopDongBanCung,
	--		getdate() NgayChuyenHopDongChoKeToan,
	--		'0' So,
	--		0 Thang,
	--		0 Nam,
	--		0 GiaTriHopDong,
	--		0 CongNo,
	--		0 HopDongChiTietREF,
	--		5001 DangSuDung,
	--		0 IsGiayPhep,
	--		0 TrangThaiHopDong,
	--		0 IsBanCung,
	--		-1 DmPhongBanREF,
	--		'' TenPhongBan,
	--		-1 DmBoPhanREF,
	--		'' TenBoPhan,
	--		-1 DmNhomLamViecREF,
	--		'-' TenNhomLamViec,
	--		0 DmDiaDiemLamViecREF,
	--		'' TenDiaDiemLamViec,
	--		0 SysNhanVienREF,
	--		'-' TenDangNhap,
	--		'-' TenNhanVien,
	--		'' TenKhachHang,
	--		'' NhanHang,
	--		'0' DmNhomNganhREF,
	--		'' TenNhomNganh,
	--		7 DmHinhThucQuangCao,
	--		'CPC' TenHinhThucQuangCao,
	--		a.DmSanPhamREF,-------------------
	--		a.TenSanPham,---------------------
	--		0 DmNhomWebsiteREF,
	--		'' TenNhomWebsite,
	--		0 DmChuyenMucREF,
	--		'' TenChuyenMuc,
	--		0 DmLoaiBannerREF,
	--		'' TenLoaiBanner,
	--		0 DmViTriREF,
	--		'' TenViTri,
	--		'' DotChayHopDong,
	--		0 SoLuongDotChayHD,
	--		'' DotChayBooking,
	--		0 SoLuongDotChayBooking,
	--		0 SoLuong,
	--		'CLICK' DonViTinh,
	--		0 DonGia,
	--		0 DonGiaTheoDonVi,
	--		0 ChietKhau,
	--		0 GiamGia,
	--		0 ThanhTien,
	--		0 TiLeTuVan,
	--		0 ChiPhiTuVan,
	--		0 IsKhuyenMai,
	--		'' KhuyenMai,
	--		0 DmBannerREF,
	--		0 DmChienDichREF,
	--		dbo.GetWebsiteIDByDomainName(a.domain_name),-- DmWebsiteREF, -- cai nay dua vao phan moi nhe
	--		a.domain_name TenWebsite,  -- cai nay dua vao phan moi nhe
	--		0 TongViewThucChay, -- cai nay dua vao phan moi nhe
	--		0 TongClickThucChay, -- cai nay dua vao phan moi nhe
	--		0 TongSoBaiViet,
	--		sum(convert(int,ISNULL(a.domain_tt_click,0))) SoLuongThucChay, -- lay tong click thuc chay nhe 
	--		@ngaythuchien NgayThucHien, -- dien ngay vao nhe
	--		0 GiaTriThayDoi,
	--		0 ThanhTienThucChayTruocTrietKhau,
	--		0 GiaTriTrietKhauThucChay,
	--		SUM(convert(money,a.[domain_money]))/1.1 ThanhTienSauTrietKhauThucChay, -- dien gia tri  tu bang nhe
	--		0 GiaTriHoaHongThucChay,
	--		0 ThanhTienThucThu, -- dien gia tri  tu bang nhe
	--		sum(convert(money,a.[domain_promotion]))/1.1 ThanhTienKM, -- dien gia tri  tu bang nhe
	--		0 SoLuongThucChayKM, -- dien gia tri  tu bang nhe
	--		0 SoLuongThucChayLechTreoHa,
	--		0 ThanhTienLechTreoHa,
	--		GETDATE() CreatedAt,
	--		GETDATE() LastModifiedAt,
	--		'' IsPheDuyet,
	--		'' PheDuyetBy,
	--		'' PheDuyetAt,
	--		0 SoLuongThayDoi,
	--		0 SoLuongKMThayDoi,
	--		0 GiaTriKMThayDoi,
	--		'' GhiChu
	--		FROM [dbo].[ThucChayAdmarket_ViewPlus_HopDong] a WHERE (convert(money,a.[domain_money]) >0 OR convert(money,a.[domain_promotion]) > 0)
	--		AND a.NgayThucHien = @ngaythuchien and isnoibo = 0
	--		GROUP BY	a.domain_name,
	--					a.DmSanPhamREF,
	--					a.TenSanPham

	--	-- adx cpc 
	--	INSERT INTO dbo.ThucChayDaTinh
	--	(
	--	    ThucChayDaTinhID,
	--	    HopDongID,
	--	    SoHopDong,
	--	    DmMaHopDongREF,
	--	    TenMaHopDong,
	--	    NgayDanhSoHopDong,
	--	    NgayKyHopDong,
	--	    NhanHopDong,
	--	    NgayNhanBanFax,
	--	    NgayNhanHopDongBanCung,
	--	    NgayChuyenHopDongChoKeToan,
	--	    So,
	--	    Thang,
	--	    Nam,
	--	    GiaTriHopDong,
	--	    CongNo,
	--	    HopDongChiTietREF,
	--	    DangSuDung,
	--	    IsGiayPhep,
	--	    TrangThaiHopDong,
	--	    IsBanCung,
	--	    DmPhongBanREF,
	--	    TenPhongBan,
	--	    DmBoPhanREF,
	--	    TenBoPhan,
	--	    DmNhomLamViecREF,
	--	    TenNhomLamViec,
	--	    DmDiaDiemLamViecREF,
	--	    TenDiaDiemLamViec,
	--	    SysNhanVienREF,
	--	    TenDangNhap,
	--	    TenNhanVien,
	--	    TenKhachHang,
	--	    NhanHang,
	--	    DmNhomNganhREF,
	--	    TenNhomNganh,
	--	    DmHinhThucQuangCao,
	--	    TenHinhThucQuangCao,
	--	    DmSanPhamREF,
	--	    TenSanPham,
	--	    DmNhomWebsiteREF,
	--	    TenNhomWebsite,
	--	    DmChuyenMucREF,
	--	    TenChuyenMuc,
	--	    DmLoaiBannerREF,
	--	    TenLoaiBanner,
	--	    DmViTriREF,
	--	    TenViTri,
	--	    DotChayHopDong,
	--	    SoLuongDotChayHD,
	--	    DotChayBooking,
	--	    SoLuongDotChayBooking,
	--	    SoLuong,
	--	    DonViTinh,
	--	    DonGia,
	--	    DonGiaTheoDonVi,
	--	    ChietKhau,
	--	    GiamGia,
	--	    ThanhTien,
	--	    TiLeTuVan,
	--	    ChiPhiTuVan,
	--	    IsKhuyenMai,
	--	    KhuyenMai,
	--	    DmBannerREF,
	--	    DmChienDichREF,
	--	    DmWebsiteREF,
	--	    TenWebsite,
	--	    TongViewThucChay,
	--	    TongClickThucChay,
	--	    TongSoBaiViet,
	--	    SoLuongThucChay,
	--	    NgayThucHien,
	--	    GiaTriThayDoi,
	--	    ThanhTienThucChayTruocTrietKhau,
	--	    GiaTriTrietKhauThucChay,
	--	    ThanhTienSauTrietKhauThucChay,
	--	    GiaTriHoaHongThucChay,
	--	    ThanhTienThucThu,
	--	    ThanhTienKM,
	--	    SoLuongThucChayKM,
	--	    SoLuongThucChayLechTreoHa,
	--	    ThanhTienLechTreoHa,
	--	    CreatedAt,
	--	    LastModifiedAt,
	--	    IsPheDuyet,
	--	    PheDuyetBy,
	--	    PheDuyetAt,
	--	    SoLuongThayDoi,
	--	    SoLuongKMThayDoi,
	--	    GiaTriKMThayDoi,
	--	    GhiChu
	--	)
	
	--	SELECT
	--	newid(),
	--	0 HopDongID,
	--	'-' SoHopDong,
	--	0 DmMaHopDongREF,
	--	'' TenMaHopDong,
	--	getdate() NgayDanhSoHopDong,
	--	getdate() NgayKyHopDong,
	--	'' NhanHopDong,
	--	getdate() NgayNhanBanFax,
	--	getdate() NgayNhanHopDongBanCung,
	--	getdate() NgayChuyenHopDongChoKeToan,
	--	'0' So,
	--	0 Thang,
	--	0 Nam,
	--	0 GiaTriHopDong,
	--	0 CongNo,
	--	0 HopDongChiTietREF,
	--	5001 DangSuDung,
	--	0 IsGiayPhep,
	--	0 TrangThaiHopDong,
	--	0 IsBanCung,
	--	-1 DmPhongBanREF,
	--	'' TenPhongBan,
	--	-1 DmBoPhanREF,
	--	'' TenBoPhan,
	--	-1 DmNhomLamViecREF,
	--	'-' TenNhomLamViec,
	--	0 DmDiaDiemLamViecREF,
	--	'' TenDiaDiemLamViec,
	--	0 SysNhanVienREF,
	--	'-' TenDangNhap,
	--	'-' TenNhanVien,
	--	'' TenKhachHang,
	--	'' NhanHang,
	--	'0' DmNhomNganhREF,
	--	'' TenNhomNganh,
	--	7 DmHinhThucQuangCao,
	--	'CPC' TenHinhThucQuangCao,
	--	a.DmSanPhamREF DmSanPhamREF,-------------------
	--	a.TenSanPham,---------------------
	--	0 DmNhomWebsiteREF,
	--	'' TenNhomWebsite,
	--	0 DmChuyenMucREF,
	--	'' TenChuyenMuc,
	--	0 DmLoaiBannerREF,
	--	'' TenLoaiBanner,
	--	DmViTriREF DmViTriREF,
	--	TenViTri TenViTri,
	--	'' DotChayHopDong,
	--	0 SoLuongDotChayHD,
	--	'' DotChayBooking,
	--	0 SoLuongDotChayBooking,
	--	0 SoLuong,
	--	'CLICK' DonViTinh,
	--	0 DonGia,
	--	0 DonGiaTheoDonVi,
	--	0 ChietKhau,
	--	0 GiamGia,
	--	0 ThanhTien,
	--	0 TiLeTuVan,
	--	0 ChiPhiTuVan,
	--	0 IsKhuyenMai,
	--	'' KhuyenMai,
	--	0 DmBannerREF,
	--	0 DmChienDichREF,
	--	dbo.GetWebsiteIDByDomainName(a.domain_name),-- DmWebsiteREF, -- cai nay dua vao phan moi nhe
	--	a.domain_name TenWebsite,  -- cai nay dua vao phan moi nhe
	--	0 TongViewThucChay, -- cai nay dua vao phan moi nhe
	--	0 TongClickThucChay, -- cai nay dua vao phan moi nhe
	--	0 TongSoBaiViet,
	--	sum(convert(int,ISNULL(a.domain_tt_click,0))) SoLuongThucChay, -- lay tong click thuc chay nhe 
	--	@ngaythuchien NgayThucHien, -- dien ngay vao nhe
	--	0 GiaTriThayDoi,
	--	0 ThanhTienThucChayTruocTrietKhau,
	--	0 GiaTriTrietKhauThucChay,
	--	SUM(convert(money,a.domain_tt_money))/1.1 ThanhTienSauTrietKhauThucChay, -- dien gia tri  tu bang nhe
	--	0 GiaTriHoaHongThucChay,
	--	0 ThanhTienThucThu, -- dien gia tri  tu bang nhe
	--	SUM(convert(money,a.domain_tt_promotion))/1.1 ThanhTienKM, -- dien gia tri  tu bang nhe
	--	0 SoLuongThucChayKM, -- dien gia tri  tu bang nhe
	--	0 SoLuongThucChayLechTreoHa,
	--	0 ThanhTienLechTreoHa,
	--	GETDATE() CreatedAt,
	--	GETDATE() LastModifiedAt,
	--	'' IsPheDuyet,
	--	'' PheDuyetBy,
	--	'' PheDuyetAt,
	--	0 SoLuongThayDoi,
	--	0 SoLuongKMThayDoi,
	--	0 GiaTriKMThayDoi,
	--	'' GhiChu
	--	FROM [dbo].ThucChayAdmarket_ADX_CPC_HopDong a WHERE (convert(money,a.domain_tt_money) > 0 OR convert(money,a.domain_tt_promotion) > 0)
	--	AND a.NgayThucHien = @ngaythuchien and isnoibo = 0
	--	GROUP by 
	--	a.DmSanPhamREF,
	--	a.TenSanPham,
	--	a.domain_name,
	--	a.DmViTriREF,
	--	a.TenViTri
	--	------------------------------------------Nội bộ---------------------------------
 --       INSERT INTO dbo.ThucChayDaTinh
 --       (
 --           ThucChayDaTinhID,
 --           HopDongID,
 --           SoHopDong,
 --           DmMaHopDongREF,
 --           TenMaHopDong,
 --           NgayDanhSoHopDong,
 --           NgayKyHopDong,
 --           NhanHopDong,
 --           NgayNhanBanFax,
 --           NgayNhanHopDongBanCung,
 --           NgayChuyenHopDongChoKeToan,
 --           So,
 --           Thang,
 --           Nam,
 --           GiaTriHopDong,
 --           CongNo,
 --           HopDongChiTietREF,
 --           DangSuDung,
 --           IsGiayPhep,
 --           TrangThaiHopDong,
 --           IsBanCung,
 --           DmPhongBanREF,
 --           TenPhongBan,
 --           DmBoPhanREF,
 --           TenBoPhan,
 --           DmNhomLamViecREF,
 --           TenNhomLamViec,
 --           DmDiaDiemLamViecREF,
 --           TenDiaDiemLamViec,
 --           SysNhanVienREF,
 --           TenDangNhap,
 --           TenNhanVien,
 --           TenKhachHang,
 --           NhanHang,
 --           DmNhomNganhREF,
 --           TenNhomNganh,
 --           DmHinhThucQuangCao,
 --           TenHinhThucQuangCao,
 --           DmSanPhamREF,
 --           TenSanPham,
 --           DmNhomWebsiteREF,
 --           TenNhomWebsite,
 --           DmChuyenMucREF,
 --           TenChuyenMuc,
 --           DmLoaiBannerREF,
 --           TenLoaiBanner,
 --           DmViTriREF,
 --           TenViTri,
 --           DotChayHopDong,
 --           SoLuongDotChayHD,
 --           DotChayBooking,
 --           SoLuongDotChayBooking,
 --           SoLuong,
 --           DonViTinh,
 --           DonGia,
 --           DonGiaTheoDonVi,
 --           ChietKhau,
 --           GiamGia,
 --           ThanhTien,
 --           TiLeTuVan,
 --           ChiPhiTuVan,
 --           IsKhuyenMai,
 --           KhuyenMai,
 --           DmBannerREF,
 --           DmChienDichREF,
 --           DmWebsiteREF,
 --           TenWebsite,
 --           TongViewThucChay,
 --           TongClickThucChay,
 --           TongSoBaiViet,
 --           SoLuongThucChay,
 --           NgayThucHien,
 --           GiaTriThayDoi,
 --           ThanhTienThucChayTruocTrietKhau,
 --           GiaTriTrietKhauThucChay,
 --           ThanhTienSauTrietKhauThucChay,
 --           GiaTriHoaHongThucChay,
 --           ThanhTienThucThu,
 --           ThanhTienKM,
 --           SoLuongThucChayKM,
 --           SoLuongThucChayLechTreoHa,
 --           ThanhTienLechTreoHa,
 --           CreatedAt,
 --           LastModifiedAt,
 --           IsPheDuyet,
 --           PheDuyetBy,
 --           PheDuyetAt,
 --           SoLuongThayDoi,
 --           SoLuongKMThayDoi,
 --           GiaTriKMThayDoi,
 --           GhiChu
 --       )
    
	--	SELECT
	--	newid(),
	--	0 HopDongID,
	--	'-' SoHopDong,
	--	310 DmMaHopDongREF,
	--	'NB' TenMaHopDong,
	--	getdate() NgayDanhSoHopDong,
	--	getdate() NgayKyHopDong,
	--	'' NhanHopDong,
	--	getdate() NgayNhanBanFax,
	--	getdate() NgayNhanHopDongBanCung,
	--	getdate() NgayChuyenHopDongChoKeToan,
	--	'0' So,
	--	0 Thang,
	--	0 Nam,
	--	0 GiaTriHopDong,
	--	0 CongNo,
	--	0 HopDongChiTietREF,
	--	5001 DangSuDung,
	--	0 IsGiayPhep,
	--	0 TrangThaiHopDong,
	--	0 IsBanCung,
	--	-1 DmPhongBanREF,
	--	'' TenPhongBan,
	--	-1 DmBoPhanREF,
	--	'' TenBoPhan,
	--	-1 DmNhomLamViecREF,
	--	'-' TenNhomLamViec,
	--	0 DmDiaDiemLamViecREF,
	--	'' TenDiaDiemLamViec,
	--	0 SysNhanVienREF,
	--	'-' TenDangNhap,
	--	'-' TenNhanVien,
	--	'' TenKhachHang,
	--	'' NhanHang,
	--	'0' DmNhomNganhREF,
	--	'' TenNhomNganh,
	--	7 DmHinhThucQuangCao,
	--	'CPC' TenHinhThucQuangCao,
	--	a.DmSanPhamREF,-------------------
	--	a.TenSanPham,---------------------
	--	0 DmNhomWebsiteREF,
	--	'' TenNhomWebsite,
	--	0 DmChuyenMucREF,
	--	'' TenChuyenMuc,
	--	0 DmLoaiBannerREF,
	--	'' TenLoaiBanner,
	--	0 DmViTriREF,
	--	'' TenViTri,
	--	'' DotChayHopDong,
	--	0 SoLuongDotChayHD,
	--	'' DotChayBooking,
	--	0 SoLuongDotChayBooking,
	--	0 SoLuong,
	--	'CLICK' DonViTinh,
	--	0 DonGia,
	--	0 DonGiaTheoDonVi,
	--	0 ChietKhau,
	--	0 GiamGia,
	--	0 ThanhTien,
	--	0 TiLeTuVan,
	--	0 ChiPhiTuVan,
	--	0 IsKhuyenMai,
	--	'' KhuyenMai,
	--	0 DmBannerREF,
	--	0 DmChienDichREF,
	--	dbo.GetWebsiteIDByDomainName(a.domain_name),-- DmWebsiteREF, -- cai nay dua vao phan moi nhe
	--	a.domain_name TenWebsite,  -- cai nay dua vao phan moi nhe
	--	0 TongViewThucChay, -- cai nay dua vao phan moi nhe
	--	0 TongClickThucChay, -- cai nay dua vao phan moi nhe
	--	0 TongSoBaiViet,
	--	sum(convert(int,ISNULL(a.domain_tt_click,0))) SoLuongThucChay, -- lay tong click thuc chay nhe 
	--	@ngaythuchien NgayThucHien, -- dien ngay vao nhe
	--	0 GiaTriThayDoi,
	--	0 ThanhTienThucChayTruocTrietKhau,
	--	0 GiaTriTrietKhauThucChay,
	--	SUM(convert(money,a.[domain_money]))/1.1 ThanhTienSauTrietKhauThucChay, -- dien gia tri  tu bang nhe
	--	0 GiaTriHoaHongThucChay,
	--	0 ThanhTienThucThu, -- dien gia tri  tu bang nhe
	--	sum(convert(money,a.[domain_promotion]))/1.1 ThanhTienKM, -- dien gia tri  tu bang nhe
	--	0 SoLuongThucChayKM, -- dien gia tri  tu bang nhe
	--	0 SoLuongThucChayLechTreoHa,
	--	0 ThanhTienLechTreoHa,
	--	GETDATE() CreatedAt,
	--	GETDATE() LastModifiedAt,
	--	'' IsPheDuyet,
	--	'' PheDuyetBy,
	--	'' PheDuyetAt,
	--	0 SoLuongThayDoi,
	--	0 SoLuongKMThayDoi,
	--	0 GiaTriKMThayDoi,
	--	'' GhiChu
	--	from [dbo].[ThucChayAdmarket_ViewPlus_HopDong] a where (convert(money,a.[domain_money]) >0 OR convert(money,a.[domain_promotion]) > 0)
	--	AND a.NgayThucHien = @ngaythuchien and isnoibo = 1
	--	group by 
	--	a.domain_name,
	--	a.DmSanPhamREF,
	--	a.TenSanPham

	--	-- adx cpc 
	--INSERT INTO dbo.ThucChayDaTinh
	--(
	--    ThucChayDaTinhID,
	--    HopDongID,
	--    SoHopDong,
	--    DmMaHopDongREF,
	--    TenMaHopDong,
	--    NgayDanhSoHopDong,
	--    NgayKyHopDong,
	--    NhanHopDong,
	--    NgayNhanBanFax,
	--    NgayNhanHopDongBanCung,
	--    NgayChuyenHopDongChoKeToan,
	--    So,
	--    Thang,
	--    Nam,
	--    GiaTriHopDong,
	--    CongNo,
	--    HopDongChiTietREF,
	--    DangSuDung,
	--    IsGiayPhep,
	--    TrangThaiHopDong,
	--    IsBanCung,
	--    DmPhongBanREF,
	--    TenPhongBan,
	--    DmBoPhanREF,
	--    TenBoPhan,
	--    DmNhomLamViecREF,
	--    TenNhomLamViec,
	--    DmDiaDiemLamViecREF,
	--    TenDiaDiemLamViec,
	--    SysNhanVienREF,
	--    TenDangNhap,
	--    TenNhanVien,
	--    TenKhachHang,
	--    NhanHang,
	--    DmNhomNganhREF,
	--    TenNhomNganh,
	--    DmHinhThucQuangCao,
	--    TenHinhThucQuangCao,
	--    DmSanPhamREF,
	--    TenSanPham,
	--    DmNhomWebsiteREF,
	--    TenNhomWebsite,
	--    DmChuyenMucREF,
	--    TenChuyenMuc,
	--    DmLoaiBannerREF,
	--    TenLoaiBanner,
	--    DmViTriREF,
	--    TenViTri,
	--    DotChayHopDong,
	--    SoLuongDotChayHD,
	--    DotChayBooking,
	--    SoLuongDotChayBooking,
	--    SoLuong,
	--    DonViTinh,
	--    DonGia,
	--    DonGiaTheoDonVi,
	--    ChietKhau,
	--    GiamGia,
	--    ThanhTien,
	--    TiLeTuVan,
	--    ChiPhiTuVan,
	--    IsKhuyenMai,
	--    KhuyenMai,
	--    DmBannerREF,
	--    DmChienDichREF,
	--    DmWebsiteREF,
	--    TenWebsite,
	--    TongViewThucChay,
	--    TongClickThucChay,
	--    TongSoBaiViet,
	--    SoLuongThucChay,
	--    NgayThucHien,
	--    GiaTriThayDoi,
	--    ThanhTienThucChayTruocTrietKhau,
	--    GiaTriTrietKhauThucChay,
	--    ThanhTienSauTrietKhauThucChay,
	--    GiaTriHoaHongThucChay,
	--    ThanhTienThucThu,
	--    ThanhTienKM,
	--    SoLuongThucChayKM,
	--    SoLuongThucChayLechTreoHa,
	--    ThanhTienLechTreoHa,
	--    CreatedAt,
	--    LastModifiedAt,
	--    IsPheDuyet,
	--    PheDuyetBy,
	--    PheDuyetAt,
	--    SoLuongThayDoi,
	--    SoLuongKMThayDoi,
	--    GiaTriKMThayDoi,
	--    GhiChu
	--)
	--	SELECT
	--	newid(),
	--	0 HopDongID,
	--	'-' SoHopDong,
	--	310 DmMaHopDongREF,
	--	'NB' TenMaHopDong,
	--	getdate() NgayDanhSoHopDong,
	--	getdate() NgayKyHopDong,
	--	'' NhanHopDong,
	--	getdate() NgayNhanBanFax,
	--	getdate() NgayNhanHopDongBanCung,
	--	getdate() NgayChuyenHopDongChoKeToan,
	--	'0' So,
	--	0 Thang,
	--	0 Nam,
	--	0 GiaTriHopDong,
	--	0 CongNo,
	--	0 HopDongChiTietREF,
	--	5001 DangSuDung,
	--	0 IsGiayPhep,
	--	0 TrangThaiHopDong,
	--	0 IsBanCung,
	--	-1 DmPhongBanREF,
	--	'' TenPhongBan,
	--	-1 DmBoPhanREF,
	--	'' TenBoPhan,
	--	-1 DmNhomLamViecREF,
	--	'-' TenNhomLamViec,
	--	0 DmDiaDiemLamViecREF,
	--	'' TenDiaDiemLamViec,
	--	0 SysNhanVienREF,
	--	'-' TenDangNhap,
	--	'-' TenNhanVien,
	--	'' TenKhachHang,
	--	'' NhanHang,
	--	'0' DmNhomNganhREF,
	--	'' TenNhomNganh,
	--	7 DmHinhThucQuangCao,
	--	'CPC' TenHinhThucQuangCao,
	--	a.DmSanPhamREF DmSanPhamREF,-------------------
	--	a.TenSanPham,---------------------
	--	0 DmNhomWebsiteREF,
	--	'' TenNhomWebsite,
	--	0 DmChuyenMucREF,
	--	'' TenChuyenMuc,
	--	0 DmLoaiBannerREF,
	--	'' TenLoaiBanner,
	--	DmViTriREF DmViTriREF,
	--	TenViTri TenViTri,
	--	'' DotChayHopDong,
	--	0 SoLuongDotChayHD,
	--	'' DotChayBooking,
	--	0 SoLuongDotChayBooking,
	--	0 SoLuong,
	--	'CLICK' DonViTinh,
	--	0 DonGia,
	--	0 DonGiaTheoDonVi,
	--	0 ChietKhau,
	--	0 GiamGia,
	--	0 ThanhTien,
	--	0 TiLeTuVan,
	--	0 ChiPhiTuVan,
	--	0 IsKhuyenMai,
	--	'' KhuyenMai,
	--	0 DmBannerREF,
	--	0 DmChienDichREF,
	--	dbo.GetWebsiteIDByDomainName(a.domain_name),-- DmWebsiteREF, -- cai nay dua vao phan moi nhe
	--	a.domain_name TenWebsite,  -- cai nay dua vao phan moi nhe
	--	0 TongViewThucChay, -- cai nay dua vao phan moi nhe
	--	0 TongClickThucChay, -- cai nay dua vao phan moi nhe
	--	0 TongSoBaiViet,
	--	sum(convert(int,ISNULL(a.domain_tt_click,0))) SoLuongThucChay, -- lay tong click thuc chay nhe 
	--	@ngaythuchien NgayThucHien, -- dien ngay vao nhe
	--	0 GiaTriThayDoi,
	--	0 ThanhTienThucChayTruocTrietKhau,
	--	0 GiaTriTrietKhauThucChay,
	--	SUM(convert(money,a.domain_tt_money))/1.1 ThanhTienSauTrietKhauThucChay, -- dien gia tri  tu bang nhe
	--	0 GiaTriHoaHongThucChay,
	--	0 ThanhTienThucThu, -- dien gia tri  tu bang nhe
	--	SUM(convert(money,a.domain_tt_promotion))/1.1 ThanhTienKM, -- dien gia tri  tu bang nhe
	--	0 SoLuongThucChayKM, -- dien gia tri  tu bang nhe
	--	0 SoLuongThucChayLechTreoHa,
	--	0 ThanhTienLechTreoHa,
	--	GETDATE() CreatedAt,
	--	GETDATE() LastModifiedAt,
	--	'' IsPheDuyet,
	--	'' PheDuyetBy,
	--	'' PheDuyetAt,
	--	0 SoLuongThayDoi,
	--	0 SoLuongKMThayDoi,
	--	0 GiaTriKMThayDoi,
	--	'' GhiChu
	--	FROM [dbo].ThucChayAdmarket_ADX_CPC_HopDong a WHERE (convert(money,a.domain_tt_money) > 0 OR convert(money,a.domain_tt_promotion) > 0)
	--	AND a.NgayThucHien = @ngaythuchien and isnoibo = 1
	--	GROUP BY a.DmSanPhamREF,
	--			a.TenSanPham,
	--			a.domain_name,
	--			a.DmViTriREF,
	--			a.TenViTri
   
END


```
