# Function: `GetLogGiaTriThayDoiByTime`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2014-07-17 08:28:11.437000
- **Ngày sửa cuối**: 2014-10-14 10:39:36.033000

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
CREATE FUNCTION dbo.GetLogGiaTriThayDoiByTime 
(	
	-- Add the parameters for the function here
	@StartDate DATETIME,
	@EndDate DATETIME
)
RETURNS TABLE 
AS
RETURN 
(
	SELECT DISTINCT
		A.SoHopDong
		,A.DmSanPhamREF
		,(SELECT P.TenSanPham
		  FROM DmSanPhamChuan P WHERE P.DmSanPhamID = A.DmSanPhamREF) TenSanPham
		,A.DmWebsiteREF	
		,(SELECT dwr.WebsiteLink
		  FROM WebsiteMapping_HDCN_Reporting dwr WHERE dwr.DmWebsiteReportingdbID = A.DmWebsiteREF) TenWebsite
		,B.DmPhongBanREF
		,B.DmBoPhanREF
		,B.DmNhomLamViecREF
		,B.SysNhanVienREF
		,CASE WHEN (B.TenDangNhap IS NULL OR B.TenDangNhap = '') THEN 
					'NV_' + CONVERT(nvarchar(50),B.SysNhanVienREF) + '_blank_username'
				ELSE B.TenDangNhap
		END TenDangNhap
		,B.TenNhanVien
		,NoiDungLog 
		,B.GiaTriThayDoi
		,A.NgayThucHien
	FROM ThucChay_LogNNTinhGiaTriThayDoi A
		INNER JOIN ThucChayDaTinh B ON B.HopDongID = A.HopDongREF 
	WHERE 1=1
		--AND CONVERT(DATE,NgayThucHien) Between 'Sep  6 2013 12:00AM' and 'Sep  30 2013 12:00AM' 
		AND A.NgayThucHien BETWEEN @StartDate AND @EndDate
		AND B.GiaTriThayDoi <> 0
		AND B.DmSanPhamREF = 339
)

```
