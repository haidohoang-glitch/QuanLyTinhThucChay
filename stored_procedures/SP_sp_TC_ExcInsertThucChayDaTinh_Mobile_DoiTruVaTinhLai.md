# Stored Procedure: `sp_TC_ExcInsertThucChayDaTinh_Mobile_DoiTruVaTinhLai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-25 10:03:00.487000
- **Ngày sửa cuối**: 2022-12-01 14:54:27.873000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@pSoHopDong` | `nvarchar(100)` | No |
| `@NgayTinh` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
exec [dbo].[sp_TC_ExcInsertThucChayDaTinh_Mobile_DoiTruVaTinhLai] 	'2021-01-06','2021-02-07', 'QC8791220', '2021-06-03'
*/
--tinh ca truong hop 1 phan bo nhieu banner
CREATE PROCEDURE [dbo].[sp_TC_ExcInsertThucChayDaTinh_Mobile_DoiTruVaTinhLai]
	-- Add the parameters for the stored procedure here
    @StartDate DATETIME
  , @EndDate DATETIME
  , @pSoHopDong NVARCHAR(50)
  , @NgayTinh DATETIME
AS
    BEGIN
        Delete from dbo.ThucChayDaTinh_DoiTruVaTinhLai_Mobile
		DECLARE  @HopDongID INT

        DECLARE @NgayThucHien DATETIME
          , @SoHopDong NVARCHAR(50)
          , @HopDongChiTietREF INT
          , @DmBannerREF INT
          , @DmWebsiteREF INT
          , @TH INT
		  , @THCo1HDCT_YN SMALLINT = 0
	
        DECLARE @Table TABLE
            (
              SoHopDong NVARCHAR(50)
            , DmBannerID INT
            , DmWebsiteID INT
            , TH INT
            )


        DECLARE @ThucChayHopDongChiTiet_Temp TABLE
            (
              SoHopDong NVARCHAR(50)
            , DmBannerREF NVARCHAR(50)
            , IsKhuyenMai INT
            , HopDongChiTietID INT
            , HopDongID INT
			, TH INT
            )

      
		DECLARE @Table_TH TABLE
        (
           SoHopDong NVARCHAR(50)
        , DmBannerREF INT
        , DmWebsiteREF INT
		, TH INT
        )

		--Insert vao bang HopDongChiTietAndBanner
        EXEC dbo.sp_TC_HopDongChiTietAndBannerByDmSanPhamREF @DmSanPhamREF = 342
															, @NgayThucHien = @StartDate

        SET @HopDongID = (SELECT TOP (1) HopDongID FROM dbo.HopDong WHERE SoHopDong = @pSoHopDong ORDER BY HopDongID)

		IF(EXISTS(SELECT HopDongFK, COUNT(HopDongChiTietID)sl 
			FROM dbo.HopDongChiTiet
			WHERE DmSanPhamREF = 342
			AND HopDongFK = @HopDongID
			AND NOT(DmLoaiREF IN (13,42) OR DmLoaiBannerREF = 18)
			AND DmLoaiNenTangREF <> 8 
			AND DeletedStatus = 0
			GROUP BY HopDongFK HAVING COUNT(HopDongChiTietID) = 1)
		 )
		BEGIN
		    SET @THCo1HDCT_YN = 1
		END
	
		-- THUC HIEN DOI TRU THUC CHAY CU TU DAU NGAY CHAY CHO TOI NGAY @EndDate
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
                SELECT  NEWID() ThucChayDaTinhID
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
                        , @NgayTinh NgayThucHien
                        , -SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) GiaTriThayDoi
                        , 0 ThanhTienThucChayTruocTrietKhau
                        , 0 GiaTriTrietKhauThucChay
                        , 0 ThanhTienSauTrietKhauThucChay
                        , 0 GiaTriHoaHongThucChay
                        , 0 ThanhTienThucThu
                        , 0 ThanhTienKM
                        , 0 SoLuongThucChayKM
                        , -SUM(SoLuongThucChayLechTreoHa) SoLuongThucChayLechTreoHa
                        , -SUM(ThanhTienLechTreoHa) ThanhTienLechTreoHa
                        , GETDATE() CreatedAt
                        , GETDATE() LastModifiedAt
                        , 0 IsPheDuyet
                        , '' PheDuyetBy
                        , NULL PheDuyetAt
                        , -SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) SoLuongThayDoi
                        , -SUM(ISNULL(tcdt.SoLuongThucChayKM, 0) + ISNULL(tcdt.SoLuongKMThayDoi, 0)) SoLuongKMThayDoi
                        , -SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) GiaTriKMThayDoi
                        , N'ThucChay_DoiTruVaTinhLai_Mobile_Job' GhiChu
                FROM    dbo.ThucChayDaTinh tcdt
                WHERE   1 = 1
                        AND SoHopDong = @pSoHopDong
                        AND tcdt.NgayThucHien <= @EndDate
                        AND DmSanPhamREF = 342
                        AND NOT ( DmHinhThucQuangCao IN ( 42, 13 )
                                    OR DmLoaiBannerREF IN ( 17, 18 )
                                )
                        AND EXISTS( SELECT TOP (1)  HopDongChiTietID
                                                    FROM     dbo.HopDongChiTiet
                                                    WHERE    DmSanPhamREF = 342
                                                            AND DeletedStatus = 0
                                                            AND DmLoaiNenTangREF <> 8 
															AND HopDongChiTietID = tcdt.HopDongChiTietREF)
                GROUP BY HopDongID
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
						
		 --XAC DINH TRUONG HOP CAN TINH THUC CHAY VOI CAC BANNER VÀ HOPDONGCHITIET CỦA MOBILE
		INSERT  INTO @ThucChayHopDongChiTiet_Temp
        SELECT  hd.SoHopDong , tc.DmBannerID , hdct.IsKhuyenMai , hdct.HopDongChiTietID , hd.HopDongID, 1 TH
        FROM   (
					SELECT tc.HopDongREF, tc.DmBannerID, tc.HopDongChiTietREF 
					FROM dbo.ThucChayHopDongChiTietAndBanner tc 
					WHERE tc.HopDongREF = @HopDongID
					AND tc.DeletedStatus = 0
				) tc
                INNER JOIN 
				(
					SELECT hdct.HopDongFK, hdct.HopDongChiTietID, hdct.IsKhuyenMai 
					FROM dbo.HopDongChiTiet hdct 
					WHERE hdct.HopDongFK = @HopDongID AND hdct.DmSanPhamREF = 342
				)hdct ON tc.HopDongChiTietREF = hdct.HopDongChiTietID
                INNER JOIN 
				(
					SELECT hd.HopDongID, hd.SoHopDong 
					FROM dbo.HopDong hd 
					WHERE hd.HopDongID = @HopDongID
				) hd ON tc.HopDongREF = hd.HopDongID
                           
				-- Xac dinh truong hop can tinh
				IF(@THCo1HDCT_YN = 1)
				BEGIN
				     INSERT  INTO @Table_TH
                        SELECT DISTINCT
                                T.SoHopDong
                              , T.DmBannerREF
                              , 0 DmWebsiteREF
                              , 1 TH
                        FROM    ( SELECT    *
                                  FROM      @ThucChayHopDongChiTiet_Temp
                                ) T
				END
				ELSE
				BEGIN
				    INSERT  INTO @Table_TH
                    SELECT DISTINCT
                            t2.SoHopDong
                            , t2.DmBannerREF
                            , 0 DmWebsiteREF
                            , t2.TH
                    FROM    ( SELECT DISTINCT
                                t2.DmBannerREF
                                , t2.HopDongChiTietID
                                , t2.SoHopDong
                                , T6.TH
                            FROM   ( SELECT    T.DmBannerID
                                            , CASE WHEN T.HopDongChiTietREF = 1 THEN 1
                                                    WHEN T.HopDongChiTietREF > 1
                                                        AND T.KhuyenMai > 0
                                                        AND T.HopDongChiTietREF <> T.KhuyenMai THEN 2
                                                    WHEN ( T.HopDongChiTietREF > 1
                                                        AND T.KhuyenMai = 0
                                                        )
                                                        OR ( T.HopDongChiTietREF = T.KhuyenMai
                                                            AND T.HopDongChiTietREF > 1
                                                            ) THEN 3
                                                    ELSE 0
                                            END TH
                                    FROM      ( SELECT    DmBannerID
                                                        , COUNT(DISTINCT HopDongChiTietREF) HopDongChiTietREF
                                                        , SUM(T4.IsKhuyenMai) KhuyenMai
                                                FROM      ( SELECT    T1.SoHopDong
                                                                    , T1.DmBannerREF DmBannerID
                                                                    , 0 DmWebsiteREF
                                                                    , T1.HopDongChiTietID HopDongChiTietREF
                                                                    , T1.HopDongID
                                                                    , T1.IsKhuyenMai
                                                            FROM    ( SELECT    *
                                                                        FROM      @ThucChayHopDongChiTiet_Temp tchdctt
                                                                    ) T1
                                                                                    
                                                        ) T4
                                                GROUP BY  DmBannerID
                                            ) T
                                ) T6
                                INNER JOIN @ThucChayHopDongChiTiet_Temp t2 ON T6.DmBannerID = t2.DmBannerREF
                        ) t2 
				END
               

        SET @NgayThucHien = @StartDate
        WHILE ( @NgayThucHien <= @EndDate )
            BEGIN

				--Insert vao bang temp --danh cho truong hop phanbo
                EXEC dbo.ThucChay_InsertToTemp_Mobile @NgayThucHien = @NgayThucHien
	
                INSERT  INTO @Table
				SELECT tc.SoHopDong, tc.DmBannerREF
				, tc.DmWebsiteREF
				, th.TH FROM
				(
                        SELECT DISTINCT
                                A.SoHopDong
                              , A.DmBannerREF
                              , A.DmWebsiteREF
                        FROM    dbo.ThucChay_MobileTemp A
						WHERE   A.NgayThucHien = @NgayThucHien
						AND A.SoHopDong = @pSoHopDong
				)tc INNER JOIN
				@Table_TH th ON th.DmBannerREF = tc.DmBannerREF AND th.SoHopDong = tc.SoHopDong

				--DUYET TUNG PHAN BO
                DECLARE vendor_cursor CURSOR
                FOR
                    SELECT  *
                    FROM    @Table t

                OPEN vendor_cursor
		
                FETCH NEXT FROM vendor_cursor INTO @SoHopDong, @DmBannerREF, @DmWebsiteREF, @TH

                WHILE @@FETCH_STATUS = 0
                    BEGIN

			-- Truong hop map 1-1 
			--PRINT N'--------------------'
			--PRINT 'TH: ' + CONVERT(NVARCHAR(50),@TH) 
			--PRINT @NgayThucHien
			--PRINT @DmBannerREF
			--PRINT N'--------------------'

            IF @TH = 1
                BEGIN
				 print 'nhay vào day TH1'
                    EXEC sp_TC_ExcInsertThucChayDaTinh_Single_Mobile_DoiTruVaTinhLai @DmBannerREF, @NgayThucHien, @SoHopDong, @DmWebsiteREF
                END				
				

			--Tinh cho truong hop 1 banner co tren 2 HĐCT, trong do co HĐ khuyen mai
            ELSE
                IF @TH = 2
                    BEGIN
					 print 'nhay vào day TH2'
                        EXEC sp_TC_ExcInsertThucChayDaTinh_CoChietKhau_Mobile_DoiTruVaTinhLai @DmBannerREF, @NgayThucHien, @SoHopDong, @DmWebsiteREF
                    END
				

			--Tinh cho truong hop 1 banner co tren 2 HĐCT, trong do ko co HĐ khuyen mai	
            ELSE
                IF @TH = 3
                    BEGIN 
					 print 'nhay vào day TH3'
                        EXEC sp_TC_ExcInsertThucChayDaTinh_KoChietKhau_Mobile_DoiTruVaTinhLai @DmBannerREF, @NgayThucHien, @SoHopDong,
                            @DmWebsiteREF
                    END
            ELSE
                PRINT 'Khong xac dinh case'

                    FETCH NEXT FROM vendor_cursor INTO @SoHopDong, @DmBannerREF, @DmWebsiteREF, @TH
                END 
                CLOSE vendor_cursor;
                DEALLOCATE vendor_cursor;

				------************
                DELETE  FROM @Table


                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
	
            END 
			DELETE  FROM @Table_TH
			DELETE  FROM @ThucChayHopDongChiTiet_Temp
			
    END

```
