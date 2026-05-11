# Function: `ThucChay_GetDonGiaByNgayThucHien`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2017-09-11 15:02:50.223000
- **Ngày sửa cuối**: 2017-09-11 15:02:50.223000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@DonGia` | `float(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetDonGiaByNgayThucHien]
(	
	@NgayThucHien datetime,
	@HopDongChiTietID int,
	@DonGia float
)
RETURNS float

AS
BEGIN
	
	DECLARE @Result FLOAT
	/*
	SET @Result =
		(				
							SELECT Top 1 A.DonGia
							FROM dbo.HopDongChiTietThayDoi A
							INNER JOIN dbo.HopDongThayDoi B ON A.HopDongFK = B.HopDongFK
							WHERE 
							A.DeletedStatus <> 1 AND 
							B.DeletedStatus <> 1 AND
							A.HopDongChiTietREF = @HopDongChiTietID AND
							B.NgayThayDoi >= @NgayThucHien 
							Order by B.NgayThayDoi Desc
		)
	*/ --Hien dang dung gia hien tai, ve sau tinh tinh nhu cach o tren
	SET @Result = 
	(				
							SELECT Top 1 hdct.DonGia
							FROM dbo.HopDongChiTiet hdct
							WHERE hdct.DeletedStatus <> 1 AND 
							hdct.HopDongChiTietID = @HopDongChiTietID 
	)
	set @Result = Isnull(@Result,@DonGia)
	
	return @Result
End

```
