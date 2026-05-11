# Function: `ConCatDmNhanHangThucTreoByHopDongChiTiet`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2016-10-05 09:51:42.070000
- **Ngày sửa cuối**: 2016-10-05 09:55:32.167000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar` | Yes |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ConCatDmNhanHangThucTreoByHopDongChiTiet]
(
	@HopDongChiTietREF INT,
	@DmSanPhamREF INT
	
)
RETURNS nvarchar(max)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ReturnValue nvarchar(max)
	DECLARE @Out_DmNhanHang NVARCHAR(max) = ''

	SELECT @Out_DmNhanHang =  A.DmNhanHangREF + COALESCE(@Out_DmNhanHang + N',',N'')
	FROM
	(
		SELECT DISTINCT DmNhanHangREF  
		FROM dbo.ThucChayHopDongChiTiet
		where 1=1 
		AND HopDongChiTietREF = @HopDongChiTietREF
		AND DmSanPhamREF = @DmSanPhamREF
		AND DeletedStatus = 0
	)A

	SET @ReturnValue = ISNULL(@Out_DmNhanHang,'')
	-- Return the result of the function
	RETURN @ReturnValue

END

```
