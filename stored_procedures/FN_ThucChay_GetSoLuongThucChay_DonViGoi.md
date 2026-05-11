# Function: `ThucChay_GetSoLuongThucChay_DonViGoi`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2021-03-26 10:24:55.127000
- **Ngày sửa cuối**: 2021-07-20 15:43:28.950000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@TongSoluongThucChay` | `bigint(8)` | No |
| `@TongThanhTienThucChay` | `float(8)` | No |
| `@TongSoLuongThucChayKM` | `bigint(8)` | No |
| `@TongThanhTienThucChayKM` | `float(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@SoLuongHD` | `bigint(8)` | No |
| `@DonGiaHD` | `bigint(8)` | No |
| `@ThanhTien` | `bigint(8)` | No |
| `@ChietKhau` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
/*
[dbo].[ThucChay_GetSoLuongThucChay_ThanhTien_Admatic] 
(
	-- Add the parameters for the function here
	@TongSoluongThucChay BIGINT,
	@TongThanhTienThucChay FLOAT,
	@TongSoLuongThucChayKM BIGINT,
	@TongThanhTienThucChayKM FLOAT,
	@NgayThucHien DATETIME,
	@HopDongChiTietREF INT,
	@SoLuongHD BIGINT,
	@DonGiaHD BIGINT,
	@ThanhTien BIGINT,
	@ChietKhau INT
)
*/
CREATE  FUNCTION [dbo].[ThucChay_GetSoLuongThucChay_DonViGoi] 
(
	-- Add the parameters for the function here
	@TongSoluongThucChay BIGINT,
	@TongThanhTienThucChay FLOAT,
	@TongSoLuongThucChayKM BIGINT,
	@TongThanhTienThucChayKM FLOAT,
	@NgayThucHien DATETIME,
	@HopDongChiTietREF INT,
	@SoLuongHD BIGINT,
	@DonGiaHD BIGINT,
	@ThanhTien BIGINT,
	@ChietKhau INT
)
RETURNS FLOAT
AS
BEGIN
	DECLARE  @DonGiaSauChietKhau FLOAT=0, @ThanhTienHD BIGINT=0, @ThanhTienTCDT BIGINT=0
	, @SoLuongThucChay INT=0, @ThanhTienThucChay BIGINT =0
	, @ThanhTienThucChayNgay BIGINT=0
	

	
	--0. Get thanh tien thuc chay hien tai/ khuyen mai
	IF(@ChietKhau <> 100)
	BEGIN
		--XAC DINH DON GIA SAU CHIET KHAU
		SET @DonGiaSauChietKhau = (CASE WHEN @TongSoluongThucChay <> 0 THEN @TongThanhTienThucChay/@TongSoluongThucChay
									ELSE 0
									END )
		--1. TINH SO TIEN THUC CHAY DA TINH (THANHTIENSAUCHIETKHAU + GIATRITHAYDOI) (B)
		SELECT @ThanhTienTCDT = SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) 
		FROM dbo.ThucChayDaTinh
		WHERE HopDongChiTietREF = @HopDongChiTietREF
		AND NgayThucHien <= @NgayThucHien
		
		SET @ThanhTienTCDT = ISNULL(@ThanhTienTCDT,0)
		--2. TINH SO TIEN THUC CHAY TAI NGAY THEO THAM SO TRUYEN VAO (C)
		SET @ThanhTienThucChayNgay = @TongThanhTienThucChay;
		--3. XAC DINH TIEN HOPDONGCHITIET (A)
		SET @ThanhTienHD = @ThanhTien
	END
	ELSE
	BEGIN
		--XAC DINH DON GIA SAU CHIET KHAU
		SET @DonGiaSauChietKhau = (CASE WHEN @TongSoLuongThucChayKM  <> 0 THEN @TongThanhTienThucChayKM/@TongSoLuongThucChayKM
									ELSE 0
									END )
		--1. TINH SO TIEN THUC CHAY DA TINH (THANHTIENSAUCHIETKHAU + GIATRITHAYDOI) (B)
		SELECT @ThanhTienTCDT = SUM(ThanhTienKM + GiaTriKMThayDoi) 
		FROM dbo.ThucChayDaTinh
		WHERE HopDongChiTietREF = @HopDongChiTietREF
		AND NgayThucHien <= @NgayThucHien
		--AND NgayThucHien < @NgayThucHien
		
		SET @ThanhTienTCDT = ISNULL(@ThanhTienTCDT,0)
		--2. TINH SO TIEN THUC CHAY TAI NGAY THEO THAM SO TRUYEN VAO (C)
		SET @ThanhTienThucChayNgay = @TongThanhTienThucChayKM;
		--3. XAC DINH TIEN HOPDONGCHITIET (A)
		SET @ThanhTienHD = @SoLuongHD*@DonGiaHD
	END

	--4. BIEU THUC CHECK
	--4.1 NEU A >= B + C => THANH TIEN THUC CHAY = C
	IF (@ThanhTienHD >= (@ThanhTienTCDT + @ThanhTienThucChayNgay))
		SET @ThanhTienThucChay = @ThanhTienThucChayNgay
	--4.2 NEU A < B+C 
	ELSE
		BEGIN
			--4.2.1 NEU A <= B => THANH TIEN THUC CHAY = 0
			--4.2.1 NEU A <= B => THANH TIEN THUC CHAY = 05
			IF (@ThanhTienHD <= @ThanhTienTCDT) 
				SET @ThanhTienThucChay = 0
			--4.2.2 NEU A > B => THANH TIEN THUC CHAY = A- B
			ELSE
				SET @ThanhTienThucChay = @ThanhTienHD - @ThanhTienTCDT
		END
	
	--5. quy doi ra so luong phai them vao
	SET @SoLuongThucChay = (CASE WHEN @DonGiaSauChietKhau <> 0 THEN round(ISNULL(@ThanhTienThucChay/@DonGiaSauChietKhau,0),0)
							ELSE 0
							END)
	-- Return the result of the function
	RETURN @SoLuongThucChay

END

```
