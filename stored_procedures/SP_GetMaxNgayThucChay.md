# Stored Procedure: `GetMaxNgayThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 19:39:16.567000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.753000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[GetMaxNgayThucChay]
	-- Add the parameters for the stored procedure here

AS
BEGIN
	SELECT MAX(NgayThucHien) FROM dbo.ThucChay WHERE DeletedStatus <> 1
END

```
