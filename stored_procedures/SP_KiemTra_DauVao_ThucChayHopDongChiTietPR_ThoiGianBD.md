# Stored Procedure: `KiemTra_DauVao_ThucChayHopDongChiTietPR_ThoiGianBD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-22 11:08:01.627000
- **Ngày sửa cuối**: 2016-11-22 11:08:01.627000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[KiemTra_DauVao_ThucChayHopDongChiTietPR_ThoiGianBD]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT ThucChayHopDongChiTietPRID,ThoiGianBatDau  FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietPR
	)A
	FULL OUTER JOIN 
	(
	SELECT id ,  thoigianbd FROM  ThucChayHopDongChiTietPRSyn
	)B
	ON A.ThucChayHopDongChiTietPRID =B.id
	AND CONVERT(DATE, A.ThoiGianBatDau) = CONVERT (DATE,B.thoigianbd)
	WHERE A.ThucChayHopDongChiTietPRID IS NULL OR B.id IS NULL
	 OR A.ThoiGianBatDau IS NULL OR B.thoigianbd IS NULL
    
END

--SELECT * FROM dbo.ThucChayHopDongChiTiet WHERE ThucChayHopDongChiTietID=45689
```
