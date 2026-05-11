# Function: `ThucChay_GetSoLuongThucChayChuanByDonViTinh_CPD`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-21 15:55:07.260000
- **Ngày sửa cuối**: 2014-10-14 10:39:30.733000

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
CREATE  FUNCTION [dbo].[ThucChay_GetSoLuongThucChayChuanByDonViTinh_CPD] 
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
	--Haidh sua van tinh so luong bi trung booking ma khong phai la doc quyen
	SET @isDocQuyen =
				(
					SELECT COUNT(*) FROM HopDongChiTiet hdct
					WHERE dbo.FormatString(hdct.HopDongChiTietID) = @HopDongChiTietREF
					AND hdct.DmLoaiBannerREF = 5	--Doc quyen
					AND hdct.DeletedStatus = 0
				)
	
	SET  @Count = 
			(
				
				SELECT COUNT(*) FROM DotChayHopDongChiTiet dchdct
				INNER JOIN dbo.Booking b ON b.BookingID = dchdct.BookingREF
				WHERE dchdct.HopDongChiTietREF = @HopDongChiTietREF
				AND dchdct.BookingREF >0
				AND b.[Status] IN (3,5)
				AND b.HinhThucSP = 1 
				AND dchdct.DeletedStatus = 0
				AND CONVERT(DATE,b.NgayBatDau)  <= CONVERT(DATE,@NgayThucHien)
				AND CONVERT(DATE,b.NgayKetThuc) >= CONVERT(DATE,@NgayThucHien)
				/*
				SELECT COUNT(*)
				FROM( 
					SELECT dchdct.* FROM DotChayHopDongChiTiet dchdct
					where  dbo.FormatString(dchdct.HopDongChiTietREF) = @HopDongChiTietREF
					and dchdct.RecordStatus = 0 
					AND dchdct.BookingREF >0  
				)a
				INNER JOIN 
				(
				 SELECT b.* FROM Booking b
				 WHERE b.[Status] IN (3,5)
				 
				 AND CONVERT(DATE,b.NgayBatDau)  <= CONVERT(DATE,@NgayThucHien)
				 AND CONVERT(DATE,b.NgayKetThuc) >= CONVERT(DATE,@NgayThucHien)
				) b ON b.BookingID = a.BookingREF
				*/
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
