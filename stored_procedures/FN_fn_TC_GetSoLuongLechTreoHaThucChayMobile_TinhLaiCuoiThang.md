# Function: `fn_TC_GetSoLuongLechTreoHaThucChayMobile_TinhLaiCuoiThang`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2017-09-13 11:14:39.877000
- **Ngày sửa cuối**: 2017-09-13 11:14:39.877000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@HopDongChiTietID` | `int(4)` | No |
| `@DonGia` | `float(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoLuongThucChay` | `int(4)` | No |
| `@DmBannerID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
--select [dbo].[ThucChay_GetSoLuongLechTreoHaThucChayMobile]  (61676,3000,'2014-07-21',3)
CREATE FUNCTION [dbo].[fn_TC_GetSoLuongLechTreoHaThucChayMobile_TinhLaiCuoiThang] 
(
	-- Add the parameters for the function here
	@HopDongChiTietID INT,
	@DonGia FLOAT,
	@NgayThucHien DATETIME,	
	@SoLuongThucChay INT,
	@DmBannerID INT
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @DonViTinh NVARCHAR(50), 
		    @ThanhTienTCDT FLOAT, @ThanhTienHD FLOAT, 
		    @ThanhTienThucChayNgay FLOAT, 
		    @ThanhTienLTH FLOAT,@SoLuongLTH FLOAT,@DmSanPhamREF INT,
		    @ChietKhau FLOAT, @IsKhuyenMai INT, @DonGiaSauChietKhau FLOAT,@ThanhTienTruocChietKhau FLOAT;

	SELECT @DonViTinh   = hdct.DonViTinh,
		   @ThanhTienHD = hdct.ThanhTien,
		   @IsKhuyenMai = hdct.IsKhuyenMai,
		   @ChietKhau = hdct.ChietKhau,
		   @ThanhTienTruocChietKhau = hdct.SoLuong*DonGia,
		   @DmSanPhamREF = hdct.DmSanPhamREF
	FROM HopDongChiTiet hdct 
	WHERE hdct.HopDongChiTietID = @HopDongChiTietID
	
	SELECT @DonGiaSauChietKhau = (CASE WHEN (@IsKhuyenMai = 0 AND @ChietKhau  <> 100) THEN @DonGia*(100 - @ChietKhau)/100
								  ELSE @DonGia
								  END
	)
	SELECT @ThanhTienHD = ( CASE WHEN (@IsKhuyenMai = 0 AND @ChietKhau  <> 100) THEN @ThanhTienHD
							ELSE  @ThanhTienTruocChietKhau
							END
						  )
			--1. TINH SO TIEN THUC CHAY DA TINH (THANHTIENSAUCHIETKHAU + GIATRITHAYDOI) (B)
			IF @DmSanPhamREF = 342
			BEGIN
				SELECT @ThanhTienTCDT =  (CASE WHEN (@IsKhuyenMai = 1 OR @ChietKhau = 100) THEN SUM(ISNULL(tcdt.ThanhTienKM,0) + ISNULL(tcdt.GiaTriKMThayDoi,0))
									   ELSE SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0))
									  END)
				FROM dbo.ThucChayDaTinh_TinhLaiCuoiThang tcdt
				WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID --AND tcdt.DmBannerREF = @DmBannerID
					AND tcdt.NgayThucHien <= @NgayThucHien
					AND tcdt.DmSanPhamREF = 342
			END
			ELSE IF @DmSanPhamREF = 381
			BEGIN
				SELECT @ThanhTienTCDT =  (CASE WHEN (@IsKhuyenMai = 1 OR @ChietKhau = 100) THEN SUM(ISNULL(tcdt.ThanhTienKM,0) + ISNULL(tcdt.GiaTriKMThayDoi,0))
									   ELSE SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0))
									  END)
				FROM dbo.ThucChayDaTinh_TinhLaiCuoiThang tcdt
				WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID --AND tcdt.DmBannerREF = @DmBannerID
					AND tcdt.NgayThucHien <= @NgayThucHien
					AND tcdt.DmSanPhamREF = 381
			END
			
			--2. TINH SO TIEN THUC CHAY TAI NGAY THEO THAM SO TRUYEN VAO (C)
			SELECT @ThanhTienThucChayNgay = @SoLuongThucChay*@DonGiaSauChietKhau;
		
			--3. XAC DINH TIEN HOPDONGCHITIET (A)
			
			--4. BIEU THUC CHECK
			--4.1 NEU A >= B + C => THANH TIEN LECH TREO HA = 0
			--4.2 NEU A < B+C => 
			--4.2.1 NEU A <= B => THANH TIEN LECH TREO HA = C
			--4.2.2 NEU A > B => THANH TIEN LECH TREO HA = ( B + C - A)			
			--4.1
			IF (@ThanhTienHD >= (@ThanhTienTCDT + @ThanhTienThucChayNgay))
				SET @ThanhTienLTH = 0
			--4.2
			ELSE
				BEGIN
					--4.2.1 NEU A <= B => THANH TIEN LECH TREO HA = C
					IF (@ThanhTienHD <= @ThanhTienTCDT) 
						SET @ThanhTienLTH = @ThanhTienThucChayNgay
					--4.2.2 NEU A > B => THANH TIEN LECH TREO HA = (B + C) - A
					ELSE
						SET @ThanhTienLTH = (@ThanhTienTCDT + @ThanhTienThucChayNgay) - @ThanhTienHD
				END
			
			--5 SO LUONG LECH TREO HA = @ThanhTienLTH/DONGIA
								
			--lay so luong thuc chay ngay thuc hien
			IF @DonGiaSauChietKhau <> 0 
				SET @SoLuongLTH = ISNULL(@ThanhTienLTH/@DonGiaSauChietKhau,0)
			ELSE 
				set @SoLuongLTH = 0

	-- tinh thanhtien thuc chay ngay thuc hien
			
	-- Return the result of the function
	RETURN @SoLuongLTH;
END

```
