# Stored Procedure: `BPTC_Report_BCKD_GetAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:50.637000
- **Ngày sửa cuối**: 2015-06-11 18:17:50.637000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenBaoCao` | `nvarchar(510)` | No |
| `@TrangThaiPheDuyet` | `int(4)` | No |
| `@LoaiBaoCao` | `int(4)` | No |
| `@PageNumber` | `int(4)` | No |
| `@RowspPage` | `int(4)` | No |
| `@NguoiLap` | `nvarchar(200)` | No |

## Definition (Source Code)

```sql

CREATE PROC [dbo].[BPTC_Report_BCKD_GetAll]
    (
      @TenBaoCao NVARCHAR(255) ,
      @TrangThaiPheDuyet INT ,
      @LoaiBaoCao INT ,
      @PageNumber INT ,
      @RowspPage INT ,
      @NguoiLap NVARCHAR(100)
    )
AS 
    BEGIN        
    
        SELECT  RowNumber ,
                BPTC_ThongTinBCKDID AS ThongTinBCKDID ,
                TrangThaiPheDuyet ,
                ThoiGianKetThuc ,
                ThoiGianBatDau ,
                TenLoaiBaoCaoKinhDoanh ,
                TenBaoCaoKinhDoanh ,
                NguoiPheDuyet ,
                NguoiLap ,
                NgayPheDuyet ,
                NgayLap ,
                LoaiBaoCaoKinhDoanh ,
                CreatedBy ,
                CreatedAt ,
                LastModifiedBy ,
                LastModifiedAt
        FROM    ( SELECT  ROW_NUMBER() OVER ( ORDER BY NgayLap DESC ) AS RowNumber ,
                            dbo.BPTC_ThongTinBCKD.*
                  FROM      dbo.BPTC_ThongTinBCKD
                  WHERE     ( TrangThaiPheDuyet = @TrangThaiPheDuyet
                              OR @TrangThaiPheDuyet < 0
                            )
                            AND ( TenBaoCaoKinhDoanh LIKE N'%' + @TenBaoCao
                                  + '%'
                                  OR @TenBaoCao = ''
                                )
                            AND ( LoaiBaoCaoKinhDoanh = @LoaiBaoCao
                                  OR @LoaiBaoCao < 0
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
        FROM    dbo.BPTC_ThongTinBCKD
        WHERE   ( TrangThaiPheDuyet = @TrangThaiPheDuyet
                  OR @TrangThaiPheDuyet < 0
                )
                AND ( TenBaoCaoKinhDoanh LIKE N'%' + @TenBaoCao + '%'
                      OR @TenBaoCao = ''
                    )
                AND ( LoaiBaoCaoKinhDoanh = @LoaiBaoCao
                      OR @LoaiBaoCao < 0
                    )
				AND DeleteStatus = 0
                AND ( NguoiLap = @NguoiLap
                      OR @NguoiLap = ''
                    )                    
        
    END

```
