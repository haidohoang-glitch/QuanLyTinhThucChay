# Stored Procedure: `BPTC_Get_BaoCaoTTSanPhamThang_ThucChay_DanhSo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:52.423000
- **Ngày sửa cuối**: 2015-06-11 18:17:52.423000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `datetime(8)` | No |
| `@NgayKetThuc` | `datetime(8)` | No |
| `@BaoCaoTTSanPhamThangID` | `int(4)` | No |
| `@TenBaoCao` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
-- Mã sản phẩm---------------Tên Sản phẩm
--	1							Pr Solution
--	2							Balloon Ads
--	3							TVC Online
--	4							Mobile
--	5							Banner CPD
--	6							Box App
--	7							CPM
--	8							CPC
--	9							ADX
CREATE PROCEDURE [dbo].[BPTC_Get_BaoCaoTTSanPhamThang_ThucChay_DanhSo]
	-- Đặt thêm biến @NhapMaSanPham để lấy theo sản phẩm
	@NgayBatDau DATETIME ,
	@NgayKetThuc DATETIME,
	@BaoCaoTTSanPhamThangID INT,
	@TenBaoCao NVARCHAR(200)
AS
BEGIN
	DECLARE @NhomSanPhamBaoCaoID INT
	SELECT @NhomSanPhamBaoCaoID= NhomSanPhamBaoCaoID 
	FROM BPTC_BaoCaoTTSanPhamThang
	WHERE BPTC_BaoCaoTTSanPhamThangID = @BaoCaoTTSanPhamThangID
	
SELECT dnspbc.DmNhomSanPhamBaoCaoID,dnspbc.TenNhomSanPhamBaoCao,A.Thang,SUM(DsDanhSo)*1.1 DsDanhSo,SUM(A.DsDanhSoNamTruoc)*1.1 DsDanhSoNamTruoc,SUM(DsThucChay)*1.1 DsThucChay,SUM(DsThucChayNamTruoc)*1.1 DsThucChayNamTruoc,SUM(CTThucChay)CTThucChay,SUM(CTDanhSo)CTDanhSo 
INTO #Temp FROM (
-- Doanh so danh so
SELECT hdct.DmSanPhamREF,
	   MONTH(hd.NgayDanhSoHopDong) Thang,
       SUM(hdct.ThanhTien) DsDanhSo,
       0 DsDanhSoNamTruoc,
       0 DsThucChay,
       0 DsThucChayNamTruoc,
       0 CTThucChay,
       0 CTDanhSo
FROM   HopDongChiTiet hdct
       INNER JOIN HopDong hd
            ON  hdct.HopDongFK = hd.HopDongID
WHERE  (hd.NgayDanhSoHopDong) BETWEEN @NgayBatDau AND @NgayKetThuc
       AND hd.TrangThaiHopDong <> 3
       AND hd.DeletedStatus = 0
       AND hdct.DeletedStatus = 0
       AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
GROUP BY
       hdct.DmSanPhamREF,MONTH(hd.NgayDanhSoHopDong)
UNION
---- Tinh gia tri Ds Danh so nam truoc
--SELECT hdct.DmSanPhamREF,
--		MONTH(hd.NgayDanhSoHopDong),
--       0,
--       SUM(hdct.ThanhTien),
--       0,
--       0,
--       0,
--       0
--FROM   HopDongChiTiet hdct
--       INNER JOIN HopDong hd
--            ON  hdct.HopDongFK = hd.HopDongID
--WHERE  (
--           YEAR(hd.NgayDanhSoHopDong) = YEAR(@NgayKetThuc) -1
--           AND MONTH(hd.NgayDanhSoHopDong) <= MONTH(@NgayKetThuc)
--       )
--       AND hd.TrangThaiHopDong <> 3
--       AND hd.DeletedStatus = 0
--       AND hdct.DeletedStatus = 0
--       AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
--GROUP BY
--       hdct.DmSanPhamREF,MONTH(hd.NgayDanhSoHopDong)       
-- UNION
 --Tinh Doanh so thuc chay      
 SELECT tcdt.DmSanPhamREF,
	MONTH(tcdt.NgayThucHien),
       0,
       0,
       SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) ThucChay,
       0,
       0,
       0
FROM   ThucChayDaTinh tcdt INNER JOIN HopDong hd ON hd.HopDongID=tcdt.HopDongID
WHERE   tcdt.NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
		AND tcdt.TrangThaiHopDong <> 3
		and hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
		AND hd.TrangThaiHopDong<>3
		AND hd.DeletedStatus=0
		
GROUP BY
       tcdt.DmSanPhamREF,MONTH(tcdt.NgayThucHien)      
 --UNION      
--Doanh so thuc chay nam truoc
--SELECT tcdt.DmSanPhamREF,
--	MONTH(tcdt.NgayThucHien),
--       0,
--       0,
--       0,
--       SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) ThucChay,
--       0,
--       0
--FROM   ThucChayDaTinh tcdt INNER JOIN HopDong hd ON hd.HopDongID=tcdt.HopDongID
--WHERE  tcdt.TrangThaiHopDong <> 3
--		and hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
--		AND hd.TrangThaiHopDong<>3
--		AND hd.DeletedStatus=0
--		AND YEAR(tcdt.NgayThucHien) = YEAR(@NgayKetThuc) -1
--		AND MONTH(tcdt.NgayThucHien) <= MONTH(@NgayKetThuc)
--GROUP BY
--       tcdt.DmSanPhamREF,MONTH(tcdt.NgayThucHien)
--UNION
---- Chi tieu Thuc chay
--SELECT ttct.DmChiTieuBoPhanREF,
--		MONTH(ttct.ThoiGianKetThuc),
--       0,
--       0,
--       0,
--       0,
--       SUM(DoanhSoChiTieu) CTThucChay,
--       0
--FROM   ThongTinChiTieu ttct
--WHERE  ttct.LevelChiTieu = 1
--       AND ttct.LoaiTien = 1
--       AND YEAR(ttct.ThoiGianKetThuc) = YEAR(@NgayKetThuc)
--       AND MONTH(ttct.ThoiGianKetThuc) <= MONTH(@NgayKetThuc)
--GROUP BY
--       ttct.DmChiTieuBoPhanREF,MONTH(ttct.ThoiGianKetThuc)
--UNION
----ChiTieuDanhSo
--SELECT ttct.DmChiTieuBoPhanREF,
--		MONTH(ttct.ThoiGianKetThuc),
--       0,
--       0,
--       0,
--       0,
--       0,
--       SUM(DoanhSoChiTieu) CTThucChay
--FROM   ThongTinChiTieu ttct
--WHERE  ttct.LevelChiTieu = 1
--       AND ttct.LoaiTien = 2
--       AND YEAR(ttct.ThoiGianKetThuc) = YEAR(@NgayKetThuc)
--       AND MONTH(ttct.ThoiGianKetThuc) <= MONTH(@NgayKetThuc)
--GROUP BY
--       ttct.DmChiTieuBoPhanREF,MONTH(ttct.ThoiGianKetThuc)
) A INNER JOIN DmNhomSanPhamBaoCao dnspbc ON A.DmSanPhamREF=dnspbc.DmSanPhamREF
WHERE dnspbc.DmNhomSanPhamBaoCaoID=@NhomSanPhamBaoCaoID
GROUP BY dnspbc.DmNhomSanPhamBaoCaoID,dnspbc.TenNhomSanPhamBaoCao,A.Thang
ORDER BY A.Thang
SELECT * INTO #Temp2 FROM
(
SELECT * FROM #Temp
UNION
SELECT #Temp.DmNhomSanPhamBaoCaoID,#Temp.TenNhomSanPhamBaoCao,13,SUM(DsDanhSo) DsDanhSo, SUM(DsDanhSoNamTruoc) DsDanhSoNamTruoc,SUM(DsThucChay) DsThucChay,SUM(DsThucChayNamTruoc) DsThucChayNamTruoc,SUM(CTThucChay)CTThucChay,SUM(CTDanhSo)CTDanhSo FROM #Temp
WHERE #Temp.Thang<=MONTH(@NgayKetThuc)
GROUP BY #Temp.TenNhomSanPhamBaoCao,#Temp.DmNhomSanPhamBaoCaoID
) B

INSERT INTO BPTC_BaoCaoTTSanPhamThang_ThucChay_DanhSo
(
	-- BPTC_BaoCaoTTSanPhamThang_ThucChay_DanhSoID -- this column value is auto-generated
	BPTC_BaoCaoTTSanPhamThangREF,
	DmSanPhamREF,
	TenBaoCao,
	ThoiGian,
	DoanhSoDanhSo,
	DoanhSoThucChay,
	TiLeThucChay_DanhSo,
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
	@BaoCaoTTSanPhamThangID,
	#Temp2.DmNhomSanPhamBaoCaoID,
	@TenBaoCao,
	#Temp2.Thang,
	#Temp2.DsDanhSo,
	#Temp2.DsThucChay,
	Case when DsDanhSo=0 then 0 else #Temp2.DsThucChay/#Temp2.DsDanhSo*100 END,
	NULL,
	NULL,
	GETDATE(),
	NULL,
	GETDATE(),
	0,
	0,
	0
 FROM #Temp2
DROP TABLE #Temp
DROP TABLE #Temp2
END

```
