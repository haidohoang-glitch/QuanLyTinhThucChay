# Stored Procedure: `Rpt_Insert_Ky_NhanHangThongTinChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-24 09:36:15.830000
- **Ngày sửa cuối**: 2014-12-24 10:04:09.707000

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
--EXEC [dbo].[Rpt_Insert_Ky_NhanHangThongTinChiTiet] '2014-01-01'
CREATE  PROCEDURE [dbo].[Rpt_Insert_Ky_NhanHangThongTinChiTiet] 
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @SoHopDong NVARCHAR(50), @HopDongFK INT, @TenNhanVien NVARCHAR(100), @NhanVienREF INT
	DECLARE @TenKhachHang NVARCHAR(200), @DmKhachHangREF INT, @HopDongChiTietID INT, @LstTenNhanHang NVARCHAR(200), @DmLstNhanHang NVARCHAR(250)
	DECLARE @TenHinhThucSP NVARCHAR(100), @DmHinhThucSP INT, @DmNhomWebsiteREF INT, @TenNhomWebsite NVARCHAR(100), @DmWebsiteREF INT, @TenWebsite NVARCHAR(50)
	DECLARE @DmSanPhamREF INT, @TenSanPham NVARCHAR(100), @ThanhTien BIGINT, @TenHinhThucKy NVARCHAR(50)
	DECLARE @DmNhanHang INT, @TenNhanHang NVARCHAR(100), @DmNganhHang NVARCHAR(50), @TenNhomNganh NVARCHAR(200), @SoLuongNhan INT
	DECLARE @DoanhSoKyHaiDau BIGINT, @DoanhSoThucChay BIGINT, @TenKhachHangSoHuu NVARCHAR(200), @ListHopdongChiTietIDNhan NVARCHAR(50)
	DECLARE @DmKenhREF INT , @Kenh NVARCHAR(100), @CheckHopDongChiTietTcID INT, @TongThanhTienThucChayDT BIGINT, @CheckIsExist INT
	
	SET @NgayThucHien = CONVERT(date,@NgayThucHien)
	
	--DELETE THONG TIN NHAN HANG CHI TIET
	DELETE FROM dbo.Rpt_DoanhSoKy_NhanHangThongTinChiTiet
	WHERE convert(date,NgayThucHien) = @NgayThucHien
	
	--TINH DU LIEU THONG TIN NHAN HANG
	DECLARE Record_Cursor CURSOR FOR 
	SELECT hd.SoHopDong, hdct.HopDongFK, hd.TenNhanVien, hd.SysNhanVienREF
		, hd.TenKhachHang, hd.DmKhachHangREF, HDCT.HopDongChiTietID, hdct.NhanHang
		, hdct.DanhSachNhanHangREF, hdct.DmLoaiREF
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
			@SoHopDong, @HopDongFK, @TenNhanVien, @NhanVienREF, @TenKhachHang, @DmKhachHangREF, @HopDongChiTietID
			, @LstTenNhanHang, @DmLstNhanHang, @DmHinhThucSP, @TenHinhThucSP
			, @DmNhomWebsiteREF, @TenNhomWebsite, @TenWebsite, @DmWebsiteREF, @DmSanPhamREF, @TenSanPham, @ThanhTien
			
	WHILE @@FETCH_STATUS = 0
		BEGIN
			--PRINT @HopDongChiTietID
			SET @SoLuongNhan = 0
			SET @TongThanhTienThucChayDT = 0
			SET @CheckIsExist = 0
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
			SET @DoanhSoThucChay = 0
			--PRINT 'hopdongchitiet :' + CONVERT(NVARCHAR(50), @HopDongChiTietID)
			DECLARE Record_Cursor1 CURSOR FOR 
			SELECT dbo.FormatString(item) FROM dbo.ArrayToTable(dbo.Array(@DmLstNhanHang,','))
			OPEN Record_Cursor1
			FETCH NEXT FROM Record_Cursor1 into @DmNhanHang
			WHILE @@FETCH_STATUS = 0
				BEGIN
					SET @DoanhSoKyHaiDau = 0
					SET @DoanhSoThucChay = 0
					SET @TenNhanHang = ''
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
						  FROM Rpt_DoanhSoKy_NhanHangThongTinChiTiet rnhttct
						WHERE rnhttct.DmNhanHangREF = @DmNhanHang
						AND rnhttct.HopDongREF = @HopDongFK
						AND rnhttct.DmSanPhamREF = @DmSanPhamREF
						AND rnhttct.DmKenhREF = @DmKenhREF
						AND convert(date,rnhttct.NgayThucHien) = @NgayThucHien
						--PRINT 'Doanh so ky 2 dau'
						--Doanh so ky 2 dau
						SELECT @DoanhSoKyHaiDau = rnhttct.DoanhSoKy
							,@ListHopdongChiTietIDNhan = rnhttct.HopDongChiTietREF
						FROM Rpt_DoanhSoKy_NhanHangThongTinChiTiet rnhttct
						WHERE rnhttct.DmNhanHangREF = @DmNhanHang
						AND rnhttct.HopDongREF = @HopDongFK
						AND rnhttct.DmSanPhamREF = @DmSanPhamREF
						AND rnhttct.DmKenhREF = @DmKenhREF
						AND convert(date,rnhttct.NgayThucHien) = @NgayThucHien
						
						
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
						
						--PRINT 'Doanh so thuc chay'						
						--Doanh so thuc chay
						--Check HopDong co hopdongchitiet = 0 ?
						SELECT @CheckHopDongChiTietTcID = COUNT(A.HopDongChiTietREF) FROM 
						(
						SELECT DISTINCT tcdt.HopDongChiTietREF
							  FROM ThucChayDaTinh tcdt
							WHERE tcdt.HopDongID = @HopDongFK
							AND tcdt.HopDongChiTietREF = 0
							AND tcdt.DmSanPhamREF = @DmSanPhamREF 
							AND Convert(date,tcdt.NgayThucHien) = @NgayThucHien
						)A
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
							FROM KhachHangThongTinChung khf
							WHERE khf.KhachHangThongTinChungID = @DmKhachHangREF
							
							IF(@CheckHopDongChiTietTcID > 0)--Neu co hopdongchitiet = 0
								BEGIN
									SET @TongThanhTienThucChayDT = 0
									--SELECT @TongThanhTienThucChayDT = sum(tcdt.ThanhTienSauTrietKhauThucChay)
									--  FROM ThucChayDaTinh tcdt
									--WHERE tcdt.HopDongID = @HopDongFK
									--AND tcdt.DmSanPhamREF = @DmSanPhamREF 
									--AND convert(date,tcdt.NgayThucHien) = @NgayThucHien
									
									SET @DoanhSoThucChay = @DoanhSoThucChay + ISNULL(@TongThanhTienThucChayDT,0)/@SoLuongNhan
																	
								END
							ELSE
								BEGIN
									SET @TongThanhTienThucChayDT = 0
									--SELECT @TongThanhTienThucChayDT = sum(tcdt.ThanhTienSauTrietKhauThucChay)
									--  FROM ThucChayDaTinh tcdt
									--WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
									--AND tcdt.DmSanPhamREF = @DmSanPhamREF 
									--AND tcdt.NgayThucHien = @NgayThucHien
									
									SET @DoanhSoThucChay = @DoanhSoThucChay + ISNULL(@TongThanhTienThucChayDT,0)/@SoLuongNhan
								END
							
							INSERT INTO [dbo].[Rpt_DoanhSoKy_NhanHangThongTinChiTiet]
						   ([DmNhanHangREF],[TenNhanHang],[DmNganhHangREF],[TenNganhHang],[DmNhanSuREF],[TenNhanSu]
						   ,[SoHopDong],[HopDongREF],[DmKhachHangREF],[TenKhachHang],[HinhThucKy],[DmHinhThucSanPhamREF]
						   ,[HinhThucSanPham],[DmSanPhamREF],[TenSanPham],[DmKenhREF],[TenKenh],[DoanhSoKy],[DoanhSoThucChay]
						   ,[TongDoanhSoKy],[TongDoanhSoThucChay],[NgayThucHien],[HopDongChiTietREF]
						   ,[CreatedBy],[CreatedAt],[LastModifiedBy],[LastModifiedAt],[RecordStatus],[DeletedStatus])
					 VALUES
						   (@DmNhanHang,@TenNhanHang,@DmNganhHang,@TenNhomNganh,@NhanVienREF,@TenNhanVien
						   ,@SoHopDong,@HopDongFK,@DmKhachHangREF,@TenKhachHang,@TenHinhThucKy,@DmHinhThucSP
						   ,@TenHinhThucSP,@DmSanPhamREF,@TenSanPham,@DmKenhREF,@Kenh,@DoanhSoKyHaiDau,@DoanhSoThucChay
						   ,@DoanhSoKyHaiDau,@DoanhSoThucChay,@NgayThucHien,@HopDongChiTietID
						   ,'ABM',GETDATE(),'ABM',GETDATE() ,0,0)

						END
						ELSE
							BEGIN
								UPDATE Rpt_DoanhSoKy_NhanHangThongTinChiTiet
								SET
									-- RptNhanHangThongTinChiTietID = ? -- this column value is auto-generated
									DoanhSoKy = @DoanhSoKyHaiDau,
									TongDoanhSoKy = @DoanhSoKyHaiDau,
									HopDongChiTietREF = @ListHopdongChiTietIDNhan,
									LastModifiedBy = 'ABM',
									LastModifiedAt = GETDATE()
								WHERE DmNhanHangREF = @DmNhanHang
									AND HopDongREF = @HopDongFK
									AND DmSanPhamREF = @DmSanPhamREF
									AND DmKenhREF = @DmKenhREF
									AND convert(date,NgayThucHien) = @NgayThucHien 	
							END
						----
					END
					
				FETCH NEXT FROM Record_Cursor1 into @DmNhanHang
				END
			CLOSE Record_Cursor1
			DEALLOCATE Record_Cursor1
		
		FETCH NEXT FROM Record_Cursor into 
		@SoHopDong, @HopDongFK, @TenNhanVien, @NhanVienREF, @TenKhachHang, @DmKhachHangREF, @HopDongChiTietID
			, @LstTenNhanHang, @DmLstNhanHang, @DmHinhThucSP, @TenHinhThucSP
			, @DmNhomWebsiteREF, @TenNhomWebsite, @TenWebsite, @DmWebsiteREF, @DmSanPhamREF, @TenSanPham, @ThanhTien
	END

	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor
	--SELECT '1'
END

--EXEC [Rpt_InsertNhanHangThongTinChiTiet] '2013-01-01'

```
