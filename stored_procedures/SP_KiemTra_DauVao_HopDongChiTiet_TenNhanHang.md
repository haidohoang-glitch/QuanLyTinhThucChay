# Stored Procedure: `KiemTra_DauVao_HopDongChiTiet_TenNhanHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-21 17:27:48.900000
- **Ngày sửa cuối**: 2016-11-23 15:37:23.403000

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
--EXeC [dbo].[KiemTra_DauVao_HopDongChiTiet_TenNhanHang] '2016-01-01'
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDongChiTiet_TenNhanHang]
	-- Add the parameters for the stored procedure here
	@ThoiGian DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT HopDongChiTietID, NhanHang,CreatedAt,LastModifiedAt FROM ABM_Data_ThucChay.dbo.hopdongchitiet 
	WHERE CONVERT(DATE,LastModifiedAt) >=@ThoiGian
	AND DeletedStatus = 0
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongChiTietID,NhanHang,CreatedAt,LastModifiedAt FROM HopDongChiTietSyn
	)B
	ON A.HopDongChiTietID =B.HopDongChiTietID
	--AND A.NhanHang = B.NhanHang
	where A.NhanHang <> B.NhanHang
	--WHERE A.HopDongChiTietID IS NULL OR B.HopDongChiTietID IS NULL OR A.NhanHang IS NULL OR B.NhanHang IS NULL
    
END

```
