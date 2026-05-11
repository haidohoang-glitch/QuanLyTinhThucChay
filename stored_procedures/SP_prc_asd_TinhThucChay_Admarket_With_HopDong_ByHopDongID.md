# Stored Procedure: `prc_asd_TinhThucChay_Admarket_With_HopDong_ByHopDongID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-07-01 12:24:11.097000
- **Ngày sửa cuối**: 2022-03-28 15:27:53.357000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@pHopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		HAIDH
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- exec [dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong] '2017-09-05'
-- =============================================
/*
	EXEC [dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong_ByHopDongID]
	  @NgayThucHien = '2022-03-18',
		@pHopDongID = 1036297
*/

CREATE PROCEDURE [dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong_ByHopDongID]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
    @pHopDongID INT
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

	SET @HopDongID = @pHopDongID
		
	DELETE FROM [dbo].[ThucChay_PerformanceBase_ThayDoi_HopDong]
	WHERE 1=1 
	--AND RecordStatus = 0
	AND NgayThucHien = @NgayThucHien
	AND HopDongID = @pHopDongID

	--select * FROM [dbo].[ThucChay_PerformanceBase_ThayDoi_HopDong]
	--WHERE 1=1 
	----AND RecordStatus = 0
	--AND NgayThucHien = @NgayThucHien
	--AND HopDongID = @pHopDongID

	INSERT INTO [dbo].[ThucChay_PerformanceBase_ThayDoi_HopDong]
           ([ThucChay_PerformanceBase_ThayDoi_ID]
           ,[HopDongID]
           ,[HopDongChitietID]
           ,[DmSanPhamID]
           ,[TenSanPham]
           ,[TK_Admarket]
           ,[DmViTriID]
           ,[TenViTri]
           ,[NgayGhiNhanThayDoi]
           ,[TienThucChay_GhiNhan]
           ,[CreatedAt]
           ,[CreatedBy]
           ,[LastModifiedAt]
           ,[LastModifiedBy]
           ,[RecordStatus]
           ,[DeletedStatus]
           ,[LyDoLoi]
           ,[NgayThucHien]
		   ,[TienThucChayKPI])

   
	SELECT  tc.Id, tc.HopDongID, tc.HopDongChiTietREF, tc.DmSanPhamREF, tc.TenSanPham,
	tc.TK_Admarket, tc.DmViTriREF, tc.TenViTri, ISNULL(Convert(date,tc.NgayGhiNhanThayDoi),'1900-01-01') as NgayGhiNhanThayDoi, tc.TienThucChay_GhiNhan, 
	tc.CreatedAt AS CreatedAt, tc.CreatedBy AS CreatedBy, tc.LastModifiedAt AS LastModifiedAt, tc.LastModifiedBy AS LastModifiedBy,0 as RecordStatus, 0 DeletedStatus, '' LyDoTuChoi
	,Convert(date,tc.LastModifiedAt) AS NgayThucHien
	,tc.TienThucChayKPI
	FROM
	(
	 SELECT  
	 ROW_NUMBER() OVER(PARTITION BY tc.SoHopDong, tc.HopDongID, tc.HopDongChiTietREF, tc.DmSanPhamREF, tc.TenSanPham, tc.TK_Admarket
						, tc.DmViTriREF, tc.TenViTri ORDER BY tc.id DESC
		) AS Rownum, tc.Id,
	 tc.SoHopDong, tc.HopDongID, tc.HopDongChiTietREF, tc.DmSanPhamREF, tc.TenSanPham, tc.TK_Admarket
	 , tc.DmViTriREF, tc.TenViTri, tc.NgayGhiNhanThayDoi, tc.CreatedAt, tc.CreatedBy, tc.LastModifiedAt, tc.LastModifiedBy, tc.SoTienThayDoi/1.1 AS TienThucChay_GhiNhan
	 , tc.TienThucChayKPI/1.1 AS TienThucChayKPI
	  FROM ThucChay_PerformanceBase_ThayDoi tc
	  WHERE Convert(date,tc.LastModifiedAt) = @NgayThucHien
	  AND ISNULL(tc.RecordStatus,0) = 0
	  AND ISNULL(tc.DeletedStatus,0) = 0
	)tc
	WHERE tc.Rownum = 1
	AND NOT EXISTS(SELECT TOP (1) tchd.ThucChay_PerformanceBase_ThayDoi_ID 
		FROM [dbo].[ThucChay_PerformanceBase_ThayDoi_HopDong] tchd 
		WHERE tchd.ThucChay_PerformanceBase_ThayDoi_ID = tc.Id
		AND tchd.HopDongID = tc.HopDongID 
		ORDER BY tchd.ThucChay_PerformanceBase_ThayDoi_ID
	)
	AND tc.HopDongID = @pHopDongID
	 ORDER BY tc.SoHopDong, tc.HopDongID, tc.HopDongChiTietREF, tc.DmSanPhamREF, tc.TenSanPham, tc.TK_Admarket
	 , tc.DmViTriREF, tc.TenViTri

	--select * FROM [dbo].[ThucChay_PerformanceBase_ThayDoi_HopDong]
	--WHERE 1=1 
	----AND RecordStatus = 0
	----AND NgayThucHien = @NgayThucHien
	--AND HopDongID = @pHopDongID

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
		ORDER BY t.HopDongID, t.HopDongChitietID, t.DmSanPhamID, t.TK_Admarket
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
				print 'prc_asd_InsertThucChay_Admarket_With_HopDong_QC_dev'
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
