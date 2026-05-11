# Stored Procedure: `ThucChay_DoiTruVaTinhLai_CPM_Job`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-22 15:28:25.440000
- **Ngày sửa cuối**: 2018-11-19 20:20:51.127000

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


CREATE PROCEDURE [dbo].[ThucChay_DoiTruVaTinhLai_CPM_Job]
	-- Add the parameters for the stored procedure here
	@dtStart DATETIME , 
	@dtEnd DATETIME ,
    @pSoHopDong NVARCHAR(50) ,
	@pHopDongChiTietID INT,
	@NgayTinh DATETIME
AS
BEGIN
	--Tinh Thuc Chay CPM
	EXEC [dbo].[ThucChay_HopDongChiTietAndBanner] @DenNgay = @dtEnd
	EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner] 
		
	EXEC [dbo].[sp_TC_DoiTruVaTinhLai_CPM]
					@StartDate = @dtStart
					, @EndDate = @dtEnd
					, @pSoHopDong = @pSoHopDong
					, @pHopDongChiTietID = @pHopDongChiTietID
					, @NgayTinh = @NgayTinh

	UPDATE dbo.ThucChayDaTinh SET NgayThucHien = @NgayTinh 
	WHERE HopDongChiTietREF = @pHopDongChiTietID 
			AND SoHopDong = @pSoHopDong 
			AND (GhiChu = N'ThucChay_InsertThucChayDaTinh_DoiTruVaTinhLai_CPM' 
					OR GhiChu = N'sp_TC_DoiTruVaTinhLai_CPM')
			AND CONVERT(DATE, CreatedAt) = CONVERT(DATE, GETDATE())
END


```
