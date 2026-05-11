# Function: `ThucChay_GetHopDongChiTietID`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-05-29 08:21:50.083000
- **Ngày sửa cuối**: 2014-10-14 10:39:32.043000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@HopDongChiTietREF` | `nvarchar(100)` | No |
| `@DanhsachDmBookingREF` | `nvarchar(200)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetHopDongChiTietID]
(
	-- Add the parameters for the function here
	@HopDongChiTietREF NVARCHAR(50),
	@DanhsachDmBookingREF NVARCHAR(100),
	@SoHopDong NVARCHAR(50)
)
RETURNS int
AS
BEGIN

	DECLARE @TableTemp TABLE
	(
		seqno INT,
		item VARCHAR(200)

	)
	
	IF(@HopDongChiTietREF IS NULL OR RTRIM(RTRIM(@HopDongChiTietREF)) = '')
	BEGIN	
		INSERT INTO @TableTemp SELECT * FROM dbo.ArrayToTable(dbo.Array(@DanhsachDmBookingREF,','))

		set @HopDongChiTietREF = (
								SELECT TOP 1 A.HopDongChiTietREF FROM dbo.DotChayHopDongChiTiet A
								INNER JOIN @TableTemp B ON A.BookingREF = CONVERT(INT,B.item)
								INNER JOIN dbo.HopDong C ON C.HopDongID = A.HopDongREF
								WHERE C.SoHopDong = @SoHopDong
							)
	END
	RETURN @HopDongChiTietREF

END

```
