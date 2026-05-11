# Stored Procedure: `KiemTra_DauVao_DotChayChiTiet_SoLuong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-22 09:19:11.523000
- **Ngày sửa cuối**: 2016-11-22 09:19:11.523000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[KiemTra_DauVao_DotChayChiTiet_SoLuong]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT DotChayChiTietHopDongChiTietID,SoLuong FROM ABM_Data_ThucChay.dbo.DotChayChiTietHopDongChiTiet
	)A
	FULL OUTER JOIN 
	(
	SELECT id, SoLuong FROM DotChayChiTietHopDongChiTietSyn 
	)B
	ON A.DotChayChiTietHopDongChiTietID =B.id
	AND A.SoLuong =B.SoLuong
	WHERE A.DotChayChiTietHopDongChiTietID IS NULL OR B.id IS NULL OR A.SoLuong IS NULL OR B.SoLuong IS NULL
    
END


```
