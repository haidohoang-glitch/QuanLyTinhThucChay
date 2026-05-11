# Stored Procedure: `sp_TC_DoiTruVaTinhLai_CPM_TrueView`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-12-19 17:08:46.103000
- **Ngày sửa cuối**: 2018-11-20 14:24:44.530000

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


/*
EXEC ThucChay_DoiTruVaTinhLai_TrueView_Job '2018-06-13','2018-08-20','QC5620518',527807,'2018-08-29'
*/

CREATE  PROCEDURE [dbo].[sp_TC_DoiTruVaTinhLai_CPM_TrueView]
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
                              , 0 AS SoLuongThucChay
                              , @NgayThucHien
                              , -(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS GiaTriThayDoi
                              , 0 AS ThanhTienThucChayTruocTrietKhau
                              , 0 AS GiaTriTrietKhauThucChay
                              , 0 AS ThanhTienSauTrietKhauThucChay
                              , 0 AS GiaTriHoaHongThucChay
                              , -(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS ThanhTienThucThu
                              , 0 AS ThanhTienKM
                              , 0 AS SoLuongThucChayKM
                              , -SoLuongThucChayLechTreoHa
                              , -ThanhTienLechTreoHa
                              , GETDATE()
                              , GETDATE()
                              , IsPheDuyet
                              , PheDuyetBy
                              , PheDuyetAt
                              , -(SoLuongThucChay + SoLuongThayDoi) AS SoLuongThayDoi
                              , -(SoLuongThucChayKM + SoLuongKMThayDoi) AS SoLuongKMThayDoi
                              , -(ThanhTienKM + GiaTriKMThayDoi) AS GiaTriKMThayDoi
                              , N'sp_TC_DoiTruVaTinhLai_CPM_TrueView' GhiChu
                        FROM    dbo.ThucChayDaTinh
                        WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                AND DmSanPhamREF IN ( 240 )
                                --AND DonViTinh = 'True View' --Đơn vị của hình thức True View
                                AND SoHopDong = @pSoHopDong
                                AND HopDongChiTietREF = @pHopDongChiTietID
								AND DmHinhThucQuangCao <> 42


			SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
        END 




		SET @NgayThucHien = @StartDate

        WHILE ( @NgayThucHien <= @EndDate )
            BEGIN

                DELETE  FROM dbo.ThucChayTemp
                DELETE  FROM dbo.ThucChayTrueViewTemp

		
		-- Tính lại
        
               INSERT  INTO dbo.ThucChayTrueViewTemp
                        ( SoHopDong
                        , TypeProduct
                        , DmSanPhamREF
                        , TenSanPham
                        , campaignid
                        , bannerid
                        , SiteName
                        , SiteID
                        , True_View
                        , Views
                        , Clicks
                        , NgayThucHien
                        , CreatedBy
                        , CreatedAt
                        , LastModifiedBy
                        , LastModifiedAt
                        , DeletedStatus
                        )
                        SELECT  tcc.SoHopDong
                              , tcc.TypeProduct
                              , tcc.DmSanPhamREF
                              , tcc.TenSanPham
                              , tcc.campaignid
                              , tcc.bannerid
                              , tcc.SiteName
                              , tcc.SiteID
                              , tcc.True_View
                              , tcc.Views
                              , tcc.Clicks
                              , tcc.NgayThucHien
                              , tcc.CreatedBy
                              , tcc.CreatedAt
                              , tcc.LastModifiedBy
                              , tcc.LastModifiedAt
                              , tcc.DeletedStatus
                        FROM    dbo.ThucChayTrueView tcc
                        WHERE   CONVERT(DATE, tcc.NgayThucHien) = @NgayThucHien
						AND tcc.SoHopDong = @pSoHopDong

                DECLARE Record_Cursor CURSOR
                FOR
                     SELECT DISTINCT   tcc.SoHopDong
                                      , tcc.TypeProduct TypeProduct
                                      , tcc.SiteID DmWebsiteREF
                                      , tcc.SiteName TenWebsite
                                      , tcc.bannerid DmBannerREF
                              FROM     dbo.ThucChayTrueViewTemp tcc        
							  ORDER BY tcc.SoHopDong, TypeProduct    
						  	
                OPEN Record_Cursor

				-- Perform the first fetch.
                FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF
			
                WHILE @@FETCH_STATUS = 0
                    BEGIN
						PRINT @NgayThucHien
						PRINT @DmBannerREF
						PRINT @TenWebsite
						PRINT @pHopDongChiTietID

                        EXEC ThucChay_InsertThucChayDaTinhTrueView_DoiTruVaTinhLai_CPM @NgayThucHien, @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF, @pHopDongChiTietID
                        FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF
                    END

                CLOSE Record_Cursor
                DEALLOCATE Record_Cursor
		

                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
            END 



			UPDATE dbo.ThucChayDaTinh SET NgayThucHien = @NgayTinh 
			WHERE SoHopDong = @pSoHopDong 
					AND HopDongChiTietREF = @pHopDongChiTietID
					AND (GhiChu = N'ThucChay_InsertThucChayDaTinhTrueView_DoiTruVaTinhLai_CPM' 
							OR GhiChu = N'sp_TC_DoiTruVaTinhLai_CPM_TrueView')
					AND CONVERT(DATE, CreatedAt) = CONVERT(DATE, GETDATE())
    END




```
