# Function: `ThucChay_GetSoLuongNgayDotChayHopDongChiTiet`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-03-04 09:09:12.353000
- **Ngày sửa cuối**: 2014-10-14 10:39:31.330000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@SoLuong` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql

-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetSoLuongNgayDotChayHopDongChiTiet]
(
	-- Add the parameters for the function here
	@SoLuong INT, 
	@DonViTinh nvarchar(50),
	@HopDongChiTietID NVARCHAR(50)
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @SoNgayTheoDonViTinh FLOAT
	DECLARE @Count INT 
	SET @DonViTinh = UPPER(LTRIM(RTRIM(@DonViTinh)))	
	SET @Count =
	(
		SELECT COUNT(*) FROM HopDongChiTiet hdct
		WHERE dbo.FormatString(hdct.HopDongChiTietID) = @HopDongChiTietID
		AND hdct.DmLoaiBannerREF = 5	--Doc quyen
	)
	IF(@Count > 0)
		BEGIN
			SET @SoNgayTheoDonViTinh = dbo.ThucChay_GetSoLuong_DonViTinh(@SoLuong,@DonViTinh)
		END
	ELSE
		BEGIN
			SET @SoNgayTheoDonViTinh = 
			(
				SELECT ISNULL(sum(DATEDIFF(DAY, dchdct.ThoiGianBatDau, dchdct.ThoiGianKetThuc) + 1),0)
				FROM DotChayHopDongChiTiet dchdct
				WHERE dchdct.HopDongChiTietREF = @HopDongChiTietID				
				AND dchdct.RecordStatus = 0
				AND dchdct.DeletedStatus <> 1
			)	
		END
	IF(@SoNgayTheoDonViTinh = 0)
	BEGIN
		SET @SoNgayTheoDonViTinh = 
		(
			SELECT ISNULL(SUM(DATEDIFF(DAY, tchdct.ThoiGianBatDau, tchdct.ThoiGianKetThuc)+ 1),0) 
			FROM ThucChayHopDongChiTiet tchdct
			WHERE tchdct.DeletedStatus = 0
			AND tchdct.HopDongChiTietREF = @HopDongChiTietID			
		)		
	END
	RETURN @SoNgayTheoDonViTinh
END

```
