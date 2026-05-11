# Stored Procedure: `BPTC_Get_ThongTinBCKD_Huy_ThayDoi_HopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:51.010000
- **Ngày sửa cuối**: 2015-06-11 18:17:51.010000

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
CREATE PROCEDURE [dbo].[BPTC_Get_ThongTinBCKD_Huy_ThayDoi_HopDong]
	@NgayBatDau DATETIME ,
	@NgayKetThuc DATETIME,
	@ThongTinBCKDID INT,
	@TenBaoCao NVARCHAR(200)
AS
BEGIN
DECLARE @Tabl_HopDongHuy TABLE (HopDongID INT,NgayHuy DATETIME,HopDongThayDoiID INT )
INSERT INTO @Tabl_HopDongHuy
SELECT hdtd.HopDongFK, MAX(hdtd.NgayThayDoi),max(hdtd.HopDongThayDoiID) FROM HopDongThayDoi hdtd
WHERE hdtd.NgayThayDoi BETWEEN @NgayBatDau AND @NgayKetThuc
AND hdtd.LoaiThayDoi=0
GROUP BY hdtd.HopDongFK,MONTH(hdtd.NgayThayDoi)

-- Lay gia tri huy danh so
SELECT hd.SoHopDong,hd.TenNhanVien,hd.TenPhongBan,hd.NhanHopDong,(-hd.GiaTriHopDong) GiaTriHuy INTO #GiaTriHuy
  FROM @Tabl_HopDongHuy tttd INNER JOIN HopDong hd ON tttd.HopDongID=hd.HopDongID
WHERE hd.TrangThaiHopDong=3 AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
AND hd.IsBanCung=1-- La hop dong hai dau
AND hd.DeletedStatus=0
AND hd.NgayDanhSoHopDong BETWEEN @NgayBatDau AND @NgayKetThuc


DECLARE @Tabl_HopDongThayDoi TABLE (HopDongID INT,NgayThayDoi DATETIME,HopDongThayDoiID INT )
INSERT INTO @Tabl_HopDongThayDoi
SELECT hdtd.HopDongFK, MAX(hdtd.NgayThayDoi),max(hdtd.HopDongThayDoiID) FROM HopDongThayDoi hdtd
WHERE hdtd.NgayThayDoi BETWEEN @NgayBatDau AND @NgayKetThuc
AND hdtd.LoaiThayDoi=1
GROUP BY hdtd.HopDongFK,MONTH(hdtd.NgayThayDoi)

-- Gia Tri thay doi hop dong danh so
SELECT  hd.SoHopDong,hd.TenNhanVien,hd.TenPhongBan,hd.NhanHopDong,(hd.GiaTriHopDong)- (hdtd.GiaTriHopDong) GiaTriHopDongTD INTO #GiaTriThayDoi
  FROM @Tabl_HopDongThayDoi tttd 
  INNER JOIN HopDong hd ON tttd.HopDongID=hd.HopDongID
  INNER JOIN HopDongThayDoi hdtd ON hdtd.HopDongThayDoiID=tttd.HopDongThayDoiID
WHERE hd.TrangThaiHopDong<>3 AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
AND hd.IsBanCung=1-- Là hợp đồng hai dấu
AND hd.DeletedStatus=0
AND hd.NgayDanhSoHopDong BETWEEN @NgayBatDau AND @NgayKetThuc
INSERT INTO [dbo].[BPTC_ThongTinBCKD_Huy_ThayDoi_HopDong]
	  (
	    [BPTC_ThongTinBCKDREF],
	    [TenBaoCaoKinhDoanh],
	    [SoHopDong],
	    [HopDongREF],
	    [TenNhanVien],
	    [NhanVienREF],
	    [TenPhongBan],
	    [PhongBanREF],
	    [NhanHang_KhacHang],
	    [NhanHang_KhachHangREF],
	    [GiaTriHuyThayDoi],
	    [LyDoHuy],
	    [NoiDungDanhGia],
	    [CreatedBy],
	    [CreatedAt],
	    [LastModifiedBy],
	    [LastModifiedAt],
	    [DeleteStatus],
	    [PrintStatus],
	    [RecordStatus]
	  )
SELECT DISTINCT
	       @ThongTinBCKDID,
	       @TenBaoCao,
	       A.SoHopDong,
	       0,
	       A.TenNhanVien,
	       0,
	       A.TenPhongBan,
	       0,
	       A.NhanHopDong,
	       0,
	       A.GiaTriHopDongTD,
	       NULL,
	       NULL,
	       NULL,
	       GETDATE(),
	       NULL,
	       GETDATE(),
	       0,
	       0,
	       0
	       FROM (
SELECT * FROM #GiaTriThayDoi
UNION ALL
SELECT * FROM #GiaTriHuy
) A
WHERE A.GiaTriHopDongTD<=-300000000
ORDER BY A.GiaTriHopDongTD



DROP TABLE #GiaTriHuy
DROP TABLE #GiaTriThayDoi
END

```
