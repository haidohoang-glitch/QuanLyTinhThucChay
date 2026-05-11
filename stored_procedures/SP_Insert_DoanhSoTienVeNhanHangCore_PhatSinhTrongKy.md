# Stored Procedure: `Insert_DoanhSoTienVeNhanHangCore_PhatSinhTrongKy`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-12 10:47:00.773000
- **Ngày sửa cuối**: 2015-06-12 10:47:00.773000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmMaHopDongREF` | `int(4)` | No |
| `@ThongTinTienVeID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--[dbo].[Insert_DoanhSoTienVeNhanHangCore_PhatSinhTrongKy] '2014-01-01'
create PROCEDURE [dbo].[Insert_DoanhSoTienVeNhanHangCore_PhatSinhTrongKy]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@HopDongID INT,
	@HopDongChiTietREF INT,
	@DmMaHopDongREF INT,
	@ThongTinTienVeID INT
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
	DECLARE @NgayDanhSo DATETIME, @NgayKyHopDong DATETIME, @SoHoaDon NVARCHAR(50), @NgayThanhToan DATETIME;
    DECLARE @ThanhTienHoaDon float
    -- Insert statements for procedure here
   --DELETE FROM DoanhSoTienVeNhanHangCore WHERE HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietREF AND ThongTinTienVeREF = @ThongTinTienVeID
	SELECT 
		@DsTenNhanHang = hdct.NhanHang,
		@DmListNhanHangREF = hdct.DanhSachNhanHangREF,
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
		@NgayThanhToan = tthd.NgayThanhToan
		
	FROM HopDong hd
		INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		INNER JOIN ThongTinTienVe tthd ON tthd.HopDongREF = hd.HopDongID
		WHERE 1=1
		AND hd.HopDongID = @HopDongID
			AND hdct.HopDongChiTietID = @HopDongChiTietREF
			AND tthd.ThongTinTienVeID = @ThongTinTienVeID
			AND Hd.TrangThaiHopDong <>3
			AND hdct.DeletedStatus =0
			AND tthd.DeletedStatus =0
			AND (SELECT SUM(ThanhTien) FROM HopDongChiTiet hdct2 WHERE hdct2.HopDongFK = hd.HopDongID AND hdct2.DeletedStatus =0) > 0
			AND hdct.ChietKhau <> 100
		--AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](hd.DmMaHopDongREF, @NgayThucHien) = 1
			SET @ThanhTienHoaDon = (SELECT [dbo].[fn_GetThanhTienByNgay_DoanhSoTienVeCore] 
					(
						@NgayThucHien,
						@HopDongID,
						@ThongTinTienVeID,
						@ThanhTien
					))
		    SET @DmNhanHangREF = 0
			SET @TenNhanHang = ''
			SELECT @SoLuongNhan = count(a.DmNhanHang) from
			(
				SELECT distinct dbo.FormatString(item) DmNhanHang
				FROM dbo.ArrayToTable(dbo.Array(@DmListNhanHangREF,','))
			)a
			IF @DmListNhanHangREF ='' SET @SoLuongNhan =0
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
				    			SET @ChiSoSLNhanM =  @SoLuong - (@SoLuongNhan-1) * cast(@SoLuong/@SoLuongNhan AS int)
				    			SET @ChiSoTTNhanM =  CAST(@ThanhTienHoaDon AS BIGINT) - (@SoLuongNhan-1) * cast(@SoLuong/@SoLuongNhan AS int) * CAST(@ThanhTienHoaDon AS BIGINT)/@SoLuong
				    	    END
				    	ELSE
				    		BEGIN
				    			SET @ChiSoSLNhanM =  0
				    			SET @ChiSoTTNhanM =  CAST(@ThanhTienHoaDon AS BIGINT) - (@SoLuongNhan-1)  * CAST(@ThanhTienHoaDon AS BIGINT)/@SoLuongNhan
				    		END
				   
				    	END 
				    	
				   SELECT @TenNhanHang = dnh.TenNhanHang, @DmListNganhHangREF = dnh.DmNghanhHangREF
					  FROM DmNhanHang dnh
					WHERE dnh.DmNhanHangID = @DmNhanHangREF
					SET @TenNhanHang = ISNULL(@TenNhanHang,'')
					SET @DmListNganhHangREF = ISNULL(@DmListNganhHangREF,'')
					
					IF @IsHopDongNoiBo =1
					BEGIN
							--- Insert du lieu vao table DoanhSoTienVeNhanHangCore
							INSERT INTO DoanhSoTienVeNhanHangCore
							SELECT * FROM 
							(
							SELECT @NgayThucHien AS NgayThucHien,
								   @TenNhanHang AS tennhanhang,
								   @DmNhanHangREF AS dmnhanhangref,
								   '' AS DsTenNganhHang,
								   @DmListNganhHangREF AS dmlistnganhhangref,
								   @HopDongID AS hopdongid,
								   @SoHopDong AS sohopdong,
								   @NgayDanhSo AS NgayDanhSo,
								   @NgayKyHopDong AS NgayKyHopDong,
								   
								   @TenNhanVien AS tennhanvien,
								   @DmNhanVienREF AS dmnhanvienref,
								   @TenPhongBan AS tenphongban,
								   @PhongBanREF AS phongbanref,
								   @TenBoPhan AS tenbophan,
								   @BoPhanREF AS bophanref,
								   @TenNhom AS tennhom,
								   @NhomREF AS nhomref,
								   @TenKhachHang AS tenkhachhang,
								   @DmKhachHangREF AS dmkhachhangref,
								   @HopDongChiTietREF AS hopdongchitietref,
								   @DmSanPhamREF AS dmsanphamref,
								   @TenSanPham AS tensanpham,
								   @TenWebsite AS tenweb,
								   @DmWebsiteREF AS webref
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
									, @DonViTinhREF AS donvitinhref
									, @DonViTinh AS dvt
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
									  , @TrangThaiHopDong	AS trangthaihd	
										, N'Chay du lieu phat sinh' DienGiai
										, 'ASD' CreatedBy
										, GETDATE() CreatedAt
										, 'ASD' LastModifiedBy
										, GETDATE() LastModifiedAt
										, 0 RecordStatus
										, 0 DeletedStatus
										, 0 PrintStatus
										, 1 TypeRecordStatus 
								
										,@NgayThanhToan AS NgayThanhToan
										,@ThongTinTienVeID AS ThongTinTienVe
										, @DmListNhanHangREF AS DmListNhanGangREF
										, @DmMaHopDongREF AS Dmmasohd
							) A
							WHERE (A.SoLuongPhatSinhTrongKy <> 0 OR A.SoLuongKMPhatSinhTrongKy <>0 
							OR A.ThanhTienPhatSinhTrongKy<> 0 OR A.ThanhTienKMPhatSinhTrongKy <> 0) 	
																  
	                    END
	             ELSE
	             	BEGIN
	             		  INSERT INTO DoanhSoTienVeNhanHangCore
	             		  SELECT * FROM 
	             		  (
							SELECT @NgayThucHien AS NgayThucHien,
								   @TenNhanHang AS tennhanhang,
								   @DmNhanHangREF AS dmnhanhangref,
								   '' AS DsTenNganhHang,
								   @DmListNganhHangREF AS dmlistnganhhangref,
								   @HopDongID AS hopdongid,
								   @SoHopDong AS sohopdong,
								   @NgayDanhSo AS NgayDanhSo,
								   @NgayKyHopDong AS NgayKyHopDong,
								   
								   @TenNhanVien AS tennhanvien,
								   @DmNhanVienREF AS dmnhanvienref,
								   @TenPhongBan AS tenphongban,
								   @PhongBanREF AS phongbanref,
								   @TenBoPhan AS tenbophan,
								   @BoPhanREF AS bophanref,
								   @TenNhom AS tennhom,
								   @NhomREF AS nhomref,
								   @TenKhachHang AS tenkhachhang,
								   @DmKhachHangREF AS dmkhachhangref,
								   @HopDongChiTietREF AS hopdongchitietref,
								   @DmSanPhamREF AS dmsanphamref,
								   @TenSanPham AS tensanpham,
								   @TenWebsite AS tenweb,
								   @DmWebsiteREF AS webref
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
									, @DonViTinhREF AS dvtref
									, @DonViTinh AS dvt
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
									  , @TrangThaiHopDong	AS trangthaihopdong	
										, N'Chay du lieu qua ky' DienGiai
										, 'ASD' CreatedBy
										, GETDATE() CreatedAt
										, 'ASD' LastModifiedBy
										, GETDATE() LastModifiedAt
										, 0 RecordStatus
										, 0 DeletedStatus
										, 0 PrintStatus
										, 1 TypeRecordStatus 
							
										,@NgayThanhToan AS NgayThanhToan
										,@ThongTinTienVeID AS ThongTinTienVe
										, @DmListNhanHangREF AS DmListNhanGangREF
										, @DmMaHopDongREF AS Dmmasohd
	             		  ) A
	             		  WHERE (A.SoLuongPhatSinhTrongKy <> 0 OR A.SoLuongKMPhatSinhTrongKy <>0 
						OR A.ThanhTienPhatSinhTrongKy<> 0 OR A.ThanhTienKMPhatSinhTrongKy <> 0) 	
																  
	             	END
				   FETCH NEXT FROM Record_cursor2 INTO @DmNhanHangREF   
			END   

			CLOSE Record_cursor2   
			DEALLOCATE Record_cursor2
	END
	ELSE
		BEGIN
			--- Insert du lieu vao table DoanhSoTienVeNhanHangCore
			IF @IsHopDongNoiBo =1
			  BEGIN
							INSERT INTO DoanhSoTienVeNhanHangCore
							SELECT * FROM 
							(
							SELECT @NgayThucHien AS NgayThucHien,
								   @TenNhanHang AS tennhanhang,
								   @DmNhanHangREF AS dmnhanhangref,
								   '' AS DsTenNganhHang,
								   @DmListNganhHangREF AS dmlistnganhhangref,
								   @HopDongID AS hopdongid,
								   @SoHopDong AS sohopdong,
								   @NgayDanhSo AS NgayDanhSo,
								   @NgayKyHopDong AS NgayKyHopDong,
								   
								   @TenNhanVien AS tennhanvien,
								   @DmNhanVienREF AS dmnhanvienref,
								   @TenPhongBan AS tenphongban,
								   @PhongBanREF AS phongbanref,
								   @TenBoPhan AS tenbophan,
								   @BoPhanREF AS bophanref,
								   @TenNhom AS tennhom,
								   @NhomREF AS nhomref,
								   @TenKhachHang AS tenkhachhang,
								   @DmKhachHangREF AS dmkhachhangref,
								   @HopDongChiTietREF AS hopdongchitietref,
								   @DmSanPhamREF AS dmsanphamref,
								   @TenSanPham AS tensanpham,
								   @TenWebsite AS tenweb,
								   @DmWebsiteREF AS webref
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
									, @DonViTinhREF AS dvtref
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
											ELSE @ThanhTienHoaDon 	END) ThanhTienNBPhatSinhTrongKy
									, (
										CASE WHEN @ChietKhau = 100 THEN 0
											ELSE   @ThanhTienHoaDon
									  END	) ThanhTienNBPhatSinhCuoiKy
									  , @TrangThaiHopDong AS trangthaihd		
										, N'Chay du lieu qua ky' DienGiai
										, 'ASD' CreatedBy
										, GETDATE() CreatedAt
										, 'ASD' LastModifiedBy
										, GETDATE() LastModifiedAt
										, 0 RecordStatus
										, 0 DeletedStatus
										, 0 PrintStatus
										, 1 TypeRecordStatus 
								
										,@NgayThanhToan AS NgayThanhToan
										,@ThongTinTienVeID AS ThongTinTienVe
										, @DmListNhanHangREF AS DmListNhanGangREF
										, @DmMaHopDongREF AS Dmmasohd
							)A
							WHERE (A.SoLuongPhatSinhTrongKy <> 0 OR A.SoLuongKMPhatSinhTrongKy <>0 
						OR A.ThanhTienPhatSinhTrongKy<> 0 OR A.ThanhTienKMPhatSinhTrongKy <> 0) 	

			  END
			  ELSE
			  	BEGIN
			  		     INSERT INTO DoanhSoTienVeNhanHangCore
			  		     SELECT * FROM 
			  		     (
							SELECT @NgayThucHien AS NgayThucHien,
								   @TenNhanHang AS tennhanhang,
								   @DmNhanHangREF AS dmnhanhangref,
								   '' AS DsTenNganhHang,
								   @DmListNganhHangREF AS dmlistnganhhangref,
								   @HopDongID AS hopdongid,
								   @SoHopDong AS sohopdong,
								   @NgayDanhSo AS NgayDanhSo,
								   @NgayKyHopDong AS NgayKyHopDong,
								   @TenNhanVien AS tennhanvien,
								   @DmNhanVienREF AS dmnhanvienref,
								   @TenPhongBan AS tenphongban,
								   @PhongBanREF AS phongbanref,
								   @TenBoPhan AS tenbophan,
								   @BoPhanREF AS bophanref,
								   @TenNhom AS tennhom,
								   @NhomREF AS nhomref,
								   @TenKhachHang AS tenkhachhang,
								   @DmKhachHangREF AS dmkhachhangref,
								   @HopDongChiTietREF AS hopdongchitietref,
								   @DmSanPhamREF AS dmsanphamref,
								   @TenSanPham AS tensanpham,
								   @TenWebsite AS tenweb,
								   @DmWebsiteREF AS webref
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
									, @DonViTinhREF AS dvtref
									, @DonViTinh AS dvt
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
											ELSE @ThanhTienHoaDon	END ) ThanhTienPhatSinhTrongKy
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
										, N'Chay du lieu phat sinh' DienGiai
										, 'ASD' CreatedBy
										, GETDATE() CreatedAt
										, 'ASD' LastModifiedBy
										, GETDATE() LastModifiedAt
										, 0 RecordStatus
										, 0 DeletedStatus
										, 0 PrintStatus
										, 1 TypeRecordStatus 
							
										,@NgayThanhToan AS NgayThanhToan
										,@ThongTinTienVeID AS ThongTinTienVe
										, @DmListNhanHangREF AS DmListNhanGangREF
										, @DmMaHopDongREF AS Dmmasohd
										)A
										WHERE (A.SoLuongPhatSinhTrongKy <> 0 OR A.SoLuongKMPhatSinhTrongKy <>0 
						OR A.ThanhTienPhatSinhTrongKy<> 0 OR A.ThanhTienKMPhatSinhTrongKy <> 0) 	

			  	END

   
		 END
END

```
