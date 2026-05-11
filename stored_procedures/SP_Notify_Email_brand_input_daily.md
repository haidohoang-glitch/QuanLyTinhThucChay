# Stored Procedure: `Notify_Email_brand_input_daily`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-09 14:27:18.490000
- **Ngày sửa cuối**: 2021-03-20 10:56:57.987000

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
EXEC [dbo].[Notify_Email_brand_input_daily]
*/
CREATE PROCEDURE [dbo].[Notify_Email_brand_input_daily]
	
AS
BEGIN
	DECLARE @NgayThucHien DATETIME = GETDATE()
	SET @NgayThucHien = DATEADD(DAY,-1,CONVERT(DATE,@NgayThucHien)) 

	SELECT tt.NgayThucHien, hd.SoHopDong, tt.HopDongChiTietID, tt.ThucChayHopDongChiTietID, tt.TenSanPham,tt.DmNhanHangID, tt.TenNhanHang, tt.LoaiVanDe 
	, tt.TenLoaiVanDe, ISNULL(e.ListEmail,'tuyetnguyenthianh@admicro.vn, asd_thucchay@admicro.vn, haidohoang@admicro.vn,thuphamanh@admicro.vn,chungtranngoc@admicro.vn, phuongledanh@admicro.vn') [To],'' CC
	FROM dbo.ThongTinCanhBaoNhanHang tt
	INNER JOIN dbo.HopDong hd ON tt.HopDongID = hd.HopDongID
	LEFT JOIN [dbo].[ConfigEmailNotify] e ON e.LoaiVanDeID = tt.LoaiVanDe
	where tt.NgayThucHien = @NgayThucHien
	AND hd.TenMaHopDong NOT IN ('HT','TH')
	and tt.DmHinhThucQuangCaoID <> 42 --haidh 2021-03-20 comment khong check nhan tren thuc treo vi nhan hang khi tinh la thong tin hopdongchitiet
	ORDER BY tt.LoaiVanDe


END


```
