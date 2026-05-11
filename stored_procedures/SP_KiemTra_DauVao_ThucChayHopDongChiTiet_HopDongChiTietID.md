# Stored Procedure: `KiemTra_DauVao_ThucChayHopDongChiTiet_HopDongChiTietID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-22 10:54:58.763000
- **Ngày sửa cuối**: 2016-11-22 10:54:58.763000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[KiemTra_DauVao_ThucChayHopDongChiTiet_HopDongChiTietID]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT ThucChayHopDongChiTietID, HopDongChiTietREF FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet
	)A
	FULL OUTER JOIN 
	(
	SELECT id ,phanbosite_id FROM  ThucChayHopDongChiTietSyn
	)B
	ON A.ThucChayHopDongChiTietID =B.id
	AND A.HopDongChiTietREF = B.phanbosite_id
	WHERE A.ThucChayHopDongChiTietID IS NULL OR B.id IS NULL
	 OR A.HopDongChiTietREF IS NULL OR B.phanbosite_id IS NULL
    
END

```
