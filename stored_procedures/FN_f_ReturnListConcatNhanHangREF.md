# Function: `f_ReturnListConcatNhanHangREF`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2016-03-17 09:20:57.253000
- **Ngày sửa cuối**: 2016-03-17 09:20:57.253000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar(2000)` | Yes |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql
/*
select [dbo].[f_ReturnListConcatNhanHangREF] (13044)
* */
CREATE FUNCTION [dbo].[f_ReturnListConcatNhanHangREF] 
(
	@HopDongChiTietREF  INT
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
	       ) T	       	
	
	RETURN @out;
END
```
