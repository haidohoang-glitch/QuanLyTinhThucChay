# Function: `ThucChay_GetSoLuongThucChay_ThanhTien_GGFB`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2020-08-17 14:26:58.543000
- **Ngày sửa cuối**: 2020-10-17 11:18:58.740000

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
[dbo].[ThucChay_GetSoLuongThucChay_ThanhTien_GGFB] 
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
CREATE  FUNCTION [dbo].[ThucChay_GetSoLuongThucChay_ThanhTien_GGFB] 
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
	@ChietKhau INT,
	@MaxTienThucChayBanOrder FLOAT,
	@TongTienThucChaySauChietKhauOder FLOAT
)
RETURNS FLOAT
AS
BEGIN
	DECLARE  @DonGiaSauChietKhau FLOAT=0, @ThanhTienHD BIGINT=0, @ThanhTienTCDT BIGINT=0
	--, @SoLuongThucChay INT=0
	, @ThanhTienThucChay BIGINT =0
	, @ThanhTienThucChayNgay BIGINT=0
	--**
	, @ThanhTienHD_HDCT BIGINT=0, @ThanhTienTCDT_HDCT BIGINT=0
	, @SoLuongThucChay_HDCT INT=0, @ThanhTienThucChay_HDCT BIGINT =0
	, @ThanhTienThucChayNgay_HDCT BIGINT=0
	

	
	--0. Get thanh tien thuc chay hien tai/ khuyen mai
	IF(@ChietKhau <> 100)
	BEGIN
		--XAC DINH DON GIA SAU CHIET KHAU
		SET @DonGiaSauChietKhau = (CASE WHEN @TongSoluongThucChay <> 0 THEN @TongThanhTienThucChay/@TongSoluongThucChay
									ELSE 0
									END )
		--1. TINH SO TIEN THUC CHAY DA TINH (THANHTIENSAUCHIETKHAU + GIATRITHAYDOI) (B)
		SELECT @ThanhTienTCDT_HDCT = SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) 
		FROM dbo.ThucChayDaTinh
		WHERE HopDongChiTietREF = @HopDongChiTietREF
		AND NgayThucHien <= @NgayThucHien

		SET @ThanhTienTCDT = @TongTienThucChaySauChietKhauOder

		SET @ThanhTienTCDT = ISNULL(@ThanhTienTCDT,0)
		SET @ThanhTienTCDT_HDCT = ISNULL(@ThanhTienTCDT_HDCT,0)
		--2. TINH SO TIEN THUC CHAY TAI NGAY THEO THAM SO TRUYEN VAO (C)
		SET @ThanhTienThucChayNgay = @TongThanhTienThucChay;
		--3. XAC DINH TIEN HOPDONGCHITIET (A)
		--SET @ThanhTienHD = @ThanhTien
		SET @ThanhTienHD = @MaxTienThucChayBanOrder
		SET @ThanhTienHD_HDCT = @ThanhTien
	END
	ELSE
	BEGIN
		--XAC DINH DON GIA SAU CHIET KHAU
		SET @DonGiaSauChietKhau = (CASE WHEN @TongSoLuongThucChayKM  <> 0 THEN @TongThanhTienThucChayKM/@TongSoLuongThucChayKM
									ELSE 0
									END )
		----1. TINH SO TIEN THUC CHAY DA TINH (THANHTIENSAUCHIETKHAU + GIATRITHAYDOI) (B)
		SELECT @ThanhTienTCDT_HDCT = SUM(ThanhTienKM + GiaTriKMThayDoi) 
		FROM dbo.ThucChayDaTinh
		WHERE HopDongChiTietREF = @HopDongChiTietREF
		AND NgayThucHien <= @NgayThucHien
		----AND NgayThucHien < @NgayThucHien
		SET @ThanhTienTCDT = @TongTienThucChaySauChietKhauOder
		
		SET @ThanhTienTCDT = ISNULL(@ThanhTienTCDT,0)
		SET @ThanhTienTCDT_HDCT = ISNULL(@ThanhTienTCDT_HDCT,0)
		--2. TINH SO TIEN THUC CHAY TAI NGAY THEO THAM SO TRUYEN VAO (C)
		SET @ThanhTienThucChayNgay = @TongThanhTienThucChayKM;
		--3. XAC DINH TIEN HOPDONGCHITIET (A)
		--SET @ThanhTienHD = @SoLuongHD*@DonGiaHD
		SET @ThanhTienHD = @MaxTienThucChayBanOrder
		SET @ThanhTienHD_HDCT = @SoLuongHD*@DonGiaHD
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
	
	----5. quy doi ra so luong phai them vao
	--SET @SoLuongThucChay = (CASE WHEN @DonGiaSauChietKhau <> 0 THEN round(ISNULL(@ThanhTienThucChay/@DonGiaSauChietKhau,0),0)
	--						ELSE 0
	--						END)

	
	--**** CHECK LAI BIEU THUC LAN 2 VOI THONG TIN LA HOP DONG***----
	SET @ThanhTienThucChayNgay_HDCT = @ThanhTienThucChay

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
	SET @SoLuongThucChay_HDCT = (CASE WHEN @DonGiaSauChietKhau <> 0 THEN round(ISNULL(@ThanhTienThucChay_HDCT/@DonGiaSauChietKhau,0),0)
							ELSE 0
							END)
	-- Return the result of the function
	RETURN @SoLuongThucChay_HDCT

END

```
