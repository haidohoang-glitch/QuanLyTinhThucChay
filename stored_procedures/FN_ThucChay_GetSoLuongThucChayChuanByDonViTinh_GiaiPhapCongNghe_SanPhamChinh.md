# Function: `ThucChay_GetSoLuongThucChayChuanByDonViTinh_GiaiPhapCongNghe_SanPhamChinh`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2016-05-12 14:24:34.373000
- **Ngày sửa cuối**: 2016-05-12 14:24:39.410000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@NgayGioiHanTinh` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE FUNCTION [dbo].[ThucChay_GetSoLuongThucChayChuanByDonViTinh_GiaiPhapCongNghe_SanPhamChinh] 
(
	-- Add the parameters for the function here	
	@NgayThucHien DATETIME,
	@NgayGioiHanTinh DATETIME,
	@HopDongChiTietREF INT
)
RETURNS FLOAT
AS
BEGIN
	DECLARE @SoLuongThucChay FLOAT, @IsDaTinhThucChay INT=0
	DECLARE @Count INT =0	
	
	SET @IsDaTinhThucChay = (
		SELECT COUNT(tcdt.HopDongChiTietREF) FROM ThucChayDaTinh tcdt
		WHERE tcdt.HopDongChiTietREF = @HopDongChiTietREF	
		AND (tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) <> 0
	)
	IF(@IsDaTinhThucChay <> 0)
	BEGIN
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
	END
	IF(@Count >0)
		SET @SoLuongThucChay = @Count
	ELSE
		SET @SoLuongThucChay = 0
				
	-- Return the result of the function
	RETURN @SoLuongThucChay
END

```
