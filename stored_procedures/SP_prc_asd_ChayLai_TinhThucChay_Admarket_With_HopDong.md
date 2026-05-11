# Stored Procedure: `prc_asd_ChayLai_TinhThucChay_Admarket_With_HopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-12-23 17:21:19.810000
- **Ngày sửa cuối**: 2021-12-23 17:24:58.980000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		HAIDH
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- exec [dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong] '2017-09-05'
-- =============================================
/*
	 [dbo].[prc_asd_ChayLai_TinhThucChay_Admarket_With_HopDong] '2021-12-22'
*/

CREATE PROCEDURE [dbo].[prc_asd_ChayLai_TinhThucChay_Admarket_With_HopDong]
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime
AS
BEGIN
	DECLARE @ThucChay_PerformanceBase_ThayDoi_ID INT
			  ,@HopDongID   BIGINT
			  ,@HopDongChitietID   BIGINT
			  ,@DmSanPhamID   INT
			  ,@TK_Admarket   NVARCHAR(100)
			  ,@DmViTriID   INT
			  ,@NgayGhiNhanThayDoi   DATETIME
			  ,@TienThucChay_GhiNhan   FLOAT =0
			  ,@TienThucChayKPI FLOAT = 0
			  ,@LyDoLoi NVARCHAR(500) = N''
			  ,@RecordStatus int = 0
			  ,@GiaTriPhuTroi int = 1
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	DECLARE db_cursor_thaydoi CURSOR FOR  
		SELECT t.[ThucChay_PerformanceBase_ThayDoi_ID]
			  ,t.[HopDongID]
			  ,t.[HopDongChitietID]
			  ,t.[DmSanPhamID]
			  ,t.[TK_Admarket]
			  ,t.[DmViTriID]
			  ,t.[NgayGhiNhanThayDoi]
			  ,t.[TienThucChay_GhiNhan]
			  ,t.[TienThucChayKPI]
	  FROM [dbo].[ThucChay_PerformanceBase_ThayDoi_HopDong] t
		WHERE Convert(date,t.NgayThucHien) = @NgayThucHien
		AND t.RecordStatus = 0
		AND t.DeletedStatus = 0
		--ORDER BY t.HopDongID, t.HopDongChitietID, t.DmSanPhamID, t.TK_Admarket
	 --, t.DmViTriID
	 ORDER BY t.[ThucChay_PerformanceBase_ThayDoi_ID],t.HopDongID,t.HopDongChitietID, t.DmSanPhamID, t.TK_Admarket
	 , t.DmViTriID
	OPEN db_cursor_thaydoi   
	FETCH NEXT FROM db_cursor_thaydoi INTO @ThucChay_PerformanceBase_ThayDoi_ID ,@HopDongID ,@HopDongChitietID ,@DmSanPhamID,@TK_Admarket 
									,@DmViTriID ,@NgayGhiNhanThayDoi ,@TienThucChay_GhiNhan, @TienThucChayKPI

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
		DECLARE @DmMaHopDongREF INT, @SoHopDong NVARCHAR(100) = ''
		
		SELECT TOP (1) @DmMaHopDongREF = hd.DmMaHopDongREF
						,@SoHopDong = hd.SoHopDong  
		FROM dbo.HopDong hd
		WHERE hd.HopDongID = @HopDongID 
		ORDER BY hd.HopDongID

		SET @DmMaHopDongREF = ISNULL(@DmMaHopDongREF,0)
		SET @SoHopDong = ISNULL(@SoHopDong,'')
		--SH: 533,NB: 310 TINH CHO HOP DONG NOI BO
		IF(@DmMaHopDongREF IN (533,310))
		BEGIN
			IF(@TienThucChay_GhiNhan <> 0)
			BEGIN
				--TINH THUC CHAY HOPDONG NB, SH, KPI
				EXEC [dbo].[prc_asd_InsertThucChay_Admarket_With_HopDong_NB_SH_KPI]
				-- Add the parameters for the stored procedure here
				@NgayThucHien = @NgayThucHien
				,@SoHopDong = @SoHopDong
				,@HopDongID = @HopDongID
				,@HopDongChitietID = @HopDongChitietID
				,@ThucChay_PerformanceBase_ThayDoi_ID = @ThucChay_PerformanceBase_ThayDoi_ID
				,@DmSanPhamID = @DmSanPhamID
				,@TK_Admarket = @TK_Admarket
				,@DmViTriID = @DmViTriID
				,@TienThucChay_GhiNhan = @TienThucChay_GhiNhan
				,@TienThucChayKPI = 0
				,@TypeNB_SH_KPI = 1 --1 SH/NB, 2 KPI
			END
			--ghi nhan cho KPI
			IF(@TienThucChayKPI <> 0)
			BEGIN
				--TINH THUC CHAY HOPDONG NB, SH, KPI
				EXEC [dbo].[prc_asd_InsertThucChay_Admarket_With_HopDong_NB_SH_KPI]
				-- Add the parameters for the stored procedure here
				@NgayThucHien = @NgayThucHien
				,@SoHopDong = @SoHopDong
				,@HopDongID = @HopDongID
				,@HopDongChitietID = @HopDongChitietID
				,@ThucChay_PerformanceBase_ThayDoi_ID = @ThucChay_PerformanceBase_ThayDoi_ID
				,@DmSanPhamID = @DmSanPhamID
				,@TK_Admarket = @TK_Admarket
				,@DmViTriID = @DmViTriID
				,@TienThucChay_GhiNhan = 0
				,@TienThucChayKPI = @TienThucChayKPI
				,@TypeNB_SH_KPI = 2 --1 SH/NB, 2 KPI
			END
		END
		ELSE
		BEGIN
			IF(@TienThucChay_GhiNhan <> 0)
			BEGIN	
				EXEC [dbo].[prc_asd_InsertThucChay_Admarket_With_HopDong_QC]
				-- Add the parameters for the stored procedure here
				@NgayThucHien = @NgaythucHien
				,@SoHopDong = @SoHopDong
				,@HopDongID = @HopDongID
				,@HopDongChitietID = @HopDongChiTietID
				,@ThucChay_PerformanceBase_ThayDoi_ID = @ThucChay_PerformanceBase_ThayDoi_ID
				,@DmSanPhamID = @DmSanPhamID
				,@TK_Admarket = @TK_Admarket
				,@DmViTriID  = @DmViTriID
				,@TienThucChay_GhiNhan = @TienThucChay_GhiNhan
	
			END
			IF(@TienThucChayKPI <> 0)
			BEGIN
				--TINH THUC CHAY HOPDONG NB, SH, KPI
				EXEC [dbo].[prc_asd_InsertThucChay_Admarket_With_HopDong_QC_KPI]
				@NgayThucHien = @NgayThucHien
				,@SoHopDong = @SoHopDong
				,@HopDongID  = @HopDongID
				,@HopDongChitietID  = @HopDongChiTietID
				,@ThucChay_PerformanceBase_ThayDoi_ID  = @ThucChay_PerformanceBase_ThayDoi_ID
				,@DmSanPhamID  = @DmSanPhamID
				,@TK_Admarket = @TK_Admarket
				,@DmViTriID = @DmViTriID
				,@TienThucChayKPI = @TienThucChayKPI
			END

		END

		FETCH NEXT FROM db_cursor_thaydoi INTO @ThucChay_PerformanceBase_ThayDoi_ID ,@HopDongID ,@HopDongChitietID ,@DmSanPhamID,@TK_Admarket 
									,@DmViTriID ,@NgayGhiNhanThayDoi ,@TienThucChay_GhiNhan, @TienThucChayKPI
	END   

	CLOSE db_cursor_thaydoi   
	DEALLOCATE db_cursor_thaydoi

END

```
