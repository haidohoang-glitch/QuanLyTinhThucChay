# Function: `ThucChay_CheckLenhNgayTreoHa`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-13 17:20:58.777000
- **Ngày sửa cuối**: 2014-10-14 10:39:33.977000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@DanhSachDmBookingREF` | `nvarchar(200)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_CheckLenhNgayTreoHa]
(
	-- Add the parameters for the function here
	@DanhSachDmBookingREF NVARCHAR(100), 
	@NgayThucHien datetime
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result INT
	
			
	IF(DATALENGTH(@DanhSachDmBookingREF) >0) 
		BEGIN
			SET @Result = (
					select count(*) from dbo.DotChayHopDongChiTiet
					where convert(nvarchar(50),BookingREF) in (select DanhsachDmBookingREF from dbo.ThucChay)
					AND ThoiGianBatDau <= @NgayThucHien
					AND ThoiGianKetThuc >= @NgayThucHien
					AND DeletedStatus = 0
					)
		END
	RETURN @Result;

END

```
