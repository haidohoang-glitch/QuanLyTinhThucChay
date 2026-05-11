# Function: `ThucChay_ThanhTienThucChay_ThanhTien_GGFB_DEV`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2020-10-15 15:49:18.410000
- **Ngày sửa cuối**: 2020-10-15 16:24:35.690000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@TongThanhTienThucChay` | `float(8)` | No |
| `@TongThanhTienThucChayKM` | `float(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@SoLuongHD` | `bigint(8)` | No |
| `@DonGiaHD` | `bigint(8)` | No |
| `@ThanhTien` | `bigint(8)` | No |
| `@ChietKhau` | `int(4)` | No |
| `@MaxTienThucChayBanOrder` | `float(8)` | No |
| `@TongTienThucChaySauChietKhauOder` | `float(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
/*
select[dbo].[ThucChay_ThanhTienThucChay_ThanhTien_GGFB] 
(
	@TongThanhTienThucChay FLOAT,
	@TongThanhTienThucChayKM FLOAT,
	@NgayThucHien DATETIME,
	@HopDongChiTietREF INT,
	@SoLuongHD BIGINT,
	@DonGiaHD BIGINT,
	@ThanhTien BIGINT,
	@ChietKhau INT
)
*/
CREATE  FUNCTION [dbo].[ThucChay_ThanhTienThucChay_ThanhTien_GGFB_DEV] 
(
	@TongThanhTienThucChay FLOAT,
	@TongThanhTienThucChayKM FLOAT,
	@NgayThucHien DATETIME,
	@HopDongChiTietREF INT,
	@SoLuongHD BIGINT,
	@DonGiaHD BIGINT,
	@ThanhTien BIGINT,
	@ChietKhau INT,
	@MaxTienThucChayBanOrder FLOAT,
	@TongTienThucChaySauChietKhauOder FLOAT
)
RETURNS FLOAT
AS
BEGIN
	DECLARE  @ThanhTienHD FLOAT=0, @ThanhTienTCDT FLOAT=0
	, @ThanhTienThucChay FLOAT =0
	, @ThanhTienThucChayNgay FLOAT=0
	, @ThanhTienHD_HDCT FLOAT=0, @ThanhTienTCDT_HDCT FLOAT=0
	, @ThanhTienThucChay_HDCT FLOAT =0
	, @ThanhTienThucChayNgay_HDCT FLOAT=0
	
	--0. Get thanh tien thuc chay hien tai/ khuyen mai
	IF(@ChietKhau <> 100)
	BEGIN
		--1. TINH SO TIEN THUC CHAY DA TINH (THANHTIENSAUCHIETKHAU + GIATRITHAYDOI) (B)
		SELECT @ThanhTienTCDT_HDCT = SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) 
		FROM dbo.ThucChayDaTinh
		WHERE HopDongChiTietREF = @HopDongChiTietREF
		AND NgayThucHien <= @NgayThucHien

		SET @ThanhTienTCDT = @TongTienThucChaySauChietKhauOder


		SET @ThanhTienTCDT = ISNULL(@ThanhTienTCDT,0)
		SET @ThanhTienTCDT_HDCT = ISNULL(@ThanhTienHD_HDCT,0)
		--2. TINH SO TIEN THUC CHAY TAI NGAY THEO THAM SO TRUYEN VAO (C)
		SET @ThanhTienThucChayNgay = @TongThanhTienThucChay;
		
		--3. XAC DINH TIEN HOPDONGCHITIET (A)
		--SET @ThanhTienHD = @ThanhTien
		SET @ThanhTienHD = @MaxTienThucChayBanOrder
		SET @ThanhTienHD_HDCT = @ThanhTien 
	END
	ELSE
	BEGIN
		--1. TINH SO TIEN THUC CHAY DA TINH (THANHTIENSAUCHIETKHAU + GIATRITHAYDOI) (B)
		SELECT @ThanhTienTCDT_HDCT = SUM(ThanhTienKM + GiaTriKMThayDoi) 
		FROM dbo.ThucChayDaTinh
		WHERE HopDongChiTietREF = @HopDongChiTietREF
		AND NgayThucHien <= @NgayThucHien
		--AND NgayThucHien < @NgayThucHien
		SET @ThanhTienTCDT = @TongTienThucChaySauChietKhauOder
		
		SET @ThanhTienTCDT = ISNULL(@ThanhTienTCDT,0)
		SET @ThanhTienTCDT_HDCT = ISNULL(@ThanhTienTCDT_HDCT,0)
		--2. TINH SO TIEN THUC CHAY TAI NGAY THEO THAM SO TRUYEN VAO (C)
		SET @ThanhTienThucChayNgay = @TongThanhTienThucChayKM;
		
		--3. XAC DINH TIEN HOPDONGCHITIET (A)
		--SET @ThanhTienHD = @SoLuongHD*@DonGiaHD
		SET @ThanhTienHD = @MaxTienThucChayBanOrder
		SET @ThanhTienHD_HDCT = @DonGiaHD*@SoLuongHD
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
	SET @ThanhTienThucChay = ISNULL(@ThanhTienThucChay,0);

	SET @ThanhTienThucChayNgay_HDCT = @ThanhTienThucChay;

	--**** CHECK LAI BIEU THUC LAN 2 VOI THONG TIN LA HOP DONG
	--4. BIEU THUC CHECK
	--4.1 NEU A >= B + C => THANH TIEN THUC CHAY = C
	IF (@ThanhTienHD_HDCT >= (@ThanhTienTCDT_HDCT + @ThanhTienThucChayNgay_HDCT))
		SET @ThanhTienThucChay_HDCT = @ThanhTienThucChayNgay_HDCT
	--4.2 NEU A < B+C 
	ELSE
		BEGIN
			--4.2.1 NEU A <= B => THANH TIEN THUC CHAY = 0
			--4.2.1 NEU A <= B => THANH TIEN THUC CHAY = 05
			IF (@ThanhTienHD_HDCT <= @ThanhTienTCDT_HDCT) 
				SET @ThanhTienThucChay_HDCT = 0
			--4.2.2 NEU A > B => THANH TIEN THUC CHAY = A- B
			ELSE
				SET @ThanhTienThucChay_HDCT = @ThanhTienHD_HDCT - @ThanhTienTCDT_HDCT
		END
	
	--5. quy doi ra so luong phai them vao
	SET @ThanhTienThucChay_HDCT = ISNULL(@ThanhTienThucChay_HDCT,0);
	-- Return the result of the function
	RETURN @ThanhTienThucChay_HDCT

END

```
