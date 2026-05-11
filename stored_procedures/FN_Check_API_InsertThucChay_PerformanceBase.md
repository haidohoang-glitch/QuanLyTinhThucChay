# Function: `Check_API_InsertThucChay_PerformanceBase`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2021-02-02 13:29:57.137000
- **Ngày sửa cuối**: 2021-02-04 09:48:27.093000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@HopDongChiTietID` | `int(4)` | No |
| `@Tk_Admarket` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@SoTienThayDoi` | `float(8)` | No |
| `@NgayGhiNhanThucChay` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[Check_API_InsertThucChay_PerformanceBase] 
(
	-- Add the parameters for the function here
	@HopDongChiTietID int,
	@Tk_Admarket nvarchar(50),
	@DmSanPhamREF int,
	@DmViTriREF int,
	@SoTienThayDoi float,
	@NgayGhiNhanThucChay datetime
)
RETURNS int
AS
BEGIN
Declare @RecordStatus int
Set @RecordStatus = 0

	-- Declare the return variable here
	--1. Kiem tra NgayGhiNhanThucChay
	IF @NgayGhiNhanThucChay >= convert(date,getdate())
	set @RecordStatus = 0
	
	-- Return the result of the function
	RETURN @RecordStatus

END



	--  exec API_GetThucChay_PerformanceBase 'QC0110121'
```
