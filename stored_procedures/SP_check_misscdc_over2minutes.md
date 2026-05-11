# Stored Procedure: `check_misscdc_over2minutes`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-04-28 16:12:41.447000
- **Ngày sửa cuối**: 2021-06-24 14:44:06.670000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--select * 
--from  sys.dm_cdc_log_scan_sessions
--where session_id = 0  --  all sessions since the instance of SQL Server was last started.

CREATE PROCEDURE dbo.check_misscdc_over2minutes
AS
BEGIN
		DECLARE @id int,
				@last_scan datetime2(7),
				@latency decimal(18,2),
				@Max_time datetime2(7),
				@DBName nvarchar(50),
				@SQL_Statement1 nvarchar(1000),
				@SQL_Statement2 nvarchar(1000),
				@Status nvarchar(30),
				@DbCount int 

        CREATE TABLE #OutputTbl 
		( Id int identity(1,1),
		  [DBName] nvarchar(50),
		  [Last Scan] datetime2(7),
		  [Current latency] decimal(18,2),
		  [status] nvarchar(30)
		)

		INSERT INTO #OutputTbl (DBName)
		SELECT [name]
		FROM sys.databases         
		WHERE is_cdc_enabled = 1 

		--INSERT INTO #OutputTbl (DBName)
		--SELECT 'ABM_Data_Release'
	
		SELECT @DbCount  = MAX(id), @Max_time = GETDATE()
		FROM #OutputTbl 

	    SET @id = 1
		WHILE @id <= @DbCount
		BEGIN
		        -- DbName
		        SELECT @DBName = DBName
				FROM #OutputTbl
				WHERE Id = @id

				---- trạng thái cdc và mô tả
				SET @SQL_Statement2 = N' USE {DBNAME}
													 select TOP 1 @last_scanOUT = end_time
													 from  (select top 2 end_time,             
													                     session_id 
													        from sys.dm_cdc_log_scan_sessions
														    order by session_id  desc
														   ) t
													 order by session_id desc    -- if session_id = 0, that  description all session since the current service start

													 select TOP 1 @latencyOUT = latency
													 from  (select top 2 end_time,             -- end time scan session
													                     session_id, 
																		 latency,
																		 last_commit_cdc_time  -- time commit write change data to cdc table of this scan session
													        from sys.dm_cdc_log_scan_sessions
														    order by session_id  desc
														   ) t
													 order by session_id     -- if session_id = 0, that  description all session since the current service start
									   '
				SET @SQL_Statement2 = REPLACE(@SQL_Statement2, '{DBNAME}', @DBName)
				BEGIN TRY  
					EXEC sp_executesql @SQL_Statement2, N'@last_scanOUT datetime2(7) OUTPUT, @latencyOUT decimal(18,2) OUTPUT', @last_scanOUT = @last_scan OUTPUT, @latencyOUT = @latency OUTPUT
					-- cần đưa ra lập luận cho đk này, hiện tại mới chỉ dựa vào biểu hiện của hôm miss log trên asdag/abm_data_release hôm 20210527, miss hơn 1 ngày và thấy như vậy,
					IF DATEDIFF ( MINUTE, @last_scan, @Max_time ) >=  2     
							BEGIN
								SET @Status = N'miss log'           -- unavailable
							END
					ELSE
							IF @latency >= 60
								BEGIN 
									SET @Status = N'Latency is high'
								END
							ELSE
								BEGIN
									SET @Status = N'good'       -- available
								END
					UPDATE b
					SET [Last Scan] = @last_scan, [status] = @Status, [Current latency] = @latency
					FROM #OutputTbl b
					WHERE Id = @id

				END TRY  
				BEGIN CATCH  
					    SET @Status  = N'can not check'                  -- can't check
						UPDATE b
						SET [Last Scan] = NULL, [Current latency] = NULL, [status] = @Status
						FROM #OutputTbl b
						WHERE Id = @id
				END CATCH

				SET @id = @id + 1
		END

		SELECT DBName, [Last Scan], [Current latency], [status]
		FROM #OutputTbl
		WHERE [status] in ( 'miss log', 'Latency is high')

		DROP TABLE #OutputTbl

END

```
