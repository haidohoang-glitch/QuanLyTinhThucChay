# Function: `ThucChay_GetSoLuongThucChayChuanByDonViTinh_CPDDotChay`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-06-16 16:49:14.703000
- **Ngày sửa cuối**: 2015-06-17 15:59:27.570000

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
CREATE  FUNCTION [dbo].[ThucChay_GetSoLuongThucChayChuanByDonViTinh_CPDDotChay] 
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
					SELECT DISTINCT tchdct.HopDongChiTietREF, tchdct.DeletedStatus, tchdct.ThoiGianBatDau
					, tchdct.ThoiGianKetThuc
					, tchdct.BookingREF
					  FROM ThucChayHopDongChiTiet tchdct
				    WHERE tchdct.DeletedStatus = 0
				)tchdct
				ON tchdct.HopDongChiTietREF = dchdct.HopDongChiTietREF AND dchdct.BookingREF = tchdct.BookingREF
				WHERE 1=1  
				AND dchdct.HopDongChiTietREF = @HopDongChiTietREF
				AND tchdct.DeletedStatus = 0
				AND dchdct.DeletedStatus = 0
				AND CONVERT(DATE,tchdct.ThoiGianBatDau)  <= CONVERT(DATE,@NgayThucHien)
				AND CONVERT(DATE,tchdct.ThoiGianKetThuc) >= CONVERT(DATE,@NgayThucHien)
				AND year(dchdct.ThoiGianKetThuc) >= 2013					

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
