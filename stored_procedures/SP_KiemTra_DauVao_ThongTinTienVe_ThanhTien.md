# Stored Procedure: `KiemTra_DauVao_ThongTinTienVe_ThanhTien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-22 10:41:32.287000
- **Ngày sửa cuối**: 2016-11-22 10:41:32.287000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[KiemTra_DauVao_ThongTinTienVe_ThanhTien]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT ThongTinTienVeID,GiaTri FROM ABM_Data_ThucChay.dbo.ThongTinTienVe
	)A
	FULL OUTER JOIN 
	(
	SELECT id,giathanhtoan FROM  ThongTinTienVeSyn 
	)B
	ON A.ThongTinTienVeID =B.id
	AND A.GiaTri = B.giathanhtoan
	WHERE A.ThongTinTienVeID IS NULL OR B.id IS NULL
	 OR A.GiaTri IS NULL OR B.giathanhtoan IS NULL
    
END

```
