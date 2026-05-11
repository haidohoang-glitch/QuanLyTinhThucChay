# Stored Procedure: `KiemTra_DauVao_Performancebase_TaiKhoanCoHonMotKhachHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-18 10:36:58.510000
- **Ngày sửa cuối**: 2016-11-18 10:36:58.510000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThoiGianBatDau` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE KiemTra_DauVao_Performancebase_TaiKhoanCoHonMotKhachHang
	-- Add the parameters for the stored procedure here
	--Check các tài khoản theo sản phẩm có > 1 khách hàng để xem sale có gán sai tài khoản không

	@ThoiGianBatDau DATETIME

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	
SELECT hdct.DmSanPhamREF, hdct.TenSanPham,  hdct.TK_AdMarket, COUNT(DISTINCT hd.TenKhachHang) sokhachhang
 FROM dbo.HopDong hd INNER JOIN hopdongchitiet hdct
ON hd.HopDongID = hdct.HopDongFK
 WHERE hdct.DmSanPhamREF IN (144,585,628)
AND hdct.DeletedStatus = 0 
AND hdct.TK_AdMarket <> ''
AND hd.TrangThaiHopDong <> 3
GROUP BY hdct.DmSanPhamREF, hdct.TenSanPham,  hdct.TK_AdMarket
HAVING COUNT(DISTINCT hd.TenKhachHang) > 1
ORDER BY hdct.DmSanPhamREF, hdct.TenSanPham



END

```
