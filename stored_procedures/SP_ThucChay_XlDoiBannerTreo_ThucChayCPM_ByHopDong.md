# Stored Procedure: `ThucChay_XlDoiBannerTreo_ThucChayCPM_ByHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-05-22 10:19:59.613000
- **Ngày sửa cuối**: 2021-05-22 10:51:31.163000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |
| `@ListHopDongChiTietID` | `nvarchar(400)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@NgayGhiNhanThucChay` | `datetime(8)` | No |

## Definition (Source Code)

```sql
/*
EXEC [dbo].[ThucChay_XlDoiBannerTreo_ThucChayCPM_ByHopDong]
	@HopDongID = 1029084
	,@ListHopDongChiTietID = '606329,606326' --List cac phan bo can xu ly
	,@DmSanPhamREF = 240
	,@NgayGhiNhanThucChay = '2021-05-20'
*/
CREATE PROCEDURE [dbo].[ThucChay_XlDoiBannerTreo_ThucChayCPM_ByHopDong]
	@HopDongID INT
	,@ListHopDongChiTietID NVARCHAR(200)--List cac phan bo can xu ly
	,@DmSanPhamREF INT
	,@NgayGhiNhanThucChay DATETIME

AS
BEGIN
	DECLARE @HopDongChiTietID int
	, @SoHopDong NVARCHAR(100)
	, @MinNgayThucHien DATETIME
	, @MaxNgayThucHien DATETIME
	, @MinNgayThucHientc DATETIME
	, @MaxNgayThucHientc DATETIME
	, @TypeProduct int

	--Thuc hien xu ly lai banner treo huy hoac chuyen phan bo trong cung hopdong
	EXEC [dbo].[ThucChay_HopDongChiTietAndBannerByHopDongID]	@HopDongID = @HopDongID
	--Thuc hien update lai ti le
	EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_ByHopDong]	@HopDongID = @HopDongID

	SET @SoHopDong = ISNULL((SELECT TOP (1) SoHopDong FROM dbo.HopDong WHERE HopDongID = @HopDongID ORDER BY HopDongID),'')
	--xac dinh list cac phan bo can xu ly
	DECLARE Record_Cursor_HDCT CURSOR FOR 

	SELECT  Convert(int,splitdata) AS HopDongChiTietID FROM dbo.fnSplitString(@ListHopDongChiTietID,',')
	
	OPEN Record_Cursor_HDCT

	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor_HDCT into @HopDongChiTietID
		
	WHILE @@FETCH_STATUS = 0
		BEGIN
		--ngày min (tcdt/tc), ngày max(tcdt/tc), số hợp đồng, pboid, ngày ghi nhận
		SELECT @MinNgayThucHien = Min(tcdt.NgayThucHien)
		, @MaxNgayThucHien = MAX(tcdt.NgayThucHien) FROM dbo.ThucChayDaTinh tcdt
		WHERE tcdt.HopDongID = @HopDongID
		AND tcdt.HopDongChiTietREF = @HopDongChiTietID
		AND tcdt.DmSanPhamREF = @DmSanPhamREF
		
		SET @MinNgayThucHien = ISNULL(@MinNgayThucHien,'3000-01-01')
		SET @MaxNgayThucHien = ISNULL(@MaxNgayThucHien,'3000-01-01')

		--XAC DINH TYPEPRODUCT
		SET @TypeProduct = [dbo].[GetDmSanPhamIDByTypeProductID](@DmSanPhamREF)

		SELECT @MinNgayThucHientc = 
		(CASE WHEN @MinNgayThucHien <ISNULL(MIN(tc.NgayThucHien),'3000-01-01') THEN @MinNgayThucHien
		ELSE ISNULL(MIN(tc.NgayThucHien),'3000-01-01')
		END),
		@MaxNgayThucHientc =
		(CASE WHEN @MaxNgayThucHien > ISNULL(MAX(tc.NgayThucHien),'3000-01-01') THEN @MinNgayThucHien
		ELSE ISNULL(MAX(tc.NgayThucHien),'3000-01-01')
		END) 
		FROM dbo.ThucChay tc
		WHERE tc.SoHopDong = @SoHopDong
		AND tc.TypeProduct = @TypeProduct

		PRINT @HopDongChiTietID
		PRINT @MinNgayThucHientc
		PRINT @MaxNgayThucHientc
		PRINT @SoHopDong
		--THUC HIEN DOI TRU VA TINH LAI
		EXEC [dbo].[ThucChay_DoiTruVaTinhLai_CPM_Job]  @MinNgayThucHientc,@MaxNgayThucHientc,@SoHopDong,@HopDongChiTietID,@NgayGhiNhanThucChay
		PRINT @HopDongChiTietID
		FETCH NEXT FROM Record_Cursor_HDCT into @HopDongChiTietID
	END

	CLOSE Record_Cursor_HDCT
	DEALLOCATE Record_Cursor_HDCT


SELECT '1'
END



```
