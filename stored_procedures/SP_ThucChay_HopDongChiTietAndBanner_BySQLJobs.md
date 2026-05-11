# Stored Procedure: `ThucChay_HopDongChiTietAndBanner_BySQLJobs`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-02 14:08:22.730000
- **Ngày sửa cuối**: 2014-11-19 12:16:58.493000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_HopDongChiTietAndBanner_BySQLJobs]
	-- Add the parameters for the stored procedure here

AS
BEGIN
	DECLARE @dtEnd DATETIME
	
	--SET @dtEnd = GETDATE()
	--SET @dtEnd = DATEADD(dd,-1, @dtEnd)
	
	SET @dtEnd = (SELECT MAX(LastModifiedAt) FROM dbo.ThucChayHopDongChiTietAndBanner)
	
	IF(@dtEnd IS NULL)
		SET @dtEnd = (SELECT MAX(CreatedAt) FROM dbo.ThucChayHopDongChiTietAndBanner)
		
	--Tinh HopDongChiTietAndBanner - Thuc Chay CPM
	EXEC [dbo].[ThucChay_HopDongChiTietAndBanner] @dtEnd

	
END

```
