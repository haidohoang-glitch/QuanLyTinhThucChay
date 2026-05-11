# Stored Procedure: `ThucChay_UpdateGia_From_AdmaticDonGiaBanner_To_TCBanner_Admatic_DsBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-01-06 13:01:51.580000
- **Ngày sửa cuối**: 2017-02-09 17:11:42.163000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DsDmBannerREF` | `nvarchar(2000)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_UpdateGia_From_AdmaticDonGiaBanner_To_TCBanner_Admatic] 391390

CREATE  PROCEDURE [dbo].[ThucChay_UpdateGia_From_AdmaticDonGiaBanner_To_TCBanner_Admatic_DsBanner] 
	@DsDmBannerREF NVARCHAR(1000)
AS
BEGIN
	DECLARE @DmBannerREF INT = 0
	DECLARE Cursor_BANNER CURSOR FOR
		--1. Xac dinh hop dong
	SELECT DISTINCT VALUE FROM dbo.asd_split(',',@DsDmBannerREF)
	OPEN Cursor_BANNER
	FETCH NEXT FROM Cursor_BANNER INTO @DmBannerREF
	WHILE @@FETCH_STATUS =0
	BEGIN
		PRINT @DmBannerREF
		EXEC [dbo].[ThucChay_UpdateGia_From_AdmaticDonGiaBanner_To_TCBanner_Admatic] @DmBannerREF
	FETCH NEXT FROM Cursor_BANNER INTO @DmBannerREF
	END
	CLOSE Cursor_BANNER;
	DEALLOCATE Cursor_BANNER;
END


```
