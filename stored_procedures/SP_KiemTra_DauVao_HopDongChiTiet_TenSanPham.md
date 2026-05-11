# Stored Procedure: `KiemTra_DauVao_HopDongChiTiet_TenSanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-21 17:28:10.257000
- **Ngày sửa cuối**: 2016-11-23 15:45:03.630000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThoiGian` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXeC [dbo].[KiemTra_DauVao_HopDongChiTiet_TenSanPham] '2016-01-01'
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDongChiTiet_TenSanPham]
	-- Add the parameters for the stored procedure here
	@ThoiGian DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT HopDongFK, HopDongChiTietID,DmSanPhamREF, TenSanPham,CreatedAt, LastModifiedAt FROM ABM_Data_ThucChay.dbo.hopdongchitiet 
	WHERE CONVERT(DATE,LastModifiedAt) >=@ThoiGian
	AND DeletedStatus = 0
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongFK, HopDongChiTietID,DmSanPhamREF,TenSanPham,CreatedAt, LastModifiedAt FROM HopDongChiTietSyn
	)B
	ON A.HopDongChiTietID =B.HopDongChiTietID
	AND A.DmSanPhamREF = B.DmSanPhamREF
	where A.TenSanPham <> B.TenSanPham
	--WHERE A.HopDongChiTietID IS NULL OR B.HopDongChiTietID IS NULL OR A.TenSanPham IS NULL OR B.TenSanPham IS NULL
    ORDER BY A.HopDongChiTietID
END

```
