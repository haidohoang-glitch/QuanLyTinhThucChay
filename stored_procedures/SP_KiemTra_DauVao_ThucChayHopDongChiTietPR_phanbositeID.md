# Stored Procedure: `KiemTra_DauVao_ThucChayHopDongChiTietPR_phanbositeID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-22 11:07:38.550000
- **Ngày sửa cuối**: 2016-11-22 11:07:38.550000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[KiemTra_DauVao_ThucChayHopDongChiTietPR_phanbositeID]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT ThucChayHopDongChiTietPRID,HopDongChiTietREF  FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietPR
	)A
	FULL OUTER JOIN 
	(
	SELECT id , phanbosite_id FROM  ThucChayHopDongChiTietPRSyn
	)B
	ON A.ThucChayHopDongChiTietPRID =B.id
	AND A.HopDongChiTietREF = B.phanbosite_id
	WHERE A.ThucChayHopDongChiTietPRID IS NULL OR B.id IS NULL
	 OR A.HopDongChiTietREF IS NULL OR B.phanbosite_id IS NULL
    
END

--SELECT * FROM dbo.ThucChayHopDongChiTiet WHERE ThucChayHopDongChiTietID=45689
```
