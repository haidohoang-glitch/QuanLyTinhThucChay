# Stored Procedure: `BPTC_Get_ThongTinBCKD_XuatHoaDon`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:51.907000
- **Ngày sửa cuối**: 2015-06-11 18:17:51.907000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `datetime(8)` | No |
| `@NgayKetThuc` | `datetime(8)` | No |
| `@ThongTinBCKDID` | `int(4)` | No |
| `@TenBaoCao` | `nvarchar(200)` | No |

## Definition (Source Code)

```sql

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[BPTC_Get_ThongTinBCKD_XuatHoaDon]		
		@NgayBatDau       DATETIME,
		@NgayKetThuc       DATETIME,
        @ThongTinBCKDID  INT,
        @TenBaoCao       NVARCHAR(100)
AS
BEGIN
	
DECLARE @NamXuatHD INT = YEAR(@NgayKetThuc)		
	
SELECT A.HopDong,
       SUM(A.XuatHD2014) AS XuatHDNamTruoc,
       SUM(A.XuatHD2015) XuatHDNamHienTai,
       (
           CASE 
                WHEN (@NamXuatHD -A.HopDong) = 2 THEN 0
                ELSE SUM(A.DsHaiDau)
           END
       ) AS DsHaiDau,
       (
           CASE 
                WHEN (@NamXuatHD -A.HopDong) = 2 THEN 0
                ELSE (SUM(A.XuatHD2014) + SUM(A.XuatHD2015)) / SUM(A.DsHaiDau)
           END
       ) AS 'XHD/HD',
       (
           CASE 
                WHEN (@NamXuatHD -A.HopDong) = 2 THEN 0
                ELSE SUM(A.DsHaiDau) -(SUM(A.XuatHD2014) + SUM(A.XuatHD2015))
           END
       ) AS ChuaXuat
       INTO #HD2013
FROM   (
           SELECT @NamXuatHD -2 HopDong,
                  ISNULL(
                      (
                          CASE 
                               WHEN YEAR(tthd.NgayXuatHoaDon) = @NamXuatHD -1
                          AND YEAR(hd.NgayDanhSoHopDong) = @NamXuatHD -2 THEN 
                              SUM(tthd.GiaTri) 
                              END
                      ),
                      0
                  ) XuatHD2014,
                  ISNULL(
                      (
                          CASE 
                               WHEN YEAR(tthd.NgayXuatHoaDon) = @NamXuatHD
                          AND YEAR(hd.NgayDanhSoHopDong) = @NamXuatHD -2 THEN 
                              SUM(tthd.GiaTri) 
                              END
                      ),
                      0
                  ) XuatHD2015,
                  0 AS DsHaiDau
           FROM   ThongTinHoaDon tthd
                  INNER JOIN HopDong hd
                       ON  tthd.HopDongREF = hd.HopDongID
           WHERE  hd.DeletedStatus = 0
                  AND hd.TrangThaiHopDong <> 3
                  AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
                  AND tthd.DeletedStatus=0
           GROUP BY
                  YEAR(tthd.NgayXuatHoaDon),
                  YEAR(hd.NgayDanhSoHopDong)
           UNION ALL
           SELECT YEAR(hd.NgayDanhSoHopDong),
                  0,
                  0,
                  SUM(hdct.ThanhTien) * 1.1
           FROM   HopDong hd
                  INNER JOIN HopDongChiTiet hdct
                       ON  hd.HopDongID = hdct.HopDongFK
           WHERE  YEAR(hd.NgayDanhSoHopDong) = @NamXuatHD -2
                  AND hd.DeletedStatus = 0
                  AND hd.TrangThaiHopDong <> 3
                  AND hdct.DeletedStatus = 0
                  AND hd.IsBanCung = 1
                  AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
           GROUP BY
                  YEAR(hd.NgayDanhSoHopDong)
       ) A
GROUP BY
       A.HopDong

SELECT A.HopDong,
       SUM(A.XuatHD2014) AS XuatHD2014,
       SUM(A.XuatHD2015) XuatHD2015,
       SUM(A.DsHaiDau) AS DsHaiDau,
       (SUM(A.XuatHD2014) + SUM(A.XuatHD2015)) / SUM(A.DsHaiDau) AS 'XHD/HD',
       SUM(A.DsHaiDau) -(SUM(A.XuatHD2014) + SUM(A.XuatHD2015)) AS ChuaXuat
       INTO #HD2014
FROM   (
           SELECT @NamXuatHD -1 HopDong,
                  ISNULL(
                      (
                          CASE 
                               WHEN YEAR(tthd.NgayXuatHoaDon) = @NamXuatHD -1
                          AND YEAR(hd.NgayDanhSoHopDong) = @NamXuatHD -1 THEN 
                              SUM(tthd.GiaTri) 
                              END
                      ),
                      0
                  ) XuatHD2014,
                  ISNULL(
                      (
                          CASE 
                               WHEN YEAR(tthd.NgayXuatHoaDon) = @NamXuatHD
                          AND YEAR(hd.NgayDanhSoHopDong) = @NamXuatHD -1 THEN 
                              SUM(tthd.GiaTri) 
                              END
                      ),
                      0
                  ) XuatHD2015,
                  0 AS DsHaiDau
           FROM   ThongTinHoaDon tthd
                  INNER JOIN HopDong hd
                       ON  tthd.HopDongREF = hd.HopDongID
           WHERE  hd.DeletedStatus = 0
                  AND hd.TrangThaiHopDong <> 3
                  AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
                  AND tthd.DeletedStatus=0
           GROUP BY
                  YEAR(tthd.NgayXuatHoaDon),
                  YEAR(hd.NgayDanhSoHopDong)
           UNION ALL
           SELECT YEAR(hd.NgayDanhSoHopDong),
                  0,
                  0,
                  SUM(hdct.ThanhTien) * 1.1
           FROM   HopDong hd
                  INNER JOIN HopDongChiTiet hdct
                       ON  hd.HopDongID = hdct.HopDongFK
           WHERE  YEAR(hd.NgayDanhSoHopDong) = @NamXuatHD -1
                  AND hd.DeletedStatus = 0
                  AND hd.TrangThaiHopDong <> 3
                  AND hdct.DeletedStatus = 0
                  AND hd.IsBanCung = 1
                  AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
           GROUP BY
                  YEAR(hd.NgayDanhSoHopDong)
       ) A
GROUP BY
       A.HopDong


SELECT A.HopDong,
       SUM(A.XuatHD2014) AS XuatHD2014,
       SUM(A.XuatHD2015) XuatHD2015,
       SUM(A.DsHaiDau) AS DsHaiDau,
       (SUM(A.XuatHD2014) + SUM(A.XuatHD2015)) / SUM(A.DsHaiDau) AS 'XHD/HD',
       SUM(A.DsHaiDau) -(SUM(A.XuatHD2014) + SUM(A.XuatHD2015)) AS ChuaXuat
       INTO #HD2015
FROM   (
           SELECT @NamXuatHD HopDong,
                  ISNULL(
                      (
                          CASE 
                               WHEN YEAR(tthd.NgayXuatHoaDon) = @NamXuatHD -1
                          AND YEAR(hd.NgayDanhSoHopDong) = @NamXuatHD THEN SUM(tthd.GiaTri) 
                              END
                      ),
                      0
                  ) XuatHD2014,
                  ISNULL(
                      (
                          CASE 
                               WHEN YEAR(tthd.NgayXuatHoaDon) = @NamXuatHD
                          AND YEAR(hd.NgayDanhSoHopDong) = @NamXuatHD THEN SUM(tthd.GiaTri) 
                              END
                      ),
                      0
                  ) XuatHD2015,
                  0 AS DsHaiDau
           FROM   ThongTinHoaDon tthd
                  INNER JOIN HopDong hd
                       ON  tthd.HopDongREF = hd.HopDongID
           WHERE  hd.DeletedStatus = 0
                  AND hd.TrangThaiHopDong <> 3
                  and hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
                  AND tthd.DeletedStatus=0
           GROUP BY
                  YEAR(tthd.NgayXuatHoaDon),
                  YEAR(hd.NgayDanhSoHopDong)
           UNION ALL
           SELECT YEAR(hd.NgayDanhSoHopDong),
                  0,
                  0,
                  SUM(hdct.ThanhTien) * 1.1
           FROM   HopDong hd
                  INNER JOIN HopDongChiTiet hdct
                       ON  hd.HopDongID = hdct.HopDongFK
           WHERE  (hd.NgayDanhSoHopDong) BETWEEN @NgayBatDau AND @NgayKetThuc
                  AND hd.DeletedStatus = 0
                  AND hd.TrangThaiHopDong <> 3
                  AND hdct.DeletedStatus = 0
                  AND hd.IsBanCung = 1
                  AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
           GROUP BY
                  YEAR(hd.NgayDanhSoHopDong)
       ) A
GROUP BY
       A.HopDong
       
SELECT A.Thang,
       0 XuatHDNamTruoc,
       SUM(A.XuatHD) AS XuatHDNamHienTai,
       SUM(A.DsHaiDau) DsHaiDau,
       (0 + SUM(A.XuatHD)) / SUM(A.DsHaiDau) AS 'XHD/HD',
       SUM(A.DsHaiDau) -(0 + SUM(A.XuatHD)) AS ChuaXuat INTO #HDThang
FROM   (
           SELECT MONTH(hd.NgayDanhSoHopDong) AS Thang,
                  SUM(tthd.GiaTri) XuatHD,
                  0 DsHaiDau
           FROM   ThongTinHoaDon tthd
                  INNER JOIN HopDong hd
                       ON  tthd.HopDongREF = hd.HopDongID
           WHERE  (tthd.NgayXuatHoaDon) BETWEEN @NgayBatDau AND @NgayKetThuc
                  AND (hd.NgayDanhSoHopDong) BETWEEN @NgayBatDau AND @NgayKetThuc
                  AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
           AND hd.DeletedStatus=0 AND hd.TrangThaiHopDong<>3
           AND tthd.DeletedStatus=0
           GROUP BY
                  MONTH(hd.NgayDanhSoHopDong)
           --ORDER BY MONTH(tthd.NgayXuatHoaDon)
           UNION ALL
           SELECT MONTH(hd.NgayDanhSoHopDong),
                  0,
                  SUM(hdct.ThanhTien) * 1.1
           FROM   HopDong hd
                  INNER JOIN HopDongChiTiet hdct
                       ON  hd.HopDongID = hdct.HopDongFK
           WHERE  (hd.NgayDanhSoHopDong) BETWEEN @NgayBatDau AND @NgayKetThuc
           AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
           AND hd.DeletedStatus=0 AND hd.TrangThaiHopDong<>3
           AND hdct.DeletedStatus=0
           GROUP BY
                  MONTH(hd.NgayDanhSoHopDong)
       )A
GROUP BY
       A.Thang

INSERT INTO BPTC_ThongTinBCKD_XuatHoaDon
  (
    -- BPTC_ThongTinBCKD_XuatHoaDon [int] IDENTITY(1,1) NOT NULL,
    BPTC_ThongTinBCKDREF,
    TenBaoCaoKinhDoanh,
    Nam_HopDong,
    DoanhSoXuatHDNamTruoc,
    DoanhSoXuatHD,
    DoanhSoHaiDau,
    TiLeXuatHD_HD,
    GiaTriChuaXuatHD,
    NoiDungDanhGia,
    CreatedBy,
    CreatedAt,
    LastModifiedBy,
    LastModifiedAt,
    DeleteStatus,
    PrintStatus,
    RecordStatus,
    TTHT
  )
 SELECT  @ThongTinBCKDID,
       @TenBaoCao,C.* FROM (
SELECT 
       B.HopDong,
       SUM(B.XuatHDNamTruoc) XuatHDNamTruoc,
       SUM(B.XuatHDNamHienTai)XuatHDNamHienTai,
       SUM(B.DsHaiDau)DsHaiDau,
       SUM(B.[XHD/HD]) * 100[XHD/HD],
       SUM(B.ChuaXuat)ChuaXuat,
       NULL a,
       NULL b,
       GETDATE() c,
       NULL d,
       GETDATE() e,
       0 f,
       0 g,
       0 h,
       B.TTHT
FROM   (
           SELECT *,1 AS TTHT
           FROM   #HD2013
           UNION ALL
           SELECT *,2
           FROM   #HD2014
           UNION ALL
           SELECT *,4
           FROM   #HD2015
           UNION ALL
           SELECT *,3
           FROM   #HDThang
       )B
GROUP BY
       B.HopDong,B.TTHT
UNION ALL
SELECT
		13,
       SUM(B.XuatHDNamTruoc),
       SUM(B.XuatHDNamHienTai),
       0,0,
       --SUM(B.DsHaiDau),
       --SUM(B.[XHD/HD]) * 100,
       SUM(B.ChuaXuat),
       NULL,
       NULL,
       GETDATE(),
       NULL,
       GETDATE(),
       0,
       0,
       0,
       4
FROM   (
           SELECT *,1 AS TTHT
           FROM   #HD2013
           UNION ALL
           SELECT *,2
           FROM   #HD2014
           UNION ALL
           SELECT *,4
           FROM   #HD2015
           UNION ALL
           SELECT *,3
           FROM   #HDThang
           UNION ALL
           SELECT 0 NamHopDong,ISNULL(SUM(GiaTri),0),0,0,0,0,0 FROM ThongTinHoaDon_KhongSoHopDong
           WHERE YEAR(NgayXuatHoaDon)=@NamXuatHD-1
           UNION ALL
           SELECT 0 NamHopDong,0,ISNULL(SUM(GiaTri),0),0,0,0,0 FROM ThongTinHoaDon_KhongSoHopDong
           WHERE YEAR(NgayXuatHoaDon)=@NamXuatHD
       )B
WHERE b.HopDong<>@NamXuatHD
) C
DROP TABLE #HD2013
DROP TABLE #HD2014
DROP TABLE #HD2015
DROP TABLE #HDThang

END


```
