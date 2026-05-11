# Stored Procedure: `UpdateHopDongChiTietREFInThucChayByBannerMobile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-03-22 15:47:33.387000
- **Ngày sửa cuối**: 2017-03-22 16:39:34.813000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--UpdateHopDongChiTietREFInThucChayByBannerMobile  'QC1710217',109386,'2017-03-08'
CREATE PROCEDURE UpdateHopDongChiTietREFInThucChayByBannerMobile  
	-- Add the parameters for the stored procedure here
	@SoHopDong NVARCHAR(50),
	@HopDongChiTietREF INT,
	@NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	DECLARE @DmBannerREF int
    -- Insert statements for procedure here
	BEGIN
	DECLARE vendor_cursor CURSOR FOR
	SELECT DISTINCT DmBannerREF FROM thucchay WHERE SoHopDong = @SoHopDong AND TypeProduct = 10
	AND NgayThucHien = @NgayThucHien AND HopDongChiTietREF = @HopDongChiTietREF

	OPEN vendor_cursor
	FETCH NEXT FROM vendor_cursor INTO @DmBannerREF

		WHILE @@FETCH_STATUS = 0
		BEGIN


					UPDATE dbo.ThucChay SET HopDongChiTietREF =
					 (SELECT TOP 1 HopDongChiTietREF FROM dbo.ThucChayHopDongChiTietAndBanner WHERE DmBannerID = CONVERT(NVARCHAR(50),@DmBannerREF))
					WHERE SoHopDong = @SoHopDong AND  DmBannerREF = @DmBannerREF AND TypeProduct = 10 	AND NgayThucHien = @NgayThucHien
					AND HopDongChiTietREF = @HopDongChiTietREF

	FETCH NEXT FROM vendor_cursor INTO @DmBannerREF
		END 
		CLOSE vendor_cursor;
		DEALLOCATE vendor_cursor;
	END

    EXEC TinhLaiThucChayMobile @SoHopDong, @NgayThucHien
END

```
