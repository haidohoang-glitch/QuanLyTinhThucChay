# Function: `Fn_LayDanhSachKhachHangByDmNhanHangREF`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-01-25 18:34:41.410000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.490000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar` | Yes |
| `@DmNhanHangREF` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE FUNCTION Fn_LayDanhSachKhachHangByDmNhanHangREF
(
	-- Add the parameters for the function here
	@DmNhanHangREF INT
)
RETURNS nvarchar(MAX)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @DanhSachTenKhangHang nvarchar(MAX);
	
	SET @DanhSachTenKhangHang =
	(
	SELECT 
	
		STUFF(
		(
		SELECT cast(',' as nvarchar(max)) + A.TenKhachHang FROM 
		(
		SELECT distinct hd.TenKhachHang FROM HopDong hd
		INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		WHERE hdct.DanhSachNhanHangREF = CONVERT(NVARCHAR(50),@DmNhanHangREF)
		AND hd.TrangThaiHopDong <> 3
		)A 
		FOR XML PATH('')),1,1,'')
	)
	set @DanhSachTenKhangHang = ISNULL(@DanhSachTenKhangHang,'')
		
	RETURN @DanhSachTenKhangHang;

END


```
