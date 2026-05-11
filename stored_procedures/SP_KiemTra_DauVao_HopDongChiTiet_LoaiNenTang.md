# Stored Procedure: `KiemTra_DauVao_HopDongChiTiet_LoaiNenTang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-21 17:26:16.490000
- **Ngày sửa cuối**: 2016-11-23 15:22:46.040000

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
--EXeC [dbo].[KiemTra_DauVao_HopDongChiTiet_LoaiNenTang]
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDongChiTiet_LoaiNenTang]
	-- Add the parameters for the stored procedure here
	@ThoiGian DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT HopDongChiTietID, DmloaiNenTangREF,CreatedAt,LastModifiedAt FROM ABM_Data_ThucChay.dbo.hopdongchitiet 
	WHERE CONVERT(DATE,LastModifiedAt) >=@ThoiGian
	AND DeletedStatus = 0
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongChiTietID, DmloaiNenTangREF,CreatedAt,LastModifiedAt FROM HopDongChiTietSyn
	)B
	ON A.HopDongChiTietID =B.HopDongChiTietID
	AND A.DmloaiNenTangREF = B.DmloaiNenTangREF
	WHERE A.HopDongChiTietID IS NULL OR B.HopDongChiTietID IS NULL OR A.DmloaiNenTangREF IS NULL OR B.DmloaiNenTangREF IS NULL
    
END

```
