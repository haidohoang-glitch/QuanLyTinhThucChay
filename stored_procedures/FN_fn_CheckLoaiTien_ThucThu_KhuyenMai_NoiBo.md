# Function: `fn_CheckLoaiTien_ThucThu_KhuyenMai_NoiBo`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-02-10 09:59:56.283000
- **Ngày sửa cuối**: 2015-02-10 09:59:56.283000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@ChietKhau` | `int(4)` | No |
| `@IsKhuyenMai` | `int(4)` | No |
| `@DmLoaiHopDongREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[fn_CheckLoaiTien_ThucThu_KhuyenMai_NoiBo]
(
	@ChietKhau         INT,
	@IsKhuyenMai       INT,
	@DmLoaiHopDongREF  INT,
	@NgayThucHien      DATETIME
)
RETURNS INT

BEGIN
	DECLARE @LoaiTien INT -- 1 NB, 2 KM, 3 ThucThu
	DECLARE @out INT
	--CHECK HOP DONG CO LA HOP DONG NOI BO KHONG
	SET @out = 0 --Khong phai la hd noi bo
	SET @out = (
	        SELECT COUNT(loaihd.DmLoaiHopDongNoiBoID)
	        FROM   DmLoaiHopDongNoiBo loaihd
	        WHERE  1 = 1
	               AND loaihd.DeletedStatus = 0
	               AND CONVERT(date, @NgayThucHien) BETWEEN loaihd.ThoiGiaBatDauHieuLuc 
	                   AND loaihd.ThoiGianKetThucHieuLuc
	    )
	
	SET @out = ISNULL(@out, 0)
	IF (@out > 0)
	    SET @LoaiTien = 1
	        
	ELSE
	--NEU HOP DONG KHONG PHAI LA NOI BO
	BEGIN
	    IF (@ChietKhau = 100 OR @IsKhuyenMai = 1)
	        SET @LoaiTien = 2
	    ELSE
	        SET @LoaiTien = 3
	END
	
	RETURN @LoaiTien;
END

```
