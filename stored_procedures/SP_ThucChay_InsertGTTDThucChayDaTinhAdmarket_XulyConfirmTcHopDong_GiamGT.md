# Stored Procedure: `ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirmTcHopDong_GiamGT`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-05-29 15:41:10.693000
- **Ngày sửa cuối**: 2018-06-08 08:59:25.953000

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

CREATE PROCEDURE [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirmTcHopDong_GiamGT]
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
	 --NEU THANHTIENTHUCCHAYHDCT = 0
		IF(@ThanhTienThucChayHopDongChiTiet = 0)
		BEGIN
			PRINT 'Ghi nhan toan bo thuc chay cho hop dong chi tiet'
				--1. ADX
			SET @DmViTriREF = 1 
			SET @TenViTri = 'ADX'
			SET @ThanhTienOnlineVitri = (ISNULL((SELECT SUM(money)/1.1 AS ThanhTienThucChay FROM dbo.ThucChayAdXforUsers 
							WHERE 1=1 AND DmViTriREF = @DmViTriREF AND NgayThucHien <'2017-09-11' 
							AND  username = @Tk),0)

								+ ISNULL(( SELECT SUM(CONVERT(FLOAT,ISNULL(domain_tt_money,0)))/1.1 AS ThanhTienThucChay 
								FROM dbo.ThucChayAdmarket_ADX_CPC_HopDong 
								WHERE 1=1 AND DmViTriREF = @DmViTriREF
								AND NgayThucHien >='2017-09-11' 
								AND NgayThucHien < @NgayThucHien
								AND username = @Tk 
								AND DmSanPhamREF = @DmSanPhamREF),0)
								)

				SET @TiLeViTri_Adx = (CASE	WHEN @ThanhTienOnlineVitri = 0 THEN 0
											WHEN @ThanhTienThucChayOnline = 0 THEN 0
											ELSE @ThanhTienOnlineVitri/@ThanhTienThucChayOnline
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
				SET @ThanhTienOnlineVitri = (ISNULL((SELECT SUM(money)/1.1 AS ThanhTienThucChay FROM dbo.ThucChayAdXforUsers 
							WHERE 1=1 AND DmViTriREF = @DmViTriREF AND NgayThucHien <'2017-09-11' 
							AND  username = @Tk),0)

								+ ISNULL(( SELECT SUM(CONVERT(FLOAT,ISNULL(domain_tt_money,0)))/1.1 AS ThanhTienThucChay 
								FROM dbo.ThucChayAdmarket_ADX_CPC_HopDong 
								WHERE 1=1 AND DmViTriREF = @DmViTriREF
								AND NgayThucHien >='2017-09-11' 
								AND NgayThucHien < @NgayThucHien
								AND username = @Tk 
								AND DmSanPhamREF = @DmSanPhamREF),0)
								)

				SET @TiLeViTri_Adx = (CASE	WHEN @ThanhTienOnlineVitri = 0 THEN 0
											WHEN @ThanhTienThucChayOnline = 0 THEN 0
											ELSE @ThanhTienOnlineVitri/@ThanhTienThucChayOnline
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
				SET @ThanhTienOnlineVitri = (ISNULL((SELECT SUM(money)/1.1 AS ThanhTienThucChay FROM dbo.ThucChayAdXforUsers 
							WHERE 1=1 AND DmViTriREF = @DmViTriREF AND NgayThucHien <'2017-09-11' 
							AND  username = @Tk),0)

								+ ISNULL(( SELECT SUM(CONVERT(FLOAT,ISNULL(domain_tt_money,0)))/1.1 AS ThanhTienThucChay 
								FROM dbo.ThucChayAdmarket_ADX_CPC_HopDong 
								WHERE 1=1 AND DmViTriREF = @DmViTriREF
								AND NgayThucHien >='2017-09-11' 
								AND NgayThucHien < @NgayThucHien
								AND username = @Tk 
								AND DmSanPhamREF = @DmSanPhamREF),0)
								)

				SET @TiLeViTri_Adx = (CASE	WHEN @ThanhTienOnlineVitri = 0 THEN 0
											WHEN @ThanhTienThucChayOnline = 0 THEN 0
											ELSE @ThanhTienOnlineVitri/@ThanhTienThucChayOnline
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
		--NEU THANHTIENTHUCCHAYHDCT <> 0
		ELSE
		BEGIN
			--1. ADX
			SET @DmViTriREF = 1 
			SET @TenViTri = 'ADX'
			SET @ThanhTienThucChayHDCTVitri = ISNULL((SELECT  SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhTienThucChay 
													FROM dbo.ThucChayDaTinhAdmarket
													WHERE TrangThaiHopDong <> 3 AND DmViTriREF = 1
													AND DmSanPhamREF = @DmSanPhamREF
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

	 END  
	
END

```
