# Stored Procedure: `sp_TC_DoiTruVaTinhLai_CPM_CPV`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-22 11:46:52.407000
- **Ngày sửa cuối**: 2019-07-23 14:21:46.757000

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

CREATE  PROCEDURE [dbo].[sp_TC_DoiTruVaTinhLai_CPM_CPV]
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
                              , 0 SoLuongThucChay
                              , @NgayThucHien
                              , -(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) GiaTriThayDoi
                              ,0  ThanhTienThucChayTruocTrietKhau
                              ,0  GiaTriTrietKhauThucChay
                              ,0 ThanhTienSauTrietKhauThucChay
                              ,0 GiaTriHoaHongThucChay
                              ,0 ThanhTienThucThu
                              ,0 ThanhTienKM
                              ,0 SoLuongThucChayKM
                              ,-SoLuongThucChayLechTreoHa
                              ,-ThanhTienLechTreoHa
                              , GETDATE()
                              , GETDATE()
                              , IsPheDuyet
                              , PheDuyetBy
                              , PheDuyetAt
                              , -(SoLuongThucChay + SoLuongThayDoi) SoLuongThayDoi
                              , -(SoLuongThucChayKM + SoLuongKMThayDoi) SoLuongKMThayDoi
                              , -(ThanhTienKM + GiaTriKMThayDoi) GiaTriKMThayDoi
                              , N'sp_TC_DoiTruVaTinhLai_CPM_CPV' GhiChu
                        FROM    dbo.ThucChayDaTinh
                        WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                AND DmSanPhamREF IN ( 240 , 598)
                                AND DonViTinh = 'CPV' --Đơn vị của hình thức CPV	
                                AND SoHopDong = @pSoHopDong
                                AND HopDongChiTietREF = @pHopDongChiTietID


			SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
        END 




		SET @NgayThucHien = @StartDate

        WHILE ( @NgayThucHien <= @EndDate )
            BEGIN

                DELETE  FROM dbo.ThucChayTemp
				WHERE 1=1

                DELETE  FROM dbo.ThucChayCPVTemp
				WHERE 1=1

		
			-- Tính lại
            INSERT  INTO dbo.ThucChayCPVTemp
                    ( typeproduct
                    , ProductName
                    , bannerid
                    , totalview
                    , percent_rate
                    , CPV
                    , NgayThucHien
		            )
                    SELECT  typeproduct
                            , ProductName
                            , bannerid
                            , totalview
                            , percent_rate
                            , CPV
                            , NgayThucHien
                    FROM    dbo.ThucChayCPV tcc
                    WHERE   CONVERT(DATE, tcc.NgayThucHien) = @NgayThucHien

		
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
                        FROM    dbo.ThucChay
                        WHERE   NgayThucHien = @NgayThucHien
                                AND TypeProduct NOT IN ( 1, 2, 17)
                                AND DmWebsiteREF <> 0
                                AND SoHopDong = @pSoHopDong
                                --AND HopDongChiTietREF = @pHopDongChiTietID

                DECLARE Record_Cursor CURSOR
                FOR
                    SELECT DISTINCT
                            A.SoHopDong
                          , A.TypeProduct
                          , A.DmWebsiteREF
                          , A.TenWebsite
                          , A.DmBannerREF
                    FROM    ( SELECT    tct.SoHopDong
                                      , tct.TypeProduct
                                      , tct.DmWebsiteREF
                                      , tct.TenWebsite
                                      , tct.DmBannerREF
                              FROM      dbo.ThucChayTemp tct
                                        INNER JOIN dbo.ThucChayCPVTemp tcc ON tct.DmBannerREF = tcc.bannerid
                                                                          AND tct.NgayThucHien = tcc.NgayThucHien
																		  AND tcc.typeproduct = tct.TypeProduct
                            ) A
                    ORDER BY A.SoHopDong
                          , A.TypeProduct	
                OPEN Record_Cursor

		-- Perform the first fetch.
                FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF
			
                WHILE @@FETCH_STATUS = 0
                    BEGIN
                        EXEC dbo.ThucChay_InsertThucChayDaTinhCPV_DoiTruVaTinhLai_CPM @NgayThucHien, @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite,
                            @DmBannerREF, @pHopDongChiTietID, @NgayTinh
                        FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF
                    END

                CLOSE Record_Cursor
                DEALLOCATE Record_Cursor

                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
            END 

		--ThucChay_InsertThucChayDaTinhCPV_DoiTruVaTinhLai_CPM
		--UPDATE NGAY GHI NHAN TINH THUC CHAY 
		UPDATE dbo.ThucChayDaTinh
		SET NgayThucHien = @NgayTinh
		WHERE HopDongChiTietREF = @pHopDongChiTietID
		AND NgayThucHien <> @NgayTinh
		AND CONVERT(DATE, CreatedAt) = CONVERT(DATE,GETDATE())
		--AND GhiChu = N'ThucChay_InsertThucChayDaTinhCPV_DoiTruVaTinhLai_CPM'
		
    END




```
