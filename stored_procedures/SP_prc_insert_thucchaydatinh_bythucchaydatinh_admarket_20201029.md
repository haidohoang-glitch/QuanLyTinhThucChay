# Stored Procedure: `prc_insert_thucchaydatinh_bythucchaydatinh_admarket_20201029`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-10-29 10:35:14.797000
- **Ngày sửa cuối**: 2020-10-30 10:19:10.313000

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
--delete from ThucChayDaTinh where DmSanPhamREF = 585 and DmHinhThucQuangCao <> 42 and NgayThucHien between '2020-10-01' and '2020-10-22' and HopDongID = 0
--select * from ThucChayDaTinh where DmSanPhamREF = 585 and DmHinhThucQuangCao <> 42 and NgayThucHien between '2020-10-01' and '2020-10-22'and HopDongID = 0

-- exec [dbo].[prc_insert_thucchaydatinh_bythucchaydatinh_admarket] '2018-10-08'
/*
select * from ThucChayDaTinh where CreatedAt >'2020-10-29 17:40'

EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_20201029] '2020-10-01';
EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_20201029] '2020-10-02';
EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_20201029] '2020-10-03';
EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_20201029] '2020-10-04';
EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_20201029] '2020-10-05';
EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_20201029] '2020-10-06';
EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_20201029] '2020-10-07';
EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_20201029] '2020-10-08';
EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_20201029] '2020-10-09';
EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_20201029] '2020-10-10';
EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_20201029] '2020-10-11';
EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_20201029] '2020-10-12';
EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_20201029] '2020-10-13';
EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_20201029] '2020-10-14';
EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_20201029] '2020-10-15';
EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_20201029] '2020-10-16';
EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_20201029] '2020-10-17';
EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_20201029] '2020-10-18';
EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_20201029] '2020-10-19';
EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_20201029] '2020-10-20';
EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_20201029] '2020-10-21';
EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_20201029] '2020-10-22';
*/
CREATE PROCEDURE [dbo].[prc_insert_thucchaydatinh_bythucchaydatinh_admarket_20201029] 
	-- Add the parameters for the stored procedure here
	@ngaythuchien datetime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	DECLARE @Count INT, @slsite INT, @pTenWebiste NVARCHAR(1000) =''
	

	/*XU LY THONG TIN WEBSITE TRUOC KHI THUC HIEN INSERT*/
	--[dbo].ThucChayAdmarket_ADX_CPC_HopDong
	SET @Count = 0
    SET @slsite = 0
    SET @pTenWebiste =''

	SET @slsite = ( SELECT  COUNT(DISTINCT a.TenWebsite)
                    FROM    ( SELECT    [dbo].[GetWebsiteIDByDomainName](domain_name) DmWebsiteREF ,
                                        domain_name TenWebsite
                                FROM      [dbo].ThucChayAdmarket_ADX_CPC_HopDong_test
                                WHERE     CONVERT(DATE, NgayThucHien) = @ngaythuchien
                            ) a
                    WHERE   a.DmWebsiteREF IS NULL
                    )
    IF ( @slsite > 0 )
        BEGIN
        DECLARE Cursor_admarket_site_adx CURSOR FOR

		SELECT DISTINCT  TenWebsite
		FROM
			( SELECT [dbo].[GetWebsiteIDByDomainName](domain_name) DmWebsiteREF ,
				domain_name TenWebsite
				FROM [dbo].ThucChayAdmarket_ADX_CPC_HopDong_test
				WHERE CONVERT(DATE, NgayThucHien) = @NgayThucHien
			) a
		WHERE a.DmWebsiteREF IS NULL
			ORDER BY a.TenWebsite

		OPEN Cursor_admarket_site_adx
		FETCH NEXT FROM Cursor_admarket_site_adx INTO @pTenWebiste

		WHILE @@FETCH_STATUS = 0
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
				VALUES  ( @pTenWebiste ,	-- TenWebsite - nvarchar(200)
							N'asd' ,	-- CreatedBy - nvarchar(50)
							GETDATE() ,	-- CreatedAt - datetime
							N'asd' ,	-- LastModifiedBy - nvarchar(50)
							GETDATE() ,	-- LastModifiedAt - datetime
							0 ,	-- DeletedStatus - int
							0 ,	-- PrintStatus - int
							0 ,	-- RecordStatus - int
							N'New' -- ID - nvarchar(50)
						)	
			FETCH NEXT FROM Cursor_admarket_site_adx INTO @pTenWebiste
		END
		CLOSE Cursor_admarket_site_adx
		DEALLOCATE Cursor_admarket_site_adx
    END



	
	

		-- adx cpc 
		INSERT INTO dbo.ThucChayDaTinh
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
	
		SELECT
		newid(),
		0 HopDongID,
		'-' SoHopDong,
		0 DmMaHopDongREF,
		'' TenMaHopDong,
		getdate() NgayDanhSoHopDong,
		getdate() NgayKyHopDong,
		'' NhanHopDong,
		getdate() NgayNhanBanFax,
		getdate() NgayNhanHopDongBanCung,
		getdate() NgayChuyenHopDongChoKeToan,
		'0' So,
		0 Thang,
		0 Nam,
		0 GiaTriHopDong,
		0 CongNo,
		0 HopDongChiTietREF,
		5001 DangSuDung,
		0 IsGiayPhep,
		0 TrangThaiHopDong,
		0 IsBanCung,
		-1 DmPhongBanREF,
		'' TenPhongBan,
		-1 DmBoPhanREF,
		'' TenBoPhan,
		-1 DmNhomLamViecREF,
		'-' TenNhomLamViec,
		0 DmDiaDiemLamViecREF,
		'' TenDiaDiemLamViec,
		0 SysNhanVienREF,
		'-' TenDangNhap,
		'-' TenNhanVien,
		'' TenKhachHang,
		'' NhanHang,
		'0' DmNhomNganhREF,
		'' TenNhomNganh,
		7 DmHinhThucQuangCao,
		'CPC' TenHinhThucQuangCao,
		a.DmSanPhamREF DmSanPhamREF,-------------------
		a.TenSanPham,---------------------
		0 DmNhomWebsiteREF,
		'' TenNhomWebsite,
		0 DmChuyenMucREF,
		'' TenChuyenMuc,
		0 DmLoaiBannerREF,
		'' TenLoaiBanner,
		DmViTriREF DmViTriREF,
		TenViTri TenViTri,
		'' DotChayHopDong,
		0 SoLuongDotChayHD,
		'' DotChayBooking,
		0 SoLuongDotChayBooking,
		0 SoLuong,
		'CLICK' DonViTinh,
		0 DonGia,
		0 DonGiaTheoDonVi,
		0 ChietKhau,
		0 GiamGia,
		0 ThanhTien,
		0 TiLeTuVan,
		0 ChiPhiTuVan,
		0 IsKhuyenMai,
		'' KhuyenMai,
		0 DmBannerREF,
		0 DmChienDichREF,
		dbo.GetWebsiteIDByDomainName(a.domain_name),-- DmWebsiteREF, -- cai nay dua vao phan moi nhe
		a.domain_name TenWebsite,  -- cai nay dua vao phan moi nhe
		0 TongViewThucChay, -- cai nay dua vao phan moi nhe
		0 TongClickThucChay, -- cai nay dua vao phan moi nhe
		0 TongSoBaiViet,
		sum(convert(int,ISNULL(a.domain_tt_click,0))) SoLuongThucChay, -- lay tong click thuc chay nhe 
		@ngaythuchien NgayThucHien, -- dien ngay vao nhe
		0 GiaTriThayDoi,
		0 ThanhTienThucChayTruocTrietKhau,
		0 GiaTriTrietKhauThucChay,
		SUM(convert(money,a.domain_tt_money))/1.1 ThanhTienSauTrietKhauThucChay, -- dien gia tri  tu bang nhe
		0 GiaTriHoaHongThucChay,
		0 ThanhTienThucThu, -- dien gia tri  tu bang nhe
		SUM(convert(money,a.domain_tt_promotion))/1.1 ThanhTienKM, -- dien gia tri  tu bang nhe
		0 SoLuongThucChayKM, -- dien gia tri  tu bang nhe
		0 SoLuongThucChayLechTreoHa,
		0 ThanhTienLechTreoHa,
		GETDATE() CreatedAt,
		GETDATE() LastModifiedAt,
		'' IsPheDuyet,
		'' PheDuyetBy,
		'' PheDuyetAt,
		0 SoLuongThayDoi,
		0 SoLuongKMThayDoi,
		0 GiaTriKMThayDoi,
		'' GhiChu
		FROM [dbo].ThucChayAdmarket_ADX_CPC_HopDong_test a WHERE (convert(money,a.domain_tt_money) > 0 OR convert(money,a.domain_tt_promotion) > 0)
		AND a.NgayThucHien = @ngaythuchien and isnoibo = 0
		and DmSanPhamREF = 585
		GROUP by 
		a.DmSanPhamREF,
		a.TenSanPham,
		a.domain_name,
		a.DmViTriREF,
		a.TenViTri
		------------------------------------------Nội bộ---------------------------------
       
		-- adx cpc 
	INSERT INTO dbo.ThucChayDaTinh
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
		SELECT
		newid(),
		0 HopDongID,
		'-' SoHopDong,
		310 DmMaHopDongREF,
		'NB' TenMaHopDong,
		getdate() NgayDanhSoHopDong,
		getdate() NgayKyHopDong,
		'' NhanHopDong,
		getdate() NgayNhanBanFax,
		getdate() NgayNhanHopDongBanCung,
		getdate() NgayChuyenHopDongChoKeToan,
		'0' So,
		0 Thang,
		0 Nam,
		0 GiaTriHopDong,
		0 CongNo,
		0 HopDongChiTietREF,
		5001 DangSuDung,
		0 IsGiayPhep,
		0 TrangThaiHopDong,
		0 IsBanCung,
		-1 DmPhongBanREF,
		'' TenPhongBan,
		-1 DmBoPhanREF,
		'' TenBoPhan,
		-1 DmNhomLamViecREF,
		'-' TenNhomLamViec,
		0 DmDiaDiemLamViecREF,
		'' TenDiaDiemLamViec,
		0 SysNhanVienREF,
		'-' TenDangNhap,
		'-' TenNhanVien,
		'' TenKhachHang,
		'' NhanHang,
		'0' DmNhomNganhREF,
		'' TenNhomNganh,
		7 DmHinhThucQuangCao,
		'CPC' TenHinhThucQuangCao,
		a.DmSanPhamREF DmSanPhamREF,-------------------
		a.TenSanPham,---------------------
		0 DmNhomWebsiteREF,
		'' TenNhomWebsite,
		0 DmChuyenMucREF,
		'' TenChuyenMuc,
		0 DmLoaiBannerREF,
		'' TenLoaiBanner,
		DmViTriREF DmViTriREF,
		TenViTri TenViTri,
		'' DotChayHopDong,
		0 SoLuongDotChayHD,
		'' DotChayBooking,
		0 SoLuongDotChayBooking,
		0 SoLuong,
		'CLICK' DonViTinh,
		0 DonGia,
		0 DonGiaTheoDonVi,
		0 ChietKhau,
		0 GiamGia,
		0 ThanhTien,
		0 TiLeTuVan,
		0 ChiPhiTuVan,
		0 IsKhuyenMai,
		'' KhuyenMai,
		0 DmBannerREF,
		0 DmChienDichREF,
		dbo.GetWebsiteIDByDomainName(a.domain_name),-- DmWebsiteREF, -- cai nay dua vao phan moi nhe
		a.domain_name TenWebsite,  -- cai nay dua vao phan moi nhe
		0 TongViewThucChay, -- cai nay dua vao phan moi nhe
		0 TongClickThucChay, -- cai nay dua vao phan moi nhe
		0 TongSoBaiViet,
		sum(convert(int,ISNULL(a.domain_tt_click,0))) SoLuongThucChay, -- lay tong click thuc chay nhe 
		@ngaythuchien NgayThucHien, -- dien ngay vao nhe
		0 GiaTriThayDoi,
		0 ThanhTienThucChayTruocTrietKhau,
		0 GiaTriTrietKhauThucChay,
		SUM(convert(money,a.domain_tt_money))/1.1 ThanhTienSauTrietKhauThucChay, -- dien gia tri  tu bang nhe
		0 GiaTriHoaHongThucChay,
		0 ThanhTienThucThu, -- dien gia tri  tu bang nhe
		SUM(convert(money,a.domain_tt_promotion))/1.1 ThanhTienKM, -- dien gia tri  tu bang nhe
		0 SoLuongThucChayKM, -- dien gia tri  tu bang nhe
		0 SoLuongThucChayLechTreoHa,
		0 ThanhTienLechTreoHa,
		GETDATE() CreatedAt,
		GETDATE() LastModifiedAt,
		'' IsPheDuyet,
		'' PheDuyetBy,
		'' PheDuyetAt,
		0 SoLuongThayDoi,
		0 SoLuongKMThayDoi,
		0 GiaTriKMThayDoi,
		'' GhiChu
		FROM [dbo].ThucChayAdmarket_ADX_CPC_HopDong_test a WHERE (convert(money,a.domain_tt_money) > 0 OR convert(money,a.domain_tt_promotion) > 0)
		AND a.NgayThucHien = @ngaythuchien and isnoibo = 1
			and DmSanPhamREF = 585
		GROUP BY a.DmSanPhamREF,
				a.TenSanPham,
				a.domain_name,
				a.DmViTriREF,
				a.TenViTri
   
END


```
