# Stored Procedure: `KSTC_CheckHopDongAndThucTreo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-08 16:52:58.877000
- **Ngày sửa cuối**: 2014-12-08 16:52:58.877000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE dbo.KSTC_CheckHopDongAndThucTreo 
	-- Add the parameters for the stored procedure here
	@DmSanPhamREF INT 
AS
BEGIN
	SELECT dbo.GetSoHopDongByID(b.HopDongFK) SoHopDong, a.*,b.*
	FROM (
	SELECT distinct HopDongREF, tchdct.HopDongChiTietREF
	FROM ThucChayHopDongChiTiet tchdct 
	WHERE tchdct.DeletedStatus <> 1 
	AND tchdct.HopDongChiTietREF IN (SELECT HopDongChiTietID FROM HopDongChiTiet 
	                                 WHERE DmSanPhamREF = @DmSanPhamREF AND DeletedStatus <> 1)
	AND tchdct.HopDongREF IN (SELECT HopDongID FROM HopDong WHERE TrangThaiHopDong <> 3)
	)a
	FULL OUTER JOIN
	(
	SELECT HopDongFK , HopDongChiTietID, hdct.DonViTinhREF, hdct.DonViTinh
	FROM HopDongChiTiet hdct
	WHERE hdct.DmSanPhamREF = @DmSanPhamREF AND hdct.DeletedStatus <> 1

	)b
	ON (a.HopDongREF = b.HopDongFK
	AND a.HopDongChiTietREF = b.HopDongChiTietID
	)
	WHERE (--a.HopDongREF IS NULL OR 
	b.HopDongFK IS NULL
	--OR a.HopDongChiTietREF IS NULL
	--OR b.HopDongChiTietID IS NULL
	)

	ORDER BY a.HopDongREF, a.HopDongChiTietREF, b.HopDongFK, b.HopDongChiTietID

END

```
