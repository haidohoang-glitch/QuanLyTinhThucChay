# Stored Procedure: `Insert_DoanhSoHaiDauNhanHangCore_NoiBo_History`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-22 16:43:09.717000
- **Ngày sửa cuối**: 2015-04-22 16:43:09.717000

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
CREATE PROCEDURE [dbo].[Insert_DoanhSoHaiDauNhanHangCore_NoiBo_History]
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	DECLARE @CountNhan INT, @ChiSoSLNhanM BIGINT, @ChiSoTTNhanM BIGINT ;
	SET @CountNhan = 0;
	
	DECLARE @CheckHopDongChiTietTcID INT;
	DECLARE @SoLuongNhan INT;
	DECLARE @DsTenNhanHang NVARCHAR(200),@DmListNhanHangREF NVARCHAR(200), @DsTenNganhHang NVARCHAR(500), @DmListNganhHangREF NVARCHAR(500);
	DECLARE @HopDongID INT ,@SoHopDong NVARCHAR(200), @TenNhanVien NVARCHAR(200), @DmNhanVienREF INT, @TenPhongBan NVARCHAR(200), @PhongBanREF INT;
	DECLARE @TenBoPhan NVARCHAR(200), @BoPhanREF INT, @TenNhom NVARCHAR(200), @NhomREF INT, @TenKhachHang NVARCHAR(200),@DmKhachHangREF INT;
	DECLARE @HopDongChiTietREF INT, @TenSanPham NVARCHAR(200), @DmSanPhamREF INT, @TenWebsite NVARCHAR(200), @DmWebsiteREF INT; 
	DECLARE @DonViTinhREF INT, @DonViTinh NVARCHAR(50),@TenDangNhap NVARCHAR(50), @TenNhanHang NVARCHAR(200),@DmNhanHangREF INT ;
	DECLARE @ChietKhau FLOAT, @DonGia FLOAT, @SoLuong BIGINT, @ThanhTien FLOAT,@TrangThaiHopDong INT ;
	DECLARE @NgayDanhSo DATETIME, @NgayKyHopDong DATETIME,@DmMaHopDongREF INT ;
    -- Insert statements for procedure here
	DECLARE Record_cursor1 CURSOR FOR  
	SELECT 
		hdct.NhanHang,
		hdct.DanhSachNhanHangREF,
		hdct.TenNhomNganh,
		hdct.DmNhomNganhREF,
		hd.HopDongID,
		hd.SoHopDong,
		hd.NgayDanhSoHopDong,
		hd.NgayKyHopDong,
		hd.TenNhanVien,
		hd.SysNhanVienREF,
		hd.TenPhongBan,
		hd.DmPhongBanREF,
		Hd.TenBoPhan,
		hd.DmBoPhanREF,
		hd.TenNhom,
		hd.DmNhomREF,
		hd.TenKhachHang,
		hd.DmKhachHangREF,
		hdct.HopDongChiTietID,
		hdct.TenSanPham,
		hdct.DmSanPhamREF,
		hdct.TenWebsite,
		hdct.DmWebsiteREF,
		hdct.DonViTinhREF,
		hdct.DonViTinh,
		hd.TenDangNhap,
		hdct.ChietKhau,
		hdct.DonGia,
		hdct.SoLuong,
		hdct.ThanhTien,
		hd.TrangThaiHopDong,
		hd.DmMaHopDongREF
	FROM HopDong hd
		INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		WHERE convert(date,hd.NgayDanhSoHopDong) = @NgayThucHien
		AND hdct.DeletedStatus = 0
		AND hd.IsBanCung = 1
		AND hd.DeletedStatus = 0
		AND hd.TrangThaiHopDong <> 3
		AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](hd.DmMaHopDongREF, @NgayThucHien) = 1

	OPEN Record_cursor1  
	 
	FETCH NEXT FROM Record_cursor1 INTO @DsTenNhanHang, @DmListNhanHangREF,@DsTenNganhHang , @DmListNganhHangREF 
	,@HopDongID  ,@SoHopDong, @NgayDanhSo, @NgayKyHopDong , @TenNhanVien , @DmNhanVienREF , @TenPhongBan, @PhongBanREF 
	, @TenBoPhan , @BoPhanREF , @TenNhom , @NhomREF , @TenKhachHang ,@DmKhachHangREF 
	, @HopDongChiTietREF , @TenSanPham , @DmSanPhamREF , @TenWebsite , @DmWebsiteREF 
	, @DonViTinhREF , @DonViTinh,@TenDangNhap,@ChietKhau , @DonGia , @SoLuong , @ThanhTien ,@TrangThaiHopDong
	, @DmMaHopDongREF
	WHILE @@FETCH_STATUS = 0   
	BEGIN   
		    SET @DmNhanHangREF = 0
			SET @TenNhanHang = ''
			SET @CountNhan = 0
			
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
										, N'Chay du lieu qua ky' DienGiai
										, 'ASD' CreatedBy
										, GETDATE() CreatedAt
										, 'ASD' LastModifiedBy
										, GETDATE() LastModifiedAt
										, 0 RecordStatus
										, 0 DeletedStatus
										, 0 PrintStatus
										, 0 TypeRecordStatus -- 0 La chay du lieu qua khu\
										,@NgayDanhSo
								        ,@NgayKyHopDong
								        ,@DmListNhanHangREF
								        ,@DmMaHopDongREF
																  
				   FETCH NEXT FROM Record_cursor2 INTO @DmNhanHangREF   
			END   

			CLOSE Record_cursor2   
			DEALLOCATE Record_cursor2
	END
	ELSE
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
									--SoLuongNB
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
										, N'Chay du lieu qua ky' DienGiai
										, 'ASD' CreatedBy
										, GETDATE() CreatedAt
										, 'ASD' LastModifiedBy
										, GETDATE() LastModifiedAt
										, 0 RecordStatus
										, 0 DeletedStatus
										, 0 PrintStatus
										, 0 TypeRecordStatus -- 0 La chay du lieu qua khu
										,@NgayDanhSo
								        ,@NgayKyHopDong 
								        ,@DmListNhanHangREF
								        ,@DmMaHopDongREF
		END

   FETCH NEXT FROM Record_cursor1 INTO @DsTenNhanHang, @DmListNhanHangREF,@DsTenNganhHang , @DmListNganhHangREF 
	,@HopDongID  ,@SoHopDong, @NgayDanhSo, @NgayKyHopDong , @TenNhanVien , @DmNhanVienREF , @TenPhongBan, @PhongBanREF 
	, @TenBoPhan , @BoPhanREF , @TenNhom , @NhomREF , @TenKhachHang ,@DmKhachHangREF 
	, @HopDongChiTietREF , @TenSanPham , @DmSanPhamREF , @TenWebsite , @DmWebsiteREF 
	, @DonViTinhREF , @DonViTinh,@TenDangNhap,@ChietKhau , @DonGia , @SoLuong , @ThanhTien ,@TrangThaiHopDong  
	,@DmMaHopDongREF
	END   
	CLOSE Record_cursor1   
	DEALLOCATE Record_cursor1
END

```
