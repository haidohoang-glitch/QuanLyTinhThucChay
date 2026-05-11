# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinh_DonViBai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-03-03 10:52:49.607000
- **Ngày sửa cuối**: 2021-06-07 11:30:41.903000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

/*
EXEC [dbo].[ThucChay_ExcInsertThucChayDaTinh_DonViBai] 
	@StartDate = '2021-03-04',
	@EndDate = '2021-03-04'
*/

CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinh_DonViBai] 
	@StartDate datetime,
	@EndDate datetime
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @Count INT =0
	DECLARE @SoHopDong NVARCHAR(50)
			   ,@HopDongID INT
			   ,@HopDongChiTietREF INT
			   ,@DmSanPhamREF INT
			   ,@DmBannerREF INT
			   ,@ThucChayHopDongChiTietREF INT
				, @NgayDanhSoGioiHan DATETIME
	SET @NgayDanhSoGioiHan = '2021-06-10'
	SET @NgayThucHien = @StartDate

	DELETE FROM dbo.ThucChayDaTinh
	WHERE CONVERT(date,NgayThucHien)BETWEEN @StartDate AND @EndDate
	AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao IN (13))
	AND DmSanPhamREF = 598
	AND DmHinhThucQuangCao = 5001
	AND DmVitriREF = 9198
	AND DonViTinh = N'BÀI'
	AND DotChayHopDong = N'CPM_DonViBai'
	AND NgayDanhSoHopDong < @NgayDanhSoGioiHan

	WHILE(@NgayThucHien <= @EndDate)
	BEGIN
		--THUC HIEN XOA DL THUC CHAY DONVIBAI TRUOC KHI TINH
		DELETE FROM [dbo].[ThucChay_DonViBai_Temp]

		INSERT INTO [dbo].[ThucChay_DonViBai_Temp]
			   ([ThucChayID]
			   ,[SoHopDong]
			   ,[HopDongREF]
			   ,[DmSanPhamREF]
			   ,[TenSanPham]
			   ,[DmBannerREF]
			   ,[NgayThucHien]
			   ,[HopDongChiTietREF]
			   ,[ThucChayHopDongChiTietREF]
			   ,CreatedBy
			   ,CreatedAt
			   ,LastModifiedBy
			   ,LastModifiedAt
			   ,DeletedStatus
			   ,PrintStatus
			   ,RecordStatus
			  )

		SELECT DISTINCT 0 as ThucChayID, tcc.SoHopDong,  hd.HopDongID, tcc.DmSanPhamREF, tcc.TenSanPham, tcc.DmBannerREF
			, tcc.NgayThucHien, hd.HopDongChiTietID as HopDongChiTietREF, hd.ThucChayHopDongChiTietID
			,'' AS CreatedBy, getdate() CreatedAt,'' AS LastModifiedBy, getdate() LastModifiedAt
			, 0 as DeletedStatus , 0 as PrintStatus , 0 as RecordStatus FROM
		(
			SELECT Distinct tc.SoHopDong, 0 HopDongREF, tc.DmSanPhamREF, tc.TenSanPham, tc.DmBannerREF
			, tc.NgayThucHien, tc.HopDongChiTietREF FROM dbo.ThucChay tc
			WHERE tc.NgayThucHien = @NgayThucHien
			AND tc.DmSanPhamREF = 598
			AND (tc.TongViewThucChay <> 0 or tc.TongClickThucChay <> 0)
		)tcc
		INNER JOIN
		(
			SELECT hd.HopDongID, hd.SoHopDong, hdct.HopDongChiTietID
			, hdct.DmSanPhamREF, tchdct.DmBannerREF, tchdct.ThucChayHopDongChiTietID FROM
			(
				SELECT hd.SoHopDong, hd.HopDongID FROM dbo.HopDong hd 
				WHERE hd.NgayDanhSoHopDong >= '2021-01-01'
				AND hd.NgayDanhSoHopDong < @NgayDanhSoGioiHan --HAIDH COMMENT THEM VAO VI THEO CACH TINH MOI THEO TUNG THUC TREO VA CHAY 2021-06-07
				AND hd.TrangThaiHopDong in (1,2,4)
			)hd
			INNER JOIN
			(
				SELECT hdct.HopDongFK, hdct.HopDongChiTietID, hdct.DmSanPhamREF, hdct.DmViTriREF
				, hdct.DonViTinhREF FROM dbo.HopDongChiTiet hdct 
				WHERE hdct.DeletedStatus = 0
				AND hdct.DmSanPhamREF = 598 AND hdct.DmViTriREF = 9198 AND hdct.DonViTinhREF = 7 --King size, Sponsor Page, Bai 
				AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18) --loai mua ngoai
				AND hdct.DmLoaiREF = 5001 --Display ads
			)hdct ON hd.HopDongID = hdct.HopDongFK
			INNER JOIN (
				SELECT tchdct.* FROM dbo.ThucChayHopDongChiTiet tchdct 
				WHERE tchdct.DmSanPhamREF = 598
				AND tchdct.DmHinhThucQuangCaoREF = 5001
				AND tchdct.DeletedStatus = 0
			)tchdct ON hdct.HopDongFK = tchdct.HopDongREF AND hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
			AND hdct.DmSanPhamREF = tchdct.DmSanPhamREF 
		)hd ON tcc.SoHopDong = hd.SoHopDong AND tcc.DmSanPhamREF = hd.DmSanPhamREF
		AND tcc.DmBannerREF = hd.DmBannerREF

		--THUC HIEN TINH GIA TRI THUC CHAY

		DECLARE Record_Cursor_DonViBai CURSOR FOR 
		SELECT distinct [SoHopDong]
			   ,[HopDongREF]
			   ,[HopDongChiTietREF]
			   ,[DmSanPhamREF]
		FROM	dbo.[ThucChay_DonViBai_Temp]
		ORDER BY [HopDongREF], [HopDongChiTietREF]	

		OPEN Record_Cursor_DonViBai

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor_DonViBai into @SoHopDong ,@HopDongID ,@HopDongChiTietREF,@DmSanPhamREF
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				--XAC DINH HOP DONG CHI TIET DA TINH THUC CHAY CHUA
				--NEU CHUA TINH THUC CHAY
				IF NOT EXISTS(
					SELECT tcdt.HopDongChiTietREF, sum(tcdt.ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) FROM dbo.ThucChayDaTinh tcdt
					WHERE tcdt.HopDongID = @HopDongID
					AND tcdt.HopDongChiTietREF = @HopDongChiTietREF
					AND tcdt.NgayThucHien <= @NgayThucHien
					GROUP BY tcdt.HopDongChiTietREF HAVING sum(tcdt.SoLuongThucChay + SoLuongThayDoi)  <> 0
				)
				BEGIN
					--THUC HIEN TINH THUC CHAY
					PRINT 'TINH THUC CHAY CHO TOAN BO PHAN BO'

					SELECT TOP (1) @ThucChayHopDongChiTietREF = tc.[ThucChayHopDongChiTietREF],
					@DmBannerREF = tc.[DmBannerREF]  FROM [ThucChay_DonViBai_Temp] tc
					WHERE tc.SoHopDong = @SoHopDong
					AND tc.[HopDongREF] = @HopDongID
					AND tc.[HopDongChiTietREF] = @HopDongChiTietREF
					AND tc.DmSanPhamREF = @DmSanPhamREF
					ORDER BY tc.[ThucChayHopDongChiTietREF]

					--select @NgayThucHien,@HopDongID,@HopDongChiTietREF,@DmSanPhamREF,@DmBannerREF, @ThucChayHopDongChiTietREF

					EXEC [dbo].[ThucChay_InsertThucChayDaTinh_CPM_DonViBai] 
						@NgayThucHien = @NgayThucHien,
						@HopDongID = @HopDongID,
						@HopDongChiTietREF = @HopDongChiTietREF,
						@DmSanPhamREF = @DmSanPhamREF,
						@DmBannerREF = @DmBannerREF,
						@ThucChayHopDongChiTietREF = @ThucChayHopDongChiTietREF
				END
			FETCH NEXT FROM Record_Cursor_DonViBai into @SoHopDong ,@HopDongID ,@HopDongChiTietREF,@DmSanPhamREF
			END

		CLOSE Record_Cursor_DonViBai
		DEALLOCATE Record_Cursor_DonViBai

		SET @NgayThucHien = DATEADD(d,1,@NgayThucHien)
		DELETE FROM dbo.[ThucChay_DonViBai_Temp]
	END 
	
	SELECT '1'
END


```
