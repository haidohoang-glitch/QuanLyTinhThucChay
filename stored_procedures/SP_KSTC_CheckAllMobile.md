# Stored Procedure: `KSTC_CheckAllMobile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-08 17:09:25.930000
- **Ngày sửa cuối**: 2014-12-08 17:09:25.930000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE dbo.KSTC_CheckAllMobile 
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
DELETE FROM TableMobile																
DECLARE @HopDongChiTietID INT,																
		@HopDongID INT,														
		@SoHopDong NVARCHAR(50),														
		@DeletedStatus INT,														
		@IsKhuyenMai INT,														
		@ChietKhau FLOAT,														
		@SoLuong FLOAT, @DonViTinh NVARCHAR(50),														
		@ThanhTien INT,@ThanhTienKM INT,														
		@DonGia FLOAT,														
		@SoLuongThucChaySP INT,														
		@TienThucChayTuTinh FLOAT, 														
		@ThucChayKhuyenMai FLOAT, 														
		@ThanhTienThucChay2013 FLOAT, 														
		@ThucChayKhuyenMai2013 FLOAT,														
		@ThucChayThucTe FLOAT,														
		@KhuyenMaiThucTe FLOAT,																											
		@DonGiaTheoDonVi FLOAT,														
		@ProductUnitName Varchar(10), @tc INT, @tv INT, @count INT														
																
																
DECLARE @TongClick INT, @TongView INT																
															
DECLARE vendor_cursor CURSOR FOR 																
	SELECT HopDongChiTietID,HopDongFK, dbo.GetSoHopDongByID(HopDongFK)SoHopDong,hdct.DeletedStatus,hdct.IsKhuyenMai,hdct.ChietKhau,hdct.SoLuong,DonViTinh,hdct.ThanhTien,DonGia															
	  FROM HopDongChiTiet hdct															
	WHERE hdct.DmSanPhamREF = 342															
	AND hdct.HopDongChiTietID IN (SELECT tcmt.HopDongChiTietREF															
	                                FROM ThucChay tcmt WHERE tcmt.TypeProduct = 10)																													
																
	ORDER BY HopDongChiTietID															
																
OPEN vendor_cursor																
																
FETCH NEXT FROM vendor_cursor INTO @HopDongChiTietID,@HopDongID,@SoHopDong,@DeletedStatus,@IsKhuyenMai,@ChietKhau,@SoLuong,@DonViTinh,@ThanhTien,@DonGia																
																
WHILE @@FETCH_STATUS = 0																
BEGIN																
	PRINT CONVERT(NVARCHAR(10),@HopDongChiTietID)															
	SET @ThanhTienKM = (SELECT DonGia*SoLuong FROM HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = @HopDongChiTietID )															
	SET @ThanhTienKM = ISNULL(@ThanhTienKM,0) 															
																
	SET @ThucChayKhuyenMai2013 = (SELECT SUM(ThanhTienKM)															
	                                  FROM ThucChayDaTinhMobile WHERE HopDongChiTietREF = @HopDongChiTietID AND YEAR(NgayThucHien) = 2013)															
																
	SET @ThanhTienThucChay2013 = (SELECT SUM(ThanhTienSauTrietKhauThucChay+ GiaTriThayDoi)															
	                                  FROM ThucChayDaTinhMobile WHERE HopDongChiTietREF = @HopDongChiTietID AND YEAR(NgayThucHien) = 2013) 															
	SET @ThucChayKhuyenMai2013 = ISNULL(@ThucChayKhuyenMai2013,0)															
	SET @ThanhTienThucChay2013 = ISNULL(@ThanhTienThucChay2013,0)															
																
	SET @ThucChayKhuyenMai = 0															
	SET @TienThucChayTuTinh = 0															
	SET @TongClick = 0															
	SET @TongView = 0															
	SET @count = 0															
	 															
	IF @DeletedStatus = 1															
		BEGIN														
			SET @TienThucChayTuTinh = 0													
			SET @ThucChayKhuyenMai = 0													
		END														
	ELSE 															
	BEGIN			 												
			SELECT @TongClick  = SUM(tcmt.TongClickThucChay),													
				   @TongView   = SUM(tcmt.TongViewThucChay)												
			FROM ThucChay tcmt 													
			WHERE tcmt.HopDongChiTietREF = @HopDongChiTietID													
				AND tcmt.TypeProduct = 10												
				AND tcmt.NgayThucHien <=@NgayThucHien												
																
			IF (@DonViTinh = 'CPC' and @IsKhuyenMai = 0) 													
				SET @TienThucChayTuTinh = @TongClick * @DonGia * (100 - @ChietKhau)/100												
												 				
			else IF (@DonViTinh = 'CPM' and @IsKhuyenMai = 0) 													
				SET @TienThucChayTuTinh = @TongView * @DonGia/1000 * (100 - @ChietKhau)/100												
																
			ELSE IF (@DonViTinh = 'CPC' and @IsKhuyenMai = 1)													
				 SET @ThucChayKhuyenMai = @TongClick * @DonGia												
				 												
			ELSE IF (@DonViTinh = 'CPM' and @IsKhuyenMai = 1)													
				SET @ThucChayKhuyenMai =  @TongView * @DonGia/1000												
																
			ELSE IF (@DonViTinh NOT IN ('CPC','CPV','CPM'))													
				BEGIN												
																
																
					SELECT @count = count(distinct tcmt.ProductUnitName) 											
					 FROM ThucChay tcmt											
					WHERE tcmt.TypeProduct =10 											
						AND tcmt.HopDongChiTietREF = @HopDongChiTietID										
						AND tcmt.NgayThucHien <=@NgayThucHien										
					SET @ProductUnitName = (SELECT TOP 1 tcmt.ProductUnitName 											
					                        FROM ThucChay tcmt											
					 WHERE tcmt.HopDongChiTietREF = @HopDongChiTietID											
						AND tcmt.NgayThucHien <=@NgayThucHien )										
																
																
																
					SET @DonGiaTheoDonVi = (SELECT CASE WHEN @ProductUnitName = 'CPC' THEN AVG(dbo.ThucChay_GetDonGiaTheoDonViTruocChietKhau(HopDongChiTietREF,ProductUnitName,BannerType,@NgayThucHien))											
										ELSE AVG(dbo.ThucChay_GetDonGiaTheoDonViTruocChietKhau(HopDongChiTietREF,ProductUnitName,BannerType,@NgayThucHien))						
										END		 				
				                       FROM ThucChay tcmt 												
					                        WHERE tcmt.TypeProduct = 10 											
									   and tcmt.HopDongChiTietREF = @HopDongChiTietID							
									   AND tcmt.NgayThucHien  <= @NgayThucHien)							
																
					IF @count = 1											
					BEGIN											
						--PRINT CONVERT(NVARCHAR(10),@DonGiaTheoDonVi)										
																
						IF @IsKhuyenMai = 0 										
							BEGIN									
								set @TienThucChayTuTinh = 								
								(SELECT CASE WHEN @ProductUnitName = 'CPC' THEN 								
									sum(TongClickThucChay*@DonGiaTheoDonVi*(100-@ChietKhau)/100)							
								 ELSE 								
								 	sum(TongViewThucChay*@DonGiaTheoDonVi*(100-@ChietKhau)/100)							
								 END								
								 								
								 FROM ThucChay tcmt 								
								 WHERE tcmt.TypeProduct =10								
								 AND tcmt.HopDongChiTietREF = @HopDongChiTietID								
								 AND tcmt.NgayThucHien  <= @NgayThucHien								
								)								
								SET @ThucChayKhuyenMai = 0								
							END 									
						ELSE 										
							BEGIN									
								set @TienThucChayTuTinh = 0								
								SET @ThucChayKhuyenMai = (SELECT CASE WHEN @ProductUnitName = 'CPC' THEN sum(TongClickThucChay*dbo.ThucChay_GetDonGiaTheoDonViTruocChietKhau(HopDongChiTietREF,ProductUnitName,BannerType,@NgayThucHien))								
																ELSE sum(TongViewThucChay*dbo.ThucChay_GetDonGiaTheoDonViTruocChietKhau(HopDongChiTietREF,ProductUnitName,BannerType,@NgayThucHien))
																end
								                           FROM ThucChay tcmt 								
								                          WHERE tcmt.TypeProduct =10								
								                           AND tcmt.HopDongChiTietREF = @HopDongChiTietID								
								                           AND tcmt.NgayThucHien  <= @NgayThucHien								
															)	
							END 									
					END											
				END												
				--PRINT CONVERT(NVARCHAR(10),@TienThucChayTuTinh) 												
																
				--Insert vào bảng tạm											
					IF (@ThanhTienThucChay2013 + @TienThucChayTuTinh) > @ThanhTien 											
						SET @TienThucChayTuTinh = ISNULL(@ThanhTien,0)										
					ELSE											
						SET @TienThucChayTuTinh = @ThanhTienThucChay2013 + ISNULL(@TienThucChayTuTinh,0)										
																
					IF  (@ThucChayKhuyenMai2013 + @ThucChayKhuyenMai) > @ThanhTienKM 											
						SET @ThucChayKhuyenMai = ISNULL(@ThanhTienKM,0)										
					ELSE											
						SET @ThucChayKhuyenMai = @ThucChayKhuyenMai2013 + ISNULL(@ThucChayKhuyenMai,0)										
																
				 IF @DonViTinh IN ('CPC','CPV') 												
					BEGIN											
						SET @DonGiaTheoDonVi = @DonGia										
						SET @ProductUnitName = @DonViTinh										
					END											
																
				ELSE IF @DonViTinh IN ('CPM')												
					BEGIN											
						SET @DonGiaTheoDonVi = @DonGia/1000										
						SET @ProductUnitName = @DonViTinh										
					END											
				ELSE 												
					BEGIN											
						SET @DonGiaTheoDonVi = @DonGiaTheoDonVi										
						SET @ProductUnitName = @ProductUnitName										
					END											
																
				SELECT @ThucChayThucTe = SUM(tcdtm.ThanhTienSauTrietKhauThucChay + tcdtm.GiaTriThayDoi)												
				                                      FROM ThucChayDaTinhMobile tcdtm 												
				WHERE tcdtm.HopDongChiTietREF = @HopDongChiTietID 												
				AND tcdtm.NgayThucHien <=@NgayThucHien  												
																
				SELECT @KhuyenMaiThucTe = SUM(tcdtm.ThanhTienKM + tcdtm.GiaTriKMThayDoi)												
				                                      FROM ThucChayDaTinhMobile tcdtm 												
				WHERE tcdtm.HopDongChiTietREF = @HopDongChiTietID 												
				AND tcdtm.NgayThucHien <=@NgayThucHien  												
																
					 INSERT INTO TableMobile SELECT @HopDongChiTietID, @HopDongID , 											
					 @SoHopDong ,@DeletedStatus ,@IsKhuyenMai ,@ChietKhau ,											
					 @SoLuong ,@DonViTinh ,@ProductUnitName ,@DonGia ,@DonGiaTheoDonVi,@TongClick , @TongView ,@ThanhTien ,											
					 @ThanhTienThucChay2013, @TienThucChayTuTinh, @ThucChayKhuyenMai, @ThucChayThucTe, @KhuyenMaiThucTe				 							
		END					        									
    FETCH NEXT FROM vendor_cursor INTO @HopDongChiTietID,@HopDongID,@SoHopDong,@DeletedStatus,@IsKhuyenMai,@ChietKhau,@SoLuong,@DonViTinh,@ThanhTien,@DonGia																
END 																
CLOSE vendor_cursor;																
DEALLOCATE vendor_cursor;																
/*																
--CPC																
SELECT * FROM TableMobile WHERE IsKhuyenMai = 0 AND DonViTinh IN ('CPC')																
--CPM																
SELECT * FROM TableMobile WHERE IsKhuyenMai = 0 AND DonViTinh IN ('CPM')																
--#CPC																
SELECT * FROM TableMobile WHERE IsKhuyenMai = 0 AND DonViTinh NOT IN ('CPC','CPM','CPV') AND ProductUnitName IN ('CPC')																
--#CPM																
SELECT * FROM TableMobile WHERE IsKhuyenMai = 0 AND DonViTinh NOT IN ('CPC','CPM','CPV') AND ProductUnitName IN ('CPM')																
--KM																
SELECT * FROM TableMobile WHERE IsKhuyenMai = 1 and DonViTinh in ('CPC')																
SELECT * FROM TableMobile WHERE IsKhuyenMai = 1 and DonViTinh in ('CPM')																
SELECT * FROM TableMobile WHERE IsKhuyenMai = 1 and DonViTinh not in ('CPC','CPM','CPV')																
*/																

END

```
