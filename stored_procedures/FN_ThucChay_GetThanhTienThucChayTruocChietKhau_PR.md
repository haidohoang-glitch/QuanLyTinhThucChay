# Function: `ThucChay_GetThanhTienThucChayTruocChietKhau_PR`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2019-12-05 16:24:54.197000
- **Ngày sửa cuối**: 2024-08-26 14:09:36.417000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@ChietKhauHDC` | `float(8)` | No |
| `@ThanhTienHDCT` | `float(8)` | No |
| `@SoLuongThucChay` | `float(8)` | No |
| `@DonGiaChay` | `float(8)` | No |
| `@ChietKhauChay` | `float(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
/*
ISNULL([dbo].[ThucChay_GetThanhTienThucChayTruocChietKhau_PR]
							(
								-- Add the parameters for the function here
								1020365,
								575054,
								20,
								120000000,
								1,
								6000000,
								20
							),0)
*/
CREATE FUNCTION [dbo].[ThucChay_GetThanhTienThucChayTruocChietKhau_PR]
(
	-- Add the parameters for the function here
	@HopDongID INT,
	@HopDongChiTietID INT,
	@ChietKhauHDC FLOAT,
	@ThanhTienHDCT FLOAT,
	@SoLuongThucChay FLOAT, 
	@DonGiaChay FLOAT,
	@ChietKhauChay FLOAT
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ThanhTienThucChayTruocCK FLOAT = 0, @ThanhTienThucChayDaTinhSauCK FLOAT = 0
	, @ThanhTienThucChayDaTinhKM FLOAT =0
	--TH1: KHONG PHAI LA KM
	IF(@ChietKhauHDC <> 100)
	BEGIN
		--XAC DINH THANH TIEN THUC CHAY HIEN TAI
		SET @ThanhTienThucChayDaTinhSauCK = ISNULL((SELECT SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) 
												FROM dbo.ThucChayDaTinh tcdt 
												WHERE tcdt.HopDongID = @HopDongID 
												AND tcdt.HopDongChiTietREF = @HopDongChiTietID),0)

		IF(ROUND((@ThanhTienThucChayDaTinhSauCK + (@DonGiaChay*@SoLuongThucChay*(100-@ChietKhauChay)/100)),0) <= @ThanhTienHDCT)
		SET @ThanhTienThucChayTruocCK = @DonGiaChay*@SoLuongThucChay
		ELSE
		SET @ThanhTienThucChayTruocCK = 0 
	END
	--TH2: LA KM
	ELSE
	BEGIN
		DECLARE @ThanhtienHDCT_KM FLOAT = 0
		--XAC DINH THANH TIEN THUC CHAY KM HIEN TAI
		SET @ThanhTienThucChayDaTinhSauCK = ISNULL((SELECT SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) 
												FROM dbo.ThucChayDaTinh tcdt 
												WHERE tcdt.HopDongID = @HopDongID 
												AND tcdt.HopDongChiTietREF = @HopDongChiTietID),0)

	    SELECT TOP (1) @ThanhtienHDCT_KM = hdct.DonGia*hdct.SoLuong
		FROM dbo.HopDongChiTiet hdct
		WHERE hdct.HopDongChiTietID = @HopDongChiTietID
		ORDER BY hdct.HopDongChiTietID

		IF(ROUND((@ThanhTienThucChayDaTinhKM + (@DonGiaChay*@SoLuongThucChay)),0) <= @ThanhtienHDCT_KM)
		SET @ThanhTienThucChayTruocCK = @DonGiaChay*@SoLuongThucChay
		ELSE
		SET @ThanhTienThucChayTruocCK = 0
		
	END
	
	RETURN @ThanhTienThucChayTruocCK

END

```
