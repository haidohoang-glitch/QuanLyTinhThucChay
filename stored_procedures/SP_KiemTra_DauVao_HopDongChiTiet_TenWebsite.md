# Stored Procedure: `KiemTra_DauVao_HopDongChiTiet_TenWebsite`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-21 17:28:31.590000
- **Ngày sửa cuối**: 2016-11-23 15:58:39.067000

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
--EXeC [dbo].[KiemTra_DauVao_HopDongChiTiet_TenWebsite] '2016-01-01'
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDongChiTiet_TenWebsite]
	-- Add the parameters for the stored procedure here
		@ThoiGian DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT HopDongFK, HopDongChiTietID, DmWebsiteREF, TenWebsite,CreatedAt, LastModifiedAt FROM ABM_Data_ThucChay.dbo.hopdongchitiet 
	WHERE CONVERT(DATE,LastModifiedAt) >=@ThoiGian
	AND DeletedStatus = 0
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongFK, HopDongChiTietID,DmWebsiteREF, TenWebSite FROM HopDongChiTietSyn
	)B
	ON A.HopDongChiTietID =B.HopDongChiTietID
	where A.TenWebsite <> LTRIM(RTRIM(B.TenWebSite))
	or A.HopDongChiTietID IS NULL OR B.HopDongChiTietID IS NULL OR A.TenWebsite IS NULL OR B.TenWebSite IS NULL
    ORDER BY A.HopDongChiTietID
END

```
