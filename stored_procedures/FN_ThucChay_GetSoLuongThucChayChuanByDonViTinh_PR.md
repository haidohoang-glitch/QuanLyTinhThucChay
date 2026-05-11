# Function: `ThucChay_GetSoLuongThucChayChuanByDonViTinh_PR`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-07-05 13:55:34.107000
- **Ngày sửa cuối**: 2015-12-03 14:08:20.377000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@NgayGioiHanTinh` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetSoLuongThucChayChuanByDonViTinh_PR] 
(
	-- Add the parameters for the function here	
	@NgayThucHien DATETIME,
	@NgayGioiHanTinh DATETIME,
	@HopDongChiTietREF INT,
	@DmWebsiteREF INT
)
RETURNS FLOAT
AS
BEGIN
	DECLARE @SoLuongThucChay FLOAT
	DECLARE @Count INT	
	SET  @Count = 
			(
				SELECT SUM(ISNULL(tchdctp.SoLuong,0)) FROM ThucChayHopDongChiTietPR tchdctp
				WHERE tchdctp.HopDongChiTietREF = @HopDongChiTietREF
				AND (CASE when CreatedAt >= LastModifiedAt THEN Convert(date,CreatedAt) 
					else Convert(date,LastModifiedAt)
				  END
				)   = CONVERT(DATE,@NgayThucHien)
				AND tchdctp.DeletedStatus = 0
				AND tchdctp.RecordStatus = 0				
				AND Convert(date,tchdctp.ThoiGianBatDau) >= @NgayGioiHanTinh
				AND (tchdctp.DmWebsiteREF = @DmWebsiteREF
				OR dbo.[GetDmWebsiteIDIDByDmWebsiteReportingdb](@DmWebsiteREF) = tchdctp.DmWebsiteREF
				) 
				
			)	
			IF(@Count >0)
				SET @SoLuongThucChay = @Count
			ELSE
				SET @SoLuongThucChay = 0
				
	-- Return the result of the function
	RETURN @SoLuongThucChay

END

```
