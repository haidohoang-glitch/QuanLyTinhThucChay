# Stored Procedure: `KiemTra_DauVao_ThucChayHopDongChiTietPR_GiaTien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-22 11:06:32.890000
- **Ngày sửa cuối**: 2016-11-22 11:06:32.890000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[KiemTra_DauVao_ThucChayHopDongChiTietPR_GiaTien]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT ThucChayHopDongChiTietPRID,GiaTien  FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietPR
	)A
	FULL OUTER JOIN 
	(
	SELECT id , giatien FROM  ThucChayHopDongChiTietPRSyn
	)B
	ON A.ThucChayHopDongChiTietPRID =B.id
	AND A.GiaTien = B.giatien
	WHERE A.ThucChayHopDongChiTietPRID IS NULL OR B.id IS NULL
	 OR A.GiaTien IS NULL OR B.giatien IS NULL
    
END

--SELECT * FROM dbo.ThucChayHopDongChiTiet WHERE ThucChayHopDongChiTietID=45689
```
