# Stored Procedure: `sp_TC_TinhGiaTriThayDoiThucChayDaTinh_PR_ByHopDongID_TrongSo_bk20181031`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-10-31 14:08:27.370000
- **Ngày sửa cuối**: 2018-10-31 14:08:27.370000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@pHopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

/*
EXEC [dbo].[sp_TC_TinhGiaTriThayDoiThucChayDaTinh_PR_ByHopDongID_TrongSo]    '2014-01-01', '2018-10-14',  '2018-10-14', 141 , 1005948
*/

CREATE PROCEDURE [dbo].[sp_TC_TinhGiaTriThayDoiThucChayDaTinh_PR_ByHopDongID_TrongSo_bk20181031]
    @StartDate DATETIME ,
    @EndDate DATETIME ,
	@NgayThucHien DATETIME,
	@DmSanPhamREF INT,
    @pHopDongID INT
AS
    BEGIN

        DECLARE  @NgayGioiHanTinh DATETIME, @v_row_thucchaytreopr INT = 0, @Count INT = 0
        SET @NgayGioiHanTinh = '2014-01-01';

        DECLARE @ThucChayHopDongChiTietPRID INT ,
            @HopDongREF INT ,
            @ChietKhau FLOAT ,
            @ThucChayHopDongChiTietPrREF INT ,
            @HopDongChiTietREF INT ,
            @DmHinhThucQuangCaoREF INT ,
            @DmWebsiteREF INT ,
            @GiaTien BIGINT ,
            @SoLuong INT

		SET @v_row_thucchaytreopr = ( SELECT  COUNT(ThucChayHopDongChiTietPRID)
            FROM    dbo.ThucChayHopDongChiTietPR
            WHERE   DeletedStatus <> 1
					AND HopDongREF = @pHopDongID
					AND DmSanPhamREF = @DmSanPhamREF
                    AND RecordStatus = 0
                    AND DmHinhThucQuangCaoREF <> 0
                    AND ThoiGianBatDau >= '2014-01-01'
                    AND ( CASE WHEN CreatedAt >= LastModifiedAt
                                THEN CONVERT(DATE, CreatedAt)
                                ELSE CONVERT(DATE, LastModifiedAt)
                            END ) <= @EndDate
			)
		WHILE (@Count < @v_row_thucchaytreopr)
		BEGIN
			--XAC DINH TRONG SO CUA CAC THUC TREO PR CAN TINH THUC CHAY
			EXEC [dbo].[sp_TC_CapNhatThuTuTrongSoThucChayHopDongChiTietPR_ByHopDongSanPham]
				@EndDate = @EndDate ,
				@DmSanPhamREF = @DmSanPhamREF,
				@pHopDongID = @pHopDongID
		
			INSERT  INTO dbo.ThucChayDaTinh
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
		
            SELECT  NEWID() , T.*
            FROM    ( SELECT  DISTINCT
                                hd.HopDongID ,
                                hd.SoHopDong ,
                                hd.DmMaHopDongREF ,
                                hd.TenMaHopDong ,
                                hd.NgayDanhSoHopDong ,
                                hd.NgayKyHopDong ,
                                ISNULL(hd.NhanHopDong,
                                        '') AS NhanHopDong ,
                                hd.NgayNhanBanFax ,
                                hd.NgayNhanHopDongBanCung ,
                                hd.NgayChuyenHopDongChoKeToan ,
                                hd.So ,
                                hd.Thang ,
                                hd.Nam , 
                                hd.GiaTriHopDong ,
                                hd.CongNo ,
	                            tchpctpr.HopDongChiTietID ,
	                            hd.DangSuDung ,
                                hd.IsGiayPhep ,
                                hd.TrangThaiHopDong ,
                                hd.IsBanCung , 
		                        hd.DmPhongBanREF ,
                                ISNULL(hd.TenPhongBan,
                                        '') AS TenPhongBan ,
                                hd.DmBoPhanREF ,
                                ISNULL(hd.TenBoPhan,
                                        '') AS TenBoPhan ,
                                hd.DmNhomLamViecREF ,
                                ISNULL(hd.TenNhom, '') AS TenNhom ,
                                hd.DmDiaDiemLamViecREF ,
                                ISNULL(hd.TenDiaDiemLamViec,
                                        '') AS TenDiaDiemLamViec ,
                                hd.SysNhanVienREF ,
                                ISNULL(hd.TenDangNhap,
                                        '') AS TenDangNhap ,
                                hd.TenNhanVien ,
                                hd.TenKhachHang ,
                                tchpctpr.DmNhanHangREF AS NhanHang ,
                                0 DmNhomNganhREF ,
                                '' TenNhomNganh , 
		                        hdct.DmLoaiREF AS DmHinhThucQuangCao ,
                                hdct.TenLoai AS TenHinhThucQuangCao , 
	                            hdct.DmSanPhamREF AS DmSanPhamREF ,
                                hdct.TenSanPham ,
                                0 DmNhomWebsiteREF ,
                                '' TenNhomWebsite ,
                                tchpctpr.DmChuyenMucREF ,
                                tchpctpr.TenChuyenMuc ,
                                hdct.DmLoaiBannerREF ,
                                hdct.TenLoaiBanner ,
                                tchpctpr.DmViTriREF ,
                                tchpctpr.TenViTri ,
                                '' DotChayHopDong ,
                                0 AS SoLuongDotChayHD ,
	                            tchpctpr.ThucChayHopDongChiTietPRID DotChayBooking ,
                                0 AS SoLuongDotChayBooking , 
	                            hdct.SoLuong AS SoLuong ,
                                dbo.FormatDonViTinh(hdct.DonViTinh) DonViTinh ,
                                hdct.DonGia AS DonGia ,
                                tchpctpr.GiaTien AS DonGiaTheoDonViTinh ,
                                tchpctpr.ChietKhau ,
                                hdct.GiamGia ,
                                hdct.ThanhTien ,
                                hdct.TiLeTuVan ,
                                hdct.ChiPhiTuVan ,
                                tchpctpr.KhuyenMai IsKhuyenMai ,
                                '' KhuyenMai ,
		                        0 DmBannerREF ,--A.DmBannerREF,
                                0 DmChienDichREF ,--A.DmChienDichREF,
                                dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(tchpctpr.DmWebsiteREF) DmWebsiteREF ,
                                dbo.GetWebsiteLinkByDmWebsiteID(tchpctpr.DmWebsiteREF,
                                        tchpctpr.TenWebsite) TenWebsite ,
                                0 TongViewThucChay ,
                                0 TongClickThucChay ,
                                0 TongSoBaiViet ,
                                0  AS SoLuongThucChay ,
                                @NgayThucHien AS NgayThucHien ,
                                ISNULL(tchpctpr.GiaTien,0)* ISNULL(tchpctpr.SoLuong,0)* ( CONVERT(FLOAT, ( 100- tchpctpr.ChietKhau ))/ 100 ) AS GiaTriThayDoi ,
                                0 AS ThanhTienThucChayTruocChietKhau ,
                                0 AS GiaTriTrietKhauThucChay ,
                                0 AS ThanhTienThucChaySauChietKhau ,
                                0 AS GiaTriHoaHongThucChay ,
                                ( CASE WHEN ( tchpctpr.KhuyenMai = 1
												OR tchpctpr.ChietKhau = 100
												OR tchpctpr.GiaTien = 0
												OR tchpctpr.SoLuong = 0
												) THEN 0
                                ELSE (100- hdct.TiLeTuVan)/(ISNULL(tchpctpr.GiaTien,0)*ISNULL(tchpctpr.SoLuong,0)*(CONVERT(FLOAT,( 100- tchpctpr.ChietKhau))/ 100))
								END ) AS ThanhTienThucThu ,
                                0 AS ThanhTienKM ,
                                0 AS SoLuongThucChayKM ,
                                0 SoLuongLechTreoHa ,
                                0 ThanhTienLechTreoHa ,
                                GETDATE() CreatedAt ,
                                GETDATE() LastModifiedAt ,
                                0 IsPheDuyet ,
                                '' PheDuyetBy ,
                                '' PheDuyetAt ,
                                ( CASE
                                        WHEN tchpctpr.KhuyenMai = 0
                                        AND tchpctpr.ChietKhau <> 100
                                        THEN ISNULL(tchpctpr.SoLuong,
                                        0)
                                        ELSE 0
                                    END ) SoLuongThayDoi ,
                                ( CASE
                                        WHEN tchpctpr.KhuyenMai = 1
                                        OR tchpctpr.ChietKhau = 100
                                        THEN ISNULL(tchpctpr.SoLuong,
                                        0)
                                        ELSE 0
                                    END ) SoLuongKMThayDoi ,
                                ( CASE
                                        WHEN tchpctpr.KhuyenMai = 1
                                        OR tchpctpr.ChietKhau = 100
                                        THEN ISNULL(tchpctpr.GiaTien,
                                        0)
                                        * ISNULL(tchpctpr.SoLuong,
                                        0)
                                        ELSE 0
                                    END ) GiaTriKMThayDoi ,
                                N'Tinh giá trị thay đổi cho hop dong pr bi doi tru' GhiChu
                        FROM      ( SELECT tchpctpr.* ,T.HopDongChiTietREF HopDongChiTietID 
                                    FROM
                                        (SELECT * FROM  dbo.ThucChayHopDongChiTietPR WHERE HopDongREF = @pHopDongID) tchpctpr
                                        INNER JOIN (
												SELECT TOP (1) HopDongREF, HopDongChiTietREF, ThucChayHopDongChiTietPRID,ThuTuTrongSo 
												FROM dbo.[ThucChayHopDongChiTietPR_ThuTuTrongSo_Temp]
												WHERE HopDongREF = @pHopDongID
												ORDER BY ThuTuTrongSo, ThucChayHopDongChiTietPRID
									) T ON tchpctpr.ThucChayHopDongChiTietPRID = T.ThucChayHopDongChiTietPRID
                                ) tchpctpr
                                INNER JOIN ( SELECT --ID Hop Dong
                                        D.HopDongID ,
                                        D.SoHopDong ,
                                        D.DmMaHopDongREF ,
                                        D.TenMaHopDong , 
                                        D.NgayDanhSoHopDong ,
                                        D.NgayKyHopDong ,
                                        ISNULL(D.NhanHopDong,
                                        '') AS NhanHopDong ,
                                        D.NgayNhanBanFax ,
                                        D.NgayNhanHopDongBanCung ,
                                        D.NgayChuyenHopDongChoKeToan ,
                                        D.So ,
                                        D.Thang ,
                                        D.Nam , 
                                        D.GiaTriHopDong ,
                                        D.CongNo ,
                                        D.DangSuDung ,
                                        D.IsGiayPhep ,
                                        D.TrangThaiHopDong ,
                                        D.IsBanCung , 
                                        D.DmPhongBanREF ,
                                        ISNULL(D.TenPhongBan,
                                        '') AS TenPhongBan ,
                                        D.DmBoPhanREF ,
                                        ISNULL(D.TenBoPhan,
                                        '') AS TenBoPhan ,
                                        D.DmNhomLamViecREF ,
                                        ISNULL(D.TenNhom,
                                        '') AS TenNhom ,
                                        D.DmDiaDiemLamViecREF ,
                                        D.TenDiaDiemLamViec ,
                                        D.SysNhanVienREF ,
                                        ISNULL(D.TenDangNhap,
                                        '') AS TenDangNhap ,
                                        D.TenNhanVien ,
                                        D.TenKhachHang
                                        FROM dbo.HopDong D
                                        WHERE D.TrangThaiHopDong <> 3
											AND D.Nam >= 2013
											AND D.HopDongID = @pHopDongID
                                        ) hd ON tchpctpr.HopDongREF = hd.HopDongID
                                INNER JOIN (SELECT * FROM dbo.HopDongChiTiet WHERE HopDongFK = @pHopDongID) hdct ON tchpctpr.HopDongChiTietID = hdct.HopDongChiTietID
                                        AND hdct.DmLoaiREF = tchpctpr.DmHinhThucQuangCaoREF
                                        AND hdct.DmSanPhamREF = tchpctpr.DmSanPhamREF
                
                        ) T;            
					-- Insert HopDongChiTietID vao bang de dung khi tinh thay doi
                    IF NOT EXISTS ( SELECT  *
                                    FROM    dbo.ThucChay_ThongTinHopDongChiTietID_PR
                                    WHERE   ThucChayHopDongChiTietPRID IN (
                                            SELECT  t.ThucChayHopDongChiTietPRID
                                            FROM  (
												SELECT TOP (1) HopDongREF, HopDongChiTietREF, ThucChayHopDongChiTietPRID,ThuTuTrongSo 
												FROM dbo.[ThucChayHopDongChiTietPR_ThuTuTrongSo_Temp]
												WHERE HopDongREF = @pHopDongID
												ORDER BY ThuTuTrongSo, ThucChayHopDongChiTietPRID
									)t ) )
                        BEGIN
                            INSERT  INTO dbo.ThucChay_ThongTinHopDongChiTietID_PR
                                    SELECT  t.HopDongChiTietREF ,
                                            t.ThucChayHopDongChiTietPRID
                                    FROM    (
												SELECT TOP (1) HopDongREF, HopDongChiTietREF, ThucChayHopDongChiTietPRID,ThuTuTrongSo 
												FROM dbo.[ThucChayHopDongChiTietPR_ThuTuTrongSo_Temp]
												WHERE HopDongREF = @pHopDongID
												ORDER BY ThuTuTrongSo, ThucChayHopDongChiTietPRID
									) t
                        END
			
			--SELECT * FROM ThucChay_ThongTinHopDongChiTietID_PR

			EXEC [dbo].[sp_TC_UpdateRecordStatus_ThucChayHopDongChiTietPR_NotBy_NgayThucHien]  @NgayThucHien,@pHopDongID ,@DmSanPhamREF  
			DELETE FROM dbo.[ThucChayHopDongChiTietPR_ThuTuTrongSo_Temp]
		    SET @Count = @Count + 1
		END



  END;


```
