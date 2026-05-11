# Function: `ThucChay_GetSoLuongThucChayChuanByDonViTinh_ChiPhi_SanPhamChinh`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-05-16 10:54:38.613000
- **Ngày sửa cuối**: 2016-11-12 09:50:18.017000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@NgayGioiHanTinh` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE FUNCTION [dbo].[ThucChay_GetSoLuongThucChayChuanByDonViTinh_ChiPhi_SanPhamChinh] 
(
	-- Add the parameters for the function here	
	@NgayThucHien DATETIME,
	@NgayGioiHanTinh DATETIME,
	@HopDongChiTietREF INT
)
RETURNS FLOAT
AS
BEGIN
	DECLARE @SoLuongThucChay FLOAT =0, @SoLuongThucChayBefore FLOAT =0
	DECLARE @Count INT	
	SET @SoLuongThucChayBefore =
	ISNULL(
		(SELECT SUM(SoLuongThucChay) FROM dbo.ThucChayDaTinh
		WHERE HopDongChiTietREF = @HopDongChiTietREF
		AND NgayThucHien <@NgayThucHien)
		,0)
	SET  @Count = 
			(
				SELECT COUNT(*) FROM ThucChayHopDongChiTiet tchdctp
				WHERE tchdctp.HopDongChiTietREF = @HopDongChiTietREF
				AND (CASE when CreatedAt >= LastModifiedAt THEN Convert(date,CreatedAt) 
					else Convert(date,LastModifiedAt)
				  END
				)   = CONVERT(DATE,@NgayThucHien)
				AND tchdctp.DeletedStatus = 0
				AND tchdctp.RecordStatus = 0
				--AND tchdctp.InputType = 1 --TreoTuDong
				AND Convert(date,tchdctp.ThoiGianBatDau) >= @NgayGioiHanTinh 
			)	
			IF(@Count >0)
			BEGIN
				IF(@SoLuongThucChayBefore =0)
					SET @SoLuongThucChay = @Count
			END
			ELSE
				SET @SoLuongThucChay = 0
				
	-- Return the result of the function
	RETURN @SoLuongThucChay
END

```
