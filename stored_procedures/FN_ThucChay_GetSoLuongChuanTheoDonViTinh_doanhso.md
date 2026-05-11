# Function: `ThucChay_GetSoLuongChuanTheoDonViTinh_doanhso`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-11-27 10:14:02.670000
- **Ngày sửa cuối**: 2014-10-14 10:39:31.667000

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
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE  FUNCTION [dbo].[ThucChay_GetSoLuongChuanTheoDonViTinh_doanhso]
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
	DECLARE @SoLuongTheoDonViTinh FLOAT
	DECLARE @SoNgayTheoDonViTinh INT
	DECLARE @Count INT 
	SET @DonViTinh = UPPER(LTRIM(RTRIM(@DonViTinh)))
	
	IF(@DonViTinh = 'CPM' or @DonViTinh = 'CPC')
	BEGIN
		SET @SoLuongTheoDonViTinh = @SoLuong*1000
	END
	ELSE
		IF(@DonViTinh = N'BÀI')
		BEGIN
			SET @SoLuongTheoDonViTinh = @SoLuong
		END
		ELSE
			IF(@DonViTinh = 'GOI')
			BEGIN
				SET @SoLuongTheoDonViTinh = 5000
				SET @SoLuongTheoDonViTinh = @SoLuong
			END
			ELSE			
			BEGIN
				SET @Count =
				(
					SELECT COUNT(*) FROM HopDongChiTiet hdct
					WHERE dbo.FormatString(hdct.HopDongChiTietID) = @HopDongChiTietID
					AND hdct.DmLoaiBannerREF = 5	--Doc quyen
					AND hdct.DeletedStatus = 0
				)
				IF(@Count > 0)
					BEGIN
						SET @SoNgayTheoDonViTinh = dbo.ThucChay_GetSoLuong_DonViTinh(@SoLuong,@DonViTinh)
					END
				ELSE
					BEGIN
						SET @SoNgayTheoDonViTinh = 
						(
							SELECT ISNULL(sum(DATEDIFF(day, b.NgayBatDau, b.NgayKetThuc) + 1),0)
							FROM DotChayHopDongChiTiet dchdct
							INNER JOIN 
							Booking B ON b.BookingID = dchdct.BookingREF
							AND dbo.FormatString(dchdct.HopDongChiTietREF) = @HopDongChiTietID
							AND dchdct.RecordStatus = 0
							AND dchdct.DeletedStatus = 0
							AND B.[Status] IN (2,3,4,5)
							AND B.HinhThucSP = 1 
							 
						)		
					END	
				SET @SoLuongTheoDonViTinh = @SoNgayTheoDonViTinh
			END
	-- Return the result of the function
	RETURN @SoLuongTheoDonViTinh

END

```
