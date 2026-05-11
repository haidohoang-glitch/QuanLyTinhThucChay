# Stored Procedure: `BPTC_Get_ThongTinBCKD_Huy_ThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:52.230000
- **Ngày sửa cuối**: 2015-06-11 18:17:52.230000

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
CREATE PROCEDURE [dbo].[BPTC_Get_ThongTinBCKD_Huy_ThayDoi]
	@NgayBatDau DATETIME,
	@NgayKetThuc DATETIME,
	@ThongTinBCKDID INT,
	@TenBaoCao NVARCHAR(100)
AS
BEGIN


DECLARE @Tabl_HopDongHuy TABLE (HopDongID INT,NgayHuy DATETIME,HopDongThayDoiID INT )
INSERT INTO @Tabl_HopDongHuy
SELECT hdtd.HopDongFK, MAX(hdtd.NgayThayDoi),max(hdtd.HopDongThayDoiID) FROM HopDongThayDoi hdtd
WHERE hdtd.NgayThayDoi BETWEEN @NgayBatDau AND @NgayKetThuc
AND hdtd.LoaiThayDoi=0
GROUP BY hdtd.HopDongFK,MONTH(hdtd.NgayThayDoi)


-- Lay gia tri huy danh so
SELECT MONTH(hd.NgayDanhSoHopDong) Thang,SUM(-hd.GiaTriHopDong) GiaTriHuy INTO #GiaTriHuy
  FROM @Tabl_HopDongHuy tttd INNER JOIN HopDong hd ON tttd.HopDongID=hd.HopDongID
WHERE hd.TrangThaiHopDong=3 AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
AND hd.DeletedStatus=0
AND hd.NgayDanhSoHopDong BETWEEN @NgayBatDau AND @NgayKetThuc
GROUP BY MONTH(hd.NgayDanhSoHopDong)

DECLARE @Tabl_HopDongThayDoi TABLE (HopDongID INT,NgayThayDoi DATETIME,HopDongThayDoiID INT )
INSERT INTO @Tabl_HopDongThayDoi
SELECT hdtd.HopDongFK, MAX(hdtd.NgayThayDoi),max(hdtd.HopDongThayDoiID) FROM HopDongThayDoi hdtd
WHERE hdtd.NgayThayDoi BETWEEN @NgayBatDau AND @NgayKetThuc
AND hdtd.LoaiThayDoi=1
GROUP BY hdtd.HopDongFK,MONTH(hdtd.NgayThayDoi)

-- Gia Tri thay doi hop dong danh so
SELECT  MONTH(hd.NgayDanhSoHopDong) Thang,SUM(hd.GiaTriHopDong)- SUM(hdtd.GiaTriHopDong) GiaTriHopDongTD INTO #GiaTriThayDoi
  FROM @Tabl_HopDongThayDoi tttd 
  INNER JOIN HopDong hd ON tttd.HopDongID=hd.HopDongID
  INNER JOIN HopDongThayDoi hdtd ON hdtd.HopDongThayDoiID=tttd.HopDongThayDoiID
WHERE hd.TrangThaiHopDong<>3 AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
AND hd.DeletedStatus=0
AND hd.NgayDanhSoHopDong BETWEEN @NgayBatDau AND @NgayKetThuc
GROUP BY  MONTH(hd.NgayDanhSoHopDong)

-- Lay gia tri huy hai dau
SELECT MONTH(hd.NgayDanhSoHopDong) Thang,SUM(-hd.GiaTriHopDong) GiaTriHuy INTO #GiaTriHuyHaiDau
  FROM @Tabl_HopDongHuy tttd INNER JOIN HopDong hd ON tttd.HopDongID=hd.HopDongID
WHERE hd.TrangThaiHopDong=3 AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
AND hd.DeletedStatus=0
AND hd.IsBanCung=1
AND hd.NgayDanhSoHopDong BETWEEN @NgayBatDau AND @NgayKetThuc
GROUP BY MONTH(hd.NgayDanhSoHopDong)
-- Lay gia tri thay doi hai dau
SELECT  MONTH(hd.NgayDanhSoHopDong) Thang,SUM(hd.GiaTriHopDong)- SUM(hdtd.GiaTriHopDong) GiaTriHopDongTD INTO #GiaTriThayDoiHaiDau
  FROM @Tabl_HopDongThayDoi tttd 
  INNER JOIN HopDong hd ON tttd.HopDongID=hd.HopDongID
  INNER JOIN HopDongThayDoi hdtd ON hdtd.HopDongThayDoiID=tttd.HopDongThayDoiID
WHERE hd.TrangThaiHopDong<>3 AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
AND hd.DeletedStatus=0
AND hd.IsBanCung=1
AND hd.NgayDanhSoHopDong BETWEEN @NgayBatDau AND @NgayKetThuc
GROUP BY  MONTH(hd.NgayDanhSoHopDong)



SELECT #GiaTriHuy.Thang,#GiaTriHuy.GiaTriHuy+#GiaTriThayDoi.GiaTriHopDongTD DanhSo,A.HaiDau INTO #Temp FROM #GiaTriHuy LEFT JOIN #GiaTriThayDoi
ON #GiaTriHuy.Thang=#GiaTriThayDoi.Thang
LEFT JOIN (
SELECT #GiaTriHuyHaiDau.Thang,#GiaTriHuyHaiDau.GiaTriHuy+#GiaTriThayDoiHaiDau.GiaTriHopDongTD HaiDau FROM #GiaTriHuyHaiDau LEFT JOIN #GiaTriThayDoiHaiDau
ON #GiaTriHuyHaiDau.Thang=#GiaTriThayDoiHaiDau.Thang) A
ON A.Thang=#GiaTriHuy.Thang

	
	SELECT MONTH(hd.NgayDanhSoHopDong) Thang,
	       SUM(hdct.ThanhTien) * 1.1 DsDanhSo INTO #DsDanhSo
	FROM   HopDong hd
	       INNER JOIN HopDongChiTiet hdct
	            ON  hd.HopDongID = hdct.HopDongFK
	WHERE  (hd.NgayDanhSoHopDong) BETWEEN @NgayBatDau AND @NgayKetThuc
	       AND 
	       hd.TrangThaiHopDong <> 3
	       AND hd.DeletedStatus = 0
	       AND hdct.DeletedStatus = 0
	       AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
	GROUP BY
	       MONTH(hd.NgayDanhSoHopDong)
	
	SELECT MONTH(hd.NgayDanhSoHopDong) Thang,
	       SUM(hdct.ThanhTien) * 1.1 DsHaiDau INTO #DsHaiDau
	FROM   HopDong hd
	       INNER JOIN HopDongChiTiet hdct
	            ON  hd.HopDongID = hdct.HopDongFK
	WHERE  
	(hd.NgayDanhSoHopDong) BETWEEN @NgayBatDau AND @NgayKetThuc
	       AND 
	       hd.TrangThaiHopDong <> 3
	       AND hd.DeletedStatus = 0
	       AND hdct.DeletedStatus = 0
	       AND IsBanCung = 1
	       AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
	GROUP BY
	       MONTH(hd.NgayDanhSoHopDong)
-- Chèn dữ liệu chi tiết	
INSERT INTO BPTC_ThongTinBCKD_Huy_ThayDoi
	  (
	    [BPTC_ThongTinBCKDID],
	    [TenBaoCaoKinhDoanh],
	    [HopDong_Thang],
	    [DoanhSoDanhSo],
	    [DoanhSoHaiDau],
	    [TiLeDanhSo_TongDanhSo],
	    [TiLeHaiDau_TongHaiDau],
	    [NoiDungDanhGia],
	    [CreatedBy],
	    [CreatedAt],
	    [LastModifiedBy],
	    [LastModifiedAt],
	    [DeleteStatus],
	    [PrintStatus],
	    [RecordStatus]
	  )
	  SELECT * FROM (
SELECT		@ThongTinBCKDID a,
	       @TenBaoCao b,
	       #Temp.Thang,
	       ISNULL(#Temp.DanhSo,0) DanhSo,
	       ISNULL(#Temp.HaiDau,0) HaiDau,
	       --#DsDanhSo.DsDanhSo,
	       --#DsHaiDau.DsHaiDau,
	       ROUND(
	           ISNULL(#Temp.DanhSo,0) / (ISNULL(#DsDanhSo.DsDanhSo,0) -ISNULL(#Temp.DanhSo,0))
	           * 100,
	           2
	       ) TLDanhSo,
	       ROUND(
	           ISNULL(#Temp.HaiDau,0) / (ISNULL(#DsHaiDau.DsHaiDau,0) -ISNULL(#Temp.HaiDau,0))
	           * 100,
	           2
	       ) TLHaiDau,
	       NULL c,
	       NULL d,
	       GETDATE() e,
	       NULL f,
	       GETDATE() g,
	       0 h,
	       0 i,
	       0 j
FROM   #Temp
	       INNER JOIN #DsDanhSo
	            ON  #Temp.Thang = #DsDanhSo.Thang
	       INNER JOIN #DsHaiDau
	            ON  #Temp.Thang = #DsHaiDau.Thang
-- Chèn dữ liệu tổng
UNION ALL
SELECT		@ThongTinBCKDID,
	       @TenBaoCao,
	       13,
	       SUM(ISNULL(#Temp.DanhSo,0)) DanhSo,
	       SUM(ISNULL(#Temp.HaiDau,0)) HaiDau,
	       --#DsDanhSo.DsDanhSo,
	       --#DsHaiDau.DsHaiDau,
	       ROUND(
	           SUM(ISNULL(#Temp.DanhSo,0)) / (SUM(ISNULL(#DsDanhSo.DsDanhSo,0)) -SUM(ISNULL(#Temp.DanhSo,0)))
	           * 100,
	           2
	       ) TLDanhSo,
	       ROUND(
	           SUM(ISNULL(#Temp.HaiDau,0)) / (SUM(ISNULL(#DsHaiDau.DsHaiDau,0)) -SUM(ISNULL(#Temp.HaiDau,0)))
	           * 100,
	           2
	       ) TLHaiDau,
	       NULL,
	       NULL,
	       GETDATE(),
	       NULL,
	       GETDATE(),
	       0,
	       0,
	       0
FROM   #Temp
	       INNER JOIN #DsDanhSo
	            ON  #Temp.Thang = #DsDanhSo.Thang
	       INNER JOIN #DsHaiDau
	            ON  #Temp.Thang = #DsHaiDau.Thang
	  ) A
DROP TABLE #GiaTriHuy
DROP TABLE #GiaTriThayDoi
DROP TABLE #GiaTriThayDoiHaiDau
DROP TABLE #GiaTriHuyHaiDau
DROP TABLE #Temp
DROP TABLE #DsDanhSo
DROP TABLE #DsHaiDau
END

```
