# Stored Procedure: `Notify_Email_Brand_Calc_Daily`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-10 10:00:58.973000
- **Ngày sửa cuối**: 2025-07-29 11:59:22.420000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC [dbo].[Notify_Email_Brand_Calc_Daily]
*/
CREATE PROCEDURE [dbo].[Notify_Email_Brand_Calc_Daily]

AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = DATEADD(DAY,-1,CONVERT(DATE,GETDATE())) 

	SELECT tt.NgayThucHien, hd.SoHopDong, tt.HopDongChiTietID, tt.ThucChayHopDongChiTietID, tt.TenSanPham,tt.DmNhanHangID, tt.TenNhanHang, tt.LoaiVanDe 
	, tt.TenLoaiVanDe, ISNULL(e.ListEmail,'asd_thucchay@admicro.vn, haidohoang@admicro.vn') [To],'' CC
	FROM dbo.ThongTinCanhBaoNhanHangHopDongChiTiet tt
	INNER JOIN dbo.HopDong hd ON tt.HopDongID = hd.HopDongID
	LEFT JOIN [dbo].[ConfigEmailNotify] e ON e.LoaiVanDeID = tt.LoaiVanDe
	where tt.NgayThucHien = @NgayThucHien
	AND hd.TenMaHopDong NOT IN ('HT','TH')
	AND hd.NgayDanhSoHopDong >= '2015-01-01'
	ORDER BY tt.LoaiVanDe


END

```
