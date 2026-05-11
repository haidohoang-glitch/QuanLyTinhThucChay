# Stored Procedure: `prc_asd_InsertThucChay_Admarket_With_HopDong_Admarket_ThangDuGP`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-09-07 10:53:35.623000
- **Ngày sửa cuối**: 2025-06-30 14:30:41.020000

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

CREATE PROCEDURE [dbo].[prc_asd_InsertThucChay_Admarket_With_HopDong_Admarket_ThangDuGP]
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

		IF(@DmSanPhamID IN  (144,585,628))
		BEGIN
			SET @ThanhTienThucChayDaTinh = ISNULL(
			 (SELECT SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)
			   FROM ThucChayDaTinhAdmarket tcdt 
			   WHERE tcdt.HopDongID =  @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChitietID
			   AND tcdt.DmSanPhamREF = @DmSanPhamID AND tcdt.NgayThucHien <= @NgayThucHien
			   ),0)
		END
		ELSE
		BEGIN
			SET @ThanhTienThucChayDaTinh = ISNULL(
			 (SELECT SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)
			   FROM ThucChayDaTinh tcdt 
			   WHERE tcdt.HopDongID =  @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChitietID
			   AND tcdt.DmSanPhamREF = @DmSanPhamID AND tcdt.NgayThucHien <= @NgayThucHien
			   ),0)
		END
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
			--PRINT 'Ghi nhan thuc chay thang du giai phap'
			--3. Sp insert dữ liệu
			DECLARE @DmWebsiteREF INT, @TenWebsite NVARCHAR(50), @TenViTri nvarchar(50) = '', @GhiChu NVARCHAR(max) ='',
			@v_ThucChayDaTinhID_output NVARCHAR(200)
			SET @DmWebsiteREF = 826
			SET @TenWebsite = '(Blanks)'
			SET @GhiChu = N'Update TC'
			SET @TenViTri  = (CASE WHEN @DmViTriID = 1 THEN N'AdX'
									WHEN @DmViTriID = 2 THEN N'AdX Mobile'
									WHEN @DmViTriID = 3 THEN N'AdX Ecommerce'
									WHEN @DmViTriID = 4 THEN N'AdX Leadform'
								ELSE N''
							END)
			
			EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_With_HopDong_Admarket_ThangDuGP]
			@NgayThucHien = @NgayThucHien, 
			@ThucChay_PerformanceBase_ThayDoi_ID = @ThucChay_PerformanceBase_ThayDoi_ID,
			@HopDongID = @HopDongID,
			@HopDongChiTietID = @HopDongChitietID, 
			@DmSanPhamREF = @DmSanPhamID, 
			@Tk = @TK_Admarket,
			@DmViTriREF = @DmViTriID,
			@TenViTri = @TenViTri,
			@DmWebsiteREF = @DmWebsiteREF,
			@TenWebsite = @TenWebsite,
			@TienThucChay_GhiNhan = @TienThucChay_GhiNhan, 
			@GhiChu = @GhiChu,
			@ThucChayDaTinhID_output = @v_ThucChayDaTinhID_output OUTPUT

			--select   isnull(@v_ThucChayDaTinhID_output,'')

			IF(EXISTS(SELECT TOP (1) tc.HopDongID FROM ThucChayDaTinh tc
			WHERE tc.ThucChayDaTinhID = @v_ThucChayDaTinhID_output
			AND tc.HopDongID = @HopDongID
			AND tc.HopDongChiTietREF = @HopDongChitietID
			AND tc.DmSanPhamREF = @DmSanPhamID
			AND tc.NgayThucHien = @NgayThucHien
			AND tc.DmChienDichREF = 3 --GHI NHAN THEO THANG DU GIAI PHAP
			ORDER BY tc.HopDongID ))
			BEGIN
				--PRINT 'Update trang thai da tinh'
				--print convert(varchar(50), @ThucChay_PerformanceBase_ThayDoi_ID)
				UPDATE tc
				SET tc.RecordStatus = 1
				FROM [ThucChay_PerformanceBase_ThayDoi_HopDong] tc
				WHERE tc.ThucChay_PerformanceBase_ThayDoi_ID = @ThucChay_PerformanceBase_ThayDoi_ID
				AND tc.HopDongID = @HopDongID
				AND tc.HopDongChitietID = @HopDongChitietID
				--AND convert(date,tc.NgayThucHien) = @NgayThucHien
				
				----HAIDH COMMENT neu san pham khong phai la cac san pham performance base hoac Nhieu san pham  hoac facebookin, tiktok thi se khong ghi nhan ThucCHayDaTinh
				----(144,585,628,306,423,733,5188)--HAIDH Update 04/03/2023 them các san pham facebooking, tiktok thi thuc hien xoa dl thucchaydatinh da ghi nhan truoc do

				IF(@DmSanPhamID NOT IN (144,585,628,306,423,733,5188))
				BEGIN
					DELETE FROM ThucChayDaTinh 
					WHERE ThucChayDaTinhID = @v_ThucChayDaTinhID_output
					AND HopDongID = @HopDongID
					AND HopDongChiTietREF = @HopDongChitietID
					AND DmSanPhamREF = @DmSanPhamID
					AND DmSanPhamREF  NOT IN (144,585,628,306,423,733,5188)
					AND NgayThucHien = @NgayThucHien
					AND DmChienDichREF = 3 --GHI NHAN THEO THANG DU GIAI PHAP
				END
				--SET @RecordStatus = 1
				SET @RecordStatus =
				(CASE WHEN (@RecordStatus_UPDATE = 0) THEN 1 --DONE GHI NHAN THUC CHAY 
					WHEN (@RecordStatus_UPDATE = 3)  THEN 8  --DONE GHI NHAN THUC CHAY, DONE GHI NHAN THUC CHAY KPI
					WHEN (@RecordStatus_UPDATE = 4) THEN 5  --DONE GHI NHAN THUC CHAY, LOI GHI NHAN THUC CHAY KPI
					ELSE 1
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

		--CAP NHAP LY DO TU CHOI
		UPDATE tctd
		SET tctd.LyDoLoi = tctd.LyDoLoi + @LyDoLoi
		, tctd.RecordStatus = @RecordStatus
		FROM [dbo].[ThucChay_PerformanceBase_ThayDoi_HopDong] tctd
		WHERE tctd.ThucChay_PerformanceBase_ThayDoi_ID = @ThucChay_PerformanceBase_ThayDoi_ID
		--AND convert(date,tctd.NgayThucHien) = @NgayThucHien

END

```
