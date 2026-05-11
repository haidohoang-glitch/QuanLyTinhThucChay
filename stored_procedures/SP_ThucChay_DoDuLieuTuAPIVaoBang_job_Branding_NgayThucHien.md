# Stored Procedure: `ThucChay_DoDuLieuTuAPIVaoBang_job_Branding_NgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-07-08 16:52:06.497000
- **Ngày sửa cuối**: 2021-07-08 16:54:54.650000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_job_Branding_NgayThucHien] @NgayThucHien = '2021-07-07'
	*/
CREATE PROCEDURE [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_job_Branding_NgayThucHien]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	
	

	DECLARE @ID INT = 0
	DECLARE @JobID INT
	--SET @NgayThucHien = '2018-01-13'
	IF @NgayThucHien IS NULL
			BEGIN
			    SET @NgayThucHien = DATEADD(dd, -1, GETDATE())	

				SET @NgayThucHien = CONVERT(DATE, @NgayThucHien)
			END
	
	DECLARE icursor CURSOR FOR   
		SELECT DISTINCT Id
		FROM RecurringJobs.dbo.JOBS_LOG 
		WHERE CONVERT(DATE, DateExecute) = @NgayThucHien
				AND Status = 1
				AND Id IN (22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 59, 61,74)
		ORDER BY Id
	
	OPEN icursor  
	
	FETCH NEXT FROM icursor   
	INTO @JobID
	
	WHILE @@FETCH_STATUS = 0  
	BEGIN  
		-- Do du lieu cho các sp:
		--		Banner_CPD_by_Contract
		--		BoxApp CPD by Contract
		--		CPM Chuyen trang
		--		Balloon Ads
		--		TVC
		--		Boxapp CPM
		--		Mobile
		--		King Size
		--		CPM Stick
		--		Brand Page
		--		Content Network Sponsorship
		--		Sponsor
		--		Native asd chay theo ngay


		IF @JobID IN (22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 59, 61,74)
			BEGIN
				IF @JobID IN (22,60) --CPD tool cp cu
					BEGIN
						SET @ID = -3
					END
				IF @JobID = 23 -- CPD tool cp cu
					BEGIN
						SET @ID = -2
					END
				IF @JobID = 25
					BEGIN
						SET @ID = 5
					END
				IF @JobID = 26
					BEGIN
						SET @ID = 8
					END
				IF @JobID = 27
					BEGIN
						SET @ID = 9
					END
				IF @JobID = 28
					BEGIN
						SET @ID = 10
					END
				IF @JobID = 29
					BEGIN
						SET @ID = 14
					END
				IF @JobID = 30
					BEGIN
						SET @ID = 15
					END
				IF @JobID = 31
					BEGIN
						SET @ID = 16
					END
				IF @JobID = 32
					BEGIN
						SET @ID = 17
					END
				IF @JobID = 33
					BEGIN
						SET @ID = 18
					END
				IF @JobID = 59
					BEGIN
						SET @ID = 5056
					END
				IF @JobID = 61
					BEGIN
					    SET @ID = 19
					END
				IF @JobID = 74 --CPD tool cp moi
					BEGIN
					    SET @ID = 1
					END
				PRINT 'CPM'
			    EXEC dbo.ThucChay_DoDuLieuTuAPIVaoBang @ID, 1, @NgayThucHien
			END

	    FETCH NEXT FROM icursor   
	    INTO @JobID 
	END   
	CLOSE icursor;  
	DEALLOCATE icursor;  

END


```
