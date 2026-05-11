# Stored Procedure: `KSCT_CheckThucTreoAndThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-08 17:20:09.350000
- **Ngày sửa cuối**: 2014-12-08 17:20:09.350000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE dbo.KSCT_CheckThucTreoAndThucChayDaTinh 
	-- Add the parameters for the stored procedure here
	@StartDate DATETIME, 
	@EndDate datetime
AS
BEGIN
SELECT A.*,B.* FROM (
 SELECT HopDongChiTietREF,HopDongREF, sum(tchdct.GiaTien * (100-hdct.ChietKhau)/100)TT
 FROM ThucChayHopDongChiTietPR tchdct 
  INNER JOIN HopDongChiTiet hdct ON 
 tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
 AND tchdct.HopDongREF = hdct.HopDongFK
 WHERE tchdct.DeletedStatus <> 1
 AND hdct.DeletedStatus <> 1
 AND tchdct.ThoiGianBatDau >= '2013-01-01'
 AND (CONVERT(date, tchdct.CreatedAt) BETWEEN @StartDate AND @EndDate
   OR CONVERT(date, tchdct.CreatedAt) BETWEEN @StartDate AND @EndDate)
 AND tchdct.DeletedStatus = 0
 GROUP BY tchdct.HopDongChiTietREF, tchdct.HopDongREF
 )A
 FULL OUTER JOIN
 (
 SELECT HopDongChiTietREF,HopDongID,SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)TCDT
 FROM ThucChayDaTinh tcdt  
 WHERE 
 NgayThucHien BETWEEN @StartDate AND @EndDate
 GROUP BY tcdt.HopDongID, tcdt.HopDongChiTietREF 
 )B
 ON A.HopDongChiTietREF = B.HopDongChiTietREF
 AND A.HopDongREF = B.HopDongID
    WHERE A.TT <> B.TCDT
     OR A.TT IS NULL 
     OR B.TCDT IS NULL

END

```
