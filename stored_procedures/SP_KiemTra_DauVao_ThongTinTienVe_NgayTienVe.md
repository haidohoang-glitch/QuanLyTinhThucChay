# Stored Procedure: `KiemTra_DauVao_ThongTinTienVe_NgayTienVe`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-22 10:40:56.490000
- **Ngày sửa cuối**: 2016-11-22 10:41:02.837000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[KiemTra_DauVao_ThongTinTienVe_NgayTienVe]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT ThongTinTienVeID,NgayThanhToan FROM ABM_Data_ThucChay.dbo.ThongTinTienVe
	)A
	FULL OUTER JOIN 
	(
	SELECT id,ngaythanhtoan FROM  ThongTinTienVeSyn 
	)B
	ON A.ThongTinTienVeID =B.id
	AND CONVERT (DATE,A.NgayThanhToan) = CONVERT (DATE,B.ngaythanhtoan)
	WHERE A.ThongTinTienVeID IS NULL OR B.id IS NULL
	 OR A.NgayThanhToan IS NULL OR B.ngaythanhtoan IS NULL
    
END

```
