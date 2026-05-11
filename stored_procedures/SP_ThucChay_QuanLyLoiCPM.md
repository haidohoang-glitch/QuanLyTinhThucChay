# Stored Procedure: `ThucChay_QuanLyLoiCPM`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-10-26 08:16:02.360000
- **Ngày sửa cuối**: 2017-01-10 15:46:03.780000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@MaXacDinhLoi` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@IsXemLoi` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC ThucChay_QuanLyLoiCPM -1, '2013-10-24','2013-10-24',1

CREATE PROCEDURE [dbo].[ThucChay_QuanLyLoiCPM]
	-- Add the parameters for the stored procedure here
	@MaXacDinhLoi INT,
	@StartDate datetime,
	@EndDate DATETIME,
	@IsXemLoi INT
AS
BEGIN

IF(@IsXemLoi = 1)
BEGIN
IF(@MaXacDinhLoi <> -1)
	SELECT 
	DISTINCT
	SoHopDong,
	TenSanPham,
	DmSanPhamREF,
	NoiDungLoi,
	TrangThaiLoi
	FROM ThucChayKiemTra_CPM
	WHERE 
	1=1
	--AND TongViewDaTinh <> TongViewKiemTra
	AND ((TongViewDaTinh - TongViewKiemTra >=100) OR (TongViewDaTinh - TongViewKiemTra < -100))
	AND SoHopDong NOT LIKE '%hd_demo%'
	AND SoHopDong NOT LIKE '%HD_DEMO%'
	AND SoHopDong NOT LIKE '%hd_test%'
	AND SoHopDong NOT LIKE '%doitac_cpm7k%'
	AND SoHopDong NOT LIKE '%AD%'
	AND TrangThaiLoi LIKE '%'+CONVERT(NVARCHAR(50),@MaXacDinhLoi)+'%'
	AND NgayThucHien BETWEEN @StartDate AND @EndDate
ELSE
	SELECT 
	DISTINCT
	SoHopDong,
	TenSanPham,
	DmSanPhamREF,
	NoiDungLoi,
	TrangThaiLoi
	FROM ThucChayKiemTra_CPM
	WHERE 
	1=1
	--AND TongViewDaTinh <> TongViewKiemTra
	AND ((TongViewDaTinh - TongViewKiemTra >=100) OR (TongViewDaTinh - TongViewKiemTra < -100))
	AND SoHopDong NOT LIKE '%hd_demo%'
	AND SoHopDong NOT LIKE '%HD_DEMO%'
	AND SoHopDong NOT LIKE '%hd_test%'
	AND SoHopDong NOT LIKE '%doitac_cpm7k%'
	AND SoHopDong NOT LIKE '%AD%'
	AND NgayThucHien BETWEEN @StartDate AND @EndDate
END
ELSE
	SELECT 
	DISTINCT
	SoHopDong,
	TenSanPham,
	DmSanPhamREF,
	NoiDungLoi,
	TrangThaiLoi
	FROM ThucChayKiemTra_CPM
	WHERE 
	1=1
	AND TongViewDaTinh = TongViewKiemTra
	AND SoHopDong NOT LIKE '%hd_demo%'
	AND SoHopDong NOT LIKE '%HD_DEMO%'
	AND SoHopDong NOT LIKE '%hd_test%'
	AND SoHopDong NOT LIKE '%doitac_cpm7k%'
	AND SoHopDong NOT LIKE '%AD%'
	AND NgayThucHien BETWEEN @StartDate AND @EndDate
	ORDER BY DmSanPhamREF
END

```
