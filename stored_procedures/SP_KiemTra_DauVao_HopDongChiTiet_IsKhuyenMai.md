# Stored Procedure: `KiemTra_DauVao_HopDongChiTiet_IsKhuyenMai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-21 17:25:31.193000
- **Ngày sửa cuối**: 2016-11-23 15:17:55.977000

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
--EXEC [dbo].[KiemTra_DauVao_HopDongChiTiet_IsKhuyenMai] '2016-01-01'
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDongChiTiet_IsKhuyenMai]
	-- Add the parameters for the stored procedure here
	@ThoiGian DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT HopDongChiTietID, IsKhuyenMai FROM ABM_Data_ThucChay.dbo.hopdongchitiet 
	WHERE CONVERT(DATE,LastModifiedAt) >=@ThoiGian
	AND DeletedStatus = 0
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongChiTietID, IsKhuyenMai FROM HopDongChiTietSyn
	)B
	ON A.HopDongChiTietID =B.HopDongChiTietID
	AND A.IsKhuyenMai = B.IsKhuyenMai
	WHERE A.HopDongChiTietID IS NULL OR B.HopDongChiTietID IS NULL OR A.IsKhuyenMai IS NULL OR B.IsKhuyenMai IS NULL
    
END

```
