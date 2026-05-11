# Stored Procedure: `BPTC_Get_ThongTinBCKD_Khoi_ThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:51.997000
- **Ngày sửa cuối**: 2015-06-11 18:17:51.997000

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
-- Description:	SP_BPTC_ThongTinBCKD_Khoi_ThucChay_GetData
-- =============================================
CREATE PROCEDURE [dbo].[BPTC_Get_ThongTinBCKD_Khoi_ThucChay]
(
    @NgayBatDau      DATETIME,
    @NgayKetThuc     DATETIME,
    @ThongTinBCKDID  INT,
    @TenBaoCao       NVARCHAR(200)
)
AS
BEGIN
	SELECT MONTH(tcdt.NgayThucHien) Thang,
	       SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0)) * 1.1 
	       DsThucChay INTO #DsThucChay
	FROM   ThucChayDaTinh tcdt
	WHERE  tcdt.NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
	       AND tcdt.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
	       AND tcdt.TrangThaiHopDong <> 3
	GROUP BY
	       MONTH(tcdt.NgayThucHien)
	
	SELECT MONTH(tcdt.NgayThucHien) Thang,
	       SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0)) * 1.1 
	       DsThucChayNamTruoc INTO #DsThucChayNamTruoc
	FROM   ThucChayDaTinh tcdt
	WHERE  YEAR(tcdt.NgayThucHien) = YEAR(@NgayKetThuc) -1
	       --AND MONTH(tcdt.NgayThucHien) <= MONTH(@NgayKetThuc) -- Loại bỏ trường hợp này để lấy full giá trị thực chạy năm trước
	       AND tcdt.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
	       AND tcdt.TrangThaiHopDong <> 3
	GROUP BY
	       MONTH(tcdt.NgayThucHien)
	
	
	
	
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
	                  --AND MONTH(ttct.ThoiGianKetThuc) <= MONTH(@NgayKetThuc) -- Loại bỏ trường hợp này để lấy full giá trị chỉ tiêu
	           GROUP BY
	                  MONTH(ttct.ThoiGianKetThuc),
	                  ttct.LoaiTien
	       ) B
	GROUP BY
	       B.Thang
	
	INSERT INTO BPTC_ThongTinBCKD_Khoi_ThucChay
	  (
	    -- BPTC_ThongTinBCKD_Khoi_ThucChayID -- this column value is auto-generated
	    BPTC_ThongTinBCKDREF,
	    TenBaoCaoKinhDoanh,
	    ThoiGian,
	    ChiTieuThucChay,
	    DoanhSoThucChayCungKy,
	    DoanhSoThucChay,
	    NoiDungDanhGia,
	    CreatedBy,
	    CreatedAt,
	    LastModifiedBy,
	    LastModifiedAt,
	    DeleteStatus,
	    PrintStatus,
	    RecordStatus
	  )
	SELECT 
		@ThongTinBCKDID,
		@TenBaoCao,
		#ThongTinChiTieu.Thang,
	    ISNULL(CTThucChay,0)CTThucChay,
	    ISNULL(DsThucChayNamTruoc,0)DsThucChayNamTruoc,
	    ISNULL(DsThucChay,0)DsThucChay,
	    NULL,
	    NULL,
	    GETDATE(),
	    NULL,
	    GETDATE(),
	    0,
	    0,
	    0
	FROM   #ThongTinChiTieu
	       LEFT JOIN #DsThucChayNamTruoc
	            ON  #ThongTinChiTieu.Thang = #DsThucChayNamTruoc.Thang
	       LEFT JOIN #DsThucChay
	            ON  #DsThucChay.Thang = #ThongTinChiTieu.Thang
	ORDER BY #ThongTinChiTieu.Thang
	DROP TABLE #ThongTinChiTieu
	DROP TABLE #DsThucChayNamTruoc
	DROP TABLE #DsThucChay
END

```
