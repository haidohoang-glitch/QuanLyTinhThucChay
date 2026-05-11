# Stored Procedure: `KiemTraVuotGiaTriHopDongCPD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-14 16:50:35.253000
- **Ngày sửa cuối**: 2017-02-14 16:50:35.253000

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
CREATE PROCEDURE KiemTraVuotGiaTriHopDongCPD 
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

   SELECT TC.*, HD.ThanhTien, TC.TienChay - HD.ThanhTien FROM
(
	SELECT tcdt.HopDongID, tcdt.SoHopDong, tcdt.DmSanPhamREF
		, ROUND(SUM(tcdt.ThanhTienSauTrietKhauThucChay+ tcdt.GiaTriThayDoi),0) AS TienChay
	FROM ThucChayDaTinh tcdt WHERE tcdt.DmSanPhamREF IN 
	--(241,242,264,300,268,248,270,243,244,249,385) 
	(140,228,241,564,549)
		AND tcdt.NgayThucHien = @NgayThucHien
	GROUP BY  tcdt.HopDongID, tcdt.SoHopDong, tcdt.DmSanPhamREF
) TC LEFT JOIN 
(
SELECT hd.HopDongID, hd.SoHopDong, hdct.DmSanPhamREF, SUM(hdct.ThanhTien) ThanhTien
FROM HopDong hd INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK AND hd.TrangThaiHopDong <> 3 AND hdct.DeletedStatus = 0
GROUP BY hd.HopDongID, hd.SoHopDong, hdct.DmSanPhamREF
) HD ON HD.HopDongID = TC.HopDongID AND HD.DmSanPhamREF = TC.DmSanPhamREF
WHERE TC.TienChay - HD.ThanhTien > 2
END

```
