# Function: `ThucChay_CheckSoLuongThucChayChuanByDonViTinh_ChiPhi_SanPhamChinh`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2019-07-05 14:40:00.800000
- **Ngày sửa cuối**: 2019-07-05 14:59:40.207000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@NgayGioiHanTinh` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@HopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
/*
select  [dbo].[ThucChay_GetSoLuongThucChayChuanByDonViTinh_ChiPhi_SanPhamChinh] 
(
	'2019-07-04',
	'2015-01-10',
	522115
)
*/
CREATE FUNCTION [dbo].[ThucChay_CheckSoLuongThucChayChuanByDonViTinh_ChiPhi_SanPhamChinh] 
(
	-- Add the parameters for the function here	
	@NgayThucHien DATETIME,
	@NgayGioiHanTinh DATETIME,
	@HopDongChiTietREF INT,
	@HopDongID INT
)
RETURNS FLOAT
AS
BEGIN
	DECLARE @SoLuongThucChay FLOAT =0, @SoLuongThucChayBefore FLOAT =0
	DECLARE @Count INT	
	SET @SoLuongThucChayBefore =
	ISNULL(
		(SELECT SUM(SoLuongThucChay + SoLuongThayDoi) FROM dbo.ThucChayDaTinh
		WHERE HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietREF
		AND NgayThucHien <@NgayThucHien
		)
		,0)
	
	--SET  @Count = 
	--		ISNULL((
	--			SELECT COUNT(*) FROM dbo.ThucChayHopDongChiTiet tchdctp
	--			WHERE tchdctp.HopDongChiTietREF = @HopDongChiTietREF
	--			AND tchdctp.DeletedStatus = 0
	--			AND tchdctp.RecordStatus = 1
	--			--AND tchdctp.InputType = 1 --TreoTuDong
	--			AND Convert(date,tchdctp.ThoiGianBatDau) >= @NgayGioiHanTinh 
	--		),0)

	--IF(ISNULL(@Count,0) >0)
	--BEGIN
	--	IF(@SoLuongThucChayBefore =0)
	--		SET @SoLuongThucChay = @Count
	--END
	--ELSE
	--	SET @SoLuongThucChay = 0
	
	-- Return the result of the function
	RETURN @SoLuongThucChayBefore
END

```
