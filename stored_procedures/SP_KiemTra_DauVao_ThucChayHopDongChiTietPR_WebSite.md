# Stored Procedure: `KiemTra_DauVao_ThucChayHopDongChiTietPR_WebSite`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-22 11:08:21.893000
- **Ngày sửa cuối**: 2016-11-22 11:08:21.893000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[KiemTra_DauVao_ThucChayHopDongChiTietPR_WebSite]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT ThucChayHopDongChiTietPRID,DmWebsiteREF  FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietPR
	)A
	FULL OUTER JOIN 
	(
	SELECT id , website_id FROM  ThucChayHopDongChiTietPRSyn
	)B
	ON A.ThucChayHopDongChiTietPRID =B.id
	AND A.DmWebsiteREF = B.website_id
	WHERE A.ThucChayHopDongChiTietPRID IS NULL OR B.id IS NULL
	 OR A.DmWebsiteREF IS NULL OR B.website_id IS NULL
    
END

--SELECT * FROM dbo.ThucChayHopDongChiTiet WHERE ThucChayHopDongChiTietID=45689
```
