# Stored Procedure: `BPTC_Search_ThongTinBCSP`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:50.157000
- **Ngày sửa cuối**: 2015-06-11 18:17:50.157000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenBaoCao` | `nvarchar(510)` | No |
| `@TrangThaiPheDuyet` | `int(4)` | No |
| `@NhomSanPhamBaoCaoID` | `int(4)` | No |
| `@PageNumber` | `int(4)` | No |
| `@RowspPage` | `int(4)` | No |
| `@NguoiLap` | `nvarchar(200)` | No |

## Definition (Source Code)

```sql

CREATE PROC [dbo].[BPTC_Search_ThongTinBCSP]
    (
      @TenBaoCao NVARCHAR(255) ,
      @TrangThaiPheDuyet INT ,
      @NhomSanPhamBaoCaoID INT ,
      @PageNumber INT ,
      @RowspPage INT ,
      @NguoiLap NVARCHAR(100)
    )
AS 
    BEGIN        
    
        SELECT  RowNumber ,
                BPTC_BaoCaoTTSanPhamThangID AS BaoCaoTTSanPhamThangID ,
                TenBaoCao ,
                NhomSanPhamBaoCaoID ,
                TenNhomSanPhamBaoCao ,
                TrangThaiPheDuyet ,
                ThoiGianKetThuc ,
                ThoiGianBatDau ,
                NguoiPheDuyet ,
                NguoiLap ,
                NgayPheDuyet ,
                NgayLap ,
                CreatedBy ,
                CreatedAt ,
                LastModifiedBy ,
                LastModifiedAt
        FROM    ( SELECT    ROW_NUMBER() OVER ( ORDER BY BPTC_BaoCaoTTSanPhamThangID ) AS RowNumber ,
                            ttsp.*
                  FROM      dbo.BPTC_BaoCaoTTSanPhamThang ttsp
                  WHERE     ( TrangThaiPheDuyet = @TrangThaiPheDuyet
                              OR @TrangThaiPheDuyet < 0
                            )
                            AND ( TenBaoCao LIKE N'%' + @TenBaoCao + '%'
                                  OR @TenBaoCao = ''
                                )
                            AND ( NhomSanPhamBaoCaoID = @NhomSanPhamBaoCaoID
                                  OR @NhomSanPhamBaoCaoID < 0
                                )
                            AND DeleteStatus = 0
                            AND ( NguoiLap = @NguoiLap
                                  OR @NguoiLap = ''
                                )
                ) AS TBL
        WHERE   RowNumber BETWEEN ( ( @PageNumber - 1 ) * @RowspPage + 1 )
                          AND     ( @PageNumber * @RowspPage )
        ORDER BY TBL.NgayLap DESC 
        
        SELECT  COUNT(*) AS TotalRows
        FROM    dbo.BPTC_BaoCaoTTSanPhamThang
        WHERE   ( TrangThaiPheDuyet = @TrangThaiPheDuyet
                  OR @TrangThaiPheDuyet < 0
                )
                AND ( TenBaoCao LIKE N'%' + @TenBaoCao + '%'
                      OR @TenBaoCao = ''
                    )
                AND ( NhomSanPhamBaoCaoID = @NhomSanPhamBaoCaoID
                      OR @NhomSanPhamBaoCaoID < 0
                    )
        
    END

```
