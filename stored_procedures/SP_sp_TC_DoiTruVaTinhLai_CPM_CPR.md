# Stored Procedure: `sp_TC_DoiTruVaTinhLai_CPM_CPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-22 11:56:28.557000
- **Ngày sửa cuối**: 2018-03-16 11:29:58.527000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@pSoHopDong` | `nvarchar(100)` | No |
| `@pHopDongChiTietID` | `int(4)` | No |
| `@NgayTinh` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================


--DELETE FROM ThucChayDaTinh

CREATE  PROCEDURE [dbo].[sp_TC_DoiTruVaTinhLai_CPM_CPR]
    @StartDate DATETIME
  , @EndDate DATETIME
  , @pSoHopDong NVARCHAR(50)
  , @pHopDongChiTietID INT
  , @NgayTinh DATETIME
AS
    BEGIN
        DECLARE @NgayThucHien DATETIME

        DECLARE @SoHopDong NVARCHAR(50)
          , @TypeProduct INT
          , @HDLechGiaYN NVARCHAR(50)
          , @TenWebsite NVARCHAR(50)
          , @DmWebsiteREF INT
          , @DmBannerREF INT



		SET @NgayThucHien = @StartDate

        WHILE ( @NgayThucHien <= @EndDate )
            BEGIN
				-- Đối trừ thực chạy cũ

                INSERT  INTO dbo.ThucChayDaTinh
                        SELECT  NEWID()
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
                              , 0 TongViewThucChay
                              , 0 TongClickThucChay
                              , 0 TongSoBaiViet
                              , -SoLuongThucChay
                              , @NgayThucHien
                              , -GiaTriThayDoi
                              , ThanhTienThucChayTruocTrietKhau
                              , GiaTriTrietKhauThucChay
                              , -ThanhTienSauTrietKhauThucChay
                              , GiaTriHoaHongThucChay
                              , ThanhTienThucThu
                              , -ThanhTienKM
                              , -SoLuongThucChayKM
                              , -SoLuongThucChayLechTreoHa
                              , -ThanhTienLechTreoHa
                              , GETDATE()
                              , GETDATE()
                              , IsPheDuyet
                              , PheDuyetBy
                              , PheDuyetAt
                              , -SoLuongThayDoi
                              , -SoLuongKMThayDoi
                              , -GiaTriKMThayDoi
                              , N'sp_TC_DoiTruVaTinhLai_CPM_CPR' GhiChu
                        FROM    dbo.ThucChayDaTinh
                        WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                AND DmSanPhamREF IN ( 680 )
                                AND SoHopDong = @pSoHopDong
                                AND HopDongChiTietREF = @pHopDongChiTietID
								AND DonViTinh LIKE N'Gói'

			SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
        END 



        SET @NgayThucHien = @StartDate

        WHILE ( @NgayThucHien <= @EndDate )
            BEGIN

		-- Tính lại

                DELETE  FROM ThucChayCPRTemp
	
                DELETE  FROM dbo.ThucChayTemp
        
                INSERT  INTO dbo.ThucChayTemp
                        ( ThucChayID
                        , SoHopDong
                        , DanhsachDmBookingREF
                        , DmSanPhamREF
                        , TenSanPham
                        , DmNhomWebsiteREF
                        , TenNhomWebsite
                        , DmWebsiteREF
                        , TenWebsite
                        , DmChienDichREF
                        , TenChienDich
                        , DmBannerREF
                        , TenBanner
                        , NgayThucHien
                        , TongViewThucChay
                        , TongClickThucChay
                        , CreatedBy
                        , CreatedAt
                        , LastModifiedBy
                        , LastModifiedAt
                        , DeletedStatus
                        , PrintStatus
                        , RecordStatus
                        , TongSoBaiViet
                        , SoThuTuTheoNgay
                        , TypeProduct
                        , BannerType
                        , UserName
                        , SaleName
                        , Email
                        , LastTimeCalc
                        , sys_date
                        , IsReady
                        , ProductUnitID
                        , ProductUnitName
                        , BannerTypeName
                        , HopDongChiTietREF
                        , CampainStatus
                        , BannerStatus
                        , IsNoiBo
		                )
                        SELECT  ThucChayID
                              , SoHopDong
                              , DanhsachDmBookingREF
                              , DmSanPhamREF
                              , TenSanPham
                              , DmNhomWebsiteREF
                              , TenNhomWebsite
                              , DmWebsiteREF
                              , TenWebsite
                              , DmChienDichREF
                              , TenChienDich
                              , DmBannerREF
                              , TenBanner
                              , NgayThucHien
                              , TongViewThucChay
                              , TongClickThucChay
                              , CreatedBy
                              , CreatedAt
                              , LastModifiedBy
                              , LastModifiedAt
                              , DeletedStatus
                              , PrintStatus
                              , RecordStatus
                              , TongSoBaiViet
                              , SoThuTuTheoNgay
                              , TypeProduct
                              , BannerType
                              , UserName
                              , SaleName
                              , Email
                              , LastTimeCalc
                              , sys_date
                              , IsReady
                              , ProductUnitID
                              , ProductUnitName
                              , BannerTypeName
                              , HopDongChiTietREF
                              , CampainStatus
                              , BannerStatus
                              , IsNoiBo
                        FROM    ThucChay
                        WHERE   NgayThucHien = @NgayThucHien
                                AND TypeProduct IN ( 16 )
                                AND DmWebsiteREF != 0
                                AND SoHopDong = @pSoHopDong
                                --AND HopDongChiTietREF = @pHopDongChiTietID
		
                INSERT  INTO ThucChayCPRTemp
                        SELECT  *
                        FROM    ThucChayCPR tcc
                        WHERE   NgayThucHien = @NgayThucHien
		
                DECLARE Record_Cursor CURSOR
                FOR
                    SELECT DISTINCT
                            A.SoHopDong
                          , A.TypeProduct
                          , A.DmWebsiteREF
                          , A.TenWebsite
                    FROM    ( SELECT    tct.SoHopDong
                                      , tct.TypeProduct
                                      , tct.DmWebsiteREF
                                      , tct.TenWebsite
                              FROM      ThucChayTemp tct
                            ) A
                    ORDER BY A.SoHopDong
                          , A.TypeProduct	
                OPEN Record_Cursor

		-- Perform the first fetch.
                FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite
			
                WHILE @@FETCH_STATUS = 0
                    BEGIN
				
				
                        EXEC ThucChay_InsertThucChayDaTinh_CPR_DoiTruVaTinhLai_CPM @NgayThucHien, @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite,
                            @pHopDongChiTietID, @NgayTinh
                        FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite
                    END

                CLOSE Record_Cursor
                DEALLOCATE Record_Cursor


                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
                DELETE  FROM dbo.ThucChayTemp
                DELETE  FROM ThucChayCPRTemp
            END 




			--UPDATE dbo.ThucChayDaTinh SET NgayThucHien = @NgayTinh 
			--WHERE SoHopDong = @pSoHopDong 
			--		AND HopDongChiTietREF = @pHopDongChiTietID
			--		AND (GhiChu = N'ThucChay_InsertThucChayDaTinh_CPR_DoiTruVaTinhLai_CPM' 
			--				OR GhiChu = N'sp_TC_DoiTruVaTinhLai_CPM_CPR')
			--		AND CONVERT(DATE, CreatedAt) = CONVERT(DATE, GETDATE())


    END




```
