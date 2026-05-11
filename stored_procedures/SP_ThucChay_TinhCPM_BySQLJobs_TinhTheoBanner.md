# Stored Procedure: `ThucChay_TinhCPM_BySQLJobs_TinhTheoBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-11-07 11:11:51.790000
- **Ngày sửa cuối**: 2017-11-07 11:49:54.210000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@dtStart` | `datetime(8)` | No |
| `@dtEnd` | `datetime(8)` | No |
| `@BannerID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--


CREATE PROCEDURE [dbo].[ThucChay_TinhCPM_BySQLJobs_TinhTheoBanner]
	-- Add the parameters for the stored procedure here
    @dtStart DATETIME
  , @dtEnd DATETIME
  , @BannerID INT
AS
    BEGIN
	
		
        EXEC dbo.ThucChay_ExcInsertThucChayDaTinh_TinhTheoBanner @dtStart, @dtEnd, @BannerID
        EXEC [dbo].[ThucChay_ExcInsertThucChayDaTinhCPV_TinhTheoBanner] @dtStart, @dtEnd, @BannerID
	
	--Tinh gia tri thuc chay CPR voi don vi la Goi
        EXEC [ThucChay_ExcInsertThucChayDaTinh_CPR_TinhTheoBanner] @dtStart, @dtEnd, @BannerID
	
	--Tinh gia tri thu chay voi don vi la CPR
        EXEC [ThucChay_ExcInsertThucChayDaTinh_CPR_ByDVT_CPR_TinhTheoBanner] @dtStart, @dtEnd, @BannerID


		-- Cap nhat ThucChayBannerGanNhieuHD sau khi xu ly
		DELETE FROM dbo.ThucChayBannerGanNhieuHD WHERE DmBannerREF = @BannerID

    END

--EXEC [dbo].[ThucChay_TinhCPM_BySQLJobs]

```
