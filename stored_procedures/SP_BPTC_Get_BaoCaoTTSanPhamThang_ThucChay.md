# Stored Procedure: `BPTC_Get_BaoCaoTTSanPhamThang_ThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:52.473000
- **Ngày sửa cuối**: 2015-06-11 18:17:52.473000

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
CREATE PROCEDURE [dbo].[BPTC_Get_BaoCaoTTSanPhamThang_ThucChay]
@NgayBatDau DATETIME,
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
-- Doanh số đánh số
 SELECT tcdt.DmSanPhamREF,
	MONTH(tcdt.NgayThucHien) Thang,
       0 DsDanhSo,
       0 DsDanhSoNamTruoc,
       SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0)) DsThucChay ,
       0 DsThucChayNamTruoc,
       0 CTThucChay,
       0 CTDanhSo
FROM   ThucChayDaTinh tcdt INNER JOIN HopDong hd ON hd.HopDongID=tcdt.HopDongID
WHERE   tcdt.NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
		and tcdt.TrangThaiHopDong <> 3
		and hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
		AND hd.TrangThaiHopDong<>3
		AND hd.DeletedStatus=0
		
GROUP BY
       tcdt.DmSanPhamREF,MONTH(tcdt.NgayThucHien)      
 UNION ALL     
--Doanh so thuc chay nam truoc
SELECT tcdt.DmSanPhamREF,
	MONTH(tcdt.NgayThucHien),
       0,
       0,
       0,
       SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0)) DsThucChayNamTruoc,
       0,
       0
FROM   ThucChayDaTinh tcdt INNER JOIN HopDong hd ON hd.HopDongID=tcdt.HopDongID
WHERE   YEAR(tcdt.NgayThucHien) = YEAR(@NgayKetThuc) -1
		AND MONTH(tcdt.NgayThucHien) <= MONTH(@NgayKetThuc)
		and tcdt.TrangThaiHopDong <> 3
		and hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
		AND hd.TrangThaiHopDong<>3
		AND hd.DeletedStatus=0
		
GROUP BY
       tcdt.DmSanPhamREF,MONTH(tcdt.NgayThucHien)
UNION ALL
-- Chi tieu Thuc chay
SELECT ttct.DmChiTieuBoPhanREF,
		MONTH(ttct.ThoiGianKetThuc),
       0,
       0,
       0,
       0,
       SUM(ISNULL(DoanhSoChiTieu,0)) CTThucChay,
       0
FROM   ThongTinChiTieu ttct
WHERE  YEAR(ttct.ThoiGianKetThuc) = YEAR(@NgayKetThuc)
       AND MONTH(ttct.ThoiGianKetThuc) <= MONTH(@NgayKetThuc)
	   and ttct.LevelChiTieu = 1
       AND ttct.LoaiTien = 1
       
GROUP BY
       ttct.DmChiTieuBoPhanREF,MONTH(ttct.ThoiGianKetThuc)

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
       
INSERT INTO BPTC_BaoCaoTTSanPhamThang_ThucChay
       (
       [BPTC_BaoCaoTTSanPhamThangREF]
      ,[TenBaoCao]
      ,[ThoiGian]
      ,[DoanhSoNamTruoc]
      ,[ChiTieuHienTai]
      ,[DoanhSoHienTai]
      ,[TiLeTTCungKy]
      ,[TiLeHTChiTieu]
      ,[NoiDungDanhGia]
      ,[CreatedBy]
      ,[CreatedAt]
      ,[LastModifiedBy]
      ,[LastModifiedAt]
      ,[DeleteStatus]
      ,[PrintStatus]
      ,[RecordStatus]
      )

SELECT 
@BaoCaoTTSanPhamThangID,
@TenBaoCao,
#Temp2.Thang,
#Temp2.DsThucChayNamTruoc,
#Temp2.CTThucChay,
#Temp2.DsThucChay,
(CASE WHEN DsThucChayNamTruoc =0 THEN 0 ELSE  #Temp2.DsThucChay/#Temp2.DsThucChayNamTruoc-1 END)*100 ,
(Case when CTThucChay=0 then 0 else #Temp2.DsThucChay/#Temp2.CTThucChay END)*100 ,
NULL,
NULL,
GETDATE(),
NULL,
GETDATE(),
0,
0,
0

FROM   #Temp2

DROP TABLE #Temp
DROP TABLE #Temp2
END

```
