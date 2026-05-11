# Stored Procedure: `KiemTra_DauVao_CPM_DVTKhacCPMCPC`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-18 10:16:48.393000
- **Ngày sửa cuối**: 2016-11-24 15:15:28.797000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[KiemTra_DauVao_CPM_DVTKhacCPMCPC]
	-- Add the parameters for the stored procedure here
	--Check đơn vị tính của sản phẩm CPM khác CPC, CPM

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT hdct.DmSanPhamREF, hdct.TenSanPham, HopDongFK, 
	hd.SoHopDong, TenLoai, hdct.DonViTinh, ThanhTien, hdct.ThanhtienThucChay,(ThanhTien- hdct.ThanhtienThucChay) lech,
	 hdct.TenLoaiNenTang,hdct.DmLoaiBannerREF, hdct.TenLoaiBanner, hdct.GhiChu
 FROM dbo.HopDong hd INNER JOIN hopdongchitiet hdct
ON hd.HopDongID = hdct.HopDongFK
 WHERE DonViTinh NOT in ('CPC','CPM') AND hdct.DmSanPhamREF IN (339,240,370,598,613,342,680)
AND hdct.DeletedStatus = 0 AND hd.Nam>=2014 AND ROUND(hdct.ThanhTien,0) <> ROUND(hdct.ThanhTienThucChay,0)
AND hd.TrangThaiHopDong <> 3
AND NOT ((hdct.ThanhTien = 0) )
ORDER BY  hdct.DonViTinh, hdct.DmSanPhamREF, hd.HopDongID






END

```
