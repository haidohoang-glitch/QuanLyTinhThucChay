# Stored Procedure: `ThucChay_TinhCPM_BySQLJobs_BySanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-07-09 15:55:56.240000
- **Ngày sửa cuối**: 2022-01-17 16:19:14.600000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@dtStart` | `datetime(8)` | No |
| `@dtEnd` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--[ThucChay_TinhCPM_BySQLJobs_BySanPham] 613
/*
EXEC [dbo].[ThucChay_TinhCPM_BySQLJobs_BySanPham] '2022-01-15', '2022-01-15', 240
*/
CREATE PROCEDURE [dbo].[ThucChay_TinhCPM_BySQLJobs_BySanPham]
	-- Add the parameters for the stored procedure here
	@dtStart DATETIME,
	@dtEnd DATETIME , 
	@DmSanPhamREF INT 
AS
BEGIN
	--DECLARE @dtStart DATETIME, @dtEnd DATETIME
		
	--SET @dtStart = '2017-05-16'
	--SET @dtEnd =  '2017-05-16'
	
	--Tinh Thuc Chay CPM
	EXEC [dbo].[ThucChay_HopDongChiTietAndBanner_BySanPham] @dtEnd,@DmSanPhamREF
	
	EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_BySanPham] @DmSanPhamREF
		
	EXEC [dbo].[ThucChay_ExcInsertThucChayDaTinh_BySanPham] 
	@StartDate = @dtStart,
	@EndDate = @dtEnd,
	@DmSanPhamREF = @DmSanPhamREF

	EXEC [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_CPM_BySanPham] 
    @StartDate = @dtStart ,
    @EndDate = @dtEnd ,
    @pSoHopDong= NULL,
    @pDmSanPhamREF = @DmSanPhamREF

END

--EXEC [dbo].[ThucChay_TinhCPM_BySQLJobs]

```
