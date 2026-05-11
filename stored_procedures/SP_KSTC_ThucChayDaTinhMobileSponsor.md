# Stored Procedure: `KSTC_ThucChayDaTinhMobileSponsor`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-09 14:29:19.733000
- **Ngày sửa cuối**: 2014-12-09 15:08:38.653000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--KSTC_ThucChayDaTinhMobileSponsor '2014-12-06',10
CREATE PROCEDURE dbo.KSTC_ThucChayDaTinhMobileSponsor 
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@DmSanPhamREF INT --10: Mobile, 381: Sponsor
	
AS
BEGIN
--UPDATE thucchay SET TypeProduct = 381 WHERE DmSanPhamREF = 381 WHERE NgayThucHien = @NgayThucHien

DECLARE @SoHopDong NVARCHAR(50), 
		@HopDongChiTietREF INT, 
		@ProductUnitName NVARCHAR(50), 
		@BannerType INT,
		@DonViTinh NVARCHAR(50),
		@DonGia INT,
		@SoLuong INT,
		@ChietKhau INT,
		@IsKhuyenMai INT,
		@ThanhTien INT,
		@DeletedStatus INT,
		@TienThucChayTuTinh FLOAT,@TienThucChayKMTuTinh FLOAT,
		@SoLuongThucChayNgay INT, @SoLuongThucChay INT,
		
		@TienThucChayNgay FLOAT,@TienThucChayKMNgay FLOAT, @TienThucChay FLOAT, @TienThucChayKM FLOAT,
		@TienThucChay2013 FLOAT, @TienThucChayKM2013 FLOAT,
		@DonGiaSauChietKhau FLOAT
		
DECLARE @Table TABLE 
	(HopDongChiTietREF INT,
	NgayThucHien DATETIME,
	IsKhuyenMai INT,
	TienThucChayNgay FLOAT,
	TienThucChayKMNgay FLOAT
	)		

IF @DmSanPhamREF = 10
DECLARE vendor_cursor CURSOR FOR 
	SELECT distinct dbo.ThucChay_FormatSoHopDong(SoHopDong)SoHopDong, 
	tc.HopDongChiTietREF, tc.ProductUnitName, tc.BannerType
	FROM ThucChay tc 
	WHERE tc.NgayThucHien = @NgayThucHien
		AND tc.TypeProduct = @DmSanPhamREF
		AND tc.NgayThucHien >='2014-01-01'
	GROUP BY dbo.ThucChay_FormatSoHopDong(SoHopDong), tc.HopDongChiTietREF, tc.ProductUnitName, tc.BannerType
	ORDER BY tc.HopDongChiTietREF

OPEN vendor_cursor

FETCH NEXT FROM vendor_cursor INTO @SoHopDong,@HopDongChiTietREF,@ProductUnitName,@BannerType

WHILE @@FETCH_STATUS = 0
BEGIN
	SET @DonGia = 0;
	SET @SoLuong = 0;
	SET	@ChietKhau = 0;
	SET @TienThucChayTuTinh = 0;
	SET @TienThucChayKMTuTinh = 0;
	
    SELECT  @DonViTinh  = hdct.DonViTinh,
		@DonGia = hdct.DonGia,
		@SoLuong = hdct.SoLuong,
		@ChietKhau = hdct.ChietKhau,
		@IsKhuyenMai = hdct.IsKhuyenMai,
		@ThanhTien = hdct.ThanhTien
    FROM HopDongChiTiet hdct 
    WHERE hdct.HopDongChiTietID = @HopDongChiTietREF
    AND hdct.DeletedStatus <> 1
    
    IF @DmSanPhamREF = 10 
		SET @DonGia = dbo.ThucChay_GetDonGiaTheoDonViTruocChietKhau(@HopDongChiTietREF,@ProductUnitName,@BannerType,@NgayThucHien)
	ELSE IF @DmSanPhamREF = 381
		SET @DonGia = (SELECT CASE WHEN @DonViTinh IN ('CPC') THEN @DonGia
						ELSE 3000
						END)       
   SET @DonGiaSauChietKhau = @DonGia*(100-@ChietKhau)/100
    
    
    SET @TienThucChayNgay = (SELECT CASE WHEN @DonViTinh = 'CPC' THEN SUM(TongClickThucChay*@DonGiaSauChietKhau)
										    WHEN @DonViTinh = 'CPM' THEN SUM(TongViewThucChay*@DonGiaSauChietKhau)
										    WHEN (@DonViTinh NOT IN ('CPC','CPM','CPV') AND @ProductUnitName = 'CPC') THEN SUM(TongClickThucChay*@DonGiaSauChietKhau)
										    WHEN (@DonViTinh NOT IN ('CPC','CPM','CPV') AND @ProductUnitName = 'CPM') THEN  SUM(TongViewThucChay*@DonGiaSauChietKhau)
								ELSE 0
                                       END
                                FROM thucchay WHERE HopDongChiTietREF = @HopDongChiTietREF 
                                 AND NgayThucHien = @NgayThucHien
                                 AND BannerType = @BannerType                           
    )
   SET @TienThucChayKMNgay = (SELECT CASE WHEN @DonViTinh = 'CPC' THEN SUM(TongClickThucChay*@DonGia)
										    WHEN @DonViTinh = 'CPM' THEN SUM(TongViewThucChay*@DonGia)
										    WHEN (@DonViTinh NOT IN ('CPC','CPM','CPV') AND @ProductUnitName = 'CPC') THEN SUM(TongClickThucChay*@DonGia)
										    WHEN (@DonViTinh NOT IN ('CPC','CPM','CPV') AND @ProductUnitName = 'CPM') THEN  SUM(TongViewThucChay*@DonGia)
								ELSE 0
                                       END
                                FROM thucchay WHERE HopDongChiTietREF = @HopDongChiTietREF 
                                 AND NgayThucHien = @NgayThucHien
                                 AND BannerType = @BannerType                           
								)
	SET @TienThucChay = (SELECT CASE WHEN @DonViTinh = 'CPC' THEN SUM(TongClickThucChay*@DonGiaSauChietKhau)
										    WHEN @DonViTinh = 'CPM' THEN SUM(TongViewThucChay*@DonGiaSauChietKhau)
										    WHEN (@DonViTinh NOT IN ('CPC','CPM','CPV') AND @ProductUnitName = 'CPC') THEN SUM(TongClickThucChay*@DonGiaSauChietKhau)
										    WHEN (@DonViTinh NOT IN ('CPC','CPM','CPV') AND @ProductUnitName = 'CPM') THEN SUM(TongViewThucChay*@DonGiaSauChietKhau)
								ELSE 0
								END
						 FROM thucchay WHERE HopDongChiTietREF = @HopDongChiTietREF 
                                 AND NgayThucHien < @NgayThucHien
                                 AND NgayThucHien >='2014-01-01'
                                 AND BannerType = @BannerType)
    SET @TienThucChayKM = (SELECT CASE WHEN @DonViTinh = 'CPC' THEN SUM(TongClickThucChay*@DonGiaSauChietKhau)
										    WHEN @DonViTinh = 'CPM' THEN SUM(TongViewThucChay*@DonGiaSauChietKhau)
										    WHEN (@DonViTinh NOT IN ('CPC','CPM','CPV') AND @ProductUnitName = 'CPC') THEN SUM(TongClickThucChay*@DonGiaSauChietKhau)
										    WHEN (@DonViTinh NOT IN ('CPC','CPM','CPV') AND @ProductUnitName = 'CPM') THEN SUM(TongViewThucChay*@DonGiaSauChietKhau)
								ELSE 0
								END
						 FROM thucchay WHERE HopDongChiTietREF = @HopDongChiTietREF 
                                 AND NgayThucHien < @NgayThucHien
                                 AND NgayThucHien >='2014-01-01'
                                 AND BannerType = @BannerType)
                                 
	SET @TienThucChay2013 = (SELECT SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)
	                         FROM ThucChayDaTinh tcdt 
	                         WHERE YEAR(NgayThucHien) = 2013 AND HopDongChiTietREF = @HopDongChiTietREF)							
	SET @TienThucChayKM2013 = (SELECT SUM(tcdt.ThanhTienKM)
	                           FROM ThucChayDaTinh tcdt 
	                           WHERE YEAR(NgayThucHien) = 2013 AND HopDongChiTietREF = @HopDongChiTietREF)							
	
	
						

	
	IF @IsKhuyenMai = 1
		BEGIN
			IF (@TienThucChayKM2013 + @TienThucChayKM + @TienThucChayKMNgay > @SoLuong * @DonGia)
				SET 	@TienThucChayKMNgay = 0
			ELSE 
				SET @TienThucChayKMNgay = @TienThucChayKMNgay
		END	
	ELSE 
		BEGIN
			IF (@TienThucChay2013 + @TienThucChay + @TienThucChayNgay > @ThanhTien)
				SET 	@TienThucChayNgay = 0
			ELSE 
				SET @TienThucChayNgay = @TienThucChayNgay
		END	
	INSERT INTO @Table
	SELECT @HopDongChiTietREF,
		@NgayThucHien,
		@IsKhuyenMai,
		@TienThucChayNgay,
		@TienThucChayKMNgay
	
    FETCH NEXT FROM vendor_cursor INTO @SoHopDong,@HopDongChiTietREF,@ProductUnitName,@BannerType
END 
CLOSE vendor_cursor;
DEALLOCATE vendor_cursor;

SELECT a.*, b.* FROM
(
SELECT * FROM @Table
)a 
FULL OUTER JOIN
(
SELECT tcdt.HopDongChiTietREF,tcdt.NgayThucHien, tcdt.IsKhuyenMai,
SUM(tcdt.ThanhTienSauTrietKhauThucChay+GiaTriThayDoi)TCDT, 
SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi)TCDTKKM
FROM ThucChayDaTinh tcdt 
WHERE tcdt.NgayThucHien = @NgayThucHien
GROUP BY tcdt.HopDongChiTietREF, tcdt.NgayThucHien, tcdt.IsKhuyenMai
)b	
ON a.HopDongChiTietREF = b.HopDongChiTietREF
AND a.NgayThucHien = a.NgayThucHien
WHERE a.IsKhuyenMai <> b.IsKhuyenMai OR a.TienThucChayNgay <> b.TCDT OR a.TienThucChayKMNgay <> b.TCDTKKM
END

```
