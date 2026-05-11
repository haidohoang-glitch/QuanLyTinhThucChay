# Stored Procedure: `BPTC_Get_ThongTinBCKD_Khoi_DanhSo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:52.130000
- **Ngày sửa cuối**: 2015-06-11 18:17:52.130000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `datetime(8)` | No |
| `@NgayKetThuc` | `datetime(8)` | No |
| `@ThongTinBCKDID` | `int(4)` | No |
| `@TenBaoCao` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql

-- =============================================
-- Author:		ChungTN
-- Create date: 15-05-2015
-- Description:	BCTC_ThongTinBCKD_Khoi_DanhSo_GetData
-- =============================================
CREATE PROCEDURE [dbo].[BPTC_Get_ThongTinBCKD_Khoi_DanhSo]
    @NgayBatDau DATETIME ,
    @NgayKetThuc DATETIME ,
    @ThongTinBCKDID INT,
    @TenBaoCao NVARCHAR(200)
AS 
    BEGIN

--DsDanhSoHienTai
SELECT MONTH(hd.NgayDanhSoHopDong) Thang,
       SUM(hdct.ThanhTien) * 1.1 DsDanhSo INTO #DsDanhSo
FROM   HopDong hd
       INNER JOIN HopDongChiTiet hdct
            ON  hd.HopDongID = hdct.HopDongFK
WHERE  (hd.NgayDanhSoHopDong) BETWEEN @NgayBatDau AND @NgayKetThuc
       AND hd.TrangThaiHopDong <> 3
       AND hd.DeletedStatus = 0
       AND hdct.DeletedStatus = 0
       AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
GROUP BY
       MONTH(hd.NgayDanhSoHopDong)
       --DsDanhSoNamTruoc
       SELECT MONTH(hd.NgayDanhSoHopDong) Thang,
       SUM(hdct.ThanhTien) * 1.1 DsDanhSoNamTruoc INTO #DsDanhSoNamTruoc
FROM   HopDong hd
       INNER JOIN HopDongChiTiet hdct
            ON  hd.HopDongID = hdct.HopDongFK
WHERE  YEAR(hd.NgayDanhSoHopDong) = YEAR(@NgayKetThuc) -1
       --AND MONTH(hd.NgayDanhSoHopDong) <= MONTH(@NgayKetThuc) -- Loại bỏ trường hợp này để lấy full doanh số của năm trước
       AND hd.TrangThaiHopDong <> 3
       AND hd.DeletedStatus = 0
       AND hdct.DeletedStatus = 0
       AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
GROUP BY
       MONTH(hd.NgayDanhSoHopDong)
--ThongTinChiTieu
       SELECT B.Thang,
       SUM(ISNULL(B.DanhSo, 0)) CTDanhSo,
       SUM(ISNULL(B.HaiDau, 0)) CTHaiDau,
       SUM(ISNULL(B.HoaDon, 0)) CTHoaDon,
       SUM(ISNULL(B.ThucChay, 0)) CTThucChay,
       SUM(ISNULL(B.TienVe, 0)) CTTienVe INTO #ThongTinChiTieu
FROM   (
           SELECT MONTH(ttct.ThoiGianKetThuc) Thang,
                  (
                      CASE 
                           WHEN ttct.LoaiTien = 2 THEN SUM(ttct.DoanhSoChiTieu)
                      END
                  ) AS DanhSo,
                  (
                      CASE 
                           WHEN ttct.LoaiTien = 3 THEN SUM(ttct.DoanhSoChiTieu)
                      END
                  ) AS HaiDau,
                  (
                      CASE 
                           WHEN ttct.LoaiTien = 4 THEN SUM(ttct.DoanhSoChiTieu)
                      END
                  ) HoaDon,
                  (
                      CASE 
                           WHEN ttct.LoaiTien = 1 THEN SUM(ttct.DoanhSoChiTieu)
                      END
                  ) AS ThucChay,
                  (
                      CASE 
                           WHEN ttct.LoaiTien = 1 THEN SUM(ttct.DoanhSoChiTieu)
                      END
                  ) AS TienVe
           FROM   ThongTinChiTieu ttct
           WHERE  ttct.LevelChiTieu = 2
				  AND ttct.DmChiTieuBoPhanREF=0
				  AND ttct.DeleteStatus=0
                  AND YEAR(ttct.ThoiGianKetThuc) = YEAR(@NgayKetThuc)
                  --AND MONTH(ttct.ThoiGianKetThuc) <= MONTH(@NgayKetThuc) -- Loại bỏ trường hợp này để lấy full chỉ tiêu 12 tháng
           GROUP BY
                  MONTH(ttct.ThoiGianKetThuc),ttct.LoaiTien
       ) B GROUP BY B.Thang
       
INSERT  INTO BPTC_ThongTinBCKD_Khoi_DanhSo
                ( -- BPTC_ThongTinBCKD_Khoi_DanhSoID -- this column value is auto-generated
                  BPTC_ThongTinBCKDREF ,
                  TenBaoCaoKinhDoanh ,
                  ThoiGian ,
                  DoanhSoChiTieu ,
                  DoanhSoDanhSoCungKy ,
                  DoanhSoDanhSo ,
                  NoiDungDanhGia ,
                  CreatedBy ,
                  CreatedAt ,
                  LastModifiedBy ,
                  LastModifiedAt ,
                  DeleteStatus ,
                  PrintStatus ,
                  RecordStatus
	          )
       
SELECT 
		@ThongTinBCKDID,
		@TenBaoCao,
		#ThongTinChiTieu.Thang,
		ISNULL(#ThongTinChiTieu.CTDanhSo,0)CTDanhSo,
		IsNULL(#DsDanhSoNamTruoc.DsDanhSoNamTruoc,0)DsDanhSoNamTruoc,
		isnull(#DsDanhSo.DsDanhSo,0)DsDanhSo,
		NULL,
		NULL,
		GETDATE(),
		NULL,
		GETDATE(),
		0,0,0
FROM   #ThongTinChiTieu
			LEFT JOIN #DsDanhSoNamTruoc
            ON  #ThongTinChiTieu.Thang = #DsDanhSoNamTruoc.Thang
            LEFT JOIN #DsDanhSo ON  #DsDanhSo.Thang=#ThongTinChiTieu.Thang
            DROP TABLE #DsDanhSo
            DROP TABLE #DsDanhSoNamTruoc
            DROP TABLE #ThongTinChiTieu
            
--EXEC SP_EXECUTESQL @Sql,@ParamDefinition,@NgayBatDau,@NgayKetThuc,@ThongTinBCKDID,@TenBaoCao
    END


```
