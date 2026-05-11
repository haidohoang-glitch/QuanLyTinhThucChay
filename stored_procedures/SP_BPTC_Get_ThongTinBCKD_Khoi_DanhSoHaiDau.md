# Stored Procedure: `BPTC_Get_ThongTinBCKD_Khoi_DanhSoHaiDau`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:52.070000
- **Ngày sửa cuối**: 2015-06-11 18:17:52.070000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `datetime(8)` | No |
| `@NgayKetThuc` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		ChungTN
-- Create date: 15-05-2015
-- Description:	BCTC_ThongTinBCKD_Khoi_DanhSoHaiDau_GetData
-- =============================================
CREATE PROCEDURE [dbo].[BPTC_Get_ThongTinBCKD_Khoi_DanhSoHaiDau]
	 @NgayBatDau DATETIME,
    @NgayKetThuc DATETIME
AS
BEGIN
SELECT A.Thang,
       A.ThanhTienHaiDau*1.1 DoanhSoHaiDau,
       ttct.DoanhSoChiTieu,
       (
           SELECT SUM(hdct.ThanhTien) AS ThanhTienHaiDau
           FROM   HopDong hd
                  INNER JOIN HopDongChiTiet hdct
                       ON  hd.HopDongID = hdct.HopDongFK
           WHERE  YEAR(hd.NgayDanhSoHopDong) = YEAR (@NgayKetThuc)-1
                  AND A.Thang = MONTH(hd.NgayDanhSoHopDong)
                   AND hd.DeletedStatus=0 AND hd.TrangThaiHopDong<>3 AND hdct.DeletedStatus=0
                   AND hd.IsBanCung=1
           GROUP BY
                  MONTH(hd.NgayDanhSoHopDong)
       )*1.1 AS CungKyNamTruoc
FROM   (
           SELECT MONTH(hd.NgayDanhSoHopDong) AS Thang,
                  SUM(hdct.ThanhTien) AS ThanhTienHaiDau
           FROM   HopDong hd
                  INNER JOIN HopDongChiTiet hdct
                       ON  hd.HopDongID = hdct.HopDongFK
           WHERE  CONVERT(DATE,hd.NgayDanhSoHopDong) BETWEEN @NgayBatDau AND @NgayKetThuc
           AND hd.DeletedStatus=0 AND hd.TrangThaiHopDong<>3 AND hdct.DeletedStatus=0
           AND hd.IsBanCung=1
           GROUP BY
                  MONTH(hd.NgayDanhSoHopDong)
       ) A
       INNER JOIN ThongTinChiTieu ttct
            ON  A.Thang = MONTH(ttct.ThoiGianKetThuc)
WHERE  ttct.LevelChiTieu = 2
		AND ttct.LoaiTien = 3
		AND ttct.DmChiTieuBoPhanREF=0
		AND ttct.DeleteStatus=0
END

```
