# Stored Procedure: `sp_TC_DoiTruVaTinhLai_PR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-01-11 14:29:38.843000
- **Ngày sửa cuối**: 2019-11-11 09:35:23.647000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |
| `@NgaythucHien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@List_HopDongChiTietREF` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

/*
EXEC [dbo].[sp_TC_DoiTruVaTinhLai_PR] 1007328,'2018-11-09',637,''
*/


CREATE PROCEDURE [dbo].[sp_TC_DoiTruVaTinhLai_PR]
    @HopDongID INT ,
    @NgaythucHien DATETIME ,
	@DmSanPhamREF INT,
    @List_HopDongChiTietREF NVARCHAR(200)
AS
    BEGIN
        DECLARE @NgayGioiHanTinh DATETIME ,
            @NoteThongTinThayDoi NVARCHAR(200) 
        SET @NgayGioiHanTinh = '2014-01-01'
        SET @NoteThongTinThayDoi = 'DOITRUGIATRI_PR'
	
        --PRINT @HopDongID
		--1. INSERT THONG TIN GIA TRI THAY DOI TRUOC DO GIAM
        INSERT  INTO dbo.ThucChayDaTinh
                ( ThucChayDaTinhID
                , HopDongID
                , SoHopDong
                , DmMaHopDongREF
                , TenMaHopDong
                , NgayDanhSoHopDong
                , NgayKyHopDong
                , NhanHopDong
                , NgayNhanBanFax
                , NgayNhanHopDongBanCung
                , NgayChuyenHopDongChoKeToan
                , So
                , Thang
                , Nam
                , GiaTriHopDong
                , CongNo
                , HopDongChiTietREF
                , DangSuDung
                , IsGiayPhep
                , TrangThaiHopDong
                , IsBanCung
                , DmPhongBanREF
                , TenPhongBan
                , DmBoPhanREF
                , TenBoPhan
                , DmNhomLamViecREF
                , TenNhomLamViec
                , DmDiaDiemLamViecREF
                , TenDiaDiemLamViec
                , SysNhanVienREF
                , TenDangNhap
                , TenNhanVien
                , TenKhachHang
                , NhanHang
                , DmNhomNganhREF
                , TenNhomNganh
                , DmHinhThucQuangCao
                , TenHinhThucQuangCao
                , DmSanPhamREF
                , TenSanPham
                , DmNhomWebsiteREF
                , TenNhomWebsite
                , DmChuyenMucREF
                , TenChuyenMuc
                , DmLoaiBannerREF
                , TenLoaiBanner
                , DmViTriREF
                , TenViTri
                , DotChayHopDong
                , SoLuongDotChayHD
                , DotChayBooking
                , SoLuongDotChayBooking
                , SoLuong
                , DonViTinh
                , DonGia
                , DonGiaTheoDonVi
                , ChietKhau
                , GiamGia
                , ThanhTien
                , TiLeTuVan
                , ChiPhiTuVan
                , IsKhuyenMai
                , KhuyenMai
                , DmBannerREF
                , DmChienDichREF
                , DmWebsiteREF
                , TenWebsite
                , TongViewThucChay
                , TongClickThucChay
                , TongSoBaiViet
                , SoLuongThucChay
                , NgayThucHien
                , GiaTriThayDoi
                , ThanhTienThucChayTruocTrietKhau
                , GiaTriTrietKhauThucChay
                , ThanhTienSauTrietKhauThucChay
                , GiaTriHoaHongThucChay
                , ThanhTienThucThu
                , ThanhTienKM
                , SoLuongThucChayKM
                , SoLuongThucChayLechTreoHa
                , ThanhTienLechTreoHa
                , CreatedAt
                , LastModifiedAt
                , IsPheDuyet
                , PheDuyetBy
                , PheDuyetAt
                , SoLuongThayDoi
                , SoLuongKMThayDoi
                , GiaTriKMThayDoi
                , GhiChu
                )
                SELECT  NEWID() ,
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
                        @NoteThongTinThayDoi ,
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
                        0 ,
                        0 ,
                        0 ,
                        0 ,
                        @NgaythucHien ,
                        -SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) ,
                        0 ,
                        0 ,
                        0 ,
                        0 ,
                        0 ,
                        0 ,
                        0 ,
                        0 ,
                        0 ,
                        GETDATE() ,
                        GETDATE() ,
                        0 ,
                        '' ,
                        GETDATE() ,
                        -SUM(SoLuongThucChay + SoLuongThayDoi) ,
                        -SUM(SoLuongThucChayKM + SoLuongKMThayDoi) ,
                        -SUM(ThanhTienKM + GiaTriKMThayDoi) ,
                        N'Thực hiện đổi trừ giá trị toàn bộ' GhiChu
                FROM    dbo.ThucChayDaTinh
                WHERE   HopDongID = @HopDongID
                        AND NgayThucHien <= @NgaythucHien
                        AND HopDongID = @HopDongID
						AND DmSanPhamREF = @DmSanPhamREF
						AND NOT(DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18)
						--AND HopDongChiTietREF IN (SELECT CONVERT(INT,[VALUE]) FROM dbo.ASD_SPLIT(',',@List_HopDongChiTietREF))
                GROUP BY HopDongID ,
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
                        SoLuongDotChayHD ,
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
                        DotChayBooking

	    --PRINT 'Cap nhat recordstatus'    
		--2. UPDATE TRANG THAI RecordStatus = 0
		UPDATE dbo.ThucChayHopDongChiTietPR
		SET RecordStatus = 0
		WHERE HopDongREF = @HopDongID 
		AND DmSanPhamREF = @DmSanPhamREF 
		
		--PRINT 'Xoa Thong tin luu'    
		--3. XOA THONG TIN LUU 
        DELETE  FROM ThucChay_ThongTinHopDongChiTietID_PR
        WHERE   1=1
        AND HopDongChiTietID IN (SELECT HopDongChiTietID FROM dbo.HopDongChiTiet WHERE HopDongFK = @HopDongID AND DmSanPhamREF = @DmSanPhamREF)
  
		 --PRINT 'Thuc hien tinh lai'   
		--4. THUC HIEN TINH LAI
		--EXEC [dbo].[sp_TC_TinhGiaTriThayDoiThucChayDaTinh_PR_ByHopDongID]  @NgayGioiHanTinh ,@NgaythucHien, @NgaythucHien, @DmSanPhamREF , @HopDongID
		--EXEC [dbo].[sp_TC_TinhGiaTriThayDoiThucChayDaTinh_PR_ByHopDongID_TrongSo]
		--	@StartDate = @NgayGioiHanTinh ,
		--	@EndDate = @NgaythucHien ,
		--	@NgayThucHien = @NgaythucHien,
		--	@DmSanPhamREF = @DmSanPhamREF,
		--	@pHopDongID = @HopDongID

		EXEC [dbo].[sp_TC_TinhGiaTriThayDoiThucChayDaTinh_PR_ByHopDongID_TrongSo_v2]
			@StartDate = @NgayGioiHanTinh ,
			@EndDate = @NgaythucHien ,
			@NgayThucHien = @NgaythucHien,
			@DmSanPhamREF = @DmSanPhamREF,
			@pHopDongID = @HopDongID

		--PRINT 'Cap nhat lai ngay thuc hien'  
		--5. CAP NHAT LAI GIA TRI NGAY THUC HIEN
		UPDATE dbo.ThucChayDaTinh
		SET NgayThucHien = @NgaythucHien
		WHERE HopDongID= @HopDongID
		AND DmSanPhamREF = @DmSanPhamREF
		AND GhiChu = N'Tinh lai hop dong pr bi doi tru'
		AND CONVERT(DATE,CreatedAt) = CONVERT(DATE, GETDATE())
	
END


```
