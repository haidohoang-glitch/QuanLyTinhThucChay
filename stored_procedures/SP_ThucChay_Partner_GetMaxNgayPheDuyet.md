# Stored Procedure: `ThucChay_Partner_GetMaxNgayPheDuyet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-10 09:59:45.367000
- **Ngày sửa cuối**: 2014-11-19 12:16:55.910000

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
-- EXEC [ThucChay_Partner_GetMaxNgayPheDuyet]
--
CREATE PROCEDURE [dbo].[ThucChay_Partner_GetMaxNgayPheDuyet] 
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
