# Stored Procedure: `Insert_DoanhSoHaiDauNhanHangCore_PhatSinhGiaTriThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-22 16:42:54.340000
- **Ngày sửa cuối**: 2015-04-22 16:42:54.340000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmMaHopDongREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[Insert_DoanhSoHaiDauNhanHangCore_PhatSinhGiaTriThayDoi]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@HopDongID INT,
	@HopDongChiTietREF INT,
	@DmMaHopDongREF INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	DECLARE @CountNhan INT, @ChiSoSLNhanM BIGINT, @ChiSoTTNhanM BIGINT;
	SET @CountNhan = 0;
	
	DECLARE @IsHopDongNoiBo INT --1: HD Noi Bo, 0: HopDong KHONG la Noi Bo
	SET @IsHopDongNoiBo = 0
	SET @IsHopDongNoiBo = [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](@DmMaHopDongREF, @NgayThucHien)
	DECLARE @CheckHopDongChiTietTcID INT;
	DECLARE @SoLuongNhan INT;
	DECLARE @DsTenNhanHang NVARCHAR(200),@DmListNhanHangREF NVARCHAR(200), @DsTenNganhHang NVARCHAR(500), @DmListNganhHangREF NVARCHAR(500);
	DECLARE @SoHopDong NVARCHAR(200), @TenNhanVien NVARCHAR(200), @DmNhanVienREF INT, @TenPhongBan NVARCHAR(200), @PhongBanREF INT;
	DECLARE @TenBoPhan NVARCHAR(200), @BoPhanREF INT, @TenNhom NVARCHAR(200), @NhomREF INT, @TenKhachHang NVARCHAR(200),@DmKhachHangREF INT;
	DECLARE @TenSanPham NVARCHAR(200), @DmSanPhamREF INT, @TenWebsite NVARCHAR(200), @DmWebsiteREF INT; 
	DECLARE @DonViTinhREF INT, @DonViTinh NVARCHAR(50),@TenDangNhap NVARCHAR(50), @TenNhanHang NVARCHAR(200),@DmNhanHangREF INT ;
	DECLARE @ChietKhau FLOAT, @DonGia FLOAT, @SoLuong BIGINT, @ThanhTien FLOAT,@TrangThaiHopDong INT ;
	DECLARE @NgayDanhSo DATETIME, @NgayKyHopDong DATETIME;
	DECLARE @IsCheckThayDoi INT, @countbefor INT, @countaffter INT ;
    SET @IsCheckThayDoi =0 
   
	--INSERT GIA TRI CHO CAC DOI TUONG BI THAY DOI VE 0
	INSERT INTO DoanhSoHaiDauNhanHangCore
	SELECT 
	@NgayThucHien,
	dsknhc.TenNhanHang,
    dsknhc.DmNhanHangREF,
    dsknhc.DsTenNganhHang,
	dsknhc.DmListNganhHangREF,
	
	dsknhc.HopDongID,
	dsknhc.SoHopDong,
	dsknhc.TenNhanVien,
	dsknhc.DmNhanVienREF,
	dsknhc.TenPhongBan,
	dsknhc.PhongBanREF,
	dsknhc.TenBoPhan,
	dsknhc.BoPhanREF,
	dsknhc.TenNhom,
	dsknhc.NhomREF,
	dsknhc.TenKhachHang,
	dsknhc.DmKhachHangREF,
	dsknhc.HopDongChiTietREF,
	dsknhc.DmSanPhamREF,
	dsknhc.TenSanPham,
	dsknhc.TenWebsite,
	dsknhc.DmWebsiteREF
	 --SoLuongThucThu
	  ,dsknhc.SoLuongPhatSinhCuoiKy AS SoLuongPhatSinhDauKy
	  ,-dsknhc.SoLuongPhatSinhCuoiKy AS SoLuongPhatSinhTrongKy
	  ,0 SoLuongPhatSinhCuoiKy
	  --SoLuongKM
	  ,dsknhc.SoLuongKMPhatSinhCuoiKy AS SoLuongKMPhatSinhDauKy
	  ,- dsknhc.SoLuongKMPhatSinhCuoiKy SoLuongKMPhatSinhTrongKy
	  ,0 SoLuongKMPhatSinhCuoiKy
	  --SoLuongNOIBo
	  ,dsknhc.SoLuongNoiBoPhatSInhCuoiKy SoLuongNoiBoPhatSinhDauKy
	  ,-dsknhc.SoLuongNoiBoPhatSInhCuoiKy SoLuongNoiBoPhatSinhTrongKy
	  ,0 SoLuongNoiBoPhatSInhCuoiKy
	  ,dsknhc.DonViTinhREF
	  ,dsknhc.DonViTinh
	  ,dsknhc.TenDangNhap
	  ,dsknhc.DonGia
	  ,dsknhc.ChietKhau
	  --ThanhTienThucThu
	  ,dsknhc.ThucThuPhatSinhCuoiKy ThucThuPhatSinhDauKy
	  ,- dsknhc.ThucThuPhatSinhCuoiKy ThucThuPhatSinhTrongKy
	  ,0 ThucThuPhatSinhCuoiKy
	  --ThanhTienKM
	  ,dsknhc.KhuyenMaiPhatSinhCuoiKy KhuyenMaiPhatSinhDauKy
	  ,-dsknhc.KhuyenMaiPhatSinhCuoiKy KhuyenMaiPhatSinhTrongKy
	  ,0 KhuyenMaiPhatSinhCuoiKy
	  --ThanhTienNOIBo
	  ,dsknhc.NoiBoPhatSinhCuoiKy NoiBoPhatSinhDauKy
	  ,-dsknhc.NoiBoPhatSinhCuoiKy NoiBoPhatSinhTrongKy
	  ,0 NoiBoPhatSinhCuoiKy
								  
	 , dsknhc.TrangThaiHopDong		
	 , N'Update du lieu thay doi' DienGiai
	 , 'ASD' CreatedBy
	 , GETDATE() CreatedAt
	 , 'ASD' LastModifiedBy
	 , GETDATE() LastModifiedAt
	 , 0 RecordStatus
	 , 0 DeletedStatus
     , 0 PrintStatus
	 , 2 TypeRecordStatus -- 0 La chay du lieu qua khu
	 , dsknhc.NgayDanhSo
	 , dsknhc.NgayKyHopdong
	 , dsknhc.DmListNhanHangREF
	 ,dsknhc.DmMaHopDongREF
	FROM DoanhSoHaiDauNhanHangCore dsknhc 
	WHERE dsknhc.HopDongID = @HopDongID
	AND dsknhc.HopDongChiTietREF = @HopDongChiTietREF
	AND dsknhc.TypeRecordStatus IN (1,3,0)
	AND CONVERT(date,NgayThucHien) <= @NgayThucHien
	AND dsknhc.NgayThucHien = (SELECT MAX(NgayThucHien)FROM DoanhSoHaiDauNhanHangCore WHERE HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietREF)
	ORDER BY NgayThucHien DESC
    -- Insert statements for procedure here
	
		
	SELECT 
		@DsTenNhanHang = hdct.NhanHang,
		@DmListNhanHangREF = hdct.DanhSachNhanHangREF,
		@DsTenNganhHang = hdct.TenNhomNganh,
		@DmListNganhHangREF = hdct.DmNhomNganhREF,
		@SoHopDong = hd.SoHopDong,
		@TenNhanVien = hd.TenNhanVien,
		@DmNhanVienREF = hd.SysNhanVienREF,
		@TenPhongBan = hd.TenPhongBan,
		@PhongBanREF = hd.DmPhongBanREF,
		@TenBoPhan = Hd.TenBoPhan,
		@BoPhanREF = hd.DmBoPhanREF,
		@TenNhom = hd.TenNhom,
		@NhomREF = hd.DmNhomREF,
		@TenKhachHang = hd.TenKhachHang,
		@DmKhachHangREF = hd.DmKhachHangREF,
		@TenSanPham = hdct.TenSanPham,
		@DmSanPhamREF = hdct.DmSanPhamREF,
		@TenWebsite = hdct.TenWebsite,
		@DmWebsiteREF = hdct.DmWebsiteREF,
		@DonViTinhREF = hdct.DonViTinhREF,
		@DonViTinh = hdct.DonViTinh,
		@TenDangNhap = hd.TenDangNhap,
		@ChietKhau = hdct.ChietKhau,
		@DonGia = hdct.DonGia,
		@SoLuong = hdct.SoLuong,
		@ThanhTien = hdct.ThanhTien,
		@TrangThaiHopDong = hd.TrangThaiHopDong,
		@NgayDanhSo = hd.NgayDanhSoHopDong,
		@NgayKyHopDong = hd.NgayKyHopDong
	FROM HopDong hd
		INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		WHERE 1=1
		AND hd.HopDongID = @HopDongID
		AND hdct.HopDongChiTietID = @HopDongChiTietREF
		AND isnull(hd.IsBanCung,0) = 1
		AND hdct.DeletedStatus =0
		AND hd.TrangThaiHopDong <> 3
		--AND hdct.DeletedStatus = 0
		--AND hd.DeletedStatus = 0
		--AND hd.TrangThaiHopDong <> 3
		--AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](hd.DmMaHopDongREF, @NgayThucHien) = 1
	
		   SET @DmNhanHangREF = 0
			SET @TenNhanHang = ''
			SELECT @SoLuongNhan = count(a.DmNhanHang) from
			(
				SELECT distinct dbo.FormatString(item) DmNhanHang
				FROM dbo.ArrayToTable(dbo.Array(@DmListNhanHangREF,','))
			)a
			IF @DmListNhanHangREF ='' SET @SoLuongNhan=0
	IF(@SoLuongNhan >0)
	BEGIN
		    DECLARE Record_cursor2 CURSOR FOR  
		    
			SELECT distinct dbo.FormatString(item) DmNhanHang
			FROM dbo.ArrayToTable(dbo.Array(@DmListNhanHangREF,','))  

			OPEN Record_cursor2   
			FETCH NEXT FROM Record_cursor2 INTO @DmNhanHangREF   

			WHILE @@FETCH_STATUS = 0   
			BEGIN   
				 SET @CountNhan +=1;
				    IF(@CountNhan <> @SoLuongNhan) 
						BEGIN
							IF(@SoLuong <> 0)
								begin
				    				SET @ChiSoSLNhanM =  @SoLuong/@SoLuongNhan
				    				SET @ChiSoTTNhanM = @ChiSoSLNhanM * CAST(@ThanhTien AS BIGINT )/@SoLuong
								END
							ELSE
								BEGIN
									SET @ChiSoSLNhanM =  0
				    				SET @ChiSoTTNhanM = CAST(@ThanhTien AS BIGINT )/@SoLuongNhan
								END
						END
				    
				    ELSE 
				    BEGIN
				    	IF(@SoLuong <> 0)
				    	    begin
				    			SET @ChiSoSLNhanM =  @SoLuong - (@SoLuongNhan-1) * CAST(@SoLuong/@SoLuongNhan AS INT)
				    			SET @ChiSoTTNhanM =  CAST(@ThanhTien AS BIGINT) - (@SoLuongNhan-1) * CAST(@SoLuong/@SoLuongNhan AS INT) * CAST(@ThanhTien AS BIGINT)/@SoLuong
				    	    END
				    	ELSE
				    		BEGIN
				    			SET @ChiSoSLNhanM =  0
				    			SET @ChiSoTTNhanM =  CAST(@ThanhTien AS BIGINT) - (@SoLuongNhan-1)  * CAST(@ThanhTien AS BIGINT)/@SoLuongNhan
				    		END
				   
				    	END 
				   SELECT @TenNhanHang = dnh.TenNhanHang, @DmListNganhHangREF = dnh.DmNghanhHangREF
					  FROM DmNhanHang dnh
					WHERE dnh.DmNhanHangID = @DmNhanHangREF
					SET @TenNhanHang = ISNULL(@TenNhanHang,'')
					SET @DmListNganhHangREF = ISNULL(@DmListNganhHangREF,'')
					
					IF @IsHopDongNoiBo =1
					BEGIN
							--- Insert du lieu vao table DoanhSoHaiDauNhanHangCore
							INSERT INTO DoanhSoHaiDauNhanHangCore
							SELECT @NgayThucHien,
								   @TenNhanHang,
								   @DmNhanHangREF,
								   '' AS DsTenNganhHang,
								   @DmListNganhHangREF,
								   @HopDongID,
								   @SoHopDong,
								   
								   
								   @TenNhanVien,
								   @DmNhanVienREF,
								   @TenPhongBan,
								   @PhongBanREF,
								   @TenBoPhan,
								   @BoPhanREF,
								   @TenNhom,
								   @NhomREF,
								   @TenKhachHang,
								   @DmKhachHangREF,
								   @HopDongChiTietREF,
								   @DmSanPhamREF,
								   @TenSanPham,
								   @TenWebsite,
								   @DmWebsiteREF
								  --SoLuongThucThu
									, 0 SoLuongPhatSinhDauKy
									, 0 SoLuongPhatSinhTrongKy
									, 0 SoLuongPhatSinhCuoiKy
									--SoLuongKM
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE 0 	
										END	
									) SoLuongKMPhatSinhDauKy
									, (
										CASE WHEN @ChietKhau = 100 THEN  @ChiSoSLNhanM
											ELSE 0	END) SoLuongKMPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau = 100 THEN   @ChiSoSLNhanM
											ELSE 0
									  END	) SoLuongKMPhatSinhCuoiKy
									--SoLuongNB
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE 0 	
										END	
									)SoLuongNBPhatSinhDauKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE @ChiSoSLNhanM	END) SoLuongNBPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE   @ChiSoSLNhanM
									  END	) SoLuongNBPhatSinhCuoiKy
									, @DonViTinhREF
									, @DonViTinh
									, @TenDangNhap
									, @DonGia
									, @ChietKhau
									--ThanhtienThucThu
									, 0 ThanhTienPhatSinhDauKy
									, 0 ThanhTienPhatSinhTrongKy
									, 0 ThanhTienPhatSinhCuoiKy
									--ThanhTienKM
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE 0 	
										END	
									) ThanhTienKMPhatSinhDauKy
									, (
										CASE WHEN @ChietKhau = 100 THEN  @ChiSoSLNhanM * @DonGia
											ELSE 0	END) ThanhTienKMPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau = 100 THEN   @ChiSoSLNhanM * @DonGia
											ELSE 0
									  END	) ThanhTienKMPhatSinhCuoiKy
									--THanh tien noi bo
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE 0 	
										END	
									)ThanhTienNBPhatSinhDauKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE @ChiSoTTNhanM	END) ThanhTienNBPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE   @ChiSoTTNhanM
									  END	) ThanhTienNBPhatSinhCuoiKy
									  , @TrangThaiHopDong		
										, N'Chay du lieu thay doi' DienGiai
										, 'ASD' CreatedBy
										, GETDATE() CreatedAt
										, 'ASD' LastModifiedBy
										, GETDATE() LastModifiedAt
										, 0 RecordStatus
										, 0 DeletedStatus
										, 0 PrintStatus
										, 3 TypeRecordStatus -- 0 La chay du lieu qua khu
										,@NgayDanhSo
										,@NgayKyHopDong
										,@DmListNhanHangREF
										,@DmMaHopDongREF
																  
	                    END
	             ELSE
	             	BEGIN
	             		  INSERT INTO DoanhSoHaiDauNhanHangCore
							SELECT @NgayThucHien,
								   @TenNhanHang,
								   @DmNhanHangREF,
								   '' AS DsTenNganhHang,
								   @DmListNganhHangREF,
								   @HopDongID,
								   @SoHopDong,
								   
								   
								   @TenNhanVien,
								   @DmNhanVienREF,
								   @TenPhongBan,
								   @PhongBanREF,
								   @TenBoPhan,
								   @BoPhanREF,
								   @TenNhom,
								   @NhomREF,
								   @TenKhachHang,
								   @DmKhachHangREF,
								   @HopDongChiTietREF,
								   @DmSanPhamREF,
								   @TenSanPham,
								   @TenWebsite,
								   @DmWebsiteREF
								  --SoLuongThucThu
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE 0 	
										END	
									)SoLuongPhatSinhDauKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE @ChiSoSLNhanM	END) SoLuongPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE  @ChiSoSLNhanM
									  END	)SoLuongPhatSinhCuoiKy
									--SoLuongKM
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE 0 	
										END	
									) SoLuongKMPhatSinhDauKy
									, (
										CASE WHEN @ChietKhau = 100 THEN  @ChiSoSLNhanM
											ELSE 0	END) SoLuongKMPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau = 100 THEN   @ChiSoSLNhanM
											ELSE 0
									  END	) SoLuongKMPhatSinhCuoiKy
									--SoLuongNB
									, 0 SoLuongNBPhatSinhDauKy
									, 0 SoLuongNBPhatSinhTrongKy
									, 0 SoLuongNBPhatSinhCuoiKy
									, @DonViTinhREF
									, @DonViTinh
									, @TenDangNhap
									, @DonGia
									, @ChietKhau
									--ThanhtienThucThu
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE 0 	END		)SoLuongPhatSinhDauKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE @ChiSoTTNhanM	END) SoLuongPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau= 100 THEN 0
											ELSE @ChiSoTTNhanM  END	)SoLuongPhatSinhCuoiKy
									--ThanhTienKM
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE 0 	
										END	
									) ThanhTienKMPhatSinhDauKy
									, (
										CASE WHEN @ChietKhau = 100 THEN  @ChiSoSLNhanM * @DonGia
											ELSE 0	END) ThanhTienKMPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau = 100 THEN   @ChiSoSLNhanM * @DonGia
											ELSE 0
									  END	) ThanhTienKMPhatSinhCuoiKy
									--Thanh Tien Noi Bo
									, 0 NoiBoPhatSinhDauKy
									, 0 NoiBoPhatSinhTrongKy
									, 0 NoiBoPhatSinhCuoiKy
									  , @TrangThaiHopDong		
										, N'Chay du lieu thay doi' DienGiai
										, 'ASD' CreatedBy
										, GETDATE() CreatedAt
										, 'ASD' LastModifiedBy
										, GETDATE() LastModifiedAt
										, 0 RecordStatus
										, 0 DeletedStatus
										, 0 PrintStatus
										, 3 TypeRecordStatus -- 0 La chay du lieu qua khu
										,@NgayDanhSo
										,@NgayKyHopDong
										,@DmListNhanHangREF
										,@DmMaHopDongREF
	             	END
				   FETCH NEXT FROM Record_cursor2 INTO @DmNhanHangREF   
			END   

			CLOSE Record_cursor2   
			DEALLOCATE Record_cursor2
	END
	ELSE
		BEGIN
			--- Insert du lieu vao table DoanhSoHaiDauNhanHangCore
			IF @IsHopDongNoiBo =1
			  BEGIN
							INSERT INTO DoanhSoHaiDauNhanHangCore
							SELECT @NgayThucHien,
								   @TenNhanHang,
								   @DmNhanHangREF,
								   '' AS DsTenNganhHang,
								   @DmListNganhHangREF,
								   @HopDongID,
								   @SoHopDong,
								   
								   
								   @TenNhanVien,
								   @DmNhanVienREF,
								   @TenPhongBan,
								   @PhongBanREF,
								   @TenBoPhan,
								   @BoPhanREF,
								   @TenNhom,
								   @NhomREF,
								   @TenKhachHang,
								   @DmKhachHangREF,
								   @HopDongChiTietREF,
								   @DmSanPhamREF,
								   @TenSanPham,
								   @TenWebsite,
								   @DmWebsiteREF
								   --SoLuongThucThu
									, 0 SoLuongPhatSinhDauKy
									, 0 SoLuongPhatSinhTrongKy
									, 0 SoLuongPhatSinhCuoiKy
									--SoLuongKM
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE 0 	
										END	
									) SoLuongKMPhatSinhDauKy
									, (
										CASE WHEN @ChietKhau = 100 THEN  @SoLuong
											ELSE 0	END) SoLuongKMPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau = 100 THEN   @SoLuong
											ELSE 0
									  END	) SoLuongKMPhatSinhCuoiKy
									--SoLuongNB
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE 0 	
										END	
									)SoLuongNBPhatSinhDauKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE @SoLuong	END) SoLuongNBPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE   @SoLuong
									  END	) SoLuongNBPhatSinhCuoiKy
									, @DonViTinhREF
									, @DonViTinh
									, @TenDangNhap
									, @DonGia
									, @ChietKhau
									--ThanhtienThucThu
									, 0 ThanhTienPhatSinhDauKy
									, 0 ThanhTienPhatSinhTrongKy
									, 0 ThanhTienPhatSinhCuoiKy
									--ThanhTienKM
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE 0 	
										END	
									) ThanhTienKMPhatSinhDauKy
									, (
										CASE WHEN @ChietKhau = 100 THEN  @SoLuong * @DonGia
											ELSE 0	END) ThanhTienKMPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau = 100 THEN   @SoLuong * @DonGia
											ELSE 0
									  END	) ThanhTienKMPhatSinhCuoiKy
									--THanh tien noi bo
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE 0 	
										END	
									)ThanhTienNBPhatSinhDauKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE @ThanhTien	END) ThanhTienNBPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE   @ThanhTien
									  END	) ThanhTienNBPhatSinhCuoiKy
									  , @TrangThaiHopDong		
										, N'Chay du lieu thay doi' DienGiai
										, 'ASD' CreatedBy
										, GETDATE() CreatedAt
										, 'ASD' LastModifiedBy
										, GETDATE() LastModifiedAt
										, 0 RecordStatus
										, 0 DeletedStatus
										, 0 PrintStatus
										, 3 TypeRecordStatus -- 0 La chay du lieu qua khu
										,@NgayDanhSo
										,@NgayKyHopDong
										,@DmListNhanHangREF
										,@DmMaHopDongREF
			  END
			  ELSE
			  	BEGIN
			  		     INSERT INTO DoanhSoHaiDauNhanHangCore
							SELECT @NgayThucHien,
								   @TenNhanHang,
								   @DmNhanHangREF,
								   '' AS DsTenNganhHang,
								   @DmListNganhHangREF,
								   @HopDongID,
								   @SoHopDong,
								   
								   
								   @TenNhanVien,
								   @DmNhanVienREF,
								   @TenPhongBan,
								   @PhongBanREF,
								   @TenBoPhan,
								   @BoPhanREF,
								   @TenNhom,
								   @NhomREF,
								   @TenKhachHang,
								   @DmKhachHangREF,
								   @HopDongChiTietREF,
								   @DmSanPhamREF,
								   @TenSanPham,
								   @TenWebsite,
								   @DmWebsiteREF
								  --SoLuongThucThu
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE 0 	
										END	
									)SoLuongPhatSinhDauKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE @SoLuong	END) SoLuongPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE  @SoLuong
									  END	)SoLuongPhatSinhCuoiKy
									--SoLuongKM
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE 0 	
										END	
									) SoLuongKMPhatSinhDauKy
									, (
										CASE WHEN @ChietKhau = 100 THEN  @SoLuong
											ELSE 0	END) SoLuongKMPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau = 100 THEN   @SoLuong
											ELSE 0
									  END	) SoLuongKMPhatSinhCuoiKy
									--SoLuongNB
									, 0 SoLuongNBPhatSinhDauKy
									, 0 SoLuongNBPhatSinhTrongKy
									, 0 SoLuongNBPhatSinhCuoiKy
									, @DonViTinhREF
									, @DonViTinh
									, @TenDangNhap
									, @DonGia
									, @ChietKhau
									--ThanhtienThucThu
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE 0 	END		)SoLuongPhatSinhDauKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE @ThanhTien	END) SoLuongPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau= 100 THEN 0
											ELSE @ThanhTien  END	)SoLuongPhatSinhCuoiKy
									--ThanhTienKM
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE 0 	
										END	
									) ThanhTienKMPhatSinhDauKy
									, (
										CASE WHEN @ChietKhau = 100 THEN  @SoLuong * @DonGia
											ELSE 0	END) ThanhTienKMPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau = 100 THEN   @SoLuong * @DonGia
											ELSE 0
									  END	) ThanhTienKMPhatSinhCuoiKy
									--Thanh Tien Noi Bo
									, 0 NoiBoPhatSinhDauKy
									, 0 NoiBoPhatSinhTrongKy
									, 0 NoiBoPhatSinhCuoiKy
									  , @TrangThaiHopDong		
										, N'Chay du lieu thay doi' DienGiai
										, 'ASD' CreatedBy
										, GETDATE() CreatedAt
										, 'ASD' LastModifiedBy
										, GETDATE() LastModifiedAt
										, 0 RecordStatus
										, 0 DeletedStatus
										, 0 PrintStatus
										, 3 TypeRecordStatus -- 0 La chay du lieu qua khu
										,@NgayDanhSo
										,@NgayKyHopDong
										,@DmListNhanHangREF
										,@DmMaHopDongREF
			  	END

   
		END

END

```
