# Function: `Rpt_CheckNhanCoMutilNhan`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-04-22 17:42:30.030000
- **Ngày sửa cuối**: 2014-10-14 11:28:40.907000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(200)` | Yes |
| `@DmNhanHangREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author then 		<Author,,Name>
-- Create date then  <Create Date, ,>
-- Description then 	<Description, ,>
-- =============================================
CREATE  FUNCTION [dbo].[Rpt_CheckNhanCoMutilNhan]
(
	-- Add the parameters for the function here
	@DmNhanHangREF INT
)
RETURNS nvarchar(100)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result nvarchar(100), @count_hdct INT
	SET @Result = 'Khong co Mutile Nhan'
	set @count_hdct = 
	(
		SELECT count(hdct.HopDongChiTietID) FROM HopDong hd
		INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		WHERE hd.TrangThaiHopDong <> 3
		AND hd.IsBanCung = 1
		AND hdct.DeletedStatus = 0
		AND @DmNhanHangREF IN (
					SELECT dbo.FormatString(item) DmNhanHang
					FROM dbo.ArrayToTable(dbo.Array(hdct.DanhSachNhanHangREF,',') )
		)
		AND hdct.DanhSachNhanHangREF LIKE '%,%'
	)
	IF(@count_hdct >0)
		SET @Result = 'Co Mutil Nhan'
	RETURN @Result

END

```
