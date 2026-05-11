# Stored Procedure: `KSTC_KiemSoatThucChayDaTinhPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-09 16:42:30.487000
- **Ngày sửa cuối**: 2014-12-09 16:47:40.163000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE dbo.KSTC_KiemSoatThucChayDaTinhPR 
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME, 
	@DmSanPhamREF INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
    IF @DmSanPhamREF = 141
    BEGIN
    	SELECT a.*, b.* FROM (
		SELECT tchdct.HopDongREF, tchdct.HopDongChiTietREF, sum((100 - hdct.ChietKhau)/100 * tchdct.GiaTien)TT
		  FROM ThucChayHopDongChiTietPR tchdct 
		  INNER JOIN HopDongChiTiet hdct ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
		WHERE (CONVERT(date,tchdct.CreatedAt) = @NgayThucHien	
		OR CONVERT(date,tchdct.LastModifiedAt) = @NgayThucHien)
		AND tchdct.ThoiGianBatDau >= '2013-01-01'
		AND tchdct.DeletedStatus <> 1
		AND hdct.DeletedStatus <> 1
		AND hdct.HopDongFK IN (SELECT HopDongID FROM HopDong WHERE HopDong.TrangThaiHopDong <> 3)
		GROUP BY tchdct.HopDongREF, tchdct.HopDongChiTietREF
		)a
		FULL OUTER JOIN
		(
			SELECT tcdt.HopDongID, tcdt.HopDongChiTietREF, 
			SUM(tcdt.ThanhTienSauTrietKhauThucChay+GiaTriThayDoi) TCDT
			FROM ThucChayDaTinh tcdt 
			WHERE tcdt.NgayThucHien <=@NgayThucHien
			GROUP BY tcdt.HopDongID, tcdt.HopDongChiTietREF
			)b
		ON a.HopDongREF = b.HopDongID
		AND a.HopDongChiTietREF = b.HopDongChiTietREF
    	WHERE a.TT <> b.TCDT
    END
    ELSE
	 BEGIN
    	SELECT a.*, b.* FROM (
		SELECT tchdct.HopDongREF, tchdct.HopDongChiTietREF, sum((100 - hdct.ChietKhau)/100 * hdct.DonGia)TT
		  FROM ThucChayHopDongChiTiet tchdct 
		  INNER JOIN HopDongChiTiet hdct ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
		WHERE (CONVERT(date,tchdct.CreatedAt) = @NgayThucHien	
		OR CONVERT(date,tchdct.LastModifiedAt) = @NgayThucHien)
		AND tchdct.DmSanPhamREF IN (251, 252, 253, 535, 537, 538, 539 , 540, 541, 542, 555, 556, 557, 558, 559, 560, 561)
		AND tchdct.ThoiGianBatDau >= '2013-01-01'
		AND tchdct.DeletedStatus <> 1
		AND hdct.DeletedStatus <> 1
		AND hdct.HopDongFK IN (SELECT HopDongID FROM HopDong WHERE HopDong.TrangThaiHopDong <> 3)
		AND hdct.HopDongFK NOT IN (SELECT HopDongFK FROM hopdongchitiet WHERE hdct.DmSanPhamREF IN (306,423))
		GROUP BY tchdct.HopDongREF, tchdct.HopDongChiTietREF
		)a
		FULL OUTER JOIN
		(
			SELECT tcdt.HopDongID, tcdt.HopDongChiTietREF, 
			SUM(tcdt.ThanhTienSauTrietKhauThucChay+GiaTriThayDoi) TCDT
			FROM ThucChayDaTinh tcdt 
			WHERE tcdt.NgayThucHien <=@NgayThucHien
			GROUP BY tcdt.HopDongID, tcdt.HopDongChiTietREF
			)b
		ON a.HopDongREF = b.HopDongID
		AND a.HopDongChiTietREF = b.HopDongChiTietREF
    	WHERE a.TT <> b.TCDT
    END
END

```
