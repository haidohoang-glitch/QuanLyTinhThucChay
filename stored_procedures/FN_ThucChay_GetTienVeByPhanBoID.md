# Function: `ThucChay_GetTienVeByPhanBoID`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-06-10 16:07:03.053000
- **Ngày sửa cuối**: 2015-06-10 16:07:03.053000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@HopDongID` | `int(4)` | No |
| `@PhanBoID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-03-20
-- Description:	<Description, ,>
-- =============================================
/*
	PRINT dbo.ThucChay_GetTienVeByPhanBoID(28727,64404)
*/
CREATE FUNCTION [dbo].[ThucChay_GetTienVeByPhanBoID]
(
	-- Add the parameters for the function here
	@HopDongID	INT,
	@PhanBoID	INT,
	@NgayThucHien DATETIME
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @returnValue FLOAT = 0
	
	DECLARE @giaTriTienVeHopDong	FLOAT,
			@giaTriHopDong			FLOAT,
			@thanhTienPhanBo		FLOAT,
			@tyLe					FLOAT
	
	SELECT 
		@giaTriTienVeHopDong = ISNULL(SUM(A.GiaTri/1.1),0)
	FROM ThongTinTienVe A
	WHERE 1 = 1
		AND A.HopDongREF = @HopDongID
		AND A.NgayThanhToan <= @NgayThucHien;
		
	SELECT 
		@giaTriHopDong = (A.GiaTriHopDong/1.1),
		@thanhTienPhanBo = B.ThanhTien,
		@tyLe = case when A.GiaTriHopDong > 0 then (B.ThanhTien/(A.GiaTriHopDong/1.1)) else 0 end
	FROM HopDong A
		INNER JOIN HopDongChiTiet B ON B.HopDongFK = A.HopDongID
	WHERE 1 = 1
		AND B.HopDongChiTietID = @PhanBoID
		AND A.TrangThaiHopDong <> 3
		
	SET @returnValue = ROUND((@giaTriTienVeHopDong*@tyLe),0);
	
	-- Return the result of the function
	RETURN @returnValue

END

```
