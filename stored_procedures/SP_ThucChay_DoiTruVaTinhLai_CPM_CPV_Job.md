# Stored Procedure: `ThucChay_DoiTruVaTinhLai_CPM_CPV_Job`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-01-12 09:41:17.697000
- **Ngày sửa cuối**: 2018-01-12 09:57:28.543000

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


CREATE PROCEDURE [dbo].[ThucChay_DoiTruVaTinhLai_CPM_CPV_Job]
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
		
	EXEC [sp_TC_DoiTruVaTinhLai_CPM_CPV] @dtStart, @dtEnd, @pSoHopDong, @pHopDongChiTietID, @NgayTinh

	UPDATE dbo.ThucChayDaTinh SET NgayThucHien = @NgayTinh 
	WHERE SoHopDong = @pSoHopDong 
     AND HopDongChiTietREF = @pHopDongChiTietID
     AND (GhiChu = N'ThucChay_InsertThucChayDaTinhCPV_DoiTruVaTinhLai_CPM' 
       OR GhiChu = N'sp_TC_DoiTruVaTinhLai_CPM_CPV')
     AND CONVERT(DATE, CreatedAt) = CONVERT(DATE, GETDATE())
END



----Tinh gia tri thuc chay CPR voi don vi la Goi
--EXEC [sp_TC_DoiTruVaTinhLai_CPM_CPR] @dtStart, @dtEnd, @pSoHopDong, @pHopDongChiTietID, @NgayTinh

----Tinh gia tri thu chay voi don vi la CPR
--EXEC [sp_TC_DoiTruVaTinhLai_CPM_ByDVT_CPR] @dtStart, @dtEnd, @pSoHopDong, @pHopDongChiTietID, @NgayTinh

----Tinh gia tri thuc chay voi don vi la True View
--EXEC sp_TC_DoiTruVaTinhLai_CPM_TrueView @dtStart, @dtEnd, @pSoHopDong, @pHopDongChiTietID, @NgayTinh
```
