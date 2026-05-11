# Stored Procedure: `sp_TC_InsertThucChayDaTinh_PR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-05-08 10:46:56.560000
- **Ngày sửa cuối**: 2021-05-21 16:46:05.157000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@piHopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

/*
--EXEC [ThucChay_InsertThucChayDaTinh_PR_GoiHD_vt] '2017-04-08','2017-04-08'
-- [dbo].[sp_TC_InsertThucChayDaTinh_PR] '2018-10-22','2018-10-22', NULL
*/
CREATE PROCEDURE [dbo].[sp_TC_InsertThucChayDaTinh_PR]
    @StartDate DATETIME ,
    @EndDate DATETIME ,
    @piHopDongID INT = NULL
AS
    BEGIN

        DECLARE @NgayThucHien DATETIME , @NgayDSGioiHanTinh DATETIME
		DECLARE @v_count INT = 0, @v_row_thucchaytreopr INT = 0
		DECLARE @ThucTreoPRCanTinhNgay TABLE(
					ThucChayHopDongChiTietPRID INT NOT NULL,
                    HopDongREF INT NOT NULL,
                    ChietKhau FLOAT NULL,
                    ThucChayHopDongChiTietPrREF INT NULL ,
                    HopDongChiTietREF INT NULL ,
                    DmHinhThucQuangCaoREF INT NOT NULL,
                    DmSanPhamREF INT NOT NULL,
                    DmWebsiteREF INT NULL,
                    GiaTien INT NOT NULL,
                    SoLuong INT NOT NULL
		
		)
        SET @NgayThucHien = CONVERT(DATE, @StartDate);
		SET @NgayDSGioiHanTinh = '2019-12-31'
		
    --    UPDATE  dbo.ThucChayHopDongChiTietPR
    --    SET     RecordStatus = 0
    --    WHERE   1=1 AND EXISTS (
    --            SELECT DISTINCT DotChayBooking
    --            FROM    dbo.ThucChayDaTinh
    --            WHERE   NgayThucHien BETWEEN @StartDate AND @EndDate
				--		AND CONVERT(DATE,NgayDanhSoHopDong) <= @NgayDSGioiHanTinh
    --                    AND DmSanPhamREF IN ( 141, 245, 250, 637, 305 )
    --                    AND NOT ( DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18 ) 
				--		AND ( @piHopDongID IS NULL OR HopDongREF = @piHopDongID )
				--		AND DotChayBooking = ThucChayHopDongChiTietPRID
				--)

    --    DELETE  FROM dbo.ThucChayDaTinh
    --    WHERE   NgayThucHien BETWEEN @StartDate AND @EndDate
				--AND CONVERT(DATE,NgayDanhSoHopDong) <= @NgayDSGioiHanTinh
    --            AND DmSanPhamREF IN ( 141, 245, 250, 637, 305 )
    --            AND NOT ( DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18 )
				--AND ( @piHopDongID IS NULL OR HopDongID = @piHopDongID )
		
        WHILE ( @NgayThucHien <= @EndDate )
            BEGIN
				  DELETE FROM @ThucTreoPRCanTinhNgay
                  DECLARE @HopDongREF INT ,
                    @DmSanPhamREF INT
                   

					--THUC HIEN INSERT DU LIEU THUCCHAYHOPDONGCHITIETPR CAN TINH NGAY
					INSERT INTO @ThucTreoPRCanTinhNgay
					(
					    ThucChayHopDongChiTietPRID,
					    HopDongREF,
					    ChietKhau,
					    ThucChayHopDongChiTietPrREF,
					    HopDongChiTietREF,
					    DmHinhThucQuangCaoREF,
					    DmSanPhamREF,
					    DmWebsiteREF,
					    GiaTien,
					    SoLuong
					)
					
					 SELECT  ThucChayHopDongChiTietPRID ,
                            HopDongREF ,
                            ChietKhau ,
                            ThucChayHopDongChiTietPrREF ,
                            HopDongChiTietREF ,
                            DmHinhThucQuangCaoREF ,
                            DmSanPhamREF ,
                            DmWebsiteREF ,
                            GiaTien ,
                            SoLuong
                    FROM    dbo.ThucChayHopDongChiTietPR
                    WHERE   DeletedStatus <> 1
                            AND RecordStatus = 0
                            AND DmHinhThucQuangCaoREF <> 0
                            AND DmSanPhamREF <> 0
                            AND ThoiGianBatDau >= '2014-01-01'
                            AND ( CASE WHEN CreatedAt >= LastModifiedAt THEN CONVERT(DATE, CreatedAt)
                                       ELSE CONVERT(DATE, LastModifiedAt)
                                  END ) = @NgayThucHien
                            AND ( @piHopDongID IS NULL OR HopDongREF = @piHopDongID )
					UNION 
					SELECT  PR.ThucChayHopDongChiTietPRID ,
                            PR.HopDongREF ,
                            PR.ChietKhau ,
                            PR.ThucChayHopDongChiTietPrREF ,
                            PR.HopDongChiTietREF ,
                            PR.DmHinhThucQuangCaoREF ,
                            PR.DmSanPhamREF ,
                            PR.DmWebsiteREF ,
                            PR.GiaTien ,
                            PR.SoLuong
                    FROM    (SELECT * FROM dbo.ThucChayHopDongChiTietPR PR
								WHERE PR.DeletedStatus <> 1
								AND PR.RecordStatus = 0
								AND PR.DmHinhThucQuangCaoREF <> 0
								AND PR.DmSanPhamREF <> 0
								AND PR.ThoiGianBatDau >= '2014-01-01'
								AND PR.CreatedAt < @NgayThucHien
								AND ( @piHopDongID IS NULL OR HopDongREF = @piHopDongID )
							)PR
							INNER JOIN 
							(SELECT * FROM dbo.HopDong hd 
								WHERE hd.TrangThaiHopDong NOT IN (0,3)
								AND CONVERT(DATE, hd.LastModifiedAt) = @NgayThucHien
							)hd ON PR.HopDongREF = hd.HopDongID

                DECLARE icursor_pr CURSOR
                FOR
                    SELECT DISTINCT tc.HopDongREF, tc.DmSanPhamREF FROM @ThucTreoPRCanTinhNgay tc
					INNER JOIN 
					(SELECT hd.HopDongID, hd.NgayDanhSoHopDong 
						FROM dbo.HopDong hd 
						WHERE CONVERT(DATE,hd.NgayDanhSoHopDong) <= @NgayDSGioiHanTinh --Gioi han chi tinh cho tu nam 2019 tro ve truoc
					)hd ON tc.HopDongREF = hd.HopDongID
                OPEN icursor_pr;  

                FETCH NEXT FROM icursor_pr INTO @HopDongREF, @DmSanPhamREF

                WHILE @@FETCH_STATUS = 0
                    BEGIN  
							
							EXEC [dbo].[sp_TC_InsertThucChayDaTinh_PR_HopDongSanPham]
							@NgayThucHien = @NgayThucHien ,
							@HopDongREF = @HopDongREF,
							@DmSanPhamREF = @DmSanPhamREF
                       FETCH NEXT FROM icursor_pr INTO @HopDongREF, @DmSanPhamREF
                    END;   
                CLOSE icursor_pr;  
                DEALLOCATE icursor_pr;  
				DELETE FROM @ThucTreoPRCanTinhNgay;

                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien);	
            END; 	 

    END;

```
