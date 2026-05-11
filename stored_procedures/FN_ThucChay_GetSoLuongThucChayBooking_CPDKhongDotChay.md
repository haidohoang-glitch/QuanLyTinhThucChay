# Function: `ThucChay_GetSoLuongThucChayBooking_CPDKhongDotChay`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-07-01 14:33:04.620000
- **Ngày sửa cuối**: 2014-10-14 10:39:31.070000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@SoLuong` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
--select [dbo].[ThucChay_GetSoLuongThucChayBooking_CPD] (2,N'Tuần',55481,'2014-07-30')

CREATE  FUNCTION [dbo].[ThucChay_GetSoLuongThucChayBooking_CPDKhongDotChay]
(
	-- Add the parameters for the function here
	@SoLuong INT, 
	@DonViTinh nvarchar(50),
	@HopDongChiTietID NVARCHAR(50),
	@NgayThucHien DATETIME
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @SoLuongTheoDonViTinh FLOAT
	DECLARE @SoNgayTheoDonViTinh INT
	DECLARE @Count INT 
	SET @DonViTinh = UPPER(LTRIM(RTRIM(@DonViTinh)))
	
	IF(@DonViTinh = 'CPM' )
	BEGIN
		SET @SoLuongTheoDonViTinh = @SoLuong*1000
	END
	ELSE
		IF(@DonViTinh = N'BÀI' or @DonViTinh = 'CPC')
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
				SET @SoNgayTheoDonViTinh = 
					(
						SELECT ISNULL(sum(DATEDIFF(day, tchdct.ThoiGianBatDau, tchdct.ThoiGianKetThuc) + 1),0)
						FROM 
						(
							SELECT tchdct.ThoiGianBatDau
							, (
									CASE WHEN convert(date,tchdct.ThoiGianKetThuc) > @NgayThucHien THEN @NgayThucHien
										ELSE tchdct.ThoiGianKetThuc
									END
								   )AS ThoiGianKetThuc
							
							FROM ThucChayHopDongChiTiet tchdct
							WHERE 1=1
							AND tchdct.HopDongChiTietREF = @HopDongChiTietID
							and tchdct.DeletedStatus = 0  
							AND convert(date,tchdct.ThoiGianBatDau) <= @NgayThucHien
							
						)tchdct
					)	
				IF(@SoNgayTheoDonViTinh <=0)
					SET @SoNgayTheoDonViTinh = 0
				SET @SoLuongTheoDonViTinh = @SoNgayTheoDonViTinh
			END
	-- Return the result of the function
	RETURN @SoLuongTheoDonViTinh

END

```
