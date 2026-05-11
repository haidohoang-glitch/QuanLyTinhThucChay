# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinh_DonViGoi_V2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-10-29 16:44:04.650000
- **Ngày sửa cuối**: 2023-08-22 17:03:20.107000

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
exec [dbo].[ThucChay_ExcInsertThucChayDaTinh_DonViGoi_V2] 
	@StartDate = '2021-03-14',
	@EndDate = '2021-03-14'
*/

CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinh_DonViGoi_V2] 
	@StartDate datetime,
	@EndDate datetime
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @Count INT =0, @NgayGioiHanHopDong DATETIME = '2021-01-01'
	DECLARE @SoHopDong NVARCHAR(50), @HopDongID INT, @HopDongChiTietID INT, @ThucChayHopDongChiTietID INT, @DmSanPhamREF INT, @TenWebsite NVARCHAR(50), @DmWebsiteREF INT, @DmBannerREF INT

	SET @NgayThucHien = @StartDate

	DECLARE @TABLE_HOPDONG TABLE(SOHOPDONG NVARCHAR(100), HOPDONGID INT, HOPDONGCHITIETID INT, DMSANPHAMREF INT
	, TENSANPHAM NVARCHAR(200), THUCCHAYHOPDONGCHITIETID INT, NHANHANG NVARCHAR(500), DMNHANHANGREF INT
	, DMBANNERREF INT, DMDONVITINH NVARCHAR(100), DONGIA FLOAT, CHIETKHAU FLOAT)

	--THUC HIEN TINH GIA TRI THUC CHAY
	INSERT INTO @TABLE_HOPDONG
	SELECT DISTINCT hd.SoHopDong, hd.HopDongID, hdct.HopDongChiTietID, tc.DmSanPhamREF
	, sp.TenSanPham, tc.ThucChayHopDongChiTietID, tc.NhanHang, tc.DmNhanHangREF
	, tc.DmBannerREF
	, (CASE WHEN tc.DmDonViTinhREF =1 THEN N'VIEW'
			WHEN tc.DmDonViTinhREF =2 THEN N'CLICK'
			WHEN tc.DmDonViTinhREF =32 THEN N'TRUE VIEW'
		ELSE ''
	END) AS DMDONVITINH
	, (CASE WHEN tc.DmDonViTinhREF =1 THEN tc.DonGia/1000
			WHEN tc.DmDonViTinhREF =2 THEN tc.DonGia 
			WHEN tc.DmDonViTinhREF =32 THEN tc.DonGia 
		ELSE tc.DonGia
	END) AS DONGIA
	, hdct.ChietKhau
	FROM 
	(
		SELECT * FROM dbo.HopDongChiTiet hdct
		WHERE hdct.DonViTinhREF = 10 --Don Vi Goi
		AND hdct.DmSanPhamREF IN (339, 240, 598, 342, 5056, 733, 5299)---haidh comment them san pham 733 - nhieu sanpham cho donvigoi 2021-10-29
		AND NOT (hdct.DmLoaiBannerREF = 18 OR hdct.DmLoaiREF IN (42,13))
		AND hdct.DeletedStatus = 0
	)hdct
	INNER JOIN 
	(
		SELECT tc.ThucChayHopDongChiTietID
		, ROW_NUMBER() OVER(PARTITION BY tc.HopDongREF, tc.HopDongChiTietREF
		, tc.DmSanPhamREF,  tc.NhanHang, tc.DmNhanHangREF
		, tc.DmBannerREF, tc.DmDonViTinhREF, tc.DonGia ORDER BY tc.ThucChayHopDongChiTietID DESC) AS RowN
		, tc.HopDongREF, tc.HopDongChiTietREF
		, tc.DmSanPhamREF,  tc.NhanHang, tc.DmNhanHangREF
		, tc.DmBannerREF, tc.DmDonViTinhREF, tc.DonGia
		FROM dbo.ThucChayHopDongChiTiet tc
		WHERE tc.DeletedStatus = 0
		AND tc.DmSanPhamREF IN (339, 240, 598, 342, 5056, 5299)
		AND tc.DmHinhThucQuangCaoREF not IN (42,13)
		AND tc.DmDonViTinhREF IS NOT NULL
		AND tc.CreatedAt >= '2021-03-01'
	)tc ON hdct.HopDongChiTietID = tc.HopDongChiTietREF
	INNER JOIN 
	(
		SELECT hd.HopDongID, hd.SoHopDong FROM dbo.HopDong hd
		WHERE hd.DeletedStatus = 0
		AND hd.TrangThaiHopDong <> 3
		AND hd.NgayDanhSoHopDong >= @NgayGioiHanHopDong --NGAY GOI HAN TINH
	)hd ON hdct.HopDongFK = hd.HopDongID
	INNER JOIN (SELECT s.DmSanPhamID, s.TenSanPham FROM dbo.DmSanPham s WHERE s.DeletedStatus = 0) sp ON sp.DmSanPhamID = tc.DmSanPhamREF
	WHERE tc.RowN = 1

	DELETE FROM dbo.ThucChayDaTinh
	WHERE convert(date,NgayThucHien)BETWEEN @StartDate AND @EndDate
	AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao IN (13,42))
	AND DmSanPhamREF IN (339, 240, 598, 342, 5056, 5299)
	AND DotChayHopDong = N'CPM_DonViGoi'

	WHILE(@NgayThucHien <= @EndDate)
	BEGIN
		DELETE FROM dbo.[ThucChay_DonViGoi_temp]
		--Xoa du lieu ThucChayDaTinh truoc khi tinh

		INSERT INTO [dbo].[ThucChay_DonViGoi_temp]
			   ([ThucChay_ID]
			   ,[ThucChayHopDongChiTietREF]
			   ,[SoHopDong]
			   ,[HopDongREF]
			   ,[HopDongChitietREF]
			   ,[DmSanPhamREF]
			   ,[TenSanPham]
			   ,[TenNhanHang]
			   ,[DmNhanHangREF]
			   ,[DmBannerID]
			   ,[DmWebsiteID]
			   ,[TenWebsite]
			   ,[DmViTriBannerSanPhamID]
			   ,[TenViTriBannerSanPham]
			   ,[SoLuongThucChay]
			   ,[SoLuongThucChayKM]
			   ,[DonViTinh]
			   ,DonGia
			   ,[ThanhTienThucChaySauCK_ChuaVAT]
			   ,[ThanhTienThucChayKM]
			   ,[NgayThucHien]
			   ,[CreatedAt]
			   ,[CreatedBy]
			   ,[LastModifiedAt]
			   ,[LastModifiedBy]
			   ,[DeletedStatus]
			   )
		-- VIEW , CLICK
		SELECT tc.ID
		, hd.THUCCHAYHOPDONGCHITIETID
		, hd.SOHOPDONG, hd.HOPDONGID, hd.HOPDONGCHITIETID, hd.DMSANPHAMREF, hd.TENSANPHAM
		, hd.NHANHANG, hd.DMNHANHANGREF, tc.DmBannerREF, tc.DmWebsiteREF, tc.TenWebsite
		, 0 AS [DmViTriBannerSanPhamID], tc.BannerTypeName as [TenViTriBannerSanPham]
		, (CASE WHEN (hd.DMDONVITINH = N'VIEW' AND hd.CHIETKHAU <> 100) THEN tc.TongViewThucChay
				WHEN (hd.DMDONVITINH = N'CLICK' AND hd.CHIETKHAU <> 100) THEN tc.TongClickThucChay
			ELSE 0
		END) AS [SoLuongThucChay]
		, (CASE WHEN (hd.DMDONVITINH = N'VIEW' AND hd.CHIETKHAU = 100) THEN tc.TongViewThucChay
				WHEN (hd.DMDONVITINH = N'CLICK' AND hd.CHIETKHAU = 100) THEN tc.TongClickThucChay
			ELSE 0
		END) AS [SoLuongThucChayKM]
		, hd.DMDONVITINH
		, hd.DONGIA
		, (CASE WHEN (hd.DMDONVITINH = N'VIEW' AND hd.CHIETKHAU <> 100) THEN tc.TongViewThucChay*hd.DonGia*(100-hd.Chietkhau)/100
				WHEN (hd.DMDONVITINH = N'CLICK' AND hd.CHIETKHAU <> 100) THEN tc.TongClickThucChay*hd.DonGia*(100-hd.ChietKhau)/100
			ELSE 0
		END) AS [ThanhTienThucChaySauCK_ChuaVAT]
		, (CASE WHEN (hd.DMDONVITINH = N'VIEW' AND hd.CHIETKHAU = 100) THEN tc.TongViewThucChay*hd.DONGIA
				WHEN (hd.DMDONVITINH = N'CLICK' AND hd.CHIETKHAU = 100) THEN tc.TongClickThucChay*hd.DONGIA
			ELSE 0
		END) AS [ThanhTienThucChayKM]
		, @NgayThucHien AS NgayThucHien
		, tc.CreatedAt
		, tc.CreatedBy
		, tc.LastModifiedAt
		, tc.LastModifiedBy
		, tc.DeletedStatus
		FROM 
		(
			SELECT * FROM dbo.ThucChay tc
			WHERE tc.DmSanPhamREF IN (339, 240, 598, 342, 5056, 5299)
			AND tc.NgayThucHien = @NgayThucHien
		)tc
		INNER JOIN @TABLE_HOPDONG hd ON hd.SOHOPDONG = tc.SoHopDong
		AND hd.DMSANPHAMREF = tc.DmSanPhamREF
		AND hd.DMBANNERREF = tc.DmBannerREF
		WHERE (hd.DMDONVITINH = N'VIEW' OR hd.DMDONVITINH = N'CLICK')
		
		UNION
		--TRUE VIEW
		SELECT tc.ID
		, hd.THUCCHAYHOPDONGCHITIETID
		, hd.SOHOPDONG, hd.HOPDONGID, hd.HOPDONGCHITIETID, hd.DMSANPHAMREF, hd.TENSANPHAM
		, hd.NHANHANG, hd.DMNHANHANGREF, tc.DmBannerREF, tc.DmWebsiteREF, tc.TenWebsite
		, 0 AS [DmViTriBannerSanPhamID], tc.BannerTypeName as [TenViTriBannerSanPham]
		, (CASE WHEN (hd.DMDONVITINH = N'TRUE VIEW' AND hd.CHIETKHAU <> 100) THEN tc.True_View
			ELSE 0
		END) AS [SoLuongThucChay]
		, (CASE WHEN (hd.DMDONVITINH = N'TRUE VIEW' AND hd.CHIETKHAU = 100) THEN tc.True_View
			ELSE 0
		END) AS [SoLuongThucChayKM]
		, hd.DMDONVITINH
		, hd.DONGIA
		, (CASE WHEN (hd.DMDONVITINH = N'TRUE VIEW' AND hd.CHIETKHAU <> 100) THEN tc.True_View*hd.DonGia*(100-hd.ChietKhau)/100
			ELSE 0
		END) AS [ThanhTienThucChaySauCK_ChuaVAT]
		, (CASE WHEN (hd.DMDONVITINH = N'TRUE VIEW' AND hd.CHIETKHAU = 100) THEN tc.True_View*hd.DONGIA
			ELSE 0
		END) AS [ThanhTienThucChayKM]
		, @NgayThucHien AS NgayThucHien
		, tc.CreatedAt
		, tc.CreatedBy
		, tc.LastModifiedAt
		, tc.LastModifiedBy
		, tc.DeletedStatus
		FROM 
		(
			SELECT tc.ID,tc.SoHopDong,tc.DmSanPhamREF,tc.bannerid as DmBannerREF,tc.Siteid as DmWebsiteREF
			,tc.SiteName as TenWebsite,ISNULL(tc.FormatName,'') as BannerTypeName,tc.True_View,tc.CreatedAt
			,tc.CreatedBy,tc.LastModifiedAt,tc.LastModifiedBy,tc.DeletedStatus 
			FROM dbo.ThucChaytrueview tc
			WHERE tc.DmSanPhamREF IN (339, 240, 598, 342, 5056, 5299)
			AND tc.NgayThucHien = @NgayThucHien
		)tc
		INNER JOIN @TABLE_HOPDONG hd ON hd.SOHOPDONG = tc.SoHopDong
		AND hd.DMSANPHAMREF = tc.DmSanPhamREF
		AND hd.DMBANNERREF = tc.DmBannerREF
		WHERE (hd.DMDONVITINH = N'TRUE VIEW')


		DECLARE R_Cursor_DonViGoi CURSOR FOR 
		SELECT distinct A.SoHopDong, A.HopDongREF, A.HopDongChitietREF, A.ThucChayHopDongChiTietREF, A.DmSanPhamREF, A.DmWebsiteID, A.TenWebsite, A.DmBannerID
		  FROM
			(
				SELECT tct.SoHopDong, tct.HopDongREF, tct.HopDongChitietREF, tct.ThucChayHopDongChiTietREF, tct.DmSanPhamREF, tct.DmWebsiteID, tct.TenWebsite, tct.DmBannerID
				FROM dbo.[ThucChay_DonViGoi_temp] tct
			)A
		ORDER BY A.SoHopDong, A.DmSanPhamREF	

		OPEN R_Cursor_DonViGoi

		-- Perform the first fetch.
		FETCH NEXT FROM R_Cursor_DonViGoi into @SoHopDong, @HopDongID, @HopDongChiTietID, @ThucChayHopDongChiTietID, @DmSanPhamREF, @DmWebsiteREF, @TenWebsite, @DmBannerREF
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				--CHECK TRUONG HOP 1 BANNER CO NHIEU DON GIA HAY KO
				IF(EXISTS(--CHI TINH VOI TRUONG HOP 1 BANNER,SAN PHAM, HOPDONGCHITIET CO - 1 DON GIA
					SELECT count(distinct tc.DONGIA) sl 
					FROM @TABLE_HOPDONG tc
					WHERE tc.HOPDONGID = @HopDongID
					AND tc.HOPDONGCHITIETID = @HopDongChiTietID
					AND tc.DmSanPhamREF = @DmSanPhamREF
					AND tc.DmBannerREF = @DmBannerREF
					GROUP BY tc.HOPDONGID, tc.DmSanPhamREF, tc.HOPDONGCHITIETID, tc.DmBannerREF,tc.DONGIA
					HAVING COUNT(distinct tc.DONGIA) = 1
				))
				BEGIN
					--PRINT 'THUC HIEN TINH'
					EXEC [dbo].[ThucChay_InsertThucChayDaTinh_ByHD_DonViGoi_V2] 
						@NgayThucHien = @NgayThucHien,
						@SoHopDong = @SoHopDong,
						@HopDongID = @HopDongID,
						@HopDongChiTietREF = @HopDongChiTietID,
						@ThucChayHopDongChiTietREF = @ThucChayHopDongChiTietID,
						@DmSanPhamREF = @DmSanPhamREF,
						@DmWebsiteREF = @DmWebsiteREF,
						@TenWebsite = @TenWebsite, 
						@DmBannerID = @DmBannerREF,
						@GhiChu = N'Tinh Thuc Chay CPM DonViGoi'

					-----LOG SP CALL
					--INSERT INTO [dbo].[Log_SP_Call]
					--		   ([SP_NAME]
					--		   ,[SP_TIME_CALL]
					--		   ,[SP_END_TIME_CALL]
					--		   ,[NOTE]
					--		   ,[VALUE_INPUT])
					--	 VALUES
					--		   (N'[dbo].[ThucChay_InsertThucChayDaTinh_ByHD_DonViGoi_V2]'
					--		   ,GETDATE()
					--		   ,GETDATE()
					--		   ,N'SOHOPDONG:' + @SoHopDong
					--		   ,N'@HopDongID:' + CONVERT(NVARCHAR(100),@HopDongID) 
					--		   + N', @HopDongChiTietREF:' + CONVERT(NVARCHAR(100),@HopDongChiTietID) 
					--		   + N', @ThucChayHopDongChiTietREF:'  + CONVERT(NVARCHAR(100),@ThucChayHopDongChiTietID)
					--		   + N', @DmSanPhamREF:' + CONVERT(NVARCHAR(100),@DmSanPhamREF)
					--		   + N', @DmWebsiteREF:' + CONVERT(NVARCHAR(100),@DmWebsiteREF)
					--		   + N', @DmBannerID:'  + CONVERT(NVARCHAR(100),@DmBannerREF)
					--		   )

					
				END
			FETCH NEXT FROM R_Cursor_DonViGoi into @SoHopDong, @HopDongID, @HopDongChiTietID, @ThucChayHopDongChiTietID, @DmSanPhamREF, @DmWebsiteREF, @TenWebsite, @DmBannerREF
			END

		CLOSE R_Cursor_DonViGoi
		DEALLOCATE R_Cursor_DonViGoi

		SET @NgayThucHien = DATEADD(d,1,@NgayThucHien)
		DELETE FROM dbo.[ThucChay_DonViGoi_temp]
	END 
	
	--SELECT '1'
END


```
