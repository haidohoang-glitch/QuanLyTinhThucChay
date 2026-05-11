# Stored Procedure: `BI_HoSoNganhCha`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-25 16:17:15.857000
- **Ngày sửa cuối**: 2015-06-25 16:17:15.857000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNganhHangREF` | `int(4)` | No |
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROC [dbo].[BI_HoSoNganhCha]
    (
      @DmNganhHangREF INT,
      @FromDate DATETIME ,
      @ToDate DATETIME
    )
AS 
    BEGIN
        DECLARE @DmCaseNganhHang TABLE
            (
              STT INT ,
              DmNganhHangREF INT ,              
              TenNganhHang NVARCHAR(500) ,
              DmNganhHangChaREF INT ,
              Levels INT ,
              DmNganhHangChaGocREF INT,
              DmNganhHangID NVARCHAR(255)
            );
        DECLARE @tableDoanhSoNganhHangTong TABLE
            (
              Rowid INT ,
              DmNganhHangID INT ,
              TenNganhHang NVARCHAR(MAX) ,
              DmNhanHangREF NVARCHAR(MAX) ,
              TenNhanHang NVARCHAR(MAX) ,
              DmNganhHangChaREF INT ,
              levels INT ,
              SoHopDong NVARCHAR(100) ,
              HopDongREF INT ,
              TenNhanVien NVARCHAR(300) ,
              TenBoPhan NVARCHAR(200) ,
              TenKhachHang NVARCHAR(400) ,
              DoanhSoKyHaiDau BIGINT ,
              ThucChay BIGINT ,
              DmSanPhamREF INT ,
              TenSanPham NVARCHAR(200)
            );
            
--PHAN 1
--1.1 THONG TIN CHUNG

        SELECT  dnh.DmNghanhHangID DmNganhHangID ,
                dnh.TenNghanhHang TenNganhHang ,
                N'Đang chạy' TinhTrangNganhHang
        FROM    DmNghanhHang dnh
        WHERE   dnh.DmNghanhHangID = @DmNganhHangREF
	
--1.2 THONG TIN DOANH SO CHUNG

;
        WITH    cte
                  AS ( SELECT   dnh.DmNghanhHangID ,
                                TenNghanhHang ,
                                dnh.DmNghanhHangREF ,
                                levels = 0 ,
                                DmNganhHangGocID = dnh.DmNghanhHangID ,
                                RIGHT('000'
                                      + CONVERT(VARCHAR(MAX), DmNghanhHangID),
                                      3) AS Lvl
                       FROM     DmNghanhHang dnh
                       WHERE    1 = 1
                                AND dnh.DmNghanhHangID = @DmNganhHangREF 
	  --dnh.DmNghanhHangREF =0
                                AND dnh.DeletedStatus <> 1
                       UNION ALL
                       SELECT   s.DmNghanhHangID ,
                                s.TenNghanhHang ,
                                s.DmNghanhHangREF ,
                                levels = c.levels + 1 ,
                                DmNganhHangGocID ,
                                c.lvl + RIGHT('000'
                                              + CONVERT(VARCHAR(MAX), s.DmNghanhHangID),
                                              3) AS lvl
                       FROM     cte c
                                INNER JOIN DmNghanhHang s ON c.DmNghanhHangID = s.DmNghanhHangREF
                     )
                     
            INSERT  INTO @DmCaseNganhHang
                    SELECT  ROW_NUMBER() OVER ( ORDER BY lvl ) AS rowid ,
                            DmNghanhHangID ,
                            LEFT(REPLICATE('|- ', cte.levels)
                                 + cte.TenNghanhHang, 50) AS TenNghanhHang ,
                            ISNULL(DmNghanhHangREF, '') NganhHangChaREF ,
                            levels ,
                            DmNganhHangGocID,
                            CONVERT(NVARCHAR(255),DmNghanhHangID)
                    FROM    cte

--SELECT * FROM @DmCaseNganhHang

        INSERT  INTO @tableDoanhSoNganhHangTong
                SELECT  tb.STT ,
                        tb.DmNganhHangREF ,
                        tb.TenNganhHang ,
                        '' DmNhanHang ,
                        '' TenNhanHang ,
                        tb.DmNganhHangChaREF ,
                        tb.levels ,
                        ISNULL(DS.SoHopDong, '') SoHopDong ,
                        ISNULL(ds.HopDongREF, 0) HopDongREF ,
                        ISNULL(ds.TenNhanVien, '') TenNhanVien ,
                        ISNULL(ds.TenBoPhan, '') TenBoPhan ,
                        ISNULL(ds.TenKhachHang, '') TenKhachHang ,
                        ISNULL(ds.DoanhSoKyHaiDau, 0) * 1.1 DoanhSoKyHaiDau
 --, isnull(TC.ThucChay,0)*1.1 ThucChay
                        ,
                        ISNULL(( SELECT SUM(rnhtcf.DoanhSoThucChay) * 1.1
                                 FROM   RptNhanHangThucChayFull rnhtcf
                                        INNER JOIN DmNhanHang dnh ON dnh.DmNhanHangID = rnhtcf.DmNhanHangREF
                                 WHERE  dnh.DmNghanhHangREF = CONVERT(NVARCHAR(50), tb.DmNganhHangREF)
                                        AND rnhtcf.SoHopDong = ISNULL(DS.SoHopDong,
                                                              '')
                                        AND rnhtcf.DmSanPhamREF = ISNULL(ds.DmSanPhamREF,
                                                              0)
                                        AND dnh.DeletedStatus <> 1
                                        AND rnhtcf.NgayThucHien BETWEEN @FromDate AND @ToDate
                               ), 0) ThucChay ,
                        ISNULL(ds.DmSanPhamREF, 0) DmSanPhamREF ,
                        ISNULL(ds.TenSanPham, '') TenSanPham
                FROM    @DmCaseNganhHang tb
                        LEFT JOIN ( SELECT  rnhttct.DmNganhHangREF ,
                                            rnhttct.TenNganhHang ,
                                            rnhttct.TenNhanHang ,
                                            rnhttct.DmNhanHangREF ,
                                            rnhttct.SoHopDong ,
                                            rnhttct.HopDongREF ,
                                            hd.TenNhanVien ,
                                            hd.TenKhachHang ,
                                            hd.TenBoPhan ,
                                            rnhttct.TenSanPham ,
                                            rnhttct.DmSanPhamREF ,
                                            SUM(rnhttct.DoanhSoKyHaiDau) DoanhSoKyHaiDau
                                    FROM    RptNganhHangThongTinChiTiet rnhttct
                                            INNER JOIN HopDong hd ON hd.HopDongID = rnhttct.HopDongREF
	--INNER JOIN HopDongChiTiet hdct ON rnhttct.HopDongREF = hdct.HopDongFK
                                    WHERE   1 = 1
                                            AND CONVERT(DATE, rnhttct.NgayThucHien) BETWEEN @FromDate
                                                              AND
                                                              @ToDate
                                    GROUP BY rnhttct.DmNganhHangREF ,
                                            rnhttct.TenNganhHang ,
                                            rnhttct.TenNhanHang ,
                                            rnhttct.DmNhanHangREF ,
                                            rnhttct.SoHopDong ,
                                            rnhttct.HopDongREF ,
                                            hd.TenNhanVien ,
                                            hd.TenKhachHang ,
                                            hd.TenBoPhan ,
                                            rnhttct.TenSanPham ,
                                            rnhttct.DmSanPhamREF
	--,hdct.ChietKhau, hdct.TiLeTuVan
                                    
                                  ) DS ON tb.DmNganhHangREF = DS.DmNganhHangREF
                ORDER BY tb.STT

        SELECT  SUM(d.DoanhSoKyHaiDau) DoanhSoKyHaiDau ,
                SUM(d.ThucChay) ThucChay ,
                ( CASE WHEN SUM(d.DoanhSoKyHaiDau) = 0 THEN 0
                       ELSE ROUND(( CONVERT(FLOAT, SUM(d.ThucChay)) / CONVERT(FLOAT, SUM(d.DoanhSoKyHaiDau)) ) * 100,
                       3,3)
                  END ) TiLeDSThucChay_HaiDau ,
                COUNT(DISTINCT d.HopDongREF) SoLuongHD ,
                SUM(CASE WHEN d.SoHopDong LIKE 'HT%' THEN 1
                         ELSE 0
                    END) SoLuongHDHopTac
        FROM    @tableDoanhSoNganhHangTong d
	
	
	DECLARE @TongDSKyHaiDau BIGINT
	DECLARE @TongDSThucChay BIGINT
	
	SELECT @TongDSKyHaiDau = SUM(d.DoanhSoKyHaiDau),
		   @TongDSThucChay = SUM(d.ThucChay)
	FROM    @tableDoanhSoNganhHangTong d
	
----PHAN 2	
----2.1 HINH THUC KY
		SELECT A.*,
			   A.HinhThucKy + ' ' + CONVERT(NVARCHAR(255),A.TiLe_DS2Dau_DsTong) + '%' HinhThucKyShow		
		FROM
        (
			SELECT  CASE rnhhtk.HinhThucKy 
						WHEN 'Dai ly' THEN N'Đại lý' 
						WHEN 'Truc tiep' THEN N'Trực tiếp'
						ELSE rnhhtk.HinhThucKy 
						END HinhThucKy,
					SUM(rnhhtk.DoanhSoKyHaiDau) * 1.1 DoanhSoKyHaiDau,
					ROUND(( CONVERT(FLOAT, SUM(rnhhtk.DoanhSoKyHaiDau) * 1.1 )  /
					CONVERT(FLOAT,@TongDSKyHaiDau)) * 100,3,3) TiLe_DS2Dau_DsTong
			FROM    RptNganhHangThongTinChiTiet rnhhtk
			WHERE   rnhhtk.DmNganhHangREF IN (
					SELECT DISTINCT
							nh.DmNganhHangID
					FROM    @tableDoanhSoNganhHangTong nh )
					AND CONVERT(DATE, rnhhtk.NgayThucHien) BETWEEN @FromDate
														   AND    @ToDate
			GROUP BY rnhhtk.HinhThucKy
        )A

----2.2 NHAN VIEN KINH DOANH			
		DECLARE @T TABLE(
			TenNhanSu NVARCHAR(300),
			DoanhSoKyHaiDau FLOAT,
			TiLe_DS2Dau_DsTong FLOAT,
			DmNhanSuREF INT,
			TenNhanSuShow NVARCHAR(300)
		)
		
		INSERT INTO @T ( TenNhanSu, DoanhSoKyHaiDau, TiLe_DS2Dau_DsTong, DmNhanSuREF, TenNhanSuShow )			
        SELECT TOP 10 
        A.TenNhanSu,
        A.DoanhSoKyHaiDau,
        A.TiLe_DS2Dau_DsTong,
        A.DmNhanSuREF,
        A.TenNhanSu + ' ' + CONVERT(NVARCHAR(255),A.TiLe_DS2Dau_DsTong) + '%'
        FROM (
			SELECT  rnhns.DmNhanSuREF ,
					rnhns.TenNhanSu ,
					SUM(rnhns.DoanhSoKyHaiDau) * 1.1 DoanhSoKyHaiDau,
					ROUND(( CONVERT(FLOAT,(SUM(rnhns.DoanhSoKyHaiDau) * 1.1))  /
					CONVERT(FLOAT,@TongDSKyHaiDau)) * 100,3,3) TiLe_DS2Dau_DsTong
			FROM    RptNganhHangThongTinChiTiet rnhns
			WHERE   rnhns.DmNganhHangREF IN (
					SELECT DISTINCT
							nh.DmNganhHangID
					FROM    @tableDoanhSoNganhHangTong nh )
					AND CONVERT(DATE, rnhns.NgayThucHien) BETWEEN @FromDate
														  AND     @ToDate
			GROUP BY rnhns.DmNhanSuREF ,
					rnhns.TenNhanSu
        )A
        ORDER BY A.TiLe_DS2Dau_DsTong DESC
		
		DECLARE @DSOther FLOAT
		DECLARE @TongDSOther FLOAT
		
		SELECT @DSOther = 100 - SUM(T1.TiLe_DS2Dau_DsTong) 
		FROM @T T1
		
		SELECT @TongDSOther = @TongDSKyHaiDau - SUM(T1.DoanhSoKyHaiDau) 
		FROM @T T1
		
		INSERT INTO @T( TenNhanSu, DoanhSoKyHaiDau ,TiLe_DS2Dau_DsTong, TenNhanSuShow) 
		VALUES (N'Other ', @TongDSOther, @DSOther ,N'Other ' + CONVERT(NVARCHAR(255),@DSOther) + '%')
		          		
		SELECT    ISNULL(DmNhanSuREF, 0) DmNhanSuREF ,
				TenNhanSu ,
				ISNULL(DoanhSoKyHaiDau,0) DoanhSoKyHaiDau ,				
				ISNULL(TiLe_DS2Dau_DsTong,0) TiLe_DS2Dau_DsTong,
				TenNhanSuShow
		FROM    @T

----2.3 DOANH THU THUC CHAY THEO WEBSITE

        SELECT * 
        FROM 
        (
			SELECT  ISNULL(Website,'blank') Website,
					SUM(ISNULL(TC.DoanhSoThucChay, 0)) * 1.1 DoanhSoThucChay,
					ROUND((CONVERT(FLOAT,(SUM(ISNULL(TC.DoanhSoThucChay, 0)) * 1.1))  /
					CONVERT(FLOAT,@TongDSThucChay)) * 100,3,3) TiLe_DSThucChay_DsTong                
			FROM    ( SELECT    rnhtcf.DoanhSoThucChay ,
								(
				-- Doi voi cac san pham CPM 
								  CASE WHEN hdct.DmSanPhamREF IN ( 231, 238, 339,
																  342, 337, 240,
																  370 )
									   THEN hdct.TenNhomWebsite
									   ELSE hdct.TenWebsite
								  END ) AS Website
	                              
					  FROM      RptNhanHangThucChayFull rnhtcf
								INNER JOIN DmNhanHang dnh ON dnh.DmNhanHangID = rnhtcf.DmNhanHangREF
								INNER JOIN HopDongChiTiet hdct ON hdct.HopDongChiTietID = rnhtcf.HopDongChiTietREF
					  WHERE     dnh.DmNghanhHangREF IN (
								SELECT DISTINCT
										CONVERT(NVARCHAR(50), nh.DmNganhHangREF)
								FROM    @DmCaseNganhHang nh )
								AND dnh.DeletedStatus <> 1
								AND rnhtcf.NgayThucHien BETWEEN @FromDate AND @ToDate
					) TC
			GROUP BY Website
        )A ORDER BY A.Website
				
----2.4  DOANH SO HAI DAU THEO KENH
        SELECT ISNULL(A.DmKenhREF,0) DmKenhREF,
        A.TenKenh,
        A.DoanhSoKyHaiDau,
        A.TiLe_DS2Dau_DsTong ,
        A.TenKenh + ' ' + CONVERT(NVARCHAR(255),A.TiLe_DS2Dau_DsTong) + '%' TenKenhShow
        FROM
        (
			SELECT  rnhk.DmKenhREF ,
					rnhk.TenKenh ,
					SUM(rnhk.DoanhSoKyHaiDau) * 1.1 DoanhSoKyHaiDau,
					ROUND((CONVERT(FLOAT,(SUM(ISNULL(rnhk.DoanhSoKyHaiDau, 0)) * 1.1))  /
					CONVERT(FLOAT,@TongDSKyHaiDau)) * 100,3,3) TiLe_DS2Dau_DsTong
			FROM    RptNganhHangThongTinChiTiet rnhk
			WHERE   rnhk.DmNganhHangREF IN ( SELECT DISTINCT
													nh.DmNganhHangID
											 FROM   @tableDoanhSoNganhHangTong nh )
					AND CONVERT(DATE, rnhk.NgayThucHien) BETWEEN @FromDate
														 AND     @ToDate
			GROUP BY rnhk.DmKenhREF , rnhk.TenKenh
        )A ORDER BY A.TenKenh        

----PHAN 3
----3.1 DOANH SO KHACH HANG KY
        
        SELECT B.*,
        ROUND((CONVERT(FLOAT,(ISNULL(B.DoanhSoKyHaiDau, 0)))  /
		CONVERT(FLOAT,@TongDSKyHaiDau)) * 100,3,3) TiLe_DS2Dau_DsTong,
		ROUND((CONVERT(FLOAT,(ISNULL(B.ThucChay, 0)))  /
		CONVERT(FLOAT,DoanhSoKyHaiDau)) * 100,3,3) TiLe_Tc_Ds2Dau 
        FROM 
        (
			SELECT  A.TenKhachHang ,
					A.DmKhachHangREF ,					
					CASE A.HinhThucKy 
						WHEN 'Dai ly' THEN N'Đại lý' 
						WHEN 'Truc tiep' THEN N'Trực tiếp'
						ELSE A.HinhThucKy 
					END HinhThucKy,
					ISNULL(SUM(A.DoanhSoKyHaiDau),0) DoanhSoKyHaiDau ,
					ISNULL(SUM(A.ThucChay),0) ThucChay
			FROM    ( SELECT    A.* ,
								ISNULL(( SELECT SUM(rnhtcf.DoanhSoThucChay) * 1.1
										 FROM   RptNhanHangThucChayFull rnhtcf
												INNER JOIN HopDong hd ON rnhtcf.HopDongREF = hd.HopDongID
												INNER JOIN DmNhanHang dnh ON dnh.DmNhanHangID = rnhtcf.DmNhanHangREF
										 WHERE  dnh.DmNghanhHangREF = CONVERT(NVARCHAR(50), a.DmNganhHangREF)
												AND hd.DmKhachHangREF = ISNULL(a.DmKhachHangREF,
																  0)
												AND dnh.DeletedStatus <> 1
												AND rnhtcf.NgayThucHien BETWEEN @FromDate AND @ToDate
									   ), 0) ThucChay
					  FROM      ( SELECT    a.TenKhachHang ,
											a.DmKhachHangREF ,
											a.HinhThucKy ,
											a.DmNganhHangREF ,
											SUM(a.DoanhSoKyHaiDau) * 1.1 DoanhSoKyHaiDau
								  FROM      RptNganhHangThongTinChiTiet a
								  WHERE     a.DmNganhHangREF IN (
											SELECT DISTINCT
													nh.DmNganhHangID
											FROM    @tableDoanhSoNganhHangTong nh )
											AND CONVERT(DATE, a.NgayThucHien) BETWEEN @FromDate
																  AND
																  @ToDate
								  GROUP BY  a.TenKhachHang ,
											a.DmKhachHangREF ,
											a.HinhThucKy ,
											a.DmNganhHangREF
								) A
					) A
			GROUP BY A.TenKhachHang ,
					A.DmKhachHangREF ,
					A.HinhThucKy
        )B
        WHERE (B.DoanhSoKyHaiDau > 0 OR B.ThucChay > 0)
        
----PHAN 4
----DOANH THU SAN PHAM
        SELECT  B.*,
        
        ROUND((CONVERT(FLOAT,(ISNULL(B.DoanhSoKyHaiDau, 0)))  /
		CONVERT(FLOAT,@TongDSKyHaiDau)) * 100,3,3) TiLe_DS2Dau_DsTong,
		
		ROUND((CONVERT(FLOAT,(ISNULL(B.DoanhSoThucChay, 0)))  /
		CONVERT(FLOAT, CASE 
				WHEN B.DoanhSoKyHaiDau IS NULL THEN 1 
				WHEN B.DoanhSoKyHaiDau <=0 THEN 1
				ELSE B.DoanhSoKyHaiDau 
				END )) * 100,3,3) TiLe_Tc_Ds2Dau
		
        FROM    ( SELECT    A.TenSanPham ,
                            A.DmSanPhamREF ,
                            ISNULL(SUM(A.DoanhSoKyHaiDau),0) DoanhSoKyHaiDau ,
                            ISNULL(SUM(A.DoanhSoThucChay),0) DoanhSoThucChay
                  FROM      ( SELECT    A.* ,
                                        ISNULL(( SELECT SUM(rnhtcf.DoanhSoThucChay)
                                                        * 1.1
                                                 FROM   RptNhanHangThucChayFull rnhtcf
                                                        INNER JOIN DmNhanHang dnh ON dnh.DmNhanHangID = rnhtcf.DmNhanHangREF
                                                 WHERE  dnh.DmNghanhHangREF = CONVERT(NVARCHAR(50), a.DmNganhHangREF)
                                                        AND rnhtcf.DmSanPhamREF = a.DmSanPhamREF
                                                        AND dnh.DeletedStatus <> 1
                                                        AND rnhtcf.NgayThucHien BETWEEN @FromDate AND @ToDate
                                               ), 0) DoanhSoThucChay
                              FROM      ( SELECT    a.TenSanPham ,
                                                    A.DmSanPhamREF ,
                                                    a.DmNganhHangREF ,
                                                    SUM(a.DoanhSoKyHaiDau)
                                                    * 1.1 DoanhSoKyHaiDau
                                          FROM      RptNganhHangThongTinChiTiet a
                                          WHERE     a.DmNganhHangREF IN (
                                                    SELECT DISTINCT
                                                            nh.DmNganhHangID
                                                    FROM    @tableDoanhSoNganhHangTong nh )
                                                    AND CONVERT(DATE, a.NgayThucHien) BETWEEN @FromDate
                                                              AND
                                                              @ToDate
                                          GROUP BY  a.TenSanPham ,
                                                    A.DmSanPhamREF ,
                                                    a.DmNganhHangREF
                                        ) A
                            ) A
                  GROUP BY  A.TenSanPham ,
                            A.DmSanPhamREF
                ) B
                WHERE (B.DoanhSoKyHaiDau > 0 OR B.DoanhSoThucChay > 0)


----PHAN 5
----5.1 CHI TIET NGANH HANG
        SELECT  T1.*
        FROM    @tableDoanhSoNganhHangTong T1
        WHERE (T1.DoanhSoKyHaiDau > 0 OR T1.ThucChay > 0)
        ORDER BY T1.Rowid
        
----5.2 CHI TIET NHAN HANG THUOC NGANH HANG		
	   SELECT * FROM (
		   SELECT   tb.STT ,
					tb.DmNhanHangID ,
					tb.TenNhanHang ,
					tb.DmNganhHangREF ,
					dnh.TenNghanhHang TenNganhHang ,
					tb.DmNhanHangChaREF ,
					tb.DmNhanHangGocREF ,
					tb.levels ,
					ISNULL(DS.SoHopDong, '') SoHopDong ,
					ISNULL(ds.HopDongREF, 0) HopDongREF ,
					ISNULL(ds.TenNhanVien, '') TenNhanVien ,
					ISNULL(ds.TenBoPhan, '') TenBoPhan ,
					ISNULL(ds.TenKhachHang, '') TenKhachHang ,
					ISNULL(ds.DoanhSoKyHaiDau, 0) * 1.1 DoanhSoKyHaiDau ,
					ISNULL(TC.ThucChay, 0) * 1.1 ThucChay ,
					ISNULL(ds.DmSanPhamREF, 0) DmSanPhamREF ,
					ISNULL(ds.TenSanPham, '') TenSanPham
		   FROM     ( SELECT    *
					  FROM      DmCaseNhanHang dcnh
					  WHERE     dcnh.DmNganhHangREF IN ( SELECT DISTINCT
																DmNganhHangID
														 FROM   @DmCaseNganhHang )
					) tb
					INNER JOIN DmNghanhHang dnh ON tb.DmNganhHangREF = CONVERT(NVARCHAR(50), dnh.DmNghanhHangID)
					LEFT JOIN ( SELECT  rnhttct.DmNhanHangREF ,
										rnhttct.TenNhanHang ,
										rnhttct.TenNganhHang ,
										rnhttct.SoHopDong ,
										rnhttct.HopDongREF ,
										hd.TenNhanVien ,
										hd.TenKhachHang ,
										hd.TenBoPhan ,
										rnhttct.TenSanPham ,
										rnhttct.DmSanPhamREF ,
										SUM(rnhttct.DoanhSoKyHaiDau) DoanhSoKyHaiDau
								FROM    RptNhanHangThongTinChiTiet rnhttct
										INNER JOIN HopDong hd ON hd.HopDongID = rnhttct.HopDongREF
								WHERE   1 = 1
										AND CONVERT(DATE, rnhttct.NgayThucHien) BETWEEN @FromDate
																	  AND
																	  @ToDate
								GROUP BY rnhttct.DmNhanHangREF ,
										rnhttct.TenNhanHang ,
										rnhttct.TenNganhHang ,
										rnhttct.SoHopDong ,
										rnhttct.HopDongREF ,
										hd.TenNhanVien ,
										hd.TenKhachHang ,
										hd.TenBoPhan ,
										rnhttct.TenSanPham ,
										rnhttct.DmSanPhamREF
							  ) DS ON tb.DmNhanHangID = DS.DmNhanHangREF
					LEFT JOIN ( SELECT  rnhtcf.DmNhanHangREF ,
										rnhtcf.TenNhanHang ,
										rnhtcf.HopDongREF ,
										rnhtcf.DmSanPhamREF ,
										SUM(rnhtcf.DoanhSoThucChay) ThucChay
								FROM    RptNhanHangThucChayFull rnhtcf
								WHERE   1 = 1
										AND CONVERT(DATE, rnhtcf.NgayThucHien) BETWEEN @FromDate
																	  AND
																	  @ToDate
								GROUP BY rnhtcf.DmNhanHangREF ,
										rnhtcf.TenNhanHang ,
										rnhtcf.HopDongREF ,
										rnhtcf.DmSanPhamREF
							  ) TC ON DS.DmNhanHangREF = tc.DmNhanHangREF
									  AND ds.HopDongREF = tc.HopDongREF
									  AND ds.DmSanPhamREF = tc.DmSanPhamREF
		   --WHERE 1 = 1									  
		   --ORDER BY tb.DmNhanHangGocREF , tb.STT
	   )A
	   WHERE A.DoanhSoKyHaiDau > 0 OR A.ThucChay > 0
	   ORDER BY A.DmNhanHangGocREF,A.STT
	   	
----5.3 TONG DS NHAN HANG THUOC NGANH HANG      
       
       SELECT   A.DmNhanHangGocREF DmNhanHangREF ,
                DNH.TenNhanHang ,
                ISNULL(SUM(A.DoanhSoKyHaiDau),0) DoanhSoKyHaiDau ,
                ISNULL(SUM(A.ThucChay),0) ThucChay
       FROM     ( SELECT    tb.STT ,
                            tb.DmNhanHangID ,
                            tb.TenNhanHang ,
                            tb.DmNganhHangREF ,
                            dnh.TenNghanhHang TenNganhHang ,
                            tb.DmNhanHangChaREF ,
                            tb.DmNhanHangGocREF ,
                            tb.levels ,
                            ISNULL(DS.SoHopDong, '') SoHopDong ,
                            ISNULL(ds.HopDongREF, 0) HopDongREF ,
                            ISNULL(ds.TenNhanVien, '') TenNhanVien ,
                            ISNULL(ds.TenBoPhan, '') TenBoPhan ,
                            ISNULL(ds.TenKhachHang, '') TenKhachHang ,
                            ISNULL(ds.DoanhSoKyHaiDau, 0) * 1.1 DoanhSoKyHaiDau ,
                            ISNULL(TC.ThucChay, 0) * 1.1 ThucChay ,
                            ISNULL(ds.DmSanPhamREF, 0) DmSanPhamREF ,
                            ISNULL(ds.TenSanPham, '') TenSanPham
                  FROM      ( SELECT    *
                              FROM      DmCaseNhanHang dcnh
                              WHERE     dcnh.DmNganhHangREF IN (
                                        SELECT DISTINCT
                                                DmNganhHangID
                                        FROM    @DmCaseNganhHang )
                            ) tb
                            INNER JOIN DmNghanhHang dnh ON tb.DmNganhHangREF = CONVERT(NVARCHAR(50), dnh.DmNghanhHangID)
                            LEFT JOIN ( SELECT  rnhttct.DmNhanHangREF ,
                                                rnhttct.TenNhanHang ,
                                                rnhttct.TenNganhHang ,
                                                rnhttct.SoHopDong ,
                                                rnhttct.HopDongREF ,
                                                hd.TenNhanVien ,
                                                hd.TenKhachHang ,
                                                hd.TenBoPhan ,
                                                rnhttct.TenSanPham ,
                                                rnhttct.DmSanPhamREF ,
                                                SUM(rnhttct.DoanhSoKyHaiDau) DoanhSoKyHaiDau
                                        FROM    RptNhanHangThongTinChiTiet rnhttct
                                                INNER JOIN HopDong hd ON hd.HopDongID = rnhttct.HopDongREF
                                        WHERE   1 = 1
                                                AND CONVERT(DATE, rnhttct.NgayThucHien) BETWEEN @FromDate
                                                              AND
                                                              @ToDate
                                        GROUP BY rnhttct.DmNhanHangREF ,
                                                rnhttct.TenNhanHang ,
                                                rnhttct.TenNganhHang ,
                                                rnhttct.SoHopDong ,
                                                rnhttct.HopDongREF ,
                                                hd.TenNhanVien ,
                                                hd.TenKhachHang ,
                                                hd.TenBoPhan ,
                                                rnhttct.TenSanPham ,
                                                rnhttct.DmSanPhamREF
                                      ) DS ON tb.DmNhanHangID = DS.DmNhanHangREF
                            LEFT JOIN ( SELECT  rnhtcf.DmNhanHangREF ,
                                                rnhtcf.TenNhanHang ,
                                                rnhtcf.HopDongREF ,
                                                rnhtcf.DmSanPhamREF ,
                                                SUM(rnhtcf.DoanhSoThucChay) ThucChay
                                        FROM    RptNhanHangThucChayFull rnhtcf
                                        WHERE   1 = 1
                                                AND CONVERT(DATE, rnhtcf.NgayThucHien) BETWEEN @FromDate
                                                              AND
                                                              @ToDate
                                        GROUP BY rnhtcf.DmNhanHangREF ,
                                                rnhtcf.TenNhanHang ,
                                                rnhtcf.HopDongREF ,
                                                rnhtcf.DmSanPhamREF
                                      ) TC ON DS.DmNhanHangREF = tc.DmNhanHangREF
                                              AND ds.HopDongREF = tc.HopDongREF
                                              AND ds.DmSanPhamREF = tc.DmSanPhamREF
                  WHERE     1 = 1
                ) A
                INNER JOIN DmNhanHang dnh ON DNH.DmNhanHangID = a.DmNhanHangGocREF
	   WHERE A.DoanhSoKyHaiDau > 0 OR A.ThucChay > 0	                
       GROUP BY A.DmNhanHangGocREF ,
                DNH.TenNhanHang
        
    END

```
