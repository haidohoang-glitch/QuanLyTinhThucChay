# Function: `GenderSQLCommandStringByGroupName1`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-14 12:56:55.050000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.113000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@GroupFieldName` | `nvarchar(100)` | No |
| `@FilterString` | `nvarchar(8000)` | No |
| `@IsOrderBy` | `bit(1)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[GenderSQLCommandStringByGroupName1]
(
	-- Add the parameters for the function here
	@GroupFieldName nvarchar(50),
	@FilterString nvarchar(4000),
	@IsOrderBy bit
)
RETURNS nvarchar(4000)
AS
BEGIN

Declare @SQLCommand nvarchar(4000)
Declare @DauNhay nvarchar(50)
Declare @GroupByFildID nvarchar(50)
Declare @GroupByFild nvarchar(50)

set @DauNhay = ''''

IF UPPER(@GroupFieldName) = 'TENSANPHAM'
	Begin
		SET @GroupByFild = 'DmSanPhamREF,'
		SET @GroupByFildID = 'DmSanPhamREF AS ID,' 
	End
ELSE IF UPPER(@GroupFieldName) = 'TENWEBSITE'
	Begin
		SET @GroupByFild = 'DmWebsiteREF,'
		SET @GroupByFildID = 'DmWebsiteREF AS ID,' 
	End
ELSE IF UPPER(@GroupFieldName) = 'TENPHONGBAN'
	Begin
		SET @GroupByFild = 'DmPhongBanREF,'
		SET @GroupByFildID = 'DmPhongBanREF AS ID,' 
	End
ELSE IF UPPER(@GroupFieldName) = 'TENBOPHAN'
	Begin
		SET @GroupByFild = 'DmBoPhanREF,'
		SET @GroupByFildID = 'DmBoPhanREF AS ID,' 
	End
ELSE IF UPPER(@GroupFieldName) = 'TENNHOMLAMVIEC'
	Begin
		SET @GroupByFild = 'DmNhomLamViecREF,'
		SET @GroupByFildID = 'DmNhomLamViecREF AS ID,' 
	End
ELSE
	Begin
		SET @GroupByFildID = ''
		SET @GroupByFild = ''
	End

set @SQLCommand = '

SELECT
' + @GroupByFildID + 
  +@GroupFieldName+ '
,dbo.FormatDonViTinh(DonViTinh) AS DonViTinh,
SUM(GiaTriThayDoi) AS GiaTriThayDoi,
0 AS SoLuongHopDongKhuyenMai,
0 AS SoLuongThucChayKhuyenMai,
0 AS SoLuongHopDongNoiBo,
0 AS SoLuongThucChayNoiBo,
ISNULL(ROUND(SUM(CAST(SoLuong AS BIGINT)),0),0) AS SoLuongHopDongThucThu,
ISNULL(ROUND(SUM(SoLuongThucChay),0),0) AS SoLuongThucChayThucThu,
0 AS ThanhTienKhuyenMai,
0 AS ThanhTienNoiBo,
ISNULL(ROUND(SUM(ThanhTienThucThu),0),0) AS ThanhTienThucThu
FROM dbo.ThucChay_ViewBizAll
WHERE UPPER(TenMaHopDong) <> '+ @DauNhay + 'NB'+ @DauNhay +' AND IsKhuyenMai <> 1 '
+ @FilterString + 
' GROUP BY ' + @GroupFieldName+ ',' + @GroupByFild +
'dbo.FormatDonViTinh(DonViTinh) '

if(@IsOrderBy = 1)
	set @SQLCommand = @SQLCommand +' Order By 
	' + 
	@GroupFieldName +
	',dbo.FormatDonViTinh(DonViTinh) '
	-- Return the result of the function
	RETURN @SQLCommand

END
```
