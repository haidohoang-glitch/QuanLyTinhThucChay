# Stored Procedure: `API_GetThucChay_PerformanceBase_ThangDuGP`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-08-29 10:34:10.937000
- **Ngày sửa cuối**: 2025-08-05 10:35:01.737000

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

--[dbo].[API_GetThucChay_PerformanceBase_ThangDuGP] N'PC0010820'--'QC7620421'--

CREATE PROCEDURE [dbo].[API_GetThucChay_PerformanceBase_ThangDuGP]
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
	
	if (@MHD IN (N'QC',N'K',N'PC',N'TD',N'S-WC',N'MA',N'P',N'AX'))
		EXEC [dbo].[API_GetThucChay_PerformanceBase_ThangDuGP_QC] @SoHopDong
	else if  @MHD IN(N'SH', N'NB', N'S-NB')
		EXEC [dbo].[API_GetThucChay_PerformanceBase_ThangDuGP_SHNB] @SoHopDong
		
	--HAIDH COMMNET 27/06/2025 TOI UU LAI CODE
	--else if  @MHD = 'NB' 
	--	EXEC [dbo].[API_GetThucChay_PerformanceBase_ThangDuGP_SHNB] @SoHopDong
	--else if @MHD = 'S-NB'
	--	EXEC [dbo].[API_GetThucChay_PerformanceBase_ThangDuGP_SHNB] @SoHopDong
END;





```
