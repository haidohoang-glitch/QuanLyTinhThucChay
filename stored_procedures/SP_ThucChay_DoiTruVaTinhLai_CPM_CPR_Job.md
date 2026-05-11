# Stored Procedure: `ThucChay_DoiTruVaTinhLai_CPM_CPR_Job`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-01-12 09:42:59.840000
- **Ngày sửa cuối**: 2018-03-16 11:30:24.183000

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


CREATE PROCEDURE [dbo].[ThucChay_DoiTruVaTinhLai_CPM_CPR_Job]
	-- Add the parameters for the stored procedure here
	@dtStart DATETIME , 
	@dtEnd DATETIME ,
    @pSoHopDong NVARCHAR(50) ,
	@pHopDongChiTietID INT,
	@NgayTinh DATETIME
AS
BEGIN
	--Tinh Thuc Chay CPM
	EXEC [dbo].[ThucChay_HopDongChiTietAndBanner] @dtEnd
	EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner] 
		
	--Tinh gia tri thuc chay CPR voi don vi la Goi
	EXEC [sp_TC_DoiTruVaTinhLai_CPM_CPR] @dtStart, @dtEnd, @pSoHopDong, @pHopDongChiTietID, @NgayTinh
	--Tinh gia tri thu chay voi don vi la CPR
	EXEC [sp_TC_DoiTruVaTinhLai_CPM_ByDVT_CPR] @dtStart, @dtEnd, @pSoHopDong, @pHopDongChiTietID, @NgayTinh

	UPDATE dbo.ThucChayDaTinh SET NgayThucHien = @NgayTinh 
	WHERE SoHopDong = @pSoHopDong 
     AND HopDongChiTietREF = @pHopDongChiTietID
     AND (GhiChu = N'ThucChay_InsertThucChayDaTinh_CPR_DoiTruVaTinhLai_CPM' 
       OR GhiChu = N'sp_TC_DoiTruVaTinhLai_CPM_CPR'
       OR GhiChu = N'ThucChay_InsertThucChayDaTinh_CPR_ByDVT_CPR_DoiTruVaTinhLai_CPM' 
       OR GhiChu = N'sp_TC_DoiTruVaTinhLai_CPM_ByDVT_CPR')
     AND CONVERT(DATE, CreatedAt) = CONVERT(DATE, GETDATE())
END


```
