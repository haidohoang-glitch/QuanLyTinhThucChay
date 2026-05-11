# Function: `ThucChay_GetSoLuongThucChayChuanByDonViTinh_ChiPhi`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-02-27 10:49:42.520000
- **Ngày sửa cuối**: 2015-05-14 16:46:23.190000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@NgayGioiHanTinh` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE FUNCTION [dbo].[ThucChay_GetSoLuongThucChayChuanByDonViTinh_ChiPhi] 
(
	-- Add the parameters for the function here	
	@NgayThucHien DATETIME,
	@NgayGioiHanTinh DATETIME,
	@HopDongChiTietREF INT
)
RETURNS FLOAT
AS
BEGIN
	DECLARE @SoLuongThucChay FLOAT
	DECLARE @Count INT	
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
				SET @SoLuongThucChay = @Count
			ELSE
				SET @SoLuongThucChay = 0
				
	-- Return the result of the function
	RETURN @SoLuongThucChay
END

```
