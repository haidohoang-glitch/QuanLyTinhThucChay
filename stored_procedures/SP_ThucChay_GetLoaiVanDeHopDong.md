# Stored Procedure: `ThucChay_GetLoaiVanDeHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-03-16 17:29:36.220000
- **Ngày sửa cuối**: 2017-03-16 17:29:36.220000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		BangDV
-- Create date: 
-- Description:	
-- =============================================
CREATE PROCEDURE dbo.ThucChay_GetLoaiVanDeHopDong 
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT DISTINCT loaivande AS [Name] FROM dbo.CheckThongTinDauVao;
END

```
