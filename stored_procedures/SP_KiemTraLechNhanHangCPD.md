# Stored Procedure: `KiemTraLechNhanHangCPD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-14 16:52:33.950000
- **Ngày sửa cuối**: 2017-02-14 16:52:33.950000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE KiemTraLechNhanHangCPD 
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    SELECT A.*, B.*
	  FROM
	  ( SELECT distinct HopDongREF, HopDongChiTietREF, DmNhanHangREF
	FROM dbo.ThucChayHopDongChiTiet tt
	WHERE DeletedStatus <> 1  
	)A
	 right join
	(SELECT  SoHopDong, HopDongID, HopDongChiTietREF, NhanHang, DmSanPhamREF, Tensanpham, SUM(ThanhtienSautrietkhauthucchay+Giatrithaydoi)tc
	FROM ThucChayDaTinh
	
	WHERE DmSanPhamREF IN --(370,339,240,613,598,342,680)
	(140,549,228,385) 
	AND HopDongChiTietREF  IN  (SELECT A.HopDongChiTietREF FROM (SELECT HopDongChiTietREF, COUNT(DISTINCT DmNhanHangREF) nhan, MAX(LastModifiedAt)tg 
														FROM dbo.ThucChayHopDongChiTiet
													 WHERE 1=1  
													 GROUP BY HopDongChiTietREF)A WHERE A.nhan = 1 AND tg >= '2016-04-01')
	
	AND TrangThaiHopDong <> 3
	AND NOT (DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18)
	AND Nam >=2014
	AND SoHopDong <> ('QC1420116')
	AND NgayThucHien = @NgayThucHien
	GROUP BY SoHopDong, HopDongID, HopDongChiTietREF, NhanHang, DmSanPhamREF, Tensanpham
	HAVING ROUND(SUM(ThanhtienSautrietkhauthucchay+Giatrithaydoi),0) <> 0
	)B
	
	ON A.HopDongREF =B.HopDongID
	AND A.HopDongChiTietREF =B.HopDongChiTietREF
	AND A.DmNhanHangREF = B.NhanHang
	WHERE-- A.HopDongChiTietREF = 89088 and 
	A.HopDongREF IS NULL OR A.HopDongChiTietREF IS NULL OR A.DmNhanHangREF IS NULL
	OR B.HopDongID IS NULL OR B.HopDongChiTietREF IS NULL OR B.NhanHang IS NULL

	ORDER BY B.HopDongChiTietREF
END

```
