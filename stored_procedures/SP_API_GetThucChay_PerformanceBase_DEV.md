# Stored Procedure: `API_GetThucChay_PerformanceBase_DEV`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-12 09:22:01.480000
- **Ngày sửa cuối**: 2021-06-12 10:32:47.893000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--select * from ThucChay_PerformanceBase_ThayDoi
--[API_GetThucChay_PerformanceBase_DEV] N'qc5870320'
--[API_GetThucChay_PerformanceBase_DEV] N'NB0010421'
CREATE PROCEDURE [dbo].[API_GetThucChay_PerformanceBase_DEV]
    -- Add the parameters for the stored procedure here
    @SoHopDong NVARCHAR(50)
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;
	
    Declare @MHD nvarchar(10)
	set @MHD = (select left (@SoHopDong, 2) )
	
	if @MHD = 'QC' 
		EXEC API_GetThucChay_PerformanceBase_QC_DEV @SoHopDong
	else if  @MHD = 'SH' 
		EXEC API_GetThucChay_PerformanceBase_SHNB_DEV @SoHopDong
	else if  @MHD = 'NB' 
		EXEC API_GetThucChay_PerformanceBase_SHNB_DEV @SoHopDong
END;





```
