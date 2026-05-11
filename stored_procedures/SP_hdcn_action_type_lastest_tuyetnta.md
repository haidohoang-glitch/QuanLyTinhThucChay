# Stored Procedure: `hdcn_action_type_lastest_tuyetnta`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-19 17:29:08.810000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.740000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [dbo].[hdcn_action_type_lastest_tuyetnta] '',''
--EXEC [dbo].[hdcn_action_type_lastest_tuyetnta] '2014-05-27'
CREATE PROCEDURE [dbo].[hdcn_action_type_lastest_tuyetnta] 
(
	 @StartDate DATETIME
)	
AS
BEGIN

DECLARE @id_thucchay INT, @id_thucchay1 INT--,@id_thucchay2 INT,@id_thucchay3 INT
DECLARE @dem INT, @dem2 INT
SET @dem = 0
SET @dem2 = 0
--Du lieu <=26/5/2014 đã lấy về đủ
--Chi ap dung voi cac truong hop tu 27/05/2014
IF @StartDate >='2014-05-27'
	BEGIN
		DELETE FROM dbo.hdcn_thucchay_status_tuyetnta  
		WHERE (
				CASE 
					WHEN createddate >= modifieddate or modifieddate is NULL        
					THEN Convert(Date,createddate,101)
					ELSE Convert(Date,modifieddate,101)
				END
			) >='2014-05-27'-- BETWEEN @StartDate AND @EndDate

		-- Lấy dữ liệu từ hdcn_thucchay_pr	có hoặc không có trong bảng hdcn_thucchay_pr_version
		DECLARE Record_Cursor CURSOR FOR 
			SELECT distinct A.id
			FROM hdcn_thucchay_pr_tuyetnta A	
			WHERE (
				CASE 
					WHEN A.createddate >= A.modifieddate or A.modifieddate is NULL        
					THEN Convert(Date,A.createddate,101)
					ELSE Convert(Date,A.modifieddate,101)
				END
			)= @StartDate
			ORDER BY A.id

		OPEN Record_Cursor
		FETCH NEXT FROM Record_Cursor into @id_thucchay		   
		WHILE @@FETCH_STATUS = 0
		BEGIN
			SET @dem = (SELECT COUNT(id) 
						FROM hdcn_thucchay_pr_version_tuyetnta 
						WHERE id_thucchay_pr = @id_thucchay)
			IF @dem > 0 		
				INSERT INTO hdcn_thucchay_status_tuyetnta
					SELECT TOP 1  id_thucchay_pr,action_type, createddate, modifieddate,141, hd_id, phanbosite_id			
					FROM hdcn_thucchay_pr_version_tuyetnta 
					WHERE id_thucchay_pr =@id_thucchay																
					ORDER BY convert(datetime,modifieddate) desc , id DESC
			ELSE
				INSERT INTO hdcn_thucchay_status_tuyetnta
					SELECT TOP 1 id, 1, createddate,modifieddate,141, hd_id, phanbosite_id			
					FROM hdcn_thucchay_pr_tuyetnta
					WHERE id =@id_thucchay
					ORDER BY convert(datetime,modifieddate) desc , id DESC
			SET @dem = 0	 				
		FETCH NEXT FROM Record_Cursor into @id_thucchay			
		END
		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor

		-- Lấy dữ liệu có trong bảng hdcn_thucchay_pr_version nhưng không có trong hdcn_thucchay_pr
		DECLARE Record_Cursor1 CURSOR FOR 
			SELECT DISTINCT A.id_thucchay_pr 
			FROM hdcn_thucchay_pr_version_tuyetnta A 
			WHERE (
			(
				CASE 
					WHEN A.createddate >= A.modifieddate or A.modifieddate is NULL        
					THEN Convert(Date,A.createddate,101)
					ELSE Convert(Date,A.modifieddate,101)
				END
			)=@StartDate
			AND (A.id_thucchay_pr NOT IN (SELECT id FROM hdcn_thucchay_pr_tuyetnta ))
			)	
			ORDER BY A.id_thucchay_pr

		OPEN Record_Cursor1

		FETCH NEXT FROM Record_Cursor1 into @id_thucchay1
		   
		WHILE @@FETCH_STATUS = 0
		BEGIN		
				INSERT INTO hdcn_thucchay_status_tuyetnta
					SELECT TOP 1 id_thucchay_pr, action_type, createddate,modifieddate,141, hd_id, phanbosite_id			
					FROM hdcn_thucchay_pr_version_tuyetnta
					WHERE id_thucchay_pr =@id_thucchay1
					ORDER BY convert(datetime,modifieddate) desc , id DESC
				
		FETCH NEXT FROM Record_Cursor1 into @id_thucchay1
			
		END
		CLOSE Record_Cursor1
		DEALLOCATE Record_Cursor1
	END
	/*
ELSE
	BEGIN
		DECLARE Record_Cursor2 CURSOR FOR 
			SELECT distinct A.id
			FROM hdcn_thucchay_pr_tuyetnta A	
			WHERE (CONVERT(DATE, A.createddate) < @StartDate OR A.createddate IS NULL)
			--WHERE A.id = 10155	
			ORDER BY A.id

		OPEN Record_Cursor2

		FETCH NEXT FROM Record_Cursor2 into @id_thucchay2
		   
		WHILE @@FETCH_STATUS = 0
		BEGIN
			SET @dem2 = (SELECT COUNT(id) 
						FROM hdcn_thucchay_pr_version_tuyetnta 
						WHERE id_thucchay_pr = @id_thucchay2)
			IF @dem2 > 0 		
				INSERT INTO hdcn_thucchay_status_tuyetnta
					SELECT TOP 1  id_thucchay_pr,action_type, createddate, modifieddate,141, hd_id, phanbosite_id			
					FROM hdcn_thucchay_pr_version_tuyetnta 
					WHERE id_thucchay_pr =@id_thucchay2																
					ORDER BY convert(datetime,modifieddate) desc , id DESC
			ELSE
				INSERT INTO hdcn_thucchay_status_tuyetnta
					SELECT TOP 1 id, 1, createddate,modifieddate,141, hd_id, phanbosite_id			
					FROM hdcn_thucchay_pr_tuyetnta
					WHERE id =@id_thucchay2
					ORDER BY convert(datetime,modifieddate) desc , id DESC
			SET @dem2 = 0	 
				
		FETCH NEXT FROM Record_Cursor into @id_thucchay2
			
		END
		CLOSE Record_Cursor2
		DEALLOCATE Record_Cursor2

		-- Lấy dữ liệu có trong bảng hdcn_thucchay_pr_version nhưng không có trong hdcn_thucchay_pr
		DECLARE Record_Cursor2 CURSOR FOR 
			SELECT DISTINCT id_thucchay_pr FROM hdcn_thucchay_pr_version_tuyetnta 
			WHERE thoigianbd >= '2013-01-01' 
			AND (CONVERT(DATE, createddate) < @StartDate OR createddate IS NULL)				
			AND id_thucchay_pr NOT IN (SELECT A.id FROM hdcn_thucchay_pr_tuyetnta A)	
			ORDER BY id_thucchay_pr

		OPEN Record_Cursor3

		FETCH NEXT FROM Record_Cursor1 into @id_thucchay3
		   
		WHILE @@FETCH_STATUS = 0
		BEGIN		
				INSERT INTO hdcn_thucchay_status_tuyetnta
					SELECT TOP 1 id_thucchay_pr, action_type, createddate,modifieddate,141, hd_id, phanbosite_id			
					FROM hdcn_thucchay_pr_version_tuyetnta
					WHERE id_thucchay_pr =@id_thucchay3
					ORDER BY convert(datetime,modifieddate) desc , id DESC
				
		FETCH NEXT FROM Record_Cursor3 into @id_thucchay3			
		END
		CLOSE Record_Cursor3
		DEALLOCATE Record_Cursor3
	END
*/
IF @StartDate = '' 
	SELECT * FROM dbo.hdcn_thucchay_status_tuyetnta 
	WHERE createddate IS NULL 
ELSE	
	SELECT COUNT(A.id_thucchay) FROM dbo.hdcn_thucchay_status_tuyetnta A WHERE (
				CASE 
					WHEN A.createddate >= A.modifieddate or A.modifieddate is NULL        
					THEN Convert(Date,A.createddate,101)
					ELSE Convert(Date,A.modifieddate,101)
				END
			)= @StartDate 
		

END

```
