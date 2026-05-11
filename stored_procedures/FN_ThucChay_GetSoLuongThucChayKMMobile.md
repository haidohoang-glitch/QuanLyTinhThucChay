# Function: `ThucChay_GetSoLuongThucChayKMMobile`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-09-29 09:09:08.090000
- **Ngày sửa cuối**: 2014-11-19 12:17:40.527000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@HopDongChiTietID` | `int(4)` | No |
| `@IsKhuyenMai` | `int(4)` | No |
| `@DonGia` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoLuongThucChay` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
--select dbo.ThucChay_GetSoLuongThucChayKMMobile(56937,1,35,'2014-06-09',19956)
CREATE FUNCTION [dbo].[ThucChay_GetSoLuongThucChayKMMobile]
(
	-- Add the parameters for the function here
	@HopDongChiTietID INT,
	@IsKhuyenMai INT,
	@DonGia INT,
	@NgayThucHien DATETIME,
	@SoLuongThucChay INT	
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @DonViTinh NVARCHAR(50), 
			@ThanhTienHD FLOAT,
		    @ThanhTienTCDT FLOAT, 
		    @ThanhTienThucChayNgay FLOAT, 
		    @ThanhTienThucChayKM FLOAT,		    
		    @DonGiaSauChietKhau FLOAT,
		    @SoLuongThucChayKM FLOAT,
		    @DmSanPhamREF INT;

	SELECT @DonViTinh   = hdct.DonViTinh,		  		 
		   @DonGiaSauChietKhau = @DonGia,
		   @ThanhTienHD = hdct.SoLuong*DonGia,
		   @DmSanPhamREF = hdct.DmSanPhamREF
	FROM HopDongChiTiet hdct 
	WHERE hdct.HopDongChiTietID = @HopDongChiTietID
	
			
	--1. TINH SO TIEN THUC CHAY DA TINH (THANHTIENSAUCHIETKHAU + GIATRITHAYDOI) (B)
	IF @DmSanPhamREF = 342
	BEGIN
		SELECT @ThanhTienTCDT = ISNULL(SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi),0)
		FROM ThucChayDaTinhMobile tcdt
		WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
		AND tcdt.NgayThucHien <= @NgayThucHien
		AND tcdt.TrangThaiHopDong <> 3
	END
	ELSE IF @DmSanPhamREF = 381
	BEGIN
		SELECT @ThanhTienTCDT = ISNULL(SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi),0)
		FROM ThucChayDaTinhSponsorPost tcdt
		WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
		AND tcdt.NgayThucHien <= @NgayThucHien
		AND tcdt.TrangThaiHopDong <> 3
	END
	--2. TINH SO TIEN THUC CHAY TAI NGAY THEO THAM SO TRUYEN VAO (C)
	SELECT @ThanhTienThucChayNgay = @SoLuongThucChay*@DonGiaSauChietKhau;
	
	--3. XAC DINH TIEN HOPDONGCHITIET (A)
	
	--4. BIEU THUC CHECK
	--4.1 NEU A >= B + C => THANH TIEN THUC CHAY = C
	IF (@ThanhTienHD >= (@ThanhTienTCDT + @ThanhTienThucChayNgay))
		SET @ThanhTienThucChayKM = @ThanhTienThucChayNgay
	--4.2 NEU A < B+C 
	ELSE
		BEGIN
			--4.2.1 NEU A <= B => THANH TIEN THUC CHAY = 0
			--4.2.1 NEU A <= B => THANH TIEN THUC CHAY = 0
			IF (@ThanhTienHD <= @ThanhTienTCDT) 
				SET @ThanhTienThucChayKM = 0
			--4.2.2 NEU A > B => THANH TIEN THUC CHAY = A- B
			ELSE
				SET @ThanhTienThucChayKM = @ThanhTienHD - @ThanhTienTCDT
		END
	
	--5 SO LUONG THUC CHAY = THANHTIENTHUCCHAY/DONGIA
	--lay so luong thuc chay ngay thuc hien
	IF @DonGiaSauChietKhau <> 0 
		SET @SoLuongThucChayKM = ISNULL(@ThanhTienThucChayKM/@DonGiaSauChietKhau,0);
	ELSE 
		SET @SoLuongThucChayKM = 0
	-- Return the result of the function
	RETURN @SoLuongThucChayKM
	
END

```
