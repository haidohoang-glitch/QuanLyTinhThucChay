# Stored Procedure: `sp_get_VanDeDauRaThucChay_TongHop`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-08-22 14:28:55.393000
- **Ngày sửa cuối**: 2017-09-11 15:01:15.407000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmNhomSanPham` | `int(4)` | No |
| `@HopDongID` | `int(4)` | No |
| `@DmHinhThucQuangCaoREF` | `int(4)` | No |
| `@VanDe` | `int(4)` | No |
| `@TinhTrangXuLy` | `int(4)` | No |
| `@PageIndex` | `int(4)` | No |
| `@PageSize` | `int(4)` | No |
| `@TotalRows` | `int(4)` | Yes |

## Definition (Source Code)

```sql
--sp_get_VanDeDauRaThucChay_TongHop '1900-01-01',-1,-1,-1,-1,-1,1,5,10 
CREATE PROCEDURE [dbo].[sp_get_VanDeDauRaThucChay_TongHop]
    @NgayThucHien DATETIME = '1900-01-01' ,
    @DmNhomSanPham INT = -1 ,
    @HopDongID INT = -1 ,
    @DmHinhThucQuangCaoREF INT = -1 ,
    @VanDe INT = -1 ,
    @TinhTrangXuLy INT = -1 ,
    @PageIndex INT = 1 ,
    @PageSize INT = 5 ,
    @TotalRows INT OUTPUT
AS
    BEGIN
	SET @DmNhomSanPham = ISNULL(@DmNhomSanPham,-1)
	SET @HopDongID = ISNULL(@HopDongID,-1)
	SET @DmHinhThucQuangCaoREF = ISNULL(@DmHinhThucQuangCaoREF,-1)
	SET @VanDe = ISNULL(@VanDe,-1)
	SET @TinhTrangXuLy = ISNULL(@TinhTrangXuLy,-1)
	--IF @NgayThucHien = '1900-01-01' SET @NgayThucHien = GETDATE()

	--SELECT @DmNhomSanPham,@HopDongID,@DmHinhThucQuangCaoREF,@VanDe,@TinhTrangXuLy
        SELECT  ROW_NUMBER() OVER ( ORDER BY A.IDNhomSanPham, A.HopDongID, A.DmSanPhamREF ) AS STT ,
                *
        INTO    #Temp
        FROM    ( SELECT DISTINCT
                            [NgayThucHien] ,
                            [HopDongID] ,
                            [SoHopDong] ,
                            [HopDongChiTietREF] ,
                            [DmSanPhamREF] ,
                            [TenSanPham] ,
                            [DmHinhThucQuangCaoREF] ,
                            A.TrangThaiXuLy ,							
                            B.IDNhomSanPham ,
                            B.NhomSanPham,
							c.TenHinhThucQuangCao
                  FROM      [ABM_Data_ThucChay].[dbo].[KiemSoatDauRaThucChay_ChiTiet] A
                            INNER JOIN dbo.KiemSoatThucChay_DanhSachLoi B ON A.IDLoi = B.ID
							LEFT JOIN dbo.DmHinhThucQuangCao c ON a.DmHinhThucQuangCaoREF = c.DmHinhThucQuangCaoID
                  WHERE     (@NgayThucHien='1900-01-01' OR NgayThucHien = @NgayThucHien)
                            AND @HopDongID = CASE WHEN @HopDongID = -1 THEN -1
                                                  ELSE A.HopDongID
                                             END
                            AND @DmNhomSanPham = CASE WHEN @DmNhomSanPham = -1
                                                      THEN -1
                                                      ELSE B.IDNhomSanPham
                                                 END
                            AND @DmHinhThucQuangCaoREF = CASE WHEN @DmHinhThucQuangCaoREF = -1
                                                              THEN -1
                                                              ELSE A.DmHinhThucQuangCaoREF
                                                         END
                            AND @VanDe = CASE WHEN @VanDe = -1 THEN -1
                                              ELSE A.IDLoi
                                         END
                            AND @TinhTrangXuLy = CASE WHEN @TinhTrangXuLy = -1
                                                      THEN -1
                                                      ELSE A.TrangThaiXuLy
                                                 END
                ) A;

        SELECT  @TotalRows = MAX(STT)
        FROM    #Temp;

        SELECT  a.*, @TotalRows Total
        FROM    #Temp A
        WHERE   A.STT BETWEEN ( ( @PageIndex - 1 ) * @PageSize + 1 )
                      AND     ( @PageIndex * @PageSize );

    END;
                             
```
