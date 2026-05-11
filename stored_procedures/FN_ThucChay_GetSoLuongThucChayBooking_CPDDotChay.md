# Function: `ThucChay_GetSoLuongThucChayBooking_CPDDotChay`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-06-16 16:49:14.927000
- **Ngày sửa cuối**: 2015-08-15 09:46:34.717000

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
--select [dbo].[ThucChay_GetSoLuongThucChayBooking_CPD] (2,N'Tuần',55481,'2014-09-24')
CREATE  FUNCTION [dbo].[ThucChay_GetSoLuongThucChayBooking_CPDDotChay]
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
				SET @Count =
				(
					SELECT COUNT(*) FROM HopDongChiTiet hdct
					WHERE dbo.FormatString(hdct.HopDongChiTietID) = @HopDongChiTietID
					AND hdct.DmLoaiBannerREF = 5	--Doc quyen
					AND hdct.DeletedStatus = 0
				)
				IF(@Count > 0)
					BEGIN
						SET @SoNgayTheoDonViTinh = 
						(
							SELECT ISNULL(sum(DATEDIFF(day, dchdct.ThoiGianBatDau, dchdct.ThoiGianKetThuc) + 1),0)
							FROM 
							(
								SELECT distinct  tchdct.ThoiGianBatDau
								, (
										CASE WHEN convert(date,tchdct.ThoiGianKetThuc) > @NgayThucHien THEN @NgayThucHien
											ELSE tchdct.ThoiGianKetThuc
										END
									   )AS ThoiGianKetThuc
								
								FROM DotChayHopDongChiTiet dchdct 
								INNER JOIN 
								(
									SELECT DISTINCT tchdct.HopDongChiTietREF, tchdct.DeletedStatus, tchdct.ThoiGianBatDau
									, tchdct.ThoiGianKetThuc
									, tchdct.BookingREF
									  FROM ThucChayHopDongChiTiet tchdct
									WHERE tchdct.DeletedStatus = 0

								) tchdct
								ON tchdct.HopDongChiTietREF = dchdct.HopDongChiTietREF	AND dchdct.BookingREF = tchdct.BookingREF
								WHERE 1=1
								AND dchdct.HopDongChiTietREF = @HopDongChiTietID
								and tchdct.DeletedStatus = 0  
								AND dchdct.RecordStatus = 0
								AND dchdct.DeletedStatus = 0
								AND convert(date,tchdct.ThoiGianBatDau) <= @NgayThucHien
							)dchdct
						)
					END
				ELSE
					BEGIN
						SET @SoNgayTheoDonViTinh = 
						(
							SELECT ISNULL(sum(DATEDIFF(day, dchdct.ThoiGianBatDau, dchdct.ThoiGianKetThuc) + 1),0)
							FROM 
							(
								SELECT distinct tchdct.ThoiGianBatDau
								, dchdct.BookingREF--Tuyetnta bo sung
								, (
										CASE WHEN convert(date,tchdct.ThoiGianKetThuc) > @NgayThucHien THEN @NgayThucHien
											ELSE tchdct.ThoiGianKetThuc
										END
									   )AS ThoiGianKetThuc
								
								FROM DotChayHopDongChiTiet dchdct 
								INNER JOIN (
									SELECT DISTINCT tchdct.HopDongChiTietREF, tchdct.DeletedStatus, tchdct.ThoiGianBatDau
									, tchdct.ThoiGianKetThuc
									, tchdct.BookingREF
									  FROM ThucChayHopDongChiTiet tchdct
									WHERE tchdct.DeletedStatus = 0

								) tchdct
								ON tchdct.HopDongChiTietREF = dchdct.HopDongChiTietREF	AND dchdct.BookingREF = tchdct.BookingREF
								WHERE 1=1
								AND dchdct.HopDongChiTietREF = @HopDongChiTietID
								and tchdct.DeletedStatus = 0  
								AND dchdct.RecordStatus = 0
								AND dchdct.DeletedStatus = 0
								AND convert(date,tchdct.ThoiGianBatDau) <= @NgayThucHien
								
							)dchdct
						)
					END	
					IF(@SoNgayTheoDonViTinh <=0)
						SET @SoNgayTheoDonViTinh = 0
					SET @SoLuongTheoDonViTinh = @SoNgayTheoDonViTinh
			END
	-- Return the result of the function
	RETURN @SoLuongTheoDonViTinh

END

```
