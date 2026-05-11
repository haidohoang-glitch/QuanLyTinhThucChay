# Stored Procedure: `sp_CheckDauVaoSanPhamAdmatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-08-24 09:33:57.497000
- **Ngày sửa cuối**: 2024-02-20 16:57:31.320000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayDanhSo` | `datetime(8)` | No |
| `@NgayBatDau` | `datetime(8)` | No |
| `@NgayKetThuc` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- [dbo].[sp_CheckDauVaoSanPhamAdmatic] '2014-01-01', '2017-11-08', '2017-11-08'
CREATE PROCEDURE [dbo].[sp_CheckDauVaoSanPhamAdmatic]
    @NgayDanhSo DATETIME = '2014-01-01'
  , @NgayBatDau DATETIME
  , @NgayKetThuc DATETIME
AS
    BEGIN
        
		--DECLARE @NgayDanhSo DATETIME = '2014-01-01'

        IF ISNULL(@NgayBatDau, '1900-01-01 00:00:00.000') = '1900-01-01 00:00:00.000'
            SET @NgayBatDau = DATEADD(DD, -1, CONVERT(DATE, GETDATE()));
      
        IF ISNULL(@NgayKetThuc, '1900-01-01 00:00:00.000') = '1900-01-01 00:00:00.000'
            SET @NgayKetThuc = DATEADD(DD, -1, CONVERT(DATE, GETDATE())); 



		
		---- Xác định hợp đồng đã chạy xong
  --      SELECT  hd.HopDongChiTietID
  --      INTO    #HopDongChayXong
  --      FROM    [192.168.23.217].ABM_Data_Release.dbo.HopDongChiTiet hd
  --      WHERE   hd.DmSanPhamREF IN ( 231, 238, 339, 240, 370, 598, 613, 733, 342 )
  --              AND ABS(hd.ThanhtienThucChay - hd.ThanhTien) < 10;



		-- Xác định đơn vị tính và đơn giá nếu có
        SELECT DISTINCT
                DmBannerID
              , ISNULL(DonGiaBanner_VAT, 0) / 1.1 DonGiaBanner
              , ( CASE WHEN LoaiDonGiaTheoDVT = 1 THEN N'CPC'
                       WHEN LoaiDonGiaTheoDVT IN ( 2, 3 ) THEN N'CPM'
                       WHEN LoaiDonGiaTheoDVT IN ( 4 ) THEN N'TRUE VIEW'
                       ELSE N''
                  END ) DonViTinh
        INTO    #AdmaticDonGiaBanner
        FROM    dbo.AdmaticDonGiaBanner
        WHERE   DmBannerID <> 0



		-- Xác định banner có đơn giá ko chuẩn với đơn vị tính
        SELECT  DmBannerID
        INTO    #CheckDonGia
        FROM    dbo.AdmaticDonGiaBanner
        WHERE   ( ( LoaiDonGiaTheoDVT IN ( 2, 3 )
                    AND DonGiaBanner_VAT < 10000
                  )
                  OR ( LoaiDonGiaTheoDVT IN ( 1 )
                       AND DonGiaBanner_VAT > 10000
                     )
                )
                AND DmBannerID <> 0
                AND DmBannerID IN ( SELECT DISTINCT
                                            DmBannerREF
                                    FROM    dbo.ThucChay
                                    WHERE   TypeProduct IN ( 10, 5, 8, 9, 14, 15, 16 )
                                            AND NgayThucHien >= @NgayBatDau )



        SELECT  *
        INTO    #ThucChayTraVe
        FROM    ( SELECT    A.SoHopDong
                          , [dbo].[GetProductIDByTypeProduct](A.TypeProduct) DmSanPhamREF
                          , A.TenSanPham
                          , A.DmBannerREF
                          , A.TenBanner
                          , DG.DonViTinh
                          , CASE WHEN DG.DonViTinh = N'CPM' THEN A.TongViewThucChay
                                 WHEN DG.DonViTinh = N'CPC' THEN A.TongClickThucChay
                                 ELSE 0
                            END SLChay
                          , DG.DonGiaBanner
                          , A.NgayThucHien
                          , CASE WHEN DG.DmBannerID IS NULL THEN 0
                                 ELSE 1
                            END CoDonGia
                  FROM      dbo.ThucChay A
                            INNER JOIN #AdmaticDonGiaBanner DG ON A.DmBannerREF = DG.DmBannerID
                  WHERE     A.NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
                            AND [dbo].[GetProductIDByTypeProduct](A.TypeProduct) IN ( 231, 238, 339, 240, 370, 598, 613, 733, 342 )
                            AND A.SoHopDong IN ( SELECT HD.SoHopDong
                                                 FROM   dbo.HopDongChiTiet CT
                                                        INNER JOIN dbo.HopDong HD ON CT.HopDongFK = HD.HopDongID
                                                 WHERE  CT.DmLoaiREF = 42 )
                  UNION ALL
                  SELECT    A.SoHopDong
                          , [dbo].[GetProductIDByTypeProduct](A.TypeProduct) DmSanPhamREF
                          , A.TenSanPham
                          , A.[bannerid] DmBannerREF
                          , '' TenBanner
                          , DG.DonViTinh
                          , CASE WHEN DG.DonViTinh = N'CPM' THEN A.[Views]
                                 WHEN DG.DonViTinh = N'CPC' THEN A.[Clicks]
                                 ELSE 0
                            END SLChay
                          , DG.DonGiaBanner
                          , A.NgayThucHien
                          , CASE WHEN DG.DmBannerID IS NULL THEN 0
                                 ELSE 1
                            END CoDonGia
                  FROM      dbo.ThucChayTrueView A
                            INNER JOIN #AdmaticDonGiaBanner DG ON A.[bannerid] = DG.DmBannerID
                  WHERE     A.NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
                            AND [dbo].[GetProductIDByTypeProduct](A.TypeProduct) IN ( 231, 238, 339, 240, 370, 598, 613, 733, 342 )
                            AND A.SoHopDong IN ( SELECT HD.SoHopDong
                                                 FROM   dbo.HopDongChiTiet CT
                                                        INNER JOIN dbo.HopDong HD ON CT.HopDongFK = HD.HopDongID
                                                 WHERE  CT.DmLoaiREF = 42 )
                ) T



        SELECT DISTINCT
                ThucChayHopDongChiTietID
              , CONVERT(INT, DmBannerREF) DmBannerREF
              , HopDongREF
              , DmNhanHangREF
              , ISNULL(DG.DonGiaBanner_VAT, 0) / 1.1 DonGiaBanner
              , DmHinhThucQuangCaoREF
              , DmSanPhamREF
              , ( SELECT TOP 1
                            ( CASE WHEN LoaiDonGiaTheoDVT = 1 THEN N'CPC'
                                   WHEN LoaiDonGiaTheoDVT IN ( 2, 3 ) THEN N'CPM'
                                   WHEN LoaiDonGiaTheoDVT IN ( 4 ) THEN N'TRUE VIEW'
                                   ELSE N''
                              END )
                  FROM      dbo.AdmaticDonGiaBanner
                  WHERE     DmBannerID = DmBannerREF
                ) DonViTinh
        INTO    #ThucChayHopDongChiTietAndBanner_Admatic
        FROM    dbo.ThucChayHopDongChiTiet CT
                LEFT JOIN ( SELECT  A.*
                            FROM    dbo.AdmaticDonGiaBanner A
                                    INNER JOIN ( SELECT MAX(AdmaticDonGiaBannerID) ID
                                                 FROM   dbo.AdmaticDonGiaBanner
                                                 WHERE  DeletedStatus = 0
                                                 GROUP BY DmBannerID
                                               ) B ON A.AdmaticDonGiaBannerID = B.ID
                          ) DG ON CT.DmBannerREF = DG.DmBannerID
        WHERE   DmHinhThucQuangCaoREF = 42
                AND CT.DeletedStatus = 0
			--AND CONVERT(DATE, CT.LastModifiedAt) >= @NgayThucHien




        SELECT  T.HopDongREF
              , T.SoHopDong
              , T.DmNhanHangREF
              , T.DmHinhThucQuangCaoREF
              , T.DmSanPhamREF
              , T.TenSanPham
              , T.DonViTinh
              , T.DmBannerREF
              , SUM(SLChay) SLChay
              , T.DonGiaBanner
              , T.NgayThucHien
              , T.CoDonGia
              , T.IsTreo
        INTO    #ThucChay_Admatic
        FROM    ( SELECT    A.SoHopDong
                          , B.HopDongREF
                          , B.DmNhanHangREF
                          , B.DmHinhThucQuangCaoREF
                          , A.DmSanPhamREF
                          , A.TenSanPham
                          , A.DonViTinh
                          , A.DmBannerREF
                          , A.TenBanner
                          , A.SLChay
                          , B.DonGiaBanner
                          , A.NgayThucHien
                          , CASE WHEN ISNULL(B.DonGiaBanner, 0) = 0 THEN 0
                                 ELSE 1
                            END CoDonGia
                          , CASE WHEN B.HopDongREF IS NULL THEN 0
                                 ELSE 1
                            END IsTreo
                  FROM      #ThucChayTraVe A
                            LEFT JOIN ( SELECT DISTINCT
                                                HD.SoHopDong
                                              , bn.HopDongREF
                                              , bn.DmBannerREF DmBannerID
                                              , bn.ThucChayHopDongChiTietID
                                              , bn.DmBannerREF
                                              , bn.DmNhanHangREF
                                              , bn.DonGiaBanner
                                              , bn.DmHinhThucQuangCaoREF
                                              , bn.DmSanPhamREF
                                              , bn.DonViTinh
                                        FROM    #ThucChayHopDongChiTietAndBanner_Admatic bn
                                                INNER JOIN dbo.HopDong HD ON HD.HopDongID = bn.HopDongREF
                                      ) B ON B.SoHopDong = A.SoHopDong
                                             AND A.DmBannerREF = B.DmBannerREF
                                             AND A.DmSanPhamREF = B.DmSanPhamREF
                ) T
                INNER JOIN HopDong D ON D.SoHopDong = T.SoHopDong
        WHERE   D.TrangThaiHopDong != 3
        GROUP BY T.HopDongREF
              , T.SoHopDong
              , T.DmNhanHangREF
              , T.DmHinhThucQuangCaoREF
              , T.DmSanPhamREF
              , T.TenSanPham
              , T.DonViTinh
              , T.DmBannerREF
              , T.DonGiaBanner
              , T.NgayThucHien
              , T.CoDonGia
              , T.IsTreo

		

		-- Check trường hợp có thực chạy, có thực treo nhưng ko có đơn giá trả về
        SELECT  *
        INTO    #ThucChay
        FROM    ( SELECT    A.SoHopDong
                          , [dbo].[GetProductIDByTypeProduct](A.TypeProduct) DmSanPhamREF
                          , A.TenSanPham
                          , A.DmBannerREF
                          , A.TenBanner
                          , A.NgayThucHien
                  FROM      dbo.ThucChay A
                  WHERE     A.NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
                            AND [dbo].[GetProductIDByTypeProduct](A.TypeProduct) IN ( 231, 238, 339, 240, 370, 598, 613, 733, 342 )
                            AND A.SoHopDong IN ( SELECT HD.SoHopDong
                                                 FROM   dbo.HopDongChiTiet CT
                                                        INNER JOIN dbo.HopDong HD ON CT.HopDongFK = HD.HopDongID
                                                 WHERE  CT.DmLoaiREF = 42 )
                  UNION ALL
                  SELECT    A.SoHopDong
                          , [dbo].[GetProductIDByTypeProduct](A.TypeProduct) DmSanPhamREF
                          , A.TenSanPham
                          , A.[bannerid] DmBannerREF
                          , '' TenBanner
                          , A.NgayThucHien
                  FROM      dbo.ThucChayTrueView A
                  WHERE     A.NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
                            AND [dbo].[GetProductIDByTypeProduct](A.TypeProduct) IN ( 231, 238, 339, 240, 370, 598, 613, 733, 342 )
                            AND A.SoHopDong IN ( SELECT HD.SoHopDong
                                                 FROM   dbo.HopDongChiTiet CT
                                                        INNER JOIN dbo.HopDong HD ON CT.HopDongFK = HD.HopDongID
                                                 WHERE  CT.DmLoaiREF = 42 )
                ) T


        INSERT  INTO #ThucChay_Admatic
                SELECT  T.HopDongREF
                      , T.SoHopDong
                      , T.DmNhanHangREF
                      , T.DmHinhThucQuangCaoREF
                      , T.DmSanPhamREF
                      , T.TenSanPham
                      , T.DonViTinh
                      , T.DmBannerREF
                      , SUM(SLChay) SLChay
                      , T.DonGiaBanner
                      , T.NgayThucHien
                      , T.CoDonGia
                      , T.IsTreo
                FROM    ( SELECT    A.SoHopDong
                                  , B.HopDongREF
                                  , B.DmNhanHangREF
                                  , B.DmHinhThucQuangCaoREF
                                  , A.DmSanPhamREF
                                  , A.TenSanPham
                                  , '' DonViTinh
                                  , A.DmBannerREF
                                  , A.TenBanner
                                  , 0 SLChay
                                  , B.DonGiaBanner
                                  , A.NgayThucHien
                                  , 0 CoDonGia
                                  , 1 IsTreo
                          FROM      #ThucChay A
                                    INNER JOIN ( SELECT DISTINCT
                                                        HD.SoHopDong
                                                      , bn.HopDongREF
                                                      , bn.DmBannerREF DmBannerID
                                                      , bn.ThucChayHopDongChiTietID
                                                      , bn.DmBannerREF
                                                      , bn.DmNhanHangREF
                                                      , bn.DonGiaBanner
                                                      , bn.DmHinhThucQuangCaoREF
                                                      , bn.DmSanPhamREF
                                                      , bn.DonViTinh
                                                 FROM   #ThucChayHopDongChiTietAndBanner_Admatic bn
                                                        INNER JOIN dbo.HopDong HD ON HD.HopDongID = bn.HopDongREF
                                               ) B ON B.SoHopDong = A.SoHopDong
                                                      AND A.DmBannerREF = B.DmBannerREF
                                                      AND A.DmSanPhamREF = B.DmSanPhamREF
                                    LEFT JOIN #AdmaticDonGiaBanner DG ON A.DmBannerREF = DG.DmBannerID
                          WHERE     DG.DmBannerID IS NULL
                        ) T
                        INNER JOIN HopDong D ON D.SoHopDong = T.SoHopDong
                WHERE   D.TrangThaiHopDong != 3
                GROUP BY T.HopDongREF
                      , T.SoHopDong
                      , T.DmNhanHangREF
                      , T.DmHinhThucQuangCaoREF
                      , T.DmSanPhamREF
                      , T.TenSanPham
                      , T.DonViTinh
                      , T.DmBannerREF
                      , T.DonGiaBanner
                      , T.NgayThucHien
                      , T.CoDonGia
                      , T.IsTreo




		-- Check trường hợp so sánh đơn giá trả về trên AdmaticDonGiaBanner với đơn giá ký trên HopDongChiTiet
        SELECT  A.HopDongREF
              , A.SoHopDong
              , A.DmNhanHangREF
              , A.DmHinhThucQuangCaoREF
              , A.DmSanPhamREF
              , A.TenSanPham
              , A.DonViTinh
              , A.DmBannerREF
              , A.SLChay
              , A.DonGiaBanner
              , A.NgayThucHien
              , A.CoDonGia
              , A.IsTreo
        INTO    #SoSanhDonGia
        FROM    ( SELECT    T.HopDongREF
                          , T.SoHopDong
                          , T.DmNhanHangREF
                          , T.DmHinhThucQuangCaoREF
                          , T.DmSanPhamREF
                          , T.TenSanPham
                          , T.DonViTinh
                          , T.DmBannerREF
                          , SUM(SLChay) SLChay
                          , T.DonGiaBanner
                          , T.NgayThucHien
                          , T.CoDonGia
                          , T.IsTreo
                  FROM      ( SELECT    A.SoHopDong
                                      , B.HopDongREF
                                      , B.DmNhanHangREF
                                      , B.DmHinhThucQuangCaoREF
                                      , A.DmSanPhamREF
                                      , A.TenSanPham
                                      , A.DonViTinh
                                      , A.DmBannerREF
                                      , A.TenBanner
                                      , A.SLChay
                                      , B.DonGiaBanner
                                      , A.NgayThucHien
                                      , A.CoDonGia
                                      , CASE WHEN B.HopDongREF IS NULL THEN 0
                                             ELSE 1
                                        END IsTreo
                              FROM      #ThucChayTraVe A
                                        INNER JOIN ( SELECT DISTINCT
                                                            HD.SoHopDong
                                                          , bn.HopDongREF
                                                          , bn.DmBannerREF DmBannerID
                                                          , bn.ThucChayHopDongChiTietID
                                                          , bn.DmBannerREF
                                                          , bn.DmNhanHangREF
                                                          , bn.DonGiaBanner
                                                          , bn.DmHinhThucQuangCaoREF
                                                          , bn.DmSanPhamREF
                                                          , bn.DonViTinh
                                                     FROM   #ThucChayHopDongChiTietAndBanner_Admatic bn
                                                            INNER JOIN dbo.HopDong HD ON HD.HopDongID = bn.HopDongREF
                                                   ) B ON B.SoHopDong = A.SoHopDong
                                                          AND A.DmBannerREF = B.DmBannerREF
                                                          AND A.DmSanPhamREF = B.DmSanPhamREF
                            ) T
                            INNER JOIN HopDong D ON D.SoHopDong = T.SoHopDong
                  WHERE     D.TrangThaiHopDong != 3
                  GROUP BY  T.HopDongREF
                          , T.SoHopDong
                          , T.DmNhanHangREF
                          , T.DmHinhThucQuangCaoREF
                          , T.DmSanPhamREF
                          , T.TenSanPham
                          , T.DonViTinh
                          , T.DmBannerREF
                          , T.DonGiaBanner
                          , T.NgayThucHien
                          , T.CoDonGia
                          , T.IsTreo
                ) A
                INNER JOIN ( SELECT HD.HopDongFK
                                  , HD.DonGia
                             FROM   dbo.HopDongChiTiet HD
                                    INNER JOIN ( SELECT *
                                                 FROM   ( SELECT    HopDongFK
                                                                  , COUNT(HopDongChiTietID) Dem
                                                          FROM      dbo.HopDongChiTiet
                                                          WHERE     DmLoaiREF = 42
                                                          GROUP BY  HopDongFK
                                                        ) T
                                                 WHERE  T.Dem = 1
                                               ) T ON HD.HopDongFK = T.HopDongFK
                             WHERE  HD.DmLoaiREF = 42
                                    AND HD.DmSanPhamREF <> 733
                           ) B ON A.HopDongREF = B.HopDongFK
        WHERE   A.DonGiaBanner <> B.DonGia


        SELECT DISTINCT
                ThucChay.NgayThucHien
              , '' DotChayBooking
              , ThucChay.HopDongREF HopDongID
              , ThucChay.SoHopDong
              , NULL HopDongChiTietREF
              , ThucChay.DmSanPhamREF
              , ThucChay.TenSanPham
              , ThucChay.DmHinhThucQuangCaoREF
              , ThucChay.DmBannerREF
              , ThucChay.SLChay SLThucChay
              , ThucChay.ThanhTienThucChay
              , TCDaTinh.SLThucChay SLDaTinh
              , TCDaTinh.TTThucChay ThanhTienDaTinh
              , CASE WHEN IsTreo = 0 THEN 14
                     WHEN CoDonGia = 0 THEN 15
                     ELSE 9999
                END IDLoi
              , '' TenLoiChiTiet
              , '' SPXuLy
              , 0 TrangThaiXuLy
              , GETDATE() CreateAt
              , ThucChay.IsTreo
              , ThucChay.CoDonGia
        INTO    #KetQua
        FROM    ( SELECT    T.HopDongREF
                          , T.SoHopDong
                          , T.DmNhanHangREF
                          , T.DmHinhThucQuangCaoREF
                          , T.DmSanPhamREF
                          , T.TenSanPham
                          , T.DonViTinh
                          , T.DmBannerREF
                          , T.SLChay
                          , T.DonGiaBanner
                          , ROUND(T.SLChay * ( CASE WHEN T.DonViTinh = 'CPM' THEN T.DonGiaBanner / 1000
                                                    ELSE T.DonGiaBanner
                                               END ), 0) AS ThanhTienThucChay
                          , T.NgayThucHien
                          , T.CoDonGia
                          , T.IsTreo
                  FROM      ( SELECT    *
                              FROM      #ThucChay_Admatic A
                            ) T
                ) ThucChay
                LEFT JOIN ( SELECT  HopDongID
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
                                    --AND DmSanPhamREF IN ( 231, 238, 339, 240, 370, 598, 613, 733, 342 ) --duongnt comment 19/06/2023
									AND DmSanPhamREF IN ( 231, 238, 339, 240, 370, 598, 613, 733, 342,305,680,821,5056,5133,5224,5268,5312)
									
                                    AND DmLoaiBannerREF NOT IN ( 17, 18 )
                                    AND NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
									--AND HopDongID = 503189
                            GROUP BY HopDongID
                                  , SoHopDong
                                  , DmSanPhamREF
                                  , DmBannerREF
                                  , NgayThucHien
                          ) TCDaTinh ON ThucChay.HopDongREF = TCDaTinh.HopDongID
                                        AND TCDaTinh.DmSanPhamREF = ThucChay.DmSanPhamREF
                                        AND TCDaTinh.DmBannerREF = ThucChay.DmBannerREF
                                        AND TCDaTinh.NgayThucHien = ThucChay.NgayThucHien
        WHERE   ThucChay.IsTreo = 0
                OR ThucChay.CoDonGia = 0

			
			-- Check trường hợp so sánh đơn giá trả về trên AdmaticDonGiaBanner với đơn giá ký trên HopDongChiTiet >> Cho vào #KetQua
        INSERT  INTO #KetQua
                SELECT DISTINCT
                        NgayThucHien
                      , '' DotChayBooking
                      , HopDongREF HopDongID
                      , SoHopDong
                      , NULL HopDongChiTietREF
                      , DmSanPhamREF
                      , TenSanPham
                      , DmHinhThucQuangCaoREF
                      , DmBannerREF
                      , SLChay SLThucChay
                      , ROUND(SLChay * ( CASE WHEN DonViTinh = 'CPM' THEN DonGiaBanner / 1000
                                              ELSE DonGiaBanner
                                         END ), 0) AS ThanhTienThucChay
                      , 0 SLDaTinh
                      , 0 ThanhTienDaTinh
                      , 17 IDLoi
                      , '' TenLoiChiTiet
                      , '' SPXuLy
                      , 0 TrangThaiXuLy
                      , GETDATE() CreateAt
                      , IsTreo
                      , CoDonGia
                FROM    #SoSanhDonGia 


        INSERT  INTO #KetQua
                SELECT  NULL
                      , '' DotChayBooking
                      , 0 HopDongID
                      , '' SoHopDong
                      , NULL HopDongChiTietREF
                      , 0 DmSanPhamREF
                      , '' TenSanPham
                      , 0
                      , DmBannerID
                      , 0 SLThucChay
                      , 0 AS ThanhTienThucChay
                      , 0 SLDaTinh
                      , 0 ThanhTienDaTinh
                      , 18 IDLoi
                      , '' TenLoiChiTiet
                      , '' SPXuLy
                      , 0 TrangThaiXuLy
                      , GETDATE() CreateAt
                      , 0
                      , 0
                FROM    #CheckDonGia


        SELECT  NgayThucHien
              , DotChayBooking
              , HopDongID
              , SoHopDong
              , HopDongChiTietREF
              , DmSanPhamREF
              , TenSanPham
              , DmHinhThucQuangCaoREF
              , DmBannerREF
              , SLThucChay
              , ThanhTienThucChay
              , SLDaTinh
              , ThanhTienDaTinh
              , IDLoi
              , L.TenLoiChiTiet
              , L.SPXuly
              , TrangThaiXuLy
              , CreateAt
        FROM    #KetQua KQ
                INNER JOIN dbo.KiemSoatThucChay_DanhSachLoi L ON KQ.IDLoi = L.ID
			where --LEN(DmBannerREF) =6
			DmBannerREF IN (SELECT DmBannerREF FROM dbo.ThucChayHopDongChiTiet WHERE LEN(DmBannerREF) = 6 AND CreatedBy LIKE N'%Branding%' ) ---Nhung sửa chỉ check vs các banner treo trên tool Branding
			

    END;
	--sp_CheckDauRaSanPhamCPD_v1 '2015-01-01','2017-07-02','2017-08-02'




```
