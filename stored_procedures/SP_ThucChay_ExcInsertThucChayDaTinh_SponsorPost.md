# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinh_SponsorPost`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-11 10:43:49.517000
- **Ngày sửa cuối**: 2014-11-19 12:25:05.480000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- Stored Procedure

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC ThucChay_ExcInsertThucChayDaTinh_SponsorPost '2014-09-25','2014-09-25'
CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinh_SponsorPost]  
	-- Add the parameters for the stored procedure here
	@StartDate datetime,
	@EndDate datetime
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	DECLARE @SoHopDong NVARCHAR(50)
	DECLARE @DmWebsiteREF INT, @TenWebsite NVARCHAR(255)

	DECLARE @DmChienDichREF INT
	DECLARE @DmBannerREF INT
	DECLARE @DonViTinh NVARCHAR(50)
	
	DECLARE @SoHopDong1 NVARCHAR(50)

	set @NgayThucHien = @StartDate
	SET @DonViTinh = 'CLICK'
	--PRINT 'NgayThucHien: ' + convert(nvarchar(50),@NgayThucHien)
	WHILE(@NgayThucHien <= @EndDate)
	BEGIN				

		-- Delete du lieu truoc khi tinh neu da ton tai
		DELETE FROM ThucChayDaTinh WHERE DmSanPhamREF = 381 AND NgayThucHien BETWEEN @StartDate AND @EndDate 

		-- Thuc chay khong hop dong 
		EXEC dbo.ThucChay_InsertThucChayDaTinh_SponsorPostNotBySoHopDong @NgayThucHien

		 -- Thuc chay co so hop dong
		DECLARE Record_Cursor CURSOR FOR 

		SELECT --TOP 1 *
		DISTINCT dbo.ThucChay_FormatSoHopDong(tc.SoHopDong)SoHopDong ,tc.DmWebsiteREF, tc.TenWebsite, tc.DmChienDichREF, tc.DmBannerREF
		FROM ThucChay AS tc
		WHERE tc.DmSanPhamREF = 381 
			AND convert (date,tc.NgayThucHien) = @NgayThucHien
			AND (tc.SoHopDong <>'' AND tc.SoHopDong IS NOT NULL AND tc.SoHopDong NOT LIKE '%demo%' AND SoHopDong <>'-')
			
		OPEN Record_Cursor

		 -- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor into @SoHopDong, @DmWebsiteREF, @TenWebsite, @DmChienDichREF, @DmBannerREF

		WHILE @@FETCH_STATUS = 0
			BEGIN
				--select @NgayThucHien,
				--@SoHopDong,
				--@DmWebsiteREF,
				--@TenWebsite,
				--@DmChienDichREF,
				--@DmBannerREF,
				--@DonViTinh	
				EXEC ThucChay_InsertThucChayDaTinh_SponsorPostBySoHopDong
				@NgayThucHien,
				@SoHopDong,
				@DmWebsiteREF,
				@TenWebsite,
				@DmChienDichREF,
				@DmBannerREF,
				@DonViTinh	

			FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @DmWebsiteREF, @TenWebsite, @DmChienDichREF, @DmBannerREF
			END

		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor

		SET @NgayThucHien = DATEADD(d,1,@NgayThucHien)	
	end 

	SELECT '1'
END

```
