# Function: `ThucChay_GetSoLuongThucChay_Admatic_v1`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2016-12-09 16:38:20.083000
- **Ngày sửa cuối**: 2019-11-09 10:01:48.573000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@TongViewThucChay` | `float(8)` | No |
| `@TongClickThucChay` | `float(8)` | No |
| `@TongTrueViewThucChay` | `float(8)` | No |
| `@DonGia_Banner` | `float(8)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@SoLuongHD` | `bigint(8)` | No |
| `@DonGiaHD` | `float(8)` | No |
| `@ThanhTien` | `float(8)` | No |
| `@ChietKhau` | `float(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
/*
select [dbo].[ThucChay_GetSoLuongThucChay_Admatic_v1] 
(
	-- Add the parameters for the function here
	@TongViewThucChay FLOAT,
	@TongClickThucChay FLOAT,
	@TongTrueViewThucChay FLOAT,
	@DonGia_Banner FLOAT,
	@DonViTinh NVARCHAR(50),
	@NgayThucHien DATETIME,
	@HopDongChiTietREF INT,
	@SoLuongHD BIGINT,
	@DonGiaHD BIGINT,
	@ThanhTien BIGINT,
	@ChietKhau INT
)
*/
CREATE  FUNCTION [dbo].[ThucChay_GetSoLuongThucChay_Admatic_v1] 
(
	-- Add the parameters for the function here
	@TongViewThucChay FLOAT,
	@TongClickThucChay FLOAT,
	@TongTrueViewThucChay FLOAT,
	@DonGia_Banner FLOAT,
	@DonViTinh NVARCHAR(50),
	@NgayThucHien DATETIME,
	@HopDongChiTietREF INT,
	@SoLuongHD BIGINT,
	@DonGiaHD FLOAT,
	@ThanhTien FLOAT,
	@ChietKhau FLOAT
)
RETURNS FLOAT
AS
BEGIN
	DECLARE @IsKM INT, @DonViQuyDoi INT = 1
	, @DonGiaSauChietKhau FLOAT=0, @ThanhTienHD FLOAT=0, @ThanhTienTCDT FLOAT=0
	, @SoLuongThucChay INT=0, @ThanhTienThucChay FLOAT =0
	, @SoLuongThucChayNgay INT=0, @ThanhTienThucChayNgay FLOAT=0
	

	--DECLARE @MinDate DATETIME
	IF(@DonGia_Banner = 0)
		SET @DonGia_Banner = 1
	IF (UPPER(@DonViTinh) = 'CPM') OR ((UPPER(@DonViTinh) = 'VIEW'))
	BEGIN
		SET @DonViQuyDoi = 1000
		SET @SoLuongThucChayNgay = @TongViewThucChay
	END
	IF (UPPER(@DonViTinh) = 'CPC') OR (UPPER(@DonViTinh) = 'CLICK') 
	BEGIN
		SET @DonViQuyDoi = 1
		SET @SoLuongThucChayNgay = @TongClickThucChay
	END
	--HAIDH COMMENT: them thong tin don vi tinh voi True View
	IF (UPPER(@DonViTinh) = 'TRUE VIEW')
	BEGIN
		SET @DonViQuyDoi = 1
		SET @SoLuongThucChayNgay = @TongTrueViewThucChay
	END
	--0. Get thanh tien thuc chay hien tai/ khuyen mai
	IF(@ChietKhau <> 100)
	BEGIN
		--XAC DINH DON GIA SAU CHIET KHAU
		SET @DonGiaSauChietKhau = (@DonGia_Banner*(100-@ChietKhau)/100)/@DonViQuyDoi
		--1. TINH SO TIEN THUC CHAY DA TINH (THANHTIENSAUCHIETKHAU + GIATRITHAYDOI) (B)
		SELECT @ThanhTienTCDT = SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) 
		FROM dbo.ThucChayDaTinh
		WHERE HopDongChiTietREF = @HopDongChiTietREF
		AND NgayThucHien <= @NgayThucHien
		--AND NgayThucHien < @NgayThucHien
		
		SET @ThanhTienTCDT = ISNULL(@ThanhTienTCDT,0)
		--2. TINH SO TIEN THUC CHAY TAI NGAY THEO THAM SO TRUYEN VAO (C)
		SET @ThanhTienThucChayNgay = @SoLuongThucChayNgay*@DonGiaSauChietKhau;
		--3. XAC DINH TIEN HOPDONGCHITIET (A)
		SET @ThanhTienHD = @ThanhTien
	END
	ELSE
	BEGIN
		--XAC DINH DON GIA SAU CHIET KHAU
		SET @DonGiaSauChietKhau = @DonGia_Banner/@DonViQuyDoi
		--1. TINH SO TIEN THUC CHAY DA TINH (THANHTIENSAUCHIETKHAU + GIATRITHAYDOI) (B)
		SELECT @ThanhTienTCDT = SUM(ThanhTienKM + GiaTriKMThayDoi) 
		FROM dbo.ThucChayDaTinh
		WHERE HopDongChiTietREF = @HopDongChiTietREF
		AND NgayThucHien <= @NgayThucHien
		--AND NgayThucHien < @NgayThucHien
		
		SET @ThanhTienTCDT = ISNULL(@ThanhTienTCDT,0)
		--2. TINH SO TIEN THUC CHAY TAI NGAY THEO THAM SO TRUYEN VAO (C)
		SET @ThanhTienThucChayNgay = @SoLuongThucChayNgay*@DonGiaSauChietKhau;
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
	SET @SoLuongThucChay = round(ISNULL(@ThanhTienThucChay/@DonGiaSauChietKhau,0),0);
	-- Return the result of the function
	RETURN @SoLuongThucChay

END

```
