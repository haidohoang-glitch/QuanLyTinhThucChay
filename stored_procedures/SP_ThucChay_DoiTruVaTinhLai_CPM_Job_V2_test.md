# Stored Procedure: `ThucChay_DoiTruVaTinhLai_CPM_Job_V2_test`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-10-04 14:27:14.393000
- **Ngày sửa cuối**: 2024-10-04 14:27:30.733000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@dtStart` | `datetime(8)` | No |
| `@dtEnd` | `datetime(8)` | No |
| `@pSoHopDong` | `nvarchar(100)` | No |
| `@pHopDongChiTietID` | `int(4)` | No |
| `@NgayTinh` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--
/*
EXEC [ThucChay_DoiTruVaTinhLai_CPM_Job_V2_test]
	@dtStart = '2023-03-22 00:00:00.000' , 
	@dtEnd = '2023-08-10 00:00:00.000' ,
    @pSoHopDong = N'QC3290323' ,
	@pHopDongChiTietID = 694330,
	@NgayTinh = '2023-08-10'
*/

CREATE PROCEDURE [dbo].[ThucChay_DoiTruVaTinhLai_CPM_Job_V2_test]
	-- Add the parameters for the stored procedure here
	@dtStart DATETIME , 
	@dtEnd DATETIME ,
    @pSoHopDong NVARCHAR(50) ,
	@pHopDongChiTietID INT,
	@NgayTinh DATETIME
AS
BEGIN
	DECLARE @HopDongID INT

	SET @HopDongID = ISNULL((SELECT TOP 1 hd.HopDongID FROM dbo.HopDong hd
	WHERE hd.SoHopDong = @pSoHopDong),0)
	--Tinh Thuc Chay CPM
	--PRINT 'TAO BANNER'
	EXEC [dbo].[ThucChay_HopDongChiTietAndBannerByHopDongID]
	@HopDongID = @HopDongID
	--PRINT 'UPDATE TI LE BANNER'
	EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_ByHopDong]
	@HopDongID = @HopDongID

	--PRINT 'THUC HIEN DOI TRU VA TINH LAI'
	--THUC HIEN DOI TRU VA TINH LAI
	EXEC [dbo].[sp_TC_DoiTruVaTinhLai_CPM_V2]
					@StartDate = @dtStart
					, @EndDate = @dtEnd
					, @pSoHopDong = @pSoHopDong
					, @pHopDongChiTietID = @pHopDongChiTietID
					, @NgayTinh = @NgayTinh
	
	------Đẩy dl tu [ThucChayDaTinh_DoiTruVaTinhLai_CPM] về ThucChayDaTinh
	--EXEC [dbo].[ThucChay_Update_ThucChayDaTinh_To_DoiTruVaTinhLai_CPM]
 -- 	@pHopDongChiTietID = @pHopDongChiTietID,
	--@NgayTinh = @NgayTinh

END


```
