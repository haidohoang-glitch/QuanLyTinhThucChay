# Stored Procedure: `prc_asd_UpdateTrangThai_ThucChay_PerformanceBase_ThayDoi_With_HopDong_ByHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-07-01 12:26:30.543000
- **Ngày sửa cuối**: 2021-07-01 12:26:30.543000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@pHopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		HAIDH
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- exec [dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong] '2017-09-05'
-- =============================================
CREATE PROCEDURE [dbo].[prc_asd_UpdateTrangThai_ThucChay_PerformanceBase_ThayDoi_With_HopDong_ByHopDong]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@pHopDongID INT
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
	AND tchd.HopDongID = @pHopDongID

END

```
