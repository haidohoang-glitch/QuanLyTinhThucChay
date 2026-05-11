# Function: `ThucChay_GetSoLuongThucChay_Admatic_v1_test`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2017-06-02 09:55:28.063000
- **Ngày sửa cuối**: 2017-06-02 09:57:31.470000

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

CREATE FUNCTION [dbo].[ThucChay_GetSoLuongThucChay_Admatic_v1_test] 
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
RETURNS FLOAT
AS
BEGIN
	DECLARE @IsKM INT, @DonViQuyDoi INT = 1
	, @DonGiaSauChietKhau FLOAT=0, @ThanhTienHD BIGINT=0, @ThanhTienTCDT BIGINT=0
	, @SoLuongThucChay INT=0, @ThanhTienThucChay BIGINT =0
	, @SoLuongThucChayNgay INT=0, @ThanhTienThucChayNgay BIGINT=0
	

	--DECLARE @MinDate DATETIME
	IF(@DonGia_Banner = 0)
		SET @DonGia_Banner = 1
	IF (UPPER(@DonViTinh) = 'CPM')
	BEGIN
		SET @DonViQuyDoi = 1000
		SET @SoLuongThucChayNgay = @TongViewThucChay
	END
	IF (UPPER(@DonViTinh) = 'CPC')
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
	--RETURN @SoLuongThucChay
	RETURN @DonGia_Banner
END
--SELECT dbo.[ThucChay_GetSoLuongThucChay_Admatic_v1_test] (1942,9,NULL ,65000 ,'TRUE VIEW','2017-05-10', 505381,1, 75000000,60000000, 20 )
```
