# Stored Procedure: `BPTC_Get_ThongTinBCKD_XuatHoaDon_ThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:51.853000
- **Ngày sửa cuối**: 2015-06-11 18:17:51.853000

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
CREATE PROCEDURE [dbo].[BPTC_Get_ThongTinBCKD_XuatHoaDon_ThucChay]
	@NgayBatDau DATETIME ,
	@NgayKetThuc DATETIME ,
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
	                  AND hd.TrangThaiHopDong <> 3
	                  AND hd.DeletedStatus = 0
	                  AND hd.TenMaHopDong NOT IN ('NB','NBDT','SH','HT')
	                  AND tthd.DeletedStatus=0
	           GROUP BY
	                  MONTH(tthd.NgayXuatHoaDon)
	           UNION ALL
	           SELECT hdkshd.ThangXuat,
	                  SUM(hdkshd.GiaTri)
	           FROM   @HoaDonKhongSoHopDong hdkshd
	           WHERE  hdkshd.NamXuat = YEAR(@NgayKetThuc) --AND hdkshd.DeletedStatus=0
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

	
	INSERT INTO BPTC_ThongTinBCKD_XuatHoaDon_ThucChay
	  (
	    -- BPTC_ThongTinBCKD_XuatHoaDon -- this column value is auto-generated
	    [BPTC_ThongTinBCKDID],
	    [TenBaoCaoKinhDoanh],
	    [Thang],
	    [DoanhSoThucChay],
	    [DoanhSoHoaDon],
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
	       #DsXuatHD.Thang,
		   DsThucChay,
	       DsXuatHD,
	       NULL,
	       GETDATE(),
	       NULL,
	       GETDATE(),
	       NULL,
	       0,
	       0,
	       0
	FROM   #DsXuatHD
	       INNER JOIN #DsThucChay
	            ON  #DsThucChay.Thang = #DsXuatHD.Thang
	ORDER BY
	       Thang
	DROP TABLE #DsXuatHD
	DROP TABLE #DsThucChay
END

```
