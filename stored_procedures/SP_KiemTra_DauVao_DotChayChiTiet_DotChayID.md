# Stored Procedure: `KiemTra_DauVao_DotChayChiTiet_DotChayID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-22 09:18:39.310000
- **Ngày sửa cuối**: 2016-11-22 09:18:39.310000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[KiemTra_DauVao_DotChayChiTiet_DotChayID]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT DotChayChiTietHopDongChiTietID,DotChayHopDongChitietREF FROM ABM_Data_ThucChay.dbo.DotChayChiTietHopDongChiTiet
	)A
	FULL OUTER JOIN 
	(
	SELECT id, DotChayID FROM DotChayChiTietHopDongChiTietSyn 
	)B
	ON A.DotChayChiTietHopDongChiTietID =B.id
	AND A.DotChayHopDongChitietREF = B.DotChayID
	WHERE A.DotChayChiTietHopDongChiTietID IS NULL OR B.id IS NULL OR A.DotChayHopDongChitietREF IS NULL OR B.DotChayID IS NULL
    
END

```
