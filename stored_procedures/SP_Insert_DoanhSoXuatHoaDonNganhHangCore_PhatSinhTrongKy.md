# Stored Procedure: `Insert_DoanhSoXuatHoaDonNganhHangCore_PhatSinhTrongKy`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-12 10:47:02.820000
- **Ngày sửa cuối**: 2015-06-12 10:47:02.820000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmMaHopDongREF` | `int(4)` | No |
| `@ThongTinHoaDonID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[Insert_DoanhSoXuatHoaDonNganhHangCore_PhatSinhTrongKy]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@HopDongID INT,
	@HopDongChiTietREF INT,
	@DmMaHopDongREF INT,
	@ThongTinHoaDonID INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	DECLARE @CountNhan INT, @ChiSoSLNhanM BIGINT, @ChiSoTTNhanM BIGINT;
	SET @CountNhan = 0;
	DECLARE @ThanhTienHoaDon FLOAT;
	DECLARE @IsHopDongNoiBo INT --1: HD Noi Bo, 0: HopDong KHONG la Noi Bo
	SET @IsHopDongNoiBo = 0
	SET @IsHopDongNoiBo = [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](@DmMaHopDongREF, @NgayThucHien)
	DECLARE @CheckHopDongChiTietTcID INT;
	DECLARE @SoLuongNhan INT;
	DECLARE @DsTenNganhHang NVARCHAR(500), @DmListNganhHangREF NVARCHAR(500);
	DECLARE @SoHopDong NVARCHAR(200), @TenNhanVien NVARCHAR(200), @DmNhanVienREF INT, @TenPhongBan NVARCHAR(200), @PhongBanREF INT;
	DECLARE @TenBoPhan NVARCHAR(200), @BoPhanREF INT, @TenNhom NVARCHAR(200), @NhomREF INT, @TenKhachHang NVARCHAR(200),@DmKhachHangREF INT;
	DECLARE @TenSanPham NVARCHAR(200), @DmSanPhamREF INT, @TenWebsite NVARCHAR(200), @DmWebsiteREF INT; 
	DECLARE @DonViTinhREF INT, @DonViTinh NVARCHAR(50),@TenDangNhap NVARCHAR(50), @TenNganhHang NVARCHAR(200),@DmNganhHangREF INT ;
	DECLARE @ChietKhau FLOAT, @DonGia FLOAT, @SoLuong BIGINT, @ThanhTien FLOAT,@TrangThaiHopDong INT ;
	DECLARE @NgayDanhSo DATETIME, @NgayKyHopDong DATETIME, @SoHoaDon NVARCHAR(50), @NgayXuatHoaDon DATETIME;
    -- Insert statements for procedure here
	--DELETE FROM DoanhSoXuatHoaDonNganhHangCore WHERE HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietREF AND ThongTinHoaDonREF = @ThongTinHoaDonID
	SELECT 
		@DsTenNganhHang = hdct.TenNhomNganh,
		@DmListNganhHangREF = hdct.DmNhomNganhREF,
		@SoHopDong = hd.SoHopDong,
		@NgayDanhSo = hd.NgayDanhSoHopDong,
		@NgayKyHopDong = hd.NgayKyHopDong,
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
		@SoHoaDon = tthd.SoHoaDon,
		@NgayXuatHoaDon = tthd.NgayXuatHoaDon,
		@ThongTinHoaDonID = tthd.ThongTinHoaDonID
	FROM HopDong hd
		INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		INNER JOIN ThongTinHoaDon tthd ON tthd.HopDongREF = hd.HopDongID
		WHERE 1=1
		AND hd.HopDongID = @HopDongID
			AND hdct.HopDongChiTietID = @HopDongChiTietREF
			AND tthd.ThongTinHoaDonID = @ThongTinHoaDonID
			AND Hd.TrangThaiHopDong <>3
			AND hdct.DeletedStatus =0
			AND tthd.DeletedStatus =0
					AND (SELECT SUM(ThanhTien) FROM HopDongChiTiet hdct2 WHERE hdct2.HopDongFK = hd.HopDongID) > 0
			AND hd.GiaTriHopDong > 0
			AND hdct.ChietKhau <> 100
		--AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](hd.DmMaHopDongREF, @NgayThucHien) = 1
			SET @ThanhTienHoaDon = (SELECT [dbo].[fn_GetThanhTienByNgay_DoanhSoXuatHoaDonCore] 
					(
						@NgayThucHien,
						@HopDongID,
						@ThongTinHoaDonID,
						@ThanhTien
					))
		    SET @DmNganhHangREF = 0
			SET @TenNganhHang = ''
			SELECT @SoLuongNhan = count(a.DmNhanHang) from
			(
				SELECT distinct dbo.FormatString(item) DmNhanHang
				FROM dbo.ArrayToTable(dbo.Array(@DmListNganhHangREF,','))
			)a
			IF  @DmListNganhHangREF = '' SET @SoLuongNhan =0
	IF(@SoLuongNhan >0)
	BEGIN
		    DECLARE Record_cursor2 CURSOR FOR  
		    
			SELECT distinct dbo.FormatString(item) DmNhanHang
			FROM dbo.ArrayToTable(dbo.Array(@DmListNganhHangREF,','))  
			OPEN Record_cursor2   
			FETCH NEXT FROM Record_cursor2 INTO @DmNganhHangREF   

			WHILE @@FETCH_STATUS = 0   
			BEGIN   
				 SET @CountNhan +=1;
				    IF(@CountNhan <> @SoLuongNhan) 
						BEGIN
							IF(@SoLuong <> 0)
								begin
				    				SET @ChiSoSLNhanM =  @SoLuong/@SoLuongNhan
				    				SET @ChiSoTTNhanM = @ChiSoSLNhanM * CAST(@ThanhTienHoaDon AS BIGINT )/@SoLuong
								END
							ELSE
								BEGIN
									SET @ChiSoSLNhanM =  0
				    				SET @ChiSoTTNhanM = CAST(@ThanhTienHoaDon AS BIGINT )/@SoLuongNhan
								END
						END
				    
				    ELSE 
				    BEGIN
				    	IF(@SoLuong <> 0)
				    	    begin
				    			SET @ChiSoSLNhanM =  @SoLuong - (@SoLuongNhan-1) * CAST(@SoLuong/@SoLuongNhan AS INT)
				    			SET @ChiSoTTNhanM =  CAST(@ThanhTienHoaDon AS BIGINT) - (@SoLuongNhan-1) * CAST(@SoLuong/@SoLuongNhan AS INT) * CAST(@ThanhTienHoaDon AS BIGINT)/@SoLuong
				    	    END
				    	ELSE
				    		BEGIN
				    			SET @ChiSoSLNhanM =  0
				    			SET @ChiSoTTNhanM =  CAST(@ThanhTienHoaDon AS BIGINT) - (@SoLuongNhan-1)  * CAST(@ThanhTienHoaDon AS BIGINT)/@SoLuongNhan
				    		END
				   
				    	END 
				    SELECT @TenNganhHang = dnh.TenNghanhHang
					FROM DmNghanhHang dnh
					WHERE dnh.DmNghanhHangID = @DmNganhHangREF
					SET @TenNganhHang = ISNULL(@TenNganhHang,'')
					
					IF @IsHopDongNoiBo =1
					BEGIN
							--- Insert du lieu vao table DoanhSoXuatHoaDonNganhHangCore
							INSERT INTO DoanhSoXuatHoaDonNganhHangCore
							SELECT * FROM 
							(
							SELECT @NgayThucHien AS NgayThucHien,
								   @TenNganhHang AS TenNganhHang,
								   @DmNganhHangREF AS DmNganhHangREF,
								   @HopDongID AS HopDongID,
								   @SoHopDong AS SoHopDong,
								   @NgayDanhSo AS NgayDanhSo,
								   @NgayKyHopDong AS NgayKyHopDong,
								   @TenNhanVien AS TenNhanVien,
								   @DmNhanVienREF AS DmNhanVienREF,
								   @TenPhongBan AS TenPhongBan,
								   @PhongBanREF AS PhongBanREF,
								   @TenBoPhan AS TenBoPhan,
								   @BoPhanREF AS BoPhanREF,
								   @TenNhom AS TenNhom,
								   @NhomREF AS NhomREF,
								   @TenKhachHang AS TenKhachHang,
								   @DmKhachHangREF AS DmKhachHangREF,
								   @HopDongChiTietREF AS HopDongChiTietREF,
								   @DmSanPhamREF AS DmSanPham,
								   @TenSanPham AS TenSanPham,
								   @TenWebsite AS TenWebsite,
								   @DmWebsiteREF AS DmWebsiteREF
								   --SoLuongThucThu
									, 0 SoLuongPhatSinhDauKy
									, 0 SoLuongPhatSinhTrongKy
									, 0 SoLuongPhatSinhCuoiKy
									--SoLuongKM
									, 0 SoLuongKMPhatSinhDauKy
									, 0 SoLuongKMPhatSinhTrongKy
									, 0 SoLuongKMPhatSinhCuoiKy
											
									--SoLuongNB
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE 0
										END	
									) SoLuongNoiBoPhatSinhDauKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE @ChiSoSLNhanM 

											END
									) SoLuongNoiBoPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE  @ChiSoSLNhanM
									  END	
									) SoLuongNoiBoPhatSinhCuoiKy
									, @DonViTinhREF AS DonViTinhREF
									, @DonViTinh AS DonViTinh
									, @TenDangNhap AS TenDangNhap
									, @DonGia AS DonGia
									, @ChietKhau AS ChietKhau
									--ThanhtienThucThu
									, 0 ThanhTienPhatSinhDauKy
									, 0 ThanhTienPhatSinhTrongKy
									, 0 ThanhTienPhatSinhCuoiKy
									--ThanhTienKM
									, 0 ThanhTienKMPhatSinhDauKy
									, 0 ThanhTienKMPhatSinhTrongKy
									, 0 ThanhTienKMPhatSinhCuoiKy
									--Thanh tien noi bo
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE 0
										END	
									)ThanhTienNBPhatSinhDauKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE @ChiSoTTNhanM 
											END) ThanhTienNBPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE   @ChiSoTTNhanM
									  END	) ThanhTienNBPhatSinhCuoiKy
									  , @TrangThaiHopDong	AS TrangThaiHopDong	
										, N'Chay du lieu phat sinh' DienGiai
										, 'ASD' CreatedBy
										, GETDATE() CreatedAt
										, 'ASD' LastModifiedBy
										, GETDATE() LastModifiedAt
										, 0 RecordStatus
										, 0 DeletedStatus
										, 0 PrintStatus
										, 1 TypeRecordStatus -- 0 La chay du lieu qua khu
										,@SoHoaDon AS SoHoaDon
										,@NgayXuatHoaDon AS NgayXuatHD
										,@ThongTinHoaDonID AS TTHDID
										, @DmListNganhHangREF AS dmlistnganhhangref
										, @DmMaHopDongREF AS DmmaHD
							) A
							WHERE (A.SoLuongPhatSinhTrongKy <> 0 OR A.SoLuongKMPhatSinhTrongKy <>0 
							OR A.ThanhTienPhatSinhTrongKy<> 0 OR A.ThanhTienKMPhatSinhTrongKy <> 0) 	
																  
	                    END
	             ELSE
	             	BEGIN
	             		  INSERT INTO DoanhSoXuatHoaDonNganhHangCore
	             		  SELECT * FROM 
	             		  (
							SELECT @NgayThucHien AS NgayThucHien,
								   @TenNganhHang AS TenNganhHang,
								   @DmNganhHangREF AS DmNganhHangREF,
								   @HopDongID AS HopDongID,
								   @SoHopDong AS SoHopDong,
								   @NgayDanhSo AS NgayDanhSo,
								   @NgayKyHopDong AS NgayKyHopDong,
								   @TenNhanVien AS TenNhanVien,
								   @DmNhanVienREF AS DmNhanVienREF,
								   @TenPhongBan AS TenPhongBan,
								   @PhongBanREF AS PhongBanREF,
								   @TenBoPhan AS TenBoPhan,
								   @BoPhanREF AS BoPhanREF,
								   @TenNhom AS TenNhom,
								   @NhomREF AS NhomREF,
								   @TenKhachHang AS TenKhachHang,
								   @DmKhachHangREF AS DmKhachHangREF,
								   @HopDongChiTietREF AS HopDongChiTietREF,
								   @DmSanPhamREF AS DmSanPham,
								   @TenSanPham AS TenSanPham,
								   @TenWebsite AS TenWebsite,
								   @DmWebsiteREF AS DmWebsiteREF
								     --SoLuongThucThu
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
										else 0
										END	
									) SoLuongPhatSinhDauKy
									,(
										CASE WHEN @ChietKhau = 100 THEN 0 
										else @ChiSoSLNhanM 
											END
									) SoLuongPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
										else @ChiSoSLNhanM

									  END	
									) SoLuongPhatSinhCuoiKy
									--SoLuongKM
									, 0 SoLuongKMPhatSinhDauKy
									, 0 SoLuongKMPhatSinhTrongKy
									, 0 SoLuongKMPhatSinhCuoiKy
											
									--SoLuongNB
									, 0 SoLuongNoiBoPhatSinhDauKy
									, 0 SoLuongNoiBoPhatSinhTrongKy
									, 0 SoLuongNoiBoPhatSinhCuoiKy
									, @DonViTinhREF AS DonViTinhREF
									, @DonViTinh AS DonViTinh
									, @TenDangNhap AS tendangNhap
									, @DonGia AS DonGia
									, @ChietKhau AS ChietKhau
									--ThanhtienThucThu
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE 0
										END	
									)ThanhTienPhatSinhDauKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE @ChiSoTTNhanM 
											END) ThanhTienPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE   @ChiSoTTNhanM
									  END	) ThanhTienPhatSinhCuoiKy
									--ThanhTienKM
									, 0 ThanhTienKMPhatSinhDauKy
									, 0 ThanhTienKMPhatSinhTrongKy
									, 0 ThanhTienKMPhatSinhCuoiKy
									--Thanh tien noi bo
									, 0 ThanhTienNBPhatSinhDauKy
									, 0 ThanhTienNBPhatSinhTrongKy
									, 0 ThanhTienNBPhatSinhCuoiKy
									  , @TrangThaiHopDong	 AS TrangThaiHD	
										, N'Chay du lieu phat sinh' DienGiai
										, 'ASD' CreatedBy
										, GETDATE() CreatedAt
										, 'ASD' LastModifiedBy
										, GETDATE() LastModifiedAt
										, 0 RecordStatus
										, 0 DeletedStatus
										, 0 PrintStatus
										, 1 TypeRecordStatus -- 0 La chay du lieu qua khu
										,@SoHoaDon AS SoHoaDon
										,@NgayXuatHoaDon AS NgayXuatHD
										,@ThongTinHoaDonID AS TTHDID
										, @DmListNganhHangREF AS dmlistnganhhangref
										, @DmMaHopDongREF AS DmmaHD
	             		  ) A
	             		  WHERE (A.SoLuongPhatSinhTrongKy <> 0 OR A.SoLuongKMPhatSinhTrongKy <>0 
							OR A.ThanhTienPhatSinhTrongKy<> 0 OR A.ThanhTienKMPhatSinhTrongKy <> 0) 	
							
	             	END
				   FETCH NEXT FROM Record_cursor2 INTO @DmNganhHangREF   
			END   -- kết thúc trường hơp nhiều ngành hàng

			CLOSE Record_cursor2   
			DEALLOCATE Record_cursor2
	END
	ELSE
		BEGIN
			--- Insert du lieu vao table DoanhSoXuatHoaDonNganhHangCore
			IF @IsHopDongNoiBo =1
			  BEGIN
							INSERT INTO DoanhSoXuatHoaDonNganhHangCore
						    SELECT * FROM (
							SELECT @NgayThucHien AS NgayThucHien,
								   @TenNganhHang AS TenNganhHang,
								   @DmNganhHangREF AS DmNganhHangREF,
								   @HopDongID AS HopDongID,
								   @SoHopDong AS SoHopDong,
								   @NgayDanhSo AS NgayDanhSo,
								   @NgayKyHopDong AS NgayKyHopDong,
								   @TenNhanVien AS TenNhanVien,
								   @DmNhanVienREF AS DmNhanVienREF,
								   @TenPhongBan AS TenPhongBan,
								   @PhongBanREF AS PhongBanREF,
								   @TenBoPhan AS TenBoPhan,
								   @BoPhanREF AS BoPhanREF,
								   @TenNhom AS TenNhom,
								   @NhomREF AS NhomREF,
								   @TenKhachHang AS TenKhachHang,
								   @DmKhachHangREF AS DmKhachHangREF,
								   @HopDongChiTietREF AS HopDongChiTietREF,
								   @DmSanPhamREF AS DmSanPham,
								   @TenSanPham AS TenSanPham,
								   @TenWebsite AS TenWebsite,
								   @DmWebsiteREF AS DmWebsiteREF
								   --SoLuongThucThu
									, 0 SoLuongPhatSinhDauKy
									, 0 SoLuongPhatSinhTrongKy
									, 0 SoLuongPhatSinhCuoiKy
									--SoLuongKM
									, 0 SoLuongKMPhatSinhDauKy
									, 0 SoLuongKMPhatSinhTrongKy
									, 0 SoLuongKMPhatSinhCuoiKy
									--SoLuongNB
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE 0
										END	
									)SoLuongNBPhatSinhDauKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE @SoLuong 
												END) SoLuongNBPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE   @SoLuong
									  END	) SoLuongNBPhatSinhCuoiKy
									, @DonViTinhREF AS DonViTinhRef
									, @DonViTinh AS donvitinh
									, @TenDangNhap AS tendangnhap
									, @DonGia AS dongia
									, @ChietKhau AS chietkhau
									--ThanhtienThucThu
									, 0 ThanhTienPhatSinhDauKy
									, 0 ThanhTienPhatSinhTrongKy
									, 0 ThanhTienPhatSinhCuoiKy
									--ThanhTienKM
									, 0 ThanhTienKMPhatSinhDauKy
									, 0 ThanhTienKMPhatSinhTrongKy
									, 0 ThanhTienKMPhatSinhCuoiKy
									--SoLuongNB
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE 0
										END	
									)ThanhTienNBPhatSinhDauKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE @ThanhTienHoaDon	END) ThanhTienNBPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE   @ThanhTienHoaDon
									  END	) ThanhTienNBPhatSinhCuoiKy
									  , @TrangThaiHopDong	AS trangthaihd	
										, N'Chay du lieu qua ky' DienGiai
										, 'ASD' CreatedBy
										, GETDATE() CreatedAt
										, 'ASD' LastModifiedBy
										, GETDATE() LastModifiedAt
										, 0 RecordStatus
										, 0 DeletedStatus
										, 0 PrintStatus
										, 1 TypeRecordStatus -- 0 La chay du lieu qua khu
										,@SoHoaDon AS SoHoaDon
										,@NgayXuatHoaDon AS NgayXuatHD
										,@ThongTinHoaDonID AS TTHDID
										, @DmListNganhHangREF AS dmlistnganhhangref
										, @DmMaHopDongREF AS DmmaHD
						    ) A
						     WHERE (A.SoLuongPhatSinhTrongKy <> 0 OR A.SoLuongKMPhatSinhTrongKy <>0 
							OR A.ThanhTienPhatSinhTrongKy<> 0 OR A.ThanhTienKMPhatSinhTrongKy <> 0) 	
						    
			  END
			  ELSE
			  	BEGIN
			  		     INSERT INTO DoanhSoXuatHoaDonNganhHangCore
			  		     SELECT * FROM(
							SELECT @NgayThucHien AS NgayThucHien,
								   @TenNganhHang AS TenNganhHang,
								   @DmNganhHangREF AS DmNganhHangREF,
								   @HopDongID AS HopDongID,
								   @SoHopDong AS SoHopDong,
								   @NgayDanhSo AS NgayDanhSo,
								   @NgayKyHopDong AS NgayKyHopDong,
								   @TenNhanVien AS TenNhanVien,
								   @DmNhanVienREF AS DmNhanVienREF,
								   @TenPhongBan AS TenPhongBan,
								   @PhongBanREF AS PhongBanREF,
								   @TenBoPhan AS TenBoPhan,
								   @BoPhanREF AS BoPhanREF,
								   @TenNhom AS TenNhom,
								   @NhomREF AS NhomREF,
								   @TenKhachHang AS TenKhachHang,
								   @DmKhachHangREF AS DmKhachHangREF,
								   @HopDongChiTietREF AS HopDongChiTietREF,
								   @DmSanPhamREF AS DmSanPham,
								   @TenSanPham AS TenSanPham,
								   @TenWebsite AS TenWebsite,
								   @DmWebsiteREF AS DmWebsiteREF
								   --SoLuongThucThu
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE 0
										END	
									)SoLuongPhatSinhDauKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE @SoLuong 
												END) SoLuongPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE   @SoLuong
									  END	) SoLuongPhatSinhCuoiKy
									--SoLuongKM
									, 0 SoLuongKMPhatSinhDauKy
									, 0 SoLuongKMPhatSinhTrongKy
									, 0 SoLuongKMPhatSinhCuoiKy
									--SoLuongNB
									, 0 SoLuongNBPhatSinhDauKy
									, 0 SoLuongNBPhatSinhTrongKy
									, 0 SoLuongNBPhatSinhCuoiKy
									, @DonViTinhREF AS DonViTinhref
									, @DonViTinh AS donvitinh
									, @TenDangNhap AS tendangnhap
									, @DonGia AS dongia
									, @ChietKhau AS chietkhau
									--ThanhtienThucThu
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE 0
										END	
									)ThanhTienPhatSinhDauKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE @ThanhTienHoaDon 	END ) ThanhTienPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE   @ThanhTienHoaDon
									  END	) ThanhTienPhatSinhCuoiKy
									--ThanhTienKM
									, 0 ThanhTienKMPhatSinhDauKy
									, 0 ThanhTienKMPhatSinhTrongKy
									, 0 ThanhTienKMPhatSinhCuoiKy
									--Thanh tien noi bo
									, 0 ThanhTienNBPhatSinhDauKy
									, 0 ThanhTienNBPhatSinhTrongKy
									, 0 ThanhTienNBPhatSinhCuoiKy
									  , @TrangThaiHopDong	AS trangthaihd	
										, N'Chay du lieu qua ky' DienGiai
										, 'ASD' CreatedBy
										, GETDATE() CreatedAt
										, 'ASD' LastModifiedBy
										, GETDATE() LastModifiedAt
										, 0 RecordStatus
										, 0 DeletedStatus
										, 0 PrintStatus
										, 1 TypeRecordStatus -- 0 La chay du lieu qua khu
										,@SoHoaDon AS SoHoaDon
										,@NgayXuatHoaDon AS NgayXuatHD
										,@ThongTinHoaDonID AS TTHDID
										, @DmListNganhHangREF AS dmlistnganhhangref
										, @DmMaHopDongREF AS DmmaHD
			  		     ) A
			  		      WHERE (A.SoLuongPhatSinhTrongKy <> 0 OR A.SoLuongKMPhatSinhTrongKy <>0 
							OR A.ThanhTienPhatSinhTrongKy<> 0 OR A.ThanhTienKMPhatSinhTrongKy <> 0) 	
			  	END

   
		 END
END

```
