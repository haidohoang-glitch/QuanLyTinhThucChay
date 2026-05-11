# Stored Procedure: `BPTC_Get_ThongTinBCKD_XuatHoaDon_Nam`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:51.110000
- **Ngày sửa cuối**: 2015-06-11 18:17:51.110000

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
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[BPTC_Get_ThongTinBCKD_XuatHoaDon_Nam]
		@NgayBatDau DATETIME,
		@NgayKetThuc DATETIME,
		@ThongTinBCKDID  INT,
		@TenBaoCao       NVARCHAR(100)
AS
BEGIN
	DECLARE  @NamXuatHD INT=YEAR (@NgayKetThuc)
	
SELECT * INTO #Temp FROM (                  
SELECT		YEAR(hd.NgayDanhSoHopDong) Nam_ThangDanhSoHopDong,MONTH(tthd.NgayXuatHoaDon) ThangXuatHoaDon,SUM(tthd.GiaTri) TienXuatHD,1 TTHT FROM ThongTinHoaDon tthd INNER JOIN HopDong hd ON tthd.HopDongREF=hd.HopDongID
WHERE		YEAR(hd.NgayDanhSoHopDong)=@NamXuatHD-2
			AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
			AND hd.DeletedStatus=0 AND hd.TrangThaiHopDong<>3
			AND tthd.DeletedStatus=0
			AND (tthd.NgayXuatHoaDon) BETWEEN @NgayBatDau AND @NgayKetThuc
GROUP BY	YEAR(hd.NgayDanhSoHopDong),MONTH(tthd.NgayXuatHoaDon)
UNION ALL
SELECT		YEAR(hd.NgayDanhSoHopDong) NamDanhSoHopDong,MONTH(tthd.NgayXuatHoaDon) ThangXuatHoaDon,SUM(tthd.GiaTri),2 FROM ThongTinHoaDon tthd INNER JOIN HopDong hd ON tthd.HopDongREF=hd.HopDongID
WHERE		YEAR(hd.NgayDanhSoHopDong)=@NamXuatHD-1
			AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
			AND hd.DeletedStatus=0 AND hd.TrangThaiHopDong<>3
			AND tthd.DeletedStatus=0
			AND (tthd.NgayXuatHoaDon) BETWEEN @NgayBatDau AND @NgayKetThuc
GROUP BY	YEAR(hd.NgayDanhSoHopDong),MONTH(tthd.NgayXuatHoaDon)
UNION ALL
SELECT		MONTH(hd.NgayDanhSoHopDong) NamDanhSoHopDong,MONTH(tthd.NgayXuatHoaDon) ThangXuatHoaDon,SUM(tthd.GiaTri),3 FROM ThongTinHoaDon tthd INNER JOIN HopDong hd ON tthd.HopDongREF=hd.HopDongID
WHERE		(hd.NgayDanhSoHopDong) BETWEEN @NgayBatDau AND @NgayKetThuc
			AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
			AND hd.DeletedStatus=0 AND hd.TrangThaiHopDong<>3
			AND tthd.DeletedStatus=0
			AND (tthd.NgayXuatHoaDon) BETWEEN @NgayBatDau AND @NgayKetThuc
GROUP BY	MONTH(hd.NgayDanhSoHopDong),MONTH(tthd.NgayXuatHoaDon)
) A  

DECLARE @BPTC_BaoCaoXuatHoaDonNam TABLE 
	(
	[Thang] [int] NULL,
	[NamBaoCaoHT_Thang1] [numeric](20, 5) NULL,
	[NamBaoCaoHT_Thang2] [numeric](20, 5) NULL,
	[NamBaoCaoHT_Thang3] [numeric](20, 5) NULL,
	[NamBaoCaoHT_Thang4] [numeric](20, 5) NULL,
	[NamBaoCaoHT_Thang5] [numeric](20, 5) NULL,
	[NamBaoCaoHT_Thang6] [numeric](20, 5) NULL,
	[NamBaoCaoHT_Thang7] [numeric](20, 5) NULL,
	[NamBaoCaoHT_Thang8] [numeric](20, 5) NULL,
	[NamBaoCaoHT_Thang9] [numeric](20, 5) NULL,
	[NamBaoCaoHT_Thang10] [numeric](20, 5) NULL,
	[NamBaoCaoHT_Thang11] [numeric](20, 5) NULL,
	[NamBaoCaoHT_Thang12] [numeric](20, 5) NULL
	)
	INSERT INTO @BPTC_BaoCaoXuatHoaDonNam
	SELECT 
		Nam_ThangDanhSoHopDong,
       ISNULL([1], 0),
       ISNULL([2], 0),
       ISNULL([3], 0),
       ISNULL([4], 0),
       ISNULL([5], 0),
       ISNULL([6], 0),
       ISNULL([7], 0),
       ISNULL([8], 0),
       ISNULL([9], 0),
       ISNULL([10], 0),
       ISNULL([11], 0),
       ISNULL([12], 0)
FROM   #Temp 
       PIVOT(
           SUM(TienXuatHD) FOR ThangXuatHoaDon IN ([1], [2], [3], [4], 
                                                           [5], [6], [7], [8], 
                                                           [9], [10], [11], [12])
       ) Temp          
DROP TABLE #Temp  
INSERT INTO BPTC_ThongTinBCKD_XuatHoaDon_Nam
(
	-- BPTC_ThongTinBCKD_XuatHoaDon_NamID -- this column value is auto-generated
	BPTC_ThongTinBCKDREF,
	TenBaoCaoKinhDoanh,
	Thang,
	NamBaoCaoHT_Thang1,
	NamBaoCaoHT_Thang2,
	NamBaoCaoHT_Thang3,
	NamBaoCaoHT_Thang4,
	NamBaoCaoHT_Thang5,
	NamBaoCaoHT_Thang6,
	NamBaoCaoHT_Thang7,
	NamBaoCaoHT_Thang8,
	NamBaoCaoHT_Thang9,
	NamBaoCaoHT_Thang10,
	NamBaoCaoHT_Thang11,
	NamBaoCaoHT_Thang12,
	NoiDungDanhGia,
	CreatedBy,
	CreatedAt,
	LastModifiedBy,
	LastModifiedAt,
	DeleteStatus,
	PrintStatus,
	RecordStatus
)
 
SELECT @ThongTinBCKDID,@TenBaoCao,*,NULL,NULL,GETDATE(),NULL,GETDATE(),0,0,0 from @BPTC_BaoCaoXuatHoaDonNam

END

```
