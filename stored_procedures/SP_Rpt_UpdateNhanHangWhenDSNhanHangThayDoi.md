# Stored Procedure: `Rpt_UpdateNhanHangWhenDSNhanHangThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:35.320000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.730000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE  PROCEDURE [dbo].[Rpt_UpdateNhanHangWhenDSNhanHangThayDoi]
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @SoHopDong NVARCHAR(50), @HopDongFK INT, @TenNhanVien NVARCHAR(100), @NhanVienREF INT
	DECLARE @TenKhachHang NVARCHAR(200), @DmKhachHangREF INT, @HopDongChiTietID INT, @LstTenNhanHang NVARCHAR(200), @DmLstNhanHang NVARCHAR(250)
	DECLARE @TenHinhThucSP NVARCHAR(100), @DmHinhThucSP INT, @DmNhomWebsiteREF INT, @TenNhomWebsite NVARCHAR(100), @DmWebsiteREF INT, @TenWebsite NVARCHAR(50)
	DECLARE @DmSanPhamREF INT, @TenSanPham NVARCHAR(100), @ThanhTien BIGINT, @TenHinhThucKy NVARCHAR(50)
	DECLARE @DmNhanHang INT, @TenNhanHang NVARCHAR(100), @DmNganhHang NVARCHAR(50), @TenNhomNganh NVARCHAR(200), @SoLuongNhan INT
	DECLARE @DoanhSoKyHaiDau BIGINT, @DoanhSoThucChay BIGINT, @TenKhachHangSoHuu NVARCHAR(200), @ListHopdongChiTietIDNhan NVARCHAR(50)
	DECLARE @DmKenhREF INT , @Kenh NVARCHAR(100), @TongThanhTienThucChayDT BIGINT, @CheckIsExist INT
	DECLARE @NgayDanhSoHopDong DATETIME	
	
	SET @NgayThucHien = CONVERT(date,@NgayThucHien)
	
	--TINH DU LIEU THONG TIN NHAN HANG
	DECLARE Record_Cursor CURSOR FOR
	SELECT distinct dnh.DmNhanHangID FROM DmNhanHang dnh
	WHERE dnh.RecordStatus = 1
	AND dnh.DeletedStatus = 0
	AND CONVERT(date,
		( 
			CASE WHEN dnh.CreatedAt >= dnh.LastModifiedAt THEN dnh.CreatedAt 
				ELSE dnh.LastModifiedAt
			END
		)
	) = @NgayThucHien 
		
	OPEN Record_Cursor
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor INTO @DmNhanHang 
	WHILE @@FETCH_STATUS = 0
		BEGIN
			--THUC HIEN CAP NHAT DOANH SO CHO TABLE CHI TIET NHAN HANG
			PRINT @DmNhanHang
			SET @SoLuongNhan = 0
			SET @TongThanhTienThucChayDT = 0
			SET @CheckIsExist = 0
			SET @DoanhSoThucChay = 0

			--XOA DU LIEU DOANH SO KY CUA NHAN
			DELETE FROM RptNhanHangThongTinChiTiet
			WHERE DmNhanHangREF = @DmNhanHang
			
			DECLARE Record_Cursor_ds CURSOR FOR 
			
			SELECT hd.SoHopDong, hdct.HopDongFK, hd.TenNhanVien, hd.SysNhanVienREF
				, hd.TenKhachHang, hd.DmKhachHangREF, hd.NgayDanhSoHopDong, HDCT.HopDongChiTietID, hdct.NhanHang
				, hdct.DanhSachNhanHangREF, hdct.DmLoaiREF
				, hdct.TenLoai, hdct.DmNhomWebsiteREF, hdct.TenNhomWebsite, hdct.TenWebsite, hdct.DmWebsiteREF
				, hdct.DmSanPhamREF, hdct.TenSanPham, hdct.ThanhTien
			  FROM HopDong hd 
			INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
			WHERE hd.TrangThaiHopDong <> 3
			AND hd.IsBanCung = 1 
			AND hdct.DeletedStatus = 0
			AND @DmNhanHang in 
			( 
				SELECT dbo.FormatString(item) DmNhanHang
				FROM dbo.ArrayToTable(dbo.Array(hdct.DanhSachNhanHangREF,',') )
			)
			ORDER BY hd.NgayDanhSoHopDong
			
			OPEN Record_Cursor_ds
			FETCH NEXT FROM Record_Cursor_ds into 
				@SoHopDong, @HopDongFK, @TenNhanVien, @NhanVienREF, @TenKhachHang, @DmKhachHangREF, @NgayDanhSoHopDong, @HopDongChiTietID
				, @LstTenNhanHang, @DmLstNhanHang, @DmHinhThucSP, @TenHinhThucSP
				, @DmNhomWebsiteREF, @TenNhomWebsite, @TenWebsite, @DmWebsiteREF, @DmSanPhamREF, @TenSanPham, @ThanhTien
			WHILE @@FETCH_STATUS = 0
				BEGIN
					SET @DoanhSoKyHaiDau = 0
					SET @DoanhSoThucChay = 0
					SET @TenNhanHang = ''
					SET @SoHopDong = ISNULL(@SoHopDong,'')
					SET @HopDongFK = ISNULL(@HopDongFK,0)
					SET @TenNhanVien = ISNULL(@TenNhanVien,'')
					SET @NhanVienREF = ISNULL(@NhanVienREF ,0)
					SET @TenKhachHang = ISNULL(@TenKhachHang,'')
					SET @DmKhachHangREF = ISNULL(@DmKhachHangREF,0)
					SET @HopDongChiTietID = ISNULL(@HopDongChiTietID,0)
					SET @LstTenNhanHang = ISNULL(@LstTenNhanHang,'')
					SET @DmLstNhanHang = ISNULL(@DmLstNhanHang,'')
					SET @DmHinhThucSP = ISNULL(@DmHinhThucSP,0)
					SET @TenHinhThucSP = ISNULL(@TenHinhThucSP,'')
					SET @DmNhomWebsiteREF = ISNULL(@DmNhomWebsiteREF,0)
					SET @TenNhomWebsite = ISNULL(@TenNhomWebsite,'')
					IF(@DmNhanHang <> 0)
					BEGIN
						SELECT @SoLuongNhan = count(a.DmNhanHang) from
						(
							SELECT dbo.FormatString(item) DmNhanHang
							FROM dbo.ArrayToTable(dbo.Array(@DmLstNhanHang,','))
						)a
						IF(@SoLuongNhan <> 0)
						BEGIN
						--PRINT @DmNhanHang
						--Ten Hinh thuc san pham
						SET @TenHinhThucSP =
						(
							SELECT dlsp.TenLoaiSanPham FROM DmLoaiSanPham dlsp
							WHERE dlsp.DmLoaiSanPhamID = @DmHinhThucSP
							AND dlsp.DeletedStatus = 0
						)
						SET @TenHinhThucSP = ISNULL(@TenHinhThucSP,'')
						--Get Ten kenh và DmKenh
						IF(@DmSanPhamREF IN (231,238,339,342,337,240,370))
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
						--Check ban ghi da ton tai
						SELECT @CheckIsExist = COUNT(rnhttct.DoanhSoThucChay)
						  FROM RptNhanHangThongTinChiTiet rnhttct
						WHERE rnhttct.DmNhanHangREF = @DmNhanHang
						AND rnhttct.HopDongREF = @HopDongFK
						AND rnhttct.DmSanPhamREF = @DmSanPhamREF
						AND rnhttct.DmKenhREF = @DmKenhREF
						AND convert(date,rnhttct.NgayThucHien) = @NgayDanhSoHopDong
						--PRINT 'Doanh so ky 2 dau'
						--Doanh so ky 2 dau
						SELECT @DoanhSoKyHaiDau = rnhttct.DoanhSoKyHaiDau
							,@ListHopdongChiTietIDNhan = rnhttct.HopDongChiTietREF
						FROM RptNhanHangThongTinChiTiet rnhttct
						WHERE rnhttct.DmNhanHangREF = @DmNhanHang
						AND rnhttct.HopDongREF = @HopDongFK
						AND rnhttct.DmSanPhamREF = @DmSanPhamREF
						AND rnhttct.DmKenhREF = @DmKenhREF
						AND convert(date,rnhttct.NgayThucHien) = @NgayDanhSoHopDong
						
						
						SET @DoanhSoKyHaiDau = ISNULL(@DoanhSoKyHaiDau,0)
						SET @DoanhSoKyHaiDau = @DoanhSoKyHaiDau + (@ThanhTien/@SoLuongNhan)
						SET @ListHopdongChiTietIDNhan = isnull(@ListHopdongChiTietIDNhan,'') + ',' + CONVERT(NVARCHAR(50), @HopDongChiTietID)
						--PRINT 'ten nhan hang'
						--Get Ten Nhan hang
						SELECT @TenNhanHang = dnh.TenNhanHang
						, @DmNganhHang = dnh.DmNghanhHangREF
						FROM DmNhanHang dnh
						WHERE dnh.DmNhanHangID = @DmNhanHang
						
						SET @TenNhanHang = ISNULL(@TenNhanHang,'')
						
						--PRINT '@CheckIsExist:' + CONVERT(NVARCHAR(50),@DmKhachHangREF)
						IF(@CheckIsExist = 0)
						BEGIN
							--Get Hinh thuc ky
							--3 = Hinh thuc dai ly
							--khach 3 la hinh thuc truc tiep
							SELECT @TenHinhThucKy = B.TenHinhThuc FROM 
							(
								SELECT distinct	(CASE WHEN khf.Loai = 3 THEN N'Ð?i lý'
											ELSE N'Tr?c ti?p'
						      			 END
						      			 ) TenHinhThuc
								FROM KhachHangFull khf
								WHERE khf.KhachHangID = @DmKhachHangREF
							)B
							
							--PRINT 'ten nhom nganh:' + CONVERT(NVARCHAR(50),@DmNganhHang)
							--Get ten nhom nganh
							SET @TenNhomNganh = 
							(SELECT
								stuff(
								(
								select cast(',' as varchar(max)) + U.TenNghanhHang
								from DmNghanhHang U
								WHERE U.DmNghanhHangID IN (SELECT dbo.FormatString(item) FROM dbo.ArrayToTable(dbo.Array(@DmNganhHang,',')))
								order by U.TenNghanhHang
								for xml path('') 
								), 1, 1, '') AS TenNganhHang
							)
							SET @DmNganhHang = ISNULL(@DmNganhHang,'')
							SET @TenNhomNganh = ISNULL(@TenNhomNganh,'')
							--PRINT 'khach hang' + CONVERT(NVARCHAR(50),@DmKhachHangREF)
													
							--Get ten khach hang so huu
							SELECT @TenKhachHangSoHuu = khf.TenKhachHang 
							FROM KhachHangFull khf
							WHERE khf.KhachHangID = @DmKhachHangREF
							
							set @DoanhSoThucChay = 0
							
							INSERT INTO [dbo].[RptNhanHangThongTinChiTiet]
						   ([DmNhanHangREF],[TenNhanHang],[DmNganhHangREF],[TenNganhHang],[DmNhanSuREF],[TenNhanSu]
						   ,[SoHopDong],[HopDongREF],[DmKhachHangREF],[TenKhachHang],[HinhThucKy],[DmHinhThucSanPhamREF]
						   ,[HinhThucSanPham],[DmSanPhamREF],[TenSanPham],[DmKenhREF],[TenKenh],[DoanhSoKyHaiDau],[DoanhSoThucChay]
						   ,[TongDoanhSoKyHaiDau],[TongDoanhSoThucChay],[NgayThucHien],[HopDongChiTietREF]
						   ,[CreatedBy],[CreatedAt],[LastModifiedBy],[LastModifiedAt],[RecordStatus],[DeletedStatus])
					 VALUES
						   (@DmNhanHang,@TenNhanHang,@DmNganhHang,@TenNhomNganh,@NhanVienREF,@TenNhanVien
						   ,@SoHopDong,@HopDongFK,@DmKhachHangREF,@TenKhachHang,@TenHinhThucKy,@DmHinhThucSP
						   ,@TenHinhThucSP,@DmSanPhamREF,@TenSanPham,@DmKenhREF,@Kenh,@DoanhSoKyHaiDau,@DoanhSoThucChay
						   ,@DoanhSoKyHaiDau,@DoanhSoThucChay,@NgayDanhSoHopDong,@HopDongChiTietID
						   ,'ABM',GETDATE(),'ABM',GETDATE() ,0,0)

						END
						ELSE
							BEGIN
								UPDATE RptNhanHangThongTinChiTiet
								SET
									-- RptNhanHangThongTinChiTietID = ? -- this column value is auto-generated
									DoanhSoKyHaiDau = @DoanhSoKyHaiDau,
									TongDoanhSoKyHaiDau = @DoanhSoKyHaiDau,
									HopDongChiTietREF = @ListHopdongChiTietIDNhan,
									LastModifiedBy = 'ABM',
									LastModifiedAt = GETDATE()
								WHERE DmNhanHangREF = @DmNhanHang
									AND HopDongREF = @HopDongFK
									AND DmSanPhamREF = @DmSanPhamREF
									AND DmKenhREF = @DmKenhREF
									AND convert(date,NgayThucHien) = @NgayDanhSoHopDong 	
							END
						----
					END
					
				FETCH NEXT FROM Record_Cursor_ds into 
				@SoHopDong, @HopDongFK, @TenNhanVien, @NhanVienREF, @TenKhachHang, @DmKhachHangREF, @NgayDanhSoHopDong, @HopDongChiTietID
				, @LstTenNhanHang, @DmLstNhanHang, @DmHinhThucSP, @TenHinhThucSP
				, @DmNhomWebsiteREF, @TenNhomWebsite, @TenWebsite, @DmWebsiteREF, @DmSanPhamREF, @TenSanPham, @ThanhTien
				END
			CLOSE Record_Cursor_ds
			DEALLOCATE Record_Cursor_ds
		--THUC HIEN CAP NHAT DOANH SO CHO CAC TABLE KHAC
		--2. HINH THUC KY
		EXEC [dbo].[Rpt_InsertNhanHangHinhThucKyByNhanHangID] @DmNhanHang
		--3. Tinh gia tri cho table RptNhanHangHinhThucKy
		EXEC [dbo].[Rpt_InsertNhanHangKhachHangKyByNhanHangID] @DmNhanHang
		--4. Tính gia tri cho table RptNhanHangKhachHangKy
		EXEC [dbo].[Rpt_InsertNhanHangNhanSuByNhanHangID] @DmNhanHang
		--5. Tinh gia tri cho table RptNhanHangKenh
		EXEC [dbo].[Rpt_InsertNhanHangKenhByNhanHangID] @DmNhanHang
		--6. Tinh gia tri cho table RptNhanHangNhanSu
		EXEC [dbo].[Rpt_InsertNhanHangNhanSuByNhanHangID] @DmNhanHang
		--7. Tinh gia tri cho table RptNhanHangSanPham
		EXEC [dbo].[Rpt_InsertNhanHangSanPhamByNhanHangID]	@DmNhanHang
		FETCH NEXT FROM Record_Cursor INTO @DmNhanHang 
	END

	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor
	--SELECT '1'
END

--EXEC [dbo].[Rpt_UpdateNhanHangWhenDSNhanHangThayDoi] '2013-01-01'

```
