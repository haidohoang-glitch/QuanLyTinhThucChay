# Stored Procedure: `Gen_InsertOrUpdate_Operating_Result_Map_Order_GGFB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-08-07 10:40:39.457000
- **Ngày sửa cuối**: 2025-10-24 09:54:03.567000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_Operating_Result_Map_Order_GGFB] 	
As 	
BEGIN
 

DECLARE @NgayThucHien DATETIME
DECLARE @SQL NVARCHAR(MAX),@server_id nvarchar(100) = ''
, @database nvarchar(100) = '', @daunhay nvarchar(10) = ''''
, @NgayThucHienNow DATETIME = CONVERT(DATE,GETDATE())--getdate() --CONVERT(DATE,GETDATE())
SET @NgayThucHien = 
	ISNULL((
        SELECT MAX([LastModificationTime])   -- ngày sửa
        FROM   dbo.[ADS_Operating_Result_Map_Order]  
    ),'1900-01-01')

SET @server_id =
	(SELECT TOP (1) (SERVER_ID) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'GGFB' ORDER BY id)

SET @database= 
	(SELECT TOP (1) (DATA_NAME) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'GGFB' ORDER BY id)
SET @NgayThucHien = DATEADD(HOUR,-8,@NgayThucHien)

--SET @NgayThucHien = '2025-10-24'
--set @NgayThucHienNow = '2025-10-25'

CREATE TABLE #ADS_Operating_Result_Map_Order(
	[Id] [int] NOT NULL,
	[Operating_Order_Id] [int] NULL,         -- id order
	[operating_Result_Id] [int] NULL,        -- id result
	[Result] [decimal](18, 4) NULL,           -- kết quả
	[Sell_Money_VND] [decimal](18, 4) NULL,  -- thành tiền bán
	[CreationTime] [datetime2](7) NULL,    
	[CreatedBy] Nvarchar(50) NULL,
	[LastModificationTime] [datetime2](7) NULL,     -- ngày sửa
	[LastModifiedBy] Nvarchar(50) NULL,
	[IsDeleted] [bit] NOT NULL,
	[DeletedBy] Nvarchar(50) NULL,
	[DeletionTime] [datetime2](7) NULL,
	[Status_record] smallint               -- trạng thái insert, update
)

SET @SQL =
'INSERT INTO #ADS_Operating_Result_Map_Order
           (Id
		   ,[Operating_Order_Id]
           ,[operating_Result_Id]
           ,[Result]
           ,[Sell_Money_VND]
           ,[CreationTime]
           ,[CreatedBy]
           ,[LastModificationTime]
           ,[LastModifiedBy]
           ,[IsDeleted]
           ,[DeletedBy]
           ,[DeletionTime]
		   ,[Status_record]) '
SET @SQL +=
	' SELECT [Id]
		  ,[Operating_Order_Id]
		  ,[operating_Result_Id]
		  ,[Result]
		  ,[Sell_Money_VND]
		  ,[CreationTime]
		  ,isnull((SELECT TOP (1) [UserName]
			FROM ' + @server_id + '.' + @database + '.[dbo].[AbpUsers] u WHERE cp.[CreatorUserId] = u.[Id] ORDER BY u.id
			),'''') AS [CreatedBy]
		  ,[LastModificationTime]
		  ,isnull((SELECT TOP (1) [UserName]
			FROM ' + @server_id + '.' + @database + '.[dbo].[AbpUsers] u WHERE cp.[LastModifierUserId] = u.[Id] ORDER BY u.id
			),'''') AS [LastModifiedBy]
		  ,[IsDeleted]
		  ,isnull((SELECT TOP (1) [UserName]
			FROM ' + @server_id + '.' + @database + '.[dbo].[AbpUsers] u WHERE cp.[DeleterUserId] = u.[Id] ORDER BY u.id
			),'''')  AS [DeletedBy]
		  ,[DeletionTime]
		  ,0 AS [Status_record]
	  FROM ' + @server_id + '.' + @database + '.dbo.[Operating_Result_Map_Order] cp
	  WHERE cp.[LastModificationTime] >= ' + @daunhay + convert(nvarchar(23),@ngaythuchien,121)+ @daunhay+' '
	  + ' AND cp.[LastModificationTime] < ' + @daunhay + convert(nvarchar(23),@NgayThucHienNow,121)+ @daunhay+' ' 

	PRINT @SQL
	EXEC(@SQL)
	UPDATE t 
	SET    t.[Status_record] = 1
	FROM  #ADS_Operating_Result_Map_Order t 
	INNER JOIN dbo.ADS_Operating_Result_Map_Order dc
			   ON t.Id = dc.id

	-- Update nhung row da ton ton                                      
	UPDATE D
	   SET
		   D.[Operating_Order_Id] = S.[Operating_Order_Id]
		  ,D.[operating_Result_Id] = S.[operating_Result_Id]
		  ,D.[Result] = S.[Result]
		  ,D.[Sell_Money_VND] = S.[Sell_Money_VND]
		  ,D.[CreationTime] = S.[CreationTime]
		  ,D.[CreatedBy] = S.[CreatedBy]
		  ,D.[LastModificationTime] = S.[LastModificationTime]
		  ,D.[LastModifiedBy] = S.[LastModifiedBy]
		  ,D.[IsDeleted] = S.[IsDeleted]
		  ,D.[DeletedBy] = S.[DeletedBy]
		  ,D.[DeletionTime] = S.[DeletionTime]
	FROM  #ADS_Operating_Result_Map_Order S 
	LEFT JOIN [dbo].[ADS_Operating_Result_Map_Order] D
				ON D.ID = S.ID AND S.[Status_record] =1
	WHERE S.[Status_record] =1

	-- insert row chưa có
	 INSERT INTO [dbo].[ADS_Operating_Result_Map_Order]
           ([Id]
           ,[Operating_Order_Id]
           ,[operating_Result_Id]
           ,[Result]
           ,[Sell_Money_VND]
           ,[CreationTime]
           ,[CreatedBy]
           ,[LastModificationTime]
           ,[LastModifiedBy]
           ,[IsDeleted]
           ,[DeletedBy]
           ,[DeletionTime]
		   ,[IsCaculatedActual] )
     SELECT [Id]
		   ,[Operating_Order_Id]
		   ,[operating_Result_Id]
		   ,[Result]
		   ,[Sell_Money_VND]
		   ,[CreationTime]
		  ,[CreatedBy]
		  ,[LastModificationTime]
		  ,[LastModifiedBy]
		  ,[IsDeleted]
		  ,[DeletedBy]
		  ,[DeletionTime]
		  ,0 as [IsCaculatedActual]
     FROM #ADS_Operating_Result_Map_Order
	 WHERE Status_record = 0

	DROP TABLE #ADS_Operating_Result_Map_Order

END




```
