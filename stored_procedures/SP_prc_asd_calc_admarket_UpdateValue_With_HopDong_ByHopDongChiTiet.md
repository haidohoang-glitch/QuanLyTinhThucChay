# Stored Procedure: `prc_asd_calc_admarket_UpdateValue_With_HopDong_ByHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-12-20 17:19:32.163000
- **Ngày sửa cuối**: 2025-07-10 16:57:37.173000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayXuly` | `datetime(8)` | No |
| `@NgayGhiNhanThucChay` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv	
-- Create date: 20170909
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_asd_calc_admarket_UpdateValue_With_HopDong_ByHopDongChiTiet]
	-- Add the parameters for the stored procedure here
	@NgayXuly DATETIME,
	@NgayGhiNhanThucChay DATETIME,
	@HopDongID INT,
	@HopDongChiTietID INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	--Chu y trang thai va du lieu table ThucChay_PerformanceBase_ThayDoi  va table ThucChay_PerformanceBase_ThayDoi_HopDong
 
	EXEC [dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong_NgayDauThang_ThangDuGP_ByHopDongChiTiet]
	@NgayXuly = @NgayXuly,
	@NgayGhiNhanThucChay = @NgayGhiNhanThucChay,
	@HopDongID = @HopDongID,
	@HopDongChiTietID = @HopDongChiTietID


	--haidh comment thuc hien day trang thai de gui cho ben admarket biet 
	print '[prc_asd_UpdateTrangThai_ThucChay_PerformanceBase_ThayDoi_With_HopDong_ByHopDongChiTiet]'
	exec [dbo].[prc_asd_UpdateTrangThai_ThucChay_PerformanceBase_ThayDoi_With_HopDong_ByHopDongChiTiet]
	@NgayXuLy = @NgayXuly,
	@HopDongID = @HopDongID,
	@HopDongChiTietID = @HopDongChiTietID

	--haidh comment tao ban ghi cho job quet thong bao admarket
	IF(NOT EXISTS(SELECT TOP (1) ToDate FROM ADX_Job_UpdateStatusThayDoiThucChay WHERE ToDate = @NgayGhiNhanThucChay ORDER BY ToDate))
	BEGIN
		insert 	into  ADX_Job_UpdateStatusThayDoiThucChay (Status, FromDate, ToDate, IsDeleted, RequestKeyError)
		select 1, @NgayGhiNhanThucChay,@NgayGhiNhanThucChay,0,''
	END
END 



```
