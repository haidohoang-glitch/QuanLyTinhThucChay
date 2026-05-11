# Function: `GetNhanVienInfoByNhanVienID`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2013-12-25 17:19:22.587000
- **Ngày sửa cuối**: 2014-10-14 10:39:36.003000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanVienID` | `int(4)` | No |
| `@NgayTinhThucChay` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
-- SELECT * FROM dbo.GetNhanVienInfoByNhanVienID(3,'2013-09-01')
CREATE FUNCTION dbo.GetNhanVienInfoByNhanVienID
(	
	-- Add the parameters for the function here
	@NhanVienID INT,
	@NgayTinhThucChay DATETIME
)
RETURNS TABLE 
AS
RETURN 
(
	-- Add the SELECT statement with parameter references here
	SELECT A.NhanSuSoYeuLyLichREF,
		B.HoVaTen,
		B.Email,
		B.DienThoai AS Mobile,
		A.DmPhongBanREF, C.TenPhongBan,
		A.DmBoPhanREF, D.TenBoPhanNghiepVu,
		A.DmNhomLamViecREF, E.TenNhomLamViec,
		A.DmDiaDiemLamViecREF,
		CASE A.DmDiaDiemLamViecREF 
			WHEN 287 THEN N'Hà Nội'
			WHEN 288 THEN N'Tp. Hồ Chí Minh'
		END AS TenDiaDiemLamViec
	FROM NhanSuQuaTrinhCongTac A
		INNER JOIN NhanSuSoYeuLyLichFull B ON B.NhanSuSoYeuLyLichID = A.NhanSuSoYeuLyLichREF
		LEFT JOIN DmPhongBan C ON C.DmPhongBanID = A.DmPhongBanREF
		LEFT JOIN DmBoPhanNghiepVu D ON D.DmBoPhanNghiepVuID = A.DmBoPhanREF
		LEFT JOIN DmNhomLamViec E ON E.DmNhomLamViecID = A.DmNhomLamViecREF
	WHERE 
		A.NhanSuSoYeuLyLichREF = @NhanVienID
		AND (
			(
				@NgayTinhThucChay BETWEEN CONVERT(DATE,A.NgayBatDauLamViec) AND CONVERT(DATE, ISNULL(A.NgayNghiViec,'3000-01-01'))
			)
			OR
			(
				CONVERT(DATE,A.NgayBatDauLamViec) BETWEEN @NgayTinhThucChay AND @NgayTinhThucChay	
			)
		)
		--AND CONVERT(DATE,A.NgayBatDauLamViec) <= @NgayTinhThucChay
		--AND CONVERT(DATE, ISNULL(A.NgayNghiViec,'3000-01-01')) <= @NgayTinhThucChay
)

```
