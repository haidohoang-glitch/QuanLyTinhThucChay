# Stored Procedure: `sp_TC_DoiTruVaTinhLai_CPM_DEV`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2023-08-11 15:57:04.870000
- **Ngày sửa cuối**: 2023-08-15 16:03:28.123000

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
EXEC [dbo].[sp_TC_DoiTruVaTinhLai_CPM_DEV]
    @StartDate = '2023-03-22 00:00:00.000'
  , @EndDate =  '2023-08-10 00:00:00.000' 
  , @pSoHopDong = N'QC3290323'
  , @pHopDongChiTietID = 694330
  , @NgayTinh = '2023-08-10'
*/

CREATE  PROCEDURE [dbo].[sp_TC_DoiTruVaTinhLai_CPM_DEV]
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
		  , @DmSanPhamREF INT
		  , @ThanhTienTruocCK FLOAT =0
		  , @ThanhTienThucChayTruocCK FLOAT =0

		  SET @DmSanPhamREF = ISNULL((SELECT TOP (1) C.DmSanPhamREF 
									FROM dbo.HopDongChiTiet C WHERE C.HopDongChiTietID = @pHopDongChiTietID ORDER BY C.HopDongChiTietID)
									,0)

  --      --THUC HIEN DOI TRU TOAN BO GROUP THEO BANNER,...
		---- Đối trừ thực chạy cũ
		--INSERT  INTO dbo.[ThucChayDaTinh_DoiTruVaTinhLai_CPM]
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
		--				SELECT  NEWID()
		--					, HopDongID
		--					, SoHopDong
		--					, DmMaHopDongREF
		--					, TenMaHopDong
		--					, NgayDanhSoHopDong
		--					, NgayKyHopDong
		--					, NhanHopDong
		--					, NgayNhanBanFax
		--					, NgayNhanHopDongBanCung
		--					, NgayChuyenHopDongChoKeToan
		--					, So
		--					, Thang
		--					, Nam
		--					, GiaTriHopDong
		--					, CongNo
		--					, HopDongChiTietREF
		--					, DangSuDung
		--					, IsGiayPhep
		--					, TrangThaiHopDong
		--					, IsBanCung
		--					, DmPhongBanREF
		--					, TenPhongBan
		--					, DmBoPhanREF
		--					, TenBoPhan
		--					, DmNhomLamViecREF
		--					, TenNhomLamViec
		--					, DmDiaDiemLamViecREF
		--					, TenDiaDiemLamViec
		--					, SysNhanVienREF
		--					, TenDangNhap
		--					, TenNhanVien
		--					, TenKhachHang
		--					, NhanHang
		--					, DmNhomNganhREF
		--					, TenNhomNganh
		--					, DmHinhThucQuangCao
		--					, TenHinhThucQuangCao
		--					, DmSanPhamREF
		--					, TenSanPham
		--					, DmNhomWebsiteREF
		--					, TenNhomWebsite
		--					, DmChuyenMucREF
		--					, TenChuyenMuc
		--					, DmLoaiBannerREF
		--					, TenLoaiBanner
		--					, DmViTriREF
		--					, TenViTri
		--					, N'PS_DOITRU_CPM' AS DotChayHopDong
		--					, 0 AS SoLuongDotChayHD
		--					, '' AS DotChayBooking
		--					, 0 AS SoLuongDotChayBooking
		--					, SoLuong
		--					, DonViTinh
		--					, DonGia
		--					, DonGiaTheoDonVi
		--					, ChietKhau
		--					, GiamGia
		--					, ThanhTien
		--					, TiLeTuVan
		--					, ChiPhiTuVan
		--					, IsKhuyenMai
		--					, KhuyenMai
		--					, DmBannerREF
		--					, DmChienDichREF
		--					, DmWebsiteREF
		--					, TenWebsite
		--					, 0 TongViewThucChay
		--					, 0 TongClickThucChay
		--					, 0 TongSoBaiViet
		--					, 0 AS SoLuongThucChay
		--					, @NgayTinh AS NgayThucHien
		--					, -SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS GiaTriThayDoi
		--					, 0 AS ThanhTienThucChayTruocTrietKhau
		--					, 0 AS GiaTriTrietKhauThucChay
		--					, 0 AS ThanhTienSauTrietKhauThucChay
		--					, 0 AS GiaTriHoaHongThucChay
		--					, 0 AS ThanhTienThucThu
		--					, 0 AS ThanhTienKM
		--					, 0 AS SoLuongThucChayKM
		--					, -SUM(SoLuongThucChayLechTreoHa) AS SoLuongThucChayLechTreoHa
		--					, -SUM(ThanhTienLechTreoHa) AS ThanhTienLechTreoHa
		--					, GETDATE()
		--					, GETDATE()
		--					, 0 AS IsPheDuyet
		--					, '' AS PheDuyetBy
		--					, GETDATE() PheDuyetAt
		--					, -SUM(SoLuongThucChay + SoLuongThayDoi) AS SoLuongThayDoi
		--					, -SUM(SoLuongThucChayKM + SoLuongKMThayDoi) AS SoLuongKMThayDoi
		--					, -SUM(ThanhTienKM + GiaTriKMThayDoi) AS GiaTriKMThayDoi
		--					, N'sp_TC_DoiTruVaTinhLai_CPM' GhiChu
		--			FROM    dbo.[ThucChayDaTinh_DoiTruVaTinhLai_CPM]
		--			WHERE   CONVERT(DATE, NgayThucHien) BETWEEN  @StartDate AND @EndDate
		--					AND DmSanPhamREF IN ( 231, 238, 339, 240, 598, 613, 370, 680, 735, 5056 )
		--					AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, DonViTinh) = 3	 --Đơn vị của hình thức CPM, TRUE REACH
		--					AND NOT ( DmLoaiBannerREF IN ( 17, 18 )
		--								OR DmHinhThucQuangCao IN ( 13, 42 )
		--							)
		--					AND SoHopDong = @pSoHopDong
		--					AND HopDongChiTietREF = @pHopDongChiTietID
		--					AND DonViTinh <> N'TRUE REACH'
		--			GROUP BY HopDongID
		--					, SoHopDong
		--					, DmMaHopDongREF
		--					, TenMaHopDong
		--					, NgayDanhSoHopDong
		--					, NgayKyHopDong
		--					, NhanHopDong
		--					, NgayNhanBanFax
		--					, NgayNhanHopDongBanCung
		--					, NgayChuyenHopDongChoKeToan
		--					, So
		--					, Thang
		--					, Nam
		--					, GiaTriHopDong
		--					, CongNo
		--					, HopDongChiTietREF
		--					, DangSuDung
		--					, IsGiayPhep
		--					, TrangThaiHopDong
		--					, IsBanCung
		--					, DmPhongBanREF
		--					, TenPhongBan
		--					, DmBoPhanREF
		--					, TenBoPhan
		--					, DmNhomLamViecREF
		--					, TenNhomLamViec
		--					, DmDiaDiemLamViecREF
		--					, TenDiaDiemLamViec
		--					, SysNhanVienREF
		--					, TenDangNhap
		--					, TenNhanVien
		--					, TenKhachHang
		--					, NhanHang
		--					, DmNhomNganhREF
		--					, TenNhomNganh
		--					, DmHinhThucQuangCao
		--					, TenHinhThucQuangCao
		--					, DmSanPhamREF
		--					, TenSanPham
		--					, DmNhomWebsiteREF
		--					, TenNhomWebsite
		--					, DmChuyenMucREF
		--					, TenChuyenMuc
		--					, DmLoaiBannerREF
		--					, TenLoaiBanner
		--					, DmViTriREF
		--					, TenViTri
		--					, SoLuong
		--					, DonViTinh
		--					, DonGia
		--					, DonGiaTheoDonVi
		--					, ChietKhau
		--					, GiamGia
		--					, ThanhTien
		--					, TiLeTuVan
		--					, ChiPhiTuVan
		--					, IsKhuyenMai
		--					, KhuyenMai
		--					, DmBannerREF
		--					, DmChienDichREF
		--					, DmWebsiteREF
		--					, TenWebsite

		--2. THUC HIEN TINH LAI

		--2.1 THUC HIEN TRUNCATE TABLE dbo.[ThucChayDaTinh_DoiTruVaTinhLai_CPM] TRUOC KHI TINH LAI
		DELETE FROM dbo.[ThucChayDaTinh_DoiTruVaTinhLai_CPM]

		SELECT TOP (1) @ThanhTienTruocCK =  ROUND(TD.SoLuongThucChay*TD.DonGiaTheoDonViTinh,0) ,
			@ThanhTienThucChayTruocCK = td.ThanhtientruocCK 
		FROM
		(
			SELECT  ( CASE WHEN ((UPPER(C.DonViTinh) = 'CPM' ) OR (UPPER(C.DonViTinh) = 'TRUE REACH' ))
													   THEN ISNULL(A.TongViewThucChay,0)
													   WHEN ( ( C.IsKhuyenMai = 0 )
															  AND (( UPPER(C.DonViTinh) = 'CPC' ) )
															)
													   THEN ISNULL(A.TongClickThucChay,0)
													   ELSE 0
					END ) AS SoLuongThucChay ,
				ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,
																		  C.DonViTinh,
																		  C.DonGia,
																		  GETDATE(),
																		  GETDATE(),
																		  A.HopDongChiTietREF),
													   0) AS DonGiaTheoDonViTinh ,
				C.DONGIA*C.SOLUONG ThanhtientruocCK,
				C.HopDongChiTietID
			FROM  
				( SELECT   ROUND(SUM(( A.TongViewThucChay
								* B.TiLeThucChayHDCTSoVoiBanner )
								/ 100), 0) TongViewThucChay ,
					ROUND(SUM(( A.TongClickThucChay
								* B.TiLeThucChayHDCTSoVoiBanner )
								/ 100), 0) TongClickThucChay ,
					B.HopDongChiTietREF ,
					A.DmSanPhamREF
					FROM      (SELECT SUM(A.TongViewThucChay) TongViewThucChay 
							, SUM(A.TongClickThucChay) TongClickThucChay
						, A.SoHopDong,A.DmSanPhamREF, A.DmBannerREF  
						FROM dbo.ThucChay A WHERE 1=1 
						AND A.DmSanPhamREF = @DmSanPhamREF
						AND A.SoHopDong = @SoHopDong
						GROUP BY A.SoHopDong,A.DmSanPhamREF, A.DmBannerREF
					) A
					INNER JOIN ( SELECT DISTINCT
									B.DmBannerID ,
									B.HopDongChiTietREF ,
									B.HopDongREF ,
									B.TiLeThucChayHDCTSoVoiBanner ,
									B.DeletedStatus ,
									B.DaThucHienUpdateTiLe
									FROM
									dbo.ThucChayHopDongChiTietAndBanner B
									WHERE B.HopDongChiTietREF = 694330
									AND B.DeletedStatus = 0
								) B ON B.DmBannerID = CONVERT(NVARCHAR(50), A.DmBannerREF)
			WHERE     1=1
			GROUP BY  B.HopDongChiTietREF ,
					A.DmSanPhamREF 
			) A
			INNER JOIN (SELECT C.* FROM dbo.HopDongChiTiet C WHERE C.HopDongChiTietID = @pHopDongChiTietID
					AND C.DeletedStatus = 0
					AND C.DmSanPhamREF IN ( 231, 238, 339, 240,370, 598, 613, 735, 5056 )
					AND C.DmLoaiBannerREF NOT IN ( 17, 18 )--Khong tinh cho cac loai banner ChiPhi va Mua ngoai
					AND C.DmLoaiREF <> 13 --Khong tinh thuc chay cho HTQC Mua Ngoai
					AND C.DonViTinhREF <> 31 --Don vi tinh la TRUE REACH
					AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](C.DonViTinhREF,C.DonViTinh) = 3 --Đơn vị của hình thức CPM
			) C ON C.HopDongChiTietID = A.HopDongChiTietREF AND C.DmSanPhamREF = A.DmSanPhamREF
			)TD
			--WHERE ROUND(TD.SoLuongThucChay*TD.DonGiaTheoDonViTinh,0) <= TD.ThanhtientruocCK
			SET @ThanhTienTruocCK = ISNULL(@ThanhTienTruocCK,0)
			SET @ThanhTienThucChayTruocCK = ISNULL(@ThanhTienThucChayTruocCK,0)

		--1. NEU CO LECH TREO HA THI TINH TUNG NGAY
		IF @ThanhTienThucChayTruocCK > @ThanhTienTruocCK
		BEGIN
			PRINT 'TINH THEO TƯNG NGAY'
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
							 EXEC [dbo].[ThucChay_InsertThucChayDaTinh_DoiTruVaTinhLai_CPM_DEV] 
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
		--2. NEU KHONG CO LECH TREO HA THI TINH TONG
		ELSE
		BEGIN
			PRINT 'TINH TONG LUON'
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
					SELECT  1 AS ThucChayID
							, SoHopDong
							, '' AS DanhsachDmBookingREF
							, DmSanPhamREF
							, TenSanPham
							, 0 AS DmNhomWebsiteREF
							, '' AS TenNhomWebsite
							, DmWebsiteREF
							, TenWebsite
							, 0 AS DmChienDichREF
							, '' AS TenChienDich
							, DmBannerREF
							, '' TenBanner
							, @NgayThucHien NgayThucHien
							, SUM(TongViewThucChay) TongViewThucChay
							, SUM(TongClickThucChay) TongClickThucChay
							, '' AS CreatedBy
							, GETDATE() CreatedAt
							, '' LastModifiedBy
							, GETDATE() LastModifiedAt
							, 0 DeletedStatus
							, 0 PrintStatus
							, 0 RecordStatus
							, 0 TongSoBaiViet
							, 0 SoThuTuTheoNgay
							, TypeProduct
							, 0 BannerType
							, '' UserName
							, '' SaleName
							, '' Email
							, GETDATE() LastTimeCalc
							, GETDATE() sys_date
							, 0 IsReady
							, 0 ProductUnitID
							, '' ProductUnitName
							, '' BannerTypeName
							, 0 HopDongChiTietREF
							, '' CampainStatus
							, '' BannerStatus
							, 0 IsNoiBo
					FROM    dbo.ThucChay
					WHERE   NgayThucHien BETWEEN  @StartDate AND @EndDate
							AND TypeProduct NOT IN ( 1, 2, 17 )
							AND DmWebsiteREF <> 0
							AND SoHopDong = @pSoHopDong
					GROUP BY SoHopDong
							, DmSanPhamREF
							, TenSanPham
							, DmWebsiteREF
							, TenWebsite
							, DmBannerREF
							, TypeProduct

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
						EXEC [dbo].[ThucChay_InsertThucChayDaTinh_DoiTruVaTinhLai_CPM_DEV] 
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

			DELETE  FROM dbo.ThucChayTemp

		END

		
  
END



```
