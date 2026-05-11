# Stored Procedure: `prc_asd_InsertThucChay_Admarket_With_HopDong_NB_SH_KPI_dev`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-15 11:56:42.503000
- **Ngày sửa cuối**: 2021-06-29 11:12:12.127000

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
| `@TienThucChayKPI` | `float(8)` | No |
| `@TypeNB_SH_KPI` | `smallint(2)` | No |

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

CREATE PROCEDURE [dbo].[prc_asd_InsertThucChay_Admarket_With_HopDong_NB_SH_KPI_dev]
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
	,@TienThucChayKPI FLOAT
	,@TypeNB_SH_KPI SMALLINT --1 SH/NB, 2 KPI
AS
BEGIN
	DECLARE @LyDoLoi NVARCHAR(500) = N''
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

		--**********************RULE************
		--Check gia tri muon them dam bao rule
		--1. gia tri them vao hop dong ko vuot qua gia tri phan bo
		IF(EXISTS(SELECT TOP (1) hdct.HopDongChiTietID FROM dbo.HopDongChiTiet hdct 
				WHERE hdct.HopDongChiTietID = @HopDongChiTietID 
				AND hdct.DmSanPhamREF = @DmSanPhamID AND hdct.DeletedStatus = 0
				AND hdct.ThanhTien >= (@ThanhTienThucChayDaTinh + @TienThucChay_GhiNhan) - @GiaTriPhuTroi
				ORDER BY hdct.HopDongChiTietID
			))
		BEGIN
			--THUC HIEN GHI NHAN THUC CHAY
			-- Sp insert dữ liệu
			print 'ghi nhan thuc chay'
			DECLARE @DmWebsiteREF INT, @TenWebsite NVARCHAR(50), @TenViTri nvarchar(50) = '', @GhiChu NVARCHAR(max) ='',
			@v_ThucChayDaTinhID_output NVARCHAR(200)
			SET @DmWebsiteREF = 826
			SET @TenWebsite = '(Blanks)'
			SET @GhiChu =
				CASE WHEN @TypeNB_SH_KPI = 1 THEN N'Yêu cầu từ sản phẩm, Update TC NB - SH '
					WHEN @TypeNB_SH_KPI = 2 THEN N'Yêu cầu từ sản phẩm, Update TC KPI '
					ELSE N'Yêu cầu từ sản phẩm, Update TC '
				END

			SET @TenViTri  = (CASE WHEN @DmViTriID = 1 THEN N'AdX'
									WHEN @DmViTriID = 2 THEN N'AdX Mobile'
									WHEN @DmViTriID = 3 THEN N'AdX Ecommerce'
								ELSE N''
							END)
			IF(@TypeNB_SH_KPI = 2)
			BEGIN
				SET @DmViTriID = 0
				SET @TenViTri = ''
			END
			
			EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_With_HopDong_NB_SH_KPI]
				@NgayThucHien = @NgayThucHien, 
				@ThucChay_PerformanceBase_ThayDoi_ID = @ThucChay_PerformanceBase_ThayDoi_ID,
				@HopDongID = @HopDongID,
				@HopDongChiTietID = @HopDongChitietID, 
				@DmSanPhamREF = @DmSanPhamID, 
				@Tk		= @TK_Admarket,
				@DmViTriREF = @DmViTriID,
				@TenViTri = @TenViTri,
				@DmWebsiteREF  = @DmWebsiteREF,
				@TenWebsite = @TenWebsite,
				@GiaTriThayDoi = @TienThucChay_GhiNhan, 
				@GhiChu = @GhiChu,
				@TypeNB_SH_KPI = @TypeNB_SH_KPI,
				@ThucChayDaTinhID_output = @v_ThucChayDaTinhID_output OUTPUT

			IF(EXISTS(SELECT TOP (1) tc.HopDongID FROM ThucChayDaTinhAdmarket tc
			WHERE tc.ThucChayDaTinhID = @v_ThucChayDaTinhID_output
			AND tc.HopDongID = @HopDongID
			AND tc.HopDongChiTietREF = @HopDongChitietID
			AND tc.DmSanPhamREF = @DmSanPhamID
			AND tc.NgayThucHien = @NgayThucHien
			ORDER BY tc.HopDongID ))
			BEGIN
				--SET @RecordStatus = 1
				--DONE GHI NHAN
				SET @RecordStatus =
				(CASE WHEN (@RecordStatus_UPDATE = 0) AND (@TypeNB_SH_KPI = 1) THEN 1 --DONE GHI NHAN THUC CHAY 
					WHEN (@RecordStatus_UPDATE = 3) AND (@TypeNB_SH_KPI = 1)  THEN 8  --DONE GHI NHAN THUC CHAY, DONE GHI NHAN THUC CHAY KPI
					WHEN (@RecordStatus_UPDATE = 4) AND (@TypeNB_SH_KPI = 1)  THEN 5  --DONE GHI NHAN THUC CHAY, LOI GHI NHAN THUC CHAY KPI
					WHEN (@RecordStatus_UPDATE = 0) AND (@TypeNB_SH_KPI = 2)  THEN 3  -- DONE GHI NHAN THUC CHAY KPI
					WHEN (@RecordStatus_UPDATE = 1) AND (@TypeNB_SH_KPI = 2)  THEN 8  --DONE GHI NHAN THUC CHAY, DONE GHI NHAN THUC CHAY KPI
					WHEN (@RecordStatus_UPDATE = 2) AND (@TypeNB_SH_KPI = 2)  THEN 6  -- LOI GHI NHAN THUC CHAY, DONE GHI NHAN THUC CHAY KPI
					ELSE 1
				END)
			END
		END
		ELSE 
		BEGIN
			print 'LOI GIA TRI THANH TIEN VUOT PHAN BO'
			--LOI GIA TRI THANH TIEN VUOT PHAN BO
			SET @LyDoLoi =
			(CASE WHEN @TypeNB_SH_KPI = 1 THEN N'Giá trị thự chạy nb thêm vào hợp đồng vượt giá trị phân bổ, '
				WHEN @TypeNB_SH_KPI = 2 THEN N'Giá trị thự chạy kpi nb thêm vào hợp đồng vượt giá trị phân bổ, '
				ELSE  N'Giá trị thêm vào hợp đồng vượt giá trị phân bổ, '
				END
			)
			SET @RecordStatus =
				(CASE WHEN (@RecordStatus_UPDATE = 0) AND (@TypeNB_SH_KPI = 1) THEN 2 --LOI GHI NHAN THUC CHAY 
					WHEN (@RecordStatus_UPDATE = 3) AND (@TypeNB_SH_KPI = 1)  THEN 6   -- LOI GHI NHAN THUC CHAY, DONE GHI NHAN THUC CHAY KPI
					WHEN (@RecordStatus_UPDATE = 4) AND (@TypeNB_SH_KPI = 1)  THEN 7  -- LOI GHI NHAN THUC CHAY, LOI GHI NHAN THUC CHAY KPI
					WHEN (@RecordStatus_UPDATE = 0) AND (@TypeNB_SH_KPI = 2)  THEN 4  -- LOI GHI NHAN THUC CHAY KPI
					WHEN (@RecordStatus_UPDATE = 1) AND (@TypeNB_SH_KPI = 2)  THEN 5   -- DONE GHI NHAN THUC CHAY, LOI GHI NHAN THUC CHAY KPI
					WHEN (@RecordStatus_UPDATE = 2) AND (@TypeNB_SH_KPI = 2)  THEN 7  -- LOI GHI NHAN THUC CHAY, LOI GHI NHAN THUC CHAY KPI
					ELSE 2
				END)
		END

		--CAP NHAP LY DO TU CHOI
		UPDATE tctd
		SET tctd.LyDoLoi = tctd.LyDoLoi + @LyDoLoi
		, tctd.RecordStatus = @RecordStatus
		FROM [dbo].[ThucChay_PerformanceBase_ThayDoi_HopDong] tctd
		WHERE tctd.ThucChay_PerformanceBase_ThayDoi_ID = @ThucChay_PerformanceBase_ThayDoi_ID
		AND convert(date,tctd.NgayThucHien) = @NgayThucHien

END

/*
CAC TRANG THAI
0: CHUA DUOC DUYET
1:  DONE GHI NHAN THUC CHAY 
2: LOI GHI NHAN THUC CHAY
3: DONE GHI NHAN THUC CHAY KPI
4: LOI GHI NHAN THUC CHAY KPI
5: DONE GHI NHAN THUC CHAY, LOI GHI NHAN THUC CHAY KPI
6: LOI GHI NHAN THUC CHAY, DONE GHI NHAN THUC CHAY KPI
7: LOI GHI NHAN THUC CHAY, LOI GHI NHAN THUC CHAY KPI
8: DON GHI NHAN THUC CHAY, DONE GHI NHAN THUC CHAY KPI
*/
```
