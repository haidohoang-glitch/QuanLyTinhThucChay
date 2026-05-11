# Stored Procedure: `Gen_InsertOrUpdate_ThucChayMuaNgoaiChot_syn`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-24 15:32:14.933000
- **Ngày sửa cuối**: 2016-11-24 15:32:18.263000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucChayMuaNgoaiChot_syn] 	
As 	
BEGIN
	IF(EXISTS (SELECT * FROM ThucChayMuaNgoaiChotTemp))
	BEGIN
		CREATE TABLE #ThucChayMuaNgoaiChot(
			[ID] [int] NULL,
			[PAYROLL_MONTH] [int] NULL,
			[PAYROLL_YEAR] [int] NULL,
			[CONTRACT_ID] [int] NULL,
			[CONTRACT_DETAIL_ID] [int] NULL,
			[FOMALITY_ID] [int] NULL,
			[FOMALITY_NAME] [nvarchar](200) NULL,
			[PRODUCT_ID] [int] NULL,
			[PRODUCT_NAME] [nvarchar](200) NULL,
			[BANNER_TYPE_ID] [int] NULL,
			[BANNER_NAME] [nvarchar](200) NULL,
			[MONEY_SELL] [float] NULL,
			[MONEY_BUY] [float] NULL,
			[MONEY_PROFIT] [float] NULL,
			[LAST_MODIFIED_AT] [datetime] NULL,
			[LAST_MODIFIED_BY] [nvarchar](200) NULL,
			[DELETED_STATUS] [int] NULL,
			record_status INT
		)



		INSERT INTO #ThucChayMuaNgoaiChot
		SELECT d.*, 0 record_status FROM ThucChayMuaNgoaiChotTemp d
		   -- Set trang thai = 1 doi voi nhung truong hop sua chua 
			UPDATE #ThucChayMuaNgoaiChot
			SET    record_status = 1
			FROM  #ThucChayMuaNgoaiChot t INNER JOIN dbo.ThucChayMuaNgoaiChot dc
			ON t.ID = dc.ID


		-- Update nhung row da ton ton                                      
		UPDATE [dbo].[ThucChayMuaNgoaiChot]
		   SET [PAYROLL_MONTH] = A.PAYROLL_MONTH
			  ,[PAYROLL_YEAR] = A.PAYROLL_YEAR
			  ,[CONTRACT_ID] = A.CONTRACT_ID
			  ,[CONTRACT_DETAIL_ID] = A.CONTRACT_DETAIL_ID
			  ,[FOMALITY_ID] = A.FOMALITY_ID
			  ,[FOMALITY_NAME] = A.FOMALITY_NAME
			  ,[PRODUCT_ID] = A.PRODUCT_ID
			  ,[PRODUCT_NAME] = A.PRODUCT_NAME
			  ,[BANNER_TYPE_ID] = A.BANNER_TYPE_ID
			  ,[BANNER_NAME] = A.BANNER_NAME
			  ,[MONEY_SELL] = A.MONEY_SELL
			  ,[MONEY_BUY] = A.MONEY_BUY
			  ,[MONEY_PROFIT] = A.MONEY_PROFIT
			  ,[LAST_MODIFIED_AT] = A.LAST_MODIFIED_AT
			  ,[LAST_MODIFIED_BY] = A.LAST_MODIFIED_BY
			  ,[DELETED_STATUS] = A.DELETED_STATUS
			FROM   #ThucChayMuaNgoaiChot A 
			WHERE  record_status = 1 
			AND A.ID = [dbo].[ThucChayMuaNgoaiChot].ID

	

			---- Insert Row chua ton tai
			INSERT INTO [dbo].[ThucChayMuaNgoaiChot]
					   ([ID]
					   ,[PAYROLL_MONTH]
					   ,[PAYROLL_YEAR]
					   ,[CONTRACT_ID]
					   ,[CONTRACT_DETAIL_ID]
					   ,[FOMALITY_ID]
					   ,[FOMALITY_NAME]
					   ,[PRODUCT_ID]
					   ,[PRODUCT_NAME]
					   ,[BANNER_TYPE_ID]
					   ,[BANNER_NAME]
					   ,[MONEY_SELL]
					   ,[MONEY_BUY]
					   ,[MONEY_PROFIT]
					   ,[LAST_MODIFIED_AT]
					   ,[LAST_MODIFIED_BY]
					   ,[DELETED_STATUS])
				 SELECT 
					   ID
					   ,PAYROLL_MONTH
					   ,PAYROLL_YEAR
					   ,CONTRACT_ID
					   ,CONTRACT_DETAIL_ID
					   ,FOMALITY_ID
					   ,FOMALITY_NAME
					   ,PRODUCT_ID
					   ,PRODUCT_NAME
					   ,BANNER_TYPE_ID
					   ,BANNER_NAME
					   ,MONEY_SELL
					   ,MONEY_BUY
					   ,MONEY_PROFIT
					   ,LAST_MODIFIED_AT
					   ,LAST_MODIFIED_BY
					   ,DELETED_STATUS
			FROM #ThucChayMuaNgoaiChot dchdct WHERE dchdct.record_status=0
	
	
	END

END

```
