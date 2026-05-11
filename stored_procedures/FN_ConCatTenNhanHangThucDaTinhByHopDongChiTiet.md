# Function: `ConCatTenNhanHangThucDaTinhByHopDongChiTiet`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2016-10-05 10:04:33.747000
- **Ngày sửa cuối**: 2016-10-05 11:53:52.920000

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
CREATE FUNCTION [dbo].[ConCatTenNhanHangThucDaTinhByHopDongChiTiet]
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

	IF(@DmSanPhamREF IN (144,299,337,585,628))
	BEGIN
		--SELECT @Out_DmNhanHang =  A.NhanHang + COALESCE(@Out_DmNhanHang + N',',N'')
		--FROM
		--(
		--	SELECT DISTINCT NhanHang  
		--	FROM dbo.ThucChayDaTinhAdmarket
		--	where 1=1 
		--	AND HopDongChiTietREF = @HopDongChiTietREF
		--	AND DmSanPhamREF = @DmSanPhamREF
		--)A
		SELECT  @Out_DmNhanHang = d.NhanHang 
		FROM ThucChayDaTinhAdmarket_catNhanHang d
		WHERE d.HopDongChiTietREF = @HopDongChiTietREF
	END
	ELSE
    BEGIN
  --  	SELECT @Out_DmNhanHang =  A.NhanHang + COALESCE(@Out_DmNhanHang + N',',N'')
		--FROM
		--(
		--	SELECT DISTINCT NhanHang  
		--	FROM dbo.ThucChayDaTinh
		--	where 1=1 
		--	AND HopDongChiTietREF = @HopDongChiTietREF
		--	AND DmSanPhamREF = @DmSanPhamREF
		--)A

		SELECT  @Out_DmNhanHang = d.NhanHang 
		FROM ThucChayDaTinh_catNhanHang d
		WHERE d.HopDongChiTietREF = @HopDongChiTietREF
    END


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
		) nh ON ds.items = CONVERT(NVARCHAR(100),nh.DmNhanHangID)

	)B

	SET @ReturnValue = ISNULL(@Out_TenNhan,'')
	-- Return the result of the function
	RETURN @ReturnValue

END

```
