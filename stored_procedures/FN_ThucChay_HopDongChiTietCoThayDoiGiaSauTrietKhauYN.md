# Function: `ThucChay_HopDongChiTietCoThayDoiGiaSauTrietKhauYN`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-07-19 17:56:56.777000
- **Ngày sửa cuối**: 2014-10-14 10:39:29.610000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(100)` | Yes |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author then 		<Author,,Name>
-- Create date then  <Create Date, ,>
-- Description then 	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_HopDongChiTietCoThayDoiGiaSauTrietKhauYN]
(
	-- Add the parameters for the function here
	@HopDongChiTietID INT,
	@NgayThucHien DATETIME
)
RETURNS nvarchar(50)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result nvarchar(50), @Count INT
	SET @Result = 'N'
	SET @Count = 
	(               
		SELECT COUNT(*) FROM 
		(
			SELECT TOP 1 HDCTTD.HopDongChiTietREF,HDTD.NgayThayDoi, HDCTTD.ChietKhau, HDCTTD.DonGia 
			FROM HopDongThayDoi hdtd
			INNER JOIN HopDongChiTietThayDoi hdcttd ON hdtd.HopDongThayDoiID = hdcttd.HopDongThayDoiREF
			WHERE hdcttd.HopDongChiTietREF = @HopDongChiTietID 
			AND Convert(date,hdtd.NgayThayDoi) =  Convert(date,@NgayThucHien)
			ORDER BY HDCTTD.HopDongChiTietThayDoiID DESC
		)A
		INNER JOIN HopDongChiTiet hdct ON HDCT.HopDongChiTietID = A.HopDongChiTietREF
		WHERE (A.DonGia != HDCT.DonGia OR A.ChietKhau != HDCT.ChietKhau)
	)
	IF(@Count >0)
		SET @Result = 'Y'
	-- Return the result of the function
	RETURN @Result

END

```
