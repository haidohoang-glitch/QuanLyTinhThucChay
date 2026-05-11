# Function: `AdmarketGetQuaTrinhCongTacByNhanVien`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2013-12-25 17:19:22.843000
- **Ngày sửa cuối**: 2014-10-14 10:39:38.127000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuSoYeuLyLichREF` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-12-18
-- Description:	<Description,,>
-- =============================================
CREATE FUNCTION [dbo].[AdmarketGetQuaTrinhCongTacByNhanVien]
(	
	-- Add the parameters for the function here
	@NhanSuSoYeuLyLichREF int,
	@StartDate datetime,
	@EndDate datetime
)
RETURNS TABLE 
AS
RETURN 
(
	SELECT 
		A.NhanSuQuaTrinhCongTacID, NhanSuSoYeuLyLichREF,
		A.DmPhongBanREF, B.TenPhongBan,
		A.DmBoPhanREF, C.TenBoPhanNghiepVu,
		A.DmNhomLamViecREF, D.TenNhomLamViec,
		A.DmDiaDiemLamViecREF,
		CASE A.DmDiaDiemLamViecREF
			WHEN 287 THEN N'Hà Nội'
			WHEN 288 THEN N'TP HCM'
		END TenDiaDiemLamViec,
		A.Active,
		A.NgayBatDauLamViec,
		A.NgayNghiViec
	FROM NhanSuQuaTrinhCongTac A
		LEFT JOIN DmPhongBan B ON B.DmPhongBanID = A.DmPhongBanREF
		LEFT JOIN DmBoPhanNghiepVu C ON C.DmBoPhanNghiepVuID = A.DmBoPhanREF
		LEFT JOIN DmNhomLamViec D ON D.DmNhomLamViecID = A.DmNhomLamViecREF
	WHERE 
		A.NhanSuSoYeuLyLichREF = @NhanSuSoYeuLyLichREF
		AND 
		(
			(@StartDate BETWEEN A.NgayBatDauLamViec AND ISNULL(A.NgayNghiViec,'3000-01-01'))
			OR (@EndDate BETWEEN A.NgayBatDauLamViec AND ISNULL(A.NgayNghiViec,'3000-01-01'))
			OR (CONVERT(DATE,A.NgayBatDauLamViec) <= @EndDate AND CONVERT(DATE,ISNULL(A.NgayNghiViec,'3000-01-01')) >= @StartDate)
			OR (CONVERT(DATE,A.NgayBatDauLamViec) BETWEEN @StartDate AND @EndDate)
		)
)

```
