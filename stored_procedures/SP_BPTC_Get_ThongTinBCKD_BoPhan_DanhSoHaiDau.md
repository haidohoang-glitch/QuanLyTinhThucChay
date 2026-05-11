# Stored Procedure: `BPTC_Get_ThongTinBCKD_BoPhan_DanhSoHaiDau`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:52.310000
- **Ngày sửa cuối**: 2015-06-11 18:17:52.310000

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
-- Author:		ChungTN
-- Create date: 18-05-2015
-- Description:	BPTC_Get_ThongTinBCKD_BoPhan_DanhSoHaiDau
-- =============================================
CREATE PROCEDURE [dbo].[BPTC_Get_ThongTinBCKD_BoPhan_DanhSoHaiDau]
	@NgayBatDau DATETIME, 
	@NgayKetThuc DATETIME,
	@ThongTinBCKDID INT,
    @TenBaoCao NVARCHAR(100)
AS
BEGIN
	SELECT hd.DmPhongBanREF,SUM(hdct.ThanhTien)*1.1 DanhSo INTO #DanhSo
FROM HopDong hd INNER JOIN HopDongChiTiet hdct
ON hd.HopDongID=hdct.HopDongFK
WHERE (hd.NgayDanhSoHopDong) BETWEEN @NgayBatDau AND @NgayKetThuc
       AND hd.TrangThaiHopDong <> 3
       AND hd.DeletedStatus = 0
       AND hdct.DeletedStatus = 0
       AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
GROUP BY hd.DmPhongBanREF
       
    SELECT hd.DmPhongBanREF,SUM(hdct.ThanhTien)*1.1 HaiDau INTO #HaiDau
    FROM HopDong hd INNER JOIN HopDongChiTiet hdct
    ON hd.HopDongID=hdct.HopDongFK
    WHERE (hd.NgayDanhSoHopDong) BETWEEN @NgayBatDau AND @NgayKetThuc
          AND hd.TrangThaiHopDong <> 3
       AND hd.DeletedStatus = 0
       AND hdct.DeletedStatus = 0
       AND hd.IsBanCung=1
       AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
         GROUP BY hd.DmPhongBanREF
   
      SELECT hd.DmPhongBanREF,SUM(tthd.GiaTri) XuatHD INTO #XuatHD
      FROM HopDong hd INNER JOIN ThongTinHoaDon tthd
      ON hd.HopDongID=tthd.HopDongREF
      WHERE tthd.NgayXuatHoaDon BETWEEN @NgayBatDau AND @NgayKetThuc
      AND hd.TrangThaiHopDong <> 3
       AND hd.DeletedStatus = 0
       AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
         GROUP BY hd.DmPhongBanREF
         
         SELECT hd.DmPhongBanREF,SUM(tttv.GiaTri) TienVe INTO #TienVe
      FROM HopDong hd INNER JOIN ThongTinTienVe tttv
      ON hd.HopDongID=tttv.HopDongREF
      WHERE tttv.NgayThanhToan BETWEEN @NgayBatDau AND @NgayKetThuc
      AND hd.TrangThaiHopDong <> 3
       AND hd.DeletedStatus = 0
       AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
         GROUP BY hd.DmPhongBanREF
         
 SELECT A.DmPhongBanREF,SUM(a.ThanhTienTc)*1.1 ThanhTienTc INTO #ThucChay FROM
(
 SELECT tcdt.DmPhongBanREF, SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)ThanhTienTc
   FROM ThucChayDaTinh tcdt
 LEFT JOIN HopDong hd ON tcdt.HopDongID = hd.HopDongID
 WHERE 1=1
 and tcdt.TrangThaiHopDong <> 3
 AND ISNULL(hd.TrangThaiHopDong,0) <> 3
 AND (tcdt.NgayThucHien) BETWEEN @NgayBatDau AND @NgayKetThuc
 AND tcdt.DmSanPhamREF NOT IN (144,585,299,337,628)
 AND tcdt.TenMaHopDong NOT IN ('NB','SH','NBDT')
 GROUP BY  tcdt.DmPhongBanREF
 UNION
 SELECT tcdt.DmPhongBanREF, SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)ThanhTienTc 
 FROM ThucChayDaTinhAdmarket tcdt
 LEFT JOIN HopDong hd ON tcdt.HopDongID = hd.HopDongID
 WHERE 1=1
 and tcdt.TrangThaiHopDong <> 3
 AND ISNULL(hd.TrangThaiHopDong,0) <> 3
 AND (tcdt.NgayThucHien) BETWEEN @NgayBatDau AND @NgayKetThuc
 --AND tcdt.DmSanPhamREF NOT IN (144,585,299,337)
 AND tcdt.TenMaHopDong NOT IN ('NB','SH','NBDT')
 GROUP BY  tcdt.DmPhongBanREF
)A GROUP BY A.DmPhongBanREF
         
       SELECT B.*  into #DsHD FROM (
      SELECT dpb.TenPhongBan,SUM(A.DanhSo) DsDanhSo, SUM(A.HaiDau) DsHaiDau, SUM(A.XuatHD) DsXuatHD,SUM(A.TienVe) DsTienVe, SUM(A.ThucChay) DsThucChay
        FROM (
      SELECT *,0 HaiDau,0 XuatHD,0 TienVe,0 ThucChay FROM #DanhSo
      UNION
      SELECT #HaiDau.DmPhongBanREF,0,#HaiDau.HaiDau,0,0,0 FROM #HaiDau
      UNION
      SELECT #XuatHD.DmPhongBanREF,0,0,#XuatHD.XuatHD,0,0 FROM #XuatHD
      UNION
      SELECT #TienVe.DmPhongBanREF,0,0,0,#TienVe.TienVe,0 FROM #TienVe
      UNION
      SELECT #ThucChay.DmPhongBanREF,0,0,0,0, #ThucChay.ThanhTienTc FROM #ThucChay
      ) A 
      INNER JOIN DmPhongBan dpb ON A.DmPhongBanREF=dpb.DmPhongBanID
      WHERE dpb.DeletedStatus=0 AND dpb.DmPhongBanID IN (3, 10, 11, 7, 19, 5, 6)
      GROUP BY dpb.TenPhongBan
      
      UNION ALL
      SELECT 'BP Khac',SUM(A.DanhSo) DsDanhSo, SUM(A.HaiDau) DsHaiDau, SUM(A.XuatHD) DsXuatHD,SUM(A.TienVe) DsTienVe, SUM(A.ThucChay) DsThucChay
        FROM (
      SELECT *,0 HaiDau,0 XuatHD,0 TienVe,0 ThucChay FROM #DanhSo
      UNION
      SELECT #HaiDau.DmPhongBanREF,0,#HaiDau.HaiDau,0,0,0 FROM #HaiDau
      UNION
      SELECT #XuatHD.DmPhongBanREF,0,0,#XuatHD.XuatHD,0,0 FROM #XuatHD
      UNION
      SELECT #TienVe.DmPhongBanREF,0,0,0,#TienVe.TienVe,0 FROM #TienVe
      UNION
      SELECT #ThucChay.DmPhongBanREF,0,0,0,0, #ThucChay.ThanhTienTc FROM #ThucChay
      ) A 
      INNER JOIN DmPhongBan dpb ON A.DmPhongBanREF=dpb.DmPhongBanID
      WHERE dpb.DeletedStatus=0 AND dpb.DmPhongBanID NOT  IN (3, 10, 11, 7, 19, 5, 6)
       ) B
        
      
      
INSERT INTO BPTC_ThongTinBCKD_BoPhan_DanhSoHaiDau
(
	-- BPTC_ThongTinBCKD_BoPhan_DanhSoHaiDauID -- this column value is auto-generated
	BPTC_ThongTinBCKDREF,
	TenBaoCaoKinhDoanh,
	DmBoPhanREF,
	TenBoPhan,
	DoanhSoDanhSo,
	DoanhSoHaiDau,
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
	'',
	T.TenPhongBan,
	T.DsDanhSo,
	T.DsHaiDau,
	NULL,
	NULL,
	GETDATE(),
	NULL,
	GETDATE(),
	0,
	0,
	0
FROM #DsHD T
DROP TABLE #DanhSo
      DROP TABLE #HaiDau
      DROP TABLE #XuatHD
      DROP TABLE #TienVe
      DROP TABLE #ThucChay
      DROP TABLE #DsHD
END

```
