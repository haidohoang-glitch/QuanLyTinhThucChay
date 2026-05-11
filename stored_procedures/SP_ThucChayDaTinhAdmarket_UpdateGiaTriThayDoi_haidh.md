# Stored Procedure: `ThucChayDaTinhAdmarket_UpdateGiaTriThayDoi_haidh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-10 16:07:03.460000
- **Ngày sửa cuối**: 2015-06-10 16:07:03.460000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-06-24
-- Description:	<Description,,>
-- =============================================
/*
 *	EXEC dbo.ThucChayDaTinhAdmarket_UpdateGiaTriThayDoi '2015-03-12'
 */
CREATE PROCEDURE [dbo].[ThucChayDaTinhAdmarket_UpdateGiaTriThayDoi_haidh] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien			DATETIME

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
			@DonGiaCurrent	BIGINT,
			@ChietKhauCurrent	FLOAT,
			@ThanhTienCurrent	FLOAT,
			@DeltaValue			FLOAT,
			@GiaTriThayDoiByWebsite	FLOAT,
			@GiaTriThayDoi		FLOAT = 0,
			@GiaTriThayDoiByViTri	FLOAT = 0			
			
	DECLARE @SoLuongOld	INT,
			@DonGiaOld	BIGINT,
			@ChietKhauOld	FLOAT,
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
			
	DECLARE @ThanhTienHopDongChiTiet		FLOAT,
			@GiaTriThucChay	FLOAT
		
	DECLARE @MaHopDongId				INT,
			@TenMaHopDong			NVARCHAR(50)
			
	DECLARE @UserBalance	FLOAT,
			@MaxValue					FLOAT
			
	BEGIN
		-- check xem gia tri thuc chay da vuot qua gia tri hop dong hay chua
		
		
		PRINT CONVERT(NVARCHAR(20),@NgayThucHien)
		SET @count_HDCT = 0
		SET @SoLuongThucChayBF = 0							
		
		DECLARE Record_Cursor CURSOR FOR 
	    
		SELECT
			A.HopDongID, A.SoHopDong, B.HopDongChiTietID, B.DmSanPhamREF, B.TenSanPham, B.DonViTinh,
			A.DmMaHopDongREF, A.TenMaHopDong,B.ThanhTien
		FROM HopDong A
			INNER JOIN HopDongChiTiet B ON B.HopDongFK = A.HopDongID
		WHERE 1=1
			AND A.TrangThaiHopDong <> 3
			AND B.DmSanPhamREF IN (144, 585, 628)
			AND CONVERT(DATE, B.LastModifiedAt) = @NgayThucHien

		OPEN Record_Cursor

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong, @HopDongChiTietID, @DmSanPhamREF, @TenSanPham, @DonViTinh, 
			@MaHopDongId, @TenMaHopDong,@ThanhTienHopDongChiTiet
			
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
					
				SELECT @GiaTriThucChay = ISNULL(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi),0)
				FROM ThucChayDaTinhAdmarket AS tcdt
				WHERE tcdt.HopDongID = @HopDongREF
					AND tcdt.HopDongChiTietREF = @HopDongChiTietID
					AND tcdt.DmSanPhamREF = @DmSanPhamREF
					AND tcdt.NgayThucHien BETWEEN '2014-01-01' AND @NgayThucHien 				
				
				SET @MaxValue = @ThanhTienHopDongChiTiet	

				PRINT '@ThanhTienHopDongChiTiet: ' + CONVERT(NVARCHAR(50), @ThanhTienHopDongChiTiet);
				PRINT '@GiaTriThucChay: ' + CONVERT(NVARCHAR(50), @GiaTriThucChay);
					
				IF (@MaxValue < @GiaTriThucChay AND @GiaTriThucChay <> 0)
				BEGIN
					SET @GiaTriThayDoi = (@MaxValue - @GiaTriThucChay);
					
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
					
					SELECT TOP 1
						@SoLuongOld = ISNULL(SoLuong,0),
						@DonGiaOld = ISNULL(A.DonGia,0),
						@ChietKhauOld = ISNULL(A.ChietKhau,0),
						@ThanhTienOld = ISNULL(A.ThanhTien,0)
					FROM dbo.HopDongChiTietLog A
					WHERE 
						A.DeletedStatus <> 1 AND 
						A.HopDongFK = @HopDongREF
						AND A.HopDongChiTietREF = @HopDongChiTietID
						AND A.DmSanPhamREF = @DmSanPhamREF
						AND A.IsKhuyenMai <> 1
						AND CONVERT(date,A.ThoiGianLog) < @NgayThucHien
					ORDER BY A.ThoiGianLog DESC					
						
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
							
							PRINT '@GiaTriThayDoiByViTri: ' + CONVERT(NVARCHAR(50), @GiaTriThayDoiByViTri);
							
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
				
			FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong, @HopDongChiTietID, @DmSanPhamREF, @TenSanPham, @DonViTinh, 
					@MaHopDongId, @TenMaHopDong,@ThanhTienHopDongChiTiet
			END
		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor
	END
	SELECT 2
END


```
