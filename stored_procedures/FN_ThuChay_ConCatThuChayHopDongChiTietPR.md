# Function: `ThuChay_ConCatThuChayHopDongChiTietPR`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-11-01 08:46:47.880000
- **Ngày sửa cuối**: 2015-05-19 17:40:41.040000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@NgayGioiHanTinh` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThuChay_ConCatThuChayHopDongChiTietPR]
(
	-- Add the parameters for the function here
	@NgayThucHien DATETIME,
	@NgayGioiHanTinh DATETIME,
	@HopDongChiTietREF INT,
	@DmWebsiteREF INT
)
RETURNS nvarchar(max)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ReturnValue nvarchar(max)
	SET @ReturnValue = ''
	-- Add the T-SQL statements to compute the return value here
	SET @ReturnValue = (SELECT
		stuff(
		(
			SELECT cast(',' as varchar(max)) + Convert(nvarchar(20),tchdctp.ThucChayHopDongChiTietPRID)
			  FROM ThucChayHopDongChiTietPR tchdctp
			WHERE tchdctp.HopDongChiTietREF = @HopDongChiTietREF
			AND (CASE when tchdctp.CreatedAt >= tchdctp.LastModifiedAt THEN Convert(date,tchdctp.CreatedAt) 
				else Convert(date,tchdctp.LastModifiedAt)
			  END
			) = @NgayThucHien
			AND Convert(date,tchdctp.ThoiGianBatDau) >= @NgayGioiHanTinh
			AND tchdctp.RecordStatus = 0
			AND tchdctp.DeletedStatus = 0
			AND tchdctp.DmWebsiteREF = @DmWebsiteREF
			for xml path('') 
		), 1, 1, '') AS TenPhongBan
    )

	-- Return the result of the function
	RETURN @ReturnValue

END

```
