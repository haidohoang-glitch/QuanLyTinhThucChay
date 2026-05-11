# Stored Procedure: `GetMaxNgayThucHienByCPM`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-08 10:09:44.600000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.750000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[GetMaxNgayThucHienByCPM] 
	-- Add the parameters for the stored procedure here
AS
BEGIN
	SELECT MAX(NgayThucHien) FROM ThucChayDaTinh
	WHERE DmSanPhamREF IN (231,238,339,342,337,240,370)
END

```
