# Stored Procedure: `GetMaxNgayThucHienByHopDongChiTietAndBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-08 10:06:53.273000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.390000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[GetMaxNgayThucHienByHopDongChiTietAndBanner]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	SELECT MAX(LastModifiedAt)FROM dbo.ThucChayHopDongChiTiet 
END

```
