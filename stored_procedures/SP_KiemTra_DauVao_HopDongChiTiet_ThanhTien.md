# Stored Procedure: `KiemTra_DauVao_HopDongChiTiet_ThanhTien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-21 17:28:52.270000
- **Ngày sửa cuối**: 2016-11-23 11:34:01.263000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [dbo].[KiemTra_DauVao_HopDongChiTiet_ThanhTien]
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDongChiTiet_ThanhTien]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT HopDongChiTietID, ThanhTien FROM ABM_Data_ThucChay.dbo.hopdongchitiet 
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongChiTietID, ThanhTien FROM HopDongChiTietSyn
	)B
	ON A.HopDongChiTietID =B.HopDongChiTietID
	AND A.ThanhTien = B.ThanhTien
	WHERE A.HopDongChiTietID IS NULL OR B.HopDongChiTietID IS NULL OR A.ThanhTien IS NULL OR B.ThanhTien IS NULL
    
END

```
