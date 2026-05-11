# Stored Procedure: `ThucChayDaTinh_UpdateGiaTriThayDoi_BoxAppSSV`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-24 16:20:00.907000
- **Ngày sửa cuối**: 2015-01-14 10:42:15.573000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmHinhThucQuangCao` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-06-24
-- Description:	<Description,,>
-- =============================================

-- EXEC ThucChayDaTinh_UpdateGiaTriThayDoi_BoxAppSSV '2014-08-20', '2014-08-20', 375, 26
CREATE PROCEDURE [dbo].[ThucChayDaTinh_UpdateGiaTriThayDoi_BoxAppSSV] 
	-- Add the parameters for the stored procedure here
	@StartDate			DATETIME,
	@EndDate			DATETIME,
	@DmSanPhamREF		INT,
	@DmHinhThucQuangCao INT
AS
BEGIN
	DECLARE	@HopDongREF INT,
			@SoHopDong NVARCHAR(50),
			@HopDongChiTietID INT
			
	DECLARE @SoLuongDotChayHD INT,
			@ThanhTienHDCT FLOAT, 
			@DmWebsiteREF INT, 
			@TenWebsite		NVARCHAR(50),
			@TenSanPham		NVARCHAR(50) = 'Box App'
			
	DECLARE @NgayThucHien DATETIME, 
			@count_HDCT INT, 
			@SoLuongThucChayBF INT
			
	DECLARE @SoLuongCurrent	INT,
			@DonGiaCurrent	INT,
			@ChietKhauCurrent	INT,
			@ThanhTienCurrent	FLOAT,
			@DeltaValue			FLOAT,
			@GiaTriThayDoiByWebsite	FLOAT
			
	DECLARE @SoLuongOld	INT,
			@DonGiaOld	INT,
			@ChietKhauOld	INT,
			@ThanhTienOld	FLOAT	
	
	DECLARE @NgayThayDoiMax	DATETIME,
			@HopDongThayDoiREFMax INT	
	
	DECLARE @Count INT,
			@ThucChayTheoSite FLOAT,
			@Tyle				FLOAT,
			@TongTienThucChay	FLOAT
		
	DECLARE @NoiDungLog			NVARCHAR(MAX),
			@GhiChu				NVARCHAR(MAX)
			
	DECLARE @GiaTriHopDong		FLOAT,
			@GiaTriThucChay	FLOAT
			
	set @NgayThucHien = @StartDate

	WHILE(@NgayThucHien <= @EndDate)
	BEGIN
		-- check xem gia tri thuc chay da vuot qua gia tri hop dong hay chua
		PRINT CONVERT(NVARCHAR(20),@NgayThucHien)
		SET @count_HDCT = 0
		SET @SoLuongThucChayBF = 0
		
		DECLARE Record_Cursor CURSOR FOR 
	    
		SELECT distinct  hd.HopDongID, hd.SoHopDong, hdcttd.HopDongChiTietREF, hdcttd.DmSanPhamREF
		FROM HopDong hd
			INNER JOIN HopDongThayDoi hdtd ON hd.HopDongID = hdtd.HopDongFK AND hd.TrangThaiHopDong <> 3
			INNER JOIN HopDongChiTietThayDoi hdcttd ON hdtd.HopDongFK = hdcttd.HopDongFK
				AND hdcttd.DmSanPhamREF = @DmSanPhamREF 
				AND hdtd.LoaiThayDoi = 1
				AND hdcttd.DmLoaiREF = @DmHinhThucQuangCao 
		WHERE CONVERT(Date,hdtd.NgayThayDoi) = @NgayThucHien
			--AND hd.SoHopDong = 'SH020614'
		ORDER BY hd.SoHopDong	
		
		OPEN Record_Cursor

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong, @HopDongChiTietID, @DmSanPhamREF
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				PRINT '@SoHopDong: ' + CONVERT(NVARCHAR(50), @SoHopDong);
				PRINT '@HopDongREF: ' + CONVERT(NVARCHAR(50), @HopDongREF);
				
				SELECT @GiaTriHopDong = SUM(ThanhTien)
				FROM HopDongChiTiet AS hdct
				WHERE hdct.HopDongFK = @HopDongREF
					AND hdct.DeletedStatus = 0
					AND hdct.DmSanPhamREF = @DmSanPhamREF
					AND hdct.DmLoaiREF <> 13
					--AND (hdct.DmLoaiREF = @DmHinhThucQuangCao
					--		OR hdct.TenViTri IN ('300x250','300x385')) 
							
				SELECT @GiaTriThucChay = ISNULL(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi),0)
				FROM ThucChayDaTinh AS tcdt
				WHERE tcdt.HopDongID = @HopDongREF
					AND tcdt.DmSanPhamREF = @DmSanPhamREF
					AND tcdt.DmHinhThucQuangCao <> 13
					--AND (tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCao
					--		OR tcdt.TenViTri IN ('300x250','300x385'))
					AND tcdt.NgayThucHien BETWEEN '2014-01-01' AND @NgayThucHien 
					
				IF @GiaTriHopDong < @GiaTriThucChay
				BEGIN
					SELECT 
						@SoLuongCurrent = ISNULL(SUM(SoLuong),0),
						@DonGiaCurrent = ISNULL(SUM(hdct.DonGia),0),
						@ChietKhauCurrent = ISNULL(SUM(hdct.ChietKhau),0),
						@ThanhTienCurrent = ISNULL(SUM(hdct.ThanhTien),0)
					FROM HopDong hd
						INNER JOIN HopDongChiTiet AS hdct ON hd.HopDongID = hdct.HopDongFK
					WHERE 
						hd.HopDongID = @HopDongREF
						AND hdct.HopDongChiTietID = @HopDongChiTietID
						AND hdct.DmSanPhamREF = @DmSanPhamREF
						--AND (hdct.DmLoaiREF = @DmHinhThucQuangCao
						--		OR hdct.TenViTri IN ('300x250','300x385')) 
						AND hdct.DeletedStatus = 0
						AND hdct.IsKhuyenMai <> 1
						AND hdct.DmLoaiREF <> 13
						
					PRINT '@SoLuongCurrent: ' + CONVERT(NVARCHAR(50), @SoLuongCurrent);
					PRINT '@DonGiaCurrent: ' + CONVERT(NVARCHAR(50), @DonGiaCurrent);
					PRINT '@ChietKhauCurrent: ' + CONVERT(NVARCHAR(50), @ChietKhauCurrent);
					PRINT '@ThanhTienCurrent: ' + CONVERT(NVARCHAR(50), @ThanhTienCurrent);
						
					SELECT 
						@NgayThayDoiMax = convert(date,MAX(B.NgayThayDoi)),
						@HopDongThayDoiREFMax = MAX(B.HopDongThayDoiID)
					FROM dbo.HopDongChiTietThayDoi A
					INNER JOIN dbo.HopDongThayDoi B ON A.HopDongFK = B.HopDongFK
					WHERE 
						A.DeletedStatus <> 1 AND 
						B.DeletedStatus <> 1 AND
						A.HopDongFK = @HopDongREF
						AND A.DmSanPhamREF = @DmSanPhamREF
						--AND (A.DmLoaiREF = @DmHinhThucQuangCao
						--		OR A.TenViTri IN ('300x250','300x385')) 
						AND A.IsKhuyenMai <> 1
						
					PRINT '@NgayThayDoiMax: ' + CONVERT(NVARCHAR(50), @NgayThayDoiMax);
					PRINT '@HopDongThayDoiREFMax: ' + CONVERT(NVARCHAR(50), @HopDongThayDoiREFMax);
					
					SELECT 
						@SoLuongOld = ISNULL(SUM(SoLuong),0),
						@DonGiaOld = ISNULL(SUM(A.DonGia),0),
						@ChietKhauOld = ISNULL(SUM(A.ChietKhau),0),
						@ThanhTienOld = ISNULL(SUM(A.ThanhTien),0)
					FROM dbo.HopDongChiTietThayDoi A
					WHERE 
						A.DeletedStatus <> 1 AND 
						A.HopDongFK = @HopDongREF
						AND A.DmSanPhamREF = @DmSanPhamREF
						--AND (A.DmLoaiREF = @DmHinhthucQuangCao
						--		OR A.TenViTri IN ('300x250','300x385')) 
						AND A.IsKhuyenMai <> 1
						AND A.HopDongThayDoiREF = @HopDongThayDoiREFMax
						
					PRINT '@SoLuongOld: ' + CONVERT(NVARCHAR(50), @SoLuongOld);
					PRINT '@DonGiaOld: ' + CONVERT(NVARCHAR(50), @DonGiaOld);
					PRINT '@ChietKhauOld: ' + CONVERT(NVARCHAR(50), @ChietKhauOld);
					PRINT '@ThanhTienOld: ' + CONVERT(NVARCHAR(50), @ThanhTienOld);
					
					IF @ThanhTienCurrent <> @ThanhTienOld
					BEGIN
						PRINT 'Change***';
						
						SET @NoiDungLog = N'Giá trị thay đổi: - PhanBoID: ' + CONVERT(NVARCHAR(50),@HopDongChiTietID) + ' - ';
						SET @GhiChu		= '';
						
						IF @SoLuongOld <> @SoLuongCurrent
							SET @NoiDungLog += N'Thay đổi số lượng - Trước: ' + CONVERT(NVARCHAR(50),@SoLuongOld) + N' - Sau: ' + CONVERT(NVARCHAR(50),@SoLuongCurrent) + '; ';
							
						IF @DonGiaOld <> @DonGiaCurrent 
							SET @NoiDungLog += N'Thay đổi đơn giá - Trước: ' + CONVERT(NVARCHAR(50),@DonGiaOld) + N' - Sau: ' + CONVERT(NVARCHAR(50),@DonGiaCurrent) + '; ';
							
						IF @ChietKhauOld <> @ChietKhauCurrent
							SET @NoiDungLog += N'Thay đổi chiết khấu - Trước: ' + CONVERT(NVARCHAR(50),@ChietKhauOld) + N' - Sau: ' + CONVERT(NVARCHAR(50),@ChietKhauCurrent) + '; ';
						
						--SET @DeltaValue = ISNULL((@ThanhTienCurrent - @ThanhTienOld),0);
						--PRINT '@DeltaValue: ' + CONVERT(NVARCHAR(50), @DeltaValue);
						
						-- check neu ton tai hop dong chi tiet id trong bang thuc chay da tinh 
						IF EXISTS(SELECT HopDongChiTietREF 
								  FROM ThucChayDaTinh AS tcdt 
								  WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
									AND tcdt.NgayThucHien BETWEEN '2014-01-01' AND @NgayThucHien)
						BEGIN
							PRINT 'Ton tai phan bo Id: 1';
							
							
							SELECT 
								@Count = COUNT(DISTINCT DmWebsiteREF),
								@TongTienThucChay = SUM(ISNULL(ThanhTienSauTrietKhauThucChay,0) + ISNULL(GiaTriThayDoi,0))
							FROM ThucChayDaTinh AS tcdt
							WHERE tcdt.HopDongID = @HopDongREF 
								AND tcdt.HopDongChiTietREF = @HopDongChiTietID
								AND tcdt.DmSanPhamREF = @DmSanPhamREF
								--AND (tcdt.DmHinhThucQuangCao = @DmHinhthucQuangCao
								--		OR tcdt.TenViTri IN ('300x250','300x385')) 
								AND tcdt.NgayThucHien <= @NgayThucHien;
			
							PRINT 'SoLuongWebsite: ' + CONVERT(NVARCHAR(50),@Count);						
							PRINT '@TongTienThucChay: ' + CONVERT(NVARCHAR(50),@TongTienThucChay);
							
							SET @DeltaValue = (@ThanhTienCurrent - @TongTienThucChay);
							PRINT '@DeltaValue: ' + CONVERT(NVARCHAR(50), @DeltaValue);
							
							-- Insert Log gia tri thay doi
							PRINT 'Log: ' + @NoiDungLog;
							EXEC dbo.ThucChay_LogNNTinhGiaTriThayDoi_Insert
								@HopDongREF
								,@SoHopDong
								,@HopDongChiTietID
								,@DmSanPhamREF
								,@DmWebsiteREF
								,@NgayThucHien
								,@DeltaValue
								,@DonGiaCurrent
								,@SoLuongCurrent
								,@DonGiaOld
								,@SoLuongOld
								,@NoiDungLog
								,'HopDongChiTiet_BoxAppSSV'
								,@GhiChu
								
							DECLARE td_cursor CURSOR FOR
							SELECT DISTINCT DmWebsiteREF, TenWebsite
							FROM ThucChayDaTinh AS tcdt
							WHERE tcdt.HopDongID = @HopDongREF 
								AND tcdt.HopDongChiTietREF = @HopDongChiTietID
								AND tcdt.DmSanPhamREF = @DmSanPhamREF
								--AND (tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCao
								--		OR TenViTri IN ('300x250','300x385')) 
								AND tcdt.NgayThucHien <= @NgayThucHien
						END
						ELSE
						BEGIN
							PRINT 'Ton tai phan bo Id: 0';
							SELECT 
								@Count = COUNT(DISTINCT DmWebsiteREF),
								@TongTienThucChay = SUM(ISNULL(ThanhTienSauTrietKhauThucChay,0) + ISNULL(GiaTriThayDoi,0))
							FROM ThucChayDaTinh AS tcdt
							WHERE tcdt.HopDongID = @HopDongREF 
								AND tcdt.DmSanPhamREF = @DmSanPhamREF
								--AND (tcdt.DmHinhThucQuangCao = @DmHinhthucQuangCao
								--		OR tcdt.TenViTri IN ('300x250','300x385')) 
								AND tcdt.NgayThucHien <= @NgayThucHien;
			
							PRINT 'SoLuongWebsite: ' + CONVERT(NVARCHAR(50),@Count);						
							PRINT '@TongTienThucChay: ' + CONVERT(NVARCHAR(50),@TongTienThucChay);
							
							SET @DeltaValue = (@ThanhTienCurrent - @TongTienThucChay);
							PRINT '@DeltaValue: ' + CONVERT(NVARCHAR(50), @DeltaValue);
							
							-- Insert Log gia tri thay doi
							PRINT 'Log: ' + @NoiDungLog;
							EXEC dbo.ThucChay_LogNNTinhGiaTriThayDoi_Insert
								@HopDongREF
								,@SoHopDong
								,@HopDongChiTietID
								,@DmSanPhamREF
								,@DmWebsiteREF
								,@NgayThucHien
								,@DeltaValue
								,@DonGiaCurrent
								,@SoLuongCurrent
								,@DonGiaOld
								,@SoLuongOld
								,@NoiDungLog
								,'HopDongChiTiet_BoxAppSSV'
								,@GhiChu
							
							DECLARE td_cursor CURSOR FOR
							SELECT DISTINCT DmWebsiteREF, TenWebsite
							FROM ThucChayDaTinh AS tcdt
							WHERE tcdt.HopDongID = @HopDongREF 
								AND tcdt.DmSanPhamREF = @DmSanPhamREF
								--AND (tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCao
								--		OR tcdt.TenViTri IN ('300x250','300x385')) 
								AND tcdt.NgayThucHien <= @NgayThucHien
						END
		
						OPEN td_cursor
						
						FETCH NEXT FROM td_cursor INTO @DmWebsiteREF, @TenWebsite
						WHILE @@FETCH_STATUS = 0
						BEGIN
							SELECT @ThucChayTheoSite = SUM(ISNULL(ThanhTienSauTrietKhauThucChay,0) + ISNULL(GiaTriThayDoi,0))
							FROM ThucChayDaTinh AS tcdt
							WHERE tcdt.HopDongID = @HopDongREF
								AND tcdt.DmSanPhamREF = @DmSanPhamREF
								AND tcdt.DmWebsiteREF = @DmWebsiteREF
								--AND (tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCao
								--		OR tcdt.TenViTri IN ('300x250','300x385')) 
							
							SET @TyLe = (@ThucChayTheoSite/@TongTienThucChay*100);
							SET @GiaTriThayDoiByWebsite = ((@DeltaValue*@TyLe)/100);
							
							PRINT 'Website: ' + @TenWebsite;
							PRINT 'TyLe: ' + CONVERT(NVARCHAR(50),@TyLe);
							PRINT 'GiaTriThayDoiByWebsite: ' + CONVERT(NVARCHAR(50),@GiaTriThayDoiByWebsite);
							
							IF @GiaTriThayDoiByWebsite <> 0
							BEGIN
								PRINT '@DeltaValue: ' + CONVERT(NVARCHAR(50),@DeltaValue); 
								PRINT '@TyLe: ' + CONVERT(NVARCHAR(50),@TyLe); 
								PRINT '@GTTD: ' + CONVERT(NVARCHAR(50),(@DeltaValue*@TyLe)/100); 
								
								EXEC dbo.ThucChayDaTinh_BoxappSSV_InsertGiaTriThayDoi
										@NgayThucHien				= @NgayThucHien
										,@HopDongId					= @HopDongREF
										,@PhanBoId					= @HopDongChiTietID
										,@SanPhamId					= @DmSanPhamREF
										,@TenSanPham				= @TenSanPham
										,@WebsiteId					= @DmWebsiteREF
										,@TenWebsite				= @TenWebsite
										,@DonViTinh					= 'VIEW'
										,@SoLuongThayDoiThucChay	= 0
										,@GiaTriThayDoiThucChay		= @GiaTriThayDoiByWebsite
										,@SoLuongThayDoiKhuyenMai	= 0
										,@GiaTriThayDoiKhuyenMai	= 0
							END
			
							FETCH NEXT FROM td_cursor INTO @DmWebsiteREF, @TenWebsite
						END
						
						CLOSE td_cursor;
						DEALLOCATE td_cursor;
					END
				END
				
			FETCH NEXT FROM Record_Cursor into @HopDongREF, @SoHopDong, @HopDongChiTietID, @DmSanPhamREF
			END
		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor
				
		-- Check xem co hop dong huy hay khong
		DECLARE @HopDongHuyId	int,
				@SoHopDongHuy	nvarchar(50),
				@PhanBoHuyId	int,
				@WebsiteHuyId		int,
				@TenWebsiteHuy		nvarchar(50),
				@SoLuongThayDoiThucChayBySite	bigint,
				@ThanhTienThayDoiThucChayBySite	float
		
		DECLARE hd_cursor CURSOR FOR
		
		SELECT hd.HopDongID, hd.SoHopDong, hdct.HopDongChiTietID
		FROM HopDongThayDoi AS hdtd
			INNER JOIN HopDong AS hd ON hdtd.HopDongFK = hd.HopDongID
			INNER JOIN HopDongChiTiet AS hdct ON hdct.HopDongFK = hd.HopDongID
		WHERE hd.TrangThaiHopDong = 3
			AND hdtd.LoaiThayDoi = 0
			AND CONVERT(date,hdtd.NgayThayDoi) = @NgayThucHien
			AND hdct.DmSanPhamREF IN (375)
		
		OPEN hd_cursor
		FETCH NEXT FROM hd_cursor INTO @HopDongHuyId, @SoHopDongHuy, @PhanBoHuyId
		
		WHILE @@FETCH_STATUS = 0
		BEGIN
			PRINT 'Hop Dong Huy';
			-- Tinh tien thuc chay theo tung website theo phan bo id
			DECLARE website_cursor CURSOR FOR
			SELECT A.DmWebsiteREF, A.TenWebsite,
				SUM(ISNULL(ThanhTienSauTrietKhauThucChay,0) + ISNULL(GiaTriThayDoi,0)) as GiaTriThayDoiThucChayBySite
			FROM ThucChayDaTinh A
			WHERE A.HopDongID = @HopDongHuyID
				and A.HopDongChiTietREF = @PhanBoHuyId
			GROUP BY
				A.DmWebsiteREF, A.TenWebsite
				
			OPEN website_cursor
			
			FETCH NEXT FROM website_cursor INTO @WebsiteHuyId, @TenWebsiteHuy, @ThanhTienThayDoiThucChayBySite
			WHILE @@FETCH_STATUS = 0
			BEGIN
				SET @ThanhTienThayDoiThucChayBySite = (0 - @ThanhTienThayDoiThucChayBySite);
				
				PRINT '@ThanhTienThayDoiThucChayBySite: ' + cast(@ThanhTienThayDoiThucChayBySite as nvarchar(50))
				-- Insert gia tri thay doi
				EXEC dbo.ThucChayDaTinh_BoxappSSV_InsertGiaTriThayDoi
					@NgayThucHien				= @NgayThucHien
					,@HopDongId					= @HopDongHuyId
					,@PhanBoId					= @PhanBoHuyId
					,@SanPhamId					= @DmSanPhamREF
					,@TenSanPham				= @TenSanPham
					,@WebsiteId					= @WebsiteHuyId
					,@TenWebsite				= @TenWebsiteHuy
					,@DonViTinh					= 'VIEW'
					,@SoLuongThayDoiThucChay	= 0
					,@GiaTriThayDoiThucChay		= @ThanhTienThayDoiThucChayBySite
					,@SoLuongThayDoiKhuyenMai	= 0
					,@GiaTriThayDoiKhuyenMai	= 0
					
				-- Insert Log gia tri thay doi
				PRINT 'Log: ' + @NoiDungLog;
				EXEC dbo.ThucChay_LogNNTinhGiaTriThayDoi_Insert
					@HopDongHuyId
					,@SoHopDongHuy
					,@PhanBoHuyId
					,@DmSanPhamREF
					,@WebsiteHuyId
					,@NgayThucHien
					,@ThanhTienThayDoiThucChayBySite
					,0
					,0
					,0
					,0
					,'Update Gia tri thay doi cho hop dong Huy'
					,'HopDongChiTiet_BoxAppSSV_HopDongHuy'
					,''
				
				FETCH NEXT FROM website_cursor INTO @WebsiteHuyId, @TenWebsiteHuy, @ThanhTienThayDoiThucChayBySite	
			END
			CLOSE website_cursor;
			DEALLOCATE website_cursor;
			
			FETCH NEXT FROM hd_cursor INTO @HopDongHuyId, @SoHopDongHuy, @PhanBoHuyId						
		END
		
		CLOSE hd_cursor;
		DEALLOCATE hd_cursor; 
						
		SET @NgayThucHien = dateadd(d,1,@NgayThucHien)
	END
	SELECT 2
END


/****** Object:  StoredProcedure [dbo].[ThucChay_TotalSumByFillterCondition]    Script Date: 10/24/2014 10:08:14 ******/
SET ANSI_NULLS ON

```
