# Function: `ConCatTenNhanHangThucTreoByHopDongChiTiet`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2016-10-05 09:55:01.480000
- **Ngày sửa cuối**: 2016-10-05 09:55:01.480000

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
CREATE FUNCTION [dbo].[ConCatTenNhanHangThucTreoByHopDongChiTiet]
(
	@HopDongChiTietREF INT,
	@DmSanPhamREF INT
	
)
RETURNS nvarchar(max)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ReturnValue nvarchar(max)
	DECLARE @Out_DmNhanHang NVARCHAR(max) = '',@Out_TenNhan NVARCHAR(max) = ''

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


	SET @Out_DmNhanHang = ISNULL(@Out_DmNhanHang,'')

	SELECT @Out_TenNhan = B.tennhan + COALESCE(@Out_TenNhan,N'') 
	FROM
	(
		SELECT (nh.TenNhanHang + ' - ' + nh.TenLoaiNhan + '; ') tennhan
		FROM [dbo].[Split](@Out_DmNhanHang,',') ds
		INNER JOIN 
		(
			SELECT DmNhanHangID, TenNhanHang, IsNhanHangLon, (CASE WHEN IsNhanHangLon = 1 THEN N'Doanh nghiệp'
			WHEN IsNhanHangLon = 2 THEN N'Chiến lược'
			ELSE N'Không xác định'
			END)TenLoaiNhan FROM [ASD-SQLSVR_UUTP].ABM_Data_Release.dbo.DmNhanHang
		) nh ON CONVERT(INT,ds.items) = nh.DmNhanHangID

	)B

	SET @ReturnValue = ISNULL(@Out_TenNhan,'')
	-- Return the result of the function
	RETURN @ReturnValue

END

```
