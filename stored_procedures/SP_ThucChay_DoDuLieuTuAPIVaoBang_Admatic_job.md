# Stored Procedure: `ThucChay_DoDuLieuTuAPIVaoBang_Admatic_job`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-11-22 10:40:48.927000
- **Ngày sửa cuối**: 2018-01-13 08:27:03.153000

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
CREATE PROCEDURE [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_Admatic_job]
	-- Add the parameters for the stored procedure here

AS
BEGIN
	
	

	DECLARE @ID INT = 0
	DECLARE @JobID INT
	DECLARE @NgayThucHien DATETIME = NULL
	--SET @NgayThucHien = '2017-09-29'
	
	DECLARE icursor CURSOR FOR   
		SELECT DISTINCT Id
		FROM RecurringJobs.dbo.JOBS_LOG 
		WHERE CONVERT(DATE, DateExecute) = CONVERT(DATE, GETDATE())
				AND Status = 1
				AND Id IN (45, 46, 47, 48, 49, 50, 51, 52)
		ORDER BY Id
	
	OPEN icursor  
	
	FETCH NEXT FROM icursor   
	INTO @JobID
	
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


		IF @JobID IN (45, 46, 47, 48, 49, 50, 51, 52)
			BEGIN
				IF @JobID = 45
					BEGIN
						SET @ID = 5
					END
				IF @JobID = 46
					BEGIN
						SET @ID = 8
					END
				IF @JobID = 47
					BEGIN
						SET @ID = 9
					END
				IF @JobID = 48
					BEGIN
						SET @ID = 10
					END
				IF @JobID = 49
					BEGIN
						SET @ID = 14
					END
				IF @JobID = 50
					BEGIN
						SET @ID = 15
					END
				IF @JobID = 51
					BEGIN
						SET @ID = 16
					END
				IF @JobID = 52
					BEGIN
						SET @ID = 18
					END
				

			    EXEC dbo.ThucChay_DoDuLieuTuAPIVaoBang_Admatic @ID, @NgayThucHien
			END


		
		 
	    FETCH NEXT FROM icursor   
	    INTO @JobID 
	END   
	CLOSE icursor;  
	DEALLOCATE icursor;  

END


```
