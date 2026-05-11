# Stored Procedure: `ThucChay_AdminBoPhanWebsiteGetAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-20 17:39:10.090000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.790000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
-- dbo.ThucChay_AdminBoPhanWebsiteGetAll
CREATE PROCEDURE [dbo].[ThucChay_AdminBoPhanWebsiteGetAll]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    IF OBJECT_ID('tempdb..#TableResult') IS NOT NULL
		BEGIN
			DROP TABLE #TableResult
		END
			
	CREATE TABLE #TableResult
	(
		ID nvarchar(50),
		TenDangNhap nvarchar(50)
	)

	INSERT INTO #TableResult(ID,TenDangNhap) VALUES('-1',N'-- Nhập tên đăng nhập --')

	INSERT INTO #TableResult
	SELECT DISTINCT
		TenDangNhap AS ID,
		TenDangNhap 
	FROM AdminBoPhanWebsite
	ORDER BY TenDangNhap

	SELECT ID,TenDangNhap FROM #TableResult
END

```
