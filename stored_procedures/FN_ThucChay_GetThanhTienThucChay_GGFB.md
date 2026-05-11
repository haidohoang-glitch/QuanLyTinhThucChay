# Function: `ThucChay_GetThanhTienThucChay_GGFB`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2020-08-12 18:10:14.630000
- **Ngày sửa cuối**: 2020-08-12 18:33:37.497000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@ThanhTienTCNgay_In` | `float(8)` | No |
| `@IsKhuyenMai` | `float(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@SoLuongHDCT` | `bigint(8)` | No |

## Definition (Source Code)

```sql
CREATE  FUNCTION [dbo].[ThucChay_GetThanhTienThucChay_GGFB] 
(
	@ThanhTienTCNgay_In FLOAT,
	@IsKhuyenMai FLOAT,
	@NgayThucHien DATETIME,
	@HopDongChiTietREF INT,
	@SoLuongHDCT BIGINT
)
RETURNS FLOAT
AS
BEGIN
	DECLARE  
	  @ThanhTienTCNgay_Out FLOAT =0
	, @ThanhTienTCDT FLOAT=0

	--1. Xác định thành tiền đã tính
	IF (@IsKhuyenMai = 1)
		BEGIN	
			SELECT @ThanhTienTCDT = SUM(isnull(ThanhTienKM, 0) +  isnull(GiaTriKMThayDoi, 0))
			FROM dbo.ThucChayDaTinh_GGFB_Test
			WHERE HopDongChiTietREF = @HopDongChiTietREF
				  AND NgayThucHien <= @NgayThucHien
		END
	ELSE
		BEGIN
			SELECT @ThanhTienTCDT = SUM(isnull(ThanhTienSauTrietKhauThucChay, 0) +  isnull(GiaTriThayDoi, 0))
			FROM dbo.ThucChayDaTinh_GGFB_Test
			WHERE HopDongChiTietREF = @HopDongChiTietREF
				  AND NgayThucHien <= @NgayThucHien
		END

	-- 2. Tính giá trị vượt hợp đồng
	IF (@SoLuongHDCT >=@ThanhTienTCDT +@ThanhTienTCNgay_In)
		SET @ThanhTienTCNgay_Out = @ThanhTienTCNgay_In
	ELSE
		SET @ThanhTienTCNgay_Out = @SoLuongHDCT - @ThanhTienTCDT
	
	RETURN @ThanhTienTCNgay_Out

END

```
