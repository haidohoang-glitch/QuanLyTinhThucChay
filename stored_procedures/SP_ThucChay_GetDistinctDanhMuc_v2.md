# Stored Procedure: `ThucChay_GetDistinctDanhMuc_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-26 14:34:43.983000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.370000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@GroupFieldName` | `nvarchar(100)` | No |
| `@StartDate` | `date(3)` | No |
| `@EndDate` | `date(3)` | No |
| `@DmSanPhamREFList` | `nvarchar(8000)` | No |
| `@DmWebsiteREFList` | `nvarchar(8000)` | No |
| `@SoHopDongList` | `nvarchar(8000)` | No |
| `@DmPhongBanREFList` | `nvarchar(8000)` | No |
| `@DmBoPhanREFList` | `nvarchar(8000)` | No |
| `@DmNhomLamViecREFList` | `nvarchar(8000)` | No |
| `@TenNhanVienList` | `nvarchar(8000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@KeyWord` | `nvarchar(510)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_GetDistinctDanhMuc]
--	-- Add the parameters for the stored procedure here
--	@GroupFieldName = 'TenSanPham',
--	@StartDate = '1/1/0001 12:00:00 AM',
--	@EndDate = '1/1/0001 12:00:00 AM',
--	@DmSanPhamREFList ='',
--	@DmWebsiteREFList ='',
--	@SoHopDongList ='',
--	@DmPhongBanREFList ='',
--	@DmBoPhanREFList ='',
--	@DmNhomLamViecREFList ='',
--	@TenNhanVienList =''

-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-06-26
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_GetDistinctDanhMuc_v2]
	-- Add the parameters for the stored procedure here
	@GroupFieldName			nvarchar(50),
	@StartDate				date,
	@EndDate				date,
	@DmSanPhamREFList		nvarchar(4000),
	@DmWebsiteREFList		nvarchar(4000),
	@SoHopDongList			nvarchar(4000),
	@DmPhongBanREFList		nvarchar(4000),
	@DmBoPhanREFList		nvarchar(4000),
	@DmNhomLamViecREFList	nvarchar(4000),
	@TenNhanVienList		nvarchar(4000),
	@TenDangNhap			nvarchar(50),
	@KeyWord				NVARCHAR(255)
AS
BEGIN
	DECLARE @sql VARCHAR(8000) ='';

	DECLARE @RecordCound INT = '15';    
	
	-- San pham
	IF @GroupFieldName = 'TenSanPham' 
		SELECT TOP (@RecordCound) 
			DmSanPhamID AS ID, 
			TenSanPham AS [NAME]
		FROM DmSanPham A
		WHERE 1 = 1
			AND A.TenSanPham LIKE N'' + @KeyWord + '%'
			AND A.DeletedStatus = 0			
		ORDER BY
			A.TenSanPham;
	-- Website
	ELSE IF @GroupFieldName = 'TenWebsite'
		SELECT TOP (@RecordCound)
			A.DmWebsiteReportingdbID AS ID, 
			A.TenWebsite AS [NAME]
		FROM DmWebsiteReportingdb A 
		WHERE 1 = 1			
			AND A.TenWebsite LIKE N'' + @KeyWord + '%'
			AND A.DeletedStatus = 0
END

```
