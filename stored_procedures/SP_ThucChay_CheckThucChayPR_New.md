# Stored Procedure: `ThucChay_CheckThucChayPR_New`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-05 11:11:55.610000
- **Ngày sửa cuối**: 2014-11-19 12:24:50.777000

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
CREATE PROCEDURE [dbo].[ThucChay_CheckThucChayPR_New]
	@StartDate DATETIME,
	@EndDate DATETIME
AS
BEGIN
			SELECT 
			A.SoHopDong,
			A.HopDongID,
			A.HopDongChiTietREF,
			A.NgayThucHien,
			ISNULL(A.SLChay, 0) AS SLThucChay,
			ISNULL(A.SLKM, 0) AS SLThucChayKM,
			ISNULL(A.DonGia, 0) AS DonGia,
			ISNULL(A.TT ,0) AS ThanhTienThucChay,
			B.HopDongREF,
			B.HopDongChiTietREF,
			ISNULL(B.SoLuong,0) AS SLThucTreo,
			ISNULL(B.TT ,0) AS ThanhTienThucTreo,
			(ISNULL(A.SLChay, 0) + ISNULL(A.SLKM, 0) - ISNULL(B.SoLuong,0)) AS SLLech,
			ISNULL(A.TT ,0) - ISNULL(B.TT ,0) AS ThanhTienLech
		FROM
		(
			SELECT tcdt.SoHopDong,
			tcdt.HopDongID,
			tcdt.HopDongChiTietREF,
			tcdt.NgayThucHien,
			SUM(tcdt.SoLuongThucChay) AS SLChay,
			SUM(tcdt.SoLuongThucChayKM) AS SLKM,
			tcdt.DonGia,
			SUM(tcdt.ThanhTienThucChayTruocTrietKhau) AS TT
			FROM   ThucChayDaTinh tcdt
			WHERE  tcdt.DmSanPhamREF IN (141, 245, 250)
			AND CONVERT(date, tcdt.NgayThucHien) BETWEEN @StartDate AND @EndDate
			GROUP BY
			tcdt.SoHopDong,
			tcdt.HopDongID,
			tcdt.HopDongChiTietREF,
			tcdt.DonGia,
			tcdt.NgayThucHien 
		)A
		FULL OUTER JOIN
		(                  
			SELECT 
			ThucChayHopDongChiTietPRID,
			HopDongREF,
			HopDongChiTietREF,
			COUNT(HopDongChiTietREF) AS SoLuong,
			GiaTien,
			GiaTien * COUNT(HopDongChiTietREF) AS TT, 
			CASE WHEN CreatedAt >= LastModifiedAt THEN 
				 CONVERT(date, CreatedAt)
			ELSE CONVERT(date, LastModifiedAt)
			END NgayThucHien 												
			FROM   ThucChayHopDongChiTietPR
			WHERE  (
			CASE 
			WHEN CreatedAt >= LastModifiedAt THEN 
				 CONVERT(date, CreatedAt)
			ELSE CONVERT(date, LastModifiedAt)
			END
			) BETWEEN @StartDate AND @EndDate
			AND HopDongChiTietREF <> 0	                          
			AND DeletedStatus = 0
			GROUP BY
			HopDongREF,
			HopDongChiTietREF,
			GiaTien,
			CreatedAt,
			LastModifiedAt,
			ThucChayHopDongChiTietPRID
		)
		B ON 
		( 
			A.HopDongID = B.HopDongREF
			AND A.HopDongChiTietREF = B.HopDongChiTietREF
			AND A.NgayThucHien = B.NgayThucHien
		)
		WHERE 
		(ISNULL(A.SLChay, 0) + ISNULL(A.SLKM, 0) - ISNULL(B.SoLuong,0)) <> 0 OR 
		ISNULL(A.TT ,0) - ISNULL(B.TT ,0) <> 0
END

```
