# Function: `f_ReturnListConcatNhanHangREF_v2`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2016-03-30 11:35:45.733000
- **Ngày sửa cuối**: 2016-03-30 14:34:07.670000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar(2000)` | Yes |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
/*
select [dbo].[f_ReturnListConcatNhanHangREF_v2] (13044,'')
* */
CREATE FUNCTION [dbo].[f_ReturnListConcatNhanHangREF_v2] 
(
	@HopDongChiTietREF  INT,
	@NgayThucHien DATETIME
)
RETURNS VARCHAR(2000)

BEGIN
	DECLARE @out NVARCHAR(2000);
	SELECT @out = COALESCE(@out + ',', '') + CAST(T.DmNhanHangREF AS VARCHAR(1000))
	FROM   (
	           SELECT distinct  tchdct.DmNhanHangREF 
	           FROM ThucChayHopDongChiTiet tchdct
				WHERE tchdct.DeletedStatus = 0
				AND tchdct.HopDongChiTietREF = @HopDongChiTietREF
				AND NOT (tchdct.ThoiGianBatDau > @NgayThucHien OR tchdct.ThoiGianKetThuc < @NgayThucHien)
	       ) T	       	
	
	IF(@out IS NULL)
	BEGIN
		SELECT @out = COALESCE(@out + ',', '') + CAST(T.DmNhanHangREF AS VARCHAR(1000))
	FROM   (
	           SELECT distinct  tchdct.DmNhanHangREF 
	           FROM ThucChayHopDongChiTiet tchdct
				WHERE tchdct.DeletedStatus = 0
				AND tchdct.HopDongChiTietREF = @HopDongChiTietREF
	       ) T	
	END 
	SET @out = ISNULL(@out,'')
	RETURN @out;
END
```
