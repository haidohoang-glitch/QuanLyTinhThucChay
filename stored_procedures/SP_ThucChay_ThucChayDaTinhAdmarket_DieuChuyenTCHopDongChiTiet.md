# Stored Procedure: `ThucChay_ThucChayDaTinhAdmarket_DieuChuyenTCHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-05-29 17:08:14.350000
- **Ngày sửa cuối**: 2018-06-01 15:10:58.350000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@GiaTriConfirm_VAT` | `float(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@Tk_Admarket` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[ThucChay_ThucChayDaTinhAdmarket_DieuChuyenTCHopDongChiTiet]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME, 
	@HopDongID INT,
	@HopDongChiTietID INT, 
	@GiaTriConfirm_VAT FLOAT, 
	@DmSanPhamREF INT, 
	@Tk_Admarket NVARCHAR(50)
AS
BEGIN
	DECLARE @DmWebsiteREF INT, @TenWebsite NVARCHAR(50),@TenViTri nvarchar(50)
	DECLARE @ThanhTienThucChayHDCTVitri FLOAT = 0, @TiLeViTri_Adx FLOAT = 0, @DmViTriREF INT, @ThanhTienVitri_theoTile FLOAT = 0
	DECLARE @GiaTriThayDoi FLOAT = 0, @GiaTriConfirm FLOAT = 0, @ThanhTienHDCT FLOAT = 0, @ThanhTienThucChayHDCT FLOAT = 0, @GhiChu NVARCHAR(max) =''
	DECLARE @TongThanhTienThucChayOnline FLOAT = 0, @ThanhTienThucChayOnlineVitri FLOAT = 0

	SET @ThanhTienHDCT = (SELECT TOP (1) ThanhTien FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID ORDER BY HopDongChiTietID)
	SET @ThanhTienThucChayHDCT = ISNULL((SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) 
									FROM dbo.ThucChayDaTinhAdmarket 
									WHERE HopDongChiTietREF = @HopDongChiTietID 
									AND TrangThaiHopDong <> 3),0)
	SET @GiaTriConfirm = @GiaTriConfirm_VAT/1.1
	 IF(@GiaTriConfirm < @ThanhTienHDCT)
	 BEGIN
			 print 'run'
			 SET @DmWebsiteREF = 826
			 SET @TenWebsite = '(Blanks)'
			 SET @GhiChu = N'Điểu chuyển giá trị thực chạy HDCT'

			 SET @GiaTriThayDoi = @GiaTriConfirm - @ThanhTienThucChayHDCT

			 IF @DmSanPhamREF = 144 
			 BEGIN
				 SET @TenViTri = 'CPC Admarket' 
					EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirm_DoiTruOnline]
					@NgayThucHien		= @NgayThucHien, 
					@HopDongID			= @HopDongID,
					@HopDongChiTietID	= @HopDongChiTietID, 
					@DmSanPhamREF		= @DmSanPhamREF, 
					@Tk					= @Tk_Admarket,
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
					@Tk					= @Tk_Admarket,
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
				IF(@ThanhTienThucChayHDCT = 0)
				BEGIN
				    PRINT 'Ghi nhan toan bo thuc chay cho hop dong chi tiet'
					SET @TongThanhTienThucChayOnline = (ISNULL((SELECT SUM(money)/1.1 AS ThanhTienThucChay FROM dbo.ThucChayAdXforUsers 
									WHERE 1=1 AND NgayThucHien <'2017-09-11' 
									AND  username = @Tk_Admarket),0)

										+ ISNULL(( SELECT SUM(CONVERT(FLOAT,ISNULL(domain_tt_money,0)))/1.1 AS ThanhTienThucChay 
										FROM dbo.ThucChayAdmarket_ADX_CPC_HopDong 
										WHERE 1=1 
										AND NgayThucHien >='2017-09-11' 
										AND NgayThucHien < @NgayThucHien
										AND username = @Tk_Admarket 
										AND DmSanPhamREF = @DmSanPhamREF),0)
										)
					 --1. ADX
					SET @DmViTriREF = 1 
					SET @TenViTri = 'ADX'
					SET @ThanhTienThucChayOnlineVitri = (ISNULL((SELECT SUM(money)/1.1 AS ThanhTienThucChay FROM dbo.ThucChayAdXforUsers 
									WHERE 1=1 AND DmViTriREF = @DmViTriREF AND NgayThucHien <'2017-09-11' 
									AND  username = @Tk_Admarket),0)

										+ ISNULL(( SELECT SUM(CONVERT(FLOAT,ISNULL(domain_tt_money,0)))/1.1 AS ThanhTienThucChay 
										FROM dbo.ThucChayAdmarket_ADX_CPC_HopDong 
										WHERE 1=1 AND DmViTriREF = @DmViTriREF
										AND NgayThucHien >='2017-09-11' 
										AND NgayThucHien < @NgayThucHien
										AND username = @Tk_Admarket 
										AND DmSanPhamREF = @DmSanPhamREF),0)
										)

						SET @TiLeViTri_Adx = (CASE	WHEN @ThanhTienThucChayOnlineVitri = 0 THEN 0
													WHEN @TongThanhTienThucChayOnline = 0 THEN 0
													ELSE @ThanhTienThucChayOnlineVitri/@TongThanhTienThucChayOnline
												END)
						--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
						SET @ThanhTienVitri_theoTile = @GiaTriThayDoi*@TiLeViTri_Adx
						IF(@ThanhTienVitri_theoTile <> 0)
							EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirm_DoiTruOnline]
							@NgayThucHien		= @NgayThucHien, 
							@HopDongID			= @HopDongID,
							@HopDongChiTietID	= @HopDongChiTietID, 
							@DmSanPhamREF		= @DmSanPhamREF, 
							@Tk					= @Tk_Admarket,
							@DmViTriREF			= @DmViTriREF,
							@TenViTri			= @TenViTri,
							@DmWebsiteREF		= @DmWebsiteREF,
							@TenWebsite			= @TenWebsite,
							@GiaTriThayDoi		= @ThanhTienVitri_theoTile, 
							@GhiChu				= @GhiChu

						--2. 'AdX Mobile' 
						SET @DmViTriREF = 2
						SET @TenViTri = 'AdX Mobile' 
						SET @ThanhTienThucChayOnlineVitri = (ISNULL((SELECT SUM(money)/1.1 AS ThanhTienThucChay FROM dbo.ThucChayAdXforUsers 
									WHERE 1=1 AND DmViTriREF = @DmViTriREF AND NgayThucHien <'2017-09-11' 
									AND  username = @Tk_Admarket),0)

										+ ISNULL(( SELECT SUM(CONVERT(FLOAT,ISNULL(domain_tt_money,0)))/1.1 AS ThanhTienThucChay 
										FROM dbo.ThucChayAdmarket_ADX_CPC_HopDong 
										WHERE 1=1 AND DmViTriREF = @DmViTriREF
										AND NgayThucHien >='2017-09-11' 
										AND NgayThucHien < @NgayThucHien
										AND username = @Tk_Admarket 
										AND DmSanPhamREF = @DmSanPhamREF),0)
										)

						SET @TiLeViTri_Adx = (CASE	WHEN @ThanhTienThucChayOnlineVitri = 0 THEN 0
													WHEN @TongThanhTienThucChayOnline = 0 THEN 0
													ELSE @ThanhTienThucChayOnlineVitri/@TongThanhTienThucChayOnline
												END)
						--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
						SET @ThanhTienVitri_theoTile = @GiaTriThayDoi*@TiLeViTri_Adx
						IF(@ThanhTienVitri_theoTile <> 0)
							EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirm_DoiTruOnline]
							@NgayThucHien		= @NgayThucHien, 
							@HopDongID			= @HopDongID,
							@HopDongChiTietID	= @HopDongChiTietID, 
							@DmSanPhamREF		= @DmSanPhamREF, 
							@Tk					= @Tk_Admarket,
							@DmViTriREF			= @DmViTriREF,
							@TenViTri			= @TenViTri,
							@DmWebsiteREF		= @DmWebsiteREF,
							@TenWebsite			= @TenWebsite,
							@GiaTriThayDoi		= @ThanhTienVitri_theoTile, 
							@GhiChu				= @GhiChu
						--3. AdX Ecommerce'
						SET @DmViTriREF = 3
						SET @TenViTri = 'AdX Ecommerce'
						SET @ThanhTienThucChayOnlineVitri = (ISNULL((SELECT SUM(money)/1.1 AS ThanhTienThucChay FROM dbo.ThucChayAdXforUsers 
									WHERE 1=1 AND DmViTriREF = @DmViTriREF AND NgayThucHien <'2017-09-11' 
									AND  username = @Tk_Admarket),0)

										+ ISNULL(( SELECT SUM(CONVERT(FLOAT,ISNULL(domain_tt_money,0)))/1.1 AS ThanhTienThucChay 
										FROM dbo.ThucChayAdmarket_ADX_CPC_HopDong 
										WHERE 1=1 AND DmViTriREF = @DmViTriREF
										AND NgayThucHien >='2017-09-11' 
										AND NgayThucHien < @NgayThucHien
										AND username = @Tk_Admarket 
										AND DmSanPhamREF = @DmSanPhamREF),0)
										)

						SET @TiLeViTri_Adx = (CASE	WHEN @ThanhTienThucChayOnlineVitri = 0 THEN 0
													WHEN @TongThanhTienThucChayOnline = 0 THEN 0
													ELSE @ThanhTienThucChayOnlineVitri/@TongThanhTienThucChayOnline
												END)
						SET @ThanhTienVitri_theoTile = @GiaTriThayDoi*@TiLeViTri_Adx
						--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
						IF(@ThanhTienVitri_theoTile <> 0)
							EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirm_DoiTruOnline]
							@NgayThucHien		= @NgayThucHien, 
							@HopDongID			= @HopDongID,
							@HopDongChiTietID	= @HopDongChiTietID, 
							@DmSanPhamREF		= @DmSanPhamREF, 
							@Tk					= @Tk_Admarket,
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
													WHEN @ThanhTienThucChayHDCT = 0 THEN 0
													ELSE @ThanhTienThucChayHDCTVitri/@ThanhTienThucChayHDCT
												END)
						--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
						SET @ThanhTienVitri_theoTile = @GiaTriThayDoi*@TiLeViTri_Adx
						IF(@ThanhTienVitri_theoTile <> 0)
							EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirm_DoiTruOnline]
							@NgayThucHien		= @NgayThucHien, 
							@HopDongID			= @HopDongID,
							@HopDongChiTietID	= @HopDongChiTietID, 
							@DmSanPhamREF		= @DmSanPhamREF, 
							@Tk					= @Tk_Admarket,
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
													WHEN @ThanhTienThucChayHDCT = 0 THEN 0
													ELSE @ThanhTienThucChayHDCTVitri/@ThanhTienThucChayHDCT
												END)
						--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
						SET @ThanhTienVitri_theoTile = @GiaTriThayDoi*@TiLeViTri_Adx
						IF(@ThanhTienVitri_theoTile <> 0)
							EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirm_DoiTruOnline]
							@NgayThucHien		= @NgayThucHien, 
							@HopDongID			= @HopDongID,
							@HopDongChiTietID	= @HopDongChiTietID, 
							@DmSanPhamREF		= @DmSanPhamREF, 
							@Tk					= @Tk_Admarket,
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
														and HopDongChiTietREF = @HopDongChiTietID
														),0)
						SET @TiLeViTri_Adx = (CASE	WHEN @ThanhTienThucChayHDCTVitri = 0 THEN 0
													WHEN @ThanhTienThucChayHDCT = 0 THEN 0
													ELSE @ThanhTienThucChayHDCTVitri/@ThanhTienThucChayHDCT
												END)
						SET @ThanhTienVitri_theoTile = @GiaTriThayDoi*@TiLeViTri_Adx
						--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
						IF(@ThanhTienVitri_theoTile <> 0)
							EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirm_DoiTruOnline]
							@NgayThucHien		= @NgayThucHien, 
							@HopDongID			= @HopDongID,
							@HopDongChiTietID	= @HopDongChiTietID, 
							@DmSanPhamREF		= @DmSanPhamREF, 
							@Tk					= @Tk_Admarket,
							@DmViTriREF			= @DmViTriREF,
							@TenViTri			= @TenViTri,
							@DmWebsiteREF		= @DmWebsiteREF,
							@TenWebsite			= @TenWebsite,
							@GiaTriThayDoi		= @ThanhTienVitri_theoTile, 
							@GhiChu				= @GhiChu
                END
			
			END
	 END
	
	
END

```
