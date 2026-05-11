# Stored Procedure: `prc_asd_InsertThucChay_Admarket_With_HopDong_QC_dev`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-15 11:56:22.550000
- **Ngày sửa cuối**: 2024-06-26 15:15:00.670000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(200)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChitietID` | `int(4)` | No |
| `@ThucChay_PerformanceBase_ThayDoi_ID` | `int(4)` | No |
| `@DmSanPhamID` | `int(4)` | No |
| `@TK_Admarket` | `nvarchar(1000)` | No |
| `@DmViTriID` | `int(4)` | No |
| `@TienThucChay_GhiNhan` | `float(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		HAIDH
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- exec [dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong] '2017-09-05'
-- =============================================
/*
	[dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong] '2021-03-24'
*/

CREATE PROCEDURE [dbo].[prc_asd_InsertThucChay_Admarket_With_HopDong_QC_dev]
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime
	,@SoHopDong NVARCHAR(100)
	,@HopDongID INT
	,@HopDongChitietID INT
	,@ThucChay_PerformanceBase_ThayDoi_ID INT
	,@DmSanPhamID INT
	,@TK_Admarket NVARCHAR(500)
	,@DmViTriID INT
	,@TienThucChay_GhiNhan FLOAT

AS
BEGIN
	DECLARE @NgayGhiNhanThayDoi   DATETIME
			  ,@LyDoLoi NVARCHAR(500) = N''
			  ,@RecordStatus int = 0
			  ,@GiaTriPhuTroi int = 1
	DECLARE @ThanhTienThucChayDaTinh FLOAT = 0, 
		@ThanhTienThucChayDaTinhHopDong_All_Tk FLOAT = 0,
		@TongTienThucChayTK FLOAT = 0,
		@RecordStatus_UPDATE INT = 0

		SET @RecordStatus_UPDATE = ISNULL((
							SELECT tctd.RecordStatus FROM [dbo].[ThucChay_PerformanceBase_ThayDoi_HopDong] tctd
							WHERE tctd.ThucChay_PerformanceBase_ThayDoi_ID = @ThucChay_PerformanceBase_ThayDoi_ID
						),0)

		SET @LyDoLoi = N''
		SET @RecordStatus = 0
		-----------ThucChayDaTinh----------------THONG TIN THUC CHAY DA TINH THEO HOP DONG
		SET @ThanhTienThucChayDaTinh = ISNULL(
		 (SELECT SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)
		   FROM ThucChayDaTinhAdmarket tcdt 
		   WHERE tcdt.HopDongID =  @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChitietID
		   AND tcdt.DmSanPhamREF = @DmSanPhamID AND tcdt.NgayThucHien <= @NgayThucHien
		   ),0)

		   print N'vao day roi'
		   select (@ThanhTienThucChayDaTinh + @TienThucChay_GhiNhan) - @GiaTriPhuTroi
		   SELECT hdct.thanhtien FROM dbo.HopDongChiTiet hdct 
				WHERE hdct.HopDongChiTietID = @HopDongChiTietID 
				AND hdct.DmSanPhamREF = @DmSanPhamID 
				AND hdct.DeletedStatus = 0
		--**********************RULE************
		--Check gia tri muon them dam bao rule
		--1. gia tri them vao hop dong ko vuot qua gia tri phan bo
		IF(EXISTS(SELECT TOP (1) hdct.HopDongChiTietID FROM dbo.HopDongChiTiet hdct 
				WHERE hdct.HopDongChiTietID = @HopDongChiTietID 
				AND hdct.DmSanPhamREF = @DmSanPhamID AND hdct.DeletedStatus = 0
				AND hdct.ThanhTien >= (@ThanhTienThucChayDaTinh + @TienThucChay_GhiNhan) - @GiaTriPhuTroi
				ORDER BY hdct.HopDongChiTietID
			)
			OR @TienThucChay_GhiNhan <0)
		BEGIN
			
			--GIA TRI HIEN TAI THEO TK DA GHI NHAN CO SOHOPDONG
			SET @ThanhTienThucChayDaTinhHopDong_All_Tk = 
			ISNULL((SELECT --tcdta.HopDongID, tcdta.HopDongChiTietREF, DmViTriREF, 
					SUM(tcdta.ThanhTienSauTrietKhauThucChay + tcdta.GiaTriThayDoi) ThanhTienSauTrietKhauThucChay
					FROM ThucChayDaTinhAdmarket tcdta 
					WHERE tcdta.NgayThucHien <= @NgayThucHien 
						AND tcdta.DmSanPhamREF = @DmSanPhamID
						AND tcdta.DmHinhThucQuangCao <> 42
						AND tcdta.DmViTriREF = @DmViTriID
						AND tcdta.HopDongID <> 0
						AND tcdta.DmChienDichREF <> 3 --THANG DU GIAI PHAP KHONG BAO GOM THUC CHAY THEO TAI KHOAN HOPDONG
						AND tcdta.DmChienDichREF <> 2 --Tien thuc chay KPI
						AND tcdta.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID 
															FROM HopDongChiTiet AS hdct 
															WHERE hdct.DmSanPhamREF = @DmSanPhamID 
															AND hdct.TK_AdMarket <> '' AND hdct.TK_AdMarket = @TK_Admarket
															AND DmHinhThucQuangCao <> 42 AND hdct.DeletedStatus <>1)
				),0)

				--TONG GIA TRI THUC CHAY TRA VE CUA TAI KHOAN
				IF(@DmSanPhamID = 585) --NEU LA ADX
				BEGIN
					SET @TongTienThucChayTK = 
						ISNULL((select SUM(tcdta1.TienChinh_VAT)
						FROM dbo.[ThucChay_CPCAdmarket_ViewAll_BF_VAT] tcdta1 
						WHERE 1=1 AND   tcdta1.DmSanPhamREF = @DmSanPhamID
										and  tcdta1.username =  @TK_Admarket
						),0)
					--SET @TongTienThucChayTK = 
					--	ISNULL((SELECT SUM(CONVERT(FLOAT,tcdta1.domain_tt_money))
					--		FROM ThucChayAdmarket_ADX_CPC_HopDong tcdta1 
					--		WHERE tcdta1.NgayThucHien BETWEEN '2017-09-11' AND @NgayThucHien 
					--		AND tcdta1.DmSanPhamREF= @DmSanPhamID 
					--		AND tcdta1.username = @TK_Admarket 
					--		AND tcdta1.DmViTriREF = @DmViTriID
					--	),0)
					--	+ ISNULL((SELECT SUM(CONVERT(FLOAT,tcdta.[money]))
					--		FROM ThucChayAdXforUsers tcdta 
					--		WHERE tcdta.NgayThucHien <= '2017-09-10' 
					--		AND tcdta.DmSanPhamREF = @DmSanPhamID AND tcdta.username = @TK_Admarket
					--		AND tcdta.DmViTriREF = @DmViTriID
					--	),0)
					
				END
				ELSE IF(@DmSanPhamID = 628) --VIEWPLUS
				BEGIN
					SET @TongTienThucChayTK = 
						ISNULL((select SUM(tcdta1.TienChinh_VAT)
							FROM dbo.[ThucChay_CPCAdmarket_ViewAll_BF_VAT] tcdta1 
							WHERE 1=1 AND   tcdta1.DmSanPhamREF = @DmSanPhamID
											and  tcdta1.username =  @TK_Admarket
							),0)
							--ISNULL(( SELECT SUM(convert(float,A1.domain_money))/1.1
							--		FROM ThucChayAdmarket_Viewplus_HopDong A1	
							--		WHERE (A1.NgayThucHien between '2017-09-11' and  @NgayThucHien) 
							--			AND A1.DmSanPhamREF= @DmSanPhamID 
							--			AND A1.username = @TK_Admarket
							--	),0)

							--+ ISNULL((	SELECT SUM(A.[money])/1.1
							--	FROM ThucChayViewPlusForUsers A
							--	WHERE A.NgayThucHien <= '2017-09-10' 
							--	AND A.DmSanPhamREF= @DmSanPhamID 
							--	AND A.username = @TK_Admarket
							--),0)
				END
				ELSE IF(@DmSanPhamID = 144)
				BEGIN
					SET @TongTienThucChayTK = 
						ISNULL((select SUM(tcdta1.TienChinh_VAT)
							FROM dbo.[ThucChay_CPCAdmarket_ViewAll_BF_VAT] tcdta1 
							WHERE 1=1 AND   tcdta1.DmSanPhamREF = @DmSanPhamID
											and  tcdta1.username =  @TK_Admarket
							),0)
						--ISNULL((
						--	SELECT SUM(convert(float,A1.domain_tt_money)) / 1.1
						--	FROM   ThucChayAdmarket_ADX_CPC_HopDong A1 
						--	WHERE  A1.NgayThucHien between '2017-09-11' and @NgayThucHien
						--		   AND A1.DmSanPhamREF = @DmSanPhamID
						--		   AND A1.username = @TK_Admarket
						--),0)
						--+ ISNULL((
						--	SELECT SUM(A.[money]) / 1.1
						--	FROM   ThucChayAdmarketUsers A
						--	WHERE  A.NgayThucHien  <= '2017-09-10'
						--		   AND A.DmSanPhamREF = @DmSanPhamID
						--		   AND A.username = @TK_Admarket
						--   ),0)
				END

				select @TienThucChay_GhiNhan + @ThanhTienThucChayDaTinhHopDong_All_Tk
				select @TongTienThucChayTK + @GiaTriPhuTroi
				print @TienThucChay_GhiNhan
				print @ThanhTienThucChayDaTinhHopDong_All_Tk
				print @TongTienThucChayTK
				print @GiaTriPhuTroi

				--2. gia tri them + gia tri hien tai theo tk da ghi nhan co sohhopdong <= tong gia tri thuc chay tra ve cua tai  khoan ( theo tk va format)
				IF (@TienThucChay_GhiNhan + @ThanhTienThucChayDaTinhHopDong_All_Tk <= @TongTienThucChayTK + @GiaTriPhuTroi)
				BEGIN
					--THUC HIEN GHI NHAN THUC CHAY
					PRINT 'THUC HIEN GHI NHAN THUC CHAY'
					----3. Sp insert dữ liệu
					--DECLARE @DmWebsiteREF INT, @TenWebsite NVARCHAR(50), @TenViTri nvarchar(50) = '', @GhiChu NVARCHAR(max) ='',
					--@v_ThucChayDaTinhID_output NVARCHAR(200)
					--SET @DmWebsiteREF = 826
					--SET @TenWebsite = '(Blanks)'
					--SET @GhiChu = N'Update TC'
					--SET @TenViTri  = (CASE WHEN @DmViTriID = 1 THEN N'AdX'
					--						WHEN @DmViTriID = 2 THEN N'AdX Mobile'
					--						WHEN @DmViTriID = 3 THEN N'AdX Ecommerce'
					--					ELSE N''
					--				END)

					--EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_With_HopDong_QC]
					--	@NgayThucHien = @NgayThucHien, 
					--	@ThucChay_PerformanceBase_ThayDoi_ID = @ThucChay_PerformanceBase_ThayDoi_ID,
					--	@HopDongID = @HopDongID,
					--	@HopDongChiTietID = @HopDongChitietID, 
					--	@DmSanPhamREF = @DmSanPhamID, 
					--	@Tk		= @TK_Admarket,
					--	@DmViTriREF = @DmViTriID,
					--	@TenViTri = @TenViTri,
					--	@DmWebsiteREF  = @DmWebsiteREF,
					--	@TenWebsite = @TenWebsite,
					--	@GiaTriThayDoi = @TienThucChay_GhiNhan, 
					--	@GhiChu = @GhiChu,
					--	@ThucChayDaTinhID_output = @v_ThucChayDaTinhID_output OUTPUT

					--IF(EXISTS(SELECT TOP (1) tc.HopDongID FROM ThucChayDaTinhAdmarket tc
					--WHERE tc.ThucChayDaTinhID = @v_ThucChayDaTinhID_output
					--AND tc.HopDongID = @HopDongID
					--AND tc.HopDongChiTietREF = @HopDongChitietID
					--AND tc.DmSanPhamREF = @DmSanPhamID
					--AND tc.NgayThucHien = @NgayThucHien
					--ORDER BY tc.HopDongID ))
					--BEGIN
					--	--PRINT 'Update trang thai da tinh'
					--	--print convert(varchar(50), @ThucChay_PerformanceBase_ThayDoi_ID)
					--	UPDATE tc
					--	SET tc.RecordStatus = 1
					--	FROM [ThucChay_PerformanceBase_ThayDoi_HopDong] tc
					--	WHERE tc.ThucChay_PerformanceBase_ThayDoi_ID = @ThucChay_PerformanceBase_ThayDoi_ID
					--	AND tc.HopDongID = @HopDongID
					--	AND tc.HopDongChitietID = @HopDongChitietID
					--	AND convert(date,tc.NgayThucHien) = @NgayThucHien
						
					--	--SET @RecordStatus = 1
					--	SET @RecordStatus =
					--	(CASE WHEN (@RecordStatus_UPDATE = 0) THEN 1 --DONE GHI NHAN THUC CHAY 
					--		WHEN (@RecordStatus_UPDATE = 3)  THEN 8  --DONE GHI NHAN THUC CHAY, DONE GHI NHAN THUC CHAY KPI
					--		WHEN (@RecordStatus_UPDATE = 4) THEN 5  --DONE GHI NHAN THUC CHAY, LOI GHI NHAN THUC CHAY KPI
					--		ELSE 1
					--	END)
					--END
					----CAP NHAP @ThucChay_PerformanceBase_ThayDoi_ID VOI RecordStatus =1 
				END
				ELSE
				BEGIN
					SET @LyDoLoi = N'Giá trị tiền thêm vào + giá trị theo tk ghi nhận có sohopdong > tổng giá trị thực chạy tài khoản, '
					SET @RecordStatus =
					(CASE WHEN (@RecordStatus_UPDATE = 0) THEN 2 --LOI GHI NHAN THUC CHAY 
					WHEN (@RecordStatus_UPDATE = 3)  THEN 6   -- LOI GHI NHAN THUC CHAY, DONE GHI NHAN THUC CHAY KPI
					WHEN (@RecordStatus_UPDATE = 4)  THEN 7  -- LOI GHI NHAN THUC CHAY, LOI GHI NHAN THUC CHAY KPI
					ELSE 2
				END)
				END
		END
		ELSE 
		BEGIN
			--LOI GIA TRI THANH TIEN VUOT PHAN BO
			SET @LyDoLoi = N'Giá trị thêm vào hợp đồng vượt giá trị phân bổ, '
			SET @RecordStatus =
				(CASE WHEN (@RecordStatus_UPDATE = 0) THEN 2 --LOI GHI NHAN THUC CHAY 
					WHEN (@RecordStatus_UPDATE = 3)  THEN 6   -- LOI GHI NHAN THUC CHAY, DONE GHI NHAN THUC CHAY KPI
					WHEN (@RecordStatus_UPDATE = 4)  THEN 7  -- LOI GHI NHAN THUC CHAY, LOI GHI NHAN THUC CHAY KPI
					ELSE 2
				END)
		END

		----CAP NHAP LY DO TU CHOI
		--UPDATE tctd
		--SET tctd.LyDoLoi = tctd.LyDoLoi + @LyDoLoi
		--, tctd.RecordStatus = @RecordStatus
		--FROM [dbo].[ThucChay_PerformanceBase_ThayDoi_HopDong] tctd
		--WHERE tctd.ThucChay_PerformanceBase_ThayDoi_ID = @ThucChay_PerformanceBase_ThayDoi_ID
		--AND convert(date,tctd.NgayThucHien) = @NgayThucHien

END

```
