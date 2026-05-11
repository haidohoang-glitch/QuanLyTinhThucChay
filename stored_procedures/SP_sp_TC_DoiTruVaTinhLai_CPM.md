# Stored Procedure: `sp_TC_DoiTruVaTinhLai_CPM`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-22 11:25:42.710000
- **Ngày sửa cuối**: 2021-01-02 17:47:39.453000

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

CREATE  PROCEDURE [dbo].[sp_TC_DoiTruVaTinhLai_CPM]
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
							, -(SoLuongThucChayLechTreoHa) AS SoLuongThucChayLechTreoHa
							, -(ThanhTienLechTreoHa) AS ThanhTienLechTreoHa
							, GETDATE()
							, GETDATE()
							, IsPheDuyet
							, PheDuyetBy
							, PheDuyetAt
							, -(SoLuongThucChay + SoLuongThayDoi) AS SoLuongThayDoi
							, -(SoLuongThucChayKM + SoLuongKMThayDoi) AS SoLuongKMThayDoi
							, -(ThanhTienKM + GiaTriKMThayDoi) AS GiaTriKMThayDoi
							, N'sp_TC_DoiTruVaTinhLai_CPM' GhiChu
					FROM    dbo.ThucChayDaTinh
					WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien
							AND DmSanPhamREF IN ( 231, 238, 339, 240, 598, 613, 370, 680, 735, 5056 )
							AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, DonViTinh) = 3	 --Đơn vị của hình thức CPM, TRUE REACH
							AND NOT ( DmLoaiBannerREF IN ( 17, 18 )
										OR DmHinhThucQuangCao IN ( 13, 42 )
									)
							AND SoHopDong = @pSoHopDong
							AND HopDongChiTietREF = @pHopDongChiTietID
							AND DonViTinh <> N'TRUE REACH'
		SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
        END 


		

		SET @NgayThucHien = @StartDate

        WHILE ( @NgayThucHien <= @EndDate )
            BEGIN

		
		-- Tính lại
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
                        WHERE   NgayThucHien = @NgayThucHien
                                AND TypeProduct NOT IN ( 1, 2, 17 )
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
                          , A.HDLechGiaYN
                    FROM    ( SELECT    tct.SoHopDong
                                      , tct.TypeProduct
                                      , tct.DmWebsiteREF
                                      , tct.TenWebsite
                                      , tct.DmBannerREF
                                      , 'Y' HDLechGiaYN
                              FROM      dbo.ThucChayTemp tct
                            ) A
                    ORDER BY A.SoHopDong
                          , A.TypeProduct	

                OPEN Record_Cursor

		-- Perform the first fetch.
                FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF, @HDLechGiaYN
			
                WHILE @@FETCH_STATUS = 0
                    BEGIN
                         EXEC dbo.ThucChay_InsertThucChayDaTinh_DoiTruVaTinhLai_CPM 
							@NgayThucHien = @NgayThucHien
							, @SoHopDong = @pSoHopDong 
							, @TypeProduct = @TypeProduct
							, @DmWebsiteREF = @DmWebsiteREF
							, @TenWebsite = @TenWebsite
							, @DmBannerREF = @DmBannerREF
							, @pHopDongChiTietID = @pHopDongChiTietID
							, @NgayTinh = @NgayThucHien
                        FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF, @HDLechGiaYN
                    END

                CLOSE Record_Cursor
                DEALLOCATE Record_Cursor

                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
                DELETE  FROM dbo.ThucChayTemp
            END 
  
END



```
