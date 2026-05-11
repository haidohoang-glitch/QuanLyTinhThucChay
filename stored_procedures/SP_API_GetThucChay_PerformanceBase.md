# Stored Procedure: `API_GetThucChay_PerformanceBase`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-02-02 11:35:52.033000
- **Ngày sửa cuối**: 2024-03-06 16:13:16.007000

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
--[dbo].[API_GetThucChay_PerformanceBase] N'PC0010820'
--[dbo].[API_GetThucChay_PerformanceBase] N'S-NB0010122'
CREATE PROCEDURE [dbo].[API_GetThucChay_PerformanceBase]
    -- Add the parameters for the stored procedure here
    @SoHopDong NVARCHAR(50)
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;
	
    Declare @MHD nvarchar(10)

	--set @MHD = (select left (@SoHopDong, 2) )
	set @MHD = ISNULL((select Top (1) hd.TenMaHopDong from dbo.hopdong hd
						where hd.sohopdong = @SoHopDong ORDER BY hd.hopdongid),'')
	
	if (@MHD IN (N'QC',N'K',N'PC',N'TD',N'S-WC'))
		EXEC API_GetThucChay_PerformanceBase_QC @SoHopDong
	else if  @MHD = 'SH' 
		EXEC API_GetThucChay_PerformanceBase_SHNB @SoHopDong
	else if  @MHD = 'NB' 
		EXEC API_GetThucChay_PerformanceBase_SHNB @SoHopDong
	else if @MHD = 'S-NB'
		EXEC API_GetThucChay_PerformanceBase_SHNB @SoHopDong
END;





```
