# Stored Procedure: `GetMaxNgayThucHienByCPD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-08 09:56:14.290000
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
CREATE PROCEDURE [dbo].[GetMaxNgayThucHienByCPD] 
	-- Add the parameters for the stored procedure here
AS
BEGIN
SELECT MAX(NgayThucHien) FROM ThucChayDaTinh
WHERE DmSanPhamREF IN (140,228,241) 

END

```
