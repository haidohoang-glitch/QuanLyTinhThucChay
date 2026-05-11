# Stored Procedure: `KiemTra_DauVao_DotChayChiTiet_ThoiGianBD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-22 09:19:55.937000
- **Ngày sửa cuối**: 2016-11-22 09:19:55.937000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[KiemTra_DauVao_DotChayChiTiet_ThoiGianBD]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT DotChayChiTietHopDongChiTietID,ThoiGianBatDau FROM ABM_Data_ThucChay.dbo.DotChayChiTietHopDongChiTiet
	)A
	FULL OUTER JOIN 
	(
	SELECT id, ThoigianBD FROM DotChayChiTietHopDongChiTietSyn 
	)B
	ON A.DotChayChiTietHopDongChiTietID =B.id
	AND convert(date,A.ThoiGianBatDau) = CONVERT(date,B.ThoigianBD)
	WHERE A.DotChayChiTietHopDongChiTietID IS NULL OR B.id IS NULL OR A.ThoiGianBatDau IS NULL OR B.ThoigianBD IS NULL
    
END


```
