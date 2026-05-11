# Stored Procedure: `prc_admarket_xoa_dl`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-01-13 17:14:54.077000
- **Ngày sửa cuối**: 2022-01-13 17:15:05.677000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmViTriREF` | `smallint(2)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_admarket_xoa_dl]
	-- Add the parameters for the stored procedure here
	@FromDate DATETIME,
	@ToDate DATETIME,
	@DmSanPhamREF INT,
	@DmViTriREF SMALLINT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

   DELETE FROM ThucChayAdmarket_ADX_CPC_HopDong 
   WHERE  DmSanPhamREF = @DmSanPhamREF 
   AND DmViTriREF = @DmViTriREF
   AND NgayThucHien BETWEEN @FromDate AND @ToDate

END

```
