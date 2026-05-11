# Stored Procedure: `sp_TC_ExcUpdateGTTDThucChayDaTinh_Mobile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-27 14:59:05.300000
- **Ngày sửa cuối**: 2017-12-05 09:53:02.933000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |
| `@pSoHopDong` | `nvarchar(100)` | No |
| `@DmBannerID` | `int(4)` | No |
| `@NgayTinhThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--SELECT * FROM  dbo.ThucChayDaTinh tcdt
--WHERE tcdt.HopDongChiTietREF = 109964
--AND tcdt.NgayThucHien = '2017-07-03 00:00:00.000'


--ThucChay_ExcInsertThucChayDaTinhMobile_v4_BySoHopDong '2015-07-15','2015-07-15','QC180615'
--	exec [dbo].[sp_TC_ExcUpdateGTTDThucChayDaTinh_Mobile]  109964, 'SH0050617', 0, '2017-07-03 00:00:00.000'
CREATE PROCEDURE [dbo].[sp_TC_ExcUpdateGTTDThucChayDaTinh_Mobile]--tinh ca truong hop 1 phan bo nhieu banner
	-- Add the parameters for the stored procedure here
   
	@HopDongChiTietID INT,
    @pSoHopDong NVARCHAR(50),
	@DmBannerID INT,--Banner thay doi
	@NgayTinhThucHien DATETIME
AS
    BEGIN




        DECLARE @NgayThucHien DATETIME ,
            @SoHopDong NVARCHAR(50) ,
            @HopDongChiTietREF INT ,
            @DmBannerREF INT ,
            @DmWebsiteREF INT ,
            @TH INT
			DECLARE  @StartDate DATETIME ,    @EndDate DATETIME 
	
        DECLARE @Table TABLE
            (
              SoHopDong NVARCHAR(50) ,
              DmBannerID INT ,
              DmWebsiteID INT ,
              TH INT
            )



        DECLARE @ThucChayHopDongChiTiet_Temp TABLE
            (
              SoHopDong NVARCHAR(50) ,
              DmBannerREF NVARCHAR(50) ,
              IsKhuyenMai INT ,
              HopDongChiTietID INT ,
              HopDongID INT
            )

        DECLARE @Temp TABLE
            (
              SoHopDong NVARCHAR(50) ,
              DmBannerREF INT ,
              DmWebsiteREF INT
            )



			--Insert vao bang HopDongChiTietAndBanner
        EXEC sp_TC_HopDongChiTietAndBannerByDmSanPhamREF 342,
            @NgayTinhThucHien


			--DAY DU LIEU VAO TABLE TAM
			DELETE FROM dbo.ThucChay_MobileTemp
			

			INSERT INTO dbo.ThucChay_MobileTemp
			        ( ThucChayID ,
			          SoHopDong ,
			          DanhsachDmBookingREF ,
			          DmSanPhamREF ,
			          TenSanPham ,
			          DmNhomWebsiteREF ,
			          TenNhomWebsite ,
			          DmWebsiteREF ,
			          TenWebsite ,
			          DmChienDichREF ,
			          TenChienDich ,
			          DmBannerREF ,
			          TenBanner ,
			          NgayThucHien ,
			          TongViewThucChay ,
			          TongClickThucChay ,
			          CreatedBy ,
			          CreatedAt ,
			          LastModifiedBy ,
			          LastModifiedAt ,
			          DeletedStatus ,
			          PrintStatus ,
			          RecordStatus ,
			          TongSoBaiViet ,
			          SoThuTuTheoNgay ,
			          TypeProduct ,
			          BannerType ,
			          UserName ,
			          SaleName ,
			          Email ,
			          LastTimeCalc ,
			          sys_date ,
			          IsReady ,
			          ProductUnitID ,
			          ProductUnitName ,
			          BannerTypeName ,
			          HopDongChiTietREF ,
			          CampainStatus ,
			          BannerStatus ,
			          IsNoiBo
			        )
			
			SELECT tc.ThucChayID ,
                   tc.SoHopDong ,
                   tc.DanhsachDmBookingREF ,
                   tc.DmSanPhamREF ,
                   tc.TenSanPham ,
                   tc.DmNhomWebsiteREF ,
                   tc.TenNhomWebsite ,
                   tc.DmWebsiteREF ,
                   tc.TenWebsite ,
                   tc.DmChienDichREF ,
                   tc.TenChienDich ,
                   tc.DmBannerREF ,
                   tc.TenBanner ,
                   tc.NgayThucHien ,
                   tc.TongViewThucChay ,
                   tc.TongClickThucChay ,
                   tc.CreatedBy ,
                   tc.CreatedAt ,
                   tc.LastModifiedBy ,
                   tc.LastModifiedAt ,
                   tc.DeletedStatus ,
                   tc.PrintStatus ,
                   tc.RecordStatus ,
                   tc.TongSoBaiViet ,
                   tc.SoThuTuTheoNgay ,
                   tc.TypeProduct ,
                   tc.BannerType ,
                   tc.UserName ,
                   tc.SaleName ,
                   tc.Email ,
                   tc.LastTimeCalc ,
                   tc.sys_date ,
                   tc.IsReady ,
                   tc.ProductUnitID ,
                   tc.ProductUnitName ,
                   tc.BannerTypeName ,
                   tc.HopDongChiTietREF ,
                   tc.CampainStatus ,
                   tc.BannerStatus ,
                   tc.IsNoiBo 
			FROM dbo.ThucChay tc
			WHERE tc.SoHopDong = @pSoHopDong
			AND dbo.GetDmSanPhamIDByTypeProductID(342) = tc.TypeProduct


			--Xac dinh ngay bat dau chay va ngay chay toi ngay	
			SELECT @StartDate = MIN(tcmt.NgayThucHien), @EndDate = MAX(tcmt.NgayThucHien) 
			FROM  dbo.ThucChayHopDongChiTietAndBanner tchdctab
				INNER JOIN dbo.ThucChay_MobileTemp tcmt ON CONVERT(NVARCHAR(200),tcmt.DmBannerREF) = tchdctab.DmBannerID
			WHERE tchdctab.HopDongChiTietREF = @HopDongChiTietID
				AND tcmt.NgayThucHien <= @NgayTinhThucHien
   
   

		IF CONVERT(DATE, @EndDate) = CONVERT(DATE, @NgayTinhThucHien)
			BEGIN
			    SET @EndDate = DATEADD(dd,-1, @EndDate)	
			END

	

        SET @NgayThucHien = @StartDate
        WHILE ( @NgayThucHien <= @EndDate )
            BEGIN
		
		---------------------
			
                INSERT  INTO @Temp
                        SELECT DISTINCT
                                A.SoHopDong ,
                                A.DmBannerREF ,
                                A.DmWebsiteREF
                        FROM    ThucChay_MobileTemp A
                                LEFT JOIN ( SELECT  HopDongChiTietID
                                            FROM    dbo.HopDongChiTiet
                                            WHERE   DmSanPhamREF = 342
                                                    AND ( DmLoaiBannerREF = 17
                                                          OR DmLoaiNenTangREF = 8
                                                        )
                                                    AND DeletedStatus <> 1
                                          ) T ON A.HopDongChiTietREF = T.HopDongChiTietID
                        WHERE   A.NgayThucHien = @NgayThucHien
                                AND A.HopDongChiTietREF NOT IN ( 0, 1 )
                                AND A.HopDongChiTietREF IS NOT NULL
                                AND T.HopDongChiTietID IS NULL
								--AND A.DmBannerREF = @DmBannerID



                INSERT  INTO @ThucChayHopDongChiTiet_Temp
                        SELECT  hd.SoHopDong ,
                                tc.DmBannerID ,
                                hdct.IsKhuyenMai ,
                                hdct.HopDongChiTietID ,
                                hd.HopDongID
                        FROM    ThucChayHopDongChiTietAndBanner tc
                                INNER JOIN HopDongChiTiet hdct ON tc.HopDongChiTietREF = hdct.HopDongChiTietID
                                INNER JOIN HopDong hd ON tc.HopDongREF = hd.HopDongID
                                INNER JOIN ( SELECT *
                                             FROM   @Temp
                                           ) t2 ON CONVERT(NVARCHAR(50), t2.DmBannerREF) = CONVERT(NVARCHAR(50), tc.DmBannerID)
                                                   AND t2.SoHopDong = hd.SoHopDong
                        WHERE   ( @pSoHopDong IS NULL
                                  OR hd.SoHopDong = @pSoHopDong
                                )
								AND hdct.HopDongChiTietID = @HopDongChiTietID


			--SELECT * FROM @Temp
			--SELECT * FROM  @ThucChayHopDongChiTiet_Temp tchdctt
				-- Xac dinh truong hop can tinh

				

                INSERT  INTO @Table
                        SELECT DISTINCT
                                T.SoHopDong ,
                                T.DmBannerREF ,
                                T.DmWebsiteREF ,
                                t2.TH
                        FROM    ( SELECT    *
                                  FROM      @Temp
                                ) T
                                INNER JOIN ( SELECT DISTINCT
                                                    t2.DmBannerREF ,
                                                    t2.HopDongChiTietID ,
                                                    t2.SoHopDong ,
                                                    T6.TH
                                             FROM   ( SELECT  T.DmBannerID ,
                                                              CASE
                                                              WHEN T.HopDongChiTietREF = 1
                                                              THEN 1
                                                              WHEN T.HopDongChiTietREF > 1
                                                              AND T.KhuyenMai > 0
                                                              THEN 2
                                                              WHEN T.HopDongChiTietREF > 1
                                                              AND T.KhuyenMai = 0
                                                              THEN 3
                                                              ELSE 0
                                                              END TH
                                                      FROM    ( SELECT
                                                              DmBannerID ,
                                                              COUNT(DISTINCT HopDongChiTietREF) HopDongChiTietREF ,
                                                              SUM(T4.IsKhuyenMai) KhuyenMai
                                                              FROM
                                                              ( SELECT
                                                              T1.SoHopDong ,
                                                              T1.DmBannerREF DmBannerID ,
                                                              t2.DmWebsiteREF ,
                                                              T1.HopDongChiTietID HopDongChiTietREF ,
                                                              T1.HopDongID ,
                                                              T1.IsKhuyenMai
                                                              FROM
                                                              ( SELECT
                                                              *
                                                              FROM
                                                              @ThucChayHopDongChiTiet_Temp tchdctt
                                                              ) T1
                                                              INNER JOIN ( SELECT
                                                              *
                                                              FROM
                                                              @Temp
                                                              ) t2 ON CONVERT(NVARCHAR(50), t2.DmBannerREF) = CONVERT(NVARCHAR(50), T1.DmBannerREF)
                                                              AND t2.SoHopDong = T1.SoHopDong
                                                              ) T4
                                                              GROUP BY DmBannerID
                                                              ) T
                                                    ) T6
                                                    INNER JOIN @ThucChayHopDongChiTiet_Temp t2 ON T6.DmBannerID = t2.DmBannerREF
                                             --WHERE  DmBannerID = 509570
                                           ) t2 ON T.DmBannerREF = t2.DmBannerREF
                                                   AND T.SoHopDong = t2.SoHopDong


				
				--SELECT  *
    --                FROM    @Table t
		--Duyet tung phan bo
                DECLARE vendor_cursor CURSOR
                FOR
                    SELECT  *
                    FROM    @Table t


                OPEN vendor_cursor
		
                FETCH NEXT FROM vendor_cursor INTO @SoHopDong, @DmBannerREF,
                    @DmWebsiteREF, @TH

                WHILE @@FETCH_STATUS = 0
                    BEGIN
			-- Truong hop map 1-1 
                        IF @TH = 1
                            BEGIN

                                EXEC sp_TC_ExcInsertThucChayDaTinh_Single_Mobile_TinhLai @DmBannerREF,
                                    @NgayThucHien, @SoHopDong, @DmWebsiteREF, @HopDongChiTietID, @NgayTinhThucHien
                            END				
				

			--Tinh cho truong hop 1 banner co tren 2 HĐCT, trong do co HĐ khuyen mai
                        ELSE
                            IF @TH = 2
                                BEGIN
                                    EXEC sp_TC_ExcInsertThucChayDaTinh_CoChietKhau_Mobile_TinhLai @DmBannerREF,
                                        @NgayThucHien, @SoHopDong,
                                        @DmWebsiteREF, @HopDongChiTietID, @NgayTinhThucHien
                                END
				

			--Tinh cho truong hop 1 banner co tren 2 HĐCT, trong do ko co HĐ khuyen mai	
                            ELSE
                                IF @TH = 3
                                    BEGIN 
                                        EXEC sp_TC_ExcInsertThucChayDaTinh_KoChietKhau_Mobile_TinhLai @DmBannerREF,
                                            @NgayThucHien, @SoHopDong,
                                            @DmWebsiteREF, @HopDongChiTietID, @NgayTinhThucHien
                                    END
                                ELSE
                                    PRINT 'Khong xac dinh case'
			

                        FETCH NEXT FROM vendor_cursor INTO @SoHopDong,
                            @DmBannerREF, @DmWebsiteREF, @TH
                    END 
                CLOSE vendor_cursor;
                DEALLOCATE vendor_cursor;
	
		

		------************
                DELETE  FROM @Table
                DELETE  FROM @ThucChayHopDongChiTiet_Temp
                DELETE  FROM @Temp


                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
	
            END 
    END

```
