# Stored Procedure: `sp_ThucChay_ExcInsertThucChayDaTinh_PR_HDCT_dev`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-05-24 12:01:15.223000
- **Ngày sửa cuối**: 2024-11-27 14:52:47.610000

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
 exec [dbo].[sp_TC_InsertThucChayDaTinh_PR_HDCT] '2018-10-22','2018-10-22', NULL
 exec [dbo].[sp_ThucChay_ExcInsertThucChayDaTinh_PR_HDCT] '2020-03-12','2020-03-12', 1021680
*/
CREATE PROCEDURE [dbo].[sp_ThucChay_ExcInsertThucChayDaTinh_PR_HDCT_dev]
    @StartDate DATETIME ,
    @EndDate DATETIME ,
    @piHopDongID INT = NULL
AS
    BEGIN

        DECLARE @NgayThucHien DATETIME , @NgayGioiHanTinh_HDCT DATETIME = '2020-01-01'
		
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
	
        WHILE ( @NgayThucHien <= @EndDate )
            BEGIN
				  DELETE FROM @ThucTreoPRCanTinhNgay
                  DECLARE @HopDongREF INT, @HopDongChiTietID INT, @ThucChayHopDongChiTietPRID INT, @DmSanPhamREF INT
                  , @SoLuongThucChay FLOAT, @DonGiaThucChay FLOAT, @ChietKhauThucChay FLOAT, @ThanhTienThucChayTruocCK FLOAT

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
					SELECT tc.ThucChayHopDongChiTietPRID,
                           tc.HopDongREF,
                           tc.ChietKhau,
                           tc.ThucChayHopDongChiTietPrREF,
                           tc.HopDongChiTietREF,
                           tc.DmHinhThucQuangCaoREF,
                           tc.DmSanPhamREF,
                           tc.DmWebsiteREF,
                           tc.GiaTien,
                           tc.SoLuong 
						   FROM
							(
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
									AND ISNULL(HopDongChiTietREF,0) <> 0
									AND RecordStatus = 0
									AND DmHinhThucQuangCaoREF <> 0
									AND DmSanPhamREF <> 0
									AND ThoiGianBatDau >= '2019-01-01'
									AND ( CASE WHEN CreatedAt >= LastModifiedAt THEN CONVERT(DATE, CreatedAt)
												ELSE CONVERT(DATE, LastModifiedAt)
											END ) = @NgayThucHien
									AND ( @piHopDongID IS NULL OR HopDongREF = @piHopDongID )
							)tc INNER JOIN 
							(SELECT * FROM dbo.HopDong hd 
									WHERE hd.TrangThaiHopDong NOT IN (0,3)
									AND hd.NgayDanhSoHopDong >= @NgayGioiHanTinh_HDCT --pp mapping hdct tinh cho hd >=2020
							)hd ON tc.HopDongREF = hd.HopDongID
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
								AND ISNULL(HopDongChiTietREF,0) <> 0
								AND PR.RecordStatus = 0
								AND PR.DmHinhThucQuangCaoREF <> 0
								AND PR.DmSanPhamREF <> 0
								AND PR.ThoiGianBatDau >= '2019-01-01'
								AND PR.CreatedAt < @NgayThucHien
								AND ( @piHopDongID IS NULL OR HopDongREF = @piHopDongID )
							)PR
							INNER JOIN 
							(SELECT * FROM dbo.HopDong hd 
								WHERE hd.NgayDanhSoHopDong >=@NgayGioiHanTinh_HDCT  --pp mapping hdct tinh cho hd >=2020
								AND hd.TrangThaiHopDong NOT IN (0,3)
								AND CONVERT(DATE, hd.LastModifiedAt) = @NgayThucHien
							)hd ON PR.HopDongREF = hd.HopDongID


				-- SELECT HopDongREF, HopDongChiTietREF, ThucChayHopDongChiTietPRID, @DmSanPhamREF, SoLuong, GiaTien, ChietKhau FROM @ThucTreoPRCanTinhNgay

                DECLARE icursor_pr_hdct CURSOR
                FOR
                    SELECT DISTINCT HopDongREF, HopDongChiTietREF, ThucChayHopDongChiTietPRID, DmSanPhamREF, SoLuong, GiaTien, ChietKhau FROM @ThucTreoPRCanTinhNgay

                OPEN icursor_pr_hdct;  

                FETCH NEXT FROM icursor_pr_hdct INTO @HopDongREF, @HopDongChiTietID, @ThucChayHopDongChiTietPRID, @DmSanPhamREF, @SoLuongThucChay, @DonGiaThucChay, @ChietKhauThucChay

                WHILE @@FETCH_STATUS = 0
                    BEGIN  
						DECLARE @ChietKhau_HDCT FLOAT = 0
						, @ThanhTien_HDCT FLOAT = 0

						SELECT TOP (1) @ChietKhau_HDCT = ISNULL(hdct.ChietKhau,0), @ThanhTien_HDCT = ISNULL(hdct.ThanhTien,0) FROM dbo.HopDongChiTiet hdct
						WHERE hdct.HopDongChiTietID = @HopDongChiTietID
						AND hdct.DeletedStatus = 0
						ORDER BY hdct.HopDongChiTietID
						SET @ChietKhau_HDCT = ISNULL(@ChietKhau_HDCT,0)
						SET @ThanhTien_HDCT = ISNULL(@ThanhTien_HDCT,0)

						SET @ThanhTienThucChayTruocCK = 0
						IF NOT((@ChietKhauThucChay = 0 AND @ChietKhau_HDCT = 100) OR (@ChietKhauThucChay = 100 AND @ChietKhau_HDCT = 0))
						BEGIN
							SET @ThanhTienThucChayTruocCK =
										ISNULL([dbo].[ThucChay_GetThanhTienThucChayTruocChietKhau_PR]
							(
								-- Add the parameters for the function here
								@HopDongREF,
								@HopDongChiTietID,
								@ChietKhau_HDCT,
								@ThanhTien_HDCT,
								@SoLuongThucChay,
								@DonGiaThucChay,
								@ChietKhauThucChay
							),0)
							--CHECK DIEU KIEN DE TINH THUC CHAY
							IF(@ThanhTienThucChayTruocCK >0)
							BEGIN
								----TINH THUC CHAY
								--PRINT @HopDongREF
								--PRINT @HopDongChiTietID
								--PRINT @ThucChayHopDongChiTietPRID
								--PRINT @DmSanPhamREF
								--PRINT @NgayThucHien
								DECLARE @ThucChayDaTinhID_op NVARCHAR(100) = ''
								--PRINT 'vao day @ThanhTienThucChayTruocCK'
								--HAIDH COMMENT 2021-05-21
								EXEC [dbo].[ThucChay_InsertThucChayDaTinh_PR_HDCT_op] 
								@HopDongID = @HopDongREF,
								@HopDongChiTietID = @HopDongChiTietID,
								@ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID,
								@DmSanPhamREF = @DmSanPhamREF,
								@NgayThucHien = @NgayThucHien	,
								@ThucChayDaTinhID_output = @ThucChayDaTinhID_op OUTPUT

								--EXEC [dbo].[ThucChay_InsertThucChayDaTinh_PR_HDCT] 
								--@HopDongID = @HopDongREF,
								--@HopDongChiTietID = @HopDongChiTietID,
								--@ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID,
								--@DmSanPhamREF = @DmSanPhamREF,
								--@NgayThucHien = @NgayThucHien

								--CAP NHAP TRANG THAI THUC TREO SAU KHI TINH THUC CHAY
								IF(EXISTS(SELECT TOP (1) tc.ThucChayDaTinhID FROM dbo.ThucChayDaTinh tc
								WHERE tc.ThucChayDaTinhID = @ThucChayDaTinhID_op
								AND tc.HopDongID = @HopDongREF
								AND tc.HopDongChiTietRef = @HopDongChiTietID
								AND tc.DotChayBooking = @ThucChayHopDongChiTietPRID ORDER BY tc.ThucChayDatinhID))
								BEGIN 
									UPDATE  dbo.ThucChayHopDongChiTietPR
									SET     RecordStatus = 1
									WHERE ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID
									AND HopDongREF= @HopDongREF
									AND HopDongChiTietREF = @HopDongChiTietID
									AND DmSanPhamREF = @DmSanPhamREF
								END
								
							END
						END
                       FETCH NEXT FROM icursor_pr_hdct INTO @HopDongREF, @HopDongChiTietID, @ThucChayHopDongChiTietPRID, @DmSanPhamREF, @SoLuongThucChay, @DonGiaThucChay, @ChietKhauThucChay
                    END;   
                CLOSE icursor_pr_hdct;  
                DEALLOCATE icursor_pr_hdct;  
				DELETE FROM @ThucTreoPRCanTinhNgay;

                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien);	
            END; 	 

    END;

```
