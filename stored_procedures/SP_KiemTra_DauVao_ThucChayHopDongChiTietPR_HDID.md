# Stored Procedure: `KiemTra_DauVao_ThucChayHopDongChiTietPR_HDID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-22 11:06:53.947000
- **Ngày sửa cuối**: 2016-11-22 11:06:53.947000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[KiemTra_DauVao_ThucChayHopDongChiTietPR_HDID]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT ThucChayHopDongChiTietPRID,HopDongREF  FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietPR
	)A
	FULL OUTER JOIN 
	(
	SELECT id , hd_id FROM  ThucChayHopDongChiTietPRSyn
	)B
	ON A.ThucChayHopDongChiTietPRID =B.id
	AND A.HopDongREF = B.hd_id
	WHERE A.ThucChayHopDongChiTietPRID IS NULL OR B.id IS NULL
	 OR A.HopDongREF IS NULL OR B.hd_id IS NULL
    
END

--SELECT * FROM dbo.ThucChayHopDongChiTiet WHERE ThucChayHopDongChiTietID=45689
```
