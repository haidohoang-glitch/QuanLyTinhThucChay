# Function: `ThucChay_GetDonGiaThucTreo_PR`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-06 18:20:20.363000
- **Ngày sửa cuối**: 2014-11-19 12:17:40.473000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@NgayKyHopDong` | `datetime(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietID` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetDonGiaThucTreo_PR]
(
	-- Add the parameters for the function here
	@NgayKyHopDong DATETIME,
	@NgayThucHien datetime,
	@HopDongChiTietID nvarchar(50)	
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ThanhTienThucChay FLOAT
	DECLARE @DonGiaTheoDonVi FLOAT
	DECLARE @SoLuongThucChay FLOAT
	DECLARE @intHopDongChiTietID INT
	set @intHopDongChiTietID = CONVERT(INT, @HopDongChiTietID) 
	--TINH SO LUONG BAI
	SET  @SoLuongThucChay = 
	(
		SELECT COUNT(*) FROM ThucChayHopDongChiTietPR tchdctp
		WHERE tchdctp.HopDongChiTietREF = @intHopDongChiTietID
		AND (CASE when tchdctp.CreatedAt >= tchdctp.LastModifiedAt THEN Convert(date,CreatedAt) 
			else Convert(date,tchdctp.LastModifiedAt)
		END
		)  = CONVERT(DATE,@NgayThucHien)
		AND tchdctp.DeletedStatus = 0
		AND tchdctp.RecordStatus = 0
	)
	SET @SoLuongThucChay = ISNULL(@SoLuongThucChay,0) 	
	IF(@SoLuongThucChay <0)
		SET @SoLuongThucChay = 0

	--TONG TIEN CUA BAI TREN PHAN THUC TREO
	SET @ThanhTienThucChay =
	(
		SELECT sum(ISNULL(tchdctp.GiaTien,0)) 
		FROM ThucChayHopDongChiTietPR tchdctp
		WHERE tchdctp.HopDongChiTietREF = @intHopDongChiTietID
		AND 
		(CASE when tchdctp.CreatedAt >= tchdctp.LastModifiedAt THEN Convert(date,CreatedAt) 
			else Convert(date,tchdctp.LastModifiedAt)
		END
		)   = CONVERT(DATE,@NgayThucHien)
		AND tchdctp.DeletedStatus = 0
		AND tchdctp.RecordStatus = 0
	)
	SET @ThanhTienThucChay = ISNULL(@ThanhTienThucChay,0)
	
	IF(@SoLuongThucChay = 0)
	BEGIN
		SET @DonGiaTheoDonVi = 0
	END
	ELSE
		BEGIN
			SET @DonGiaTheoDonVi = @ThanhTienThucChay/@SoLuongThucChay		
		END
	
	RETURN @DonGiaTheoDonVi

END

```
