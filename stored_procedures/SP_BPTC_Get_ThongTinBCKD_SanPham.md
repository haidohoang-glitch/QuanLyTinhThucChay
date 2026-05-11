# Stored Procedure: `BPTC_Get_ThongTinBCKD_SanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:51.970000
- **Ngày sửa cuối**: 2015-06-11 18:17:51.970000

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
CREATE PROCEDURE [dbo].[BPTC_Get_ThongTinBCKD_SanPham]
		@NgayBatDau   DATETIME,
        @NgayKetThuc  DATETIME,
        @ThongTinBCKDID INT,
        @TenBaoCao NVARCHAR(200)
AS
BEGIN
	
	SELECT A.DmSanPhamREF,SUM(DsDanhSo)*1.1 DsDanhSo,SUM(DsDanhSoNamTruoc)*1.1 DsDanhSoNamTruoc,SUM(DsThucChay)*1.1 DsThucChay,SUM(DsThucChayNamTruoc)*1.1 DsThucChayNamTruoc, SUM(CTThucChay) CTThucChay
INTO #Temp
FROM (

SELECT hdct.DmSanPhamREF,
       SUM(hdct.ThanhTien) DsDanhSo,
       0 DsDanhSoNamTruoc,
       0 DsThucChay,
       0 DsThucChayNamTruoc,
       0 CTThucChay
FROM   HopDongChiTiet hdct
       INNER JOIN HopDong hd
            ON  hdct.HopDongFK = hd.HopDongID
WHERE  (hd.NgayDanhSoHopDong) BETWEEN @NgayBatDau AND @NgayKetThuc
       AND hd.TrangThaiHopDong <> 3
       AND hd.DeletedStatus = 0
       AND hdct.DeletedStatus = 0
       AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
GROUP BY
       hdct.DmSanPhamREF
UNION ALL
SELECT hdct.DmSanPhamREF,
       0,
       SUM(hdct.ThanhTien) DsDanhSo,
       0,
       0,
       0
FROM   HopDongChiTiet hdct
       INNER JOIN HopDong hd
            ON  hdct.HopDongFK = hd.HopDongID
WHERE  (
           YEAR(hd.NgayDanhSoHopDong) = YEAR(@NgayKetThuc) -1
           AND MONTH(hd.NgayDanhSoHopDong) <= MONTH(@NgayKetThuc)
       )
       AND hd.TrangThaiHopDong <> 3
       AND hd.DeletedStatus = 0
       AND hdct.DeletedStatus = 0
       AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
GROUP BY
       hdct.DmSanPhamREF
UNION ALL
SELECT tcdt.DmSanPhamREF,
       0,
       0,
       SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) ThucChay,
       0,
       0
FROM   ThucChayDaTinh tcdt
WHERE  tcdt.TrangThaiHopDong <> 3
       AND tcdt.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
       AND tcdt.NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
GROUP BY
       tcdt.DmSanPhamREF
UNION ALL
SELECT tcdt.DmSanPhamREF,
       0,
       0,
       0,
       SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) ThucChay,
       0
FROM   ThucChayDaTinh tcdt
WHERE  tcdt.TrangThaiHopDong <> 3
       AND tcdt.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
       AND YEAR(tcdt.NgayThucHien) = YEAR(@NgayKetThuc) -1
       AND MONTH(tcdt.NgayThucHien) <= MONTH(@NgayKetThuc)
GROUP BY
       tcdt.DmSanPhamREF
UNION ALL
SELECT ttct.DmChiTieuBoPhanREF,
       0,
       0,
       0,
       0,
       SUM(DoanhSoChiTieu) CTThucChay
FROM   ThongTinChiTieu ttct
WHERE  ttct.LevelChiTieu = 1
       AND ttct.LoaiTien = 1
       AND ttct.DmChiTieuBoPhanREF<>0
       AND ttct.DeleteStatus=0
       AND YEAR(ttct.ThoiGianKetThuc) = YEAR(@NgayKetThuc)
       AND MONTH(ttct.ThoiGianKetThuc) <= MONTH(@NgayKetThuc)
GROUP BY
       ttct.DmChiTieuBoPhanREF
) A 
GROUP BY A.DmSanPhamREF
SELECT * INTO #Temp2 FROM (

SELECT dnspbc.TenNhomSanPhamBaoCao,SUM(DsDanhSo) DsDanhSo,SUM(DsDanhSoNamTruoc) DsDanhSoNamTruoc,SUM(DsThucChay) DsThucChay,SUM(DsThucChayNamTruoc) DsThucChayNamTruoc, SUM(CTThucChay) CTThucChay
  FROM #Temp INNER JOIN DmNhomSanPhamBaoCao dnspbc
ON #Temp.DmSanPhamREF=dnspbc.DmSanPhamREF
GROUP BY dnspbc.TenNhomSanPhamBaoCao

UNION ALL
SELECT 'SP Khac',SUM(DsDanhSo) DsDanhSo,SUM(DsDanhSoNamTruoc) DsDanhSoNamTruoc,SUM(DsThucChay) DsThucChay,SUM(DsThucChayNamTruoc) DsThucChayNamTruoc, SUM(CTThucChay) CTThucChay
  FROM #Temp
WHERE #Temp.DmSanPhamREF NOT IN (SELECT DISTINCT dnspbc.DmSanPhamREF
                                   FROM DmNhomSanPhamBaoCao dnspbc)

) B



-- Chèn dữ liệu vào bảng chi tiết	
	INSERT INTO BPTC_ThongTinBCKD_SanPham
(
	-- BPTC_ThongTinBCKD_SanPhamID -- this column value is auto-generated
	BPTC_ThongTinBCKDREF,
	TenBaoCaoKinhDoanh,
	TenSanPham,
	DoanhSoDanhSo,
	DoanhSoHaiDau,
	DoanhSoThucChay,
	ChiTieuThucChay,
	TangTruongDoanhSo,
	TangTruongThucChay,
	NoiDungDanhGia,
	CreatedBy,
	CreatedAt,
	LastModifiedBy,
	LastModifiedAt,
	DeleteStatus,
	PrintStatus,
	RecordStatus
)

SELECT * FROM (
SELECT 
	@ThongTinBCKDID a,
	@TenBaoCao b,
	A.TenNhomSanPhamBaoCao,
	A.DsDanhSo,
	0 TC,
	A.DsThucChay,
	A.CTThucChay,
	(CASE WHEN DsDanhSoNamTruoc=0 THEN 0 ELSE (DsDanhSo/DsDanhSoNamTruoc-1)*100 END ) c,
	(CASE WHEN DsThucChayNamTruoc=0 THEN 0 ELSE (DsThucChay/DsThucChayNamTruoc-1)*100 END) d,
	NULL e,
	NULL f,
	GETDATE() g,
	NULL h,
	GETDATE() i,
	0 j,
	0 k,
	0 l
FROM #Temp2 A

--- Chèn dữ liệu vào bảng tổng
UNION ALL
SELECT 
	@ThongTinBCKDID,
	@TenBaoCao,
	N'Tổng',
	SUM(A.DsDanhSo),
	0,
	SUM(A.DsThucChay),
	SUM(A.CTThucChay),
	(CASE WHEN SUM(DsDanhSoNamTruoc)=0 THEN 0 ELSE (SUM(DsDanhSo)/SUM(DsDanhSoNamTruoc)-1)*100 END ),
	(CASE WHEN SUM(DsThucChayNamTruoc)=0 THEN 0 ELSE (SUM(DsThucChay)/SUM(DsThucChayNamTruoc)-1)*100 END),
	NULL,
	NULL,
	GETDATE(),
	NULL,
	GETDATE(),
	0,
	0,
	0
FROM #Temp2 A     
) A
		DROP TABLE #Temp
		DROP TABLE #Temp2
END

```
