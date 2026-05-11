# Function: `Rpt_GetTinhTrangNhanHang`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-04-22 17:42:28.773000
- **Ngày sửa cuối**: 2014-10-14 11:28:39.397000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(200)` | Yes |
| `@DmNhanHangREF` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author then 		<Author,,Name>
-- Create date then  <Create Date, ,>
-- Description then 	<Description, ,>
-- =============================================
CREATE  FUNCTION [dbo].[Rpt_GetTinhTrangNhanHang]
(
	-- Add the parameters for the function here
	@DmNhanHangREF INT,
	@StartDate DATETIME,
	@EndDate DATETIME
)
RETURNS nvarchar(100)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result nvarchar(100), @CountHdOfNhan INT, @TinhTrangNhanHang NVARCHAR(100)
	DECLARE @MinNgayDanhSoHD DATETIME, @MaxNgayDanhSoHD DATETIME
	
	SET @TinhTrangNhanHang = ''
	
	SET @CountHdOfNhan =
	(
		SELECT COUNT(rnhttct.SoHopDong) 
		FROM RptNhanHangThongTinChiTiet rnhttct
		WHERE rnhttct.DmNhanHangREF = @DmNhanHangREF
		--AND CONVERT(date,rnhttct.NgayThucHien) BETWEEN @StartDate AND @EndDate
	)
	IF(@CountHdOfNhan >0)
	BEGIN
		SELECT @MaxNgayDanhSoHD = MAX(rnhttct.NgayThucHien), @MinNgayDanhSoHD = MIN(rnhttct.NgayThucHien)
		FROM RptNhanHangThongTinChiTiet rnhttct
		WHERE rnhttct.DmNhanHangREF = @DmNhanHangREF
		IF(@MinNgayDanhSoHD >@EndDate)
		BEGIN
			set @TinhTrangNhanHang = N'Chua ch?y'
		END
		ELSE
			BEGIN
				set @TinhTrangNhanHang = N'Ðang ch?y'
			END
	END
	ELSE
		BEGIN
			SET @TinhTrangNhanHang = N'Nhãn hàng chua ch?y'
		END
	SET @Result = @TinhTrangNhanHang	
	RETURN @Result

END

```
