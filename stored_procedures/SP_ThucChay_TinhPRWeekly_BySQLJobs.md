# Stored Procedure: `ThucChay_TinhPRWeekly_BySQLJobs`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-10-10 08:54:15.897000
- **Ngày sửa cuối**: 2014-11-19 12:24:53.907000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[ThucChay_TinhPRWeekly_BySQLJobs]
	-- Add the parameters for the stored procedure here

AS
BEGIN
	DECLARE @dtStart DATETIME, @dtEnd DATETIME
	
	SET @dtStart = (
					SELECT MAX(NgayThucHien) FROM dbo.ThucChayDaTinh
						WHERE DmSanPhamREF IN (141,245,250)
						--Website noi bo
						--AND DmWebsiteREF NOT IN (
						
						--			SELECT DmWebsiteReportingdbID FROM dbo.DmWebsiteReportingdb 
						--			WHERE 
						--			LOWER(TenWebsite) LIKE '%afamily%'
						--			or 
						--			LOWER(TenWebsite) LIKE '%cafef%'
						--			or 
						--			LOWER(TenWebsite) LIKE '%dantri%'
						--			or 
						--			LOWER(TenWebsite) LIKE '%gamek%'
						--			or 
						--			LOWER(TenWebsite) LIKE '%genk%'
						--			or 
						--			LOWER(TenWebsite) LIKE '%giadinh%'
						--			or 
						--			LOWER(TenWebsite) LIKE '%kenh14%'
						--			or 
						--			LOWER(TenWebsite) LIKE '%skds%'
						--			or 
						--			LOWER(TenWebsite) LIKE '%phapluattp%'
						--			or 
						--			LOWER(TenWebsite) LIKE '%soha%'
						--			or 
						--			LOWER(TenWebsite) LIKE '%vneconomy%'
						--					)
					)
	
	SET @dtEnd = GETDATE()
	SET @dtEnd = DATEADD(dd,-1, @dtEnd)	
	--Tinh Thuc Chay PR
	SET @dtStart = DATEADD(dd,-6, @dtEnd)
	EXEC [ThucChay_InsertThucChayDaTinh_PR] @dtStart,@dtEnd
	

END







```
