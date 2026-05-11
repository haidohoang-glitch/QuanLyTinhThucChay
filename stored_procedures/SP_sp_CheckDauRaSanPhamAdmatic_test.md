# Stored Procedure: `sp_CheckDauRaSanPhamAdmatic_test`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-11-02 11:37:15.873000
- **Ngày sửa cuối**: 2017-11-02 11:38:19

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayDanhSo` | `datetime(8)` | No |
| `@NgayBatDau` | `datetime(8)` | No |
| `@NgayKetThuc` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- [dbo].[sp_CheckDauRaSanPhamAdmatic_test] '2014-01-01', '2017-10-30', '2017-10-30'
CREATE PROCEDURE [dbo].[sp_CheckDauRaSanPhamAdmatic_test]
	@NgayDanhSo DATETIME = '2014-01-01',
    @NgayBatDau DATETIME ,
    @NgayKetThuc DATETIME
AS
    BEGIN
        
		--DECLARE @NgayDanhSo DATETIME = '2014-01-01'

		IF ISNULL(@NgayBatDau, '1900-01-01 00:00:00.000') = '1900-01-01 00:00:00.000'
            SET @NgayBatDau = DATEADD(DD, -1, CONVERT(DATE, GETDATE()));
      
        IF ISNULL(@NgayKetThuc, '1900-01-01 00:00:00.000') = '1900-01-01 00:00:00.000'
            SET @NgayKetThuc = DATEADD(DD, -1, CONVERT(DATE, GETDATE())); 



		
		-- Xác định hợp đồng đã chạy xong
        SELECT  hd.HopDongChiTietID
        INTO    #HopDongChayXong
        FROM    [192.168.23.217].ABM_Data_Release.dbo.HopDongChiTiet hd
        WHERE   hd.DmSanPhamREF IN ( 231, 238, 339, 240, 370, 598, 613, 733, 342 )
                AND ABS(hd.ThanhtienThucChay - hd.ThanhTien) < 10;



		-- Xac định đơn vị tính và đơn giá nếu có
		SELECT DISTINCT DmBannerID , 
				ISNULL(DonGiaBanner_VAT, 0)/1.1 DonGiaBanner ,
			( CASE WHEN LoaiDonGiaTheoDVT = 1 THEN N'CPC'
						WHEN LoaiDonGiaTheoDVT IN ( 2, 3 ) THEN N'CPM'
						WHEN LoaiDonGiaTheoDVT IN ( 4 ) THEN N'TRUE VIEW'
						ELSE N''
					END ) DonViTinh
		INTO #AdmaticDonGiaBanner
		FROM      dbo.AdmaticDonGiaBanner
		WHERE DmBannerID <> 0



		SELECT  *
		INTO    #ThucChayTraVe
		FROM    ( SELECT    A.SoHopDong ,
							[dbo].[GetProductIDByTypeProduct](A.TypeProduct) DmSanPhamREF ,
							A.TenSanPham,
							A.DmBannerREF ,
							A.TenBanner ,
							DG.DonViTinh,
							CASE WHEN DG.DonViTinh = N'CPM' THEN A.TongViewThucChay
								WHEN DG.DonViTinh = N'CPC' THEN A.TongClickThucChay
								ELSE 0
							END  SLChay ,
							DG.DonGiaBanner,
							A.NgayThucHien ,
							CASE WHEN DG.DmBannerID IS NULL THEN 0
									ELSE 1 END CoDonGia
				  FROM      dbo.ThucChay A
							INNER JOIN #AdmaticDonGiaBanner DG ON A.DmBannerREF = DG.DmBannerID
				  WHERE     A.NgayThucHien BETWEEN @NgayBatDau AND	@NgayKetThuc
							AND	 [dbo].[GetProductIDByTypeProduct](A.TypeProduct) IN ( 231, 238, 339, 240, 370, 598, 613, 733, 342 )
				  UNION ALL
				  SELECT    A.SoHopDong ,
							[dbo].[GetProductIDByTypeProduct](A.TypeProduct) DmSanPhamREF ,
							A.TenSanPham,
							A.[bannerid] DmBannerREF ,
							'' TenBanner ,
							DG.DonViTinh,
							CASE WHEN DG.DonViTinh = N'CPM' THEN A.[Views]
								WHEN DG.DonViTinh = N'CPC' THEN A.[Clicks]
								ELSE 0
							END  SLChay ,
							DG.DonGiaBanner,
							A.NgayThucHien ,
							CASE WHEN DG.DmBannerID IS NULL THEN 0
									ELSE 1 END CoDonGia
				  FROM      dbo.ThucChayTrueView A
							INNER JOIN #AdmaticDonGiaBanner DG ON A.[bannerid] = DG.DmBannerID
				  WHERE     A.NgayThucHien BETWEEN @NgayBatDau AND	@NgayKetThuc
							AND	 [dbo].[GetProductIDByTypeProduct](A.TypeProduct) IN ( 231, 238, 339, 240, 370, 598, 613, 733, 342 )
				) T



		SELECT DISTINCT
			ThucChayHopDongChiTietID ,
			CONVERT(INT, DmBannerREF) DmBannerREF ,
			HopDongREF ,
			DmNhanHangREF ,
			ISNULL(DG.DonGiaBanner_VAT, 0)/1.1 DonGiaBanner ,
			DmHinhThucQuangCaoREF ,
			DmSanPhamREF ,
			( SELECT TOP 1
						( CASE WHEN LoaiDonGiaTheoDVT = 1 THEN N'CPC'
								WHEN LoaiDonGiaTheoDVT IN ( 2, 3 ) THEN N'CPM'
								WHEN LoaiDonGiaTheoDVT IN ( 4 ) THEN N'TRUE VIEW'
								ELSE N''
							END )
				FROM      dbo.AdmaticDonGiaBanner
				WHERE     DmBannerID = DmBannerREF
			) DonViTinh
		INTO #ThucChayHopDongChiTietAndBanner_Admatic
		FROM   dbo.ThucChayHopDongChiTiet CT
			LEFT JOIN dbo.AdmaticDonGiaBanner DG ON CT.DmBannerREF = DG.DmBannerID
		WHERE  DmHinhThucQuangCaoREF = 42
			AND CT.DeletedStatus = 0
			AND DG.DeletedStatus = 0
			--AND CONVERT(DATE, CT.LastModifiedAt) >= @NgayThucHien



		


		SELECT  T.HopDongREF ,
				T.SoHopDong ,
				T.DmNhanHangREF ,
				T.DmHinhThucQuangCaoREF ,
				T.DmSanPhamREF ,
				T.TenSanPham ,
				T.DonViTinh ,
				T.DmBannerREF ,
				SUM(SLChay)  SLChay ,
				T.DonGiaBanner,
				T.NgayThucHien,
				T.CoDonGia,
				T.IsTreo
		INTO #ThucChay_Admatic
		FROM    ( SELECT    A.SoHopDong ,
							B.HopDongREF,
							B.DmNhanHangREF ,
							B.DmHinhThucQuangCaoREF ,
							A.DmSanPhamREF ,
							A.TenSanPham,
							A.DonViTinh ,
							A.DmBannerREF ,
							A.TenBanner ,
							A.SLChay ,
							B.DonGiaBanner,
							A.NgayThucHien ,
							A.CoDonGia ,
							CASE WHEN B.HopDongREF IS NULL THEN 0
									ELSE 1 END IsTreo
				  FROM      #ThucChayTraVe A
							INNER JOIN ( SELECT DISTINCT
												hd.SoHopDong,
												bn.HopDongREF,
												bn.DmBannerREF DmBannerID ,
												bn.ThucChayHopDongChiTietID ,
                                                bn.DmBannerREF ,
                                                bn.DmNhanHangREF ,
                                                bn.DonGiaBanner ,
                                                bn.DmHinhThucQuangCaoREF ,
                                                bn.DmSanPhamREF ,
                                                bn.DonViTinh
										 FROM   #ThucChayHopDongChiTietAndBanner_Admatic bn
												INNER JOIN  dbo.HopDong HD ON HD.HopDongID = bn.HopDongREF
									   ) B ON B.SoHopDong = A.SoHopDong
											  AND A.DmBannerREF = B.DmBannerREF
											  AND A.DmSanPhamREF = B.DmSanPhamREF
				) T
				INNER JOIN HopDong D on D.SoHopDong = T.SoHopDong
			WHERE D.TrangThaiHopDong != 3
			GROUP BY  T.HopDongREF ,
					T.SoHopDong ,
					T.DmNhanHangREF ,
					T.DmHinhThucQuangCaoREF ,
					T.DmSanPhamREF ,
					T.TenSanPham ,
					T.DonViTinh ,
					T.DmBannerREF ,
					T.DonGiaBanner,
					T.NgayThucHien,
					T.CoDonGia,
					T.IsTreo

		




		SELECT DISTINCT
				ThucChay.NgayThucHien,
				'' DotChayBooking,
			   ThucChay.HopDongREF HopDongID,
			   ThucChay.SoHopDong ,
			   NULL HopDongChiTietREF,
			   ThucChay.DmSanPhamREF ,
			   ThucChay.TenSanPham ,
			   ThucChay.DmHinhThucQuangCaoREF ,
			   ThucChay.DmBannerREF ,
			   ThucChay.SLChay SLThucChay,
			   ThucChay.ThanhTienThucChay,
			   TCDaTinh.SLThucChay SLDaTinh,
			   TCDaTinh.TTThucChay ThanhTienDaTinh,
			   CASE WHEN ThucChay.ThanhTienThucChay - TCDaTinh.TTThucChay != 0 THEN 13
					WHEN ThucChay.SLChay - TCDaTinh.SLThucChay != 0 THEN 21
						WHEN IsTreo = 0 THEN 14
						WHEN CoDonGia = 0 THEN 15
						WHEN (IsTreo = 1 AND CoDonGia = 1 AND TCDaTinh.TTThucChay IS NULL) THEN 16
						ELSE 9999
				END IDLoi ,
			   '' TenLoiChiTiet ,
			   '' SPXuLy ,
			   0 TrangThaiXuLy ,
			   GETDATE() CreateAt,
			   ThucChay.IsTreo,
			   ThucChay.CoDonGia
		INTO #KetQua	
		FROM 
			(
				SELECT T.HopDongREF ,
					   T.SoHopDong ,
					   T.DmNhanHangREF ,
					   T.DmHinhThucQuangCaoREF ,
					   T.DmSanPhamREF ,
					   T.TenSanPham ,
					   T.DonViTinh ,
					   T.DmBannerREF ,
					   T.SLChay ,
					   T.DonGiaBanner,
					   ROUND(T.SLChay * (CASE WHEN T.DonViTinh = 'CPM' THEN T.DonGiaBanner/1000
										ELSE T.DonGiaBanner END), 0) AS ThanhTienThucChay,
						T.NgayThucHien,
						T.CoDonGia,
						T.IsTreo
				FROM 
				(
					SELECT *
					FROM    #ThucChay_Admatic A
				) T
			) ThucChay LEFT JOIN (
								SELECT  HopDongID
									, SoHopDong
									--, HopDongChiTietREF
									--, NhanHang
									--, DmHinhThucQuangCao
									, DmSanPhamREF
									--, TenSanPham
									--, SoLuong
									--, DonViTinh
									--, DonGia
									--, DonGiaTheoDonVi
									--, ChietKhau
									--, ThanhTien
									, DmBannerREF
									--, DmWebsiteREF
									--, TenWebsite
									--, TongViewThucChay
									--, TongClickThucChay
									, SUM(SoLuongThucChay + SoLuongThucChayLechTreoHa) SLThucChay
									, ROUND(SUM(ThanhTienThucChayTruocTrietKhau + ThanhTienLechTreoHa), 0) TTThucChay
									--, SoLuongThayDoi
									--, GiaTriThayDoi
									, NgayThucHien
									--, GhiChu
									--, ThucChayDaTinhID
									--, *
							FROM    dbo.ThucChayDaTinh
							WHERE   DmHinhThucQuangCao = 42 --Admatic
									AND DmSanPhamREF IN ( 231, 238, 339, 240, 370, 598, 613, 733, 342 )
									AND DmLoaiBannerREF NOT IN ( 17, 18 )
									AND NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
									--AND HopDongID = 503189
							GROUP BY HopDongID
									, SoHopDong
									, DmSanPhamREF
									, DmBannerREF
									, NgayThucHien
						) TCDaTinh ON ThucChay.HopDongREF = TCDaTinh.HopDongID
										AND	TCDaTinh.DmSanPhamREF = ThucChay.DmSanPhamREF
										AND TCDaTinh.DmBannerREF = ThucChay.DmBannerREF
										AND TCDaTinh.NgayThucHien = ThucChay.NgayThucHien
				WHERE ThucChay.ThanhTienThucChay - TCDaTinh.TTThucChay != 0
						OR ThucChay.SLChay - TCDaTinh.SLThucChay != 0
						OR (ThucChay.IsTreo = 1 AND ThucChay.CoDonGia = 1 AND TCDaTinh.TTThucChay IS NULL)
						OR ThucChay.IsTreo = 0
						OR ThucChay.CoDonGia = 0



			
			SELECT NgayThucHien ,
                   DotChayBooking ,
                   HopDongID ,
                   SoHopDong ,
                   HopDongChiTietREF ,
                   DmSanPhamREF ,
                   TenSanPham ,
                   DmHinhThucQuangCaoREF ,
				   CASE WHEN KQ.IDLoi = 13 THEN dbo.FormatNumber(ThanhTienThucChay)
						WHEN KQ.IDLoi = 21 THEN dbo.FormatNumber(SLThucChay)
						ELSE dbo.FormatNumber(ThanhTienThucChay) END,
                   CASE WHEN KQ.IDLoi = 13 THEN dbo.FormatNumber(ThanhTienDaTinh)
						WHEN KQ.IDLoi = 21 THEN dbo.FormatNumber(SLDaTinh)
						ELSE dbo.FormatNumber(ThanhTienDaTinh) END ,
                   IDLoi ,
                   L.TenLoiChiTiet ,
                   L.SPXuly ,
                   TrangThaiXuLy ,
                   CreateAt ,
				   DmBannerREF
			FROM #KetQua KQ
					INNER JOIN dbo.KiemSoatThucChay_DanhSachLoi L ON KQ.IDLoi = L.ID
			
			

    END;
	--sp_CheckDauRaSanPhamCPD_v1 '2015-01-01','2017-07-02','2017-08-02'




```
