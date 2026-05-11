# Function: `ThucChay_GetListThucTreoIDByHopDongChiTietREF`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-02-26 17:16:06.667000
- **Ngày sửa cuối**: 2014-10-14 10:39:31.880000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@NgayGioiHanTinh` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql
--EXEC [ThucChay_InsertThucChayDaTinh_PR] '2013-12-10','2013-12-10'
-------------------------------------------------------------
CREATE FUNCTION [dbo].[ThucChay_GetListThucTreoIDByHopDongChiTietREF]
(
	-- Add the parameters for the function here
	@NgayThucHien DATETIME,
	@NgayGioiHanTinh DATETIME,
	@HopDongChiTietREF INT
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
			SELECT cast(',' as varchar(max)) + Convert(nvarchar(20),tchdctp.ThucChayHopDongChiTietID)
			  FROM ThucChayHopDongChiTiet tchdctp
			WHERE tchdctp.HopDongChiTietREF = @HopDongChiTietREF
			AND (CASE when tchdctp.CreatedAt >= tchdctp.LastModifiedAt THEN Convert(date,tchdctp.CreatedAt) 
				else Convert(date,tchdctp.LastModifiedAt)
			  END
			) = @NgayThucHien
			AND Convert(date,tchdctp.ThoiGianBatDau) >= @NgayGioiHanTinh
			AND tchdctp.RecordStatus = 0
			AND tchdctp.DeletedStatus = 0
			for xml path('') 
		), 1, 1, '') AS ListThucTreoID
    )

	-- Return the result of the function
	RETURN @ReturnValue

END

```
