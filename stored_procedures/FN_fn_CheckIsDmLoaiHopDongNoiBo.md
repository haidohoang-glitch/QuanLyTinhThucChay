# Function: `fn_CheckIsDmLoaiHopDongNoiBo`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-02-10 09:59:56.500000
- **Ngày sửa cuối**: 2015-02-10 09:59:56.500000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@DmLoaiHopDongREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[fn_CheckIsDmLoaiHopDongNoiBo]
(
	@DmLoaiHopDongREF  INT,
	@NgayThucHien      DATETIME
)
RETURNS INT

BEGIN
	DECLARE @out INT
	SET @out = 0 --Khong phai la hd noi bo
	SET @out = (
	        SELECT COUNT(loaihd.DmLoaiHopDongNoiBoID)
	        FROM   DmLoaiHopDongNoiBo loaihd
	        WHERE  1 = 1
				   AND loaihd.DmLoaiHopDongREF = @DmLoaiHopDongREF
	               AND loaihd.DeletedStatus = 0
	               AND CONVERT(date, @NgayThucHien) BETWEEN loaihd.ThoiGiaBatDauHieuLuc 
	                   AND loaihd.ThoiGianKetThucHieuLuc
	    )
	
	SET @out = ISNULL(@out, 0)
	
	RETURN @out;
END

```
