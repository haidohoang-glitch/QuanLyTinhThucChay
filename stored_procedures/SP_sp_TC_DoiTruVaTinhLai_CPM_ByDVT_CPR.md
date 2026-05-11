# Stored Procedure: `sp_TC_DoiTruVaTinhLai_CPM_ByDVT_CPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-22 15:19:02.650000
- **Ngày sửa cuối**: 2018-03-16 15:57:14.737000

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

CREATE  PROCEDURE [dbo].[sp_TC_DoiTruVaTinhLai_CPM_ByDVT_CPR]
    @StartDate DATETIME
  , @EndDate DATETIME
  , @pSoHopDong NVARCHAR(50)
  , @pHopDongChiTietID INT
  , @NgayTinh DATETIME
AS
    BEGIN
        DECLARE @NgayThucHien DATETIME

        DECLARE @SoHopDong NVARCHAR(50)
          , @HopDongID INT
          , @TypeProduct INT
          , @TenWebsite NVARCHAR(50)
          , @DmWebsiteREF INT

        SET @NgayThucHien = @StartDate
        SET @TenWebsite = '(Blanks)'
        SET @DmWebsiteREF = 826

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
                              , N'sp_TC_DoiTruVaTinhLai_CPM_ByDVT_CPR' GhiChu
                        FROM    dbo.ThucChayDaTinh
                        WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                AND DmSanPhamREF IN ( 680, 598, 735 )
                                AND DonViTinh = 'CPR'
                                AND SoHopDong = @pSoHopDong
                                AND HopDongChiTietREF = @pHopDongChiTietID

			SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
        END 



		SET @NgayThucHien = @StartDate

        WHILE ( @NgayThucHien <= @EndDate )
            BEGIN
        
				-- Tính lại

                DELETE  FROM dbo.ThucChayCPRTemp
	
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
                        FROM    dbo.ThucChay
                        WHERE   NgayThucHien =  @NgayThucHien
                                AND TypeProduct IN ( 16, 14,18 )
                                AND DmWebsiteREF <> 0
                                AND SoHopDong = @pSoHopDong
                                --AND HopDongChiTietREF = @pHopDongChiTietID

		
                INSERT  INTO dbo.ThucChayCPRTemp
                        ( bannerid
                        , uvngay
                        , uv
                        , typeproduct
                        , ProductName
                        , NgayThucHien
                        , ThoiGianTao
                        , uvhour
                        , TVDenNgay
                        , TCDenNgay
		                )
                        SELECT  bannerid
                              , uvNgay
                              , uv
                              , typeproduct
                              , ProductName
                              , NgayThucHien
                              , ThoiGianTao
                              , uvhour
                              , TVDenNgay
                              , TCDenNgay
                        FROM    dbo.ThucChayCPR tcc
                        WHERE   NgayThucHien = @NgayThucHien
		
		

		
                DECLARE Record_Cursor CURSOR
                FOR
                    SELECT DISTINCT
                            A.SoHopDong
                          , A.TypeProduct
                    FROM    ( SELECT    tct.SoHopDong
                                      , tct.TypeProduct
                                      , tct.DmBannerREF
                              FROM      ( SELECT DISTINCT
                                                    tct.SoHopDong
                                                  , tct.TypeProduct
                                                  , tct.DmBannerREF
                                          FROM      dbo.ThucChayTemp tct
                                                    INNER JOIN ( SELECT hd.SoHopDong
                                                                 FROM   dbo.HopDong hd
                                                                        INNER JOIN dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
                                                                 WHERE  hdct.DmSanPhamREF IN ( 680, 598,735 )
                                                                        AND hdct.DonViTinhREF = 30
                                                                        AND hd.TrangThaiHopDong <> 3
                                                                        AND hdct.DeletedStatus = 0
																		AND hd.SoHopDong = @pSoHopDong
                                                               ) hd ON hd.SoHopDong = tct.SoHopDong
                                        ) tct
                                        INNER JOIN dbo.ThucChayCPRTemp tcc ON tcc.typeproduct = tct.TypeProduct
                                                                          AND tcc.bannerid = tct.DmBannerREF
                            ) A
                    ORDER BY A.SoHopDong
                          , A.TypeProduct	
                OPEN Record_Cursor

		-- Perform the first fetch.
                FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct
			
                WHILE @@FETCH_STATUS = 0
                    BEGIN
                        SET @HopDongID = ISNULL(( SELECT TOP (1)
                                                            hd.HopDongID
                                                  FROM      dbo.HopDong hd
                                                  WHERE     hd.SoHopDong = @SoHopDong
												  ORDER BY hd.HopDongID
                                                ), 0)

                
                        EXEC dbo.ThucChay_InsertThucChayDaTinh_CPR_ByDVT_CPR_DoiTruVaTinhLai_CPM @NgayThucHien, @HopDongID, @TypeProduct, @DmWebsiteREF, @TenWebsite,
                            @pHopDongChiTietID, @NgayTinh
                        FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct
                    END

                CLOSE Record_Cursor
                DEALLOCATE Record_Cursor


                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
                DELETE  FROM dbo.ThucChayTemp
                DELETE  FROM dbo.ThucChayCPRTemp
            END 

    END




```
