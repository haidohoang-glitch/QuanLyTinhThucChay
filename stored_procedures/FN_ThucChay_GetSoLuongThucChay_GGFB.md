# Function: `ThucChay_GetSoLuongThucChay_GGFB`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2020-08-12 18:09:46.600000
- **Ngày sửa cuối**: 2020-08-12 18:32:54.170000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@SoLuongTCNgay_In` | `float(8)` | No |
| `@IsKhuyenMai` | `float(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@GiaTriHDCT` | `bigint(8)` | No |

## Definition (Source Code)

```sql
CREATE  FUNCTION [dbo].[ThucChay_GetSoLuongThucChay_GGFB] 
(
	@SoLuongTCNgay_In FLOAT,
	@IsKhuyenMai FLOAT,
	@NgayThucHien DATETIME,
	@HopDongChiTietREF INT,
	@GiaTriHDCT BIGINT
)
RETURNS FLOAT
AS
BEGIN
	DECLARE  
	  @SoLuongTCNgay_Out FLOAT =0
	, @SoLuongTCDT FLOAT=0
	, @SoLuongHDCT BIGINT = 0
	, @ThanhTienTCDT BIGINT = 0
	, @DonGia BIGINT = 0

	--1. Xác định số lượng thực chạy đã tính
	IF (@IsKhuyenMai = 1)
		BEGIN	
			SELECT @SoLuongTCDT = SUM(isnull(SoLuongThucChayKM, 0) +  isnull(SoLuongKMThayDoi, 0))
			FROM dbo.ThucChayDaTinh_GGFB_Test
			WHERE HopDongChiTietREF = @HopDongChiTietREF
				  AND NgayThucHien <= @NgayThucHien
		END
	ELSE
		BEGIN
			SELECT @SoLuongTCDT = SUM(isnull(SoLuongThucChay, 0) +  isnull(SoLuongThayDoi, 0))
			FROM dbo.ThucChayDaTinh_GGFB_Test
			WHERE HopDongChiTietREF = @HopDongChiTietREF
				  AND NgayThucHien <= @NgayThucHien
		END

	-- 2. Xác định thành tiền thực chạy đã tính
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

	-- 3. Xác định đơn giá theo TCDT và SLTCDT
	SET @DonGia = @ThanhTienTCDT/@SoLuongTCDT

	-- 4. Xác định só lượng theo giá trị hợp đồng và đơn giá
	SET @SoLuongHDCT = @GiaTriHDCT/@DonGia

	-- 4. Tính giá trị vượt hợp đồng
	IF (@SoLuongHDCT >=@SoLuongTCDT +@SoLuongTCNgay_In)
		SET @SoLuongTCNgay_Out = @SoLuongTCNgay_In
	ELSE
		SET @SoLuongTCNgay_Out = @SoLuongHDCT - @SoLuongTCDT
	
	RETURN @SoLuongTCNgay_Out

END













```
