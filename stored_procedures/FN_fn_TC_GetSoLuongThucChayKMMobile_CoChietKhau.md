# Function: `fn_TC_GetSoLuongThucChayKMMobile_CoChietKhau`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2017-11-01 09:26:04.300000
- **Ngày sửa cuối**: 2019-10-11 16:25:18.500000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@HopDongChiTietID` | `int(4)` | No |
| `@IsKhuyenMai` | `int(4)` | No |
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
--select dbo.ThucChay_GetSoLuongThucChayKMMobile(56937,1,35,'2014-06-09',19956)
CREATE FUNCTION [dbo].[fn_TC_GetSoLuongThucChayKMMobile_CoChietKhau]
    (
      -- Add the parameters for the function here
      @HopDongChiTietID INT ,
      @IsKhuyenMai INT ,
      @DonGia FLOAT ,
      @NgayThucHien DATETIME ,
      @SoLuongThucChay INT ,
      @DmBannerID INT
    )
RETURNS FLOAT
AS
    BEGIN
	-- Declare the return variable here
        DECLARE @DonViTinh NVARCHAR(50) ,
            @ThanhTienTCDT FLOAT ,
            @ThanhTienHD FLOAT ,
            @ThanhTienThucChayNgay FLOAT ,
            @ThanhTienThucChay FLOAT ,
            @ChietKhau FLOAT ,
            @DmSanPhamREF INT ,
            @DonGiaSauChietKhau FLOAT ,
            @HopDongID INT ,
            @SoLuongKM INT ,
            @DonGiaHDCTChinh FLOAT ,
            @ThanhTienHDCTChinh FLOAT ,
            @TyLeKM FLOAT,
			@SoLuongThucChayKM FLOAT = 0

        SELECT  @DonViTinh = hdct.DonViTinh ,
                @ThanhTienHD = hdct.ThanhTien ,
                @DmSanPhamREF = hdct.DmSanPhamREF ,
                @HopDongID = hdct.HopDongFK 
        FROM    dbo.HopDongChiTiet hdct
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

        SET @Tong_TC = CONVERT(FLOAT, ISNULL(@SoLuongThucChay, 0))
		IF(ISNULL(@DonGiaHDCTChinh,0) = 0)
		BEGIN
		    SET @TyLeKM =  ISNULL((SELECT TOP (1) ISNULL(tcct.TiLeThucChayHDCTSoVoiBanner,0) FROM dbo.ThucChayHopDongChiTietAndBanner tcct
			WHERE tcct.HopDongChiTietREF = @HopDongChiTietID
			AND tcct.DmBannerID = CONVERT(NVARCHAR(50),@DmBannerID) ORDER BY tcct.HopDongChiTietREF),0)
		END
			
		ELSE
			SET @TyLeKM = ( @SoLuongKM * @DonGiaHDCTChinh ) / @ThanhTienHDCTChinh
	
        IF ( @IsKhuyenMai = 1 AND @TyLeKM <> 100
           )
            BEGIN
                SET @SoLuongThucChayKM = ROUND(@Tong_TC - ( @Tong_TC / ( 1 + ( (100 - @ChietKhau)/100 ) * @TyLeKM ) ), 0)
            END
            
        ELSE
            BEGIN
                SET @SoLuongThucChayKM = (@Tong_TC*@TyLeKM)/100
            END
			
        RETURN @SoLuongThucChayKM
	
    END

```
