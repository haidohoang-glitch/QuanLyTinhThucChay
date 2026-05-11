# Stored Procedure: `BPTC_Get_ThongTinBCWebsite`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:51.747000
- **Ngày sửa cuối**: 2015-06-11 18:17:51.747000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |
| `@Website` | `nvarchar(510)` | No |

## Definition (Source Code)

```sql

CREATE PROC [dbo].[BPTC_Get_ThongTinBCWebsite]
    (
      @FromDate DATETIME ,
      @ToDate DATETIME ,
      @Website NVARCHAR(255)
    )
AS 
    BEGIN
        
        CREATE TABLE #WebsitePrams ( WebsiteID INT )
        DECLARE @DelimitedString NVARCHAR(255)
        DECLARE @Delimiter VARCHAR(100) 
        DECLARE @Index SMALLINT ,
            @Start SMALLINT ,
            @DelSize SMALLINT
        
        SET @Delimiter = ','
        SET @DelSize = LEN(@Delimiter)
        SET @DelimitedString = @Website
        
        WHILE LEN(@DelimitedString) > 0 
            BEGIN
                SET @Index = CHARINDEX(@Delimiter, @DelimitedString)
                IF @Index = 0 
                    BEGIN
                        INSERT  INTO #WebsitePrams
                                ( WebsiteID 
                                )
                        VALUES  ( CONVERT(INT, LTRIM(RTRIM(@DelimitedString))) 
                                )
                        BREAK
                    END
                ELSE 
                    BEGIN

                        INSERT  INTO #WebsitePrams
                                ( WebsiteID 
                                )
                        VALUES  ( CONVERT(INT, LTRIM(RTRIM(SUBSTRING(@DelimitedString,
                                                              1, @Index - 1))))
                                )
                        SET @Start = @Index + @DelSize
                        SET @DelimitedString = SUBSTRING(@DelimitedString,
                                                         @Start,
                                                         LEN(@DelimitedString)
                                                         - @Start + 1)
                    END
            END                       
        
        DECLARE @colSP NVARCHAR(MAX) ,
            @query NVARCHAR(MAX)
        SET @colSP = ''               

        SELECT  @colSP = STUFF(
           (SELECT  ',' + QUOTENAME(A.TenNhomSanPhamBaoCao)
            FROM    ( SELECT    TenNhomSanPhamBaoCao
                      FROM      dbo.DmNhomSanPhamBaoCao
                    ) AS A
            GROUP BY A.TenNhomSanPhamBaoCao
            ORDER BY A.TenNhomSanPhamBaoCao
                FOR            XML PATH('') ,
                                   TYPE
           ).value('.', 'NVARCHAR(MAX)'), 1, 1, '')

        SET @colSP = @colSP + ',' + '[SanPhamKhac]'
        PRINT @colSP
        
        SELECT  *
        INTO    #New
        FROM    ( SELECT    bc.TenNhomSanPhamBaoCao ,
                            A.DmWebsiteREF ,
                            A.TenWebsite ,
                            SUM(A.ThanhTienThucChay) ThanhTienThucChay                            
                  FROM      ( SELECT    SUM(tcdt.ThanhTienSauTrietKhauThucChay
                                            + tcdt.GiaTriThayDoi) ThanhTienThucChay ,
                                        tcdt.DmSanPhamREF ,
                                        tcdt.DmWebsiteREF ,
                                        tcdt.TenWebsite
                              FROM      ThucChayDaTinh tcdt
                              WHERE     tcdt.NgayThucHien BETWEEN @FromDate AND @ToDate
                              GROUP BY  tcdt.DmSanPhamREF ,
                                        tcdt.DmWebsiteREF ,
                                        tcdt.TenWebsite
                            ) A
                            INNER JOIN dbo.DmNhomSanPhamBaoCao bc ON A.DmSanPhamREF = bc.DmSanPhamREF
                  GROUP BY  bc.DmNhomSanPhamBaoCaoID ,
                            bc.TenNhomSanPhamBaoCao ,
                            A.DmWebsiteREF ,
                            A.TenWebsite
                  UNION
                  SELECT    'SanPhamKhac' TenNhomSanPhamBaoCao ,
                            A.DmWebsiteREF ,
                            A.TenWebsite ,
                            SUM(A.ThanhTienThucChay) ThanhTienThucChay
                  FROM      ( SELECT    SUM(tcdt.ThanhTienSauTrietKhauThucChay
                                            + tcdt.GiaTriThayDoi) ThanhTienThucChay ,
                                        tcdt.DmSanPhamREF ,
                                        tcdt.DmWebsiteREF ,
                                        tcdt.TenWebsite
                              FROM      ThucChayDaTinh tcdt
                              WHERE     tcdt.NgayThucHien BETWEEN @FromDate AND @ToDate
                              GROUP BY  tcdt.DmSanPhamREF ,
                                        tcdt.DmWebsiteREF ,
                                        tcdt.TenWebsite
                            ) A
                  WHERE     A.DmSanPhamREF NOT IN (
                            SELECT  bc.DmSanPhamREF
                            FROM    dbo.DmNhomSanPhamBaoCao bc )
                  GROUP BY  A.DmWebsiteREF ,
                            A.TenWebsite
                ) A
        WHERE   A.ThanhTienThucChay <> 0
                AND ( A.DmWebsiteREF IN ( SELECT    WebsiteID
                                          FROM      #WebsitePrams )
                      OR @Website = ''
                    )
        
        SET @query = '
SELECT A.* FROM
(
	Select A.*
	FROM #New PIVOT (SUM(ThanhTienThucChay) FOR TenNhomSanPhamBaoCao IN ('
            + @colSP + ')) A  
)A Order By TenWebsite'
        EXEC sp_executesql @query
        DROP TABLE #New
        DROP TABLE #WebsitePrams
        
        DECLARE @FooterText NVARCHAR(255)
        DECLARE @HeaderText NVARCHAR(255)
        
        SET  @FooterText = N'# Dữ liệu cập nhật ngày ' + CONVERT(NVARCHAR(10), GETDATE() , 103) + ' (có VAT)'                
        SET  @HeaderText = N'Financial Department, ' + CONVERT(NVARCHAR(10), GETDATE(), 113)
        
        SELECT @FooterText FooterText,@HeaderText HeaderText        
        
    END


```
