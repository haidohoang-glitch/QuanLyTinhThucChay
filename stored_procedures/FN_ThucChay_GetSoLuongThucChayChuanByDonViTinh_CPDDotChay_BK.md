# Function: `ThucChay_GetSoLuongThucChayChuanByDonViTinh_CPDDotChay_BK`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-07-30 14:53:57.237000
- **Ngày sửa cuối**: 2014-10-14 10:39:30.667000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
Create  FUNCTION [dbo].[ThucChay_GetSoLuongThucChayChuanByDonViTinh_CPDDotChay_BK] 
(
	-- Add the parameters for the function here	
	@NgayThucHien DATETIME,
	@HopDongChiTietREF INT
)
RETURNS FLOAT
AS
BEGIN
	DECLARE @SoLuongThucChay FLOAT
	DECLARE @Count INT, @isDocQuyen INT	
	SET @isDocQuyen =
				(
					SELECT COUNT(*) FROM HopDongChiTiet hdct
					WHERE dbo.FormatString(hdct.HopDongChiTietID) = @HopDongChiTietREF
					AND hdct.DmLoaiBannerREF = 5	--Doc quyen
					AND hdct.DeletedStatus = 0
				)
	
	SET  @Count = 
			(
				
				SELECT COUNT(dchdct.HopDongREF) FROM DotChayHopDongChiTiet dchdct
				INNER JOIN 
				(
					SELECT tchdct.HopDongChiTietREF, tchdct.BookingREF, hdct.DmSanPhamREF, hdct.TenSanPham
					  FROM ThucChayHopDongChiTiet tchdct
					INNER JOIN HopDongChiTiet hdct ON hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
					WHERE tchdct.DeletedStatus = 0
					AND hdct.DeletedStatus = 0	
				)tc ON tc.HopDongChiTietREF = dchdct.HopDongChiTietREF AND dchdct.BookingREF = tc.BookingREF
				WHERE 1=1  
				AND dchdct.HopDongChiTietREF = @HopDongChiTietREF
				AND CONVERT(DATE,dchdct.ThoiGianBatDau)  <= CONVERT(DATE,@NgayThucHien)
				AND CONVERT(DATE,dchdct.ThoiGianKetThuc) >= CONVERT(DATE,@NgayThucHien)
			)	
			IF(@isDocQuyen = 1)
			BEGIN
				IF(@Count >0)
					SET @SoLuongThucChay = 1
				ELSE
					SET @SoLuongThucChay = 0	
			END
			ELSE
				BEGIN
					SET @SoLuongThucChay = @Count
				END
				
	-- Return the result of the function
	RETURN @SoLuongThucChay

END

```
