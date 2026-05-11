# Stored Procedure: `ThucChay_DoiTruVaTinhLai_TrueView_Job`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-01-12 09:43:42.397000
- **Ngày sửa cuối**: 2018-01-12 09:43:42.397000

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


CREATE PROCEDURE [dbo].[ThucChay_DoiTruVaTinhLai_TrueView_Job]
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
		
	--Tinh gia tri thuc chay voi don vi la True View
	EXEC sp_TC_DoiTruVaTinhLai_CPM_TrueView @dtStart, @dtEnd, @pSoHopDong, @pHopDongChiTietID, @NgayTinh

END








```
