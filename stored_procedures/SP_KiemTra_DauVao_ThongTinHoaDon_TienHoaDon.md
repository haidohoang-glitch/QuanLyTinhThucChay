# Stored Procedure: `KiemTra_DauVao_ThongTinHoaDon_TienHoaDon`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-22 10:48:45.297000
- **Ngày sửa cuối**: 2016-11-22 10:48:45.297000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[KiemTra_DauVao_ThongTinHoaDon_TienHoaDon]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT ThongTinHoaDonID, GiaTri FROM ABM_Data_ThucChay.dbo.ThongTinHoaDon
	)A
	FULL OUTER JOIN 
	(
	SELECT id ,giatri FROM  ThongTinHoaDonSyn 
	)B
	ON A.ThongTinHoaDonID =B.id
	AND A.GiaTri = B.giatri
	WHERE A.ThongTinHoaDonID IS NULL OR B.id IS NULL
	 OR A.GiaTri IS NULL OR B.giatri IS NULL
    
END

```
