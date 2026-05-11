# Stored Procedure: `prc_asd_KSTC_GET_CHECK_OUTPUT_CONTRACT`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-04-14 10:11:59.227000
- **Ngày sửa cuối**: 2017-05-09 15:45:52.447000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HTQC` | `varchar(20)` | No |
| `@SoHD` | `varchar(200)` | No |
| `@SanPham` | `varchar(200)` | No |
| `@LoaiBanner` | `varchar(200)` | No |
| `@VanDe` | `varchar(200)` | No |
| `@TrangThaiXuLy` | `int(4)` | No |
| `@pageIndex` | `int(4)` | No |
| `@pageSize` | `int(4)` | No |

## Definition (Source Code)

```sql
/****** Script for SelectTopNRows command from SSMS  ******/

-- dbo.prc_asd_KSTC_GET_CHECK_OUTPUT_CONTRACT @pageIndex = 1, @soHD='QC2820115',@pageSize = 100

CREATE PROCEDURE [dbo].[prc_asd_KSTC_GET_CHECK_OUTPUT_CONTRACT]
    @NgayThucHien DATETIME = NULL ,
    @HTQC VARCHAR(20) = '' ,
    @SoHD VARCHAR(200) = '' ,
    @SanPham VARCHAR(200) = '' ,
    @LoaiBanner VARCHAR(200) = '' ,
    @VanDe VARCHAR(200) = '' ,
    @TrangThaiXuLy INT = -1 ,
    @pageIndex INT = 1 ,
    @pageSize INT = 10
AS
    BEGIN
        DECLARE @total INT;
        SET @total = ( SELECT   COUNT(1)
                       FROM     [ABM_Data_ThucChay].[dbo].[Check_ThongTinDauRaSanPham] c
                                LEFT JOIN dbo.DmSanPham s ON c.DmSanPhamREF = s.DmSanPhamID
                                LEFT JOIN dbo.HopDong h ON c.HopDongID = h.HopDongID
                                LEFT JOIN dbo.HopDongChiTiet hc ON c.HopDongChiTietID = hc.HopDongChiTietID
                                LEFT JOIN dbo.DmLoaiBanner db ON hc.DmLoaiBannerREF = db.DmLoaiBannerID
								LEFT JOIN dbo.DmHinhThucQuangCao hq ON hc.DmLoaiREF = hq.DmHinhThucQuangCaoID
                       WHERE    ( @NgayThucHien IS NULL
                                  OR CONVERT(DATE, c.NgayThucHien) = CONVERT(DATE, @NgayThucHien)
                                )
                                AND ( @SoHD = ''
                                      OR c.SoHopDong IN (
                                      SELECT    *
                                      FROM      [dbo].[fnSplitString](@SoHD,
                                                              ',') )
                                    )
                                AND ( @HTQC = ''
                                      OR hc.DmLoaiREF IN (
                                      SELECT    *
                                      FROM      [dbo].[fnSplitString](@HTQC,
                                                              ',') )
                                    )
                                AND ( @SanPham = ''
                                      OR CONVERT(VARCHAR(10), c.DmSanPhamREF) IN (
                                      SELECT    *
                                      FROM      [dbo].[fnSplitString](@SanPham,
                                                              ',') )
                                    )
                                AND ( @LoaiBanner = ''
                                      OR CONVERT(VARCHAR(10), hc.DmLoaiBannerREF) IN (
                                      SELECT    *
                                      FROM      [dbo].[fnSplitString](@LoaiBanner,
                                                              ',') )
                                    )
                                AND ( @TrangThaiXuLy = -1
                                      OR c.TrangThaiXuLy = @TrangThaiXuLy
                                    )
                                AND ( @VanDe = ''
                                      OR CONVERT(VARCHAR(10), c.IDLyDo) IN (
                                      SELECT    *
                                      FROM      [dbo].[fnSplitString](@VanDe,
                                                              ',') )
                                    )
                     );
		
        WITH    _source
                  AS ( SELECT   c.*, 
								CASE [c].[TrangThaiXuLy]
                                  WHEN 0 THEN N'Chưa xử lý'
                                  WHEN 1 THEN N'Đã xử lý'
                                END [TenTrangThaiXuLy] ,
                                CASE h.TrangThaiHopDong
                                  WHEN 1 THEN N'Bình thường'
                                  WHEN 2 THEN N'Thay đổi'
                                  WHEN 3 THEN N'Hủy'
                                END TrangThaiHopDong ,
                                s.[TenSanPham] TenSanPhamRef,
                                db.TenLoaiBanner ,
                                [NgayThucHien] NgayPhatSinh ,
								hq.TenHinhThucQuangCao HTQC,
								c.ThanhTienHD * 80 / 100 GiaTriThucChayTong,
                                ROW_NUMBER() OVER ( ORDER BY c.NgayThucHien DESC ) stt ,
                                @total Total
                       FROM     [ABM_Data_ThucChay].[dbo].[Check_ThongTinDauRaSanPham] c
                                LEFT JOIN dbo.DmSanPham s ON c.DmSanPhamREF = s.DmSanPhamID
                                LEFT JOIN dbo.HopDong h ON c.HopDongID = h.HopDongID
                                LEFT JOIN dbo.HopDongChiTiet hc ON c.HopDongChiTietID = hc.HopDongChiTietID
                                LEFT JOIN dbo.DmLoaiBanner db ON hc.DmLoaiBannerREF = db.DmLoaiBannerID
								LEFT JOIN dbo.DmHinhThucQuangCao hq ON hc.DmLoaiREF = hq.DmHinhThucQuangCaoID
                       WHERE    ( @NgayThucHien IS NULL
                                  OR CONVERT(DATE, c.NgayThucHien) = CONVERT(DATE, @NgayThucHien)
                                )
                                AND ( @SoHD = ''
                                      OR c.SoHopDong IN (
                                      SELECT    *
                                      FROM      [dbo].[fnSplitString](@SoHD,
                                                              ',') )
                                    )
                                AND ( @HTQC = ''
                                      OR hc.DmLoaiREF IN (
                                      SELECT    *
                                      FROM      [dbo].[fnSplitString](@HTQC,
                                                              ',') )
                                    )
                                AND ( @SanPham = ''
                                      OR CONVERT(VARCHAR(10), c.DmSanPhamREF) IN (
                                      SELECT    *
                                      FROM      [dbo].[fnSplitString](@SanPham,
                                                              ',') )
                                    )
                                AND ( @LoaiBanner = ''
                                      OR CONVERT(VARCHAR(10), hc.DmLoaiBannerREF) IN (
                                      SELECT    *
                                      FROM      [dbo].[fnSplitString](@LoaiBanner,
                                                              ',') )
                                    )
                                AND ( @TrangThaiXuLy = -1
                                      OR c.TrangThaiXuLy = @TrangThaiXuLy
                                    )
                                AND ( @VanDe = ''
                                      OR CONVERT(VARCHAR(10), c.IDLyDo) IN (
                                      SELECT    *
                                      FROM      [dbo].[fnSplitString](@VanDe,
                                                              ',') )
                                    )
                     )
            SELECT  *
            FROM    _source
            WHERE   stt BETWEEN ( @pageIndex - 1 ) * @pageSize + 1
                        AND     @pageIndex * @pageSize;
    END;


```
