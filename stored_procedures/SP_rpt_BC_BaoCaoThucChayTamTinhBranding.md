# Stored Procedure: `rpt_BC_BaoCaoThucChayTamTinhBranding`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-09-08 14:02:05.390000
- **Ngày sửa cuối**: 2022-09-08 14:45:23.453000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `nvarchar(200)` | No |
| `@PageIndex` | `int(4)` | No |
| `@PageSize` | `int(4)` | No |
| `@TotalRows` | `int(4)` | Yes |

## Definition (Source Code)

```sql

/*
	DECLARE @TotalRows INT;
EXEC [dbo].[rpt_BC_BaoCaoThucChayTamTinhBranding] @NgayThucHien = N'2022-03-01/2022-8-31',           -- nvarchar(100)
                                                  @PageIndex = 1,                -- int
                                                  @PageSize = 10000,                 -- int
                                                  @TotalRows = @TotalRows OUTPUT -- int

*/

CREATE PROCEDURE [dbo].[rpt_BC_BaoCaoThucChayTamTinhBranding]
--DECLARE
    @NgayThucHien NVARCHAR(100) ='2022-08-26/2022-08-28',
    @PageIndex INT=1,
    @PageSize INT=2000000,
    @TotalRows INT OUT
AS
BEGIN
	DECLARE @FromDate DATETIME;
    DECLARE @ToDate DATETIME;
    IF ISNULL(@NgayThucHien, '') = ''
    BEGIN
        SET @FromDate = CONVERT(DATE, CONVERT(NVARCHAR(10), YEAR(GETDATE())) + '-01-01');
        SET @ToDate = CONVERT(DATE, CONVERT(NVARCHAR(50), GETDATE(), 20));
    END;
    ELSE
    BEGIN
        SET @FromDate = CONVERT(DATE, SUBSTRING(@NgayThucHien, 0, 11));
        SET @ToDate = CONVERT(DATE, SUBSTRING(@NgayThucHien, 12, 11));
    END;
    PRINT 1;

    DECLARE @FromIndex INT,
            @ToIndex INT,
            @SQL NVARCHAR(MAX),
            @Fillter NVARCHAR(MAX);

	SET @Fillter = N'1=1';
    SET @FromIndex = (@PageIndex - 1) * @PageSize + 1;
    SET @ToIndex = (@PageIndex * @PageSize);


	SELECT DmHinhThucQuangCao, TenHinhThucQuangCao, DmSanPhamREF, TenSanPham, SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS TienThucChay 
	INTO #KQ
	FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh 
	WHERE NgayThucHien BETWEEN @FromDate AND @ToDate 
	AND DmMaHopDongREF NOT IN (310,5153,345,5151,5152)
	AND DmHinhThucQuangCao IN (5, 53, 5001, 5006, 52,42)
	AND DmSanPhamREF NOT IN (585)
	GROUP BY TenHinhThucQuangCao, DmSanPhamREF, TenSanPham,DmHinhThucQuangCao


	DECLARE @SQL_TotalRows NVARCHAR(MAX), @SQL_TotalRowPara NVARCHAR(MAX), @v_TotalRow FLOAT;

		SET @SQL = N'SELECT * FROM (SELECT ROW_NUMBER() OVER ( ORDER BY A.TenSanPham ) AS STT, * FROM #KQ A  WHERE ' + @Fillter + N') B WHERE STT BETWEEN '
			+ CONVERT(NVARCHAR(10), @FromIndex) + N' AND ' + CONVERT(NVARCHAR(10), @ToIndex) + N' ORDER BY b.TenHinhThucQuangCao' + N'';

			--SELECT * FROM (SELECT ROW_NUMBER() OVER ( ORDER BY A.TenSanPham ) AS STT, * FROM #KQ A  WHERE 1=1) B WHERE STT BETWEEN 1 AND 10000 ORDER BY b.DmHinhThucQuangCao

	PRINT @SQL;
	EXECUTE (@SQL);



	SET @SQL_TotalRowPara = N'@v_TotalRow bigint output ';
	SET @SQL_TotalRows = N'SELECT @v_TotalRow=  
     COUNT(*) FROM   
    #KQ A WHERE ' + @Fillter + N'';

	EXECUTE sp_executesql @SQL_TotalRows, @SQL_TotalRowPara, @v_TotalRow = @TotalRows OUTPUT;

END

```
