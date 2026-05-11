# Stored Procedure: `KiemTra_DauVao_HopDongChiTiet_NhanHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-21 17:22:00.120000
- **Ngày sửa cuối**: 2016-11-23 16:19:52.213000

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
--EXeC  [dbo].[KiemTra_DauVao_HopDongChiTiet_NhanHang] '2016-01-01'
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDongChiTiet_NhanHang]
	-- Add the parameters for the stored procedure here
	@ThoiGian DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT HopDongChiTietID, DanhSachNhanHangREF, CreatedAt, LastModifiedAt FROM ABM_Data_ThucChay.dbo.hopdongchitiet 
	WHERE CONVERT(DATE,LastModifiedAt) >=@ThoiGian
	AND DeletedStatus = 0
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongChiTietID,DanhSachNhanHangREF,CreatedAt, LastModifiedAt FROM HopDongChiTietSyn
	)B
	ON A.HopDongChiTietID =B.HopDongChiTietID
	where A.DanhSachNhanHangREF <> B.DanhSachNhanHangREF
	or A.HopDongChiTietID IS NULL OR B.HopDongChiTietID IS NULL OR A.DanhSachNhanHangREF IS NULL OR B.DanhSachNhanHangREF IS NULL
    ORDER BY A.HopDongChiTietID, B.HopDongChiTietID
END


```
