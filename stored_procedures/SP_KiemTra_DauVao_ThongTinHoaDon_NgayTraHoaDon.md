# Stored Procedure: `KiemTra_DauVao_ThongTinHoaDon_NgayTraHoaDon`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-22 10:48:13.253000
- **Ngày sửa cuối**: 2016-11-22 10:48:13.253000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[KiemTra_DauVao_ThongTinHoaDon_NgayTraHoaDon]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT ThongTinHoaDonID, NgayTraHoaDon FROM ABM_Data_ThucChay.dbo.ThongTinHoaDon
	)A
	FULL OUTER JOIN 
	(
	SELECT id ,ngaytrahoadon FROM  ThongTinHoaDonSyn 
	)B
	ON A.ThongTinHoaDonID =B.id
	AND CONVERT (DATE,A.NgayTraHoaDon) = CONVERT(DATE,B.ngaytrahoadon)
	WHERE A.ThongTinHoaDonID IS NULL OR B.id IS NULL
	 OR A.NgayTraHoaDon IS NULL OR B.ngaytrahoadon IS NULL
    
END

```
