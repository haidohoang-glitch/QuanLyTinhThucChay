# Stored Procedure: `prc_asd_TinhThucChay_Admarket_With_HopDong_BK1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-15 14:51:30.923000
- **Ngày sửa cuối**: 2021-06-15 14:51:30.923000

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
	[dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong] '2021-03-24'
*/

CREATE PROCEDURE [dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong_BK1]
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
			  ,@TienThucChay_GhiNhan   FLOAT
			  ,@LyDoLoi NVARCHAR(500) = N''
			  ,@RecordStatus int = 0
			  ,@GiaTriPhuTroi int = 1
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

		
	DELETE FROM [dbo].[ThucChay_PerformanceBase_ThayDoi_HopDong]
	WHERE 1=1 
	AND RecordStatus <> 1
	AND NgayThucHien = @NgayThucHien

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
	  FROM [dbo].[ThucChay_PerformanceBase_ThayDoi_HopDong] t
		WHERE Convert(date,t.NgayThucHien) = @NgayThucHien
		AND t.RecordStatus = 0
		AND t.DeletedStatus = 0
		ORDER BY t.HopDongID, t.HopDongChitietID, t.DmSanPhamID, t.TK_Admarket
	 , t.DmViTriID
	OPEN db_cursor_thaydoi   
	FETCH NEXT FROM db_cursor_thaydoi INTO @ThucChay_PerformanceBase_ThayDoi_ID ,@HopDongID ,@HopDongChitietID ,@DmSanPhamID,@TK_Admarket 
									,@DmViTriID ,@NgayGhiNhanThayDoi ,@TienThucChay_GhiNhan

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
		DECLARE @ThanhTienThucChayDaTinh FLOAT = 0, 
		@ThanhTienThucChayDaTinhHopDong_All_Tk FLOAT = 0,
		@TongTienThucChayTK FLOAT = 0
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
						ISNULL((SELECT SUM(CONVERT(FLOAT,tcdta1.domain_tt_money))
							FROM ThucChayAdmarket_ADX_CPC_HopDong tcdta1 
							WHERE tcdta1.NgayThucHien BETWEEN '2017-09-11' AND @NgayThucHien 
							AND tcdta1.DmSanPhamREF= @DmSanPhamID 
							AND tcdta1.username = @TK_Admarket 
							AND tcdta1.DmViTriREF = @DmViTriID
						),0)
						+ ISNULL((SELECT SUM(CONVERT(FLOAT,tcdta.[money]))
							FROM ThucChayAdXforUsers tcdta 
							WHERE tcdta.NgayThucHien <= '2017-09-10' 
							AND tcdta.DmSanPhamREF = @DmSanPhamID AND tcdta.username = @TK_Admarket
							AND tcdta.DmViTriREF = @DmViTriID
						),0)
					
				END
				ELSE IF(@DmSanPhamID = 628) --VIEWPLUS
				BEGIN
					SET @TongTienThucChayTK = 
							ISNULL(( SELECT SUM(convert(float,A1.domain_money))/1.1
									FROM ThucChayAdmarket_Viewplus_HopDong A1	
									WHERE (A1.NgayThucHien between '2017-09-11' and  @NgayThucHien) 
										AND A1.DmSanPhamREF= @DmSanPhamID 
										AND A1.username = @TK_Admarket
								),0)

							+ ISNULL((	SELECT SUM(A.[money])/1.1
								FROM ThucChayViewPlusForUsers A
								WHERE A.NgayThucHien <= '2017-09-10' 
								AND A.DmSanPhamREF= @DmSanPhamID 
								AND A.username = @TK_Admarket
							),0)
				END
				ELSE IF(@DmSanPhamID = 144)
				BEGIN
					SET @TongTienThucChayTK = 
						ISNULL((
							SELECT SUM(convert(float,A1.domain_tt_money)) / 1.1
							FROM   ThucChayAdmarket_ADX_CPC_HopDong A1 
							WHERE  A1.NgayThucHien between '2017-09-11' and @NgayThucHien
								   AND A1.DmSanPhamREF = @DmSanPhamID
								   AND A1.username = @TK_Admarket
						),0)
						+ ISNULL((
							SELECT SUM(A.[money]) / 1.1
							FROM   ThucChayAdmarketUsers A
							WHERE  A.NgayThucHien  <= '2017-09-10'
								   AND A.DmSanPhamREF = @DmSanPhamID
								   AND A.username = @TK_Admarket
						   ),0)
				END

				--2. gia tri them + gia tri hien tai theo tk da ghi nhan co sohhopdong <= tong gia tri thuc chay tra ve cua tai  khoan ( theo tk va format)
				IF (@TienThucChay_GhiNhan + @ThanhTienThucChayDaTinhHopDong_All_Tk <= @TongTienThucChayTK)
				BEGIN
					--THUC HIEN GHI NHAN THUC CHAY
					PRINT ''
					--3. Sp insert dữ liệu
					DECLARE @DmWebsiteREF INT, @TenWebsite NVARCHAR(50), @TenViTri nvarchar(50) = '', @GhiChu NVARCHAR(max) ='',
					@v_ThucChayDaTinhID_output NVARCHAR(200)
					SET @DmWebsiteREF = 826
					SET @TenWebsite = '(Blanks)'
					SET @GhiChu = N'Update TC'
					SET @TenViTri  = (CASE WHEN @DmViTriID = 1 THEN N'AdX'
											WHEN @DmViTriID = 2 THEN N'AdX Mobile'
											WHEN @DmViTriID = 3 THEN N'AdX Ecommerce'
										ELSE N''
									END)

					EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirm_DoiTruOnline]
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
						
						SET @RecordStatus = 1
					END
					--CAP NHAP @ThucChay_PerformanceBase_ThayDoi_ID VOI RecordStatus =1 
				END
				ELSE
				BEGIN
					SET @LyDoLoi = N'Giá trị tiền thêm vào + giá trị theo tk ghi nhận có sohopdong > tổng giá trị thực chạy tài khoản'
					SET @RecordStatus = 2 --LOI GHI NHAN THUC CHAY
				END
		END
		ELSE 
		BEGIN
			--LOI GIA TRI THANH TIEN VUOT PHAN BO
			SET @LyDoLoi = N'Giá trị thêm vào hợp đồng vượt giá trị phân bổ'
			SET @RecordStatus = 2
		END

		--CAP NHAP LY DO TU CHOI
		UPDATE tctd
		SET tctd.LyDoLoi = @LyDoLoi
		, tctd.RecordStatus = @RecordStatus
		FROM [dbo].[ThucChay_PerformanceBase_ThayDoi_HopDong] tctd
		WHERE tctd.ThucChay_PerformanceBase_ThayDoi_ID = @ThucChay_PerformanceBase_ThayDoi_ID
		AND convert(date,tctd.NgayThucHien) = @NgayThucHien

		FETCH NEXT FROM db_cursor_thaydoi INTO @ThucChay_PerformanceBase_ThayDoi_ID ,@HopDongID ,@HopDongChitietID ,@DmSanPhamID,@TK_Admarket 
									,@DmViTriID ,@NgayGhiNhanThayDoi ,@TienThucChay_GhiNhan
	END   

	CLOSE db_cursor_thaydoi   
	DEALLOCATE db_cursor_thaydoi

END

```
