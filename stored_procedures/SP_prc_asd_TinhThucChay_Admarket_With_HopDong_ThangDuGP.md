# Stored Procedure: `prc_asd_TinhThucChay_Admarket_With_HopDong_ThangDuGP`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-09-07 10:00:26.370000
- **Ngày sửa cuối**: 2025-07-10 14:51:00.727000

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
	[dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong_ThangDuGP] '2021-03-24'
*/

CREATE PROCEDURE [dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong_ThangDuGP]
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
			  ,@LoaiGhiNhan SMALLINT = 0
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	--haidh comment 01/07/2021
	--DELETE FROM [dbo].[ThucChay_PerformanceBase_ThayDoi_HopDong]
	--WHERE 1=1 
	--AND RecordStatus = 0
	--AND NgayThucHien = @NgayThucHien
	DECLARE @NgayBDKoVAT DATETIME = '2022-03-29'

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
		   ,[TienThucChayKPI]
		   ,[LoaiGhiNhan])

   
	SELECT  tc.Id, tc.HopDongID, tc.HopDongChiTietREF, tc.DmSanPhamREF, tc.TenSanPham,
	tc.TK_Admarket, tc.DmViTriREF, tc.TenViTri, ISNULL(Convert(date,tc.NgayGhiNhanThayDoi),'1900-01-01') as NgayGhiNhanThayDoi, tc.TienThucChay_GhiNhan, 
	tc.CreatedAt AS CreatedAt, tc.CreatedBy AS CreatedBy, tc.LastModifiedAt AS LastModifiedAt, tc.LastModifiedBy AS LastModifiedBy,tc.RecordStatus as RecordStatus, 0 DeletedStatus, '' LyDoTuChoi
	,Convert(date,tc.LastModifiedAt) AS NgayThucHien
	,tc.TienThucChayKPI
	,tc.LoaiGhiNhan --0: thuc chay điều chỉnh - chi ap dung voi Adx, Viewplus, CPC admarket, 1: thuc chay thang du giai phap - all san pham, 2: MKT fee
	FROM
	(
	 SELECT  
	 ROW_NUMBER() OVER(PARTITION BY tc.SoHopDong, tc.HopDongID, tc.HopDongChiTietREF, tc.DmSanPhamREF, tc.TenSanPham, tc.TK_Admarket
						, tc.DmViTriREF, tc.TenViTri, ISNULL(tc.LoaiGhiNhan,0) ORDER BY tc.id DESC
		) AS Rownum, tc.Id,
	 tc.SoHopDong, tc.HopDongID, tc.HopDongChiTietREF, tc.DmSanPhamREF, tc.TenSanPham, tc.TK_Admarket
	 , tc.DmViTriREF, tc.TenViTri, tc.NgayGhiNhanThayDoi
	 , tc.CreatedAt, tc.CreatedBy, tc.LastModifiedAt, tc.LastModifiedBy,ISNULL(tc.RecordStatus,0) AS RecordStatus
	 , (
			CASE WHEN (Convert(date,tc.LastModifiedAt) < @NgayBDKoVAT) THEN tc.SoTienThayDoi/1.1
			ELSE tc.SoTienThayDoi
			END
		) AS TienThucChay_GhiNhan
	 , (
			CASE WHEN (Convert(date,tc.LastModifiedAt) < @NgayBDKoVAT) THEN tc.TienThucChayKPI/1.1
			ELSE tc.TienThucChayKPI
			END
		) AS TienThucChayKPI
	, ISNULL(tc.LoaiGhiNhan,0) as LoaiGhiNhan
	  FROM ThucChay_PerformanceBase_ThayDoi tc
	  WHERE Convert(date,tc.LastModifiedAt) = @NgayThucHien
	  --AND ISNULL(tc.RecordStatus,0) = 0 --haidh comment 01/07/2021
	  AND ISNULL(tc.DeletedStatus,0) = 0
	)tc
	WHERE tc.Rownum = 1
	AND NOT EXISTS(SELECT TOP (1) tchd.ThucChay_PerformanceBase_ThayDoi_ID 
		FROM [dbo].[ThucChay_PerformanceBase_ThayDoi_HopDong] tchd 
		WHERE tchd.ThucChay_PerformanceBase_ThayDoi_ID = tc.Id
		AND tchd.HopDongID = tc.HopDongID 
		ORDER BY tchd.ThucChay_PerformanceBase_ThayDoi_ID
	)
	 ORDER BY tc.SoHopDong, tc.HopDongID, tc.HopDongChiTietREF, tc.DmSanPhamREF, tc.TenSanPham, tc.TK_Admarket
	 , tc.DmViTriREF, tc.TenViTri

	
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
			  ,t.[LoaiGhiNhan]
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
									,@DmViTriID ,@NgayGhiNhanThayDoi ,@TienThucChay_GhiNhan, @TienThucChayKPI, @LoaiGhiNhan

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
		--1. TH0: Tien thay doi
		IF(@LoaiGhiNhan = 0)
		BEGIN
			DECLARE @DmMaHopDongREF INT, @SoHopDong NVARCHAR(100) = ''
		
			SELECT TOP (1) @DmMaHopDongREF = hd.DmMaHopDongREF
							,@SoHopDong = hd.SoHopDong  
			FROM dbo.HopDong hd
			WHERE hd.HopDongID = @HopDongID 
			ORDER BY hd.HopDongID

			SET @DmMaHopDongREF = ISNULL(@DmMaHopDongREF,0)
			SET @SoHopDong = ISNULL(@SoHopDong,'')
			--SH: 533,NB: 310, 5152: S-NB TINH CHO HOP DONG NOI BO
			IF(@DmMaHopDongREF IN (533,310,5152))
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
					--TINH THUC CHAY HOPDONG KPI
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
		END
		--2. TH1: Tien thang du giai phap
		--DmChienDichREF (0: ghi nhan thuc chay bt, 1: ???, 2: Ghi nhận theo KPI, 3: Thặng dư giải pháp)
		ELSE IF(@LoaiGhiNhan = 1)
		BEGIN
			--PRINT N'TH1'
			--Nhóm 1: nhóm sản phẩm Admarket (Adx, Viewplus, CPC admarket -(144,585,628) ) -- không liên quan đến online
				--1. Ghi nhận vào table ThucchayDatinh_Admarket
				--2. Ghi nhận vào table ThucChayDaTinh (thông tin ghi nhận giống ThucChayDaTinh_admarket)
				--3. Ghi nhận vào table ThucChayDaTinh_muaNgoai
			--Nhóm 2: nhóm sản phẩm không phải là Admarket
				--1. Ghi nhận vào ThucChayDaTinh
				--2. Ghi nhận vào ThucChayDaTinh_muangoai

			EXEC [dbo].[prc_asd_InsertThucChay_Admarket_With_HopDong_Admarket_ThangDuGP]
			@NgayThucHien = @NgayThucHien
			,@SoHopDong = @SoHopDong
			,@HopDongID = @HopDongID
			,@HopDongChitietID = @HopDongChitietID
			,@ThucChay_PerformanceBase_ThayDoi_ID = @ThucChay_PerformanceBase_ThayDoi_ID
			,@DmSanPhamID = @DmSanPhamID
			,@TK_Admarket = @TK_Admarket
			,@DmViTriID = @DmViTriID
			,@TienThucChay_GhiNhan = @TienThucChay_GhiNhan
		END
		--3. TH2: @LoaiGhiNhan = 2 thi ghi nhan cho san pham Performance Base - Marketing fee
		ELSE IF(@LoaiGhiNhan = 2)
		BEGIN
			--PRINT N'TH2'
			--print @ThucChay_PerformanceBase_ThayDoi_ID
			--print '[dbo].[prc_asd_InsertThucChay_Admarket_With_HopDong_MKT_FEE]'

			EXEC [dbo].[prc_asd_InsertThucChay_Admarket_With_HopDong_MKT_FEE]
			@NgayThucHien = @NgayThucHien
			,@SoHopDong = @SoHopDong
			,@HopDongID = @HopDongID
			,@HopDongChitietID = @HopDongChitietID
			,@ThucChay_PerformanceBase_ThayDoi_ID = @ThucChay_PerformanceBase_ThayDoi_ID
			,@DmSanPhamID = @DmSanPhamID
			,@TK_Admarket = @TK_Admarket
			,@DmViTriID = @DmViTriID
			,@TienThucChay_GhiNhan = @TienThucChay_GhiNhan
		END
		
		FETCH NEXT FROM db_cursor_thaydoi INTO @ThucChay_PerformanceBase_ThayDoi_ID ,@HopDongID ,@HopDongChitietID ,@DmSanPhamID,@TK_Admarket 
									,@DmViTriID ,@NgayGhiNhanThayDoi ,@TienThucChay_GhiNhan, @TienThucChayKPI, @LoaiGhiNhan
	END   

	CLOSE db_cursor_thaydoi   
	DEALLOCATE db_cursor_thaydoi

END

```
