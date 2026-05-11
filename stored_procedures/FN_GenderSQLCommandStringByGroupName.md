# Function: `GenderSQLCommandStringByGroupName`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-09 13:07:55.040000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.140000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@GroupFieldName` | `nvarchar(100)` | No |
| `@FilterString` | `nvarchar(8000)` | No |
| `@IsOrderBy` | `bit(1)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[GenderSQLCommandStringByGroupName]
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
set @DauNhay = ''''

set @SQLCommand = '

SELECT
NgayThucHien,HopDongChiTietREF,
'+@GroupFieldName+ '
,dbo.FormatDonViTinh(DonViTinh) AS DonViTinh,
SUM(GiaTriThayDoi) AS GiaTriThayDoi,
ISNULL(dbo.ThucChay_TongSoLuongHopDongDoiTuongKhuyenMai('+ @GroupFieldName+',NgayThucHien,'+ @DauNhay + @GroupFieldName+ @DauNhay + '),0) AS SoLuongHopDongKhuyenMai,
ISNULL(dbo.ThucChay_TongSoLuongThucChayDoiTuongKhuyenMai('+ @GroupFieldName+',NgayThucHien,'+ @DauNhay + @GroupFieldName+ @DauNhay + '),0) AS SoLuongThucChayKhuyenMai,
ISNULL(dbo.ThucChay_TongSoLuongHopDongDoiTuongNoiBo('+ @GroupFieldName+',NgayThucHien,'+ @DauNhay + @GroupFieldName+ @DauNhay +'),0) AS SoLuongHopDongNoiBo,
ISNULL(dbo.ThucChay_TongSoLuongThucChayDoiTuongNoiBo('+ @GroupFieldName+',NgayThucHien,'+ @DauNhay + @GroupFieldName+ @DauNhay +'),0) AS SoLuongThucChayNoiBo,
ISNULL(SUM(SoLuong),0) AS SoLuongHopDongThucThu,
ISNULL(SUM(SoLuongThucChay),0) AS SoLuongThucChayThucThu,
ISNULL(dbo.ThucChay_TongGiaTriDoiTuongKhuyenMai('+ @GroupFieldName+',NgayThucHien,'+ @DauNhay + @GroupFieldName+ @DauNhay +'),0) AS ThanhTienKhuyenMai,
ISNULL(dbo.ThucChay_TongGiaTriDoiTuongNoiBo('+ @GroupFieldName+',NgayThucHien,'+ @DauNhay + @GroupFieldName+ @DauNhay +'),0) AS ThanhTienNoiBo,
ISNULL(SUM(ThanhTienThucThu),0) AS ThanhTienThucThu
FROM dbo.ThucChay_ViewBizAll
WHERE UPPER(TenMaHopDong) <> '+ @DauNhay + 'NB'+ @DauNhay +' AND IsKhuyenMai <> 1 '
+ @FilterString + 
' GROUP BY ' + @GroupFieldName+
',NgayThucHien,DonViTinh,HopDongChiTietREF'

if(@IsOrderBy = 1)
	set @SQLCommand = @SQLCommand +' Order By 
	NgayThucHien,' + 
	@GroupFieldName +
	',DonViTinh,HopDongChiTietREF'
	-- Return the result of the function
	RETURN @SQLCommand

END
```
