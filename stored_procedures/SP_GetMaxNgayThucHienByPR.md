# Stored Procedure: `GetMaxNgayThucHienByPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-08 10:00:19.337000
- **Ngày sửa cuối**: 2014-11-19 12:17:54.960000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[GetMaxNgayThucHienByPR]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	SELECT MAX(NgayThucHien)FROM dbo.ThucChayDaTinh 
	WHERE DmSanPhamREF IN (141,245,250)
END

```
