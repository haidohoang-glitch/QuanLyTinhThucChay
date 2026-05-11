# Function: `ConCatDmNhanHangThucChayDaTinhByHopDongChiTiet`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2016-10-05 10:00:16.093000
- **Ngày sửa cuối**: 2016-10-05 11:55:27.647000

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
CREATE FUNCTION [dbo].[ConCatDmNhanHangThucChayDaTinhByHopDongChiTiet]
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
	--IF(@DmSanPhamREF IN (144,299,337,585,628))
	--BEGIN
	--	SELECT @Out_DmNhanHang =  A.NhanHang + COALESCE(@Out_DmNhanHang + N',',N'')
	--	FROM
	--	(
	--		SELECT DISTINCT NhanHang  
	--		FROM dbo.ThucChayDaTinhAdmarket
	--		where 1=1 
	--		AND HopDongChiTietREF = @HopDongChiTietREF
	--		AND DmSanPhamREF = @DmSanPhamREF
	--	)A
	--END
	--ELSE
 --   BEGIN
 --   	SELECT @Out_DmNhanHang =  A.NhanHang + COALESCE(@Out_DmNhanHang + N',',N'')
	--	FROM
	--	(
	--		SELECT DISTINCT NhanHang  
	--		FROM dbo.ThucChayDaTinh
	--		where 1=1 
	--		AND HopDongChiTietREF = @HopDongChiTietREF
	--		AND DmSanPhamREF = @DmSanPhamREF
	--	)A
 --   END

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

	SET @ReturnValue = ISNULL(@Out_DmNhanHang,'')
	-- Return the result of the function
	RETURN @ReturnValue

END



```
