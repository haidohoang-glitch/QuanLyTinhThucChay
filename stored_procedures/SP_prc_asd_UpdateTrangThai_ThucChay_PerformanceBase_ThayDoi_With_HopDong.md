# Stored Procedure: `prc_asd_UpdateTrangThai_ThucChay_PerformanceBase_ThayDoi_With_HopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-03-18 16:17:39.600000
- **Ngày sửa cuối**: 2021-04-07 17:27:38.347000

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
CREATE PROCEDURE [dbo].[prc_asd_UpdateTrangThai_ThucChay_PerformanceBase_ThayDoi_With_HopDong]
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime
AS
BEGIN
	SET NOCOUNT ON;

	UPDATE tc
	SET tc.LyDoTuChoi = tchd.LyDoLoi
	, tc.RecordStatus = tchd.RecordStatus
	FROM ThucChay_PerformanceBase_ThayDoi_HopDong tchd
	INNER JOIN ThucChay_PerformanceBase_ThayDoi tc on tchd.ThucChay_PerformanceBase_ThayDoi_ID = tc.Id
	--AND CONVERT(date,tc.NgayGhiNhanThayDoi) =  CONVERT(date,tchd.NgayGhiNhanThayDoi)
	WHERE CONVERT(date,tchd.NgayThucHien) = @NgayThucHien

END

```
