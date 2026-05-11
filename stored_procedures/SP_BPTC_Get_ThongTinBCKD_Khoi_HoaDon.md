# Stored Procedure: `BPTC_Get_ThongTinBCKD_Khoi_HoaDon`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:51.060000
- **Ngày sửa cuối**: 2015-06-11 18:17:51.060000

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
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[BPTC_Get_ThongTinBCKD_Khoi_HoaDon]
(
    @NgayBatDau      DATETIME,
    @NgayKetThuc     DATETIME,
    @ThongTinBCKDID  INT,
    @TenBaoCao       NVARCHAR(200)
)
AS
BEGIN
DECLARE @HoaDonKhongSoHopDong TABLE
		(
		HoaDonKhongSoHopDongID [int] NULL,
		SoHoaDon NVARCHAR(50) NULL,
		[ThangXuat] [int] NULL,
		[NamXuat] [int] NULL,
		[GiaTri] [bigint] NULL
		)	
INSERT  INTO @HoaDonKhongSoHopDong
		SELECT  a.ThongTinHoaDon_KhongSoHopDongID,
				a.SoHoaDon,
				Month(A.NgayXuatHoaDon),
				YEAR(a.NgayXuatHoaDon),
				A.Giatri 
		FROM	ThongTinHoaDon_KhongSoHopDong a
		WHERE	A.[DeletedStatus]=0
	
	SELECT A.Thang,
       SUM(A.TienXuatHD) DsXuatHD INTO #DsXuatHD
	FROM   (
           SELECT MONTH(tthd.NgayXuatHoaDon) AS Thang,
                  SUM(GiaTri) TienXuatHD
           FROM   ThongTinHoaDon tthd
                  INNER JOIN HopDong hd
                       ON  tthd.HopDongREF = hd.HopDongID
           WHERE  tthd.NgayXuatHoaDon BETWEEN @NgayBatDau AND @NgayKetThuc
                  AND tthd.DeletedStatus = 0
           GROUP BY
                  MONTH(tthd.NgayXuatHoaDon)
           UNION ALL
           SELECT hdkshd.ThangXuat,
                  SUM(hdkshd.GiaTri)
           FROM   @HoaDonKhongSoHopDong hdkshd
           WHERE  hdkshd.NamXuat = YEAR(@NgayKetThuc)
           AND hdkshd.ThangXuat<= MONTH(@NgayKetThuc)
           --AND hdkshd.DeletedStatus=0
           GROUP BY
                  hdkshd.ThangXuat
       ) A    
	GROUP BY A.Thang
	
	SELECT A.Thang,
       SUM(A.TienXuatHD) DsXuatHDNamTruoc INTO #DsXuatHDNamTruoc
	FROM   (
           SELECT MONTH(tthd.NgayXuatHoaDon) AS Thang,
                  SUM(GiaTri) TienXuatHD
           FROM   ThongTinHoaDon tthd
                  INNER JOIN HopDong hd
                       ON  tthd.HopDongREF = hd.HopDongID
           WHERE  YEAR(tthd.NgayXuatHoaDon) = YEAR(@NgayKetThuc) -1
                  --AND MONTH(tthd.NgayXuatHoaDon) <= MONTH(@NgayKetThuc) -- Loại bỏ trường hợp này để lấy full năm trước
                  AND tthd.DeletedStatus = 0
           GROUP BY
                  MONTH(tthd.NgayXuatHoaDon)
           UNION ALL
           SELECT hdkshd.ThangXuat,
                  SUM(hdkshd.GiaTri)
           FROM   @HoaDonKhongSoHopDong hdkshd
           WHERE  hdkshd.NamXuat = YEAR(@NgayKetThuc) -1
                  --AND hdkshd.ThangXuat <= MONTH(@NgayKetThuc) -- Loại bỏ trường hợp này để lấy giá trị full năm trước
                 -- AND hdkshd.DeletedStatus=0
           GROUP BY
                  hdkshd.ThangXuat
       ) A 
	GROUP BY A.Thang
       
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
				  AND ttct.DeleteStatus=0
				  AND ttct.DmChiTieuBoPhanREF=0
                  AND YEAR(ttct.ThoiGianKetThuc) = YEAR(@NgayKetThuc)
                  --AND MONTH(ttct.ThoiGianKetThuc) <= MONTH(@NgayKetThuc) -- Loại bỏ trường hợp này để lấy giá trị full năm trước
           GROUP BY
                  MONTH(ttct.ThoiGianKetThuc),ttct.LoaiTien
       ) B GROUP BY B.Thang
	INSERT INTO BPTC_ThongTinBCKD_Khoi_HoaDon
	  (
	    -- BPTC_ThongTinBCKD_Khoi_HoaDonID -- this column value is auto-generated
	    BPTC_ThongTinBCKDREF,
	    TenBaoCaoKinhDoanh,
	    ThoiGian,
	    ChiTieuXuatHoaDon,
	    DoanhSoXuatHoaDonCungKy,
	    DoanhSoXuatHoaDon,
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
			ISNULL(CTHoaDon,0)CTHoaDon,
			ISNULL(DsXuatHDNamTruoc,0)DsXuatHDNamTruoc,
			ISNULL(DsXuatHD,0)DsXuatHD,
			NULL,
			NULL,
			GETDATE(),
			NULL,
			GETDATE(),
			0,
			0,
			0
	FROM   #ThongTinChiTieu
	       LEFT JOIN #DsXuatHDNamTruoc
	            ON  #ThongTinChiTieu.Thang = #DsXuatHDNamTruoc.Thang
	       LEFT JOIN #DsXuatHD
	            ON  #DsXuatHD.Thang = #ThongTinChiTieu.Thang
	ORDER BY #ThongTinChiTieu.Thang
	DROP TABLE #ThongTinChiTieu
	DROP TABLE #DsXuatHDNamTruoc
	DROP TABLE #DsXuatHD
END

```
