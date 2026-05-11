# Function: `ThucChay_GetThanhTienChuanThucChay_PR`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-07-05 15:20:46.900000
- **Ngày sửa cuối**: 2015-12-03 14:10:32.833000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@SoLuong` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@DonGia` | `float(8)` | No |
| `@NgayKyHopDong` | `datetime(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@NgayGioiHanTinh` | `datetime(8)` | No |
| `@HopDongChiTietID` | `nvarchar(100)` | No |
| `@DmWebsiteREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetThanhTienChuanThucChay_PR]
(
	-- Add the parameters for the function here
	@SoLuong INT, 
	@DonViTinh nvarchar(50), 
	@DonGia FLOAT,
	@NgayKyHopDong DATETIME,
	@NgayThucHien datetime,
	@NgayGioiHanTinh DATETIME,
	@HopDongChiTietID nvarchar(50)	,
	@DmWebsiteREF INT
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
	/*
	SET @DonViTinh = UPPER(@DonViTinh)
	SET @DonGiaTheoDonVi = ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(@SoLuong,@DonViTinh,@DonGia,@NgayKyHopDong,@NgayThucHien,@HopDongChiTietID),0)
	SET @SoLuongThucChay = ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_PR(@NgayThucHien, @HopDongChiTietID),0)
	
	SET @ThanhTienThucChay = @DonGiaTheoDonVi * @SoLuongThucChay
	*/
	--PHUONG PHAP TINH TIEN THEO NHU GIA TIEN CUA BAI TREN PHAN THUC TREO
	SET @ThanhTienThucChay =
	(
		SELECT sum(ISNULL(tchdctp.GiaTien,0)*ISNULL(tchdctp.SoLuong,0)) --haidh:GiaTien la don gia cua thuc treo pr/1dv soluong
		FROM ThucChayHopDongChiTietPR tchdctp
		WHERE tchdctp.HopDongChiTietREF = @intHopDongChiTietID
		AND 
		(CASE when CreatedAt >= LastModifiedAt THEN Convert(date,CreatedAt) 
			else Convert(date,LastModifiedAt)
		END
		)  = CONVERT(DATE,@NgayThucHien)
		AND tchdctp.DeletedStatus = 0
		AND tchdctp.RecordStatus = 0
		AND Convert(date,ThoiGianBatDau) >= @NgayGioiHanTinh
		AND tchdctp.DmWebsiteREF = @DmWebsiteREF
	)
	RETURN @ThanhTienThucChay

END

```
