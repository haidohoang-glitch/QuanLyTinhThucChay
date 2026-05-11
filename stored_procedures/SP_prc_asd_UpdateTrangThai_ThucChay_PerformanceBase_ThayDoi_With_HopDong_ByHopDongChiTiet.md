# Stored Procedure: `prc_asd_UpdateTrangThai_ThucChay_PerformanceBase_ThayDoi_With_HopDong_ByHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-12-23 09:59:25.443000
- **Ngày sửa cuối**: 2024-12-23 09:59:29.843000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayXuLy` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		HAIDH
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- exec [dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong] '2017-09-05'
-- =============================================
CREATE PROCEDURE [dbo].[prc_asd_UpdateTrangThai_ThucChay_PerformanceBase_ThayDoi_With_HopDong_ByHopDongChiTiet]
	-- Add the parameters for the stored procedure here
	@NgayXuLy DATETIME,
	@HopDongID INT,
	@HopDongChiTietID INT
AS
BEGIN
	SET NOCOUNT ON;

	UPDATE tc
	SET tc.LyDoTuChoi = tchd.LyDoLoi
	, tc.RecordStatus = tchd.RecordStatus
	FROM ThucChay_PerformanceBase_ThayDoi_HopDong tchd
	INNER JOIN ThucChay_PerformanceBase_ThayDoi tc on tchd.ThucChay_PerformanceBase_ThayDoi_ID = tc.Id
	--AND CONVERT(date,tc.NgayGhiNhanThayDoi) =  CONVERT(date,tchd.NgayGhiNhanThayDoi)
	WHERE CONVERT(date,tchd.NgayThucHien) = @NgayXuLy
	AND tchd.HopDongID = @HopDongID
	AND tchd.HopDongChiTietID = @HopDongChiTietID

END

```
