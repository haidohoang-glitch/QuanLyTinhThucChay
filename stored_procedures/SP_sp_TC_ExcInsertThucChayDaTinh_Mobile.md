# Stored Procedure: `sp_TC_ExcInsertThucChayDaTinh_Mobile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-16 10:50:00.817000
- **Ngày sửa cuối**: 2024-10-24 09:53:45.467000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@pSoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--	ThucChay_ExcInsertThucChayDaTinhMobile_v4_BySoHopDong '2015-07-15','2015-07-15','QC180615'
--	exec sp_TC_ExcInsertThucChayDaTinh_Mobile '2017-07-04', '2017-07-04', 'QC2880517' 
CREATE PROCEDURE [dbo].[sp_TC_ExcInsertThucChayDaTinh_Mobile]--tinh ca truong hop 1 phan bo nhieu banner
	-- Add the parameters for the stored procedure here
    @StartDate DATETIME ,
    @EndDate DATETIME ,
    @pSoHopDong NVARCHAR(50)
AS
    BEGIN
        DECLARE @NgayThucHien DATETIME ,
            @SoHopDong NVARCHAR(50) ,
            @HopDongChiTietREF INT ,
            @DmBannerREF INT ,
            @DmWebsiteREF INT ,
            @TH INT
	
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
            @StartDate
		--update ti le
		EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_mobile]

        SET @NgayThucHien = @StartDate
        WHILE ( @NgayThucHien <= @EndDate )
            BEGIN
		
		--Insert vao bang temp --danh cho truong hop phanbo
                EXEC dbo.ThucChay_InsertToTemp_Mobile @NgayThucHien
	
		---------------------
				
                INSERT  INTO @Temp
                        SELECT DISTINCT
                                A.SoHopDong ,
                                A.DmBannerREF ,
                                A.DmWebsiteREF
                        FROM    dbo.ThucChay_MobileTemp A
                                LEFT JOIN ( SELECT  HopDongChiTietID
                                            FROM    dbo.HopDongChiTiet
                                            WHERE   DmSanPhamREF = 342
													AND DmLoaiREF <> 42 --khong tinh cho admatic haidh comment 21/06/2023
                                                    AND ( DmLoaiBannerREF = 17
                                                          OR DmLoaiNenTangREF = 8
                                                        )
                                                    AND DeletedStatus <> 1
													AND not(DonViTinhREF in (3,4)) --KHONG PHAI LA GOI TINH THEO NGAY,TUAN
                                          ) T ON A.HopDongChiTietREF = T.HopDongChiTietID
                        WHERE   A.NgayThucHien = @NgayThucHien
                                AND A.HopDongChiTietREF NOT IN ( 0, 1 )-- 20240925 HAIDH COMMENT Y/C SP TRA HOPDONGCHITIET DE VIEC TINH NAY DUNG, VI PHUONG PHAP TINH TINH LE KHONG DUNG THUC TE VAN HANH                                
								AND A.HopDongChiTietREF IS NOT NULL
                                AND T.HopDongChiTietID IS NULL
							

                INSERT  INTO @ThucChayHopDongChiTiet_Temp
                        SELECT  hd.SoHopDong ,
                                tc.DmBannerID ,
                                hdct.IsKhuyenMai ,
                                hdct.HopDongChiTietID ,
                                hd.HopDongID
                        FROM    dbo.ThucChayHopDongChiTietAndBanner tc
                                INNER JOIN (SELECT * FROM dbo.HopDongChiTiet WHERE DeletedStatus = 0 AND DonViTinhREF <> 3) hdct 
								ON tc.HopDongChiTietREF = hdct.HopDongChiTietID
                                INNER JOIN (SELECT * FROM dbo.HopDong hd WHERE   1=1 AND ( @pSoHopDong IS NULL OR hd.SoHopDong = @pSoHopDong) ) hd 
								ON tc.HopDongREF = hd.HopDongID
                                INNER JOIN ( SELECT * FROM   @Temp ) t2 
								ON CONVERT(NVARCHAR(50), t2.DmBannerREF) = CONVERT(NVARCHAR(50), tc.DmBannerID) AND t2.SoHopDong = hd.SoHopDong
						WHERE tc.DeletedStatus = 0
                       
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
                                                              CASE WHEN T.HopDongChiTietREF = 1 THEN 1
																	WHEN T.HopDongChiTietREF > 1 AND T.KhuyenMai > 0 AND T.HopDongChiTietREF <> T.KhuyenMai THEN 2
																	WHEN (T.HopDongChiTietREF > 1 AND T.KhuyenMai = 0) OR (T.HopDongChiTietREF = T.KhuyenMai AND T.HopDongChiTietREF > 1) THEN 3
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
																	  ( SELECT *
																		  FROM @ThucChayHopDongChiTiet_Temp tchdctt
																		) T1
																		  INNER JOIN ( SELECT *
																						FROM @Temp
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
                                EXEC sp_TC_ExcInsertThucChayDaTinh_Single_Mobile @DmBannerREF,
                                    @NgayThucHien, @SoHopDong, @DmWebsiteREF
                            END				
				

				--Tinh cho truong hop 1 banner co tren 2 HĐCT, trong do co HĐ khuyen mai
                        ELSE
                            IF @TH = 2
                                BEGIN
                                    EXEC sp_TC_ExcInsertThucChayDaTinh_CoChietKhau_Mobile @DmBannerREF,
                                        @NgayThucHien, @SoHopDong,
                                        @DmWebsiteREF
                                END
				

				--Tinh cho truong hop 1 banner co tren 2 HĐCT, trong do ko co HĐ khuyen mai	
                            ELSE
                                IF @TH = 3
                                    BEGIN 
                                        EXEC sp_TC_ExcInsertThucChayDaTinh_KoChietKhau_Mobile @DmBannerREF,
                                            @NgayThucHien, @SoHopDong,
                                            @DmWebsiteREF
                                    END
                                ELSE
                                    PRINT 'Khong xac dinh case'
			

                        FETCH NEXT FROM vendor_cursor INTO @SoHopDong,
                            @DmBannerREF, @DmWebsiteREF, @TH
                    END 
                CLOSE vendor_cursor;
                DEALLOCATE vendor_cursor;
			--haidh comment 25/07/2023 từ lâu không cập bảng đơn giá tính nên không có Tiền TC
			----Tinh truong hop khong so hop dong
   --             EXEC ThucChay_InsertThucChayDaTinh_MobileNoContract @NgayThucHien 
		
			---- Update Gia tri thay doi thuc chay Mobile
                EXEC sp_ThucChayDaTinh_Mobile_UpdateGiaTriThayDoi @NgayThucHien,
                    @NgayThucHien	, @pSoHopDong	
		
		
		----------************
		----XU LY HD HUY
  --              EXEC sp_TC_UpdateGiaTriThayDoi_HDHuy @NgayThucHien,
  --                  @NgayThucHien				
		
		------************
                DELETE  FROM @Table
                DELETE  FROM @ThucChayHopDongChiTiet_Temp
                DELETE  FROM @Temp


                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
	
            END 
    END

```
