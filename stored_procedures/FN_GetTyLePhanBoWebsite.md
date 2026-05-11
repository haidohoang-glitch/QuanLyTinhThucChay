# Function: `GetTyLePhanBoWebsite`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-12-02 11:00:00.203000
- **Ngày sửa cuối**: 2014-10-14 10:39:35.013000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TagID` | `int(4)` | No |
| `@Website` | `nvarchar(100)` | No |
| `@ThoiGianThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql

CREATE FUNCTION [dbo].[GetTyLePhanBoWebsite] 
(
	-- Add the parameters for the function here
	@DmSanPhamREF int,
	@TagID int,
	@Website nvarchar(50),
	@ThoiGianThucHien datetime
)
RETURNS float
AS
BEGIN
	
	Declare @TyLePhanBoWebsite float, @PageView float, @SumPageView float
	
	
	set @PageView = (
						select sum(PageView) from dbo.TyLePhanBoWebsite
						where 
						DmSanPhamREF = @DmSanPhamREF
						and TagID = @TagID
						and UPPER(Website) = UPPER(@Website)
						and @ThoiGianThucHien between ThoiGianBatDau and ThoiGianKetThuc
					)

	set @SumPageView = (
						select sum(PageView) from dbo.TyLePhanBoWebsite
						where 
						DmSanPhamREF = @DmSanPhamREF
						and TagID = @TagID
						and @ThoiGianThucHien between ThoiGianBatDau and ThoiGianKetThuc
					)
	
	set @TyLePhanBoWebsite = @PageView/@SumPageView
	
	-- Return the result of the function
	RETURN @TyLePhanBoWebsite

END

```
