# Stored Procedure: `ThucChayDaTinhAdmarket_UpdateGiaTriThayDoiByContractNo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-28 16:01:26.310000
- **Ngày sửa cuối**: 2015-03-27 10:19:53.040000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ContractNo` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-08-28
-- Description:	Update gia tri thay doi by so hop dong
-- =============================================
-- 
-- EXEC dbo.ThucChayDaTinhAdmarket_UpdateGiaTriThayDoiByContractNo '2015-03-24', 'QC920914'
CREATE PROCEDURE [dbo].[ThucChayDaTinhAdmarket_UpdateGiaTriThayDoiByContractNo]
	-- Add the parameters for the stored procedure here
	@NgayThucHien			DATETIME,
	@ContractNo			NVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	DECLARE	@HopDongREF INT,
			@SoHopDong NVARCHAR(50),
			@HopDongChiTietID INT,
			@DonViTinh			NVARCHAR(50),
			@account			NVARCHAR(50),
			@DmViTriREF			INT,
			@TenViTri			NVARCHAR(50)
			
	DECLARE @SoLuongDotChayHD INT,
			@ThanhTienHDCT FLOAT, 
			@DmSanPhamREF	INT,
			@TenSanPham		NVARCHAR(50)
			
	DECLARE 
			@count_HDCT INT, 
			@SoLuongThucChayBF INT
			
	DECLARE @SoLuongCurrent	INT,
			@DonGiaCurrent	INT,
			@ChietKhauCurrent	INT,
			@ThanhTienCurrent	FLOAT,
			@DeltaValue			FLOAT,
			@GiaTriThayDoiByWebsite	FLOAT,
			@GiaTriThayDoi		FLOAT = 0,
			@GiaTriThayDoiByViTri	FLOAT = 0			
			
	DECLARE @SoLuongOld	INT,
			@DonGiaOld	INT,
			@ChietKhauOld	INT,
			@ThanhTienOld	FLOAT	
	
	DECLARE @NgayThayDoiMax	DATETIME,
			@HopDongThayDoiREFMax INT	
	
	DECLARE @Count INT,
			@ThucChayTheoSite FLOAT,
			@Tyle				FLOAT,
			@TongTienThucChay	FLOAT,
			@ThanhTienThucChayByViTri	FLOAT = 0,
			@TyLeByViTri			FLOAT = 0,
			@ThucChayAdXMobile	FLOAT = 0,
			@ThucChayAdxEcommerce FLOAT = 0,
			@ThucChayAdx		FLOAT = 0
		
	DECLARE @NoiDungLog			NVARCHAR(MAX),
			@GhiChu				NVARCHAR(MAX)
			
	DECLARE @GiaTriHopDong		FLOAT,
			@GiaTriThucChay	FLOAT
		
	DECLARE @MaHopDongId				INT,
			@TenMaHopDong			NVARCHAR(50)
			
	BEGIN
		-- check xem gia tri thuc chay da vuot qua gia tri hop dong hay chua
		
		
		PRINT CONVERT(NVARCHAR(20),@NgayThucHien)
		SET @count_HDCT = 0
		SET @SoLuongThucChayBF = 0
		
		DECLARE Record_Cursor CURSOR FOR 
	    
		SELECT distinct  hd.HopDongID, hd.SoHopDong, hdcttd.HopDongChiTietREF, hdcttd.DmSanPhamREF, hdcttd.TenSanPham, hdcttd.DonViTinh,
			hd.DmMaHopDongREF, hd.TenMaHopDong
		FROM HopDong hd
			INNER JOIN HopDongThayDoi hdtd ON hd.HopDongID = hdtd.HopDongFK 
			INNER JOIN HopDongChiTietThayDoi hdcttd ON hdtd.HopDongFK = hdcttd.HopDongFK		
		WHERE CONVERT(Date,hdtd.NgayThayDoi) = @NgayThucHien
			AND hd.TrangThaiHopDong <> 3
			AND hdtd.LoaiThayDoi <> 0
			AND hdcttd.DmSanPhamREF IN (144, 299, 337, 585) 
		ORDER BY hd.SoHopDong	
		
		OPEN Record_Cursor

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong, @HopDongChiTietID, @DmSanPhamREF, @TenSanPham, @DonViTinh, @MaHopDongId, @TenMaHopDong
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				SELECT @account = TK_Admarket
				FROM HopDongChiTiet AS hdct
				WHERE hdct.HopDongChiTietID = @HopDongChiTietID
				
				PRINT '1: Update gia tri thay doi';
				PRINT '@SoHopDong: ' + CONVERT(NVARCHAR(50), @SoHopDong);
				PRINT '@HopDongREF: ' + CONVERT(NVARCHAR(50), @HopDongREF);
				
				IF @DonViTinh = 'CPC'
					SET @DonViTinh = 'CLICK'
				ELSE IF @DonViTinh = 'CPM'
					SET @DonViTinh = 'VIEW'
				ELSE 
					SET @DonViTinh = 'CLICK'
				
				SELECT @GiaTriHopDong = SUM(ThanhTien)
				FROM HopDongChiTiet AS hdct
				WHERE hdct.HopDongChiTietID = @HopDongChiTietID
					AND hdct.DeletedStatus = 0
					AND hdct.DmSanPhamREF = @DmSanPhamREF
							
				SELECT @GiaTriThucChay = ISNULL(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi),0)
				FROM ThucChayDaTinhAdmarket AS tcdt
				WHERE tcdt.HopDongID = @HopDongREF
					AND tcdt.HopDongChiTietREF = @HopDongChiTietID
					AND tcdt.DmSanPhamREF = @DmSanPhamREF
					AND tcdt.NgayThucHien BETWEEN '2014-01-01' AND @NgayThucHien 				
					
				PRINT '@GiaTriHopDong: ' + CONVERT(NVARCHAR(50), @GiaTriHopDong);
				PRINT '@GiaTriThucChay: ' + CONVERT(NVARCHAR(50), @GiaTriThucChay);
					
				IF (@GiaTriHopDong < @GiaTriThucChay AND @GiaTriThucChay <> 0)
				BEGIN
					SET @GiaTriThayDoi = (@GiaTriHopDong - @GiaTriThucChay);
					
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
						AND hdct.DeletedStatus = 0
						AND hdct.IsKhuyenMai <> 1
						
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
						AND A.HopDongChiTietREF = @HopDongChiTietID
						AND A.DmSanPhamREF = @DmSanPhamREF
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
						
						SET @DeltaValue = ISNULL((@ThanhTienCurrent - @ThanhTienOld),0);
						PRINT '@DeltaValue: ' + CONVERT(NVARCHAR(50), @DeltaValue);
						PRINT '@@GiaTriThayDoi: ' + CONVERT(NVARCHAR(50), @GiaTriThayDoi);
							
						--PRINT 'Log: ' + @NoiDungLog;
						EXEC dbo.ThucChay_LogNNTinhGiaTriThayDoi_Insert
							@HopDongREF
							,@SoHopDong
							,@HopDongChiTietID
							,@DmSanPhamREF
							,0 --@DmWebsiteREF
							,@NgayThucHien
							,@DeltaValue
							,@DonGiaCurrent
							,@SoLuongCurrent
							,@DonGiaOld
							,@SoLuongOld
							,@NoiDungLog
							,'HopDongChiTiet_Admarket_SSV'
							,@GhiChu												
						
						DECLARE vitri_cursor CURSOR FOR
						SELECT DmViTriREF, TenViTri, SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)
						FROM ThucChayDaTinhAdmarket tcdt
						WHERE HopDongChiTietREF = @HopDongChiTietID
							AND tcdt.DmSanPhamREF = @DmSanPhamREF
							AND tcdt.NgayThucHien BETWEEN '2014-01-01' AND @NgayThucHien 
						GROUP BY
							DmViTriREF, TenViTri
						
						OPEN vitri_cursor
						
						FETCH NEXT FROM vitri_cursor INTO @DmViTriREF, @TenViTri, @ThanhTienThucChayByViTri
						WHILE @@FETCH_STATUS = 0
						BEGIN
							SET @TyLeByViTri = (@ThanhTienThucChayByViTri/@GiaTriThucChay)
							SET @GiaTriThayDoiByViTri = (@TyLeByViTri*@GiaTriThayDoi)
							
							IF @GiaTriThayDoiByViTri <> 0
							BEGIN
								--Insert gia tri thay doi
								EXEC dbo.ThucChayDaTinhAdmarket_Insert_GiaTriThayDoi
									@NgayThucHien				= @NgayThucHien
									,@HopDongId					= @HopDongREF
									,@SoHopDong					= @SoHopDong
									,@PhanBoId					= @HopDongChiTietID
									,@SanPhamId					= @DmSanPhamREF
									,@TenSanPham				= @TenSanPham
									,@DonViTinh					= @DonViTinh
									,@SoLuongThayDoiThucChay	= 0
									,@ThanhTienThayDoiThucChay	= @GiaTriThayDoiByViTri
									,@SoLuongThayDoiKhuyenMai	= 0
									,@ThanhTienThayDoiKhuyenMai	= 0
									,@GhiChu					= 'UPDATE_GTTD'
									,@DmViTriREF				= @DmViTriREF
									,@TenViTri					= @TenViTri
									
								-- Insert thuc chay online
								SET @GiaTriThayDoiByViTri = (@GiaTriThayDoiByViTri*(-1))
								
								SET @GhiChu = ('UPDATE_GTTD_' + @SoHopDong)
								-- Insert bu gia tri cho doi tuong khong co so hop dong
								EXEC dbo.ThucChayDaTinhAdmarket_InsertNoContractByProduct
									@DmSanPhamREF			= @DmSanPhamREF
									,@TenSanPham			= @TenSanPham
									,@DonViTinh				= @DonViTinh
									,@DmWebsiteREF			= 0
									,@TenWebsite			= ''
									,@NgayThucHien			= @NgayThucHien
									,@SoLuongThucChay		= 0
									,@SoLuongThhucChayKM	= 0
									,@ThanhTienThucChay		= 0
									,@ThanhTienThucChayKM	= 0
									,@DmMaHopDongREF		= @MaHopDongId
									,@TenMaHopDong			= @TenMaHopDong
									,@GhiChu				= @GhiChu
									,@GiaTriThayDoi			= @GiaTriThayDoiByViTri
									,@SoLuongThayDoi		= 0
									,@DmViTriREF			= @DmViTriREF
									,@TenViTri				= @TenViTri
									
								INSERT INTO ThucChayAdmarketOnline
								SELECT 
									NEWID()
									,@DmSanPhamREF
									,@TenSanPham -- AdX  CPC Admarket
									,@account
									,0 -- TotalViewOnline
									,0 -- TotalClickOnline
									,0 -- SoLuongThucChayOnline
									,@DonViTinh
									,@GiaTriThayDoiByViTri -- Tien online
									,0	-- KM online
									,@NgayThucHien
									,0 --IsNoiBo
									,'Vuot_Gia_Tri_Hop_Dong'
									,0
									,GETDATE()
									,'asd'
									,GETDATE()
									,'asd'
									,@DmViTriREF
									,@TenViTri
							END
							
							FETCH NEXT FROM vitri_cursor INTO @DmViTriREF, @TenViTri, @ThanhTienThucChayByViTri
						END
						
						CLOSE vitri_cursor
						DEALLOCATE vitri_cursor
	
						SET @GiaTriThayDoi = 0
					END
				END
				
			FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong, @HopDongChiTietID, @DmSanPhamREF, @TenSanPham, @DonViTinh, @MaHopDongId, @TenMaHopDong
			END
		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor
    END
	SELECT 2
END

```
