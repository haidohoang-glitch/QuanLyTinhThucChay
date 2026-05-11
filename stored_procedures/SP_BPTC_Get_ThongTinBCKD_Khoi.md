# Stored Procedure: `BPTC_Get_ThongTinBCKD_Khoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:52.187000
- **Ngày sửa cuối**: 2015-06-11 18:17:52.187000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `datetime(8)` | No |
| `@NgayKetThuc` | `datetime(8)` | No |
| `@ThongTinBCKDID` | `int(4)` | No |
| `@TenBaoCao` | `nvarchar(200)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[BPTC_Get_ThongTinBCKD_Khoi]
	@NgayBatDau DATETIME,
	@NgayKetThuc DATETIME,
	@ThongTinBCKDID INT,
	@TenBaoCao NVARCHAR(100)
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
INSERT	INTO @HoaDonKhongSoHopDong
		SELECT	a.ThongTinHoaDon_KhongSoHopDongID,
				a.SoHoaDon,
				Month(A.NgayXuatHoaDon),
				YEAR(a.NgayXuatHoaDon),
				A.Giatri 
		FROM	ThongTinHoaDon_KhongSoHopDong a
		WHERE	A.[DeletedStatus]=0

--SELECT * FROM @HoaDonKhongSoHopDong

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

SELECT MONTH(hd.NgayDanhSoHopDong) Thang,
       SUM(hdct.ThanhTien) * 1.1 DsHaiDau INTO #DsHaiDau
FROM   HopDong hd
       INNER JOIN HopDongChiTiet hdct
            ON  hd.HopDongID = hdct.HopDongFK
WHERE  (hd.NgayDanhSoHopDong) BETWEEN @NgayBatDau AND @NgayKetThuc
       AND hd.TrangThaiHopDong <> 3
       AND hd.DeletedStatus = 0
       AND hdct.DeletedStatus = 0
       AND IsBanCung = 1
       AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
GROUP BY
       MONTH(hd.NgayDanhSoHopDong)

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
                  AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
                  AND hd.TrangThaiHopDong <> 3
				  AND hd.DeletedStatus = 0
           GROUP BY
                  MONTH(tthd.NgayXuatHoaDon)
           UNION ALL
           SELECT hdkshd.ThangXuat,
                  SUM(hdkshd.GiaTri)
           FROM   @HoaDonKhongSoHopDong hdkshd
           WHERE  hdkshd.NamXuat = YEAR(@NgayKetThuc)
           GROUP BY
                  hdkshd.ThangXuat
       ) A          
GROUP BY A.Thang
SELECT MONTH(tcdt.NgayThucHien) Thang,
       SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) * 1.1 
       DsThucChay INTO #DsThucChay
FROM   ThucChayDaTinh tcdt
WHERE  tcdt.NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
       AND tcdt.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
       AND tcdt.TrangThaiHopDong <> 3
GROUP BY
       MONTH(tcdt.NgayThucHien)

SELECT MONTH(tttv.NgayThanhToan) Thang,
       SUM(GiaTri) DsTienVe INTO #DsTienVe
FROM   ThongTinTienVe tttv
       INNER JOIN HopDong hd
            ON  tttv.HopDongREF = hd.HopDongID
WHERE  CONVERT(DATE, tttv.NgayThanhToan) BETWEEN @NgayBatDau AND 
       @NgayKetThuc
       AND tttv.DeletedStatus = 0
                  AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
                  AND hd.TrangThaiHopDong <> 3
       AND hd.DeletedStatus = 0
GROUP BY
       MONTH(tttv.NgayThanhToan)
       
SELECT MONTH(hd.NgayDanhSoHopDong) Thang,
       SUM(hdct.ThanhTien) * 1.1 DsDanhSoNamTruoc INTO #DsDanhSoNamTruoc
FROM   HopDong hd
       INNER JOIN HopDongChiTiet hdct
            ON  hd.HopDongID = hdct.HopDongFK
WHERE  YEAR(hd.NgayDanhSoHopDong) = YEAR(@NgayKetThuc) -1
       AND MONTH(hd.NgayDanhSoHopDong) <= MONTH(@NgayKetThuc)
       AND hd.TrangThaiHopDong <> 3
       AND hd.DeletedStatus = 0
       AND hdct.DeletedStatus = 0
       AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
GROUP BY
       MONTH(hd.NgayDanhSoHopDong)

SELECT MONTH(hd.NgayDanhSoHopDong) Thang,
       SUM(hdct.ThanhTien) * 1.1 DsHaiDauNamTruoc INTO #DsHaiDauNamTruoc
FROM   HopDong hd
       INNER JOIN HopDongChiTiet hdct
            ON  hd.HopDongID = hdct.HopDongFK
WHERE  YEAR(hd.NgayDanhSoHopDong) = YEAR(@NgayKetThuc) -1
       AND MONTH(hd.NgayDanhSoHopDong) <= MONTH(@NgayKetThuc)
       AND hd.TrangThaiHopDong <> 3
       AND hd.DeletedStatus = 0
       AND hdct.DeletedStatus = 0
       AND ISbancung = 1
       AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
GROUP BY
       MONTH(hd.NgayDanhSoHopDong)


SELECT MONTH(tcdt.NgayThucHien) Thang,
       SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) * 1.1 
       DsThucChayNamTruoc INTO #DsThucChayNamTruoc
FROM   ThucChayDaTinh tcdt
WHERE  YEAR(tcdt.NgayThucHien) = YEAR(@NgayKetThuc) -1
       AND MONTH(tcdt.NgayThucHien) <= MONTH(@NgayKetThuc)
       AND tcdt.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
       AND tcdt.TrangThaiHopDong <> 3
GROUP BY
       MONTH(tcdt.NgayThucHien)
                
                      
SELECT A.Thang,
       SUM(A.TienXuatHD) DsXuatHDNamTruoc INTO #DsXuatHDNamTruoc
FROM   (
           SELECT MONTH(tthd.NgayXuatHoaDon) AS Thang,
                  SUM(GiaTri) TienXuatHD
           FROM   ThongTinHoaDon tthd
                  INNER JOIN HopDong hd
                       ON  tthd.HopDongREF = hd.HopDongID
           WHERE  YEAR(tthd.NgayXuatHoaDon) = YEAR(@NgayKetThuc) -1
                  AND MONTH(tthd.NgayXuatHoaDon) <= MONTH(@NgayKetThuc)
                  AND tthd.DeletedStatus = 0
                  AND tthd.DeletedStatus = 0
                  AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
                  AND hd.TrangThaiHopDong <> 3
           GROUP BY
                  MONTH(tthd.NgayXuatHoaDon)
           UNION ALL
           SELECT hdkshd.ThangXuat,
                  SUM(hdkshd.GiaTri)
           FROM   @HoaDonKhongSoHopDong hdkshd
           WHERE  hdkshd.NamXuat = YEAR(@NgayKetThuc) -1
                  AND hdkshd.ThangXuat <= MONTH(@NgayKetThuc)
           GROUP BY
                  hdkshd.ThangXuat
       ) A                          
GROUP BY A.Thang      
SELECT MONTH(tttv.NgayThanhToan)Thang,
       SUM(GiaTri) DsTienVeNamTruoc INTO #DsTienVeNamTruoc
FROM   ThongTinTienVe tttv
       INNER JOIN HopDong hd
            ON  tttv.HopDongREF = hd.HopDongID
WHERE  YEAR(tttv.NgayThanhToan) = YEAR(@NgayKetThuc) -1
       AND MONTH(tttv.NgayThanhToan) <= MONTH(@NgayKetThuc)
       AND tttv.DeletedStatus = 0
                  AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
                  AND hd.TrangThaiHopDong <> 3
GROUP BY
       MONTH(tttv.NgayThanhToan)

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
                  AND MONTH(ttct.ThoiGianKetThuc) <= MONTH(@NgayKetThuc)
           GROUP BY
                  MONTH(ttct.ThoiGianKetThuc),ttct.LoaiTien
       ) B GROUP BY B.Thang

--SELECT * FROM #ThongTinChiTieu


	
	INSERT INTO BPTC_ThongTinBCKD_Khoi
	  (
	    [BPTC_ThongTinBCKDREF],
	    [TenBaoCaoKinhDoanh],
	    [ThoiGian],
	    [DoanhSoDanhSo],
	    [DoanhSoHaiDau],
	    [DoanhSoThucChay],
	    [DoanhSoXuatHoaDon],
	    [DoanhSoTienVe],
	    [ThuTuHienThi],
	    [NoiDungDanhGia],
	    [CreatedBy],
	    [CreatedAt],
	    [LastModifiedBy],
	    [LastModifiedAt],
	    [DeleteStatus],
	    [PrintStatus],
	    [RecordStatus]
	  )
	SELECT @ThongTinBCKDID,
	       @TenBaoCao,
	    #DsDanhSo.Thang,
       #DsDanhSo.DsDanhSo,
       #DsHaiDau.DsHaiDau,
       #DsThucChay.DsThucChay,
       #DsXuatHD.DsXuatHD,
       #DsTienVe.DsTienVe,
        0,
	       NULL,
	       NULL,
	       GETDATE(),
	       NULL,
	       GETDATE(),
	       0,
	       0,
	       0
FROM   #DsDanhSo 
       INNER JOIN #DsHaiDau
            ON  #DsDanhSo.Thang = #DsHaiDau.Thang
       INNER JOIN #DsXuatHD
            ON  #DsDanhSo.Thang = #DsXuatHD.Thang
       INNER JOIN #DsThucChay
            ON  #DsDanhSo.Thang = #DsThucChay.Thang
       INNER JOIN #DsTienVe
            ON  #DsDanhSo.Thang = #DsTienVe.Thang
       INNER JOIN #DsDanhSoNamTruoc
            ON  #DsDanhSo.Thang = #DsDanhSoNamTruoc.Thang
       INNER JOIN #DsHaiDauNamTruoc
            ON  #DsDanhSo.Thang = #DsHaiDauNamTruoc.Thang
       INNER JOIN #DsThucChayNamTruoc
            ON  #DsDanhSo.Thang = #DsThucChayNamTruoc.Thang
       INNER JOIN #DsXuatHDNamTruoc
            ON  #DsDanhSo.Thang = #DsXuatHDNamTruoc.Thang
       INNER JOIN #DsTienVeNamTruoc
            ON  #DsDanhSo.Thang = #DsTienVeNamTruoc.Thang
       INNER JOIN #ThongTinChiTieu ON #DsDanhSo.Thang=#ThongTinChiTieu.Thang

 --Tính lũy kế, chỉ tiêu và tăng trưởng

INSERT INTO BPTC_ThongTinBCKD_Khoi_Bro
(
	 --BPTC_ThongTinBCKD_Khoi_BroID, -- this column value is auto-generated
	BPTC_ThongTinBCKDREF,
	TenBaoCaoKinhDoanh,
	ThoiGian,
	DoanhSoDanhSo,
	DoanhSoHaiDau,
	DoanhSoThucChay,
	DoanhSoXuatHoaDon,
	DoanhSoTienVe,
	ThuTuHienThi,
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
	   N'Lũy Kế',
       SUM(#DsDanhSo.DsDanhSo),
       SUM(#DsHaiDau.DsHaiDau),
       SUM(#DsThucChay.DsThucChay),
       SUM(#DsXuatHD.DsXuatHD),
       SUM(#DsTienVe.DsTienVe),
        0,
	       NULL,
	       NULL,
	       GETDATE(),
	       NULL,
	       GETDATE(),
	       0,
	       0,
	       0
FROM   #DsDanhSo 
       INNER JOIN #DsHaiDau
            ON  #DsDanhSo.Thang = #DsHaiDau.Thang
       INNER JOIN #DsXuatHD
            ON  #DsDanhSo.Thang = #DsXuatHD.Thang
       INNER JOIN #DsThucChay
            ON  #DsDanhSo.Thang = #DsThucChay.Thang
       INNER JOIN #DsTienVe
            ON  #DsDanhSo.Thang = #DsTienVe.Thang	
UNION ALL
SELECT 
			@ThongTinBCKDID,
	       @TenBaoCao,
	      N'Chỉ tiêu',
	       SUM(A.CTDanhSo),
	       SUM(A.CTHaiDau),
	       SUM(A.CTThucChay),
	       SUM(A.CTHoaDon),
	       SUM(A.CTTienVe),
	       0,
	       NULL,
	       NULL,
	       GETDATE(),
	       NULL,
	       GETDATE(),
	       0,
	       0,
	       0
	FROM   #ThongTinChiTieu A

UNION ALL
	SELECT @ThongTinBCKDID,
	       @TenBaoCao,
	    N'Tăng trưởng',
       (SUM(#DsDanhSo.DsDanhSo)/SUM(#DsDanhSoNamTruoc.DsDanhSoNamTruoc)-1)*100,
       (SUM(#DsHaiDau.DsHaiDau)/SUM(#DsHaiDauNamTruoc.DsHaiDauNamTruoc)-1)*100,
       (SUM(#DsThucChay.DsThucChay)/SUM(#DsThucChayNamTruoc.DsThucChayNamTruoc)-1)*100,
       (SUM(#DsXuatHD.DsXuatHD)/SUM(#DsXuatHDNamTruoc.DsXuatHDNamTruoc)-1)*100,
       (SUM(#DsTienVe.DsTienVe)/SUM(#DsTienVeNamTruoc.DsTienVeNamTruoc)-1)*100,
        0,
	       NULL,
	       NULL,
	       GETDATE(),
	       NULL,
	       GETDATE(),
	       0,
	       0,
	       0
FROM   #DsDanhSo 
       INNER JOIN #DsHaiDau
            ON  #DsDanhSo.Thang = #DsHaiDau.Thang
       INNER JOIN #DsXuatHD
            ON  #DsDanhSo.Thang = #DsXuatHD.Thang
       INNER JOIN #DsThucChay
            ON  #DsDanhSo.Thang = #DsThucChay.Thang
       INNER JOIN #DsTienVe
            ON  #DsDanhSo.Thang = #DsTienVe.Thang
       INNER JOIN #DsDanhSoNamTruoc
            ON  #DsDanhSo.Thang = #DsDanhSoNamTruoc.Thang
       INNER JOIN #DsHaiDauNamTruoc
            ON  #DsDanhSo.Thang = #DsHaiDauNamTruoc.Thang
       INNER JOIN #DsThucChayNamTruoc
            ON  #DsDanhSo.Thang = #DsThucChayNamTruoc.Thang
       INNER JOIN #DsXuatHDNamTruoc
            ON  #DsDanhSo.Thang = #DsXuatHDNamTruoc.Thang
       INNER JOIN #DsTienVeNamTruoc
            ON  #DsDanhSo.Thang = #DsTienVeNamTruoc.Thang	
		
	DROP TABLE #DsDanhSo
       DROP TABLE #DsHaiDau
       DROP TABLE #DsXuatHD
       DROP TABLE #DsThucChay
       DROP TABLE #DsTienVe
	   DROP TABLE #DsDanhSoNamTruoc
       DROP TABLE #DsHaiDauNamTruoc
       DROP TABLE #DsThucChayNamTruoc
       DROP TABLE #DsXuatHDNamTruoc
       DROP TABLE #DsTienVeNamTruoc
       DROP TABLE #ThongTinChiTieu
END

```
