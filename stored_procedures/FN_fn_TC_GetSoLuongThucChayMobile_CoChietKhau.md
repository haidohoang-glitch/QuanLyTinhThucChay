# Function: `fn_TC_GetSoLuongThucChayMobile_CoChietKhau`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2017-06-23 17:55:39.187000
- **Ngày sửa cuối**: 2018-05-10 11:35:25.630000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@HopDongChiTietID` | `int(4)` | No |
| `@DonGia` | `float(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@TongViewThucChay` | `int(4)` | No |
| `@TongClickThucChay` | `int(4)` | No |
| `@ProductUnitName` | `nvarchar(100)` | No |
| `@DmBannerID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
--SELECT dbo.[ThucChay_GetSoLuongThucChayMobile](69307, 3000,'2015-03-08', 1619,2,'CPC')	
CREATE FUNCTION [dbo].[fn_TC_GetSoLuongThucChayMobile_CoChietKhau]
    (
      -- Add the parameters for the function here
      @HopDongChiTietID INT ,
      @DonGia FLOAT ,
      @NgayThucHien DATETIME ,
      @TongViewThucChay INT ,
      @TongClickThucChay INT ,
      @ProductUnitName NVARCHAR(50) ,
      @DmBannerID INT 
    )
RETURNS FLOAT
AS
    BEGIN
	-- Declare the return variable here
        DECLARE @DonViTinh NVARCHAR(50) ,
            @ThanhTienTCDT FLOAT ,
            @ThanhTienHD FLOAT ,
            @IsKhuyenMai INT ,
            @ThanhTienThucChayNgay FLOAT ,
            @ThanhTienThucChay FLOAT ,
            @ChietKhau FLOAT ,
            @SoLuongThucChay FLOAT = 0,
            @DmSanPhamREF INT ,
            @DonGiaSauChietKhau FLOAT ,
            @HopDongID INT ,
            @SoLuongKM INT ,
            @DonGiaHDCTChinh FLOAT ,
            @ThanhTienHDCTChinh FLOAT ,
            @TyLeKM FLOAT

        SELECT  @DonViTinh = hdct.DonViTinh ,
                @ThanhTienHD = hdct.ThanhTien ,
                @IsKhuyenMai = hdct.IsKhuyenMai ,
                @DmSanPhamREF = hdct.DmSanPhamREF ,
                @HopDongID = hdct.HopDongFK 
        FROM    HopDongChiTiet hdct
        WHERE   hdct.HopDongChiTietID = @HopDongChiTietID


        SELECT TOP 1
                @DonGiaHDCTChinh = pb.DonGia ,
				@ChietKhau = pb.ChietKhau ,
                @ThanhTienHDCTChinh = pb.ThanhTien
        FROM    dbo.HopDongChiTiet pb
        WHERE   pb.DmSanPhamREF = 342
                AND pb.HopDongFK = @HopDongID
                AND pb.ChietKhau <> 100

		SELECT @SoLuongKM = SUM(CASE WHEN pb.DonViTinh = 'CPC' THEN pb.SoLuong
										WHEN pb.DonViTinh = 'CPM' THEN pb.SoLuong * 1000
										ELSE 0 END)
        FROM    dbo.HopDongChiTiet pb
        WHERE   pb.DmSanPhamREF = 342
                AND pb.HopDongFK = @HopDongID
                AND pb.ChietKhau = 100

        DECLARE @Tong_TC FLOAT

        SET @Tong_TC = CONVERT(FLOAT, ISNULL(( CASE WHEN @DonViTinh = 'CPC'
                                     THEN @TongClickThucChay
                                     WHEN @DonViTinh = 'CPM'
                                     THEN @TongViewThucChay
                                     WHEN @DonViTinh = 'CPV' THEN 0--anh Khanh chua tra so								
                                     ELSE ( CASE WHEN @ProductUnitName = 'CPC'
                                                 THEN @TongClickThucChay
                                                 ELSE @TongViewThucChay
                                            END )
                                END ), 0))

        SET @TyLeKM = ( @SoLuongKM * @DonGiaHDCTChinh ) / @ThanhTienHDCTChinh
	
        IF ( @IsKhuyenMai = 1
           )
            BEGIN
                SET @SoLuongThucChay = 0
            END
            
        ELSE
            BEGIN
                SET @SoLuongThucChay = ROUND(@Tong_TC / ( 1 + ( (100 - @ChietKhau)/100 )  * @TyLeKM ), 0)

				-----------check so luong thuc chay thuc te
				
                SET @DonGiaSauChietKhau = @DonGia * ( 100 - @ChietKhau ) / 100
				--1. TINH SO TIEN THUC CHAY DA TINH (THANHTIENSAUCHIETKHAU + GIATRITHAYDOI) (B)
                IF @DmSanPhamREF = 342
                    BEGIN
                        SELECT  @ThanhTienTCDT = ISNULL(SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0)), 0)
                        FROM    dbo.ThucChayDaTinh_DoiTruVaTinhLai_Mobile tcdt
                        WHERE   tcdt.HopDongChiTietREF = @HopDongChiTietID
                                AND tcdt.NgayThucHien <= @NgayThucHien
                                AND tcdt.TrangThaiHopDong <> 3
                                --AND tcdt.DmBannerREF = @DmBannerID
								AND tcdt.DmSanPhamREF = 342
                    END
              			
				--2. TINH SO TIEN THUC CHAY TAI NGAY THEO THAM SO TRUYEN VAO (C)
                SELECT  @ThanhTienThucChayNgay = @SoLuongThucChay
                        * @DonGiaSauChietKhau;
			
				--3. XAC DINH TIEN HOPDONGCHITIET (A)
			
				--4. BIEU THUC CHECK
				--4.1 NEU A >= B + C => THANH TIEN THUC CHAY = C
                IF ( @ThanhTienHD >= ( @ThanhTienTCDT + @ThanhTienThucChayNgay ) )
                    SET @ThanhTienThucChay = @ThanhTienThucChayNgay
				--4.2 NEU A < B+C 
                ELSE
                    BEGIN
						--4.2.1 NEU A <= B => THANH TIEN THUC CHAY = 0
                        IF ( @ThanhTienHD <= @ThanhTienTCDT )
                            SET @ThanhTienThucChay = 0
						--4.2.2 NEU A > B => THANH TIEN THUC CHAY = A- B
                        ELSE
                            SET @ThanhTienThucChay = @ThanhTienHD
                                - @ThanhTienTCDT
                    END
			
				--5 SO LUONG THUC CHAY = THANHTIENTHUCCHAY/DONGIA
				--lay so luong thuc chay ngay thuc hien
                IF @DonGiaSauChietKhau <> 0
                    SET @SoLuongThucChay = ROUND(ISNULL(@ThanhTienThucChay/ @DonGiaSauChietKhau,0), 0);
                ELSE
                    SET @SoLuongThucChay = 0	
			
				---------------
            END
			
	-- Return the result of the function
        RETURN @SoLuongThucChay

    END

```
