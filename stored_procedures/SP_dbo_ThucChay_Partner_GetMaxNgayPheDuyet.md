# Stored Procedure: `dbo_ThucChay_Partner_GetMaxNgayPheDuyet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-09 11:57:37.323000
- **Ngày sửa cuối**: 2014-11-19 12:16:54.823000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--
-- EXEC dbo_ThucChay_Partner_GetMaxNgayPheDuyet
--
CREATE PROCEDURE [dbo].[dbo_ThucChay_Partner_GetMaxNgayPheDuyet] 
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    SELECT MAX(NgayThucHien) MaxNgayThucHien, 
		dbo.FormatDate(MAX(NgayThucHien)) AS NgayThucHien 
    FROM ThucChayDaTinh
    WHERE 
		IsPheDuyet = 1
END

```
