# Function: `ThucChay_GetThanhTienChuanThucChay_CPR`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-09-14 14:36:23.653000
- **Ngày sửa cuối**: 2015-12-10 11:55:32.253000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@DonViTinhREF` | `int(4)` | No |
| `@DonGia` | `float(8)` | No |
| `@ChietKhau` | `float(8)` | No |
| `@UV` | `int(4)` | No |
| `@View_user` | `int(4)` | No |
| `@UVThucChay` | `int(4)` | No |
| `@UVThucChayNgay` | `int(4)` | No |
| `@TongViewThucChay` | `float(8)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(200)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetThanhTienChuanThucChay_CPR]
(
	-- Add the parameters for the function here
	@DonViTinhREF      INT,
	@DonGia            FLOAT,
	@ChietKhau         FLOAT,
	@UV                INT,
	@View_user         INT,
	@UVThucChay        INT,
	@UVThucChayNgay		INT,
	@TongViewThucChay  FLOAT,
	@HopDongChiTietID  INT,
	@SoHopDong         NVARCHAR(100),
	@TypeProduct       INT,
	@NgayThucHien      DATETIME
)
RETURNS FLOAT
AS

BEGIN
	-- Declare the return variable here
	DECLARE @ThanhTienThucChay      FLOAT,
	        @TongThucChayDaTinhBef  BIGINT = 0,
	        @TongVewInNgay          INT = 0,
	        @tongViewDenNgay        BIGINT = 0,
	        @TongViewGoiMua         BIGINT = 0,
	        @ThucChayInNgay         FLOAT = 0,
	        @TongVw_tonggoi         FLOAT = 0,
	        @TongUv_tonggoi         FLOAT = 0
	
	IF (@DonViTinhREF = 10)
	BEGIN
	    --XAC DINH TONG GIA TRI THUC CHAY TRUOC NGAY THUC HIEN
	    IF (@ChietKhau = 100)
	        SET @TongThucChayDaTinhBef = (
	                SELECT SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)
	                FROM   ThucChayDaTinh tcdt
	                WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietID
	                       AND tcdt.SoHopDong = @SoHopDong
	                       AND tcdt.NgayThucHien < @NgayThucHien
	            )
	    ELSE
	        SET @TongThucChayDaTinhBef = (
	                SELECT SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)
	                       / ((100 -@ChietKhau) / 100)
	                FROM   ThucChayDaTinh tcdt
	                WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietID
	                       AND tcdt.SoHopDong = @SoHopDong
	                       AND tcdt.NgayThucHien < @NgayThucHien
	            )
	    --XAC DINH TONG VIEW DEN NGAY THUC HIEN 
	    SET @TongThucChayDaTinhBef = ISNULL(@TongThucChayDaTinhBef, 0)
	    
	    SET @tongViewDenNgay = (
	            SELECT SUM(A.TongViewThucChay)
	            FROM   (
	                       SELECT A.NgayThucHien,
	                              ROUND(
	                                  SUM((A.TongViewThucChay * B.TiLeThucChayHDCTSoVoiBanner) / 100),
	                                  0
	                              ) TongViewThucChay,
	                              ROUND(
	                                  SUM(
	                                      (A.TongClickThucChay * B.TiLeThucChayHDCTSoVoiBanner)
	                                      / 100
	                                  ),
	                                  0
	                              ) TongClickThucChay,
	                              SUM(ISNULL(A.TongSoBaiViet, 0)) TongSoBaiViet,
	                              B.HopDongChiTietREF,
	                              A.TypeProduct
	                       FROM   ThucChay A
	                              INNER JOIN (
	                                       SELECT DISTINCT b.DmBannerID,
	                                              b.HopDongChiTietREF,
	                                              b.HopDongREF,
	                                              b.TiLeThucChayHDCTSoVoiBanner,
	                                              b.DeletedStatus,
	                                              b.DaThucHienUpdateTiLe
	                                       FROM   dbo.ThucChayHopDongChiTietAndBanner 
	                                              b
	                                   ) B
	                                   ON  B.DmBannerID = CONVERT(NVARCHAR(50), A.DmBannerREF)
	                       WHERE  a.SoHopDong = @SoHopDong
	                              AND a.TypeProduct = @TypeProduct
	                              AND B.DeletedStatus = 0
	                              AND A.NgayThucHien <= @NgayThucHien
	                       GROUP BY
	                              A.NgayThucHien,
	                              B.HopDongChiTietREF,
	                              A.TypeProduct
	                   )A
	            WHERE  1 = 1
	                   AND A.HopDongChiTietREF = @HopDongChiTietID
	        )
	    
	    SET @tongViewDenNgay = ISNULL(@tongViewDenNgay, 0)
	    
	    SET @TongVewInNgay = (
	            SELECT SUM(A.TongViewThucChay)
	            FROM   (
	                       SELECT A.NgayThucHien,
	                              ROUND(
	                                  SUM((A.TongViewThucChay * B.TiLeThucChayHDCTSoVoiBanner) / 100),
	                                  0
	                              ) TongViewThucChay,
	                              ROUND(
	                                  SUM(
	                                      (A.TongClickThucChay * B.TiLeThucChayHDCTSoVoiBanner)
	                                      / 100
	                                  ),
	                                  0
	                              ) TongClickThucChay,
	                              SUM(ISNULL(A.TongSoBaiViet, 0)) TongSoBaiViet,
	                              B.HopDongChiTietREF,
	                              A.TypeProduct
	                       FROM   ThucChayTemp A
	                              INNER JOIN (
	                                       SELECT DISTINCT b.DmBannerID,
	                                              b.HopDongChiTietREF,
	                                              b.HopDongREF,
	                                              b.TiLeThucChayHDCTSoVoiBanner,
	                                              b.DeletedStatus,
	                                              b.DaThucHienUpdateTiLe
	                                       FROM   dbo.ThucChayHopDongChiTietAndBanner 
	                                              b
	                                   ) B
	                                   ON  B.DmBannerID = CONVERT(NVARCHAR(50), A.DmBannerREF)
	                       WHERE  a.SoHopDong = @SoHopDong
	                              AND a.TypeProduct = @TypeProduct
	                              AND B.DeletedStatus = 0
	                       GROUP BY
	                              A.NgayThucHien,
	                              B.HopDongChiTietREF,
	                              A.TypeProduct
	                   )A
	            WHERE  1 = 1
	                   AND A.HopDongChiTietREF = @HopDongChiTietID
	        )
	    
	    SET @TongVewInNgay = ISNULL(@TongVewInNgay, 0)
	    
	    IF (@UV * @View_user = 0 OR @UV = 0 OR @TongVewInNgay = 0)
	    BEGIN
	        SET @ThanhTienThucChay = 0
	    END
	    ELSE
	    BEGIN
	        SET @TongViewGoiMua = @UV * @View_user
	        SET @TongVw_tonggoi = (
	                CONVERT(FLOAT, @tongViewDenNgay) / CONVERT(FLOAT, @TongViewGoiMua)
	            )
	        
	        SET @TongUv_tonggoi = (CONVERT(FLOAT, @UVThucChay) / CONVERT(FLOAT, @UV))
	        IF (@TongVw_tonggoi >= 1)
	            SET @TongVw_tonggoi = 1
	        
	        IF (@TongUv_tonggoi >= 1)
	            SET @TongUv_tonggoi = 1
	        
	        SET @ThucChayInNgay = ((@tongvw_tonggoi + @TongUv_tonggoi) / 2 * @DonGia) 
	            - @TongThucChayDaTinhBef
	        
	        SET @ThanhTienThucChay = @ThucChayInNgay * (
	                CONVERT(FLOAT, @TongViewThucChay) / CONVERT(FLOAT, @TongVewInNgay)
	            )
	    END
	END
	ELSE IF (@DonViTinhREF = 30)
	BEGIN
	
		SET @ThanhTienThucChay = @UVThucChayNgay * @DonGia

	END
	
	SET @ThanhTienThucChay = ISNULL(@ThanhTienThucChay, 0)
	RETURN @ThanhTienThucChay
END

```
