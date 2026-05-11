# Function: `fn_GetDauKy_Of_Quy_LoaiNenTang`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-03-07 12:18:14.343000
- **Ngày sửa cuối**: 2015-03-07 12:18:14.343000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@DmLoaiNenTangREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@LoaiDoanhSo` | `int(4)` | No |
| `@isSoLuong` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================

CREATE FUNCTION [dbo].[fn_GetDauKy_Of_Quy_LoaiNenTang] 
(
	-- Add the parameters for the function here
   @DmLoaiNenTangREF INT,
   @NgayThucHien DATETIME,
   @LoaiDoanhSo INT,
   @isSoLuong INT
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @out float
    DECLARE @DateCalc DATETIME 
    SET @DateCalc = DATEADD(QQ,-1,@NgayThucHien)
	-- Add the T-SQL statements to compute the return value here
	IF @isSoLuong = 0
	BEGIN
		SET @out =
		(
			SELECT TOP 1
			(
				CASE WHEN @LoaiDoanhSo = 1 THEN  isnull(dstchdc.ThucChayPhatSinhCuoiKy,0)
					 WHEN @LoaiDoanhSo = 2 THEN  isnull(dstchdc.KhuyenMaiPhatSinhCuoiKy,0)
				  ELSE isnull(dstchdc.NoiBoPhatSinhCuoiKy,0)
				END
			)DoanhSoPhatSinh
			FROM rptThucChay_LoaiNenTang_Quy dstchdc
			WHERE 1 = 1
			AND dstchdc.DmLoaiNenTang = @DmLoaiNenTangREF
			AND dstchdc.Nam = YEAR(@DateCalc) 
			AND dstchdc.Quy = datepart(QQ,@DateCalc)
		)
	END
	ELSE
		BEGIN
			SET @out =
		(
			SELECT TOP 1
			(
				CASE WHEN @LoaiDoanhSo = 1 THEN  isnull(dstchdc.SoLuongPhatSinhCuoiKy,0)
					 WHEN @LoaiDoanhSo = 2 THEN  isnull(dstchdc.SoLuongKhuyenMaiPhatSinhCuoiKy,0)
				  ELSE isnull(dstchdc.SoLuongNoiBoPhatSinhCuoiKy,0)
				END
			)DoanhSoPhatSinh
			FROM rptThucChay_LoaiNenTang_Quy dstchdc
			WHERE 1 = 1
			AND dstchdc.DmLoaiNenTang = @DmLoaiNenTangREF
			AND dstchdc.Nam = YEAR(@DateCalc) 
			AND dstchdc.Quy = datepart(QQ,@DateCalc)
		)
		END
		
		SET @out = ISNULL(@out, 0)
	-- Return the result of the function
	RETURN @out

END

```
