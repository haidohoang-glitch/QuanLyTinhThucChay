# Stored Procedure: `API_GetThucChay_PerformanceBase_BK1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-15 10:31:12.197000
- **Ngày sửa cuối**: 2021-06-15 10:31:12.197000

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
--[API_GetThucChay_PerformanceBase] N'qc5870320'
CREATE PROCEDURE [dbo].[API_GetThucChay_PerformanceBase_BK1]
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
		EXEC API_GetThucChay_PerformanceBase_QC @SoHopDong
	else if  @MHD = 'SH' 
		EXEC API_GetThucChay_PerformanceBase_SHNB @SoHopDong
	else if  @MHD = 'NB' 
		EXEC API_GetThucChay_PerformanceBase_SHNB @SoHopDong
END;





```
