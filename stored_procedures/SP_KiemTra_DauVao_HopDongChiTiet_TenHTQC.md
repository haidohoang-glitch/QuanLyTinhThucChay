# Stored Procedure: `KiemTra_DauVao_HopDongChiTiet_TenHTQC`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-21 17:27:24.690000
- **Ngày sửa cuối**: 2016-11-23 16:19:37.037000

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
--EXEC  [dbo].[KiemTra_DauVao_HopDongChiTiet_TenHTQC] '2016-01-01'
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDongChiTiet_TenHTQC]
	-- Add the parameters for the stored procedure here
	@ThoiGian DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT HopDongChiTietID, TenLoai TenHTQC,CreatedAt, LastModifiedAt FROM ABM_Data_ThucChay.dbo.hopdongchitiet 
	WHERE CONVERT(DATE,LastModifiedAt) >=@ThoiGian
	AND DeletedStatus = 0
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongChiTietID,TenLoai TenHTQC,CreatedAt, LastModifiedAt FROM HopDongChiTietSyn
	)B
	ON A.HopDongChiTietID =B.HopDongChiTietID
	where A.TenHTQC <> B.TenHTQC
	or A.HopDongChiTietID IS NULL OR B.HopDongChiTietID IS NULL OR A.TenHTQC IS NULL OR B.TenHTQC IS NULL    
END

```
