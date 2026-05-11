# Stored Procedure: `KiemTra_DauVao_HopDongChiTiet_HTQC`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-21 17:25:03.790000
- **Ngày sửa cuối**: 2016-11-23 15:17:18.993000

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
 --[KiemTra_DauVao_HopDongChiTiet_HTQC] '2016-01-01'
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDongChiTiet_HTQC]
	-- Add the parameters for the stored procedure here
	@ThoiGian DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT HopDongChiTietID, DmLoaiREF FROM ABM_Data_ThucChay.dbo.hopdongchitiet 
	WHERE CONVERT(DATE,LastModifiedAt) >=@ThoiGian
	AND DeletedStatus = 0
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongChiTietID,DmLoaiREF FROM HopDongChiTietSyn
	)B
	ON A.HopDongChiTietID =B.HopDongChiTietID
	AND A.DmLoaiREF = B.DmLoaiREF
	WHERE A.HopDongChiTietID IS NULL OR B.HopDongChiTietID IS NULL OR A.DmLoaiREF IS NULL OR B.DmLoaiREF IS NULL
    
END

```
