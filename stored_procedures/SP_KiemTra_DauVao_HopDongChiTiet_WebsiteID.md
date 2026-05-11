# Stored Procedure: `KiemTra_DauVao_HopDongChiTiet_WebsiteID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-21 17:31:29.127000
- **Ngày sửa cuối**: 2016-11-23 16:14:50.117000

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
--EXEC  [dbo].[KiemTra_DauVao_HopDongChiTiet_WebsiteID] '2016-01-01'
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDongChiTiet_WebsiteID]
	-- Add the parameters for the stored procedure here
	@ThoiGian DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT HopDongChiTietID, DmWebsiteREF,CreatedAt, LastModifiedAt FROM ABM_Data_ThucChay.dbo.hopdongchitiet 
	WHERE CONVERT(DATE,LastModifiedAt) >=@ThoiGian
	AND DeletedStatus = 0
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongChiTietID, DmWebsiteREF,CreatedAt, LastModifiedAt FROM HopDongChiTietSyn
	)B
	ON A.HopDongChiTietID =B.HopDongChiTietID
	where A.DmWebsiteREF <> B.DmWebsiteREF
	or A.HopDongChiTietID IS NULL OR B.HopDongChiTietID IS NULL OR A.DmWebsiteREF IS NULL OR B.DmWebsiteREF IS NULL
    
END

```
