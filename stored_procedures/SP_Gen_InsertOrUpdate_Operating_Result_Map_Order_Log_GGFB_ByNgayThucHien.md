# Stored Procedure: `Gen_InsertOrUpdate_Operating_Result_Map_Order_Log_GGFB_ByNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-10-24 16:20:51.430000
- **Ngày sửa cuối**: 2025-10-24 16:21:24.617000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_Operating_Result_Map_Order_Log_GGFB_ByNgayThucHien] 	
	@FromDate DATETIME,
	@ToDate DATETIME
As 	
BEGIN

DECLARE @NgayThucHien DATETIME
DECLARE @SQL NVARCHAR(MAX),@server_id nvarchar(100) = '', @database nvarchar(100) = '', @daunhay nvarchar(10) = ''''
, @NgayThucHienNow DATETIME = CONVERT(DATE,GETDATE())--getdate() -- CONVERT(DATE,GETDATE())

SET @server_id =
	ISNULL((SELECT TOP (1) (SERVER_ID) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'GGFB' ORDER BY id),'')

SET @database= 
	ISNULL((SELECT TOP (1) (DATA_NAME) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'GGFB' ORDER BY id),'')

	SET @NgayThucHien = @FromDate 
	SET @NgayThucHienNow =  @ToDate

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
	'SELECT [Id]
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
	--PRINT @SQL
	EXEC(@SQL)

	--XAC DINH TRANG THAI RECORD
	UPDATE t 
	SET    t.[Status_record] = 1
	FROM  #ADS_Operating_Result_Map_Order t 
	INNER JOIN dbo.ADS_Operating_Result_Map_Order_Log dc
			   ON t.Id = dc.ADS_Operating_Result_Map_Order_Id AND t.LastModificationTime = dc.LastModificationTime

	 -- insert row chưa có
	 INSERT INTO [dbo].[ADS_Operating_Result_Map_Order_Log]
           ([ADS_Operating_Result_Map_Order_Id]
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
		   ,[Log_time])
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
		  ,GETDATE()
     FROM #ADS_Operating_Result_Map_Order
	 WHERE Status_record = 0


	DROP TABLE #ADS_Operating_Result_Map_Order

END




```
