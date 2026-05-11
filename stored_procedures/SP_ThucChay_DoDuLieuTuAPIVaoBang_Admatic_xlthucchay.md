# Stored Procedure: `ThucChay_DoDuLieuTuAPIVaoBang_Admatic_xlthucchay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-07-14 15:11:33.130000
- **Ngày sửa cuối**: 2021-07-14 15:58:06.200000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--exec [ThucChay_TinhPR_BySQLJobs]
CREATE PROCEDURE [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_Admatic_xlthucchay]
	-- Add the parameters for the stored procedure here

AS
BEGIN
	
	

	DECLARE @ID INT = 0
	DECLARE @NgayThucHien DATETIME = NULL
	, @NgayChay DATETIME = '2021-01-01'
	, @EndNgayChay DATETIME = '2021-05-30'
	--SET @NgayThucHien = '2017-09-29'
	
	DECLARE icursor CURSOR FOR   
		SELECT DISTINCT TypeProduct, NgayThucHien
		FROM dbo.DataThucChay_Admatic
		WHERE CONVERT(DATE, NgayThucHien) BETWEEN @NgayChay AND @EndNgayChay
			ORDER BY NgayThucHien, TypeProduct
	
	OPEN icursor  
	
	FETCH NEXT FROM icursor   
	INTO @ID, @NgayThucHien
	
	WHILE @@FETCH_STATUS = 0  
	BEGIN  

		-- Balloon Ads - Admatic
		--TVC Online - Admatic
		--Box App CPM - Admatic
		--Mobile - Admatic
		--King size - Admatic
		--CPM Stick - Admatic
		--Brand Page - Admatic
		--Sponsor Page - Admatic

			EXEC dbo.ThucChay_DoDuLieuTuAPIVaoBang_Admatic @ID, @NgayThucHien
	  	FETCH NEXT FROM icursor   
		INTO @ID, @NgayThucHien
	END   
	CLOSE icursor;  
	DEALLOCATE icursor;  

END


```
