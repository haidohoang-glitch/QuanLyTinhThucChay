# Stored Procedure: `prc_asd_InsertThucChay_Admarket_With_HopDong_QC_KPI_dev`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-22 15:49:37.417000
- **Ngày sửa cuối**: 2021-06-29 11:11:53.117000

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
| `@TienThucChayKPI` | `float(8)` | No |

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

CREATE PROCEDURE [dbo].[prc_asd_InsertThucChay_Admarket_With_HopDong_QC_KPI_DEV]
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime
	,@SoHopDong NVARCHAR(100)
	,@HopDongID INT
	,@HopDongChitietID INT
	,@ThucChay_PerformanceBase_ThayDoi_ID INT
	,@DmSanPhamID INT
	,@TK_Admarket NVARCHAR(500)
	,@DmViTriID INT
	,@TienThucChayKPI FLOAT

AS
BEGIN
	DECLARE @NgayGhiNhanThayDoi   DATETIME
			  ,@LyDoLoi NVARCHAR(500) = N''
			  ,@RecordStatus int = 0
			  ,@GiaTriPhuTroi int = 1
	DECLARE @ThanhTienThucChayDaTinh FLOAT = 0, 
		@ThanhTienThucChayDaTinhHopDong_All_Tk FLOAT = 0,
		@TongTienThucChayTK FLOAT = 0,
		@RecordStatus_KPI INT = 0

		SET @RecordStatus = ISNULL((
								SELECT tctd.RecordStatus FROM [dbo].[ThucChay_PerformanceBase_ThayDoi_HopDong] tctd
								WHERE tctd.ThucChay_PerformanceBase_ThayDoi_ID = @ThucChay_PerformanceBase_ThayDoi_ID
							),0)
		SET @LyDoLoi = N''
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
				AND hdct.ThanhTien >= (@ThanhTienThucChayDaTinh + @TienThucChayKPI) - @GiaTriPhuTroi
				ORDER BY hdct.HopDongChiTietID
			))
		BEGIN
			--THUC HIEN GHI NHAN THUC CHAY
			PRINT ''
			--3. Sp insert dữ liệu
			DECLARE @DmWebsiteREF INT, @TenWebsite NVARCHAR(50), @TenViTri nvarchar(50) = '', @GhiChu NVARCHAR(max) ='',
			@v_ThucChayDaTinhID_output NVARCHAR(200)
			SET @DmWebsiteREF = 826
			SET @TenWebsite = '(Blanks)'
			SET @GhiChu = N'Update TC'
			SET @DmViTriID = 0
						
			EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_With_HopDong_NB_SH_KPI]
			-- Add the parameters for the stored procedure here
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
			@GiaTriThayDoi = @TienThucChayKPI, 
			@GhiChu = @GhiChu,
			@TypeNB_SH_KPI =  2,
			@ThucChayDaTinhID_output = @v_ThucChayDaTinhID_output OUTPUT
			
			IF(EXISTS(SELECT TOP (1) tc.HopDongID FROM ThucChayDaTinhAdmarket tc
			WHERE tc.ThucChayDaTinhID = @v_ThucChayDaTinhID_output
			AND tc.HopDongID = @HopDongID
			AND tc.HopDongChiTietREF = @HopDongChitietID
			AND tc.DmSanPhamREF = @DmSanPhamID
			AND tc.NgayThucHien = @NgayThucHien
			ORDER BY tc.HopDongID ))
			BEGIN
				PRINT 'Update trang thai da tinh'
				print convert(varchar(50), @ThucChay_PerformanceBase_ThayDoi_ID)
				UPDATE tc
				SET tc.RecordStatus = 1
				FROM [ThucChay_PerformanceBase_ThayDoi_HopDong] tc
				WHERE tc.ThucChay_PerformanceBase_ThayDoi_ID = @ThucChay_PerformanceBase_ThayDoi_ID
				AND tc.HopDongID = @HopDongID
				AND tc.HopDongChitietID = @HopDongChitietID
				AND convert(date,tc.NgayThucHien) = @NgayThucHien
				
				SET @RecordStatus_KPI =
				(CASE WHEN @RecordStatus = 0 THEN 3 --DONE GHI NHAN THUC CHAY KPI
					WHEN @RecordStatus = 1 THEN 8  --DONE GHI NHAN THUC CHAY, DONE GHI NHAN THUC CHAY KPI
					WHEN @RecordStatus = 2 THEN 6  --LOI GHI NHAN THUC CHAY, DONE GHI NHAN THUC CHAY KPI
					ELSE 3
				END)

			END
		END
		ELSE 
		BEGIN
			--LOI GIA TRI THANH TIEN VUOT PHAN BO
			SET @LyDoLoi = N'Giá trị KPI thêm vào hợp đồng vượt giá trị phân bổ, '
			SET @RecordStatus_KPI =
				(CASE WHEN @RecordStatus = 0 THEN 4 --LOI GHI NHAN THUC CHAY KPI
					WHEN @RecordStatus = 1 THEN 5  --DONE GHI NHAN THUC CHAY, LOI GHI NHAN THUC CHAY KPI
					WHEN @RecordStatus = 2 THEN 7  --LOI GHI NHAN THUC CHAY, LOI GHI NHAN THUC CHAY KPI
					ELSE 4
				END)
		END

		--CAP NHAP LY DO TU CHOI
		UPDATE tctd
		SET tctd.LyDoLoi = tctd.LyDoLoi + @LyDoLoi 
		, tctd.RecordStatus = @RecordStatus_KPI
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
