# Stored Procedure: `KSTC_GoogleFacebook_thoigian`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-08 10:00:23.023000
- **Ngày sửa cuối**: 2015-04-08 10:00:23.023000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@TaiKhoan` | `nvarchar(100)` | No |
| `@SoNgayChay` | `int(4)` | No |
| `@Type` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[KSTC_GoogleFacebook_thoigian] 
	-- Add the parameters for the stored procedure here
	@DmSanPhamREF INT, 
	@TenSanPham NVARCHAR(50), 
	@TaiKhoan NVARCHAR(50), 
	@SoNgayChay INT, 
	@Type NVARCHAR(50), 
	@NgayThucHien DATETIME
	
AS
BEGIN
	--Chu y: 1 tuan = 7 ngay, 1 thang = 30 ngay
	
	--Neu co truong hop vuot hop dong do 1 thang co 31 ngay thi check lai voi anh Binh
	DECLARE @SoNgayThucChayOnline FLOAT, @SoNgayThucChayDaTinh FLOAT,@GhiChu NVARCHAR(200)
	--Loai cam ket thoi gian co truong hop khuyen mai	
	--kiem tra so tong (TCDT + vi online = TC)
	--1.So ngay chay online
	set @SoNgayThucChayOnline  = ISNULL((select SUM(SoNgayChay) from ThucChayGoogleFacebookOnline 
						WHERE DmSanPhamREF = @DmSanPhamREF
						AND TaiKhoan = @TaiKhoan
						AND [Type] = @Type
						AND NgayThucHien = @NgayThucHien),0)
						     
     --2.Tien thuc chay da tinh
     set @SoNgayThucChayDaTinh = ISNULL((SELECT SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi + tcdt.SoLuongThucChayKM + tcdt.SoLuongKMThayDoi)
            FROM ThucChayDaTinh tcdt 
     WHERE tcdt.NgayThucHien = @NgayThucHien
     AND tcdt.HopDongChiTietREF IN (					
				     SELECT HopDongChiTietID FROM HopDongChiTiet hdct 
					 WHERE hdct.DeletedStatus <> 1	
					 AND hdct.HopDongFK IN (SELECT HopDongID FROM HopDong WHERE TrangThaiHopDong <> 3)
					 AND @TaiKhoan IN (SELECT dbo.FormatString(item) FROM dbo.ArrayToTable(dbo.Array(hdct.TK_Admarket,',')))
					 AND hdct.HopDongFK IN (SELECT HopDongFK FROM HopDongChiTiet hdct 
							 WHERE hdct.DmSanPhamREF = @DmSanPhamREF
							 AND hdct.DonViTinh IN (N'Tháng',N'Tuần',N'Ngày')
							 AND hdct.DeletedStatus <> 1)	
					 )		
	AND tcdt.DonViTinh IN (N'Ngày')		
	),0)
	IF @SoNgayChay <> (@SoNgayThucChayOnline + @SoNgayThucChayDaTinh)
		SET @GhiChu = 'So ngay tong sai'
	ELSE
		set @GhiChu = 'So ngay tong dung'
	
	Insert into #temp 
		SELECT 
		@DmSanPhamREF, 
		@TenSanPham , 
		@TaiKhoan, 
		@Type, 
		@NgayThucHien,
		@GhiChu 	
	/*
	DECLARE @HopDongChiTietID INT, @DmSanPhamREFHD INT, @IsKhuyenMai INT, 
			@ChietKhau INT, @SoLuong INT, @DonGia INT, @DonViTinh NVARCHAR(50),@ThanhTienHD FLOAT;
	Declare @ThanhTienTCDT FLOAT, @DonGiaNgay FLOAT, @TienThucChayNgay float; 
	
	DECLARE @Table TABLE 
	(HopDongChiTietID INT,
	 NgayThucHien DATETIME,
	 TienThucChayDaTinh FLOAT)
	 
	SET @DonGiaNgay = (SELECT CASE WHEN @DonViTinh = N'Ngày' THEN @DonGia/@SoLuong
	    								   WHEN @DonViTinh = N'Tuần' THEN @DonGia/(@SoLuong*7)
	    								   WHEN @DonViTinh = N'Tháng' THEN @DonGia/(@SoLuong*30)
	    								   WHEN @DonViTinh = N'Năm' THEN @DonGia/(@SoLuong*360)
	    						END
	    	                   )
	SET @TienThucChayNgay = @DonGiaNgay*@SoNgayChay
	    	 
			
	DECLARE vendor_cursor CURSOR FOR 
		SELECT hdct.HopDongChiTietID, hdct.DmSanPhamREF, hdct.IsKhuyenMai, 
			hdct.ChietKhau, hdct.SoLuong, hdct.DonGia, hdct.DonViTinh, hdct.ThanhTien 
			FROM HopDong hd
			INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
			WHERE-- hdct.TK_AdMarket = 'Herbalife HCM'--@TaiKhoan
			--AND hdct.DmSanPhamREF = 423--@DmSanPhamREF
			
			 hdct.DonViTinh IN (N'Ngày',N'Tuần',N'Tháng',N'Năm')
			AND hdct.DeletedStatus <> 1
			AND hd.TrangThaiHopDong <> 3
			ORDER BY hdct.HopDongChiTietID

	OPEN vendor_cursor

	FETCH NEXT FROM vendor_cursor 
	INTO @HopDongChiTietID, @DmSanPhamREFHD, @IsKhuyenMai, @ChietKhau, @SoLuong, @DonGia, @DonViTinh,@ThanhTienHD

	WHILE @@FETCH_STATUS = 0
	BEGIN
	    SET @ThanhTienTCDT = (SELECT CASE WHEN (@IsKhuyenMai = 0 OR @ChietKhau = 100) THEN SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)
											  ELSE SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi)
											  END
		                          FROM ThucChayDaTinh tcdt
		                          WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID AND tcdt.NgayThucHien < @NgayThucHien)
		SET @ThanhTienHD = (SELECT CASE WHEN (@IsKhuyenMai = 0 OR @ChietKhau = 100) THEN @ThanhTienHD
								ELSE @SoLuong * @DonGia
								END)                      		
	    IF @ThanhTienTCDT < @ThanhTienHD
	    BEGIN
	    	IF @TienThucChayNgay < (@ThanhTienHD - @ThanhTienTCDT)
	    		BEGIN
	    			SET  @TienThucChayNgay = @TienThucChayNgay
	    			INSERT INTO @Table SELECT @HopDongChiTietID, @NgayThucHien, @TienThucChayNgay	
	    		END
	    	ELSE IF @TienThucChayNgay >= (@ThanhTienHD - @ThanhTienTCDT)
	    		BEGIN
	    			INSERT INTO @Table SELECT @HopDongChiTietID, @NgayThucHien, (@ThanhTienHD - @ThanhTienTCDT)
	    			SET @TienThucChayNgay = @TienThucChayNgay - (@ThanhTienHD - @ThanhTienTCDT)
	    		END
	    		 
	    END
	    ELSE IF @ThanhTienTCDT = @ThanhTienHD
	    	PRINT 'Bang hop dong'
	    ELSE
	    	PRINT 'Vuot hop dong'
		FETCH NEXT FROM vendor_cursor 
		INTO @HopDongChiTietID, @DmSanPhamREFHD, @IsKhuyenMai, @ChietKhau, @SoLuong, @DonGia, @DonViTinh,@ThanhTienHD
	END 
	CLOSE vendor_cursor;
	DEALLOCATE vendor_cursor;				  
		*/	
END

```
