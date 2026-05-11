# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinh_SponsorPost_BK`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-18 09:54:17.373000
- **Ngày sửa cuối**: 2014-11-19 12:25:06.107000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@SoHopDong1` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- Stored Procedure

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_ExcInsertThucChayDaTinh_SponsorPost_BK] '2014-09-10','2014-09-10', 'qc820214'
CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinh_SponsorPost_BK]  
	-- Add the parameters for the stored procedure here
	@StartDate datetime,
	@EndDate DATETIME,
	@SoHopDong1 NVARCHAR(50)
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	DECLARE @SoHopDong NVARCHAR(50)
	DECLARE @DmWebsiteREF INT, @TenWebsite NVARCHAR(255)

	DECLARE @DmChienDichREF INT,
			@DmBannerREF INT,
			@DonViTinh NVARCHAR(50),
			@TongViewThucChay FLOAT,
			@TongClickThucChay FLOAT
	
	set @NgayThucHien = @StartDate
	SET @DonViTinh = 'CLICK'
	
	
	--PRINT 'NgayThucHien: ' + convert(nvarchar(50),@NgayThucHien)
	WHILE(@NgayThucHien <= @EndDate)
	BEGIN				

		-- Delete du lieu truoc khi tinh neu da ton tai
		DELETE FROM ThucChayDaTinh WHERE DmSanPhamREF = 381 AND NgayThucHien BETWEEN @StartDate AND @EndDate 
		and sohopdong =@SoHopDong1

		-- Thuc chay khong hop dong 
		--EXEC dbo.ThucChay_InsertThucChayDaTinh_SponsorPostNotBySoHopDong @NgayThucHien

		 -- Thuc chay co so hop dong
		DECLARE Record_Cursor CURSOR FOR 

		SELECT --DISTINCT 
		dbo.ThucChay_FormatSoHopDong(tc.SoHopDong)SoHopDong ,
		tc.DmWebsiteREF, tc.TenWebsite, tc.DmChienDichREF, tc.DmBannerREF,
		SUM(tc.TongViewThucChay) TongViewThucChay, SUM(tc.TongClickThucChay) TongClickThucChay
		FROM --ThucChaySponsorTuyetnta
		ThucChay 
		AS tc
		WHERE tc.DmSanPhamREF = 381 
			AND convert (date,tc.NgayThucHien) = @NgayThucHien
			AND (tc.SoHopDong <>'' AND tc.SoHopDong IS NOT NULL AND tc.SoHopDong NOT LIKE '%demo%' AND SoHopDong <>'-')
			AND tc.SoHopDong =@SoHopDong1
		GROUP BY dbo.ThucChay_FormatSoHopDong(tc.SoHopDong),
		tc.DmWebsiteREF, tc.TenWebsite, tc.DmChienDichREF, tc.DmBannerREF
		
		OPEN Record_Cursor

		 -- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor into @SoHopDong, @DmWebsiteREF, @TenWebsite, @DmChienDichREF, @DmBannerREF, @TongViewThucChay, @TongClickThucChay

		WHILE @@FETCH_STATUS = 0
			BEGIN		
				EXEC ThucChay_InsertThucChayDaTinh_SponsorPostBySoHopDong_BK
				
				@NgayThucHien,
				@SoHopDong,
				@DmWebsiteREF,
				@TenWebsite,
				@DmChienDichREF,
				@DmBannerREF,
				@DonViTinh

			FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @DmWebsiteREF, @TenWebsite, @DmChienDichREF, @DmBannerREF, @TongViewThucChay, @TongClickThucChay
			END

		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor

		SET @NgayThucHien = DATEADD(d,1,@NgayThucHien)	
	end 

	SELECT '1'
END

```
