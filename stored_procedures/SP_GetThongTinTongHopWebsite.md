# Stored Procedure: `GetThongTinTongHopWebsite`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-12-11 11:33:34.587000
- **Ngày sửa cuối**: 2014-11-19 12:16:58.700000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[GetThongTinTongHopWebsite]
	-- Add the parameters for the stored procedure here

AS
BEGIN
	
SELECT 

hd.SoHopDong
,dlsp.TenLoaiSanPham
,hdct.TenSanPham
,isnull(tlpbw.Tag,'') AS TagName
,isnull(lower(tlpbw.Website),lower(dw.WebsiteLink)) AS Website
,hdct.ThanhTien AS ThanhTienPhanBo
,isnull(round(dbo.GetTyLePhanBoWebsite(tlpbw.DmSanPhamREF,tlpbw.TagID,tlpbw.Website,GETDATE())*100,2) ,100) AS 'TyLe%'
,isnull(
	round(hdct.ThanhTien * dbo.GetTyLePhanBoWebsite(tlpbw.DmSanPhamREF,tlpbw.TagID,tlpbw.Website,GETDATE()),0)
	,hdct.ThanhTien
) AS ThanhTien

FROM HopDongTongHop hd
INNER JOIN dbo.ThucChayTheoDoiHopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
INNER JOIN DmWebsite dw ON hdct.DmWebsiteREF = dw.DmWebsiteID
INNER JOIN DmLoaiSanPham dlsp ON hdct.DmLoaiREF = dlsp.DmLoaiSanPhamID
LEFT JOIN TyLePhanBoWebsite tlpbw ON hdct.DmNhomWebsiteREF = tlpbw.TagID AND hdct.DmSanPhamREF = tlpbw.DmSanPhamREF

WHERE
1=1
--AND tlpbw.Website IN (SELECT website FROM WebsiteAdmicro wa)
AND year(hd.NgayKyHopDong) > 2012
AND (dlsp.TenLoaiSanPham LIKE '%CPD%' 
OR dlsp.TenLoaiSanPham LIKE '%CPM%'
)
AND hd.SoHopDong = 'QC491213'
ORDER BY hd.NgayKyHopDong desc,hd.SoHopDong


END

```
