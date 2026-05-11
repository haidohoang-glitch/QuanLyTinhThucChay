# Stored Procedure: `prc_asd_Check_DuLieuDauVaoSanPham_Get`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-05-09 15:14:28.193000
- **Ngày sửa cuối**: 2017-05-09 15:16:38.123000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@pageIndex` | `int(4)` | No |
| `@pageSize` | `int(4)` | No |
| `@fromDate` | `datetime(8)` | No |
| `@toDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql

-- PROCEDURE [dbo].[sp_asd_Check_DuLieuDauVaoSanPham_Get]
CREATE PROCEDURE [dbo].[prc_asd_Check_DuLieuDauVaoSanPham_Get]
	@pageIndex INT = 1,
	@pageSize INT = 10,
    @fromDate DATETIME ,
    @toDate DATETIME
AS
    BEGIN
		WITH _source AS (
        SELECT DISTINCT
                dsp.TenSanPham,
                ST2.LyDo,
                ST2.NgayThucHien,
				ST2.DmSanPhamREF, SUBSTRING(( SELECT  ',{"s": "'
                                    + CONVERT(VARCHAR(15), ST1.SoHopDong)
                                    + '", "h": ' + ISNULL('"'
                                                              + CONVERT(VARCHAR(100), ST1.HopDongChiTietREF)
                                                              + '"', 'null')
                                    + ', "b": ' + ISNULL('"'
                                                              + CONVERT(VARCHAR(100), ST1.HopDongChiTietREF)
                                                              + '"', 'null')
                                    + '}' AS [text()]
                            FROM    dbo.Check_DuLieuDauVaoSanPham ST1
                            WHERE   ST1.DmSanPhamREF = ST2.DmSanPhamREF
                                    AND ST1.LyDo = ST2.LyDo
                                    AND ST1.NgayThucHien = ST2.NgayThucHien
                          FOR
                            XML PATH('')
                          ), 2, 8000) [ChiTiet]
        FROM    dbo.Check_DuLieuDauVaoSanPham ST2
                LEFT JOIN dbo.DmSanPham dsp ON ST2.DmSanPhamREF = dsp.DmSanPhamID
		WHERE CONVERT(DATE, st2.NgayThucHien) BETWEEN CONVERT(DATE, @fromDate) AND CONVERT(DATE, @toDate)
    ),
	_s2 AS (
	SELECT *,
		ROW_NUMBER() OVER (ORDER BY NgayThucHien) stt,
		(SELECT COUNT(*) FROM _source) Total
		FROM _source
	)
	SELECT * 
	FROM _s2
	WHERE stt BETWEEN (@pageIndex - 1) * @pageSize AND @pageIndex * @pageSize;

    END
```
