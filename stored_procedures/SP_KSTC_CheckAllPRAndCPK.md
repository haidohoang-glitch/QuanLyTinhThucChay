# Stored Procedure: `KSTC_CheckAllPRAndCPK`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-08 17:24:48.357000
- **Ngày sửa cuối**: 2014-12-08 17:24:48.357000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE dbo.KSTC_CheckAllPRAndCPK 
	-- Add the parameters for the stored procedure here
	@StartDate DATETIME,
	@EndDate DATETIME,
	@DmSanPhamREF INT
AS
BEGIN
IF @DmSanPhamREF = 141
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
	AND tchdct.RecordStatus = 1
	 AND (CONVERT(date, tchdct.CreatedAt) BETWEEN @StartDate AND @EndDate
	   OR CONVERT(date, tchdct.LastModifiedAt) BETWEEN @StartDate AND @EndDate)
	 AND tchdct.DeletedStatus = 0
	 GROUP BY tchdct.HopDongChiTietREF, tchdct.HopDongREF
	 )A
	 FULL OUTER JOIN
	 (
	 SELECT HopDongChiTietREF,HopDongID,SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)TCDT
	 FROM ThucChayDaTinh tcdt  
	 WHERE 
	 NgayThucHien BETWEEN @StartDate AND @EndDate
	 AND tcdt.HopDongChiTietREF IN (SELECT HopDongChiTietREF
									  FROM ThucChayDaTinh WHERE YEAR(NgayThucHien) = 2014)
	 GROUP BY tcdt.HopDongID, tcdt.HopDongChiTietREF 
	 )B
	 ON A.HopDongChiTietREF = B.HopDongChiTietREF
	 AND A.HopDongREF = B.HopDongID
		WHERE A.TT <> B.TCDT
		 OR A.TT IS NULL 
		 OR B.TCDT IS NULL
	END
ELSE
	BEGIN
		SELECT A.*,B.* FROM (
		 SELECT HopDongChiTietREF,HopDongREF, sum(hdct.DonGia * (100-hdct.ChietKhau)/100)TT
		 FROM ThucChayHopDongChiTiet tchdct 
		  INNER JOIN HopDongChiTiet hdct ON 
		 tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
		 AND tchdct.HopDongREF = hdct.HopDongFK
		 WHERE tchdct.DeletedStatus <> 1
		 AND hdct.DeletedStatus <> 1
		 AND tchdct.ThoiGianBatDau >= '2013-01-01'
		AND tchdct.RecordStatus = 1
		 AND (CONVERT(date, tchdct.CreatedAt) BETWEEN @StartDate AND @EndDate
		   OR CONVERT(date, tchdct.LastModifiedAt) BETWEEN @StartDate AND @EndDate)
		 AND tchdct.DeletedStatus = 0
		 GROUP BY tchdct.HopDongChiTietREF, tchdct.HopDongREF
		 )A
		 FULL OUTER JOIN
		 (
		 SELECT HopDongChiTietREF,HopDongID,SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)TCDT
		 FROM ThucChayDaTinh tcdt  
		 WHERE 
		 NgayThucHien BETWEEN @StartDate AND @EndDate
		 AND tcdt.HopDongChiTietREF IN (SELECT HopDongChiTietREF
										  FROM ThucChayDaTinh WHERE YEAR(NgayThucHien) = 2014)
		 GROUP BY tcdt.HopDongID, tcdt.HopDongChiTietREF 
		 )B
		 ON A.HopDongChiTietREF = B.HopDongChiTietREF
		 AND A.HopDongREF = B.HopDongID
		WHERE A.TT <> B.TCDT
		 OR A.TT IS NULL 
		 OR B.TCDT IS NULL
	END
END

```
