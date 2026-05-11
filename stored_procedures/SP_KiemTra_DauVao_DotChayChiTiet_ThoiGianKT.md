# Stored Procedure: `KiemTra_DauVao_DotChayChiTiet_ThoiGianKT`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-22 09:20:57.607000
- **Ngày sửa cuối**: 2016-11-22 09:20:57.607000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[KiemTra_DauVao_DotChayChiTiet_ThoiGianKT]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT DotChayChiTietHopDongChiTietID,ThoiGianKetThuc FROM ABM_Data_ThucChay.dbo.DotChayChiTietHopDongChiTiet
	)A
	FULL OUTER JOIN 
	(
	SELECT id, ThoigianKT FROM DotChayChiTietHopDongChiTietSyn 
	)B
	ON A.DotChayChiTietHopDongChiTietID =B.id
	AND convert(date,A.ThoiGianKetThuc) = CONVERT(date,B.ThoigianKT)
	WHERE A.DotChayChiTietHopDongChiTietID IS NULL OR B.id IS NULL OR A.ThoiGianKetThuc IS NULL OR B.ThoigianKT IS NULL
    
END


```
