# Stored Procedure: `Insert_DoanhSoNganhHangCoreChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-01-22 15:15:50.220000
- **Ngày sửa cuối**: 2015-01-23 16:11:45.203000

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

--EXEC [Insert_DoanhSoNganhHangCoreChiTiet] '2013-12-31'

CREATE  PROCEDURE [dbo].[Insert_DoanhSoNganhHangCoreChiTiet] 
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @SoHopDong NVARCHAR(50), @HopDongFK INT, @TenNhanVien NVARCHAR(100), @NhanVienREF INT, @DsNhanHangREF NVARCHAR(200)
	DECLARE @TenKhachHang NVARCHAR(200), @DmKhachHangREF INT, @HopDongChiTietID INT, @LstTenNganhHang NVARCHAR(200), @DmLstNganhHang NVARCHAR(250)
	DECLARE @TenHinhThucSP NVARCHAR(100), @DmHinhThucSP INT, @DmNhomWebsiteREF INT, @TenNhomWebsite NVARCHAR(100), @DmWebsiteREF INT, @TenWebsite NVARCHAR(50)
	DECLARE @DmSanPhamREF INT, @TenSanPham NVARCHAR(100), @ThanhTien BIGINT, @TenHinhThucKy NVARCHAR(50), @TenNganhHang NVARCHAR(200), @DoanhSoTienVe BIGINT
	DECLARE @DmNganhHang INT, @TenNhanHang NVARCHAR(100),@SoLuongNganh INT, @DmPhongREF INT, @DmBoPhanREF INT
	DECLARE @DoanhSoKyHaiDau BIGINT, @DoanhSoThucChay BIGINT, @TenKhachHangSoHuu NVARCHAR(200), @ListHopdongChiTietIDNhan NVARCHAR(50)
	DECLARE @DmKenhREF INT , @Kenh NVARCHAR(100), @TongThanhTienThucChayDT BIGINT, @CheckIsExist INT
	
	SET @NgayThucHien = CONVERT(date,@NgayThucHien)
	
	--DELETE THONG TIN NGANH HANG CHI TIET
	DELETE FROM dbo.RptNganhHangThongTinChiTiet
	WHERE convert(date,NgayThucHien) = @NgayThucHien
	
	--TINH DU LIEU THONG TIN NGANH HANG
	DECLARE Record_Cursor CURSOR FOR 
	SELECT hd.SoHopDong, hdct.HopDongFK, hd.TenNhanVien, hd.SysNhanVienREF, hd.DmPhongBanREF, hd.DmBoPhanREF
		, hd.TenKhachHang, hd.DmKhachHangREF, HDCT.HopDongChiTietID, hdct.DanhSachNhanHangREF, hdct.TenNhomNganh
		, hdct.DmNhomNganhREF, hdct.DmLoaiREF
		, hdct.TenLoai, hdct.DmNhomWebsiteREF, hdct.TenNhomWebsite, hdct.TenWebsite, hdct.DmWebsiteREF
		, hdct.DmSanPhamREF, hdct.TenSanPham, hdct.ThanhTien
	  FROM HopDong hd 
	INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
	WHERE hd.TrangThaiHopDong <> 3
	--AND hd.IsBanCung = 1 
	AND hdct.DeletedStatus = 0
	AND Convert(date,hd.NgayDanhSoHopDong) = @NgayThucHien 
	ORDER BY hd.NgayDanhSoHopDong
		
	OPEN Record_Cursor

	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor into 
			@SoHopDong, @HopDongFK, @TenNhanVien, @NhanVienREF, @DmPhongREF, @DmBoPhanREF
			, @TenKhachHang, @DmKhachHangREF, @HopDongChiTietID, @DsNhanHangREF
			, @LstTenNganhHang, @DmLstNganhHang, @DmHinhThucSP, @TenHinhThucSP
			, @DmNhomWebsiteREF, @TenNhomWebsite, @TenWebsite, @DmWebsiteREF, @DmSanPhamREF, @TenSanPham, @ThanhTien
			
	WHILE @@FETCH_STATUS = 0
		BEGIN
			--PRINT @HopDongChiTietID
			SET @SoLuongNganh = 0
			SET @TongThanhTienThucChayDT = 0
			SET @CheckIsExist = 0
			SET @SoHopDong = ISNULL(@SoHopDong,'')
			SET @HopDongFK = ISNULL(@HopDongFK,0)
			SET @TenNhanVien = ISNULL(@TenNhanVien,'')
			SET @NhanVienREF = ISNULL(@NhanVienREF ,0)
			SET @TenKhachHang = ISNULL(@TenKhachHang,'')
			SET @DmKhachHangREF = ISNULL(@DmKhachHangREF,0)
			SET @HopDongChiTietID = ISNULL(@HopDongChiTietID,0)
			SET @LstTenNganhHang = ISNULL(@LstTenNganhHang,'')
			SET @DmLstNganhHang = ISNULL(@DmLstNganhHang,'')
			SET @DmHinhThucSP = ISNULL(@DmHinhThucSP,0)
			SET @TenHinhThucSP = ISNULL(@TenHinhThucSP,'')
			SET @DmNhomWebsiteREF = ISNULL(@DmNhomWebsiteREF,0)
			SET @TenNhomWebsite = ISNULL(@TenNhomWebsite,'')
			SET @DoanhSoThucChay = 0
			SET @DsNhanHangREF = ISNULL(@DsNhanHangREF,'')
			SET @DoanhSoTienVe = 0
			--PRINT 'hopdongchitiet :' + CONVERT(NVARCHAR(50), @HopDongChiTietID)
			DECLARE Record_Cursor1 CURSOR FOR 
			SELECT dbo.FormatString(item) FROM dbo.ArrayToTable(dbo.Array(@DmLstNganhHang,','))
			OPEN Record_Cursor1
			FETCH NEXT FROM Record_Cursor1 into @DmNganhHang
			WHILE @@FETCH_STATUS = 0
				BEGIN
					SET @DoanhSoKyHaiDau = 0
					SET @DoanhSoThucChay = 0
					SET @TenNhanHang = ''
					IF(@DmNganhHang <> 0)
					BEGIN
						SELECT @SoLuongNganh = count(a.DmNganhHang) from
						(
							SELECT dbo.FormatString(item) DmNganhHang
							FROM dbo.ArrayToTable(dbo.Array(@DmLstNganhHang,','))
						)a
						IF(@SoLuongNganh <> 0)
						BEGIN
						--PRINT @DmNganhHang
						--Ten Hinh thuc san pham
						SET @TenHinhThucSP =
						(
							SELECT dlsp.TenLoaiSanPham FROM DmLoaiSanPham dlsp
							WHERE dlsp.DmLoaiSanPhamID = @DmHinhThucSP
							AND dlsp.DeletedStatus = 0
						)
						SET @TenHinhThucSP = ISNULL(@TenHinhThucSP,'')
						--Get Ten kenh và DmKenh
						IF(@DmSanPhamREF IN (231,238,339,342,337,240,370,598,613))
							BEGIN
								SET @DmKenhREF = isnull(@DmNhomWebsiteREF,0)
								SET @Kenh = ISNULL(@TenNhomWebsite,'')
							END
						ELSE
							BEGIN
								SET @DmKenhREF = isnull(@DmWebsiteREF,0)
								SET @Kenh = ISNULL(@TenWebsite,'')
							END
						END 
						--PRINT @DmKenhREF
						SELECT @CheckIsExist = COUNT(rnhttct.DoanhSoThucChay)
						  FROM RptNganhHangThongTinChiTiet rnhttct
						WHERE rnhttct.DmNganhHangREF = @DmNganhHang
						AND rnhttct.HopDongREF = @HopDongFK
						AND rnhttct.DmSanPhamREF = @DmSanPhamREF
						AND rnhttct.DmKenhREF = @DmKenhREF
						AND convert(date,rnhttct.NgayThucHien) = @NgayThucHien
						
						--PRINT 'Doanh so ky 2 dau'
						--Doanh so ky 2 dau
						SELECT @DoanhSoKyHaiDau = rnhttct.DoanhSoKyHaiDau
							,@ListHopdongChiTietIDNhan = rnhttct.HopDongChiTietREF
						FROM RptNganhHangThongTinChiTiet rnhttct
						WHERE rnhttct.DmNganhHangREF = @DmNganhHang
						AND rnhttct.HopDongREF = @HopDongFK
						AND rnhttct.DmSanPhamREF = @DmSanPhamREF
						AND rnhttct.DmKenhREF = @DmKenhREF
						AND convert(date,rnhttct.NgayThucHien) = @NgayThucHien
						
						
						SET @DoanhSoKyHaiDau = ISNULL(@DoanhSoKyHaiDau,0)
						SET @DoanhSoKyHaiDau = @DoanhSoKyHaiDau + (@ThanhTien/@SoLuongNganh)
						
						--TINH DOANH SO TIEN VE
						
						SET @ListHopdongChiTietIDNhan = isnull(@ListHopdongChiTietIDNhan,'') + ',' + CONVERT(NVARCHAR(50), @HopDongChiTietID)
						--PRINT 'ten nganh hang'
						--Get Ten Nganh hang
						SELECT @TenNganhHang = dnh.TenNghanhHang
						, @DmNganhHang = dnh.DmNghanhHangID
						FROM DmNghanhHang dnh
						WHERE dnh.DmNghanhHangID = @DmNganhHang
						
						SET @TenNganhHang = ISNULL(@TenNganhHang,'')
						
						 
						
						--PRINT '@CheckIsExist:' + CONVERT(NVARCHAR(50),@DmKhachHangREF)
						IF(@CheckIsExist = 0)
						BEGIN
							--Get Hinh thuc ky
							--3 = Hinh thuc dai ly
							--khach 3 la hinh thuc truc tiep
							SELECT @TenHinhThucKy = B.TenHinhThuc FROM 
							(
								SELECT distinct	(CASE WHEN khf.DmHinhThucKhachHangREF = 3 THEN N'Dai ly'
											ELSE N'Truc tiep'
						      			 END
						      			 ) TenHinhThuc
								FROM KhachHangThongTinChung khf
								WHERE khf.KhachHangThongTinChungID = @DmKhachHangREF
							)B
							
							--PRINT 'ten nhan hang:' + CONVERT(NVARCHAR(50),@DsNhanHangREF)
							--Get ten nhan hang
							SET @TenNhanHang = 
							(SELECT
								stuff(
								(
								select cast(',' as varchar(max)) + U.TenNhanHang
								FROM DmNhanHang U
								WHERE U.DmNhanHangID IN (SELECT dbo.FormatString(item) FROM dbo.ArrayToTable(dbo.Array(@DsNhanHangREF,',')))
								order by U.TenNhanHang
								for xml path('') 
								), 1, 1, '') AS TenNganhHang
							)
							SET @DsNhanHangREF = ISNULL(@DsNhanHangREF,'')
							SET @TenNhanHang = ISNULL(@TenNhanHang,'')
							--PRINT 'khach hang' + CONVERT(NVARCHAR(50),@DmKhachHangREF)
													
							--Get ten khach hang so huu
							SELECT @TenKhachHangSoHuu = khf.TenKhachHang 
							FROM KhachHangThongTinChung khf
							WHERE khf.KhachHangThongTinChungID = @DmKhachHangREF
							
							SET @DoanhSoThucChay = 0
							
							INSERT INTO [dbo].[RptNganhHangThongTinChiTiet]
						   ([DmNganhHangREF],[TenNganhHang],[DmNhanHangREF],[TenNhanHang],[DmNhanSuREF],[TenNhanSu]
							  ,[SoHopDong],[HopDongREF],[DmPhongREF],[DmBoPhanREF],[DmKhachHangREF],[TenKhachHang]
							  ,[HinhThucKy],[DmHinhThucSanPhamREF],[HinhThucSanPham],[DmSanPhamREF],[TenSanPham]
							  ,[DmKenhREF],[TenKenh],[DoanhSoKyHaiDau],[DoanhSoThucChay],[DoanhSoTienVe]
							  ,[TongDoanhSoKyHaiDau],[TongDoanhSoThucChay],[NgayThucHien],[HopDongChiTietREF]
							  ,[CreatedBy],[CreatedAt],[LastModifiedBy],[LastModifiedAt],[RecordStatus],[DeletedStatus])
					 VALUES
						   (@DmNganhHang,@TenNganhHang,@DsNhanHangREF,@TenNhanHang,@NhanVienREF,@TenNhanVien
						   ,@SoHopDong,@HopDongFK, @DmPhongREF, @DmBoPhanREF,@DmKhachHangREF,@TenKhachHang
						   ,@TenHinhThucKy,@DmHinhThucSP,@TenHinhThucSP,@DmSanPhamREF,@TenSanPham
						   ,@DmKenhREF,@Kenh,@DoanhSoKyHaiDau,@DoanhSoThucChay, @DoanhSoTienVe
						   ,@DoanhSoKyHaiDau,@DoanhSoThucChay,@NgayThucHien,@HopDongChiTietID
						   ,'ABM',GETDATE(),'ABM',GETDATE() ,0,0)

						END
						ELSE
							BEGIN
								UPDATE RptNganhHangThongTinChiTiet
								SET
									-- RptNganhHangThongTinChiTietID = ? -- this column value is auto-generated
									DoanhSoKyHaiDau = @DoanhSoKyHaiDau,
									TongDoanhSoKyHaiDau = @DoanhSoKyHaiDau,
									HopDongChiTietREF = @ListHopdongChiTietIDNhan,
									LastModifiedBy = 'ABM',
									LastModifiedAt = GETDATE()
								WHERE DmNganhHangREF = @DmNganhHang
									AND HopDongREF = @HopDongFK
									AND DmSanPhamREF = @DmSanPhamREF
									AND DmKenhREF = @DmKenhREF
									AND convert(date,NgayThucHien) = @NgayThucHien 	
							END
						----
					END
					
				FETCH NEXT FROM Record_Cursor1 into @DmNganhHang
				END
			CLOSE Record_Cursor1
			DEALLOCATE Record_Cursor1
		
		FETCH NEXT FROM Record_Cursor into 
			@SoHopDong, @HopDongFK, @TenNhanVien, @NhanVienREF, @DmPhongREF, @DmBoPhanREF
			, @TenKhachHang, @DmKhachHangREF, @HopDongChiTietID, @DsNhanHangREF
			, @LstTenNganhHang, @DmLstNganhHang, @DmHinhThucSP, @TenHinhThucSP
			, @DmNhomWebsiteREF, @TenNhomWebsite, @TenWebsite, @DmWebsiteREF, @DmSanPhamREF, @TenSanPham, @ThanhTien
	END

	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor
	--SELECT '1'
END


```
