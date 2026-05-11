# Stored Procedure: `ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirmTcHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-05-24 13:49:31.363000
- **Ngày sửa cuối**: 2018-07-23 14:15:55.453000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@ThanhTienThucChayOnline` | `float(8)` | No |
| `@ThanhTienThucChayHopDongChiTiet` | `float(8)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@Tk` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*

EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirmTcHopDong]
	@NgayThucHien = '2018-07-20', 
	@HopDongID = 1005167,
	@HopDongChiTietID = 532045, 
	@ThanhTienThucChayOnline = 45454546 ,
	@ThanhTienThucChayHopDongChiTiet = 1449909,
	@GiaTriThayDoi = 1000545, 
	@DmSanPhamREF = 585, 
	@GhiChu= N'',
	@Tk = 'kiengiang1410'
*/
CREATE PROCEDURE [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirmTcHopDong]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME, 
	@HopDongID INT,
	@HopDongChiTietID INT, 
	@ThanhTienThucChayOnline FLOAT,
	@ThanhTienThucChayHopDongChiTiet FLOAT,
	@GiaTriThayDoi FLOAT, 
	@DmSanPhamREF INT, 
	@GhiChu nvarchar(200),
	@Tk NVARCHAR(50)
AS
BEGIN
	DECLARE @DonViTinh NVARCHAR(50),@DmWebsiteREF INT, @TenWebsite NVARCHAR(50),@SoLuongThucChay INT,@TenViTri nvarchar(50),@SoLuongThayDoi INT
	DECLARE @ThanhTienOnlineVitri FLOAT = 0, @ThanhTienThucChayHDCTVitri FLOAT = 0, @TiLeViTri_Adx FLOAT = 0, @DmViTriREF INT, @ThanhTienVitri_theoTile FLOAT = 0
	, @ThanhTienThucChayOnline_TK FLOAT = 0
     SET @SoLuongThucChay =0
     SET @SoLuongThayDoi =0
	 SET @DmWebsiteREF = 826
	 SET @TenWebsite = '(Blanks)'

	 IF @DmSanPhamREF = 144 
	 BEGIN
	     SET @TenViTri = 'CPC Admarket' 
			EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirm_DoiTruOnline]
			@NgayThucHien		= @NgayThucHien, 
			@HopDongID			= @HopDongID,
			@HopDongChiTietID	= @HopDongChiTietID, 
			@DmSanPhamREF		= @DmSanPhamREF, 
			@Tk					= @Tk,
			@DmViTriREF			= @DmViTriREF,
			@TenViTri			= @TenViTri,
			@DmWebsiteREF		= @DmWebsiteREF,
			@TenWebsite			= @TenWebsite,
			@GiaTriThayDoi		= @GiaTriThayDoi, 
			@GhiChu				= @GhiChu
	 END
	 ELSE IF  @DmSanPhamREF = 628
	 BEGIN
	      SET @TenViTri = '' 
		  EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirm_DoiTruOnline]
			@NgayThucHien		= @NgayThucHien, 
			@HopDongID			= @HopDongID,
			@HopDongChiTietID	= @HopDongChiTietID, 
			@DmSanPhamREF		= @DmSanPhamREF, 
			@Tk					= @Tk,
			@DmViTriREF			= @DmViTriREF,
			@TenViTri			= @TenViTri,
			@DmWebsiteREF		= @DmWebsiteREF,
			@TenWebsite			= @TenWebsite,
			@GiaTriThayDoi		= @GiaTriThayDoi, 
			@GhiChu				= @GhiChu
	 END
	 ELSE 
	 BEGIN
		IF (@GiaTriThayDoi <0)
		BEGIN

		    PRINT 'Gia tri thay doi <0'
			--1. ADX
			SET @DmViTriREF = 1 
			SET @TenViTri = 'ADX'
			SET @ThanhTienThucChayHDCTVitri = ISNULL((SELECT  SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhTienThucChay 
													FROM dbo.ThucChayDaTinhAdmarket
													WHERE TrangThaiHopDong <> 3 AND DmViTriREF = 1
													AND DmSanPhamREF = @DmSanPhamREF
													AND NgayThucHien <= @NgayThucHien
													AND HopDongChiTietREF = @HopDongChiTietID
												),0)

				SET @TiLeViTri_Adx = (CASE	WHEN @ThanhTienThucChayHDCTVitri = 0 THEN 0
											WHEN @ThanhTienThucChayHopDongChiTiet = 0 THEN 0
											ELSE @ThanhTienThucChayHDCTVitri/@ThanhTienThucChayHopDongChiTiet
										END)
				--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
				SET @ThanhTienVitri_theoTile = @GiaTriThayDoi*@TiLeViTri_Adx
				IF(@ThanhTienVitri_theoTile <> 0)
					EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirm_DoiTruOnline]
					@NgayThucHien		= @NgayThucHien, 
					@HopDongID			= @HopDongID,
					@HopDongChiTietID	= @HopDongChiTietID, 
					@DmSanPhamREF		= @DmSanPhamREF, 
					@Tk					= @Tk,
					@DmViTriREF			= @DmViTriREF,
					@TenViTri			= @TenViTri,
					@DmWebsiteREF		= @DmWebsiteREF,
					@TenWebsite			= @TenWebsite,
					@GiaTriThayDoi		= @ThanhTienVitri_theoTile, 
					@GhiChu				= @GhiChu

				--2. 'AdX Mobile' 
				SET @DmViTriREF = 2
				SET @TenViTri = 'AdX Mobile' 
				SET @ThanhTienThucChayHDCTVitri = ISNULL((
												SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhTienThucChay 
												FROM dbo.ThucChayDaTinhAdmarket
												WHERE TrangThaiHopDong <> 3 AND DmViTriREF = 2
												AND DmSanPhamREF = @DmSanPhamREF
												AND NgayThucHien <= @NgayThucHien
												AND HopDongChiTietREF = @HopDongChiTietID
												),0)
				SET @TiLeViTri_Adx = (CASE	WHEN @ThanhTienThucChayHDCTVitri = 0 THEN 0
											WHEN @ThanhTienThucChayHopDongChiTiet = 0 THEN 0
											ELSE @ThanhTienThucChayHDCTVitri/@ThanhTienThucChayHopDongChiTiet
										END)
				--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
				SET @ThanhTienVitri_theoTile = @GiaTriThayDoi*@TiLeViTri_Adx
				IF(@ThanhTienVitri_theoTile <> 0)
					EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirm_DoiTruOnline]
					@NgayThucHien		= @NgayThucHien, 
					@HopDongID			= @HopDongID,
					@HopDongChiTietID	= @HopDongChiTietID, 
					@DmSanPhamREF		= @DmSanPhamREF, 
					@Tk					= @Tk,
					@DmViTriREF			= @DmViTriREF,
					@TenViTri			= @TenViTri,
					@DmWebsiteREF		= @DmWebsiteREF,
					@TenWebsite			= @TenWebsite,
					@GiaTriThayDoi		= @ThanhTienVitri_theoTile, 
					@GhiChu				= @GhiChu
				--3. AdX Ecommerce'
				SET @DmViTriREF = 3
				SET @TenViTri = 'AdX Ecommerce'
				SET @ThanhTienThucChayHDCTVitri = ISNULL((
												SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhTienThucChay 
												FROM dbo.ThucChayDaTinhAdmarket
												WHERE TrangThaiHopDong <> 3 AND DmViTriREF = 3
												AND DmSanPhamREF = @DmSanPhamREF
												AND HopDongChiTietREF = @HopDongChiTietID
												AND NgayThucHien <= @NgayThucHien
												),0)
				SET @TiLeViTri_Adx = (CASE	WHEN @ThanhTienThucChayHDCTVitri = 0 THEN 0
											WHEN @ThanhTienThucChayHopDongChiTiet = 0 THEN 0
											ELSE @ThanhTienThucChayHDCTVitri/@ThanhTienThucChayHopDongChiTiet
										END)
				SET @ThanhTienVitri_theoTile = @GiaTriThayDoi*@TiLeViTri_Adx
				--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
				IF(@ThanhTienVitri_theoTile <> 0)
					EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirm_DoiTruOnline]
					@NgayThucHien		= @NgayThucHien, 
					@HopDongID			= @HopDongID,
					@HopDongChiTietID	= @HopDongChiTietID, 
					@DmSanPhamREF		= @DmSanPhamREF, 
					@Tk					= @Tk,
					@DmViTriREF			= @DmViTriREF,
					@TenViTri			= @TenViTri,
					@DmWebsiteREF		= @DmWebsiteREF,
					@TenWebsite			= @TenWebsite,
					@GiaTriThayDoi		= @ThanhTienVitri_theoTile, 
					@GhiChu				= @GhiChu
		END
		ELSE
		BEGIN
			--1. ADX
			SET @DmViTriREF = 1 
			SET @TenViTri = 'ADX'
			SET @ThanhTienOnlineVitri = (ISNULL((SELECT SUM(money)/1.1 AS ThanhTienThucChay FROM dbo.ThucChayAdXforUsers 
										WHERE 1=1 AND DmViTriREF = 1 AND NgayThucHien <'2017-09-11' 
										AND  username = @Tk),0)

											+ ISNULL(( SELECT SUM(CONVERT(FLOAT,ISNULL(domain_tt_money,0)))/1.1 AS ThanhTienThucChay 
											FROM dbo.ThucChayAdmarket_ADX_CPC_HopDong 
											WHERE 1=1 AND DmViTriREF = 1 
											AND NgayThucHien >='2017-09-11' 
											AND NgayThucHien <= @NgayThucHien
											AND username = @Tk 
											AND DmSanPhamREF = @DmSanPhamREF),0)
											)
										- (ISNULL((SELECT SUM(tcdt.ThanhTienThucChay)ThanhTienThucChay FROM
											(
													SELECT HopDongID, HopDongChiTietREF
													, SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhTienThucChay 
													FROM dbo.ThucChayDaTinhAdmarket
													WHERE TrangThaiHopDong <> 3 AND DmViTriREF = 1
													AND DmSanPhamREF = @DmSanPhamREF
													AND NgayThucHien <= @NgayThucHien
													AND HopDongChiTietREF = @HopDongChiTietID
													GROUP BY HopDongID, HopDongChiTietREF
												)tcdt 
												INNER JOIN 
												(	SELECT HopDongChiTietID FROM dbo.HopDongChiTiet 
															WHERE DeletedStatus = 0
															AND TK_AdMarket = @Tk 
															AND DmSanPhamREF = @DmSanPhamREF
															
												)hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
										),0))
				SET @TiLeViTri_Adx = (CASE	WHEN @ThanhTienOnlineVitri = 0 THEN 0
											WHEN @ThanhTienThucChayOnline = 0 THEN 0
											ELSE @ThanhTienOnlineVitri/@ThanhTienThucChayOnline
										END)
				--PRINT 'vitri = 1'
				--PRINT CONVERT(nvarchar(100),dbo.FormatNumber(@ThanhTienOnlineVitri)) 
				--PRINT CONVERT(nvarchar(100),dbo.FormatNumber(@ThanhTienThucChayOnline)) 
				--PRINT CONVERT(nvarchar(100),dbo.FormatNumber(@TiLeViTri_Adx)) 
				
				--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
				SET @ThanhTienVitri_theoTile = @GiaTriThayDoi*@TiLeViTri_Adx

				IF(@ThanhTienVitri_theoTile <> 0)
					EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirm_DoiTruOnline]
					@NgayThucHien		= @NgayThucHien, 
					@HopDongID			= @HopDongID,
					@HopDongChiTietID	= @HopDongChiTietID, 
					@DmSanPhamREF		= @DmSanPhamREF, 
					@Tk					= @Tk,
					@DmViTriREF			= @DmViTriREF,
					@TenViTri			= @TenViTri,
					@DmWebsiteREF		= @DmWebsiteREF,
					@TenWebsite			= @TenWebsite,
					@GiaTriThayDoi		= @ThanhTienVitri_theoTile, 
					@GhiChu				= @GhiChu

				--2. 'AdX Mobile' 
				SET @DmViTriREF = 2
				SET @TenViTri = 'AdX Mobile' 
				SET @ThanhTienOnlineVitri = (ISNULL((SELECT SUM([money])/1.1 AS ThanhTienThucChay FROM dbo.ThucChayAdXforUsers 
									WHERE 1=1 AND DmViTriREF = 2 AND NgayThucHien <'2017-09-11' 
									AND  username = @Tk),0)

										+ ISNULL(( SELECT SUM(CONVERT(FLOAT,ISNULL(domain_tt_money,0)))/1.1 AS ThanhTienThucChay 
										FROM dbo.ThucChayAdmarket_ADX_CPC_HopDong 
										WHERE 1=1 AND DmViTriREF = 2
										AND NgayThucHien >='2017-09-11' 
										AND NgayThucHien <= @NgayThucHien
										AND username = @Tk 
										AND DmSanPhamREF = @DmSanPhamREF),0
										) )
									- (ISNULL((SELECT SUM(tcdt.ThanhTienThucChay)ThanhTienThucChay FROM
										(
												SELECT HopDongID, HopDongChiTietREF
												, SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhTienThucChay 
												FROM dbo.ThucChayDaTinhAdmarket
												WHERE TrangThaiHopDong <> 3 AND DmViTriREF = 2
												AND DmSanPhamREF = @DmSanPhamREF
												AND NgayThucHien <= @NgayThucHien
												AND HopDongChiTietREF = @HopDongChiTietID
												GROUP BY HopDongID, HopDongChiTietREF
											)tcdt 
											INNER JOIN 
											(	SELECT HopDongChiTietID FROM dbo.HopDongChiTiet 
														WHERE DeletedStatus = 0
														AND TK_AdMarket = @Tk 
														AND DmSanPhamREF = @DmSanPhamREF
											)hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
										),0))

				SET @TiLeViTri_Adx = (CASE WHEN @ThanhTienOnlineVitri = 0 THEN 0
										 WHEN @ThanhTienThucChayOnline = 0 THEN 0
										ELSE @ThanhTienOnlineVitri/@ThanhTienThucChayOnline
									END)
				--	PRINT 'vitri = 2'
				--PRINT CONVERT(nvarchar(100),dbo.FormatNumber(@ThanhTienOnlineVitri)) 
				--PRINT CONVERT(nvarchar(100),dbo.FormatNumber(@ThanhTienThucChayOnline)) 
				--PRINT CONVERT(nvarchar(100),dbo.FormatNumber(@TiLeViTri_Adx)) 
				--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
				SET @ThanhTienVitri_theoTile = @GiaTriThayDoi*@TiLeViTri_Adx
				IF(@ThanhTienVitri_theoTile <> 0)
					EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirm_DoiTruOnline]
					@NgayThucHien		= @NgayThucHien, 
					@HopDongID			= @HopDongID,
					@HopDongChiTietID	= @HopDongChiTietID, 
					@DmSanPhamREF		= @DmSanPhamREF, 
					@Tk					= @Tk,
					@DmViTriREF			= @DmViTriREF,
					@TenViTri			= @TenViTri,
					@DmWebsiteREF		= @DmWebsiteREF,
					@TenWebsite			= @TenWebsite,
					@GiaTriThayDoi		= @ThanhTienVitri_theoTile, 
					@GhiChu				= @GhiChu
				--3. AdX Ecommerce'
				SET @DmViTriREF = 3
				SET @TenViTri = 'AdX Ecommerce'
				SET @ThanhTienOnlineVitri = (ISNULL((SELECT SUM(money)/1.1 AS ThanhTienThucChay FROM dbo.ThucChayAdXforUsers 
									WHERE 1=1 AND DmViTriREF = 3 AND NgayThucHien <'2017-09-11' 
									AND  username = @Tk),0)

										+ ISNULL(( SELECT SUM(CONVERT(FLOAT,ISNULL(domain_tt_money,0)))/1.1 AS ThanhTienThucChay 
										FROM dbo.ThucChayAdmarket_ADX_CPC_HopDong 
										WHERE 1=1 AND DmViTriREF = 3
										AND NgayThucHien >='2017-09-11' 
										AND NgayThucHien < @NgayThucHien
										AND username = @Tk 
										AND DmSanPhamREF = @DmSanPhamREF),0)
										)
									- (ISNULL((SELECT SUM(tcdt.ThanhTienThucChay)ThanhTienThucChay FROM
										(
												SELECT HopDongID, HopDongChiTietREF
												, SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhTienThucChay 
												FROM dbo.ThucChayDaTinhAdmarket
												WHERE TrangThaiHopDong <> 3 AND DmViTriREF = 3
												AND DmSanPhamREF = @DmSanPhamREF
												AND NgayThucHien <= @NgayThucHien
												AND HopDongChiTietREF = @HopDongChiTietID
												GROUP BY HopDongID, HopDongChiTietREF
											)tcdt 
											INNER JOIN 
											(	SELECT HopDongChiTietID FROM dbo.HopDongChiTiet 
														WHERE DeletedStatus = 0
														AND TK_AdMarket = @Tk 
														AND DmSanPhamREF = @DmSanPhamREF
											)hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
										),0))

				SET @TiLeViTri_Adx = (CASE WHEN @ThanhTienOnlineVitri = 0 THEN 0
										WHEN @ThanhTienThucChayOnline = 0 THEN 0
										ELSE @ThanhTienOnlineVitri/@ThanhTienThucChayOnline
									END)
				SET @ThanhTienVitri_theoTile = @GiaTriThayDoi*@TiLeViTri_Adx
				--	PRINT 'vitri = 1'
				--PRINT CONVERT(nvarchar(100),dbo.FormatNumber(@ThanhTienOnlineVitri)) 
				--PRINT CONVERT(nvarchar(100),dbo.FormatNumber(@ThanhTienThucChayOnline)) 
				--PRINT CONVERT(nvarchar(100),dbo.FormatNumber(@TiLeViTri_Adx)) 
				--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
				IF(@ThanhTienVitri_theoTile <> 0)
					EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirm_DoiTruOnline]
					@NgayThucHien		= @NgayThucHien, 
					@HopDongID			= @HopDongID,
					@HopDongChiTietID	= @HopDongChiTietID, 
					@DmSanPhamREF		= @DmSanPhamREF, 
					@Tk					= @Tk,
					@DmViTriREF			= @DmViTriREF,
					@TenViTri			= @TenViTri,
					@DmWebsiteREF		= @DmWebsiteREF,
					@TenWebsite			= @TenWebsite,
					@GiaTriThayDoi		= @ThanhTienVitri_theoTile, 
					@GhiChu				= @GhiChu
		END
	
	 END  
	
END

```
